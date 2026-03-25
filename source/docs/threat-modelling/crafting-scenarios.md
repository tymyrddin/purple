# Crafting scenarios

A scenario turns an attack path into a narrative: a specific sequence of events, with a specific adversary, producing specific consequences. Scenarios make abstract risks concrete enough to reason about, practise against, and communicate to people who were not in the threat modelling workshop.

The relationship to scenario planning is direct. Scenario planning (in the workshops section) asks what futures are possible. Threat modelling scenarios ask how a specific adversary would produce one of those futures. The two practices feed each other: threat modelling scenarios sharpen the adversarial content of strategic scenarios, and strategic scenarios provide the organisational context that makes threat modelling scenarios realistic.

## The exercise

Take one or two attack paths from the previous exercise. Choose paths that reached critical assets and produced significant impacts.

Write a short scenario for each. The scenario should include the adversary persona, the sequence of moves from entry to objective, and the operational impact when the objective is reached. One page or one index card is the right length. Longer scenarios become hard to use.

The sequence of moves is the part that takes most attention. A scenario that says "the attacker gains access and exfiltrates data" is not a scenario. A scenario that says "the attacker sends a targeted email to a finance administrator, obtains credentials for the payment system, spends three days moving laterally without triggering alerts, and extracts transaction records over a weekend" is usable for planning, detection engineering, and response preparation.

## The peer swap

Once each group has a scenario, swap with another group. Read their scenario and identify weak points and overlooked risks: places where the scenario assumes something about detection that may not hold, places where the timeline seems optimistic, places where a different adversary with different capabilities would have taken a different path.

This is the Montessori peer review in action. The group that wrote the scenario is inside its own assumptions. The group that reads it from outside notices the gaps. The conversation that follows is usually more valuable than either group's individual work.

## What makes a scenario useful

A useful scenario is specific enough to act on. Someone reading it should be able to say: we would or would not detect this step, we do or do not have a response procedure for this situation, we would or would not be able to recover within the timeframe the scenario implies.

A useful scenario is also honest about the adversary's capabilities. Scenarios written against an adversary the organisation is comfortable defending against are useful for confidence but not for capability development. The scenarios worth practising against are the ones where the honest answer to "would we detect this?" is "probably not."

## Keeping scenarios current

Like all models, scenarios drift. A scenario written against last year's adversary using last year's techniques against last year's architecture is a historical document, not a current planning tool. Mark each scenario with the date it was written and the trigger conditions for revisiting it: a new system in scope, a new technique observed in the threat landscape, an incident that resembles part of the scenario.
