# The design as a training tool

Wrapped in a generated incident, the same machinery becomes an exercise. Where the audit tool reads
capability off the architecture, the training tool puts a person in front of a record and asks them to make
the Article 23 call under something close to the real constraint.

## The generator

The generator is the [feasibility](feasibility.md) residue generator, extended. It builds an ordinary week at
the estate first: routine switching, scheduled maintenance, telemetry, work orders opened and closed, the
normal rate of the small disorders the [core-design page](evidentiary-capability-core-design.md) treats as
substrate. Where real recorded traces can be had, anonymised historian extracts or a week of captures, the
ordinary week is drawn from them rather than invented, so only the incident laid on top is synthetic and
there is less manufactured record to distrust. Onto that week it injects a ground truth, an actual
explanation for the incident, drawn from the enumerated set (a genuine fault, an emergency verbal approval, a
late maintenance window, a defect, a forged command, an attacker who dressed the incident in forged benign
evidence). The causal grammar walks the residue outward from that ground truth exactly as feasibility
describes, and the emitters serialise it into the same artefacts a real estate would hold. A critic then
checks that the assembled record is internally coherent, that the injected incident leaves no tell a benign
week never would, before the emitters commit it. The stronger form of that critic is an adversarial
discriminator, a model set to separate synthetic records from real ones at the observable layer, or a panel
of analysts run blind, and the generator is iterated until neither can tell the two apart. That turns "no
tell" from an assertion into something measured: if a discriminator can spot the synthesis, so can the
analyst being trained, and the exercise is not ready.

The result is a body of evidence in which one explanation is true by construction and the analyst does not
know which.

## The exercise

A single analyst sits with the generated record for something on the order of an hour and files the
determination the law asks for: is malice suspected, yes, no, or unknown. They work through a query interface
onto the record, and the interface is deliberately tedious, because the tedium is part of what is being
measured. Pulling the relay sequence-of-events, cross-checking it against the historian and the work-order
system, noticing that the badge log for the substation is not retrievable before Monday: the friction and the
retrieval cost are the conditions the twenty-four hour clock imposes, and an exercise that hands the analyst
a clean, instant, complete record measures nothing the real determination will face.

The deliverable is the Article 23(4)(a) early warning: a suspected-malice flag with its reasoning, produced
under the clock. It is the act the audit tool cannot perform and does not try to.

## The reveal

Afterwards the ground truth is disclosed, and with it two rankings: the full set of residue the incident
actually generated, and the subset the analyst managed to retrieve. The gap between them is the teaching. It
shows which artefacts existed and went unpulled, which were unretrievable in time, and which never existed at
all.

The reveal has to do one thing carefully, or it teaches the wrong lesson. For an incident that is undecidable
by construction, where the estate genuinely never held the diverging artefact, the correct answer is
"unknown", and a well-calibrated "unknown" is a success, not a miss. The reveal validates it as such. An
exercise that scored every "unknown" as a failure would train analysts to manufacture confidence the record
cannot support, which is the opposite of what the Article 23 bar, with its permitted "unknown", is asking
for. The honest finding that malice cannot be told from its legitimate twin at this estate is a finding, as
feasibility puts it, rather than a failure.

The reveal also carries the lesson the [core design](evidentiary-capability-core-design.md) builds in about
trusting evidence. Part of reading a record honestly is noticing which artefacts are independent of the actor
under suspicion and which that actor could have written, and not resting a determination on a single clean
source when an out-of-band one disagrees. The observable-semantics material the record is drawn from already
turns on this, the capture that is independent of the logs, the paper logbook that outlasted the platform, so
an exercise built on it can reward the analyst who cross-checks and distrusts the too-tidy record, which is
exactly the instinct a forged-benign incident would demand. That scenario is decidable only when the estate
holds a record beyond the attacker's reach, so it exercises precisely what the capability report grades,
whether the separating evidence is independent or merely forgeable.

The exercise record is reproducible: the same ordinary week, ground truth, and seed regenerate the same
incident, so a cohort can be run against one scenario and compared, and a remediated estate can be
re-exercised against the incident that previously defeated it.

*Last updated: 12 July 2026*
