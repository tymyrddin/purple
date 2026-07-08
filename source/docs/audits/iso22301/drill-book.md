# The drill book

ISO 22301, Clause 8.4: business continuity plans and procedures.

Strategies and equipment answer what the factory falls back on. The drill book answers who does what, in which
order, with whose authority, when the fallback is needed at three in the morning. Step-by-step procedures reduce
reaction time and errors during disruptions; their absence converts a manageable incident into an improvised one.

## Response structure

A disruption needs a team with the authority to act before the organisation chart catches up. The plan names who
assembles, under what activation thresholds, and who decides that the situation has crossed from operational
hiccup into continuity event. Vague activation criteria produce two familiar failures: teams assembling for
everything, or for nothing until it is late.

* Checks: Are activation thresholds defined? Are roles filled by named people with named deputies? Does the response team have decision authority documented in advance?
* Typical gaps: Plans that assume the person who wrote them is on shift, no deputy for the one role that authorises spending, activation criteria nobody can recite.

## Incident response and recovery procedures

Procedures cover the path from disruption through stabilisation to restored operation: immediate actions, damage
assessment, recovery steps for each critical function, and the return to normal working.

* Checks: Are procedures accessible and understood? Are responsibilities clearly assigned? Are escalation paths defined?
* Typical gaps: Outdated or missing procedures, unclear roles, incomplete escalation plans.

Accessibility is its own requirement. A recovery procedure stored only on the file server it is meant to help
recover has a circular dependency that gets discovered once.

## Communication plans

Coordinated communication supports timely decisions and reduces confusion.

* Checks: Are internal notifications, vendor communications, and executive reporting protocols documented? Are contact lists current and reachable when normal channels are down?
* Typical gaps: Unclear contact lists, missing escalation steps, inadequate communication for remote teams.

## The book and the floor

Recovery procedures and operational practices can diverge silently. A procedure written months ago may not
reflect how the team actually responds today: new staff, changed shift patterns, system upgrades that altered
dependencies. The procedure documents a model of how recovery works; when practice departs from it, the departure
is evidence that the model no longer fits. Validating procedures against current practice catches this before an
actual disruption does. [Running the drills](drills.md) is the scheduled way of forcing that validation.

## Executive gap-spotting

* Responsibility clarity: Is every procedure, system, and recovery action assigned to a named role?
* Activation clarity: Could the on-shift team say, without looking it up, what triggers the plan?
* Accessibility: Are current copies of plans reachable during the disruptions they are written for?
* Communication readiness: Can stakeholders be informed and coordinated efficiently in a disruption?

## Output

By the end of this stage, the organisation has documented continuity plans covering all critical functions,
a response structure with named roles, deputies, and activation thresholds, escalation paths, communication
protocols with current contact lists, and copies of all of it accessible under the conditions it is written for.

## Related

* [NIS2 Navigating hazards](../../audits/nis2/hazards.md)
* [Gap analysis](../supportive/gap-analysis.md)
* [Unseen University Power & Light Co. IT/OCS pentest](https://red.tymyrddin.dev/docs/power/)

*Last updated: 4 July 2026*
