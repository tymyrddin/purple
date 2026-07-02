# Continuity through a foundations lens

The foundations material in this volume offers four lenses that change what is visible in
continuity work. Used together, they produce a more honest picture than the BCMS standards do
on their own, and they account for the human and political dynamics that turn a technically
sound plan into a binder that fails on the day.

## SEM: the plan is a model

A continuity plan is a model of an organisation. Like all models, it is likely to be wrong in
specific ways. The interesting questions are which ways, and how recently anyone checked.

Models drift faster than continuity documents update. The plan that described an organisation
accurately at the last revision may no longer describe the organisation that exists now.
Services moved to SaaS. Teams reorganised. The principal architect left. Two key processes
were silently merged. A vendor was replaced. The plan still reads correctly. It just no longer
corresponds to anything in particular.

Recurring "lessons learned" from exercises that never reach the plan can be read as evidence
that the model is wrong in a way the system keeps trying to correct and the document does not.
The remedy may not be a more thorough exercise. It may be updating the model the document
encodes, and treating exercise findings as model failures rather than commentary.

A SEM question for a continuity plan: when was the last time each load-bearing assumption in
this document was validated against operational reality, and which of those assumptions, if
wrong, would invalidate the rest of the plan?

## PSL: rational, emotional, political

Continuity is a rational subject in theory and a political one in practice.

Rational: which dependencies, which RTOs, which procedures, which test schedules. This is the
layer the document is written in.

Emotional: who is afraid of being blamed if the plan fails, who has stopped believing the
exercise is real, who has quietly decided that none of this will work and is making private
arrangements. The emotional layer is rarely written down, but it determines whether the plan
is exercised honestly or theatrically.

Political: which functions get prioritised in degraded mode, whose work is "essential", whose
office is the recovery centre and whose office is not, who gets brought into the crisis
management team and who is told later. These decisions are framed as operational and read by
the organisation as status. A reorganisation conducted under continuity branding is still a
reorganisation.

A continuity plan that addresses only the rational dimension is likely to be undone by the
other two on the day it is needed. The political fights about prioritisation that did not
happen during planning may surface during the incident instead, at the worst possible time,
with the worst possible information.

## ChangeShop: rehearsals are diagnostic

The most useful continuity exercise is not the one that confirms the plan works. It is the one
that produces honest data about where the plan does not work. Organisations resist the second
kind because the data is uncomfortable, and because the people responsible for the plan have
incentives to show it succeeding.

A live rehearsal that reveals half the runbooks are out of date, the on-call rotation has
gaps, the comms tree depends on a phone number that has not been valid for a year, and the
authorisation chain assumes someone whose role no longer exists, is producing exactly the
information the organisation may need. Treating this as a failure of the rehearsal rather
than a finding from it can be read as the homeostatic response: the system preserving the
model the rehearsal threatened.

A ChangeShop-informed continuity programme designs exercises to surface uncomfortable
findings rather than demonstrate readiness. A useful criterion of a good exercise may not be
"did the plan work" but "did we learn something we did not already know". Exercises that
produce nothing surprising are often exercises that have been scoped to be safe.

## Satir: stress reverts people to stances

Under disaster conditions, people revert to survival stances. Placating, to keep the peace at
the cost of honesty. Blaming, to direct fault outward. Computing, to retreat into procedure
and avoid feeling. Distracting, to disengage entirely.

These are not character flaws. They are predictable responses to threat, and they are
extremely common in the conditions a continuity plan is written for. A plan that assumes
people will behave as the procedure describes is assuming a calm that does not exist in
disaster conditions.

The plan benefits from anticipating this. Roles assigned to people who lean toward placating
under pressure are unlikely to surface bad news in time, and the comms can look smoother than
the situation warrants. Comms positions filled by people who default to computing may produce
procedurally correct updates that are operationally useless. Decision authority that lands on
someone whose stance under stress is to distract may simply not be exercised, and the
disaster can run unmanaged for whatever interval that lasts.

A Satir-informed question for any role in the plan: under stress, what does this person tend
to do, and is the role compatible with that? The answer affects how the role gets filled, who
the deputy is, and how the structure tolerates the stance the named person is likely to adopt.

## The integrated programme

A continuity programme that takes these lenses seriously can look quite different from a
binder. It is worth including:

- rehearsals designed to produce uncomfortable findings, and a culture that treats those
  findings as the point rather than the embarrassment
- an explicit acknowledgement of the political dimension of recovery prioritisation, written
  down before the incident rather than improvised during it
- roles assigned with stress response in mind, not with org-chart elegance in mind
- a model maintained as a living artefact, with named owners for the assumptions, and a
  schedule for revalidating each one

The result is closer to a continuity capability than a continuity document. The two are
frequently mistaken for each other. The document is what gets photocopied for the audit. The
capability is what holds when the building floods.

## Related

- [Applying SEM to security](../foundations/system-effectiveness/applying-sem.md)
- [PSL in security work](../foundations/problem-solving/in-security.md)
- [Integrating PSL, ChangeShop, SEM, and Satir OD](../foundations/organisational-development/composite-model.md)
- [What ChangeShop is](../foundations/change-management/what-it-is.md)
- [What happens Monday morning](monday-morning.md)