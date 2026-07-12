# SCADA observables

The e-terra SCADA system at Stedin logs alarms, operator commands, mode changes, and network state at the control-centre
level. The alarm journal shows what normal operation looks like, what evidence survives when a command is issued, and
how a legitimate operational decision reads differently from an unauthorised change.

## The normal baseline

Stedin's e-terra SCADA maintains a continuous alarm and event journal that logs all state changes in the distribution
network. The journal records operator commands issued from the control room, the timestamp of each action, the
operator's user ID, the target device (a switchpoint, a load, a protection zone), the command (Open, Close, Isolate,
Restore), and whether the command was acknowledged. Each command has a corresponding event record when the field device
reports back that the operation completed (or failed to complete).

The rhythm of normal operation appears in the journal as a sequence of planned switching operations during maintenance
windows, interspersed with automatic protection events triggered by faults and subsequent restoration. During a planned
outage, the journal shows a sequence of commands issued in order, matching a bedieningsplan (switching plan) prepared in
advance, with operator acknowledgements at each step and field devices reporting successful state changes. Unplanned
faults appear as automatic protection relay trips followed by operator analysis and either immediate restoration or a
call to dispatch a field crew. The journal also logs alarm threshold changes, configuration updates to the SCADA system
itself, and login-logout events of operators connecting to e-terra.

Normal operation also includes background alarms that appear regularly and are expected by the operators. A feeder
that consistently runs near its thermal limit may generate a low-level warning alarm every warm afternoon that the
operator acknowledges and monitors; this is normal, not evidence of a problem. High-voltage transmissions under stress
during peak demand trigger alarms that the TenneT dispatcher and Stedin operator coordinate on; this too is routine. The
baseline for an operator includes learning which alarms are "crying wolf" and require investigation versus which are
expected noise. The SCADA journal captures this pattern: frequent acknowledgements of the same alarm, quick dismissals
without further action, and a steady cadence matching the network's load and weather cycles.

## Configuration changes and audit trails

Stedin's e-terra maintains version records of its alarm thresholds, load-shedding logic, under-frequency relay settings,
and the mapping between logical network model (the GIS view of the distribution network) and physical reality (the
actual substation). Configuration changes can be initiated by authorised engineers through the SCADA
engineering interface, and when a change is made, the system logs the old value and new value, the timestamp, the user
ID of whoever made the change, and sometimes a work-order reference.

A legitimate configuration change during a maintenance window appears in the journal as a documented change with an
associated work order, preceding a series of switching operations that test the new configuration. The most common
changes involve updating alarm thresholds when a network branch is upgraded (raising voltage limits because a new
transformer with higher capacity is installed), or modifying load-shedding logic when the network topology changes.
These changes go through change control at Stedin: the engineer submits a change proposal, it is reviewed and approved
by the OT lead, the engineer applies it at a scheduled time, and the change is documented in the asset management
system (Maximo).

Unauthorised changes are distinguished by their context. An alarm-threshold change made outside any documented
maintenance window stands out. A threshold change that makes protections less sensitive (raising an over-current
alarm so fewer faults trigger it) without corresponding work to address the underlying problem is a red flag. A series
of threshold changes made in rapid succession at odd hours does not fit the baseline. A configuration change that is made but never
documented in the work-order system is a clear sign of unauthorised activity. Most tellingly, a change made to the
SCADA configuration that does not match any documented maintenance and is immediately followed by anomalous field
behaviour (an unexpected switchpoint opening, a cascade of alarms) is strong evidence of compromise rather than
legitimate engineering.

## Alarm journal integrity

The SCADA alarm journal is append-only, so a gap in its sequence or an undocumented deletion reads as tampering. The
check specific to this layer is against the operator's own record. If the journal shows an operator issuing a command
to open a switchpoint, but the operator's actual command log (a separate log on their workstation or in e-terra's user
session) holds no such command, either the journal was falsified or the command came from elsewhere, a compromised
field device executing it, or an attacker with network access injecting it. When the journal contradicts the operator's
own command log, the mismatch is the signature, and whether it is compromise or a glitch turns on whether the
discrepancy is isolated or systematic, dozens of commands with no corresponding operator action.

## Operator action patterns and anomalies

Stedin's SCADA logs operator actions at a fine grain: not just which switches were operated, but which operator did it,
when, and from which control-room terminal. Over time, an operator develops a pattern of working hours, typical
commands, typical sequence of actions, and typical response times to alarms. An operator who normally works 08:00-17:00
suddenly logging in at 02:00 is anomalous. An operator who typically issues five switching commands per shift suddenly
issuing fifty in an hour is hard to explain. An operator who normally manages low-voltage distribution and suddenly accessing
high-voltage relay settings is suspicious. The credential-compromise signals underneath these patterns, simultaneous
sessions, failed-then-successful logins, logins from unexpected places, are read from the authentication record.

Commands outside the operator's authorisation level are another pattern. Stedin's Bedrijfsvoering system defines what
each operator is Schakelbevoegd to do. If an operator with authorisation only for low-voltage work attempts to
issue a command on a high-voltage substation and the command is rejected, that is evidence either of an attacker using
the operator's compromised credentials or of a confusion about what the operator is authorised for. Approval
workflows can surface mismatches: if an operator with documented authority attempts a command, and it is rejected, their
actual permissions do not match their documented role. If the rejection happens repeatedly for the same operator, there
is a systemic mismatch to investigate. If an unauthorised command is issued successfully (a low-voltage operator is
somehow able to modify high-voltage relay settings), that indicates either an access-control bypass or a compromise of
the SCADA system itself.

## The control-room evidence surface

The control room is the evidence-generating layer for the entire Stedin network. Everything visible to the operator at
the HMI (the graphical map of the network on their screen), every command they issue, every alarm they acknowledge,
every setting they change, and every time they log in is recorded by the SCADA system, transmitted to a historian, and
archived. The strength of this evidence is that it is continuous and comprehensive: if an operator acted, it is
logged. The limitation is that the logs are tool-mediated (they depend on the SCADA system itself not being compromised)
and they reflect only what the operator saw and did, not what the operator should have known.

For forensic analysis, the SCADA journal is the starting point: it is the control room's own account of what happened,
at a millisecond granularity, stamped with operator IDs and timestamps. It is compared against other independent logs (the
field device's own event logs, the historian's time-series records, the protection relay's trip records) to see if they
agree. If they diverge, something is inconsistent: either the SCADA journal is falsified, or the field device's logs
are, or both systems captured different parts of a complex sequence. The agreement between SCADA logs and field-device
logs is the core forensic signature for a system operating as designed. The divergence is the signature of compromise or
serious malfunction.

    ONE COMMAND, ITS INDEPENDENT RECORDS
    ─────────────────────
    An operator closes Switchpoint A at 15:30:42. The act lands in five records
    that are meant to agree:

      e-terra SCADA journal     15:30:42  Close A requested by operator_123, ACK
      RTU event log             15:30:42  received 104 frame, Close A, executed
      e-terra historian         15:30:42  A state transition OPEN → CLOSED
      relay sequence-of-events  15:30:42  input change at switchpoint A
      physical state            CLOSED    coil energised, contacts closed

    Agreement across all five is the signature of normal operation. A divergence,
    the SCADA journal naming A while the RTU and relay record B, or a gap where
    the historian holds no record of seconds the field devices clearly logged, is
    the signature of compromise or serious malfunction. The records differ in how
    far they sit from an attacker's reach: the SCADA journal is tool-mediated and
    editable, the RTU and relay logs sit on separate devices and network segments,
    the physical measurement is outside every system. The more independent records
    a false claim has to stay coherent across, the larger the footprint forging it
    leaves.

*Last updated: 12 July 2026*
