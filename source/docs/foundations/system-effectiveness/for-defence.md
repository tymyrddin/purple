# SEM for defence and red teaming

[SEM](core-triad.md) reads the same way from both sides of the engagement. For defenders it surfaces the assumptions
that produce blind spots. For offensive work it redraws the attack surface.

## SEM-informed defence

A security posture usually carries a set of beliefs nobody has checked recently, or ever. Finding them starts with
asking which of them, if wrong, would cost the most. The exercise stings, and the sting is the useful part: it shows how
much of the posture rests on trust rather than on verification. When was the network segmentation model last validated
against actual traffic? What does detection engineering assume about what "normal" looks like in the estate as it stands
now? Which services are assumed internal and have not been audited for external exposure?

Assumptions degrade on their own. An environment changes, an assumption does not, and a model drifts out of true without
anyone noticing.

[Deliberate model testing](../../crucible/experiments/index.rst) is not penetration testing. It puts specific questions
to the estate. Does the isolation believed to exist actually exist? Does the alert believed to fire actually fire
against this technique? Does the documented escalation path work at two in the morning? The nearest relative is chaos
engineering pointed at security assumptions rather than at infrastructure, and the goal is to make
[model drift visible before an attacker finds it](applying-sem.md).

Some models are wrong in ways not yet discovered. In any complex system, some always are. The design question that
follows is how far a wrong one reaches before anything stops it. An architecture survives its own errors better when it
segments failure, caps what a single wrong assumption can touch, and signals a violated assumption loudly. One built on
the premise that its models are right does not.

## SEM for offensive work

The models an organisation operates on are the assumptions that, when wrong, open attack paths.

A red team working from [Problem Solving Leadership](../problem-solving/in-security.md) and SEM asks not only which
technical vulnerabilities exist but which of an organisation's beliefs are false. False beliefs are often more durable
than individual vulnerabilities, because they survive patching cycles and tool upgrades. "This data is low sensitivity"
produces thin protection however well the controls are implemented. "This system is isolated" hands an attacker trust
relationships to abuse. "This process is audited" produces reliance on a process that may have drifted from whatever it
was meant to do.

A finding that says "over-permissive IAM role allows lateral movement" describes a symptom. A finding that says "no team
owns IAM lifecycle, so permissions accumulate unreviewed and the belief that someone is responsible is false" describes
the failure that reproduces the symptom whatever gets fixed today.

Model-level findings need a different class of remediation. No configuration change closes them. They need someone to
accept that a belief the organisation has been running on is wrong, which is a harder conversation than patching a
service. The resistance to having that conversation belongs in the report, because it is itself a security finding.

*Last updated: 11 August 2026*
