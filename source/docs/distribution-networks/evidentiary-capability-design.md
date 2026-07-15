# A design on the evidence layer

The [observable-semantics](observable-semantics/index.rst) pages describe what a distribution estate's record holds,
class by class. An automation reading that record could measure, before any incident, whether the estate can tell a
malicious change from its legitimate twin, and rehearse the same judgement against a made-up one. It is one engine put to
two uses, and the striking thing is how little that engine has to be to earn either.

## Explanations that predict evidence

The move the whole thing rests on is small: treat an explanation as something that predicts evidence, not something
pinned on an incident after the fact.

A breaker opens out of hours. Several accounts could be true, and each predicts a particular spread of residue. A genuine
protection trip on a fault predicts a fault-passage indication, a relay pickup in the sequence-of-events, the breaker
transition and the alarm, and a disturbance capture of the fault waveform. A forged open command, injected at the control layer, predicts the
breaker transition and the alarm and nothing upstream of the point it touched. The two accounts separate exactly where
their predicted residue diverges, at the upstream fault artefacts: present, the record reads benign; absent, it reads
malicious.

So the question is never "what happened" in the abstract. It is whether the record can carry the diverging artefacts,
and carry them in a form worth trusting. That is a property of the record, fixed before the breaker ever moves, and it is
what the engine computes.

## The estate configuration

What the engine reads is not the live estate but a structured description of its record, an estate configuration. It names
the systems of record, the fields each holds, the retention window on each, the clock discipline across them, who was
authorised to act, the cost of retrieving each artefact under the twenty-four-hour clock, and, for each record, who can
write or alter it. [Operating context](operating-context/system-portrait.md) already assembles most of this for the
worked estate; the configuration is that material rendered as something a computation can read.

The write-authority field does the work the others cannot, and it is not the authorisation model wearing a different hat.
Authorisation says who could legitimately have acted. Write-authority says who could fabricate the record. The two come
apart precisely when the actor under suspicion is one with write access, which is the case that decides everything below.

## Four gates

For a pair of explanations, take each artefact either one would leave and put it to four questions. Follow
the disturbance capture from the breaker case:

- Discriminating. Does it actually differ between the two explanations? The fault trip predicts a capture; the injection
  predicts none. Fixed once, from the explanations themselves.
- Present. Does the estate retain it? Read off the retention field: whether the relay writes disturbance records and
  keeps them long enough to reach.
- Obtainable. Can it be pulled inside the window? Read off retrieval cost: whether the relay is reachable and someone out
  of hours can extract the capture before the clock runs out.
- Independent. Is it beyond the suspect's reach to have written? A capture on the relay is independent of a control-room
  operator, and not independent of someone who has rewritten the relay's firmware.

An artefact is decisive only if it clears all four. A determination is answerable if at least one diverging artefact
clears all four. That is the verdict in full: an AND across the gates for each artefact, then an OR across artefacts. One
clean witness is enough, and needing only one is what keeps the test realistic. Where the disturbance capture fails the
last gate against a firmware-level suspect, the engine looks instead for a diverging artefact that suspect could not
reach: the fault-passage indicator down the feeder, lit on a real fault and dark on a bare command; the RTU's own
spontaneous report on a separate device; or the physical marks of a fault a field crew either finds at the plant or does
not.

The present gate carries a subtlety the others do not. An artefact the estate never had the capacity to record is
unrecordable, and its absence means nothing. An artefact the estate would have held but did not is absent, and its
absence is evidence. Mistaking the second for the first manufactures false confidence: "the trip record is not there, so
no fault occurred" holds only if the estate would have kept the trip record had there been one.

## Unknown, and against whom

Two of the gates carry more than a yes or a no, and saying so is what makes the output honest.

Obtainability is three-valued: yes, no, or not yet known, because retrieval cost is the field a real estate most often
leaves open. An artefact that is discriminating, present and independent but of unknown obtainability returns not a false
"unsupported" but a "pending", the determination would hold if that figure were filled and stalls until it is. Unknown
sitting over an otherwise-clean artefact stays unknown; unknown over an artefact already failing elsewhere changes
nothing. Obtainability is not the only gate that can stall this way: any gate reading a field the configuration has not
filled returns pending, independence among them, when whether a suspect shares a login goes unrecorded.

Independence is relative to a named suspect. The gate takes an actor as its parameter, which dissolves the one grade that
never sat comfortably. A determination resting on a record only the relay's own firmware could forge holds against an
outside attacker and fails against an insider with that firmware access. That is not a mysterious middle grade; it is one
verdict read against two suspects. Capability is adversary-relative, and naming the adversary says so out loud.

So the engine returns three outcomes, each read against a named suspect. Supported: some diverging artefact clears all
four gates against that suspect. Unsupported: none does, whether because no artefact tells the two explanations apart at
all, because the residue was never recorded or cannot be reached whoever is looking, or because every artefact that
survives is one this suspect could have written. Pending: the
verdict waits on a configuration field the estate has not filled. The suspect is the parameter, not a fourth outcome:
the same record can be decisive against an outsider and useless against the insider who could have forged it, so a
determination is only ever supported or unsupported against someone.

## Entropy sits outside

Real estates do not run clean. Clocks drift and get nudged, a login is shared, a work order is closed on Monday for work
done on Saturday, a relay is left in test mode after commissioning. The [staffing
pressures](operating-context/staffing-and-capability/staffing-realities.md) and [contractor
arrangements](operating-context/operations-and-cadence/contractor-management.md) behind a real estate are not
incidental colour; they are the disorder every determination has to survive. A malicious change that hides inside the
ordinary rate of retroactive work orders is undetectable not because the evidence is missing but because the benign
explanation is always to hand at that estate.

That disorder has a place in the engine, but strictly outside the four gates. The gates answer whether the record can
distinguish the two explanations at all; the weighting answers how far a surviving artefact actually moves belief. Where
"no work order" is the ordinary state, its absence indicts almost nothing, so a determination can be structurally
supported and evidentially thin at once. Weighting by base rates would put a number on that thinness, but the rates are
not fixed by operating context and are hard to elicit honestly, so it stays [indicative rather than
load-bearing](evidentiary-capability-limits.md): it can hollow out a supported verdict without touching whether the
record could distinguish. Keeping it outside the gates quarantines the one part that needs numbers the design does not
have, rather than letting it colour the part that needs none.

## As an audit

Run the gates statically over the configuration, determination by determination, against the suspects that concern the
operator, and the output is a capability report. It makes no finding about any actual event and needs neither an incident
nor an analyst. That is the point rather than a limitation: the report asks a question answered by the shape of the
record, not by anything that happened, so its answer is fixed before any incident and reads the same whoever is on shift.
A capable investigator and a mediocre one are equally blind to an artefact that was never recorded.

The finding is architectural, which is what makes it cheap to act on. Where a determination comes back unsupported, or holds only against an outsider because its one separating record is
forgeable by an insider, the report names the missing or unreachable artefact as the reason, and often the
fix with it: a packet capture retained beside a forgeable log, a badge record held out of band, a retention window
extended, a retrieval cost brought down. Some gaps close with a form field; others, moving contractors off a shared login
onto individual credentials, are an identity programme rather than a form change, and the report names them at their real
size instead of flattening every gap to one. Knowing which determinations the estate cannot support while it is still
peacetime is the kind of direct, checkable statement the effectiveness duty under NIS2 Article
21(2)(f) asks for, produced without waiting for an incident to expose the gap. All of it
rests on the configuration being honest about what the record holds, which is the real adoption cost: no computation can
tell a truthful configuration from a flattering one.

## As a training exercise

Wrap the same engine in a made-up incident and it becomes an exercise. The [residue generator](feasibility.md) builds an
ordinary week at the estate first, routine switching, scheduled maintenance, telemetry, work orders opened and closed,
the small disorders that are the substrate, and where real anonymised traces can be had it draws the week from them
rather than inventing it, so only the incident laid on top is synthetic. Onto that week it injects a ground truth, one
explanation made true by construction, and walks the residue outward from it into the same artefacts a real estate would
hold. A critic checks the assembled record is coherent, and its stronger form is an adversarial discriminator, a model or
a blind panel set to separate synthetic records from real ones, run until neither can. If a discriminator can spot the
synthesis, so can the analyst being trained, and the exercise is not ready.

A single analyst then sits with the record for about an hour and files the determination the law asks for: is malice
suspected, yes, no, or unknown. The query interface is deliberately tedious, because the tedium is the point, pulling the
relay sequence-of-events, cross-checking it against the historian and the work-order system, finding that the substation
badge log is not retrievable before Monday. The friction and the retrieval cost are the conditions the twenty-four-hour
clock imposes, and the deliverable is the [Article 23(4)(a)](evidentiary-capability.md) early warning produced under
them, the act the audit half cannot perform and does not try to.

Afterwards the ground truth is disclosed, with two rankings: the residue the incident actually generated, and the subset
the analyst managed to retrieve. The gap between them is the teaching. It shows which artefacts existed and went unpulled,
which were unretrievable in time, and which never existed at all. The reveal has one thing to get right, or it teaches
the wrong lesson. For an incident undecidable by construction, where the estate genuinely never held the diverging
artefact, "unknown" is the correct answer, and a well-calibrated "unknown" is a success. An exercise that scored every
"unknown" as a failure would train analysts to manufacture confidence the record cannot support, the opposite of what the
Article 23 bar, with its permitted "unknown", is asking for. The exercise is reproducible: the same week, ground truth and
seed regenerate the same incident, so a cohort can be run against one scenario, and an estate that has closed a gap can be
re-run against the incident that previously defeated it.

## One engine, two uses

The engine is the constant across both. The generator is the extra machinery the training half needs and the audit half
does without, which is why the capability report is the cheaper and more defensible of the two, and the place a design on
the evidence layer would sensibly start.

*Last updated: 14 July 2026*
