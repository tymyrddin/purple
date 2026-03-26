# Architecture as model

An architecture document is a model. It represents the intended system: its components, their relationships, the constraints they operate within, and the assumptions that explain why the design takes the form it does. Like all models, it is a simplification, and like all simplifications, it is wrong in certain respects from the moment it is produced. The question is not whether an architecture is accurate but how quickly its inaccuracy becomes consequential.

## The [SEM](../foundations/system-effectiveness/index.rst) framing

Weinberg's [SEM](../foundations/system-effectiveness/index.rst) triad places models at the centre of how people understand and act on complex systems. The model is the mental representation of how the system works. The system is the actual thing, which behaves according to its own properties regardless of what the model says about it. Errors, in this framing, are not mistakes. They are mismatches between model and system, and they persist until the model is corrected rather than the symptoms treated.

An architecture document is a formalised, shared model. The SEM insight applied here is that the document's accuracy 
is not a property it has at the time of writing and retains indefinitely. It is a property that requires active 
maintenance, because systems evolve and models drift.

## How architectural models drift

Models drift through several mechanisms:

- Implementation divergence: the system as built differs from the system as designed, through technical constraints encountered during implementation, time pressure, changed requirements, or pragmatic decisions that were never documented as changes to the architecture.
- Environmental change: the systems and services the architecture depends on change their behaviour, their interfaces, or their availability. The architectural model was accurate when it was written; it is less accurate after a major dependency upgrade or a platform migration.
- Organisational change: the people and teams who understood the design decisions, including the reasons certain approaches were chosen and certain alternatives were rejected, change roles or leave. The documentation remains but the interpretive knowledge required to apply it is no longer present.
- Scope creep and accretion: systems accumulate components, integrations, and workarounds that were not in the original design. Each addition makes sense at the time. The aggregate effect is a system that increasingly diverges from the architecture's account of it.

## Why this is important for architects

Every role that depends on systems works with imperfect models. The reason this is specifically important for architects 
is that their explicit function is to produce and maintain the authoritative model of the system. When the architecture 
diverges from the actual system and that divergence is not noticed or addressed, the architecture loses its function: 
it cannot reliably inform design decisions, it cannot be trusted as a reference during incidents, and it cannot support 
communication between teams who need a shared understanding of the system.

The SEM principle that errors are model failures rather than system failures applies here. An architecture that 
consistently produces surprises during implementation is not a sign that the implementation team is incompetent. It 
is a sign that the architecture model encoded assumptions about the implementation context that turned out not to 
be true. The response to that finding is to correct the model, not to repeat the same assumptions with more insistence.

## The architect as model maintainer

Understanding architecture as model maintenance rather than one-time design production changes what the role requires. 
The initial design is the beginning of the work, not its completion.

Model maintenance means: reviewing the architecture against the actual system at regular intervals, treating 
implementation divergence as a signal that the model needs updating rather than evidence that the implementation 
was wrong, creating feedback loops from operations and from incident findings back into the architectural model, 
and making the assumptions the architecture encodes explicit enough that they can be challenged and updated as 
conditions change.

This is not a diminished vision of the role. It is a more accurate one. The architect whose model is continuously 
accurate is more valuable, and more trusted, than the architect whose comprehensive initial design becomes 
progressively less connected to reality over the following years.
