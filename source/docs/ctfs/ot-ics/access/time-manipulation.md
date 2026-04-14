# Runbook: NTP time manipulation

`guild-clock` provides NTP to the DMZ with no authentication. Any host that
reaches UDP port 123 can query the server and, with an on-path position, forge
NTP responses to shift a client's clock. The attack is not destructive on its
own: it is a precondition. A shifted clock on a DMZ host breaks TLS certificate
validity windows, corrupts log timestamps, and makes replay-protection intervals
exploitable. It is the kind of attack that makes the post-incident investigation
significantly harder without anyone noticing until the forensics team tries to
correlate event sequences.

- Techniques: 
  - [Trust exploitation and misconfiguration](https://purple.tymyrddin.dev/docs/ctfs/ot-ics/attack-surface#trust-exploitation-and-misconfiguration-abuse)
  - [Data integrity manipulation](https://purple.tymyrddin.dev/docs/ctfs/ot-ics/attack-surface#data-integrity-manipulation)
- Challenge type: Network (PCAP) or Forensic
- Difficulty: Intermediate

## Components to start

```bash
./ctl up
```

Minimal containers: `guild-clock`, `unseen-gate`

To demonstrate the downstream effects of a clock shift, add any DMZ container that
performs TLS or certificate validation and uses this NTP server (e.g. `contractors-gate`
or `sorting-office`). To observe log timestamp corruption, `scribes-post` collects
syslog from several DMZ hosts.

Entry point: any host with a route to `guild-clock` (10.10.5.30, UDP 123).
The internet zone has direct access.

## Background

`guild-clock` runs `cturra/ntp`, pinned by digest. NTP symmetric key
authentication is not configured. `ntpq` and `ntpdc` queries are open to any
source. The server is reachable from the internet zone, so the DMZ components
that use it for time synchronisation are relying on an NTP source that any
internet-adjacent host can query and attempt to influence.

NTP manipulation in OT environments has three practical consequences:

1. TLS certificates have notBefore/notAfter fields. A clock shifted by more
   than the certificate's validity window causes connection failures, or makes
   an expired certificate appear valid.
2. Process historians and SCADA systems timestamp every event. A clock shift
   corrupts the sequence-of-events record. Alarms, trips, and operator actions
   become reordered or attributed to the wrong time.
3. Protective relays use timestamps for event logging and some protection
   schemes use time-synchronised phasors. Manipulated time affects post-event
   analysis even if protection logic itself is not disrupted.

## Attack path

### Stage 1: enumerate the NTP server

```bash
# Query the peer list: reveals the server's upstream time sources
ntpq -p 10.10.5.30
# remote           refid      st t when poll reach   delay   offset  jitter
# *time.cloudflare .INIT.     2 u   48   64  377     5.124   -0.233   0.118

# Query time offset without changing the local clock
ntpdate -q 10.10.5.30
# server 10.10.5.30, stratum 2, offset -0.003271, delay 0.02726

# Confirm no authentication mode is configured
ntpq -c "rv" 10.10.5.30
# Look for "authseqno": absent or zero means no auth
```

### Stage 2: identify clients of this NTP server

```bash
# From within the DMZ (e.g. after compromising contractors-gate):
# Check which hosts have NTP configured to use guild-clock
# On Debian/Ubuntu systems:
cat /etc/ntpsec/ntp.conf | grep server
# or
cat /etc/chrony/chrony.conf | grep server
# Look for 10.10.5.30 entries
```

### Stage 3: forge NTP responses (on-path)

NTP operates over UDP. A forged response only needs to match the client's
source port and query transaction ID, both of which are observable on the wire.
An on-path attacker can substitute the server's response with a crafted one.

```python
# Illustrative: custom NTP response forger using scapy
# Requires on-path position (e.g. ARP poisoning or network tap on DMZ segment)
from scapy.all import *
import struct, time

def forge_ntp_response(pkt):
    if pkt.haslayer(NTPHeader) and pkt[NTPHeader].mode == 3:  # client mode
        # Build a response with manipulated transmit timestamp
        # offset: shift time by 3 hours forward
        fake_time = time.time() + 10800
        # ... build and send crafted NTP response packet
        pass

sniff(filter="udp port 123", prn=forge_ntp_response, store=0)
```

The `ntpdate` tool in step-mode can also force a time change on a target host
if the attacker controls the NTP server or its responses:
```bash
# On target host (if attacker controls what it sees on UDP 123):
ntpdate -b 10.10.5.30
# -b forces an immediate step rather than gradual slew
```

### Stage 4: observe the consequences

```bash
# On a DMZ host whose clock has been shifted forward by 3 hours:

# TLS connections to services with recently-renewed certificates fail
curl https://some-internal-service/
# SSL certificate not yet valid (notBefore is in the future from the real clock's
# perspective, but future from the shifted clock's perspective means expired)

# SSH host key certificates with validity periods are rejected
# Kerberos tickets (5-minute window) are rejected immediately

# Log timestamps diverge from event reality:
tail /var/log/syslog
# Timestamps 3 hours ahead of actual events
# Correlating with historian logs or firewall logs becomes an exercise in
# figuring out which clock was lying
```

## Flag placement

For a Forensic challenge: provide a PCAP and a set of log files from two
different hosts. One host's clock has been shifted. The timestamps in the logs
are inconsistent. The participant identifies the shifted host, determines the
offset, and recovers the correct event sequence. The flag is embedded in a log
entry that only makes sense when the timestamps are corrected.

For a Network challenge: the PCAP contains forged NTP responses. The participant
identifies the injected packets by comparing the server's stated reference
timestamp against the legitimate peer list, and extracts a value from the
crafted response that encodes the flag.

## Time in OT incident response

The sequence-of-events recorder is the first thing an OT incident response team
reaches for. Every historian, relay event recorder, and SCADA alarm log depends
on the clock. A manipulation that corrupts timestamps by hours does not prevent
the logs from existing; it makes them unreliable as evidence. The attacker who
trips the turbine and manipulates the clock does not erase the record, they make
it ambiguous. That is often enough.

NTP authentication (symmetric key or autokey) is the correct mitigation and is
straightforward to configure. It is not configured here because it requires
distributing keys to every NTP client, which in an OT environment means touching
every PLC, historian, and relay IED. That coordination tends to be deferred
indefinitely.
