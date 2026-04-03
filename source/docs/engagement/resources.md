# Resource planning

Engagements require time, people, tools, and sometimes external spend. The rational layer of resource planning is straightforward: estimate the hours, identify the people, confirm the tools are available. Most engagement plans do this adequately.

What most resource plans miss is the [PSL political layer](../foundations/problem-solving/in-security.md). Staff time allocated to an engagement is time taken from other work. Whether that trade-off is genuinely supported by the people asked to make it, or whether it is nominally agreed and resented in practice, determines how the engagement actually runs. A red team operator doing engagement work alongside a full delivery load will not produce the same quality of work as one who has protected time. A blue team running a live exercise while also managing a production incident is not running the exercise the plan described.

The resource plan should be honest about these constraints rather than optimistic about them. An engagement that is adequately resourced and well-run produces more value than an ambitious one that is stretched thin.

## Time

Planning takes longer for the first engagement than for subsequent ones: one to two weeks for a new programme, faster once patterns are established. Build in time for reconnaissance and preparation before execution begins; an underprepared red team produces unrealistic pressure. Documentation and debrief are where the learning is consolidated; cutting them under time pressure is cutting the most valuable part.

## People

The testing team benefits from clear scope and protected time. The defending team is more useful when staffed to reflect realistic incident conditions rather than ideal ones. If the engagement will run with a skeleton crew because three analysts are on holiday, that is worth knowing before it begins.

A facilitator with no stake in either side's performance is what makes the debrief work. Seniority matters less than genuine neutrality and the understanding that the job is to surface learning, not to judge either team.

## Tools and infrastructure

The testing team needs tools that match the threat scenarios being simulated, and a safe environment to operate them from. The defending team needs functioning monitoring, detection, and response tooling; an engagement that tests defences against a broken SIEM is not testing the defences.

Access to a safe test environment that mirrors production closely enough to be realistic is worth the overhead of maintaining it. The gap between the test environment and production is itself worth documenting: it represents assumptions that are not being tested.

## Related

- [Objectives](objectives.md)
- [Safety and risk management](safety.md)
- [PSL applied to security work](../foundations/problem-solving/in-security.md)
