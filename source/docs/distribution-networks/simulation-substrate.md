# Using system-portrait as a testbed foundation

System-portrait describes a plausible distribution network operator: the vendors, the systems, the procedures, the
constraints. The description is grounded in real-world OSINT research but presents a fictional utility company, not a
specific real operator. The point is that it is operationally and architecturally coherent, respects the actual
constraints of how distribution operators work, and emits the same observable evidence patterns that real systems do.

## Rabbit hole

Building a realistic OT security testbed is famously a rabbit hole. "Just build a distribution network lab" rapidly
becomes "build a small utility company." A genuine distribution operator's estate involves:

- Protection relays with very specific timing behaviours (millisecond-scale protection sequences, fault detection logic)
- Remote terminal units speaking IEC 60870-5-104 or IEC 61850
- SCADA servers with control logic, state machines, and interlocks
- Historian databases tracking process values and edits
- Engineering workstations running vendor tools (DIGSI, AcSELerator, SCADA engineering environments)
- Network management and communications (fibre, serial, wireless CDMA)
- PLCs in gas pressure stations with their own control logic
- Actual electrical behaviour that software emulation does not capture

And there is an awkward coupling: the cyber side is tightly bound to the physics. A protection relay tripping 50
milliseconds earlier or later can be the difference between a contained fault and half a feeder disappearing. Emulating
packets does not necessarily emulate what the packets control.

## What a testbed could perhaps simulate

For security research grounded in [observable semantics](observable-semantics/index.rst), the expense is misplaced. 
The goal is not to prove "the transformer explodes under this attack." Useful questions are concrete:

- Was a protection setting modified?
- Did a breaker receive an unexpected open command?
- Was an engineering workstation used outside a maintenance window?
- Did an RTU accept a configuration download that does not match the baseline?
- Did process values become inconsistent with expected operating state?
- Did historian edits occur without corresponding work orders?
- Did switching operations happen in the wrong sequence or outside the documented bedieningsplan?

These observations can be represented without simulating megawatts flowing through copper. The expensive part of OT
simulation is reproducing the physics. The comparatively cheap part is reproducing the evidence.

## The abstraction layer

Building a testbed around observable semantics rather than vendor-specific implementations allows progress surprisingly
far without owning a substation in the back garden.

A realistic distribution-network simulation needs:

Evidence-emission systems (not full implementations)

- A SCADA system that emits alarm and event journals, operator action logs, and switching commands. It need not run real
  load flow; it needs to log actions and state transitions consistently.
- A historian that records process values and audit trails of edits. It need not calculate physics; it needs to emit
  time-series data and change records in the format observable-semantics describes.
- Protection relays that emit sequence-of-events logs, fault records, and disturbance captures. A relay simulator driven
  by test scenarios can produce realistic event logs without simulating electromagnetic transients.
- Engineering workstations that log configuration uploads, version comparisons, and connection records. Off-the-shelf
  tools or test harnesses can produce these logs.
- RTUs that log configuration downloads and state changes. A simulated RTU can accept commands and report state without
  driving actual hardware.

Constraint systems (the procedural layer)

- Work authorisation: documented work plans and switching plans, contractor appointments, shift approvals, maintenance
  windows. These can be a database and a state machine.
- Access control: credentials, formal appointments in access records, key management. These can be role-based access
  checks.
- Change gating: formal interlocks that prevent certain simultaneous actions (opening a breaker while a fuse is also
  open, for example). These can be implemented as business rules.
- Audit trails: logging who did what, when, and why. This is application-level logging, not simulation.

Realistic operational load (representative but not exhaustive)

- Contractor work orders and maintenance windows on a plausible schedule
- RTU telemetry and measurement updates on typical intervals
- Historian data collection and edits in realistic patterns
- Periodic relay testing and commissioning activities
- Network traffic and communications logs

Not required:

- Detailed electromagnetic transient simulation
- Realistic fault physics or protection relay operation under actual faults
- Accurate load flow
- Harmonic distortion modelling
- Communications latency down to the millisecond

Essential:

- Consistent observable evidence: if a relay settings change is logged, it appears in the relay's sequence-of-events, in
  the engineering workstation logs, in Maximo, and in the historian if relevant
- Temporal coherence: a work order completion timestamp is plausible given the maintenance window, the contractor shift
  schedule, and known travel times
- Constraint enforcement: a switching operation that violates a safety interlock cannot execute, and the log reflects
  the denial
- Realistic noise: not every measurement is exactly smooth; not every test passes on the first attempt; contractors
  sometimes make errors that require rework

## Design pattern

System-portrait provides the skeleton:

- Control architecture: SCADA system with EMS/DMS, historian layer, centralised authentication
- Field devices: protection relays, RTUs communicating over standard protocols, Smart Grid Terminals
- Asset management: maintenance workflow system with audit trails
- Enterprise systems: ERP for financial and procurement, cloud platforms for business applications
- Staffing and procedures: contractors under long-term framework contracts, documented work plans and switching plans,
  shift schedules
- Constraints: capital regulation, legacy equipment, labour shortages, regulatory pressure

A testbed instantiates that skeleton with evidence-emitting systems, constraint layers, and representative operational
load. The questions observable-semantics asks then have answers.

Did a relay settings change occur outside a scheduled maintenance window? Evidence exists: there is a work order, a
switching plan, a contractor shift log, and a relay sequence-of-events. Either they all align, or they don't.

Did a historian value edit happen without a work order? The audit trail shows.

Did an engineering workstation connect to a protection relay at an unusual time? Evidence clarifies: was there an
emergency call? Did the contractor respond within the response-time SLA?

These are solvable questions in a testbed built around observable semantics. The transformer never needs simulation.

## Implication

System-portrait is not a literal blueprint to copy line-for-line. It is an existence proof: this architecture is
plausible, these vendors are used by real operators, these procedures are published, these constraints are structural. A
testbed respects the same architecture, uses publicly available or mock versions of the same vendor tools, implements
the same procedures, and enforces the same constraints.

The fictional utility is a plausible distribution operator with observable behaviour that matches what
observable-semantics says a distribution operator emits. The evidence is the point. The physics is optional.

*Last updated: 10 July 2026*
