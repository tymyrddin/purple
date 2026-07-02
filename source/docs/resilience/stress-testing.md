# Stress-testing resilience

Continuity plans are written for a calm day and met by a loud one. Stress testing is the habit of
trying to break them on purpose, in a room with coffee rather than in the middle of a crisis, to find
out which parts hold.

A scenario is drawn from the organisation's own context: a ransomware outbreak during payroll, a key
supplier failing mid-project, a regulator arriving unannounced, the senior decision-maker unreachable
at the moment a decision is needed. A team works the event as it unfolds while a facilitator injects
complications to simulate the cascade, and observers note where it stalls, where confusion sets in, and
which dependencies prove most fragile.

## The evidence it produces

A stress test can produce compliance evidence as well as a learning afternoon. A recovery procedure that
met its time objective with current staffing is a claim a regulator, an auditor or a board can rely on.
A scenario that exposed a gap in the escalation chain is evidence that a control's model assumption had
drifted, and the corrective action that follows is a testable hypothesis for the next cycle. Run on a
recurring schedule, a single discovery becomes continuous verification: resilience the organisation can
demonstrate on any given day.

A payments company set a Friday-afternoon scenario: ransomware on the payroll host midway through a run.
The team reached the documented isolation step in four minutes and restored from an immutable snapshot
inside the two-hour objective, and that timed restore, with its logs, was the line the auditor accepted
the following month. The same afternoon surfaced that only one named person could authorise an emergency
payment rerun, with no delegate on record, which no policy had flagged.

For technical teams, a capture-the-flag exercise can serve the same function for operational competence.
Participants work structured incident scenarios with immediate feedback on whether their response
produced the intended effect. The format corrects itself: the incident is either contained or it runs
on, and the debrief surfaces exactly where the team's model of "how we respond to this" met something
the environment did differently. It is the same reading the [loop](../purple/running-the-loop.md)
performs when the defending side works live against an actual move.

## What the debrief keeps

The debrief harvests three things: what held up better than expected, where the team stumbled, and
which fixes are worth making before the next real incident. Captured in plain language and handed to
the people who ran the scenario, it is an action plan they own and can re-run. The value often sits in the
second run as much as the first, when the same scenario shows whether last round's fix survived
contact.
