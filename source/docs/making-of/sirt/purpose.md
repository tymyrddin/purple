# Why a SIRT exists

The case for a security incident response team is not primarily a technical argument. The technical argument is straightforward: incidents happen, and an organisation that has no process for handling them handles them badly. That is true and mostly accepted. The harder question is why it so often takes a significant incident before the team gets built.

The [ChangeShop](../../foundations/change-management/index.rst) explanation is that the organisation's current state is already a system. It has found equilibrium without a SIRT. Incidents are currently absorbed, suppressed, treated as IT problems, or not identified as incidents at all. Each of these existing behaviours is connected to other behaviours, to role definitions, to implicit and explicit expectations about what gets reported and to whom. Adding a SIRT disrupts all of those connections simultaneously.

This is not a reason not to build one. It is a reason to be honest about what building one requires. The SIRT is not an addition to existing operations; it is a change to how the organisation processes the category of event called an incident. That change has to be owned somewhere, funded from somewhere, and protected from the pressure to defer it indefinitely.

## What a SIRT actually does

A SIRT provides the organisation with a coordinated response when something goes wrong that has security implications. Coordination here means: a shared understanding of what is happening, agreed roles for who does what, a process for escalating and communicating, and a mechanism for learning from the event once it is resolved.

Without coordination, each incident gets handled by whoever notices it first, using whatever resources and methods they have available. That produces inconsistent outcomes, incomplete records, and the same incidents recurring because the learning does not get captured and acted on.

The [SEM](../../foundations/system-effectiveness/index.rst) framing is useful here: the current response behaviour, however improvised, is a model. It encodes assumptions about which incidents are serious enough to escalate, who the right person is to escalate to, and what response means. Making those assumptions explicit is part of what building a SIRT accomplishes. The SIRT is a better model of how incidents should be handled, not just an additional team.

## What the organisation needs to provide

A SIRT requires four things that no amount of technical planning can substitute for:

Mandate: someone with organisational authority must decide that the SIRT exists, that it has the right to be involved in incidents, and that the organisation is expected to cooperate with it. A SIRT without a mandate has no way to obtain the access and information it needs when an incident occurs.

Resources: a SIRT whose members have no time allocated to SIRT work will not function. This does not require large dedicated headcount, but it does require protected time. Incidents are not evenly distributed, and a team that can only work on incidents when nothing else is happening will always have something else happening.

Authority: the SIRT needs the authority to declare an incident, to require containment actions, and to communicate externally when communication is required. Authority that has to be negotiated from scratch during an active incident is authority that arrives too slowly.

A learning culture: the [post-incident review](learning.md) process only works if people can describe what happened honestly without expecting blame. [Satir](../../foundations/organisational-development/satir-core.md)'s [survival stances](../../foundations/organisational-development/satir-core.md) are visible in SIRT work: the person who placates by saying everything was handled correctly when it was not, the person who blames another team for the gap, the person who computes by producing a technically accurate account that omits the important decision that was made under pressure. None of these produce useful learning. Creating conditions where people can be congruent, describing what actually happened and what they actually thought at the time, is as much a prerequisite as the technical tooling.
