# Documentation

Good documentation enables learning and provides a basis for accountability. The two functions are in tension if they are not handled carefully: documentation that is primarily an accountability record shapes what people choose to write, and the result is safe rather than honest.

[SEM's framing](../foundations/system-effectiveness/core-triad.md) is useful here. The most valuable thing to document in an engagement is not just what happened, but what the organisation believed before it happened and what changed. A timeline of events with no record of the assumptions being tested is a sequence without an explanation. The next engagement will test slightly different events against the same unexamined assumptions, and the findings will look similar.

The problem with "lessons learned" documentation is the same problem [post-incident reviews](../incident-response/playbooks/index.rst) surface. Without the right conditions, lessons learned produces safe summaries: procedural improvements that nobody can argue with, and no examination of the structural conditions that produced the original gap. The documentation format is not the cause; the conditions under which it is produced are.

## Before the engagement

Document the engagement plan: objectives, scope, rules of engagement, timeline, participants, and success criteria. Document the authorisation. Document what the organisation currently believes about the capabilities being tested. This last item is rarely included and is the most valuable: it creates a baseline against which the findings can be measured as model corrections, not just event records.

## During the engagement

The testing team logs every action with a timestamp: what was attempted, what succeeded, what did not, and what was surprising. Not just "executed technique X" but "executed technique X at 14:32, expected alert within 5 minutes, no alert observed for 23 minutes." The observations matter as much as the actions.

The defending team logs alerts, decisions, and reasoning: when something was noticed, what the investigation found, what was decided and why, and what was not noticed and why. The gaps in the log are as important as the entries.

The facilitator tracks the overall timeline, notes where the two teams diverged from expectations, and captures questions for the debrief.

## After the engagement

The technical report documents findings, techniques used, detection gaps, and evidence. The executive summary translates this into business risk and improvement priorities, without losing the nuance that makes the technical findings actionable.

Action items need owners, timelines, and a distinction between procedural fixes and structural ones. Procedural fixes update a runbook or add a detection rule. Structural fixes change decision authority, visibility, or system design. If the action list is entirely procedural, the engagement found symptoms rather than causes.

## Related

- [Objectives](objectives.md)
- [Coordination and communication](coordination.md)
- [Post-incident reviews](../incident-response/playbooks/index.rst)
- [Systems, models, and errors](../foundations/system-effectiveness/core-triad.md)
