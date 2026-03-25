# Building a model

A threat model turns the outputs of separate exercises into a structured, maintainable picture. The word "maintainable" is doing important work. A threat model that cannot be updated is not a model of the current system; it is a historical record of an earlier one.

## What the model contains

Review all previous exercises: adversary personas, attack paths, operational impacts, and scenarios. Organise the findings into a structure that shows the relationships between them.

The model needs four components: the adversaries (who, with what capabilities and motivations), the attack paths (how they would move through the system from entry to objective), the operational impacts (what the consequences would be if each path were executed successfully), and the mitigations (what is already in place and what is planned).

## Making it legible outside the workshop

One test of a useful threat model is whether someone who was not in the exercises can read it and understand what the group believes about the organisation's exposure and why. This is harder than it sounds. Workshop discussions are contextual and rely on shared understanding that does not survive the transition to a document.

The attempt to make the model legible to an outsider is itself analytically useful. The places where the documentation becomes vague or qualified are usually the places where the group's understanding is thinner than it appeared in discussion. "The attacker would need to pivot through the internal network" is a description of an assumption, not a description of a known path. Making that distinction visible in the document is the difference between a model that can be tested and one that can only be believed.

## The top risks

Highlight the two or three findings that represent the most significant exposure given realistic adversaries and current conditions. Not the most technically interesting, not the ones that were easiest to document, but the ones where the combination of likelihood, access, and impact is most concerning.

For each, note what would need to be true for this risk to be reduced to acceptable levels, and who would need to decide and act to make that happen. If those conditions are not currently in place, that gap is part of the finding.

## Maintaining the model

Assign an owner. The threat model will drift toward obsolescence at the rate the environment changes. Without an owner who is responsible for keeping it current, it will not be kept current regardless of how well the initial exercises were run.

Document the assumptions the model depends on. The model assumes that a specific system is isolated from the production network. It assumes that contractor access is mediated through a specific gateway. It assumes that the billing system does not have a direct connection to the customer database. Each of these assumptions is a test that can be run and a trigger for updating the model if the test fails.

Set the triggers for revision explicitly: new system additions, significant architectural changes, incidents that resemble a modelled scenario, changes in the threat intelligence picture relevant to the named adversaries. A model revised on a fixed calendar schedule regardless of environmental change is a model that will be wrong in unpredictable ways. A model revised when its assumptions are violated is a model that stays accurate.
