# Change and homeostasis

Every architectural decision is an intervention in a system that already exists. Even when the architecture is for a new system, it is being built within an organisation that already has processes, investments, skills, and expectations. The new system will connect to existing systems, be operated by existing teams, and be governed by existing policies. The organisation is already in a steady state, and the architecture is a disturbance to that state.

## The [ChangeShop](../foundations/change-management/index.rst) framing

Weinberg's ChangeShop framework observes that organisations behave like [homeostatic](../foundations/change-management/what-it-is.md) systems: they have reached their current state through accumulated decisions and they resist changes that disturb it, not out of obstruction but because homeostasis is what systems do. Every change that moves a system away from its current state triggers forces that tend to return it to the prior state.

The ChangeShop insight is not that change is impossible. It is that change requires the creation of conditions under which the new state is stable, not just the introduction of a new design. An architectural change that addresses the technical requirements without addressing the conditions for the new state to take root will produce a pattern that architects recognise: the architecture is approved, the implementation is complete, and two years later the system operates largely as it did before.

## What homeostasis looks like in architecture work

The homeostatic resistance to architectural change takes several recognisable forms:

Technical debt as status quo protection: existing patterns become entrenched because changing them requires effort that has never been allocated and never will be, not because the patterns are preferred but because the change has no protected path through the organisation's priorities.

Shadow architectures: teams that cannot work with the official architecture, because it does not accommodate their actual requirements or because the approval process is too slow, create unofficial architectures that coexist with the official one. The official architecture then describes an increasingly fictional version of the system.

Nominal compliance: teams adopt the architectural vocabulary without adopting the architectural intent. The new integration pattern is used in the parts of the system where it was explicitly required and not used elsewhere. The architecture has changed in description but not in the underlying behaviour that the description was meant to produce.

Reversion under pressure: during incidents, during periods of high delivery pressure, or during periods of team change, teams revert to practices they were familiar with before the architectural change. This is not a failure of commitment; it is the system returning to the state it knows under conditions where the investment required to maintain the new state is unavailable.

## Designing for the organisation as well as the system

The ChangeShop framing implies that the architect's work is not complete when the design is technically sound. It is complete when the conditions for the design to be implemented and sustained are in place.

Those conditions include: ownership that is genuine rather than nominal, with people who have both the authority and the capacity to implement the architectural direction; protected time and budget for implementation, without which the architecture will be deferred in favour of more immediately pressing demands; a feedback mechanism that surfaces implementation problems before they become entrenched; and the trust and communication conditions that allow people to raise concerns about the architecture during implementation rather than routing around it silently.

These are not soft concerns that can be handed off to a project manager. They are architectural concerns, because their absence produces architectural outcomes. An architect who scopes their work to exclude them will produce technically correct designs that fail organisationally.

## Resistance as information

The ChangeShop principle that resistance should be treated as information rather than obstruction is particularly valuable in architecture work. When a proposed architectural change meets significant resistance from teams who will be affected by it, the resistance is data about the current state that the architecture may not have fully accounted for.

That does not mean resistance should always be accommodated. It means it should be understood before being dismissed. Resistance that reflects a genuine constraint or a real concern about the design deserves a response at the design level. Resistance that reflects a preference for the familiar deserves acknowledgement and a clear account of why the change is necessary. In both cases, treating the resistance as information produces better outcomes than treating it as an obstacle to be overcome.
