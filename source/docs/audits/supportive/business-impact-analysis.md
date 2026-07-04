# Business impact analysis

A business impact analysis answers two questions the rest of continuity planning depends on: what can the
organisation not afford to lose, and for how long? It is the instrument that turns an asset register into
recovery priorities, and every continuity number worth defending (tolerable downtime, recovery targets, backup
cadence) traces back to it. The [storm charts](../iso22301/storm-charts.md) stage leans on it and NIS2's
business continuity measure assumes it; this page owns the craft.

## The numbers a BIA produces

* MTPD, maximum tolerable period of disruption (often called MTD, maximum tolerable downtime): the point past which the disruption's consequences become unacceptable, whether the threshold is safety, legal, financial, or the survival of the service itself.
* RTO, recovery time objective: the target time to restore a function after disruption. Set inside the MTPD with room to spare; an RTO equal to the MTPD is a plan to arrive exactly as the building burns down.
* RPO, recovery point objective: the maximum acceptable data loss, expressed as time. It drives backup frequency directly; an RPO of one hour with nightly backups is not an objective, it is a hope.
* MBCO, minimum business continuity objective: the reduced level of service that is acceptable during recovery. Not everything needs full restoration at once, and naming the minimum is what makes staged recovery plannable.

The numbers hang together: the impact analysis sets the MTPD, the RTO fits inside it, the RPO follows from how
fast the data changes and how much of it could be re-created another way, and the MBCO defines what "recovered
enough to breathe" looks like.

## Running one

The unit of analysis is the business function or service, not the system. Systems come in later, as
dependencies. Starting from the products and services in
[scope](scope-definition.md), each function gets examined for what it delivers, to whom, and what happens when
it stops.

The central craft move is charting impact over time rather than assigning a single rating. Disruption impact
grows, and rarely linearly: an order-processing outage is an annoyance at four hours, a customer-visible
failure at a day, a contractual breach at three days, and a survival question at two weeks. A simple grid
(impact per category at 4 hours, 24 hours, 3 days, a week) captures this; a single "high" does not, and the
MTPD falls out of the grid at the point where any category crosses into intolerable.

The information comes from the people who run the function, not only their managers, which makes
[interview and workshop craft](interview-facilitation.md) part of the method. One dynamic deserves open eyes:
every function owner has a reason to rate their own function critical, since criticality attracts budget and
attention. Useful counters include scarce tiers (only so many functions may be tier one), forced ranking, and
the calibrating question "what actually happened the last time this was down?", which frequently produces a
smaller and more honest number than the hypothetical.

## Impact in more than money

The classic failure is impact defined only in financial terms, which systematically underrates the risks that
arrive by other routes. A workable category set covers:

* Safety: patient care in a hospital, process safety on a plant. Where this category applies, it usually dominates.
* Legal and regulatory: reporting deadlines missed, licence conditions breached, contractual penalties triggered.
* Operational knock-on: what this function's stoppage does to other functions, which the dependency map makes visible.
* Reputational: customer-visible failure, and the difference between an outage customers notice and one they remember.
* Financial: last, not because it is unimportant, but because it is the one category that never gets forgotten.

Each category needs its own severity anchors, defined concretely enough that two assessors would land on the
same rating; [risk scoring](risk-scoring.md) covers that calibration discipline, and the two pages share it.

## Dependency mapping

A function's recovery is only as fast as its slowest dependency, which makes the dependency map the part of
the BIA that earns its keep. For each critical function, the map covers supporting systems and data, the
people who can operate them, suppliers and external services, facilities and utilities, and the other internal
functions it relies on.

Two patterns to hunt for:

* Inherited objectives. A function with a four-hour RTO depending on a system that restores in twenty-four hours has a fiction, not an objective. Dependencies inherit recovery requirements upward, and the mismatches are findings.
* Concentration. Shared dependencies (one identity provider, one data centre, one engineer who knows the batch job) turn many small risks into one large one. The single-person dependency is the entry that tends to go unrecorded because naming it is socially expensive, the same [three-domains](../../foundations/problem-solving/three-domains.md) dynamic that shapes risk registers.

Recovery sequencing comes from the dependency order, not from criticality rank alone: the most critical
function may need three unglamorous services restored first, and a recovery plan ordered by importance rather
than by dependency discovers this during an incident.

## Numbers that survive contact

A BIA's outputs are hypotheses, and the continuity machinery exists to test them. A restoration drill measures
the real recovery time against the RTO; a backup restore measures the real data loss against the RPO; a
tabletop walks the recovery sequencing against the dependency map. When a drill takes nine hours against a
four-hour RTO, either the capability or the number is wrong, and both are respectable answers as long as one
of them changes. [Running the drills](../iso22301/drills.md) covers the exercise side; the BIA is where the
results land.

The other survival condition is resourcing. An RTO that was never costed and funded is an aspiration with a
decimal point. Function owners sign the impact assessment; whoever owns the budget signs the recovery
objectives, or the numbers describe a continuity capability the organisation has declined to buy.

## Keeping it current

A BIA describes the organisation as it was on the day of the workshops. New systems and services, reorganised
teams, changed suppliers, and shifted customer commitments all move the numbers without asking. An annual
review is the floor; the sharper triggers are architecture changes touching mapped dependencies, incidents and
exercises whose measured times disagree with the assumed ones, and business changes that alter what the
organisation has promised to whom.

## Framework notes

* ISO 22301: Clause 8.2 makes the BIA the standard's centre of gravity; the continuity strategies of Clause 8.3 are chosen against its outputs, and an auditor reads the BIA date before reading the plans.
* NIS2: the Article 21 business continuity measure (backup management, disaster recovery, crisis management) presumes the entity knows which services are essential and what their recovery needs are; the BIA is where that knowledge is supposed to come from.
* ISO 27001: the availability leg of the triad rests here, and the 2022 controls on continuity (A.5.29, A.5.30) assume BIA outputs exist to plan against.
* IEC 62443: in OT contexts availability and safety usually outrank confidentiality, and zone criticality feeds both the impact categories and the security level targets.

## Related

* [ISO 22301 Storm charts](../iso22301/storm-charts.md)
* [ISO 22301 The factory's emergency systems](../iso22301/emergency-systems.md)
* [ISO 22301 Running the drills](../iso22301/drills.md)
* [NIS2 Building a raft](../nis2/raft.md)
* [Scope definition](scope-definition.md)
* [Risk scoring](risk-scoring.md)
* [Interview and workshop facilitation](interview-facilitation.md)
* [Supply chain and third-party risk](supply-chain.md)
