# The First Foundation

*Knowledge as survival strategy*

The First Foundation was established on Terminus, a planet with no natural resources worth mentioning. This was
not an oversight. The resource poverty was the point. An organisation with nothing to fall back on except what
it knows is an organisation that takes knowledge seriously.

The First Foundation's strategy was elegant in a slightly ruthless way: become indispensable through technical
capability, make others dependent on your knowledge, and use that dependency as leverage. First they were
priests of technology, the only people who understood how the tools worked. Then traders, exchanging knowledge
for access. Eventually a proto-state, governing through the one thing nobody could replicate without them.

In security, this maps with uncomfortable accuracy.

## What the First Foundation looks like in security

The First Foundation in security is the technical and knowledge layer: the tooling, the frameworks, the
documented understanding of how attacks work and defences are built. MITRE ATT&CK is a First Foundation
artefact. So are CVE databases, compliance frameworks, SIEM playbooks, detection rules, and the accumulated
body of offensive and defensive technique that the security industry has spent several decades writing down.

The survival strategy is recognisable. Security teams with no organisational authority survive by being
indispensable: the only people who understand how the systems work, who can read the logs, who know what a
particular alert actually means. Knowledge as soft power, dependency as leverage. When the security team is
the only function that can answer certain questions, those questions give them a seat at the table.

This works, up to a point. The First Foundation of Terminus worked for several centuries before the Mule
arrived and rendered the predictions useless. Security's equivalent of the Mule arrives more frequently, but
the dynamic is the same: a sufficiently novel or unpredictable threat breaks the model that the knowledge
layer was built to handle.

## The weakness Seldon built in

The First Foundation was designed to be blind to human irrationality, because psychohistory only works at
scale. Individual behaviour is noise. Aggregate behaviour is predictable. The plan did not account for a
single mutant who could alter the aggregate by changing individual minds.

In security, the equivalent is the gap between what the technical layer assumes about human behaviour and what
human behaviour actually is. The SIEM rule that assumes analysts will investigate every high-severity alert.
The phishing simulation that assumes people have learned to distrust unexpected emails, which they have, for
the specific format those simulations use. The access control policy that assumes people will request the
minimum permissions required, rather than the ones that will avoid the need to raise another ticket later.

The First Foundation's encyclopaedia is accurate about the technical facts and silent about the people using
them. This is not a flaw in the knowledge. It is a structural limitation of a layer that was never designed
to address human behaviour directly.

## What the First Foundation cannot do alone

It cannot change the conditions under which people behave. A detection rule does not alter whether an analyst
trusts their instinct to escalate or their instinct to close the ticket and move on. A compliance framework does
not change whether the team filling out the questionnaire is being honest or is telling the auditor what they
want to hear. An incident response playbook does not change whether the people following it have ever
practised it under pressure.

These are not technical problems. They require the second foundation.

## Related

- [Indigo observatory](https://indigo.tymyrddin.dev/)
- [The Second Foundation: the invisible correction](second-foundation.md)
- [The Third Foundation: the uncomfortable question](third-foundation.md)
- [What these foundations can and cannot do](../foundations/disclaimer.md)
- [Core ideas of Satir systems OD](../foundations/organisational-development/satir-core.md)
