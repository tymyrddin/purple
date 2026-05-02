# The history assembled

AI decisions in security operations rarely run on a single signal. They run on enriched context assembled at
runtime from multiple sources, some internal, some external, and some contributed over time by the users
being assessed.

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
concrete state change is what passes to the decision layer: an event that entered with a raw
classification label leaves with an enriched risk score incorporating device reputation, account
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

## Why startup enrichment is especially vulnerable

Enrichment infrastructure in startups is often assembled from third-party APIs without a clear model of how
those signals interact. Signal weighting is rarely documented. Data retention policies for enrichment inputs
are often not aligned with product data governance. The question "which historical signals influenced this
decision, and can any of them have been shaped by the subject of the decision?" is rarely asked during
architecture reviews.

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

## Why context poisoning is slow to surface

Context poisoning is slow and produces no anomalous signal at any single moment. The account behaves
normally. The enrichment APIs return normal responses. The risk score reflects the context accurately. The
attack lies in the history that produced the context, not in the current event.

By the time the poisoned context produces a meaningful operational effect, the shaping campaign may be
months behind the detection window.

## What assembled context means for trust

Old enrichment looked up facts. New enrichment assembles a picture.

Pictures can be painted deliberately. The organisation is often not in a position to know whether the context
it is making decisions against reflects reality or a carefully constructed version of it.

## Making context harder to shape

Auditing which signals feed into enrichment pipelines, documenting their update cadences and data
origins, and reviewing weighting periodically rather than at deployment only.

Aligning data retention policies across product and enrichment infrastructure so that account resets
actually reset the relevant context, not only the product-level record.

Monitoring for slow distributional shifts in context profiles across account populations, not only
individual account behaviour. Systematic context poisoning is only visible in aggregate.

Including enrichment providers in supply chain security assessments: the same due diligence applied
to software dependencies applies to services that contribute to risk decisions.

Periodically testing whether accounts with deliberately constructed normality profiles can evade
detection, through red team exercises focused on the context layer specifically.

## Related

* [Supply chain and third-party risk](../audits/supportive/supply-chain.md)
* [The input layer](input.md)
* [The decision layer](decision.md)
* [Threat register](../audits/supportive/threat-register.md)
