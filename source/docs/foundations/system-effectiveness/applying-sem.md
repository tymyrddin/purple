# Applying SEM to security

SEM changes what you look at and what questions you ask. The shift is from "what failed" to "what model allowed this 
to seem acceptable."

## Vulnerabilities as model failures

A standard finding: over-permissive access roles allow lateral movement. The conventional response is to tighten the 
permissions.

SEM asks what model produced the over-permissioning. Usually it is something like "broad access is necessary for 
productivity" or "ownership of access review is unclear so we err toward permissiveness." If that model is not 
corrected, the same pattern of permissions will re-emerge in a different role, a different service, or a different 
team. The YAML was not the problem.

This applies to most recurring vulnerability classes. Secrets in source code persist because the model is "secret 
management is someone else's concern" and no safe alternative exists within the workflow. Unpatched systems persist 
because the model is "patching creates operational risk" and there is no mechanism for establishing that the risk 
of not patching is higher. Each class of recurring finding has a model underneath it.

## Incidents as evidence

Instead of asking what broke in an incident, ask what belief was in place that made the outcome unsurprising in retrospect.

Secrets committed to a repository: the surface explanation is developer error. The SEM question is what model allowed 
this to seem like a low-risk action. Usually: "secrets handling is handled at the infrastructure level" (someone 
else's model), or "our repo is private" (a model about exposure that may be accurate or may not be), or simply "I did not 
think about it" (absence of any model at that decision point, which is itself a system design finding about where security 
thinking is and is not embedded in the workflow).

## Tools encode assumptions

Every security tool is a materialised model. The model that produced it is encoded in what it detects, what it ignores,
and what it treats as normal.

A SIEM built on a model of "threats are external and anomalous" will systematically miss insider threats and 
slow-moving campaigns that stay within baseline behaviour. An EDR built on a model of "endpoints are controlled units" 
will have gaps in environments where endpoints are ephemeral, containerised, or BYOD. A CSPM built on a model of 
"misconfigurations are visible and teams will fix them when alerted" will produce an alert backlog that grows until it 
is ignored.

The SEM question for any tool: when does this model break, and what does the blind spot look like? That blind spot 
is a finding before an attacker finds it.

## Best practices as frozen models

Security standards and checklists encode a model of the threat environment as it existed when they were written, 
applied to an organisational context that may bear no resemblance to yours.

"Apply least privilege" is sound in principle. In a fast-moving product team with unclear ownership under delivery 
pressure, the model behind it (that access review is a manageable, owned process) does not fit the operational reality. 
The result is exceptions everywhere, shadow access patterns, and a nominal compliance posture that diverges from the 
actual one.

The SEM approach is not to abandon the principle but to ask whether the model fits the environment, and if not, what 
changes in the environment would make the model applicable.

## Error amplification in modern environments

Small model errors produce large consequences in tightly coupled, fast-moving systems. Cloud environments propagate 
misconfiguration at speed. CI/CD pipelines distribute errors across environments before anyone notices. APIs connect 
systems in ways that turn a single trust assumption into an organisation-wide exposure.

A model that says "this service is internal only" may be accurate for the service itself and entirely wrong about its 
exposure through an API gateway. The service is internal. The gateway is not. The model was correct about one layer 
and silent about the others. In a cloud-native environment, that silence scales.

## Related

- [Systems, models, and errors](core-triad.md)
- [SEM for defence and red teaming](for-defence.md)
- [Architecture as model](../../systems-architecture/architecture-as-model.md)
- [SOC maturity](../../making-of/soc/maturity.md)
