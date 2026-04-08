# Challenge concepts

## What makes a concept worth building

A good OT/ICS CTF concept passes three tests before any code is written:

* The technique is specific enough to test one thing. "SCADA attack" is not a concept. "Unauthenticated
  Modbus coil write that opens a breaker and triggers a downstream fault" is.
* The flag location follows from the technique. Earning the flag comes from understanding what happened,
  not from running `find / -name flag.txt`.
* The physical consequence is visible. One of the things OT simulation can do that a standard CTF cannot
  is show what the attack actually causes. A challenge that discards this advantage is wasting its
  environment.

## What translates well from the attack surface

The technique categories in the attack surface reference map unevenly to the simulators. The table below
shows which categories have direct simulator backing and where the coverage comes from.

| Technique                                  | Simulator coverage                                                                                                                           |
|:-------------------------------------------|:---------------------------------------------------------------------------------------------------------------------------------------------|
| 1. Unauthorised state manipulation         | power-and-light-sim: Modbus coil write, turbine overspeed, safety interlock bypass; DNP3, IEC-104, and S7 protocols present and reachable    |
| 2. Process intelligence gathering          | power-and-light-sim: OPC UA anonymous browsing, recon phase scripts; ics-simlab: relay configuration read                                    |
| 3. Data exfiltration                       | ics-simlab: historian data access, relay config pull; power-and-light-sim: register reads across protocols                                   |
| 4. Data integrity manipulation             | partial: historian tampering in ics-simlab touches this but the physics layer does not yet accept injected values as real sensor input       |
| 6. Control logic manipulation              | power-and-light-sim: setpoint-level attacks; S7 program blocks reachable on port 102 but no challenge exercises CPU stop or logic upload yet |
| 7. Denial of control and safety disruption | power-and-light-sim: safety interlock bypass, emergency stop command                                                                         |
| 8. Trust exploitation and misconfiguration | power-and-light-sim: SCADA anonymous access, RBAC bypass, OPC UA credential sniffing                                                         |
| 10. Initial access and lateral movement    | ics-simlab: EWS pivot, zone-to-zone movement; power-and-light-sim: enterprise-to-control lateral movement                                    |

Techniques 5 (replay and timing), 9 (protocol abuse), and the vendor remote access and HMI sub-surfaces
of technique 10 have no current simulator coverage.

## Feasible but not yet simulated

These techniques appear in the attack surface reference, are realistic, and in several cases the
protocol or infrastructure partially exists in the simulators. No challenge or scenario covers them yet.
They are candidates for simulator extension or new challenge development.

DNP3 CROB (unauthenticated breaker operation): DNP3 runs on ports 20000-20002 in power-and-light-sim.
No challenge exercises the control relay output block path or makes the physical consequence of a CROB
command visible.

IEC-104 command injection: the protocol is in power-and-light-sim. No challenge targets single or
double command injection, and there is no IEC-104-specific physical model consequence to show.

S7 CPU stop and program manipulation: S7 is accessible on port 102 in power-and-light-sim. No challenge
tests CPU stop, program block upload, or DB write beyond what a Modbus challenge already covers. The
interesting surface here is logic persistence, not just a single state change.

Subtle setpoint drift: power-and-light-sim supports setpoint-level access. No challenge uses a
within-bounds incremental adjustment as the attack vector. This is more realistic for stealth
scenarios than the dramatic overspeed challenges already present.

Data integrity manipulation and false sensor injection: neither simulator currently models a path
where an attacker injects false readings that the physics layer treats as real. The consequence of
spoofed sensor data (a control system responding to a lie) is absent. This is a significant gap given
how central false data injection is to real-world ICS attacks.

Replay attacks: neither simulator captures and replays protocol traffic as a challenge mechanic.
A DNP3 or Modbus replay challenge would require packet capture infrastructure and a timing model.

MQTT wildcard intelligence gathering: it is unclear whether either simulator exposes an MQTT broker.
If not, adding one to ics-simlab as a telemetry bus would be low-cost and enable a well-scoped
beginner challenge.

Protocol gateway and converter abuse: neither simulator includes a gateway device at a zone boundary.
Adding one between the operational and control zones in ics-simlab would create a realistic pivot
surface and reflect how many real environments are actually architected.

Vendor remote access abuse: the EWS pivot in ics-simlab is the closest analogue, but it is framed
as zone-to-zone movement rather than as abusing a maintenance channel. A scenario modelling a
persistent vendor VPN session would teach a different and very common attack pattern.

HMI as command-issuing endpoint: power-and-light-sim has web SCADA interfaces that could serve this
role. No challenge currently isolates the HMI as the target or teaches the participant to issue
commands through it rather than directly via protocol.

## What is saturated or unsuitable

Generic "find the open port and run a tool" challenges exist on every platform. Avoid:

* Pure nmap-to-flag exercises with no protocol interaction
* Challenges where the flag is only in a file rather than tied to a protocol outcome
* Complexity added by multiple unrelated services that are not part of the attack path

Root-Me reviewers and TryHackMe audiences both penalise challenges that could have been a web challenge
with an ICS skin painted on.

## What cannot be simulated

Some techniques from the attack surface reference cannot be reproduced in any software-based
simulation environment. These are not gaps to fill; they are architectural constraints that apply
regardless of which simulator or platform is used.

IEC 61850 GOOSE and Sampled Values operate at layer 2 Ethernet multicast. Software-based simulation
environments route IP, not raw Ethernet frames between containers or processes. Reproducing GOOSE
requires host networking or a dedicated layer 2 bridge, which breaks container isolation and is not
achievable on TryHackMe or Root-Me infrastructure. Sampled Values has the additional constraint of
requiring a realistic IED receiving the stream with protection logic that actually responds to
injected values; without that, the challenge has no consequence to observe.

GPS spoofing of PMU timestamps requires radio-frequency hardware. It is not a software simulation
problem and has no meaningful analogue in a containerised or Python-based environment.

Triconex/SIS protocol attacks (the Triton/TRISIS vector) targeted specific Schneider Electric
Triconex firmware versions using a proprietary protocol stack. No open implementation of the
Triconex communication protocol exists. A challenge can model the consequence of a safety system
being bypassed, but the Triton-specific protocol path cannot be reproduced.

Air-gap bridging via removable media is a category error in networked simulation: the technique
is definitionally about bypassing a network, which cannot be modelled in an environment that is
itself a network.

## Challenge inventory

The following challenges are ready for packaging. Each maps to an existing exercise in the simulation
repositories. The technique column references the category numbers in the attack surface reference.

| #  | Name                                             | Technique | Category | Difficulty            | Source              |
|:---|:-------------------------------------------------|:----------|:---------|:----------------------|:--------------------|
| 1  | SCADA Anonymous Access                           | 8         | Realist  | Beginner              | power-and-light-sim |
| 2  | Role-Based Access Control Bypass                 | 8         | Realist  | Beginner-Intermediate | power-and-light-sim |
| 3  | Covering Tracks (Audit Log Evasion)              | 3         | Realist  | Intermediate          | power-and-light-sim |
| 4  | Turbine Overspeed Injection                      | 1         | Realist  | Intermediate          | power-and-light-sim |
| 5  | Dangerous Modbus Function Codes                  | 1         | Realist  | Beginner-Intermediate | power-and-light-sim |
| 6  | Safety Interlock Bypass                          | 7         | Realist  | Intermediate          | power-and-light-sim |
| 7  | Credential Sniffing (OPC UA)                     | 8         | Network  | Intermediate          | power-and-light-sim |
| 8  | Lateral Movement (Enterprise to Control)         | 10        | Realist  | Advanced              | power-and-light-sim |
| 9  | Zone-to-Zone Pivot (via Engineering Workstation) | 10        | Realist  | Intermediate          | ics-simlab          |
| 10 | Historian Data Tampering                         | 3         | Realist  | Beginner-Intermediate | ics-simlab          |
| 11 | Protective Relay Configuration Read              | 2         | Network  | Beginner              | ics-simlab          |
| 12 | Modbus Coil Write Attack (Breaker Open)          | 1         | Realist  | Beginner-Intermediate | ics-simlab          |

See the [attack surface reference](attack-surface.md) for the technique mechanics behind each challenge.
