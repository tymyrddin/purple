# Resilience, continuity, and disaster recovery

These three terms tend to be used interchangeably, though they are not interchangeable. The
distinction is usually invisible until something fails, at which point the wrong word can
produce the wrong response.

## Three properties, three timescales

Resilience is a property of the system. It is the capacity to absorb shock without falling
over. It lives in design, in redundancy, in headroom, in the slack that gets cut first when
budgets tighten.

Continuity is a property of the organisation. It is the capacity to keep doing the work,
possibly badly, while something is broken. It lives in process, in delegation, in the
improvisation that staff do when the plan stops being applicable.

Disaster recovery is a property of the technology. It is the set of procedures and
capabilities that bring specific systems back from a defined failure. It lives in tooling,
contracts, runbooks, and the test restores that were scheduled and quietly skipped.

The three operate on different timescales. Resilience is continuous: it is the property the
system has all the time, whether anyone notices or not. Continuity engages the moment something
starts to fail and runs for as long as the disruption lasts. Disaster recovery is a discrete
episode with a beginning and, eventually, an end. Treating them as one bucket usually produces
underinvestment in continuity, the messy middle, because it is the least amenable to a tidy
deliverable.

## Each one in isolation

A resilient datacentre can still leave an organisation stranded if the people who knew how to
operate it have all left, or if the contract that pays for it has lapsed during the outage.

A continuity plan that does not include any technical recovery tends to be a list of
workarounds with no end state, which an organisation may eventually settle into permanently
because nobody has the capacity to undo them.

A disaster recovery procedure that restores systems by Tuesday may not help if customers,
regulators, or staff have already drawn their conclusions about the organisation by Monday
afternoon.

The combination of all three appears to be rarer than the documents suggest. Many
organisations have strong pieces of one, fragments of another, and an unspoken assumption that
the third will be handled by someone else when the time comes.

## The cost of conflation

Confusing the three tends to push investment toward whichever one feels most tractable, which
is almost always disaster recovery, because it has discrete deliverables and named systems. The
result can be organisations with credible RTO numbers for the database and no plan for how the
finance team will issue invoices on the day the database is being restored.

Naming the three separately can let the conversation about each one be honest. The resilience
conversation is about design tradeoffs. The continuity conversation is about organisational
behaviour under pressure. The disaster recovery conversation is about specific runbooks against
specific systems. Lumping them together tends to produce a continuity plan that is mostly DR,
which appears to be the most common failure mode.

## Related

- [Operational dependency mapping](dependencies.md)
- [Recovery objectives and what they mean](objectives.md)
- [Continuity through a foundations lens](foundations.md)
- [Risk treatment options](../risk-management/treatment-options.md)

*Last updated: 9 May 2026*
