# Network and Forensic challenges

Network and Forensic challenges are standalone artefacts: a PCAP file, a minimal service,
or both. They do not require the full ics-simlab environment. The three runbooks in
[runbooks/](runbooks/index.rst) cover a ready beginner, intermediate, and intermediate
challenge respectively: meter Modbus read, IED relay force-trip, and historian path traversal.
Each runbook is the concrete reference; this workflow is the framing around it.

## Phase 1: Define the challenge

Select one technique from [attack-surface.md](../attack-surface.md) and one specific mechanic.
One challenge, one technique. Decide the flag location before designing anything else.

The meter Modbus read challenge targets technique 2: the flag lives in input register `IR[4]`,
present in the capture from the first read. The IED relay challenge targets technique 1: the
flag appears in holding registers only after the force-trip write, teaching that the consequence
matters as much as the command. The historian path traversal targets technique 3: the flag is
a row in the credentials table, reachable only by downloading and querying the full database.

Identify which ics-simlab component produces the relevant traffic:

* Protocol enumeration and register reads: turbine PLC, IED relays, meter
* Credential and data exfiltration: historian, SCADA server, legacy workstation
* Lateral movement and pivot: engineering workstation, enterprise workstation

The [challenge inventory](resources.md) maps each technique to the relevant component,
difficulty, and status.

## Phase 2: Select the component scope

Start only the components required. The meter challenge needs the meter and turbine PLC
(meter values derive from the PLC physics engine). The relay challenge needs the relay, PLC,
and breaker actuator. The historian challenge needs the historian alone.

```
# Meter challenge
docker compose -f zones/control/docker-compose.yml up -d uupl-meter uupl-turbine-plc

# Relay challenge
docker compose -f zones/control/docker-compose.yml up -d uupl-relay-a uupl-turbine-plc uupl-breaker-a

# Historian challenge
docker compose -f zones/operational/docker-compose.yml up -d uupl-historian
```

See [environment.md](environment.md) for the full `make` workflow.

## Phase 3: Build the minimal scenario

Run the full attack path manually and confirm the traffic is unambiguous. Fix any register
values or database contents that change between restarts; the flag needs to appear in the same
place every time.

For the historian challenge: confirm that the SQLite database is initialised with the same
schema and flag row on every container start. The flag row is part of the Dockerfile or
the database init script, not a runtime write.

Remove or disable any services or endpoints that are not part of the attack path. An open
port that shortcuts the intended technique becomes the solution.

## Phase 4: Generate artefacts

Capture traffic with `tcpdump` during exploitation. Start the capture before the first
packet and stop after the flag is retrieved.

```
tcpdump -i any -w challenge.pcap port 502     # Modbus challenges
tcpdump -i any -w challenge.pcap port 8080    # HTTP challenges
```

For the relay challenge, the PCAP captures the full sequence: initial coil read (both False),
write coil 0 = True, confirmation, second coil read (both True), holding register read with
flag now present. The sequence tells the story without any annotation.

For the historian challenge, the PCAP captures the GET request with the traversal payload and
the binary SQLite response. A Forensic variant provides only the PCAP; the participant
reassembles the database from the HTTP response body.

Confirm the flag appears exactly once in the capture and is not visible from a partial read
or an earlier request.

## Phase 5: Write documentation

README (for participants):
* Objective: one sentence stating what to find
* Scenario: enough context to understand what the device or service represents
* No hints about the path

Solution (for Root-Me reviewers):
* Exact commands and expected outputs
* Where the flag is and what produces it
* One real-world reference: the CVE, the advisory, the incident

The historian challenge references ICS-CERT Advisory ICSA-19-274-01. The relay challenge
references CVE-2022-3084 (GE Reason RT430). These are not decorative; they are the reason
the challenge exists.

## Phase 6: Package and verify

```
zip -r challenge.zip artefact/ README.txt solution.txt
```

Extract on a clean system, follow the README exactly, confirm the solution still works.
A challenge that passes on the build machine and fails on a clean system is not ready.

## Phase 7: Submit and iterate

Submit a small batch first. Reviewer feedback on two or three challenges is more useful
than polishing ten in isolation. Patterns in reviewer notes are the most reliable signal
for what the next batch needs.
