# Organisational conditions for purple teaming to produce change

Purple teaming can be technically excellent and organisationally inert. The exercises run, the reports land,
the findings are acknowledged, and six months later the same gaps appear in the next exercise. This is not a
failure of methodology. It is a failure of conditions.

The foundations section covers the theory behind this at length. This page translates it into the specific
questions worth asking before and during a purple team programme.

## The political layer

Who has the authority to require that a finding from a purple team exercise results in a changed control, a
reallocated budget, or a modified process?

If the answer is "the CISO can recommend it," the findings will be recommendations. If the answer is "the
security function can raise it to leadership for consideration," the findings will wait their turn in a queue
of competing priorities. If the answer is "no one in security has that authority directly," then the programme
can surface risk without being able to close it, which is better than not surfacing it but is not what
most organisations think they are investing in.

The political layer question is not about blame. It is about leverage. Without it, purple teaming produces
excellent documentation of the current state, which is useful for reporting and useless for change.

## The emotional layer

How does it feel to have your detections tested and found wanting?

For a blue team analyst who has spent months building detection logic, an exercise that evades all of it is not
an abstract finding. It is a personal experience of inadequacy delivered in front of colleagues. How the
organisation responds to that experience in the first few exercises sets the behavioural pattern for everything
that follows. A response that treats the gap as a system problem (the technique was designed to evade the
detection category you were using: here is how to adjust for it) produces curiosity and engagement. A response
that treats the gap as a performance problem produces an analyst who stops caring whether the next exercise
succeeds, because caring is what made this one hurt.

The same applies to red team members asked to share their techniques openly with the blue team. For someone who
has spent time developing custom tooling and evasion methods, sharing them feels like giving away the advantage.
The framing that matters is that the organisation's resilience, not the red team's score, is the goal. That
framing has to be demonstrated repeatedly, not just stated.

## The model layer

Every purple team exercise encodes a model of the threat. If that model is wrong (the exercises target attack
paths that real adversaries are not using, the scenarios are drawn from historical incidents rather than
current intelligence, the complexity is calibrated to what the team is comfortable testing rather than what
they need to be tested on), the programme produces valid results about the wrong question.

The model layer problem is seductive because it feels like a technical problem. The solution appears to be
better threat intelligence, more sophisticated scenarios, a wider MITRE ATT&CK coverage map. All of those
help. But the model layer problem in most organisations is not primarily a lack of intelligence. It is that
the exercises are implicitly designed to produce manageable results: scenarios chosen because they are known
to be detectable, complexity calibrated to avoid the chaos phase, timing arranged to avoid disrupting
operations at inconvenient moments.

A programme that is designed to succeed will succeed, and will reveal nothing. The uncomfortable framing from
ChangeShop is that the exercise should be designed to find what the organisation is not ready for, not to
confirm what it already knows.

## The conditions worth building

Before investing in capability or complexity, the following conditions are worth establishing explicitly.

Someone, by name, has the authority and the genuine commitment to act on significant findings. Not to
acknowledge them, not to prioritise them against other work, but to treat them as requirements with owners and
timelines.

The debrief culture is set by what leadership does with the first uncomfortable finding. If that finding is
treated as information, the team learns that honesty is safe. If it is treated as an occasion for accountability,
the team learns to produce findings that will not cause discomfort.

The metrics reported to leadership are honest about what they measure. A rising detection coverage percentage
is not evidence that the organisation is harder to attack. A falling click rate in a phishing simulation is
not evidence that the organisation is more resilient to phishing. Reporting activity metrics as security
outcomes trains leadership to expect the wrong things and rewards the wrong behaviours.

The chaos phase is named in advance. When the programme starts surfacing more gaps than the previous approach
(because the previous approach was not looking very hard), the correct interpretation is that the programme is
working. That interpretation needs to be established before the metrics start looking alarming, not after.

## Related

- [The Satir Change Model](../foundations/organisational-development/satir-change-model.md)
- [What ChangeShop was/is](../foundations/change-management/what-it-is.md)
- [Why security change stalls](../foundations/change-management/why-change-fails.md)
- [When you're ready for purple teaming](readiness.md)
- [Common anti-patterns](antipatterns.md)
- [Measuring early success](measurements.md)
