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

## The tractable questions

For security research grounded in [observable semantics](observable-semantics/index.rst), the expense is misplaced. The
goal is not to prove that the transformer explodes under this attack but to answer concrete questions about the record:
whether a protection setting was modified, whether a breaker took an unexpected open command, whether a workstation was
used outside a window, whether process values drifted out of step with the operating state. Each can be represented
without simulating megawatts through copper. The expensive part of OT simulation is reproducing the physics; the cheap
part is reproducing the evidence.

## The abstraction layer

Building a testbed around observable semantics rather than vendor-specific implementations carries a complex estate
surprisingly far without standing up the plant behind it.

A realistic distribution-network simulation needs a handful of parts. The evidence-emitters come first, and one
principle runs through all of them: each leaves the record, not the physics behind it.

- A SCADA that logs alarms, operator actions and switching commands, without running load flow.
- A historian that writes time-series and edit audit trails in the shape observable-semantics describes, without
  calculating a value.
- Protection relays that emit sequence-of-events, fault records and disturbance captures, driven by test scenarios
  rather than electromagnetic transients.
- Engineering workstations that log configuration uploads, version comparisons and connections, which off-the-shelf
  tools already do.
- RTUs that log downloads and state changes and report state without driving hardware.

The constraint systems are the procedural layer:

- Work authorisation: documented work plans and switching plans, contractor appointments, shift approvals, maintenance
  windows. These can be a database and a state machine.
- Access control: credentials, formal appointments in access records, key management. These can be role-based access
  checks.
- Change gating: formal interlocks that prevent certain simultaneous actions (opening a breaker while a fuse is also
  open, for example). These can be implemented as business rules.
- Audit trails: logging who did what, when, and why. This is application-level logging, not simulation.

The operational load is representative, not exhaustive:

- Contractor work orders and maintenance windows on a plausible schedule
- RTU telemetry and measurement updates on typical intervals
- Historian data collection and edits in realistic patterns
- Periodic relay testing and commissioning activities
- Network traffic and communications logs

What it can skip is the physics entirely: electromagnetic transients, fault dynamics and relay operation under real
faults, load flow, harmonic distortion, and communications latency down to the millisecond.

What it cannot skip is coherence. A logged relay settings change has to surface everywhere it belongs, the relay's
sequence-of-events, the workstation logs, Maximo, the historian. A work-order completion time has to sit plausibly
against the maintenance window, the shift schedule and the travel. A switching operation that breaks a safety interlock
has to fail, with the log showing the denial. And the record has to carry realistic noise: not every measurement
smooth, not every test passing first time, contractors making the errors that need rework.

## Design pattern

[System-portrait](operating-context/system-portrait.md) already supplies the skeleton, the control architecture, field
devices, asset management, enterprise systems, staffing and constraints. A testbed instantiates that skeleton with
evidence-emitting systems, constraint layers and a representative operational load, and the questions observable
semantics asks then have answers.

Did a relay settings change happen outside a scheduled maintenance window? The work order, the switching plan, the
contractor shift log and the relay's sequence-of-events either line up or they do not.

Did a historian value get edited with no work order behind it? The audit trail settles that one on its own.

Did an engineering workstation reach a protection relay at an odd hour? That one turns on whether an emergency was
called and whether the crew answered inside its response window, and the record holds both.

These are solvable questions in a testbed built around observable semantics. The transformer never needs simulation.

## Implication

System-portrait is not a literal blueprint to copy line-for-line. It is an existence proof: this architecture is
plausible, these vendors are used by real operators, these procedures are published, these constraints are structural. A
testbed respects the same architecture, uses publicly available or mock versions of the same vendor tools, implements
the same procedures, and enforces the same constraints.

The fictional utility is a plausible distribution operator with observable behaviour that matches what
observable-semantics says a distribution operator emits. The evidence is the point. The physics is optional.

*Last updated: 10 July 2026*
