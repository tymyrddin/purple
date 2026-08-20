# Applying SEM to security

[SEM](core-triad.md) moves the question. "What failed" gives way to "what model made this look acceptable at the time".

## Vulnerabilities as model failures

A standard finding: over-permissive access roles allow lateral movement. The conventional response tightens the
permissions.

The model underneath is usually something like "broad access is necessary for productivity", or "nobody owns access
review, so we err towards permissiveness". Left in place, it re-emerges as the same pattern of permissions in a
different role, a different service, a different team. The YAML was not the problem.

Many recurring vulnerability classes work this way. Secrets persist in source code on a model of "secret management is
someone else's concern", with no safe alternative inside the workflow. Systems go unpatched on a model of "patching
creates operational risk", with nothing in place to establish that not patching carries more.

## Incidents as evidence

The question after an incident is usually what broke. A more useful one is what belief was in place that made the
outcome unsurprising in hindsight.

Secrets committed to a repository read, on the surface, as developer error. Underneath sit three candidate models.
"Secrets handling happens at the infrastructure level" puts the work in someone else's hands. "Our repo is private"
makes a claim about exposure that may or may not hold. "I did not think about it" is the absence of any model at that
decision point. That points at the workflow rather than the developer: security thinking is not embedded where the
decision gets made.

## Tools encode assumptions

Every security tool is a [materialised model](../../systems-architecture/architecture-as-model.md), and the model shows
in what it detects, what it ignores, and what it treats as normal.

A SIEM built on "threats are external and anomalous" can miss insider threats and slow campaigns that stay inside
baseline behaviour. An EDR built on "endpoints are controlled units" leaves gaps wherever endpoints are ephemeral,
containerised or BYOD. A CSPM built on "misconfigurations are visible and teams will fix them when alerted" grows an
alert backlog until the backlog gets ignored.

A tool's model gives out somewhere, and what falls into the gap is a [finding in its own right](for-defence.md).

## Best practices as frozen models

Standards and checklists encode a threat environment as it stood when they were written, then get applied to an
organisational context that may bear no resemblance to it.

"Apply least privilege" is sound in principle. It assumes access review is a manageable, owned process. In a fast-moving
product team with unclear ownership and delivery pressure, that assumption does not hold. What often follows is
exceptions everywhere, shadow access patterns, and a nominal compliance posture drifting away from the real one.

The principle survives the mismatch. What changes is the question: does the model fit this environment, and if not, what
would have to change in the environment before it did?

## Error amplification in modern environments

Small model errors can produce large consequences in tightly coupled, fast-moving systems. Cloud environments propagate
misconfiguration at speed. CI/CD pipelines distribute an error across environments before anyone notices. APIs turn a
single trust assumption into an organisation-wide exposure.

"This service is internal only" can be accurate about the service and entirely wrong about its exposure through an API
gateway. The service is internal. The gateway is not. The model was right about one layer and silent about the others,
and in a cloud-native environment that silence scales.

*Last updated: 11 August 2026*
