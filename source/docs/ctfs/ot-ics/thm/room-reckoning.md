# Room design: Dead Reckoning

## Premise

UU Power and Light runs a turbine at the Hex facility. The control network is reachable. Nobody
changed the defaults. You have a foothold on the corporate segment and a packet of curiosity.

The room teaches OT reconnaissance, protocol enumeration, and unauthenticated state manipulation
against a live physics simulation. Every action has a consequence the participant can observe.

Difficulty: beginner to intermediate.

Techniques covered: 1 (unauthorised state manipulation), 2 (process intelligence gathering),
8 (trust exploitation and misconfiguration abuse).

Simulator: power-and-light-sim, single-process, no Docker.

## Tasks

### Task 1: Introduction

Background reading. No flag.

Cover:
* what OT/ICS is and why it differs from standard IT environments
* what power-and-light-sim models (turbine, physics engines, Purdue network zones)
* what the participant will be doing and why it matters outside the lab

Questions (no flag, knowledge check):
* What protocol is commonly used for reading and writing to PLCs in OT environments?
* What port does Modbus TCP typically use in production environments?

### Task 2: Find what is listening

Scan the target. Identify open ports and services.

Scenario: you are inside the corporate segment. The control network is adjacent. Start with what
you can see.

Expected finds:
* OPC UA on port 4840
* Modbus TCP on port 10502 (and adjacent ports for other devices)
* Possibly a web interface

Questions:
* What OPC UA port is open on the target?
* How many Modbus TCP ports are listening? (answer leads to understanding multi-device setup)

Flag 1: visible in the OPC UA server description field, readable without credentials via any
OPC UA client. Reward for anonymous browsing before touching anything else.

### Task 3: Read the room

Enumerate the OPC UA node tree without credentials. Understand what the simulation exposes.

The OPC UA server has anonymous access enabled. Browsing the namespace reveals device names,
register descriptions, live sensor values, and the flag.

Tools: `opcua-client`, `python-opcua`, or any OPC UA browser.

Questions:
* What is the name of the turbine device exposed in the OPC UA namespace?
* What is the current turbine RPM reading? (requires live enumeration, not guessing)
* What node contains the flag?

Flag 2: stored in an OPC UA node under the turbine device subtree. Only accessible by browsing
the namespace, not by knowing the path in advance.

Learning outcome: OPC UA anonymous access is a misconfiguration, not an edge case. Namespace
browsing reveals the full information model of the device, including things the operator did not
intend to expose.

### Task 4: Speak Modbus

Read Modbus registers from the turbine PLC. Understand what each register means.

The turbine PLC exposes holding registers and coils on port 10502. No authentication. Standard
Modbus function codes work without modification.

Registers of interest:
* RPM (input register, live value from physics engine)
* Governor setpoint (holding register, writable)
* Trip status (coil, readable)
* Overspeed threshold (holding register, writable)

Tools: `mbtget`, `pymodbus`, `modbus-cli`.

Questions:
* What function code reads holding registers?
* What is the current governor setpoint value?
* Is the trip coil currently active? (0 or 1)

Flag 3: encoded in a holding register that is readable but not obviously named. The register map
is not provided; participants enumerate to find it.

Learning outcome: Modbus has no authentication. Reading registers is indistinguishable from a
legitimate engineering query. The register map is the asset worth protecting.

### Task 5: Pull the thread

Write to the governor setpoint register to command the turbine above its rated speed. Observe
the physics engine respond.

The TurbinePhysics engine updates continuously. Writing a value above the rated RPM to the
governor setpoint causes the turbine to accelerate. If no protection trip fires (because the
overspeed threshold has been raised or the trip coil disabled), the turbine enters an overspeed
condition. The simulation logs the event and changes observable state.

The flag is not awarded for sending the write command. It is awarded when the physics engine
confirms the turbine has reached the target condition. This requires understanding the register
map well enough to write the right value to the right address.

Questions:
* What register address controls the governor setpoint?
* What value causes the turbine to exceed rated speed?
* What does the trip status coil read after the overspeed condition is reached?

Flag 4: written to a register by the physics engine when the turbine reaches the overspeed
threshold. Readable via FC03 after the condition is triggered. Not present before.

Learning outcome: the consequence is physical, not just a flag in a file. The same write
command, against real equipment, causes the same outcome described in the CVE references and
incident reports linked in the room text.

### Task 6: What just happened

Post-exploitation reflection. No new flag.

Cover:
* what an operator would see in the SCADA dashboard during and after the attack: RPM spike,
  protection trip (or not), event log entry
* what logs, if any, record the event and why that matters for incident response
* the real-world equivalent: an overspeed event trips protection systems under normal
  conditions; if protection settings have been manipulated, as demonstrated here, it does not.
  Mechanical failure follows. Outage durations are measured in months rather than hours,
  depending on parts availability. CVE-2022-3084 (GE Reason RT430) confirms that protection
  relay settings are reachable via unauthenticated Modbus in deployed equipment, not just in
  simulation.

Defence (one mitigation at each stage of the attack path):
* OPC UA anonymous access disabled (security mode Sign or SignAndEncrypt): flags 1 and 2
  become unreachable without valid credentials
* network segmentation between the corporate segment and the control network: removes the
  attack surface before any scanning takes place
* Modbus TCP behind a unidirectional gateway or application-layer firewall: flag 3 and the
  governor write in task 5 become impossible

Questions (knowledge check, specific answers required):
* What network-level control would have prevented initial Modbus access?
* What authentication mechanism does OPC UA support that was not enabled here?
* Name one real-world incident where unauthenticated Modbus writes caused physical damage.

Reflection (no answer needed):
* The attack demonstrated here took minutes. What changes if the same capability is applied
  incrementally over weeks, staying within normal operating parameters until a chosen moment?
* This room defeated protection by manipulating settings before the overspeed condition was
  reached. What does relying on protection trips as the last line of defence assume about
  attacker knowledge and prior access?

No flag. The knowledge-check questions require reading. The reflection prompts have no
required answer.

## Flag summary

| Flag | Location                               | Technique | How earned                      |
|:-----|:---------------------------------------|:----------|:--------------------------------|
| 1    | OPC UA server description field        | 8         | Anonymous OPC UA connection     |
| 2    | OPC UA node under turbine device       | 2         | Namespace browsing              |
| 3    | Holding register, unlabelled           | 2         | Modbus register enumeration     |
| 4    | Written by physics engine on overspeed | 1         | Correct governor setpoint write |

## VM specification

- Base: Debian 8 compatible, BIOS boot, DHCP.
- RAM target: functional at 512 MB, comfortable at 1 GB.
- Services at startup: power-and-light-sim via systemd, exposing OPC UA (4840) and Modbus TCP (10502 minimum, additional device ports?).
- No internet dependency: all dependencies vendored during VM build.
- Ports exposed: 4840, 10502 (and adjacent). And for perhaps a webinterface.

## Room title explained

* Dead Reckoning means navigating without landmarks, which is what OT attackers do
* No Authentication Required
* The Governor

Tone we keep is dry and factual, there are more than enough "hacker aesthetic" rooms.

## References to include in room text

* [SIMULATOR_GAPS.md](https://github.com/tymyrddin/power-and-light-sim/blob/main/SIMULATOR_GAPS.md) note on Modbus FC43/MEI14 (so participants know fingerprinting will be odd)
* [ICS-CERT Advisory ICSA-10-090-01](/_static/presentations/ICSA-10-090-01.pdf) (Modbus design limitation, no auth by design)
* [CVE-2022-3084](https://euvd.enisa.europa.eu/vulnerability/CVE-2022-3084) (unauthenticated Modbus write to protection settings, GE Reason RT430)
