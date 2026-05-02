# Trust assumed

A startup's security posture includes the security posture of every AI API, fraud service, and enrichment
provider it depends on. That boundary is rarely drawn explicitly, and even less rarely tested.

## Where the security boundary blurs

- Third-party fraud detection platforms providing risk scores via API. 
- LLM providers hosting the models used for incident summarisation, triage reasoning, and abuse classification. 
- Cloud-hosted moderation APIs classifying content against policy categories. 
- Device and IP intelligence feeds enriching authentication and fraud decisions. 
- Orchestration and retrieval frameworks that abstract over multiple model providers.

In each case, part of the security decision chain runs on infrastructure the organisation does not own,
using models it did not train, returning outputs it cannot fully audit.

## From owned logic to delegated inference

When security logic runs entirely on owned infrastructure, the organisation can inspect it. Rules are
auditable. Model weights can be stored and version-controlled. A decision can be reproduced given the
same input.

When security logic depends on external API calls, the organisation is delegating part of the decision
to a vendor's model, in a version it may not have chosen, running on infrastructure it cannot examine.
A model update by the vendor can change decision behaviour without notice. A vendor's own training
pipeline is a dependency of the organisation's security posture.

The chain of trust extends outside the organisation's boundary whether it is drawn there or not.

The external layer does not add a new transformation to the pipeline. It makes existing transformations
at the context and decision stages partially unauditable: the score arriving via the API looks the same
whether the vendor model behaved as expected or shifted silently. The organisation's routing decision
changes without anything changing on the organisation's side, and the cause is not visible in any owned
system.

## How external dependencies become exposure points

*Vendor model updates that silently change decision boundaries*: A fraud API or LLM provider may update
their underlying model without versioning the change in a way the organisation can pin against. The
update changes which inputs score above or below a threshold. The organisation observes a spike in false
positives, or a drop in detection rate, or anomalous customer behaviour on a specific date. Identifying
the vendor update as the cause requires correlating the anomaly with the vendor's release timeline, which
may not be publicly available. The investigation looks like a product anomaly until it is traced to an
upstream dependency.

*Inconsistent behaviour across LLM API versions exploited to find more permissive outputs*: When a
provider supports multiple model versions, the same prompt may produce different outputs across them.
An attacker who tests systematically across available versions can identify which produces outputs more
amenable to the intended manipulation, and request that version specifically if the API allows version
pinning by the caller. Organisations that do not monitor which model version their systems are calling
may not notice that a subset of requests is being routed to an older, more permissive version.

*Dependency trust chain abuse through upstream enrichment manipulation*: A third-party enrichment provider
builds its data from sources it aggregates and curates. Those sources may themselves be influenced by
activity the attacker controls. An attacker who contributes data that reaches the provider's pipeline, through publicly visible
activity, through influencing a source the provider crawls, or through a direct data relationship,
can shape the enrichment output that reaches the organisation's risk
decisions. The organisation has no visibility into how the provider's data was assembled, and the
provider may have no visibility into the manipulation.

*Cross-vendor inconsistency exploited by probing both systems*: An organisation that uses a primary fraud
provider with a fallback creates a situation where different inputs may be evaluated by different systems
depending on which is queried. An attacker who has probed both can identify inputs that score differently
across vendors, and calibrate their activity to score acceptably in the system governing the relevant
action. The fallback intended to improve resilience has created an additional detection gap.

*Vendor compromise affecting all dependent organisations simultaneously*: A fraud API or enrichment
service that is compromised affects every organisation that uses it at the same time. Unlike a targeted
attack, the scope is determined by the vendor's customer base rather than the attacker's targeting
decisions. The organisation's own controls are intact. The vendor's may not be. The incident response
timeline starts when the vendor discloses, which may be after the affected period has already passed.

## Why startups inherit risk they cannot audit

Heavy SaaS dependence is characteristic of startups. The efficiency argument is strong: using a
specialist fraud API is faster and cheaper than building and maintaining a fraud model. The security
implication is that the fraud API's security posture is part of the organisation's security posture,
whether or not there is a contractual mechanism to audit it.

Vendor security questionnaires establish what providers claim about their practices. They do not
establish how vendor model updates are validated before deployment, how vendor training pipelines
are protected, or how quickly vendors disclose anomalies affecting client-facing model behaviour.

## Third-party AI and enrichment services

Fraud and risk APIs, LLM providers, data enrichment services, cloud ML platforms, and moderation APIs
all fall into this category.

The analytical question for each is: what security decisions does this service influence, how would
the organisation know if the service's behaviour changed, and what is the fallback if the service
is unavailable or compromised? For many startup integrations, the answer to the second and third
questions is "unclear."

## Why vendor behaviour changes are hard to catch

The organisation cannot audit vendor model behaviour at the level of detail that would reveal systematic
manipulation or drift. Output monitoring for anomalies is possible, but distinguishing legitimate model
updates from exploitation requires a baseline and a monitoring discipline that is often not in place.

Vendor compromise is particularly difficult: the service appears to function normally, returns expected
response formats, and produces outputs within historical ranges. The compromise is in the training or
serving infrastructure, not in the API interface.

The attacker's touch point in this layer is not the organisation's own systems. It is the vendor's
training pipeline, the upstream data sources the vendor aggregates, or the enrichment feeds the vendor
incorporates. The organisation's pipeline is never accessed directly; influence enters the system through
externally generated API responses that are treated as trusted inputs.

## What dependency means for the threat model

The organisation's threat model includes the threat model of every external dependency that influences
a security decision.

Knowing which decisions depend on external AI services, and what the fallback is when those services
behave unexpectedly, is a prerequisite for understanding the actual boundary of the security posture.
Organisations that have not drawn that boundary have not understood where it is.

The external layer is less a tenth transition point than an acknowledgement that some of the other
nine are not fully owned.

## Understanding what you depend on

Mapping which security decisions depend on each external AI service, and defining explicit fallback
behaviour for when that service is unavailable, behaves unexpectedly, or returns outputs outside its
normal distribution.

Monitoring vendor API outputs for distributional anomalies over time using baselines established
during normal operation. Vendor model updates that change decision boundaries are not always announced;
output monitoring is the detection path.

Pinning model versions where the vendor API supports it and treating version changes as a configuration
management event requiring review rather than a transparent update.

Including AI API providers and enrichment services in supply chain security assessments alongside
traditional software dependencies. The security posture of the organisation includes the security
posture of the vendors it depends on for security decisions.

## Related

* [Supply chain and third-party risk](../audits/supportive/supply-chain.md)
* [Gap analysis](../audits/supportive/gap-analysis.md)
* [The integration layer](integration.md)
