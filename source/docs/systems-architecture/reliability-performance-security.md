# Reliability, performance, and security trade-offs

Reliability, performance, and security are not independently optimisable properties of a system. They pull against 
each other in ways that require deliberate trade-off decisions: security controls add latency; redundancy mechanisms 
increase attack surface; performance optimisations reduce defence in depth; availability requirements sometimes force 
consistency compromises that create exploitable windows. Every system of any complexity embodies a set of these 
trade-offs, whether they were made consciously or not.

The problem is not that the trade-offs exist. The problem is that they are almost never treated as decisions.

## What usually goes wrong

Trade-offs made implicitly cannot be revisited. When a caching strategy was chosen for performance reasons at the cost of a security property, and that choice was not documented as a trade-off, the next person who encounters the system does not know it was a choice. They think it is how things are done. When conditions change and the trade-off no longer makes sense, nobody knows it was a trade-off to revisit.

Ownership is fragmented. Security is owned by the security team, reliability by the SRE or operations function, performance by the development team. Each group optimises for its own metric with limited visibility into the constraints the others are managing. The result is point solutions that produce local improvements and system-level conflicts: the security control that causes the reliability mechanism to misbehave under load, the performance optimisation that bypasses the defence the security architecture depended on.

Compliance substitutes for the trade-off decision. A compliance framework says encryption at rest is required. The checkbox is checked. Nobody asked whether the encryption implementation causes enough performance degradation that the service disables it under peak load, or re-enables a weaker algorithm silently, or routes around it in ways that preserve the checkbox while removing the protection. Compliance describes what the system is expected to have. It does not describe whether the system has it under the conditions that matter.

Trade-offs made once are never revisited. The decision was made three years ago when the load was a fraction of its current level and the threat landscape was different. The security control that was acceptable at that load has since become a performance liability. The reliability architecture that was sufficient at that scale has since accumulated workarounds that nobody assessed for security implications. The trade-off drifted without being revisited because there was no mechanism to trigger a revisit.

Whoever is under the most immediate pressure makes the call. When the system is slow, the team under performance pressure removes the security control. When the audit is approaching, the security team re-enables it. When there is a reliability incident, the operations team takes the path of least resistance regardless of its security properties. These are not individual failures. They are what happens when a decision that requires authority across multiple domains is left to whoever is currently most uncomfortable with it.

The failure modes that have not been experienced are not modelled. Reliability work tends to defend against the failure modes that have already occurred. Security incidents frequently exploit the failure modes that have not been modelled, because adversaries are not constrained to cause the failures the organisation has previously observed. A reliability architecture built exclusively on experience is a model of past failures, not of future ones.

## The [SEM](../foundations/system-effectiveness/index.rst) view

Each of the three properties is a model. Reliability expresses a model of how the system fails and what it needs in order to recover. Performance expresses a model of how the system behaves under load and what it costs. Security expresses a model of how the system could be attacked and what it needs in order to resist. None of these models is complete, and none of them contains the other two.

When they conflict, the conflict is a model problem. The reliability model encoded assumptions about failure modes that the security model shows are exploitable. The performance model encoded assumptions about acceptable latency that the security model shows are incompatible with the required controls. Treating these conflicts as implementation problems, to be resolved by whoever is under the most pressure, produces systems where the models are separately coherent and collectively incoherent.

The [SEM response](../foundations/system-effectiveness/index.rst) is to make the assumptions in each model explicit and to examine the conflicts between them as a design activity rather than an operational emergency. The trade-off is a design decision. It belongs in the architecture, with its reasoning documented, its owner identified, and it's trigger for revisit specified. A trade-off that has drifted out of alignment with current conditions is a model failure, and model failures recur until the model is corrected.

## The [ChangeShop](../foundations/change-management/index.rst) view

Security controls degrade performance. When the degradation is noticed and complained about, the organisation's [homeostatic](../foundations/change-management/what-it-is.md) response is to remove the control or weaken it. Reliability mechanisms add complexity. When the complexity introduces operational burden, the homeostatic response is to reduce it in ways that introduce security vulnerabilities. These are not failures of commitment. They are the system returning to the state it was in before the change was made.

Understanding this as homeostatic resistance rather than bad faith changes what governance of the trade-off requires. A trade-off decision that is not protected by a stable ownership structure, explicit authority, and a review mechanism will be reversed by operational pressure. The conditions for the decision to hold need to be designed, not assumed. This is the ChangeShop insight applied to architecture: the trade-off is not just a technical decision; it is a change that the organisation needs to be in a position to sustain.

When a security control keeps being disabled under load, the question is not how to make people follow the policy. The question is what conditions would need to be in place for the policy to be followable. If the answer is "the system needs to be redesigned so the control does not cost what it currently costs," that is an architectural finding, and it belongs in the architecture.

## The [PSL](../foundations/problem-solving/index.rst) view

[PSL](../foundations/problem-solving/index.rst) notes:

- At the rational layer, the trade-off question is: what are the actual costs and benefits of each option, stated specifically enough to be compared? Not "this is more secure" or "this performs better," but what the specific security property is, what the specific performance cost is, and what the organisation's actual exposure would be under each option. Vague assertions about properties produce vague decisions that are easy to reverse.
- At the emotional layer, the trade-off discussion touches on ownership and identity. The security engineer whose control is being degraded for performance reasons is not just making a technical objection; they are protecting their professional judgement and their responsibility for an outcome they will be accountable for if it goes wrong. The performance engineer being told to accept slower response times for security reasons is not just making a technical objection either. These are real concerns, and designs that do not account for them will be relitigated every time conditions change.
- At the political layer, a trade-off decision that crosses team boundaries requires authority that crosses team boundaries. If no single person or role has the standing to make a binding decision about the reliability-performance-security balance, the decision will be made by whoever is under the most pressure, and it will be made again whenever the pressure distribution changes. Creating a clear locus of authority for cross-domain architectural decisions is not bureaucracy. It is the condition under which the decisions can be made once and held.

## The [Satir](../foundations/organisational-development/satir-core.md) view

Architecture reviews of systems with contested trade-offs tend to produce [survival stances](../foundations/organisational-development/satir-core.md) rather than honest 
engagement. The computing stance produces technically accurate accounts of each property's requirements without 
addressing the conflict between them: the security section describes the security requirements, the performance 
section describes the performance requirements, and nobody in the room names that they are incompatible in the 
proposed design. The blaming stance appears after an incident: the security team blames the performance team for 
disabling the control, the performance team blames the security team for a control that was unimplementable at the 
required load. The placating stance produces agreement in the review that the trade-off is real and important and 
should be properly addressed, followed by no change in the design.

Congruent engagement with a trade-off means naming it directly: this design makes a choice, here is what the choice is, 
here are the conditions under which that choice is defensible, and here is who is accountable for it. That naming 
is uncomfortable because it makes the accountability explicit. It is also the only thing that allows the decision 
to be made properly rather than deferred until circumstances make it for the organisation.

## What compliance cannot do

A compliance checkpoint asks whether a control is present. It does not ask whether the control is effective under 
the conditions the system actually operates under. It does not ask whether the reliability mechanism added to satisfy 
one requirement introduced an attack surface that undermines another. It does not ask who made the trade-off decision, 
whether they had the authority and information to make it well, whether it has been revisited as conditions changed, 
or whether the people operating the system understand the reasoning well enough to preserve it under pressure.

Compliance frameworks ask whether the right controls are present. The foundations work asks whether the conditions 
exist for those controls to become and remain effective under operational pressure. Passing an audit and operating a 
secure system are not the same question.

A system that passes its audit and fails in production has met the compliance requirement. The compliance requirement 
was not the right question.

## Related

- [Architecture as model](architecture-as-model.md)
- [SEM for defence and red teaming](../foundations/system-effectiveness/for-defence.md)
- [Audits and resilience: beyond compliance](../audits/resilience/beyond-compliance.md)
- [Resilience stress testing](../audits/resilience/stress-testing.md)
