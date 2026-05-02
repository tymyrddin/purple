# How far an error can travel

Security in a startup or scale-up is not one system. It is a set of systems built at different times by
different teams, connected by integrations that often predate the AI components now passing data through
them.

## Where signals cross system boundaries

- Fraud signals from the payment system feeding into identity risk scoring. 
- Abuse detection outputs from the content platform propagating to account management workflows. 
- Incident classification from the SIEM enriching support ticket priority. 
- Behavioural analytics from product telemetry informing authentication risk. 
- Customer trust scores assembled from signals across support, fraud, and product systems, exposed to downstream automation.

Each connection made sense when it was built. The aggregate produces a system where AI-influenced signals
flow across subsystems in ways that no single team designed end to end.

## From siloed decisions to propagating ones

Siloed systems fail independently. If the fraud system makes a wrong decision, the effect stays in the
fraud system. The error is bounded.

Interconnected AI-influenced systems propagate decisions. A fraud score that is wrong feeds an account
risk model that updates a customer tier that triggers a support automation that limits access to a
feature. The original classification error is now a chain of five downstream effects, none of which
individually looks like an error.

This is not unique to AI. It is a standard property of coupled systems. What AI adds is that each node
in the chain is now influenceable through the content it receives, not just through direct access to its
inputs.

The integration layer is not a classification step. It propagates risk and identity attributes as cross-system state changes, without altering their
meaning within each system, carrying the output of one classification step to systems that did not
perform it. An error bounded in the fraud system
becomes an error in the account reputation model, the content moderation threshold, and the customer
tier simultaneously. The attacker who exploits any upstream AI layer gains reach proportional to how
many systems consume that layer's output, not just the system where the classification happened.

## How cross-system paths get exploited

*Signals calibrated to produce a desired output in one subsystem specifically because that output
propagates elsewhere*: If a fraud signal affects an account reputation score, which in turn affects
the content moderation threshold, the attacker's target is not the fraud system; it is the moderation
threshold. The fraud signal is the mechanism, not the goal. Achieving a desired change in system B
through a carefully calibrated action in system A requires understanding the propagation path, which
is often not documented but can be inferred by observing outcomes.

*Cross-system inconsistency exploited as a detection gap*: Two systems that draw on the same data pipeline
but apply different models may classify the same user differently. The fraud system may assess the account
as low risk; the identity risk system may flag it as moderate. An attacker who has probed both knows
which one governs the action they care about, and operates in a way that appears acceptable to that
system while triggering no response from the other. The inconsistency is not a misconfiguration; it is
a product of two systems making correct local decisions from shared data. The gap between them is the
exploitable surface.

*Lateral movement through shared enrichment data rather than network paths*: Two systems may have no
direct connection but both draw from the same enrichment source. Influencing a signal in that shared
source affects both systems, even though only one integration path exists from the attacker's perspective.
System B, which the attacker cannot reach directly, becomes reachable indirectly through the shared data
layer. This type of lateral movement does not appear in traditional network-layer threat models.

*Cascading misclassification from a single upstream decision*: A decision made by an upstream AI component
feeds downstream components as an input. If that upstream decision is manipulated, the downstream
components process it as a legitimate signal, apply their own logic correctly, and produce an output that
appears reasonable given their inputs. The error is not visible in any single component; it is visible
only in the end-to-end trace. For cascades that cross team boundaries, assembling that trace may require
coordination that does not happen within the time window of the incident.

## Why the system map is rarely complete

Startups build integrations quickly, with ownership distributed across teams and limited documentation of
what flows where. Security review in this environment typically happens at the component level: is this
service secure? The system-level question, whether the combination of correctly-functioning components
produces exploitable behaviour, is less often asked.

The system integration map, if it exists at all, usually reflects what was intentionally connected rather
than what is effectively coupled through shared data and downstream propagation.

## Integration and propagation infrastructure

Message queues and event buses, internal SDKs that propagate signals across services, API gateways, data
platform pipelines, and shared feature stores all act as the connective tissue through which AI-influenced
signals travel.

The concern is not any individual integration but the system-level picture: which AI outputs influence
which downstream systems, through which paths, and with what accumulated effect. That picture is
rarely drawn in advance and often only assembled after a failure that required tracing it.

The concrete fields that carry AI influence across system boundaries are specific: the fraud score field
in an account record, the risk tier value in a shared feature store, the classification event payload
on an internal event bus. Shaping one of these fields upstream propagates to every downstream system
that reads it.

## Why relational failures are hard to spot

Individual components produce no anomalous signals. Each is doing what it is designed to do. The failure
mode is relational and only visible when the full signal chain is traced from the attacker-controlled input
to the downstream operational effect.

That chain is often long enough to cross team boundaries, which means no single team has complete
visibility over it. The monitoring that would surface the pattern is not obviously anyone's responsibility
to build.

## What coupling changes about failure

A system whose components all function correctly can still behave unexpectedly when the components are
coupled through AI-influenced signals.

Correctness at the component level is necessary but not sufficient for correctness at the system level.
The coupling is the attack surface: not a new decision point in the pipeline, but a multiplier on the
blast radius of every decision point upstream.

## Knowing what connects to what

Maintaining a system-level integration map that reflects effective data coupling, not only intentional
API connections. The propagation paths that create exploitable cross-system behaviour are often the
ones that were not designed explicitly.

Including integration paths in threat model reviews, specifically mapping which upstream AI decisions
can reach which downstream privileged operations through shared data and event flows.

Testing cross-system inconsistencies as part of security exercises: which inputs produce different
classifications across systems sharing the same data pipeline, and can those inconsistencies be
exploited as detection gaps?

Assigning clear ownership for the system-level integration picture rather than only for individual
component security. Relational failures require a relational view to detect.

## Related

* [Attack path mapping](../threat-modelling/attack-path-mapping.md)
* [Scope definition](../audits/supportive/scope-definition.md)
* [The action layer](action.md)
* [The external dependency layer](external.md)
