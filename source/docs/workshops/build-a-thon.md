# Build-a-thon

A build-a-thon is a focused collaborative event in which a security team spends concentrated time building something real: a detection rule, a playbook, a sandboxed exercise, a monitoring dashboard, a shared reference that has been needed for months but never quite prioritised. The output is something usable, not a slide deck or a proposal.

The distinction from a hackathon is one of orientation. Hackathons tend to reward novelty and produce prototypes that 
do not survive contact with the production environment. A build-a-thon is oriented toward operational usefulness: 
things that will actually be used by the team, in the actual environment, after the event ends.

## What to build

The best candidates for a build-a-thon are things that are genuinely needed, clearly scoped, and buildable within the 
time available by the people in the room.

Detection content: rules, queries, or correlation logic for techniques that are known to be used by relevant 
adversaries but are not yet covered by existing monitoring. Purple team exercises and [threat modelling](../threat-modelling/choreography.md) sessions are 
natural sources for this list.

Playbooks: documented response procedures for scenarios that are likely but not yet covered, or for scenarios where 
the existing procedure has been found inadequate in a retrospective or exercise. A playbook built by the people who 
will use it, during a session where they can work through the logic together, is more likely to be followed than one 
written by a single analyst.

Exercises and lab scenarios: prepared environments for future training, modelled on real techniques and real conditions. These take time to build well, and a build-a-thon creates the protected time and the collaborative conditions that make building them feel worthwhile.

Tooling and automation: scripts, workflows, or integrations that reduce the friction in a commonly performed task. The constraint here is that the output needs to be something the team will actually maintain, not something that works on the day and is abandoned a month later when the person who built it is unavailable to fix it.

## Preparing the event

Gather proposals in advance. Ask the team what they have wanted to build but have not had time for. Collect the list, group related items, and let the team vote or select on the day. This surfaces what is actually felt as useful rather than what a manager believes is useful.

Prepare the environment before the event starts. A build-a-thon where the first three hours are spent getting access to systems, finding documentation, or waiting for permissions to be granted is a build-a-thon that has lost its momentum before the work begins. This is the [Montessori](../foundations/montessori/index.rst) prepared environment principle applied directly: everything needed is accessible without ceremony.

Set a clear finishing condition. Each project benefits from a stated definition of done that is achievable within the time available. "Finished enough to be useful" is a legitimate bar.

## Running it

Organise in small groups of two to four, each working on a single project. Mixing skills is useful: a detection engineer and an analyst working on a detection rule together produce something more operationally grounded than either would alone.

Keep interruptions minimal. The value of the build-a-thon is the protected time and attention. The event works best treated as genuinely protected, not as a day where people also attend their normal meetings.

Hold a brief mid-event check-in to surface projects that are stuck and may need rescoping, and to share early progress across the groups. Progress is contagious. Seeing that other teams are producing real things helps groups that are slower to get started.

## Closing and handover

End with each group presenting what they built in ten minutes or less: what it is, what problem it addresses, and how to use it. Keep the presentations functional rather than polished.

The handover is critical. Anything built during the event needs a clear owner, a home in the relevant documentation or repository, and a brief note on what conditions would indicate that it needs updating. A build-a-thon that produces things that live only on the laptops of the people who built them has produced activity rather than capability.

A retrospective using the rapid retrospective format closes the event. What got built? What did not get finished and why? What would make the next one better?

## Related

- [Rapid retrospectives](rapid-retrospectives.md)
- [The prepared environment](../foundations/montessori/prepared-environment.md)
- [Knowledge transfer: playbooks](../knowledge-transfer/playbooks.md)
- [Patch sprint](patch-sprint.md)
