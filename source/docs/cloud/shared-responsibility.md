# Shared responsibility

The shared responsibility model is the contractual fiction that organises cloud security. The provider is responsible
for security of the cloud; the customer is responsible for security in the cloud. Both halves are real, both have edge
cases, and the edge cases are where most cloud incidents originate.

## Where the line sits

The split varies by service type. IaaS leaves more to the customer: operating system patching, network configuration,
application security. PaaS shifts more to the provider, with managed runtime and often managed identity. SaaS shifts
almost everything to the provider, but leaves the customer responsible for data, access management, and the
configuration of whatever the provider exposes through its admin surface.

The trouble starts where the line is unclear. Container services that are "managed" but require the customer to
configure security groups. Serverless functions where the customer writes the code but the provider manages execution
and observability. Managed databases where the provider patches but the customer configures access. Each of these has a
documented responsibility split that few customers read carefully and many providers describe ambiguously.

A useful question to ask of any cloud service before adopting it: where is the line between provider and customer, what
happens if either side gets it wrong, and which incidents would each side be in a position to detect.

## Why the model produces the failures it does

The shared responsibility model assumes that both parties understand their share. Several conditions undermine that
assumption in practice.

The customer side is often distributed. Cloud accounts are owned by product teams, who own the configuration of the
services they run. Security teams may have policy authority but rarely operational ownership. The "customer" in the
shared responsibility diagram is often a coalition that has not met.

The provider side is documented in dense reference material that updates without notice. A configuration that was
secure-by-default last quarter may not be next quarter. The customer who configured the service correctly the first time
bears no obvious cost; the customer who relied on the default and stopped paying attention bears the cost when the
default changes.

The interface between the two sides has no shared interface. There is no protocol for "we are about to deprecate this
default" except a release note that the customer's automation may not parse. The cumulative effect, across many services
and many customers, is the misconfiguration epidemic the cloud industry has been grappling with for most of a decade.

## Reading the model honestly

Treating the shared responsibility model as a description of where the work goes, rather than where the blame goes when
things break, produces a different posture. The customer side is everything the customer can affect; the provider side
is everything the customer cannot. The interesting work is at the interface: choosing services whose interface is clear,
monitoring the interface for change, and treating each service adoption as a security-relevant decision rather than a
procurement one.

## Related

- [Cloud attack surfaces](attack-surface.md)
- [Identity collapse and the control plane](identity-collapse.md)
- [Multi-cloud trust boundaries](multi-cloud-trust.md)
- [Cloud-native attack patterns](https://red.tymyrddin.dev/docs/in/cloud/notes/cloud-centric.html)
- [Why cloud environments are hard to test](https://red.tymyrddin.dev/docs/in/cloud/notes/challenges.html)
- [Cloud complexity and misconfiguration epidemic](https://indigo.tymyrddin.dev/docs/debt/cloud.html)
