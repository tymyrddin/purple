# State machine transitions

Network devices move through defined operational states: a switchpoint Open or Closed, a breaker Healthy, Degraded or
Unhealthy, a protection relay In Service, Out of Service or Disabled, a feeder Energised or De-energised. Each reported
state is a claim, and every claim answers to two things: the logic that governs which transitions are allowed, and an
independent record of what the plant actually did. A transition reads as normal when it is permitted, authorised, and
borne out by a physical change or a second system that saw the same thing. It reads as a signature of compromise or
malfunction when the state moves against the rules, without a command, or without the physical world moving to match.
The work throughout is setting the reported state against a record the reporting device does not control.

## Switchpoint and breaker state machines

A switchpoint is Open or Closed, nothing between. An operator or the protection logic commands it, it takes seconds to a
minute to move depending on the mechanism, and it reports the new state; the SCADA records the command, the time, and
where it ended.

A normal log reads cleanly: the command goes out, a brief and consistent transition time passes, and the switchpoint
reports the state the command asked for, Close to Closed, Open to Open. The same switchpoint takes about the same time
every time.

What breaks that reads three ways. A command that never takes leaves the switchpoint in its old state. A command
answered by the opposite, a Close that opens, is a contradiction on its face. And a state that flickers Open and Closed
within seconds is not a mechanical switchpoint at all, which cannot move that fast, but a false report or a failing
sensor.

Breaker condition is tracked by an operating count, the number of open-close cycles the mechanism has run, since each
cycle wears the contacts. A mechanical counter on the breaker holds this directly, and as the count climbs the breaker
moves from Healthy towards Degraded and, at a maintenance threshold, out of service. The counter is a record in its own
right, independent of the SCADA's tally of the operations it commanded, and that independence is the check. A counter
that leaps by thousands in seconds is not a breaker that truly cycled that many times but sensor tampering, mechanical
fault, or false reporting; a handful of commanded operations beneath a counter reading thousands puts the fault in the
counter or its sensor, not in the plant.

## Protection relay service states

A protection relay reports one of a few service states, In Service and actively protecting the network, Out of Service
for maintenance and reachable by engineers but not protecting, or Disabled with the protection function explicitly off.
The state is a field the relay sets and the SCADA reads, which is precisely why it cannot be taken at face value.

The normal state is In Service. The relay continuously monitors electrical quantities and would trip if configured
thresholds are exceeded. During planned maintenance, a relay is explicitly placed Out of Service, meaning the protection
function is disabled temporarily while work is performed. After maintenance, the relay is returned to In Service. The
state transitions are logged: when the relay was transitioned out of service, by whom, and when it was transitioned back
in.

An anomalous transition would be a relay transitioning to Out of Service without corresponding work authorisation, or
remaining Out of Service for an extended period without justification. If a critical relay is Out of Service for days
without a documented maintenance activity, that is suspicious. A relay that is placed Out of Service at 01:00 without
emergency justification suggests unauthorised disabling of protection.

The state-transition log catches a discrepancy against the paperwork: a relay's internal log showing Out of Service at
03:00 UTC on a date with no scheduled maintenance, against a work order set for 09:00, leaves the relay disabled early,
its clock wrong, or the log falsified. But a service state is a claim like any other, and the firmer check does not take
the relay's word for whether it was protecting. A fault settles that. If the
[historian](../measurements-and-data-records/historian-patterns.md) shows an overcurrent that crossed the trip threshold
while the relay, reporting In Service, recorded no trip and the breaker never opened, the relay was not protecting
whatever its state field said. The reverse reads too, an RTU or the SCADA seeing protection drop out while the state log
still shows In Service, sets the reported state against what the network actually saw rather than against the relay's own
account.

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

The anomalies are a de-energisation no command explains, which is either protection tripping on a fault or someone
switching without authority, and a section that stays dead far past its window, a feeder due back at 17:00 but still
cold at 20:00, which is an overrun, a failed re-energisation, or a de-energisation held open on purpose.

The reported state answers to the measurement beneath it. A section reported De-energised while the
[historian](../measurements-and-data-records/historian-patterns.md) still holds voltage or current on it is a report the
plant contradicts, the reading an operator's safety check is there to catch before anyone works the line. A section
reported Energised while every downstream measurement sits at zero is the same contradiction the other way, and in both
the measurement is the independent word the switchpoint's own state report has to meet.

## Asset state and condition tracking

The operator tracks asset condition: transformers, capacitors, and other equipment have condition states (New, Healthy,
Degraded, Needs Replacement). These states are updated through maintenance inspections, condition monitoring, and
automated alerts. An asset that transitions from Healthy to Degraded normally has a corresponding maintenance work order
explaining why the condition changed.

Normally the state moves on the back of an inspection: a Healthy asset is examined under a work order, its condition
assessed, and the state stepped to Degraded only if the inspection found something, with the finding and the corrective
action written down.

Anomalous transitions include an asset state changed with no inspection or work order behind it, or a condition reversed
from Degraded to Healthy with no maintenance performed. Where the asset carries condition monitoring, the state has data
to answer to as well as paperwork: a downgrade to Degraded that no monitoring reading supports, no rising dissolved-gas
trend in a transformer, no temperature excursion, no partial-discharge activity, is a record moved by hand rather than
by the asset, and a reversal to Healthy with nothing between the two states is a record moved to bury a problem rather
than fix it.

## Work order and asset life-cycle states

Work orders themselves have state machines. A work order progresses through states: Submitted, Approved, In Progress,
Completed, Verified, and Closed. Transitions between states are controlled by authorisation (only a manager can approve,
only designated personnel can mark as completed, only an inspection authority can verify).

Normal work-order progression shows smooth transitions from one state to the next, with documented reasons for each
transition. A work order that is submitted and then jumps directly to Closed without passing through Approved, In
Progress, and Verified would indicate either a system malfunction or unauthorised state manipulation.

The work-order state governs what is authorised, which is why it is worth setting against what was actually done. Once a
work order is Closed the window is ended, so switching that still appears in the
[SCADA journal](../control-and-command-execution/scada-observables.md) under that work after its Closed timestamp is
activity with no authorisation behind it. A work order left In Progress indefinitely is the same gap from the other
side, work running past the window it was granted. The state transition on its own is only a claim in Maximo; the
operational record is where it is borne out or contradicted.

## Timing of state transitions

The timing of state transitions is observable and can be cross-referenced against other events. A protection relay
trip (a state transition from Normal to Tripped) occurs at the same time as the fault that triggered it appears in
the historian's measurements. A switchpoint state change is visible in the feeder's current measurements (a
sudden drop in current when a switchpoint opens).

A timing anomaly is a recorded transition with nothing physical under it: a relay trip the historian shows no fault for,
a switchpoint open with no drop in current. Either the report is false or the log was.

Similarly, the timestamp of a state transition is observable. If a state transition is recorded with a timestamp that is
out of order (a transition at 10:00 UTC is followed by a transition at 09:50 UTC), the logs have inconsistent timestamps
or the later transition was backdated. This indicates either clock-synchronisation issues or deliberate manipulation of
event timestamps.

## State consistency across replicated systems

For critical assets, there may be redundant monitoring or control systems. A switchpoint's state is reported by the
RTU that controls it and by the SCADA that commands it, and potentially by multiple sensors. These independent systems
are expected to agree on the switchpoint's state.

If the SCADA shows a switchpoint is Closed but the RTU reports it is Open, and independent measurement of the actual
switchpoint (a technician at the site or a video feed) shows it is Open, then the SCADA's state report is false. This
false reporting could indicate a software bug, a misconfiguration, or deliberate falsification in the SCADA.

The consistency check is powerful because it is independent of the system being checked. Even if one system is
compromised, the other independent systems provide validation. If multiple systems diverge in their state reports for
the same asset, the divergence is the forensic signature that something is wrong.

Planned switching makes state changes common inside a maintenance window and rare outside it, so a transition with no
command behind it stands out most where the baseline is otherwise still.

*Last updated: 13 July 2026*
