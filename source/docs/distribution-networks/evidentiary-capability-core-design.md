# Core design

The model rests on a small move: treat an explanation as something that predicts evidence, not something that
labels an incident after the fact.

## Explanations as generative models

When a breaker opens out of hours, several accounts could be true. A protection trip on a genuine fault. An
operator acting under a verbal emergency approval. A contractor on a maintenance window that ran late. A
misconfigured scheme firing on a defect. An intruder issuing a forged command. Each of these is a generative
model in the sense that it predicts a particular spread of residue: which artefacts would be present, in
what order, carrying which actors and times. A genuine fault predicts a fault-passage indication, a relay
pickup, a trip in the sequence-of-events, a disturbance capture, then the breaker transition and the alarm. A
forged command predicts the breaker transition and the alarm and nothing upstream of the point it touched.
The two accounts are separable exactly where their predicted residue diverges, which is the observation
[feasibility](feasibility.md) already draws with its two side-by-side traces.

Determining whether malice is suspected is then a comparison of predictions against a record, not a hunt for
a signature. The question is which explanations the surviving evidence is consistent with, and whether the
malicious one can be told apart from the benign ones that remain.

## Present, absent, unrecordable

Reasoning over residue needs three states for any expected artefact, not two. Present: the record holds it.
Absent: the record does not hold it, and its absence carries meaning, as the missing upstream trip does in
the injected-command trace. Unrecordable: the estate never had the capacity to hold it, so its absence
carries no meaning at all. The distinction between absent and unrecordable is the whole game. An artefact
that is absent narrows the explanations; an artefact that is unrecordable narrows nothing, and mistaking the
second for the first manufactures false confidence. A determination built on "the trip record is not there,
so no fault occurred" is sound only if the estate would have kept the trip record had there been one.

## Present, but forgeable

Presence carries a question the three states do not, once the party under suspicion could have written the
record. An artefact can be present and independent, held somewhere the investigated actor did not control, or
present but forgeable, sitting in a log they could edit as part of the act. The distinction runs through
[observable semantics](observable-semantics/index.rst): the packet capture is the objective record
because it is independent of any system's own logs, a historian edit is caught by disagreement with records
the historian does not control, and in the ACM meter dispute it was the handwritten logbook of physical read attempts, held outside the
platform, that proved decisive. A forged benign explanation can manufacture "present" where the honest reading is "absent", so
discrimination leans on the residue an actor could not have planted rather than on whatever residue happens
to be there. Synthetic evidence, in other words, is not only a thing the tool produces; it is a move an
attacker makes, and the record's worth turns on which parts of it lay beyond the attacker's reach.

## Entropy as substrate

Real estates do not run clean. Clocks drift and get nudged. Contractors share a login. A work order is closed
retroactively on Monday for work done on Saturday. A relay is left in test mode after commissioning. The
[staffing pressures](operating-context/staffing-and-capability/staffing-realities.md) and
[contractor arrangements](operating-context/operations-and-cadence/contractor-management.md) set out in
operating context are not incidental colour; they are the disorder every determination has to
survive. Treating that disorder as noise to be filtered misreads it. It is the substrate. A malicious change
that hides inside the ordinary rate of retroactive work orders is undetectable not because the evidence is
missing but because the benign explanation is always available at that estate. Entropy sets the floor below
which discrimination cannot go, and it is a property of how the estate is run, not of the attack.

## The estate configuration

What the design ingests is a structured description of the record, an estate configuration. It names the
systems of record (the SCADA alarm-and-event journal, the historian, the relay sequence-of-events, the
engineering-workstation logs, the work-order system, the access and key records), the fields each one holds,
the retention window on each, the clock discipline across them, the authorisation model that says who could
legitimately have acted, the retrieval cost of each artefact under the twenty-four hour clock, and, for each
record, who can write or alter it and whether it is append-only, tamper-evident, or held out-of-band. That
last field is not the authorisation model in another guise: the authorisation model says who could
legitimately have acted, this says who could fabricate the record, and the two come apart exactly when the
actor under suspicion is one with write access. The
[system-portrait](operating-context/system-portrait.md) and
[vendor-platform](operating-context/system-composition/vendor-platform.md) already assemble most of
this for the worked estate; the configuration is that material rendered as something a computation can read.
A given deployment supplies its own; operating context supplies a realistic default, discussed on the
[audit page](evidentiary-capability-as-audit.md).

## The identifiability computation

Given a pair of explanations and an estate configuration, the design asks a bounded question: does the record
retain, and can it retrieve in time, the artefact on which the two explanations diverge? This is
identifiability, or observability of the difference, and it is worth keeping in two layers that carry
different weights.

The structural layer is robust and needs no probabilities. For each pair of explanations, take the artefacts
where their predicted residue differs, and intersect that set with the artefacts the estate actually retains
and can retrieve inside the window. If the intersection is empty, the two explanations are indistinguishable
at this estate by construction, and the determination between them is unreachable no matter who is looking.
This is a set operation over the configuration, defensible without any estimate of how often anything
happens. The trust dimension sharpens it into three outcomes rather than two. When the explanation to be
ruled out is one the actor could fake, a malicious change dressed as routine, the diverging artefacts split
by who could have written them. A pair is Supported when at least one diverging artefact is
held independently of that actor, beyond their reach to plant; supported only on forgeable evidence when the only
diverging artefact sits in a record the actor could forge, since the malicious explanation can produce it
too; and unsupported when no diverging artefact survives at all. A forgeable artefact counts as
decisive only once an independent record corroborates it, the packet capture beside the log, the paper beside
the platform. This is still a set operation, now over the write-authority the configuration records, with no
estimate of how often anything happens, so the trust grade joins the structural core rather than the
provisional layer below.

The entropy-weighted layer is provisional and needs priors the design does not yet have. Even where a
diverging artefact survives, the benign explanation may be common enough that the artefact shifts belief only
a little. Weighting the comparison by base rates would turn a yes-or-no identifiability into a
strength-of-evidence, but it rests on estimates of how often clocks drift, work orders get backdated, logins
get shared. Those numbers are not fixed by operating context and are hard to elicit honestly, so this
layer reads as indicative rather than load-bearing, and the [limits page](evidentiary-capability-limits.md)
returns to why.

The output of the computation reads two ways: statically, it is an audit finding; wrapped in a generated incident, a
training exercise.

## The shape of the two tools

The two tools are one pipeline. Both ingest an estate configuration and both run the same engine, the
identifiability computation above; the training tool adds a second input and a generator in front of it.

    INGEST  (shared by both tools)
        operating context  ──►  estate configuration  (the default config)
        a real deployment supplies its own; the schema extends over time
        the same default also serves as the test fixture

    AUDIT TOOL
        estate configuration  ──►  engine  ──►  capability report
                                    (identifiability computation)
        no generator, no incident, no analyst; a static property of the record
        each determination graded: supported / forgeable-only / unsupported

    TRAINING TOOL
        estate configuration + training input  ──►  generator  ──►  synthetic record
        (training input: ground truth, the           (the residue
         explanation menu, a seed, difficulty)        generator)
                                                            │
                                                            ▼
        reveal  ◄──  engine  ◄──  analyst files the Article 23 call under the clock
        (full residue vs   (same
         retrieved subset)  identifiability
                            computation)

The engine is the constant. The generator is what the training tool needs and the audit tool does without,
which is why the capability report is the cheaper, more defensible half of the direction.

*Last updated: 12 July 2026*
