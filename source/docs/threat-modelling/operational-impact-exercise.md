# Operational impact exercise

Impact assessment is where the threat model connects to what actually matters to the organisation: not systems failing, but operations failing, people being affected, and recovery consuming resources that were needed elsewhere.

It is also where the [Satir](../foundations/organisational-development/satir-core.md) dynamics are most visible. Naming the operational consequences of a successful attack requires people to say uncomfortable things in front of colleagues: that a service would be down for days, not hours; that customer data would be exposed, not just at risk; that regulatory consequences would be serious, not manageable. The [survival stances](../foundations/organisational-development/satir-core.md) appear reliably here. Some people placate (the impact would probably not be that bad). Some compute (let me give you the technical explanation of what would fail). Some deflect (that is really a question for the business continuity team).

The facilitator's role is to keep the group in contact with the realistic scenario rather than the reassuring one. The political layer matters too: who in the room has the authority to acknowledge a given impact? A finding that requires someone to admit that a critical service could be unavailable for a week is a finding that will only be documented accurately if the person who needs to act on it is present and willing to own it.

## The exercise

Take one attack path from the [previous exercise](attack-path-mapping.md). Choose one that reaches a critical asset, not the most technically interesting one.

Assume the attack succeeds. This is the important step: not "what could prevent this" but "what happens next." Resistance to the assumption is itself informative.

Work through three questions:

What operations fail? Name specific services, processes, and functions, not general categories. Not "operations would be disrupted" but "invoice processing stops, the customer portal goes down, and the warehouse management system loses its data feed."

Who is directly affected, and how quickly? Staff, customers, suppliers, regulators. Name the groups and the timeframe. If the group does not know the timeframe, that is a finding.

How long until normal operations resume? This requires honesty about recovery capability that the group may or may not have. If nobody knows the answer, that is the finding.

Capture the key impacts on one sheet. The sheet should be specific enough that a decision-maker who was not in the room can understand what is at stake.

## What this exercise is really doing

Beyond the outputs, this exercise is testing whether the organisation can have a clear-eyed conversation about its own vulnerability. Groups that cannot complete the exercise honestly, that consistently soften the impacts or redirect to what they would do to prevent it, are showing something about the conditions for change in the organisation.

That observation is worth bringing to the group, carefully: the difficulty of naming the impact is related to the difficulty of acting on the finding. If acknowledging a three-day outage feels too alarming to say aloud, the discussion about how to prevent it will be shaped by the same discomfort.

## Related

- [Attack path mapping](attack-path-mapping.md)
- [Bringing it together](bringing-it-together.md)
- [Core ideas of Satir systems OD](../foundations/organisational-development/satir-core.md)
- [Risk assessment](../risk-management/risk-assessment.md)
