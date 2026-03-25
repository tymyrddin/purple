# SEM for defence and red teaming

SEM is useful in both directions. For defenders, it surfaces the assumptions that produce blind spots. For offensive work, it reframes the attack surface.

## SEM-informed defence

### Identify critical models

Start by asking where the organisation is relying on assumptions rather than verified facts. Which beliefs, if wrong, 
would cause the most damage? The exercise is uncomfortable because it reveals how much of the security posture is built 
on trust in things that have not been checked recently, or ever.

Some starting questions: when was the last time the network segmentation model was validated against actual traffic? 
What assumptions does the detection engineering depend on about what "normal" looks like in the current environment? 
Which services are assumed to be internal that have not been audited for external exposure?

### Test models deliberately

Assumptions degrade. The environment changes, the assumption does not, and the model gradually diverges from reality 
without anyone noticing.

Deliberate model testing is not the same as penetration testing. It is asking specific questions: does the isolation 
we believe exists actually exist? Does the alert we believe fires actually fire against this technique? Does the 
escalation path we have documented actually work at 2am?

This is closer to chaos engineering applied to security assumptions than to a traditional red team engagement. The 
goal is to make model drift visible before an attacker finds it.

### Design for model failure

Assume the current models are wrong in ways you have not yet discovered. This is not pessimism; it is an accurate 
assessment of the state of any complex system.

The design question is: when a model fails, what is the blast radius? Architectures that segment failure, that limit 
what a single wrong assumption can reach, and that produce visible signals when assumptions are violated are more 
resilient than architectures that assume the models are correct.

## SEM for offensive work

Attackers benefit from exactly the same analysis. The models an organisation operates on are the assumptions that, 
when wrong, produce attack paths.

### Mapping beliefs as attack surface

A PSL and SEM-aligned red team asks not only what technical vulnerabilities exist but what the organisation believes 
that is false. These beliefs are often more durable as attack surface than individual vulnerabilities, because they 
persist across patching cycles and tool upgrades.

"This data is low sensitivity" produces inadequate protection regardless of how well the technical controls are 
implemented. "This system is isolated" produces trust relationships that can be abused. "This process is audited" 
produces blind reliance on a process that may have drifted from its intended function.

### Findings that describe model failures

A finding that says "over-permissive IAM role allows lateral movement" describes a symptom. A finding that says 
"no team owns IAM lifecycle, so permissions accumulate without review and the model that someone is responsible is 
incorrect" describes the model failure that will reproduce the symptom regardless of what is fixed today.

Model-level findings require a different class of remediation. They cannot be closed with a configuration change. 
They require someone to acknowledge that a belief the organisation has been operating on is wrong, which is a harder 
conversation than patching a service. That difficulty is worth documenting, because the resistance to having it is 
itself a security finding.
