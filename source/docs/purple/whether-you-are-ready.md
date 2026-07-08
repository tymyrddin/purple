# Whether you are ready

Purple teaming makes sense once an organisation has the makings of a defensive function and the willingness
to learn from its gaps. Start earlier and it surfaces problems there is no way to act on; start later and the
gaps it would have found have already arrived as incidents.

The technical minimum is small but real. There has to be something to test: basic visibility, centralised
logging, some endpoint and network monitoring, or the exercise lands against nothing and reports only its own
absence. There has to be a defensive owner, even part-time, or the findings have nowhere to go and sit in a
folder. There has to be a safe place to run it, an isolated environment or production with scoped limits,
because an exercise that breaks production teaches only that exercises are dangerous. And there has to be
someone who can play the attacker credibly, not an elite operator but someone who understands the techniques
well enough to run them realistically and safely; early on that seat can be filled from outside, as long as
the two sides stay tightly coordinated rather than drifting onto separate timelines.

The cultural minimum is the harder half. Someone needs the authority to [turn a finding into a change](../practice/acting-on-findings.md), not just
an acknowledgement; where security sits below the line at which budgets are decided, findings become a list
everyone agrees is important and no one has time to close. And the room has to stay honest under pressure,
which is where most of the difficulty lives. Teams under stress slide into telling the facilitator what it
wants to hear, or answering every gap with a new process rather than a new capability, or naming the person
who missed the alert rather than the system that made missing it likely. None of those learn anything. An
exercise run into that pattern surfaces it rather than solves it, which is worth knowing but calls for a
different repair than more exercises.

A few patterns argue for waiting. No monitoring to see with, so visibility comes before testing it. No
response procedures to exercise, so the findings are a build list rather than a test. A purely
compliance-driven function, where an exercise that walks through a control in five minutes contradicts the
attestation that the same control is effective, and nobody has decided which reading is the real one. And an
already adversarial relationship between the two sides, which a formal exercise amplifies rather than heals;
that one is worth fixing first.

Who is in the room changes with size. In a small organisation the same people attack one week and defend the
next, and the rotation itself teaches something; the cadence is a scheduled quarter or half-year, not
continuous. A medium one can separate the sides, even where both are small, and gains a facilitator, whose
job is conditions rather than content, checking both sides have prepared, holding the debrief, and tracking
what actually changed. A large one runs dedicated teams and can move toward continuous work, when the culture
and tooling are already there to carry it.

## Related

- [Running the loop](running-the-loop.md)
- [Whether it is working](whether-it-is-working.md)
- [Incident response](../incident-response/index.rst)

*Last updated: 2 July 2026*
