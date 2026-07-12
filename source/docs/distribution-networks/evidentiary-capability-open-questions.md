# Open questions

The direction has edges that are genuinely unresolved, distinct from the entries on the
[risks page](evidentiary-capability-risks.md), which are ways the thing could mislead even when it works.
These are the parts not yet worked out.

## Eliciting the priors

The entropy-weighted layer of the [identifiability computation](evidentiary-capability-core-design.md) needs
base rates: how often clocks drift, work orders get backdated, logins get shared, relays get left in test
mode. Those numbers are not fixed by operating context, and they vary by estate. Whether they can be elicited from
operators honestly and cheaply, or estimated from a period of a site's own logs, or whether the design has to
stay on the structural layer that needs no priors, is open. The answer shapes how far the weighted layer can
ever be trusted.

## Validation against real incidents

The generator's residue is only as convincing as its resemblance to the real thing, and the determinations
are only sound if the modelled explanations match how incidents actually present. Both want calibration
against real incident records: recorded traffic, historian extracts, post-incident forensics. Those records
are scarce, confidential, and rarely shared outside the operator that holds them. Feasibility already names
validation as the open edge for the substrate; it is at least as open here, and possibly the binding
constraint on how far the direction can be taken. One concrete route short of a full body of real incidents is
an adversarial discriminator: hold the generator to the bar that neither a model nor a blind panel of analysts
can separate its output from real recorded traces at the observable layer. That does not prove the modelled
explanations match real incidents, but it turns the resemblance claim into something measured rather than
asserted.

## Compound explanations

The model as drawn compares explanations pairwise and treats them as mutually exclusive. Real incidents are
not always so tidy: a genuine fault during a maintenance window worked by a contractor on a shared login,
with a clock that had drifted, is a compound of several explanations at once, and the residue is their
superposition. Whether the pairwise comparison extends cleanly to compounds, or whether compounds defeat the
identifiability computation by making almost everything jointly consistent with the record, is not yet worked
out.

## The explanation set itself

The whole computation is relative to the set of explanations enumerated for a given class of incident. Who
assembles that set, how it is kept from quietly omitting the awkward explanation that would change the
verdict, and how a site knows its set is complete enough to trust, are open. Operating context supplies
explanations only as scattered local forks, the three-way relay divergence, the emergency verbal approval,
rather than a consolidated catalogue, so building and maintaining that catalogue is itself unfinished work.

*Last updated: 12 July 2026*
