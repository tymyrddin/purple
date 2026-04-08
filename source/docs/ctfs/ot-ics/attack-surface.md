# OT/ICS attack surface reference (technique-based)

This layer abstracts protocol specifics into attacker techniques. Each technique can be implemented via one
or more protocols in the simulation environments. If a technique is not represented here, it is either out
of scope or not supported by the current lab stack.

The protocol reference (Modbus, DNP3, IEC-104, OPC UA, S7, MQTT) remains the toolbox. This is the playbook.

Where a technique has no confirmed real-world incident, this is noted. Theoretically validated means
peer-reviewed research has established the method is sound; it does not mean it has been deployed against
live infrastructure.

## 1. Unauthorised state manipulation

Change the physical process by issuing control commands.

What it looks like:

* Flip coils, write registers, operate breakers, toggle actuators
* Start or stop PLC execution
* Override setpoints (temperature, pressure, flow)

Protocols involved:

* Modbus (writes)
* DNP3 (CROB)
* IEC-104 (single/double commands)
* S7 (DB writes, CPU control)
* OPC UA (write nodes)

Design angle: The write itself is dull. The consequence is where things get interesting. Does the pump
cavitate, does the grid destabilise, does the safety system trip?

## 2. Process intelligence gathering

Build an internal model of the system before touching it.

What it looks like:

* Enumerate registers, nodes, data points
* Map relationships between sensors and actuators
* Identify safety limits and control loops
* Passively observe process behaviour over time
* Subscribe to MQTT topic `#` to receive every message on the broker without credentials

Protocols involved:

* OPC UA (namespace browsing)
* Modbus (read functions)
* DNP3 and IEC-104 (interrogation, unsolicited responses)
* MQTT (wildcard topic subscription)

Design angle: Good attackers do this first. Good challenges reward patience here instead of rushing to
"press the red button". The MQTT wildcard is an underappreciated intelligence vector in environments that
use it for sensor telemetry: one command and every reading on the broker is visible.

## 3. Data exfiltration

Extract process data, often quietly.

What it looks like:

* Read sensor values and historian feeds
* Subscribe to telemetry streams
* Pull configuration or program logic from PLCs

Protocols involved:

* Modbus, DNP3, IEC-104 (reads)
* OPC UA (variable access)
* MQTT (subscriptions)
* S7 (program block and DB upload)

Design angle: Make the data meaningful. Stealing "register 40001 = 123" is pointless. Stealing "reactor
pressure approaching critical threshold" is a decision point. Pulling an S7 program block is a full
blueprint of what the process is doing and where the limits are.

## 4. Data integrity manipulation

Lie to the operator or control system.

What it looks like:

* Inject false sensor readings
* Replay old "safe" values
* Spoof responses from field devices
* Poison historian data

Protocols involved:

* DNP3 (replay, unsolicited responses)
* IEC-104 (response injection)
* MQTT (publish fake telemetry)
* Modbus (spoofed replies)

Design angle: This is where subtlety lives. The best attacks do not break the system, they convince it
everything is fine while it quietly breaks itself.

## 5. Replay and timing attacks

Reuse valid traffic to reproduce effects or desynchronise systems.

What it looks like:

* Capture and replay control messages
* Delay or reorder packets
* Exploit deterministic response patterns

Protocols involved:

* DNP3 (classic replay)
* Modbus (predictable transactions)
* IEC-104 (sequence manipulation)

Design angle: These are low-effort, high-impact in poorly defended environments. Also a good place to
introduce detection challenges.

## 6. Control logic manipulation

Change how the system behaves, not just its current state.

What it looks like:

* Upload modified PLC logic
* Change function blocks or ladder logic
* Alter alarm thresholds or control loops
* Adjust a single setpoint by a small increment, staying within normal operating range but nudging the
  process toward a fault condition over time

Protocols involved:

* S7 (program upload/download)
* OPC UA (method calls, configuration writes)

Design angle: This is persistence in OT clothing. The system keeps betraying itself long after the
attacker leaves. Subtle setpoint changes are more realistic for stealth operations than dramatic logic
rewrites: they stay within normal operating parameters, avoid triggering alarms, and are considerably
harder to attribute.

## 7. Denial of control and safety disruption

Prevent operators or systems from controlling the process safely.

What it looks like:

* Stop PLC CPU
* Flood communication channels
* Break protocol sessions
* Trigger fail-safe or fail-open states

Protocols involved:

* S7 (CPU stop)
* IEC-104 and DNP3 (session abuse)
* MQTT (broker flooding)

Design angle: Not all outages are loud. A slow loss of visibility can be far more dangerous than an
immediate shutdown. MQTT broker flooding is theoretically plausible as a denial-of-service on the
publish/subscribe layer but has no confirmed real-world incident in OT environments.

## 8. Trust exploitation and misconfiguration abuse

Abuse the fact that OT networks assume everything inside is friendly.

What it looks like:

* Anonymous OPC UA access
* Default MQTT credentials
* Flat network movement between zones
* Blind trust between SCADA and field devices
* Protocol gateway and converter devices at zone boundaries: they translate between Modbus, DNP3, and
  IP, are often poorly secured, and sit between network segments by design

Protocols involved: all of them, frankly.

Design angle: This is the bridge to reality. Most real incidents are not zero-days; they are "why is
this open to the entire network". Protocol gateways are a specific gap: security teams rarely own them
clearly, and they are accessible from both sides of the boundary they sit on.

## 9. Protocol abuse and malformed input

Break or stress implementations rather than using them as intended.

What it looks like:

* Send malformed frames or APDUs
* Trigger edge-case parsing behaviour
* Fuzz protocol handlers

Protocols involved:

* IEC-104 (APDU crafting)
* S7 and Modbus (implementation quirks)

Design angle: Easy to get wrong in a CTF. If overused, it turns into "guess the crash input" rather
than learning anything useful.

## 10. Initial access and lateral movement through the IT/OT boundary

Reach the OT environment from adjacent systems that span the divide.

What it looks like:

* Compromise an engineering workstation (EWS): it has legitimate protocol access to every PLC and IED
  it manages, and is often a standard Windows machine on a shared or adjacent network
* Abuse vendor remote access channels: persistent VPN or remote desktop sessions installed for
  maintenance, rarely monitored, sometimes active permanently
* Pivot via the SCADA historian: often dual-homed between IT and OT networks, running standard Windows,
  and treated as IT infrastructure by IT teams and OT infrastructure by OT teams, adequately protected
  by neither
* Reach OT systems through Active Directory or shared authentication infrastructure extended into the
  OT zone
* Use the HMI as a command-issuing endpoint: it has full protocol access to the process and is often the
  most accessible Windows machine in the OT zone

Incident anchors: Triton/TRISIS was installed on an engineering workstation that had legitimate access to
the Triconex safety controllers. Industroyer and BlackEnergy (Ukraine 2015) both reached OT systems
through prior compromise of the corporate IT network. Colonial Pipeline's initial access was a VPN
credential with no multi-factor authentication.

Design angle: The initial access layer is almost entirely absent from published CTF challenges, which
typically drop the participant already inside the OT network. Including even a simple EWS-to-PLC pivot
teaches something most participants have never practised, and reflects how the vast majority of real
incidents actually begin.

## Playbooks

This becomes the playbook.

For example, *"Manipulate the cooling system so the reactor overheats, without triggering alarms"*

A participant has options: direct write (loud, obvious), data spoofing (subtle), logic manipulation
(persistent). Learning happens. Most likely.
