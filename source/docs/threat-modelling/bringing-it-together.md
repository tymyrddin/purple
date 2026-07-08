# Bringing it together

This exercise assembles the outputs of the previous sessions into a coherent threat model. It is also the moment when
the gap between "having done the exercises" and "having produced something that will change how the organisation
behaves" becomes visible.

The group has done genuine analytical work. They have built personas, mapped paths, and assessed impacts. The question
now is one the analytical work cannot settle on its own: whether the [conditions for
acting](../foundations/change-management/what-it-is.md) on those findings are in place, given how reliably [organisations
resist the change they asked for](../foundations/change-management/index.rst). A threat model that accurately describes
the organisation's exposure and then sits in a shared drive is not a threat model in any useful sense. It is a
description of risk that the organisation chose not to act on.

This is not a failure of the exercise. It is a finding about the organisation, and it deserves to be named as one.

## The exercise

Combine the [adversary personas](adversary-persona-workshop.md) with the [mapped attack paths](attack-path-mapping.md).
For each path, note the persona or personas that could execute it and the operational impact if they do.

Prioritise. Which risks are unacceptable given the organisation's actual risk appetite, not the stated one? Which can be
tolerated?

The distinction between stated and actual risk appetite is important: organisations frequently say they have
a low appetite for certain risks and then routinely accept them in practice. The gap between those two is
worth naming.

Decide on next steps for each priority risk: specific mitigations with owners, monitoring approaches, or explicit
acceptance with the conditions under which the acceptance would be revisited. "Awareness" without an owner and a
timeline is not a next step.

## Reading the assembled model

Look at the model as a whole. Where are the chokepoints, the paths that appear most often and the assets that most
frequently appear as objectives?

These are the places where investment in defence produces the most leverage. Chokepoints and priority risks also make
workable [purple team engagement objectives](../engagement/objectives.md): specific, testable, and already agreed to be worth testing.

Also look for what is not in the model. The threats that were raised and then set aside, the attack paths that nobody
wanted to map, the impacts that were softened in discussion. These gaps are findings about the model's blind spots and
about the conditions that produced them.

## The model is already drifting

The moment the workshop ends, the model begins to diverge from reality. New systems go live, integrations change,
adversary techniques evolve, organisational structures shift. The threat model is not a completed artefact; it is a
snapshot with a timestamp.

Set explicit triggers for revisiting the model, so a review happens when something changes rather than when the calendar
says so: a significant new system or integration is added, an incident resembles a scenario in the model, a new
adversary technique becomes relevant, or the threat intelligence picture changes substantially. Without triggers, the model will be reviewed at the scheduled annual date
regardless of whether it is still accurate, which is the worst of all review schedules.

## Whether the findings will produce change

Before closing, address this directly: who in the room has the authority and the capacity
to [act on each priority finding](../practice/acting-on-findings.md)? If the answer for a critical finding is "nobody
present," then either the right person needs to be brought into the conversation or the finding needs to be escalated. A
threat model whose highest-priority findings have no owner is a document, not a programme.

What remains is [crafting scenarios](crafting-scenarios.md) for the priority paths,
then [building the model](building-model.md): assembling everything into something an owner can maintain.

*Last updated: 3 July 2026*
