# Caveats, open questions and risks

The direction is best stated against its own edges. Three kinds sit here: what it is not, what is not yet worked out,
and how it could mislead even when it runs as designed. They overlap, because the same two boundaries, the un-elicited
priors and the enumerated explanation set, show up as a caveat, an open question and a risk at once.

## What it is not

### Not physics

The design inherits the substrate framing whole: it reproduces the evidence an estate emits, not the electrical
behaviour behind it. It never computes a fault current or a load flow, and the band where the physical dynamics
themselves are the evidence sits outside it. Questions that need hardware-in-the-loop stay out of scope.

### Not detection, not the wire

This is not a monitoring product and does not watch live traffic. It reasons about a record after the fact, or about
the capacity of a record before any fact. The moment-to-moment question detection tools answer is not the one being
asked; the direction sits at the level of whether a difference is observable in the retained record, not
signature-matching on the network.

### Not accreditation

A capability report is not a compliance certificate and does not attest that an operator meets NIS2. It states which
determinations an estate's record can and cannot support. Whether a regulator or an operator treats that as evidence
toward the Article 21(2)(f) effectiveness duty is their call, not a claim the tool makes for itself.

### Local, no telemetry

The direction runs locally against an estate configuration and a generated record. It does not phone home, does not need
the operator's live data to leave the operator, and produces no telemetry of its own. The estate configuration it reads
can be as sensitive as the operator chooses, which is a reason to keep the computation on the operator's own ground.

### Relative to an enumerated set

Every verdict, the four gates included, is relative to the explanations enumerated for a class of incident. It
answers "can these explanations be told apart at this estate", not "is there any conceivable account this record could
not distinguish". An explanation left off the list cannot be weighed, and the design does not discover the explanations
for you. This is the boundary most easily forgotten, and the open questions and risks below both return to it.

## Open questions

These are the parts genuinely not yet worked out, as against the risks further down, which are ways the thing could
mislead even when it works.

### Eliciting the priors

The base-rate weighting the [design](evidentiary-capability-design.md) keeps outside the four gates needs base rates:
how often clocks drift, work orders get backdated, logins get shared, relays get left in test mode. Those numbers are
not fixed by operating context and vary by estate. Whether they can be elicited from operators honestly and cheaply,
estimated from a period of a site's own logs, or whether the design has to stay on the four gates alone, which need no
priors, is open, and the answer sets how far any weighting can ever be trusted.

### Validation against real incidents

The generator's residue is only as convincing as its resemblance to the real thing, and the determinations are only
sound if the modelled explanations match how incidents actually present. Both want calibration against real incident
records, recorded traffic, historian extracts, post-incident forensics, and those are scarce, confidential, and rarely
shared outside the operator that holds them. This is possibly the binding constraint on how far the direction can be
taken. One route short of a full body of real incidents is an adversarial discriminator: hold the generator to the bar
that neither a model nor a blind panel of analysts can separate its output from real traces at the observable layer.
That does not prove the modelled explanations match real incidents, but it turns the resemblance claim into something
measured rather than asserted.

### Compound explanations

The model as drawn compares explanations pairwise and treats them as mutually exclusive. Real incidents are not always
so tidy: a genuine fault during a maintenance window worked by a contractor on a shared login, with a clock that had
drifted, is a compound of several explanations at once, and the residue is their superposition. Whether the pairwise
comparison extends cleanly to compounds, or whether compounds defeat the computation by making almost everything jointly
consistent with the record, is not yet worked out.

### The explanation set itself

The computation is relative to the set enumerated for a class of incident, so who assembles that set, how it is kept
from quietly omitting the awkward explanation that would change the verdict, and how a site knows its set is complete
enough to trust, are all open. Operating context supplies explanations only as scattered local forks, the three-way
relay divergence, the emergency verbal approval, rather than a consolidated catalogue, so building and maintaining that
catalogue is itself unfinished work.

## Risks that remain even when it works

These are the ways the direction could mislead when it runs exactly as designed, the honest counterweight to the claim.

### The weighting rests on un-elicited priors

Presented as a number, a strength-of-evidence carries an authority the underlying estimate cannot support, and a
confident-looking weighting built on a guessed prior is worse than an honest "unknown". The four gates, which need no
priors, are the defensible core; the base-rate weighting on top is best read as indicative, and the design is better off
wearing that distinction on its face than blurring the two into one score.

### Self-reported entropy skews optimistic

The estate configuration, and any base rates elicited from an operator, are self-reported, and operators carry a mild,
structural incentive to under-report their own disorder: fewer shared logins, tighter clocks, more complete work orders
than the estate really runs. Entropy under-reported makes discrimination look easier than it is, so where the input is
self-serving the tool's error runs toward false reassurance, the least safe direction for it to fail in.

### The verdict is conditional on the menu

Because the computation is relative to the enumerated set, its verdict inherits every omission. Leave off the
explanation that would have been distinguishable, and the estate looks more capable than it is; leave off the one that
would have been indistinguishable, and it looks less. A verdict presented without its menu is not interpretable, and the
menu is exactly the part most vulnerable to quiet editing, whether by oversight or by an operator with an incentive to
look ready.

### Circular calibration

The critic that checks a generated incident for coherence, and the reveal that scores the analyst, both lean on the same
priors the design cannot yet ground. A generator and a grader tuned by the same assumptions can agree with each other
while both being wrong about how real incidents present. Without external calibration against real records, the loop can
be internally consistent and detached from the world it claims to model.

### Configuration honesty is the real barrier

Every determination rests on the estate configuration being truthful about what the record holds, retains, and can
retrieve. Getting that description honest, complete, and current is the actual adoption cost, and it is not a modelling
problem the design can solve for the operator. An estate that cannot produce an honest bedrijfsmiddelenregister, a
difficulty [operating context](operating-context/operations-and-cadence/maintenance-philosophy.md) documents, may not be
able to produce an honest estate configuration either, and the tool cannot tell a truthful configuration from a
flattering one.

### Distrust of synthetic evidence

In training mode the tool's own evidence is synthetic, so it inherits the distrust that attaches to any manufactured
record: if the generator leaves a tell no benign week would, analysts learn to spot the synthesis rather than reason
about the incident, and nothing transfers to a real determination. The coherence critic and calibration against real
traces are the intended defences, and the adversarial discriminator above is the way to stop them being a matter of
faith. The audit half's own version of the problem, a retained artefact an attacker could have forged, is handled by the
[independence gate](evidentiary-capability-design.md), which reads the verdict against the suspect who could have written
the record rather than counting it blind, and is only as good as the configuration's account of which records lie beyond
which actor's reach.

### The novelty can be overstated

The claim that evidentiary capability is measured by nobody is too strong: forensic readiness has asked a neighbouring
question for years, and logging-maturity work touches the edge of it. The defensible claim is narrower, that the
discrimination among competing benign explanations, computed as a property of the architecture and set against the
estate's ordinary disorder, appears not to be measured directly by existing tools. Overstating the novelty invites a
fair objection that discredits the sound part along with the loose part.

*Last updated: 14 July 2026*
