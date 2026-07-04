# Running the drills

ISO 22301, Clause 8.5: exercise programme.

Plans that are never exercised often fail in real scenarios. The drill is where the emergency systems, the drill
book, and the people meet the weather from the storm charts, on a day chosen in advance: the stage that converts
a documented capability into a demonstrated one, and the main source of the effectiveness evidence the
[dossier](dossier.md) will need.

## An exercise ladder

Exercises scale in cost and in what they can reveal. A programme usually climbs:

* Walkthroughs: the team reads the procedure together. Cheap, and catches the procedure that references a decommissioned system or a departed colleague.
* Tabletops: a scenario unfolds and the team talks through decisions under mild time pressure. Reveals gaps in escalation chains, authority, and communication that a walkthrough cannot.
* Component tests: a controlled failover, a restoration from backup, a switch to generator power. Tests one continuity solution against its assumption.
* Simulations and live exercises: a scenario played out with real systems or a staging environment, including PoC or red team scenarios for cyber disruptions. The most expensive rung, and the only one that tests how the pieces work together.

Scenarios are drawn from the storm charts, rotating across threat categories so the same comfortable scenario is
not rehearsed annually while the others stay theoretical.

* Checks: Are drills and simulations conducted regularly? Are results documented and follow-up actions tracked? Does the schedule cover all threat categories over a defined cycle?
* Typical gaps: No test schedule, exercises not documented, lessons not applied to plans, the same scenario exercised every year.

## Deviations are the yield

When a control performs differently under exercise conditions than expected, that divergence is a model signal
rather than a failed drill. It reveals an assumption that does not match the operational environment: the
escalation path assumed someone was available who wasn't; the failover assumed a network path that was congested;
the recovery time objective assumed skills the team had not yet consolidated. Treating exercise deviations as
feedback rather than failures is what makes the testing cycle useful. An exercise report with no findings is more
likely to describe a gentle scenario than a resilient factory.

## Executive gap-spotting

* Coverage: Has every continuity solution been exercised against the threat category it exists for?
* Realism: Do scenarios approximate actual disruption conditions, including time pressure and absent key people?
* Follow-through: Are exercise findings tracked to corrective actions, and corrective actions to the next exercise?
* Freshness: Do cyber scenarios reflect current attack patterns rather than the ones from two years ago?

*If a continuity measure has never been exercised, what exists is a purchase and a document, not a capability.*

## Output

By the end of this stage, the organisation has an exercise programme with a schedule covering all threat
categories, documented exercise reports including deviations and near-misses, and a corrective action list feeding
[after the storm](after-the-storm.md). The reports themselves are effectiveness evidence for the dossier.

## Related

* [Gap analysis](../supportive/gap-analysis.md)
* [Unseen University Power & Light Co. IT/OCS pentest](https://red.tymyrddin.dev/docs/power/)
