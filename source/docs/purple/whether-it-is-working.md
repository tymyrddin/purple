# Whether it is working

The easy metrics are the activity ones, and they trend the right way as a team practises: the share of tested
techniques that raise an alert, the time to detect and to respond, the rate at which last exercise's findings
are closed before the next. They are worth tracking and they are also a trap, because they measure activity,
not outcome. Detection coverage climbing is not the same as being harder to attack; it can just mean the team
is getting good at detecting the techniques the exercises happen to use, while the ones they never cover stay
invisible. A falling time-to-detect is not the same as investigating better; it can mean tickets are closing
faster. And the denominator is where coverage lies most easily: a number drawn from what the team can already
detect climbs to nothing in particular.

A harder question, and the one the activity metrics dodge, is whether behaviour has changed. Does an alert
get approached differently than six months ago. Does a finding produce action rather than a report. The most
honest proxy is what happens when an exercise turns up a real gap: filed to a backlog and passed over, and the
metrics can look healthy while nothing underneath moves; treated as a genuine priority, and the metrics will
likely look worse for a while, as more gaps surface in a feedback loop that has started working, before they
get better. A programme that has begun telling itself the truth goes through a spell where the numbers look
alarming. That spell is a sign it is working, and it helps to have said so before the numbers arrive.

Where finer measurement helps, it is in the movement over time rather than the level: a falling share of
objectives the attacker still reaches, a rising number of distinct techniques it takes to get there, more of
each attack path lit up even when the objective is met. Read together, those say the defences are forcing the
attacker onto longer, louder, less certain routes. Read alone, any one of them can be gamed.

Maturity, if the word earns its place at all, is less a ladder to climb than a description of how tight the
loop has become: from occasional exercises whose findings mostly evaporate, to a regular cadence with findings
that get closed, to continuous testing where coverage is checked between sessions. The traps are consistent
across programmes. Framing it as red against blue, so the score counts for more than the learning. Running
exercises with no follow-through, so findings pile up and nothing changes. Reaching for complexity the
organisation cannot yet act on. And the quiet one, a debrief that goes looking for who missed the alert, which
teaches everyone to surface fewer of them next time.

## Related

- [Whether you are ready](whether-you-are-ready.md)
- [What it leaves behind](what-it-leaves-behind.md)
- [SOC maturity](../incident-response/soc/maturity.md)
