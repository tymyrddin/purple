# Reading across the record

No single record settles anything, so the evidence is read across the classes, the SCADA journal against the relay's
records, the historian, the meter, the gas station, the phone call. What the whole reading rests on is worth setting
down.

## Independence is what a record is worth

A claim is only as strong as the independence of the records that agree on it. The [SCADA
journal](control-and-command-execution/scada-observables.md) is the control room's own account, tool-mediated and
editable; the [relay's sequence-of-events and disturbance
capture](field-devices-and-protection/protection-relay-state.md) sit on separate devices and network segments; the
physical state, a breaker's mechanical counter, a slam-shut valve's latched position, a meter read against the load, a
customer's report of gas smelled, sits outside every system. They line up in ordinary operation. When they diverge, the
divergence is the signature, and where it sits tells how hard it was to produce: the more independent records a false
claim has to stay coherent across, the larger the footprint forging it leaves. A change that shows only in the editable
journal is cheap; one that would also have to rewrite a relay's own capture, a field device's log, and a physical
counter is not.

Every page is a special case of that move: the [historian against the relay's
COMTRADE](measurements-and-data-records/historian-patterns.md), the [meter against the network
measurement](measurements-and-data-records/metre-data-semantics.md), the [gas station's telemetry against its latched
safety valve](gas-network-evidence/station-telemetry.md), the [verbal approval against the meldpunt's
roster](access-and-authorisation/telephony-and-verbal-authority.md). The records differ by class; the move does not. And
in each the same shape recurs, a benign twin and a hostile one that leave the same residue, told apart not by the
residue but by the record around it, the work order, the roster, the plan, the baseline it no longer matches. An estate
that cannot tell the twins apart cannot answer the question the [law asks](../evidentiary-capability.md), however much
it logs.

## Read against the class, not a common baseline

Two things vary the reading from class to class. First, how loud the baseline is: a [relay trips once or twice a
year](field-devices-and-protection/protection-relay-state.md), so one unexplained entry carries weight, while [alarms
run to hundreds a day](control-and-command-execution/alarm-and-event-logs.md), so only a pattern does. Second, whether a
gap indicts: an append-only log's break, a [missing COMTRADE](field-devices-and-protection/disturbance-and-fault-records.md),
a register that no longer matches the ground are strong signatures, but absence is also the commonest innocent state, a
dropped mobile link, an overdue check, so a gap tells only when it lines up with something else against a baseline
otherwise full.

## What the whole reading needs

So the record tells malice from its legitimate twin only when four things hold at once. The signature discriminates:
read against the class's own baseline, its presence or absence actually separates the explanations rather than sitting
inside the ordinary noise. The records that carry it are independent, not copies of one editable source. The signature is
present, or its absence lines up with corroboration. And the evidence is [obtainable inside the clock](obtainability.md).
Any one missing, and the honest answer is the one the law permits, unknown, reached not because nothing happened but
because the record could not be made to say.

*Last updated: 14 July 2026*
