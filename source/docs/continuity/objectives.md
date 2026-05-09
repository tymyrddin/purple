# Recovery objectives and what they actually mean

RTO, RPO, MTPD, and MBCO are quoted often and questioned rarely. The numbers attached to them
tend to drift away from operational reality on a quiet, predictable schedule.

## The four numbers

Recovery Time Objective (RTO): how long before the activity is restored.

Recovery Point Objective (RPO): how much data loss is tolerable.

Maximum Tolerable Period of Disruption (MTPD): how long the organisation can live without the
activity at all before the consequences become unrecoverable.

Minimum Business Continuity Objective (MBCO): the reduced level of service that can be
sustained during disruption, as distinct from the full level that DR is trying to restore.

RTO and RPO describe the recovery; MTPD describes the limit beyond which recovery is no longer the point; MBCO
describes what life looks like in between. Most plans capture the first two, mention the third, and skip the fourth.

## How the numbers tend to be set

The values attached to these objectives are sometimes:

- the answer the business owner gave the consultant who asked
- the answer that fits the contract that has already been signed
- the answer that does not require the IT budget to grow
- the answer that someone else's plan used, copied across without revisiting

Few of these are derived from operational reality. A useful test of the numbers is whether
anyone has rehearsed against them. An RTO of four hours that has never been measured against
actual restore time is closer to a wish than a target.

## The trouble with one number

Different activities have different RTOs depending on when they fail. A four-hour RTO for
payroll is fine in week one of the month and ruinous on the day before payday. A four-hour RTO
for a customer-facing portal is fine on a quiet Tuesday and existential during a release
window.

Time-of-day, time-of-month, and time-of-year context can usefully sit in the objective, or at
least in a note next to it. A continuity plan that omits this risks becoming a model
simplified into uselessness, because it produces the same response regardless of when the
incident lands.

## The communication clock

The objectives describe technical and operational targets. They rarely describe communication
targets. The window during which an organisation has to make a public statement, notify
regulators, brief staff, or update customers is its own clock, and it often expires faster
than the technical RTO. Restoring the database can be necessary without being sufficient.

The objectives also tend to be silent on the dependency side. An RTO of four hours for
activity A is meaningless if activity A depends on activity B, and B has an RTO of twelve
hours. The composite RTO for the chain is twelve hours, and that is the number an
organisation will actually experience. Plans that quote per-activity RTOs without composing
them along the dependency graph are usually quoting fiction.

## The honest version

A useful set of objectives includes the number, the conditions under which it was set, the
date it was last validated, the test that validated it, and the dependency context in which it
applies. That is more text than fits on a slide, which is part of why most published
objectives are shorter than the work would justify.

## Related

- [Operational dependency mapping](dependencies.md)
- [Degraded operations](degraded.md)
- [Risk assessment](../risk-management/risk-assessment.md)
- [Choreography of risk to operations](../risk-management/to-operations.md)