# State machine transitions

Stedin's network devices move through defined operational states. A switchpoint is either Open or Closed. A breaker is
Healthy, Degraded, or Unhealthy based on its mechanical operating count and contact condition. A protection relay is
either In Service, Out of Service for Maintenance, or Disabled. A feeder is either Energised or De-energised. The
transitions between these states are governed by logic and constraints, and anomalous transitions reveal compromise or
malfunction.

## Switchpoint and breaker state machines

A switchpoint has a simple binary state machine: Open or Closed. Under normal operation, the switchpoint is commanded to
transition by an operator or by protection logic. When a command is issued, the switchpoint mechanically transitions (
takes seconds to minute depending on the mechanism), and then reports its new state. The SCADA records the command, the
transition time, and the final state.

Normal transition logs show: command issued, brief delay (transition time), report received confirming new state, and
the new state matching the command. A Close command results in a Closed state report. An Open command results in an Open
state report. The delay is consistent (the same switchpoint always takes approximately the same transition time).

Anomalous transitions include: a command that is not executed (command issued but the switchpoint remains in the old
state), a state change that contradicts the command (Close command issued but the switchpoint opens instead), or a state
that oscillates rapidly (the switchpoint rapidly alternates between Open and Closed within seconds, which is physically
impossible for a mechanical switchpoint and indicates either false reporting or a sensor malfunction).

Breaker state is more complex. A breaker's mechanical condition is tracked by monitoring its operating count (the number
of times it has opened and closed). Each operation causes contact wear and mechanical stress. At Stedin, mechanical
counters on breakers track this directly. As the count increases, the breaker's condition degrades. When the count
reaches a maintenance threshold, the breaker enters a Degraded state and must be serviced or replaced. If the mechanical
count shows an impossible jump (sudden increase of thousands of operations in seconds), that indicates either sensor
tampering, mechanical failure, or false reporting.

## Protection relay service states

Protection relays can be in several states: In Service (actively protecting the network), Out of Service for
Maintenance (accessible to engineers but not protecting), or Disabled (protection function explicitly disabled). These
states are controlled by configuration and operator settings.

The normal state is In Service. The relay continuously monitors electrical quantities and would trip if configured
thresholds are exceeded. During planned maintenance, a relay is explicitly placed Out of Service, meaning the protection
function is disabled temporarily while work is performed. After maintenance, the relay is returned to In Service. The
state transitions are logged: when the relay was transitioned out of service, by whom, and when it was transitioned back
in.

An anomalous transition would be a relay transitioning to Out of Service without corresponding work authorisation, or
remaining Out of Service for an extended period without justification. If a critical relay is Out of Service for days
without a documented maintenance activity, that is suspicious. A relay that is placed Out of Service at 01:00 without
emergency justification suggests unauthorised disabling of protection.

The state-transition log is the forensic source. If the relay's internal logs show it was placed Out of Service at 03:00
UTC on a date when no maintenance was scheduled, but the work order records show the maintenance was scheduled for 09:00
UTC, there is a timing discrepancy. Either the relay's clock is incorrect, or the relay was transitioned out of service
early to allow unauthorised work, or the logs are falsified.

## Feeder and section energisation state

A feeder or network section can be Energised (carrying voltage and potentially supplying load) or De-energised (no
voltage, safe for maintenance work). Transitions between states are controlled by switchpoints and are documented in
switching plans. A normal transition sequence for planned de-energisation might be:

1. Feeder currently Energised, no alarms
2. Operator issues command to Open switchpoint at feeder source (taking the feeder out of service)
3. Switchpoint opens, feeder is now De-energised
4. Operator verifies no voltage on de-energised section (safety check)
5. Work proceeds
6. After work, feeder is re-energised by closing the switchpoint
7. Load transfers from alternate feed, feeder returns to normal operation

The logs record this sequence clearly. The switching plan specifies the steps, the SCADA logs show commands and
responses, and the switching times are consistent with the sequence.

Anomalous transitions include: a feeder transitioning from Energised to De-energised without an operator command (
spontaneous de-energisation, which would indicate either a fault triggering protection or unauthorised switching), or a
feeder remaining De-energised far longer than the planned maintenance window. A feeder that was supposed to be
re-energised at 17:00 but was still de-energised at 20:00 indicates either an extended maintenance, a problem
re-energising, or unauthorised continued de-energisation.

## Asset state and condition tracking

Stedin tracks asset condition: transformers, capacitors, and other equipment have condition states (New, Healthy,
Degraded, Needs Replacement). These states are updated through maintenance inspections, condition monitoring, and
automated alerts. An asset that transitions from Healthy to Degraded normally has a corresponding maintenance work order
explaining why the condition changed.

Normal state transitions show: asset in Healthy state, inspection performed (documented in work order), condition
assessed, and state updated if necessary (to Degraded if inspection found problems). The assessment is documented with
details (what was found, what corrective action is needed).

Anomalous transitions include: an asset state changed without a corresponding inspection or work order, or an asset's
condition state reversed (Degraded to Healthy) without maintenance being performed. If an asset's condition state is
downgraded (Healthy to Degraded) without corresponding evidence of condition change (no inspection records, no technical
justification), that is hard to explain innocently.

## Work order and asset life-cycle states

Work orders themselves have state machines. A work order progresses through states: Submitted, Approved, In Progress,
Completed, Verified, and Closed. Transitions between states are controlled by authorisation (only a manager can approve,
only designated personnel can mark as completed, only an inspection authority can verify).

Normal work-order progression shows smooth transitions from one state to the next, with documented reasons for each
transition. A work order that is submitted and then jumps directly to Closed without passing through Approved, In
Progress, and Verified would indicate either a system malfunction or unauthorised state manipulation.

The work-order state is important because it controls what activities are authorised. Once a work order is Closed, the
maintenance window is officially ended. If work continues after the work order is Closed, that work is unauthorised.
Conversely, if a work order remains In Progress indefinitely, the work is extending beyond its authorised window.

## Timing of state transitions

The timing of state transitions is observable and can be cross-referenced against other events. A protection relay
trip (a state transition from Normal to Tripped) occurs at the same time as the fault that triggered it appears in
the historian's measurements. A switchpoint state change is visible in the feeder's current measurements (a
sudden drop in current when a switchpoint opens).

Timing anomalies include: a state transition that is recorded but does not correspond to any observable physical
change (a relay trip recorded but no fault visible in the historian, a switchpoint open recorded but no current drop
measured). These mismatches indicate either false reporting or log falsification.

Similarly, the timestamp of a state transition is observable. If a state transition is recorded with a timestamp that is
out of order (a transition at 10:00 UTC is followed by a transition at 09:50 UTC), the logs have inconsistent timestamps
or the later transition was backdated. This indicates either clock-synchronisation issues or deliberate manipulation of
event timestamps.

## State consistency across replicated systems

For critical assets, Stedin may have redundant monitoring or control systems. A switchpoint's state is reported by the
RTU that controls it and by the SCADA that commands it, and potentially by multiple sensors. These independent systems
are expected to agree on the switchpoint's state.

If the SCADA shows a switchpoint is Closed but the RTU reports it is Open, and independent measurement of the actual
switchpoint (a technician at the site or a video feed) shows it is Open, then the SCADA's state report is false. This
false reporting could indicate a software bug, a misconfiguration, or deliberate falsification in the SCADA.

The consistency check is powerful because it is independent of the system being checked. Even if one system is
compromised, the other independent systems provide validation. If multiple systems diverge in their state reports for
the same asset, the divergence is the forensic signature that something is wrong.

*Last updated: 12 July 2026*
