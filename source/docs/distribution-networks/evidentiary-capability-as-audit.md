# The design as an audit tool

Read statically, the identifiability computation is an audit. It takes an estate configuration and returns,
determination by determination, whether the architecture can support the malice-or-not call and how far the
supporting evidence can be trusted, each with the reason and, where there is one, a remediation.

## No incident, no analyst

The capability report makes no determination about any actual event, and it needs neither an incident nor an
analyst in the loop. That is not a limitation; it is the point. The report asks a question answered by the
shape of the record rather than by anything that happened: given only what this estate retains and can
retrieve inside the window, is it even possible to tell a malicious change from its legitimate twin? The
answer is fixed before any incident, and it is the same whoever is on shift, because when the diverging
residue was never recorded, or cannot be reached in the time the law allows, no analyst can recover it. A
perfectly capable investigator and a mediocre one are equally blind to an artefact that does not exist.

So the report reads determinations off the architecture. For each class of incident and each pair of
competing explanations, it states whether the estate could ever separate them, and where it could not, it
names the missing or unretrievable artefact as the reason. The finding is architectural rather than
behavioural, which is what makes it cheap to establish and, often, cheap to act on.

## Three grades, not a yes or no

The report does not answer a flat yes or no. For each determination it returns one of three grades, following
the [identifiability computation](evidentiary-capability-core-design.md). Supported: the estate retains,
independently of any suspect, a record that separates the malicious explanation from its benign twin.
Supported only on forgeable evidence: the separating record exists but sits somewhere the suspect could have
written, so a determination resting on it holds against an outside attacker and weakens against an insider
with that access. Unsupported: no separating record survives at all, and the determination is forced to
"unknown" whoever is on shift.

The middle grade is the one that earns its keep, because it is often cheap to lift. A determination resting
only on a forgeable record is remediated by adding one independent source beside it, a packet capture
retained, a badge log held out-of-band, an append-only export, so the same fact is witnessed somewhere the
suspect could not reach. The report names that fix the way it names a missing field or a short retention
window elsewhere.

## Where it sits against the obligation

The report does not discharge the Article 23(4)(a) determination. A person does that, during an incident, and
the [training page](evidentiary-capability-as-training.md) is about rehearsing exactly that act. What the
report does is tell an operator, in advance, which of those determinations the estate will force to "unknown"
regardless of who is looking or how hard they try. That is useful in two registers.

It is evidence for the Article 21(2)(f) duty, the requirement to have policies and procedures to assess
whether the risk-management measures are actually effective. A list of determinations the architecture cannot
support is a direct, checkable statement about effectiveness, produced without waiting for an incident to
expose the gap.

And it is a remediation driver. Some gaps close cheaply: a field added to a work-order form so the
emergency-exception approver is recorded, a retention window extended, a clock brought under discipline.
Others are expensive: moving contractors from a shared login to individual credentials is an identity
programme, not a form change, and the report names it as such rather than flattening every gap to the same
size. The value is knowing which determinations are unreachable while it is still peacetime, when a gap is a
design decision rather than a hole discovered at hour twenty-three of a real incident.

## The input is a real substrate

The report is computed over an ingested estate configuration, the structured description of the record set
out on the [core-design page](evidentiary-capability-core-design.md): systems of record, fields, retention
values, clock discipline, authorisation model, retrieval costs. The determinations are only as sound as that
description, so the honesty of the configuration is the real constraint, a point the
[risks page](evidentiary-capability-risks.md) does not let go of.

Operating context distils into the default estate configuration, a worked example the report can run against
out of the box rather than an abstract one. It is only a default: a real deployment supplies its own, and the
schema is meant to extend. Four fields operating context does not fix are carried as explicit unknowns rather
than invented: the retrieval cost and out-of-hours obtainability of each artefact, whether a work order
records the emergency-exception approver, whether contractor credentials are individual or shared, and a
consolidated set of base rates and competing explanations. These are deployment specifics a real estate keeps
[private](operating-context/system-composition/standards.md), so marking them unknown is honest rather than a
shortfall.

The precise schema the ingestion expects, field by field, is left to be pinned down as the direction is
built; the [feasibility page](feasibility.md) treats it as part of the buildable core.

*Last updated: 12 July 2026*
