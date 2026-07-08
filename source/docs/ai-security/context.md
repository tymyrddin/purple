# The history assembled

AI decisions in security operations rarely run on a single signal. They run on enriched context assembled at
runtime from multiple sources: some internal, some external, and some built up over time by the very user the
decision is about. The subject of the assessment has, in part, written the history it runs on.

## Where enrichment decisions live

- Fraud scoring pipelines that combine account age, transaction history, device reputation, and IP intelligence into a risk score.
- Login risk engines evaluating device fingerprint, location history, and peer behaviour.
- Abuse detection systems that weight a current event against the user's prior complaint history.
- Moderation tools that factor in account standing, previous violations, and inferred user segment before classifying content.
- Support routing systems that adjust priority based on customer tier and prior interactions.

The richer the context, the more stable the decision. That is the appeal, and also the attack surface.

## From looking up facts to assembling pictures

Traditional enrichment worked with defined, bounded signals: account age in days, transaction count, known
IP ranges. The field values were discrete and auditable.

AI context assembly works with aggregated histories, inferred patterns, and signals whose contribution to
the final decision is not individually visible. A reputation score reflects dozens of prior events. A
behavioural embedding compresses months of activity into a vector. The contribution of any single past event
to the current decision is opaque.

That opacity is what makes the context layer attackable. There is no single field to audit; there is a
history to shape.

The AI component's function here is to combine structured and unstructured inputs into a composite risk score. The
concrete state change is what passes to the [decision layer](decision.md): an event that entered with a raw
[classification label](input.md) leaves with an enriched risk score incorporating device reputation, account
history, and peer signals. That score is richer than the label it replaced and harder to trace back to
any individual contributing signal.

## How context gets shaped over time

*Slow-burn accounts that establish clean histories before pivoting to abuse*: An account that spends three
months making small, legitimate-looking transactions, building a positive reputation score and a clean
device history, is treated very differently by a risk model than a new account attempting the same action.
The patience required is modest compared to the operational value of a trusted identity. The attack is
entirely invisible during the establishment phase, because nothing anomalous is happening.

*Device and IP reputation poisoning through churning clean-looking activity*: Reputation feeds that rate
infrastructure based on prior observed behaviour can be seeded with clean signals by running benign
activity through the infrastructure intended for later abuse. A hosting range that has only ever been
used for legitimate browsing looks very different to an intelligence feed than a range associated with
prior fraud. Establishing a clean reputation for infrastructure is a preparation step, not an attack
in itself; the enrichment layer does not distinguish preparation from legitimacy.

*Normality profiles built to absorb future anomalies*: A user whose historical behaviour includes
high-volume activity, irregular hours, and geographic spread will have a very different baseline than
a typical user. An attacker who spends weeks establishing an unusual-but-consistent behaviour pattern
is conditioning the system to treat their future activity as within the expected range for that profile.
When the actual attack behaviour occurs, it is assessed against a personalised baseline that was designed
to accommodate it.

*Inconsistencies across enrichment providers exploited as detection gaps*: An IP address rated clean by
one provider and risky by another, with an AI system weighting the clean signal preferentially, creates
a reliable gap: activity routed through that IP is assessed more leniently than the second provider's
data would warrant. Identifying such gaps requires only systematic probing of which provider's signal
dominates in different contexts.

*Context poisoning that survives account resets*: When a product account is deleted and a new one created,
the product-level history resets. Enrichment infrastructure often does not follow the same deletion
schedule. Device fingerprints, IP reputation data, and shared identity signals retained in third-party
systems may carry the established normality profile forward to the new account, defeating the purpose
of the reset and allowing shaped context to persist across what appears to be a fresh start.

## Startup enrichment is especially vulnerable

Enrichment infrastructure in startups is often assembled from third-party APIs without a clear model of how
those signals interact. Signal weighting is rarely documented. Data retention policies for enrichment inputs
are often not aligned with product data governance. The question "which historical signals influenced this
decision, and can any of them have been shaped by the subject of the decision?" is rarely asked during
architecture reviews, and rarely captured in a [threat register](../audits/supportive/threat-register.md).

## Signal sources and their risks

Third-party reputation and enrichment services, device intelligence platforms, IP and network intelligence
feeds, internal feature stores that aggregate historical signals, and ML feature pipelines that assemble
context at inference time all fall into this category.

The architectural risk is not any one provider. It is the assembly: context is drawn from multiple sources
with different update cadences, different data origins, and different susceptibility to shaping. The final
risk score reflects all of them, usually without weighting that is visible to the analyst reviewing it. The
fields an attacker can influence are specific: the API response from an enrichment provider, the device
fingerprint value on record, the IP reputation score from a third-party feed, the outcome label on a prior
reviewed transaction. Each is a concrete input the context assembly reads, and each can be shaped without
touching the risk scoring model directly.

## Context poisoning slow to surface

Context poisoning is slow and produces no anomalous signal at any single moment. The account behaves
normally. The enrichment APIs return normal responses. The risk score reflects the context accurately. The
attack lies in the history that produced the context, not in the current event.

By the time the poisoned context produces a meaningful operational effect, the shaping campaign may be
months behind the detection window.

## Assembled context and trust

A looked-up fact could be checked against its source. An assembled picture cannot, because it has no single
source: it is the sum of many prior events, each individually unremarkable, weighted in ways the analyst never
sees. That is what makes it trustworthy enough to be useful and shapeable enough to be dangerous.

The organisation is rarely in a position to know whether the context it is deciding against reflects reality or
a version composed for the occasion. The shaping, where it happened, happened months ago and left nothing in
the present event to notice.

## Making context harder to shape

Context cannot be secured field by field, because no single field is the problem. The measures that help work
on the assembly itself: making it legible, keeping its lifecycle honest, and watching it in aggregate.

Legibility comes first. Auditing which signals feed the enrichment pipeline, documenting their update cadences
and data origins, and reviewing the weighting periodically rather than only at deployment turns an opaque score
into something that can be reasoned about. Enrichment providers belong in [supply chain security
assessments](../audits/supportive/supply-chain.md) for the same reason: a third party that contributes to a
risk decision deserves the due diligence given to a software dependency.

Lifecycle comes next. Aligning data retention across product and enrichment infrastructure closes the gap that
lets a shaped profile outlive the account it was built on, so an account reset actually clears the enrichment
context and not only the product-level record.

The rest is catching shaping while it is under way. Monitoring for slow distributional shifts across whole
account populations, rather than individual accounts, surfaces systematic poisoning that stays invisible one
account at a time. Red team exercises that build deliberately constructed normality profiles then test whether
the context layer can be walked past on purpose.

*Last updated: 3 July 2026*
