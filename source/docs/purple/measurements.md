# Measuring early success

How do you know purple teaming is working?

## Qualitative indicators

Improved communication: Red and blue teams talk regularly, share information, collaborate on priorities.

Learning mindset: Teams view gaps as opportunities rather than failures. Psychological safety enables honest assessment.

Faster improvement: Time between discovering gaps and implementing fixes decreases.

Shared understanding: Teams use common language (MITRE ATT&CK, TTP terminology, etc.) and agree on priorities.

## Quantitative indicators

Detection coverage: Percentage of tested ATT&CK techniques that generate alerts increases.

Detection speed: Mean time to detect (MTTD) for simulated attacks decreases.

Response effectiveness: Mean time to respond (MTTR) and quality of response improve.

Remediation rate: Findings from exercises get fixed before next exercise. Gap backlog decreases rather than grows.

## The difference between activity metrics and behaviour change

The metrics above measure activity. They are necessary but not sufficient, and optimising for them without
attending to what they represent produces a programme that looks healthy while the underlying capability
stagnates.

Detection coverage increasing is not the same as the organisation becoming harder to attack. It may mean the
team is getting better at building detections for the techniques that purple team exercises happen to use, while
remaining blind to techniques the exercises have not covered. MTTD decreasing is not the same as response
improving. It may mean the team is getting faster at closing tickets rather than getting better at investigating
what those tickets represent.

The harder question, and the one that activity metrics do not answer, is whether behaviour has changed. Does the
blue team now approach an alert differently than it did six months ago? Does the red team communicate its
findings in a way that produces action rather than a report? Does the organisation treat a newly discovered gap
as information to act on rather than as a problem to manage upward?

Behaviour change is slower to observe than metric change, less satisfying to report, and considerably more
predictive of actual security improvement. One useful proxy: look at what happens when an exercise reveals a
significant gap. If the organisational response is to assign it to the backlog and continue, the metrics may
improve while the underlying capability does not. If the response is to treat it as a genuine priority, the
metrics will probably look worse in the short term (as more gaps are surfaced by the now-functioning feedback
loop) before they reflect the improvement.

The Satir arc applies here too. A programme that is genuinely improving will go through a period in which the
metrics look alarming. That is not failure. It is the chaos phase of an organisation that has started telling
itself the truth.

## Related

- [Coordination models](coordination.md)
- [Applying SEM to security](../foundations/system-effectiveness/applying-sem.md)
- [SOC maturity](../making-of/soc/maturity.md)
- [Risk register](../risk-management/risk-register.md)
- [Organisational conditions for change](conditions.md)
