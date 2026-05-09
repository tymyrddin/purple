# Measuring early success

How do we know purple teaming is working? Two kinds of measurement help.

## Activity metrics

The metrics most programmes report are activity metrics. They count things that can be counted, and they trend in the right direction as the team practises.

On the qualitative side: red and blue teams talking regularly and sharing information; teams treating gaps as opportunities rather than failures; the time between a finding and a fix shrinking; the two sides describing the same events in compatible terms.

On the quantitative side: the percentage of tested ATT&CK techniques that generate alerts (detection coverage); mean time to detect (MTTD) and mean time to respond (MTTR) for simulated attacks; the rate at which findings from one exercise are addressed before the next.

These metrics are useful. They are easy to track, easy to report, and they move in the right direction when the work is going well. They are also incomplete in a specific way.

## Activity metrics and behaviour change

The metrics above measure activity. They are necessary but not sufficient, and optimising for them without attending to what they represent produces a programme that looks healthy while the underlying capability stagnates.

Detection coverage increasing is not the same as an organisation becoming harder to attack. It may mean the team is getting better at building detections for the techniques that purple team exercises happen to use, while remaining blind to techniques the exercises have not covered. MTTD decreasing is not the same as response improving. It may mean the team is getting faster at closing tickets rather than getting better at investigating what those tickets represent.

The harder question, and the one that activity metrics do not answer, is whether behaviour has changed. Does the blue team approach an alert differently than it did six months ago? Does the red team communicate findings in a way that produces action rather than a report? Does the organisation treat a newly discovered gap as information to act on rather than as a problem to manage upward?

Behaviour change is slower to observe than metric change, less satisfying to report, and considerably more predictive of actual security improvement. One useful proxy: look at what happens when an exercise reveals a significant gap. If the organisational response is to assign it to the backlog and continue, the metrics may improve while the underlying capability does not. If the response is to treat it as a genuine priority, the metrics will probably look worse in the short term, as more gaps surface in a now-functioning feedback loop, before they reflect the improvement.

The [Satir arc](../../foundations/organisational-development/satir-change-model.md) applies here too. A programme that is genuinely improving will go through a period in which the metrics look alarming. That is not failure. It is the chaos phase of an organisation that has started telling itself the truth.

## Related

- [Coordination models](../coordination.md)
- [Applying SEM to security](../../foundations/system-effectiveness/applying-sem.md)
- [SOC maturity](../../incident-response/soc/maturity.md)
- [Risk register](../../risk-management/risk-register.md)
- [Organisational conditions for change](../conditions.md)
