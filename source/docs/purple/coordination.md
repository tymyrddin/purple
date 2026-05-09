# Coordination modes

A purple team exercise can run in several modes, distinguished by how much the defending side knows in advance. The
choice of mode shapes what the exercise can teach and what it cannot.

## Disclosed testing

In disclosed testing, the blue team knows the exercise is happening, roughly when it starts, and what general techniques
will be used. Communication runs in both directions throughout.

This is the mode with the lowest [organisational resistance](../foundations/change-management/what-it-is.md). Both sides
know what is happening, the scope is clear, and the findings land softly because everyone was prepared. It is also the
mode where an organisation learns the least about what could happen under realistic conditions, because the conditions
were never realistic.

Disclosed testing is useful for early exercises, for validating a specific detection rule, for training newer analysts,
and for testing a new defensive tool or procedure. The aim is learning the technique and the response, not testing the
surprise.

## Blind testing

In blind testing, the blue team knows that exercises happen on a regular cadence but does not know the timing or
scenario for any specific one. The red team's activity is revealed during or shortly after the exercise.

This mode tests something closer to operational behaviour without the risk that the blue team mistakes a test for a real
incident and triggers external escalation. It produces a more realistic reading of detection coverage, at the cost of
some confusion that has to be managed by clear communication channels and an agreed safe word.

## Double-blind testing

In double-blind testing, the blue team does not know that an exercise is happening at all. The red team operates
covertly. The exercise is revealed only at completion.

This is the mode that comes closest to testing actual detection and response capability. It is also the mode with the
highest risk: of inappropriate response, of operational disruption, of an analyst's professional reputation taking a hit
for missing something they were never told to expect.
The [chaos phase](../foundations/organisational-development/satir-change-model.md) that follows the reveal is real and
worth budgeting time for, not just announcing as a finding.

The conditions for this mode to produce learning rather than damage are stronger than for the others: a clearly defined
scope, a kill-switch arrangement, and a facilitator capable of holding the conversation when defensive reactions appear.
Without those conditions, double-blind testing surfaces organisational dysfunction more often than detection gaps, which
is informative in its own way but rarely the intended outcome.

## Continuous purple teaming

In continuous purple teaming, the offensive and defensive sides operate together on an ongoing basis. The red team feeds
scenarios continuously, the blue team continuously tunes detections, and automated testing validates coverage between
exercises.

This is the mode with the fastest improvement cycle and the highest tooling cost. It is mostly available to
organisations that already have dedicated red and blue functions, automation infrastructure, and a cultural acceptance
of being continuously challenged. Without those conditions, the volume of activity produces alert fatigue rather than
capability.

## Choosing a mode

The default progression in most programmes is from disclosed to blind to double-blind, with continuous arriving when the
resources and culture allow it. The progression is not mandatory: some organisations remain in disclosed mode for years
and produce excellent results, because the conditions there support the learning the rest of the programme depends on.
Others reach for double-blind too early and produce expensive findings the organisation is not yet equipped to act on.

The choice is not primarily a question of sophistication. It is a question of what the programme can support, both
technically and culturally. The [conditions document](conditions.md) goes further into what determines this.

## Related

- [Building your purple team](team.md)
- [Measurements and early success](practice/measurements.md)
- [Purple team coordination models](purple-team/coordination.md)
- [SOC detection and response](../incident-response/soc/detection.md)
