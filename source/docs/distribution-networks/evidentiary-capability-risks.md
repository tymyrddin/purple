# Risks

These are the ways the direction could mislead even when it runs as designed. They are the honest
counterweight to the claim, and worth reading before the [feasibility page](feasibility.md)
argues the thing is buildable.

## The weighted verdict rests on un-elicited priors

The entropy-weighted layer depends on base rates nobody has measured for a given estate. Presented as a
number, a strength-of-evidence carries an authority the underlying estimate cannot support, and a
confident-looking weighting built on a guessed prior is worse than an honest "unknown". The structural layer,
the set intersection that needs no priors, is the defensible core; the weighted layer is best read as
indicative, and the design is better off wearing that distinction on its face than blurring the two into one
score.

## "Measured by nobody" overclaims

The claim that evidentiary capability is currently measured by nobody is too strong. Forensic
readiness has asked a neighbouring question for years, and logging-maturity work touches the edge of it. The
defensible claim is narrower: the discrimination among competing benign explanations, computed as a property
of the architecture and set against the estate's ordinary disorder, appears not to be measured directly by
existing tools. Overstating the novelty invites a fair objection that discredits the sound part along with
the loose part.

## The verdict is conditional on the menu

Because the computation is relative to the enumerated explanation set, its verdict inherits every omission in
that set. Leave off the explanation that would have been distinguishable, and the estate looks more capable
than it is; leave off the one that would have been indistinguishable, and it looks less. A verdict presented
without its menu is not interpretable, and the menu is exactly the part most vulnerable to quiet editing,
whether by oversight or by an operator with an incentive to look ready.

## Circular calibration

The critic that checks a generated incident for coherence, and the reveal that scores the analyst, both lean
on the same priors the design cannot yet ground. A generator and a grader tuned by the same assumptions can
agree with each other while both being wrong about how real incidents present. Without external calibration
against real records, the loop can be internally consistent and detached from the world it claims to model.

## Self-reported entropy skews optimistic

The estate configuration, and any base rates elicited from an operator, are self-reported. Operators carry a
mild, structural incentive to under-report their own disorder: fewer shared logins, tighter clocks, more
complete work orders than the estate really runs. Entropy under-reported makes discrimination look easier
than it is, so the tool's error, where the input is self-serving, runs toward false reassurance, the least
safe direction for it to fail in.

## Configuration honesty is the real barrier

Every determination rests on the estate configuration being truthful about what the record holds, retains,
and can retrieve. Getting that description honest, complete, and current is the actual adoption cost, and it
is not a modelling problem the design can solve for the operator. An estate that cannot produce an honest
bedrijfsmiddelenregister, a difficulty
[operating context](operating-context/operations-and-cadence/maintenance-philosophy.md) documents, may
not be able to produce an honest estate configuration either, and the tool cannot tell a truthful
configuration from a flattering one.

## Distrust of synthetic evidence

In training mode the tool's own evidence is synthetic, so it inherits the distrust that attaches to any
manufactured record. If the generator leaves a tell no benign week would, analysts learn to spot the
synthesis rather than reason about the incident, and nothing transfers to a real determination. The coherence
critic and calibration against real traces are the intended defences. The way to stop them being a matter of
faith is an adversarial discriminator, a model or a blind panel of analysts set to separate synthetic records
from real ones; the resemblance is shown only once neither can, and asserted until then. That is a bar the
direction can be held to rather than an open hope. The audit tool does not manufacture evidence, but it
reasons as though a retained artefact is a faithful signal of what happened, and a record an attacker could
forge is not. The
[source-independence treatment in the core design](evidentiary-capability-core-design.md) is what keeps that
honest: the report grades a determination resting on a forgeable record as low-trust rather than counting it,
so the tool states its own blind spot instead of hiding it. That grading is only as good as the
configuration's account of which records lie beyond which actor's reach.

## Validation depends on records nobody shares

The one thing that would ground the priors and confirm the explanations, a body of real incident records
with known ground truth, is scarce, confidential, and held close by the operators who have it. Until such
records are available for calibration, the direction stands on internal coherence and the plausibility of the
modelled estate, enough to build and exercise it but not enough to claim it predicts real determinations
accurately.

*Last updated: 12 July 2026*
