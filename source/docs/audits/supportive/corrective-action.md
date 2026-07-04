# Corrective action

Audit findings, incident reviews, exercise deviations, and monitoring alerts all end in the same machinery: a
list of things to fix and a process for fixing them. The machinery looks administrative and decides more than
it appears to, because it is where the difference lives between an organisation that closes findings and one
that learns. The playbooks in this section rehearse the pattern stage by stage; this page is its home.

## Three levels of fixing

Correction addresses the surface condition. The failed backup is restored, the stale contact list updated, the
missing record produced. It stops the bleeding and changes nothing about tomorrow.

Corrective action addresses the cause. Why the backup failure went unnoticed: monitoring is implemented and
ownership assigned. Why the contact list went stale: the process that maintains it gets an owner and a
schedule. ISO/IEC 27001:2022 Clause 10.2 formally requires both of these levels, and external auditors check
that closed actions carry evidence of the second, not only the first.

Model correction is the third level, and the one the first two can miss. Every control operates on a belief
about its conditions: "backup responsibility is clear and someone is watching it", "access decisions follow
the approval workflow", "the escalation contact is reachable". If that belief is wrong, corrective actions
built on top of it fix instances while the belief keeps manufacturing new ones. Model correction asks what the
organisation believed about this process that allowed the failure to seem impossible until it happened, and
checks that belief against current reality. The answer is corrected at the design level, not the procedural
one.

## The lifecycle

A corrective action that will actually close has its conditions set at the start; the
[response-that-sticks conditions](findings-reporting.md) are a named owner, a realistic scope, an achievable
timeline, and a clear evidence requirement. From there the lifecycle is short:

* Open: finding reference, level of fix intended, owner, target date, and what evidence will demonstrate closure.
* Implement: the work, with the correction and the corrective action tracked separately when both apply.
* Verify: against a repeated test where one exists. A backup fix is verified by a restoration, an access review fix by the next review finding and removing something, a detection fix by the alert firing in a re-run scenario. Verification by document update is the weakest form, and verification by the person who implemented the fix is not verification.
* Close: with the evidence attached, into the [evidence base](evidence.md), where it doubles as proof the management system responds to what it finds.

## The recurrence signal

The diagnostic that routes between levels is recurrence. A corrective action that passes verification and then
reappears as the same finding in a later cycle is not evidence of carelessness; it is evidence that the
surface condition was addressed and the model was not.

The routing mechanism is cheap to run:

* Before closing any corrective action, check whether a finding of the same class has appeared before. If it has, note which assumption the previous fix left intact.
* When a finding returns after verified closure, open a model review instead of another corrective action. The model review has one question: what does the organisation currently believe about the conditions under which this control operates, and is that belief still accurate?
* The review has two outcomes. The belief is confirmed, which points to an execution failure and back to an ordinary corrective action. Or the belief no longer fits reality, which points to a design-level change: a different control, a different owner structure, a different assumption written down where the old one was.

Recurring findings clustered in one area carry a second-order signal worth reading before assigning blame: the
cost of fixing may fall on a team that does not benefit from the fix, which is a
[political constraint, not a technical one](../../foundations/problem-solving/three-domains.md).

## One log, many sources

The pattern applies wherever findings come from, which is an argument for one log rather than several:
external audit findings, internal audit results, incident and near-miss actions, exercise deviations, and
monitoring findings all age the same way and hide recurrence from each other when tracked apart. A workable
log carries:

| Field                | What it captures                                                       |
|:---------------------|:------------------------------------------------------------------------|
| Reference and source | Which audit, incident, exercise, or review produced it                 |
| Finding class        | The category used for spotting recurrence across sources               |
| Level applied        | Correction, corrective action, or model correction                     |
| Owner and dates      | Who owns it, opened when, due when, closed when                        |
| Verification         | Method (retest, re-run exercise, sample check) and result              |
| Recurrence marker    | Prior findings of the same class, if any                               |

The finding class column is what makes the log more than a task list. Recurrence is invisible when every
finding gets a fresh description; it is obvious when this year's entry shares a class with two closed ones.

## Failure modes

* Closure by documentation: the procedure is updated, the gap is untouched, and the next audit assesses the repeat more severely.
* The treadmill: finding closure becomes the security programme's operating rhythm and the audit calendar becomes its planning calendar. [Audit as compass](../compass.md) covers the executive view of this one.
* Perpetual progress: actions that sit at eighty per cent across review periods. A stalled action that was agreed and resourced usually signals a political or emotional constraint rather than a technical one.
* The pre-audit purge: bulk closure in the weeks before an external visit, which produces exactly the date cluster auditors read as theatre.

## Related

* [Audit findings and reporting](findings-reporting.md)
* [Evidence](evidence.md)
* [Gap analysis](gap-analysis.md)
* [Audit as compass](../compass.md)
* [ISO 27001 Base camp checks](../iso27001/base-camp-check.md)
* [ISO 22301 After the storm](../iso22301/after-the-storm.md)
* [How models age](../../foundations/system-effectiveness/for-defence.md)
