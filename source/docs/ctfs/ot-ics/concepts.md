# Challenge concepts

## What makes a concept worth building

A good OT/ICS CTF concept passes three tests before any code is written:

* The technique is specific enough to test one thing. "SCADA attack" is not a concept. "Unauthenticated Modbus
  coil write that opens a breaker" is.
* The flag location follows from the technique, not from filesystem exploration. Earning the flag comes from
  understanding what happened, not from running `find / -name flag.txt`.
* The physical consequence is visible. One of the things OT simulation can do that a standard CTF cannot is
  show what the attack actually causes. A challenge that discards this advantage is wasting its environment.

## What translates well from the attack surface

Protocol-level attacks with deterministic outcomes are the most reliable concepts:

* Unauthenticated read/write operations (Modbus, DNP3, IEC-104) where the consequence is a state change in
  the physical model
* Credential sniffing on unencrypted protocol traffic (OPC UA without TLS, MQTT without auth)
* Configuration misreads: anonymous OPC UA browsing that reveals more than intended
* Access control failures on SCADA interfaces (anonymous login, default credentials, no role separation)

Lateral movement and zone pivot challenges are viable but significantly harder to contain. They work best
as advanced standalone challenges where the complexity is the point, not an accident.

## What is saturated or unsuitable

Generic "find the open port and run a tool" challenges exist on every platform. Avoid:

* Pure nmap-to-flag exercises with no protocol interaction
* Challenges where the flag is only in a file rather than tied to a protocol outcome
* Complexity added by multiple unrelated services that are not part of the attack path

Root-Me reviewers and TryHackMe audiences both penalise challenges that could have been a web challenge with
an ICS skin painted on.

## Challenge inventory

The following challenges are ready for packaging. Each maps to an existing exercise in the simulation
repositories.

| #  | Name                                             | Category | Difficulty            | Source              |
|:---|:-------------------------------------------------|:---------|:----------------------|:--------------------|
| 1  | SCADA Anonymous Access                           | Realist  | Beginner              | power-and-light-sim |
| 2  | Role-Based Access Control Bypass                 | Realist  | Beginner-Intermediate | power-and-light-sim |
| 3  | Covering Tracks (Audit Log Evasion)              | Realist  | Intermediate          | power-and-light-sim |
| 4  | Turbine Overspeed Injection                      | Realist  | Intermediate          | power-and-light-sim |
| 5  | Dangerous Modbus Function Codes                  | Realist  | Beginner-Intermediate | power-and-light-sim |
| 6  | Safety Interlock Bypass                          | Realist  | Intermediate          | power-and-light-sim |
| 7  | Credential Sniffing (OPC UA)                     | Network  | Intermediate          | power-and-light-sim |
| 8  | Lateral Movement (Enterprise to Control)         | Realist  | Advanced              | power-and-light-sim |
| 9  | Zone-to-Zone Pivot (via Engineering Workstation) | Realist  | Intermediate          | ics-simlab          |
| 10 | Historian Data Tampering                         | Realist  | Beginner-Intermediate | ics-simlab          |
| 11 | Protective Relay Configuration Read              | Network  | Beginner              | ics-simlab          |
| 12 | Modbus Coil Write Attack (Breaker Open)          | Realist  | Beginner-Intermediate | ics-simlab          |

See the [attack surface reference](attack-surface.md) for the protocol mechanics behind each challenge type.
