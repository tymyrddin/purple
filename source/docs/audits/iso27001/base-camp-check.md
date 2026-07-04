# Base camp checks

![Base Camp](/_static/images/basecamp.png)

ISO/IEC 27001, Clause 9: monitoring and measurement, internal audit, and management review.

The [climb has been steady](climb.md): the ISMS implemented and operating. Before attempting the final summit
push, the external certification audit, base camp is where the expedition pauses, assesses, and makes sure
everything works as intended. This is the performance evaluation phase: the opportunity to find and fix
problems before an external auditor points them out with a raised eyebrow. A dress rehearsal before opening
night.

## Monitoring and measurement

Clause 9.1 asks for continuous checking that the ISMS works as intended: ropes, equipment, and supplies
inspected regularly rather than after the rope snaps. Monitoring covers the security objectives (is the
phishing click rate actually below the target), process effectiveness (are access reviews actually happening
quarterly), control effectiveness (do controls prevent, detect, and correct as intended), and compliance with
legal, regulatory, and contractual obligations.

Indicators work when they are specific, measurable, and time-bound. "Improve security awareness" measures
nothing; "95% completion of annual training by Q4" measures delivery, and pairs with an effectiveness
indicator like the click-rate trend that says whether the training changed anything. Each metric wants a
definition of what is measured, how, when, by whom, from what baseline, toward what target, and unrealistic
indicators create frustration and false data rather than insight. Results, analysis, and the actions taken get
documented: the evidence that security is not just implemented but verified.

## The internal audit programme

Clause 9.2 requires a planned internal audit programme: a structured, independent examination verifying that
controls are implemented as the Statement of Applicability says, that processes work in practice and not just
on paper, and that nonconformities get found and addressed. A practice run before the real audit, on the
organisation's own terms, with time to fix what turns up.

Internal audits can include running test scenarios against controls rather than only reviewing documentation:
verifying that an alert fires when expected, running a phishing simulation to check whether awareness has
actually changed behaviour, or testing whether backup restoration succeeds under realistic conditions. These
produce effectiveness evidence that document review alone cannot. The question is not only whether the control
is in place but whether it still does what the model assumed it would do.

The programme's mechanics: frequency weighted by risk (critical and recently changed areas more often, stable
areas annually, everything covered across the cycle), scope splittable into several smaller audits, auditors
who are impartial (nobody audits their own work) and understand both ISO 27001 and this ISMS, and findings
reported to management with conformities as well as nonconformities.

## Sanity check before the summit

Three things deserve particular attention during the pause at base camp.

Are ropes frayed? [Process drift](../../foundations/system-effectiveness/for-defence.md): practice departing
from documentation. The policy says 90-day password changes, the system says 180. The procedure says quarterly
reviews, the calendar says annual. The response plan lists contacts who left last year. Practice that does not
match documentation is nonconformity against the organisation's own ISMS, and auditors find it immediately.

Drift is a model failure before it is a compliance failure. The documentation describes the system as it was
understood to work; the behaviour describes it as it actually works; the question worth asking is which is
more accurate. If the behaviour, update the documentation. If the documentation, investigate why the
environment resists the procedure. A process that consistently drifts in one direction is evidence that the
documented approach does not fit the operational context, not that individuals are failing to comply.

Are logs missing? Evidence gaps: access review records, training logs, incident documentation, management
review minutes, change approvals, backup verifications. The red flags auditors know by heart: "we do it but
don't document it", "it's on Sarah's laptop", "we used to track this but stopped", documents with no dates,
versions, or authors. If it cannot be proven, in audit terms it did not happen; the fix is rarely complicated,
records just need to exist and be findable.

Is anyone off-route? Nonconformities, in three weights:

* Major: a critical requirement not met, such as no risk assessment in twelve months, a required control simply absent, or a previous finding ignored across audits. Certification does not survive these unresolved.
* Minor: a partial or isolated failure, one missed review, a control not quite as described.
* Observation: not a nonconformity yet, but headed there if unattended.

Audits are not about blame; they are about finding weak spots while the finding is still cheap.

## Recording and correcting

Findings become nonconformity reports: what was found, where, why it counts, the evidence, the severity, the
planned fix with an owner and a date, and how closure will be verified.

Correction and corrective action are different things, and ISO 27001 wants both. Correction fixes the symptom:
repair the frayed rope, restore the failed backup. Corrective action addresses the cause: the inspection
schedule, the monitoring with assigned ownership. Correction stops the bleeding; corrective action prevents
the wound.

There is a third level that the first two can miss: model correction. If the underlying belief is "backup
responsibility is clear and someone is watching it", that belief will produce the same gap under different
circumstances, whatever the corrective action fixed. Model correction asks what the organisation believed
about this process that allowed the failure to seem impossible until it happened.

The diagnostic signal is a corrective action that passes verification and then reappears as the same finding
in the next audit cycle. The surface condition was addressed; the model was not.

A practical routing mechanism: before closing any corrective action, check whether a finding of the same class
has appeared before. When a finding returns after verification, open a model review instead of another
corrective action, with one question: what does the organisation currently believe about the conditions under
which this control operates, and is that belief still accurate?

Audit results over time show whether the ISMS is maturing:

* Reactive: the same findings recurring every cycle, corrective actions taking six months, results surprising management.
* Proactive: finding counts falling, actions closed within a quarter, internal audits catching issues before external ones.
* Adaptive: mostly observations, quick response to change, learning from near-misses and not just incidents.

The trend is a better readiness signal than any single audit.

## Management review

Clause 9.3 is where leadership steps back and assesses the ISMS strategically: not a technical deep-dive but a
business-level evaluation of whether it remains adequate, effective, and aligned with where the organisation
is going. The inputs are prescribed: status of actions from previous reviews, changes in external and internal
issues, performance trends (nonconformities, monitoring results, audit findings, objective fulfilment),
feedback from interested parties, risk assessment status, and improvement opportunities.

The outputs are decisions, documented: what gets improved, what changes in the ISMS, and what resources are
committed. A review that produces minutes but no decisions has received the inputs, not reviewed them.

Annually is the floor; quarterly suits a maturing ISMS or a period of change. Attendance means top management
as the scope defines it, not delegates without decision authority.

## Output

Leaving base camp, the ISMS is monitored with metrics and trends, audited internally with corrective actions
closed or credibly in progress, reviewed by a management that made decisions, documented in a way that answers
requests quickly, and honest with itself about its maturity. Internal audits are the dress rehearsal; the
external audit is opening night, and the problems are meant to be worked out during rehearsal. The claim being
carried up the mountain is not perfection. It is control, awareness, commitment to improvement, and evidence
that the ISMS works, which is exactly what [the summit push](summit.md) will test.

## Related

* [NIS2 Reaching the far bank](../nis2/bank.md)
* [ISO 22301 The resilience dossier](../iso22301/dossier.md)
* [IEC 62443 The inspection](../iec62443/inspection.md)
* [Evidence](../supportive/evidence.md)
* [Corrective action](../supportive/corrective-action.md)
* [Gap analysis](../supportive/gap-analysis.md)
* [Applying SEM to security](../../foundations/system-effectiveness/applying-sem.md)
