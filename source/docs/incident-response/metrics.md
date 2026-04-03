# Measuring what exercises reveal

Metrics from incident exercises are not a scorecard. They are model tests. Each number is a hypothesis about the organisation's capability, and the interesting question is not whether the number improved but what it reveals about the model that produced it.

## What to measure during the exercise

Time is the most immediate and least ambiguous signal. Time to detection, time to the first containment decision, time to implementation of that decision. These do not require interpretation: the clock ran, or it did not.

Communication touchpoints matter alongside the timings. How many escalations occurred? When did the communications function enter the response loop relative to the technical one? At what point did an incident commander make a decision versus waiting for consensus? These patterns reveal the authority and coordination structure the team is actually operating with, which may differ substantially from the documented one.

The facilitator tracks key decision moments with timestamps: when the team recognised the nature of the incident, when they escalated, when they changed approach. These become the skeleton of the debrief.

## What to assess after the exercise

The numbers are the easier part. The harder assessment is qualitative, and it comes from the debrief rather than the log.

Did the team prioritise correctly, and do they know why they prioritised as they did? Correct prioritisation under pressure that the team cannot explain is a fragile capability: it worked this time, but the team does not have the model that would let them transfer it to a different scenario. Incorrect prioritisation that the team can diagnose means the model is visible and improvable.

Was coordination between functions genuine or procedural? A communications lead who receives updates but does not shape decisions has been looped in without being integrated. The difference shows up in the exercise: when external communications pressure arrives, does the communications function have the situational picture to respond, or do they need to ask questions that would already have been answered had they been in the loop?

[Satir's framing](../foundations/organisational-development/satir-core.md) is useful here. An exercise where everyone performed their roles correctly but nobody named the decision that mattered has produced procedural compliance rather than capability. The debrief is where this becomes visible.

## Tracking improvement over time

Measure trends, not individual exercises. A single slow response may reflect unusual scenario complexity. Consistently slow detection-to-decision times point to a bottleneck in the process or the tooling that is worth investigating.

The more important trend is the nature of the improvements the exercise generates. [SEM describes this directly](../foundations/system-effectiveness/core-triad.md): if the organisation's model of its own incident response capability is accurate, improvements will be specific and targeted. If the model is wrong, improvements will address surface symptoms while the conditions that generate incidents remain unchanged.

A practical signal: if the action list after each exercise is mostly procedural (update a runbook, add a detection rule, send a reminder), the exercise is finding edge cases in the process. If some actions are structural (change decision authority, redesign escalation paths, alter team configuration), the exercise is reaching the conditions that produce the edge cases. Both are valid, but a programme that only ever produces procedural actions is not reaching the structural layer.

Recurrence is the most important metric of all. If the same class of failure returns across multiple exercises in slightly different forms, the programme is trimming symptoms. The conditions generating the failures are intact.

## Related

- [Facilitator guidance](facilitator-guidance.md)
- [Systems, models, and errors](../foundations/system-effectiveness/core-triad.md)
- [Documentation](../engagement/documentation.md)
