# Systems, models, and errors

SEM works across three elements that are always present in any functioning (or dysfunctioning) security operation.

## Systems

A system is a set of interconnected parts whose behaviour emerges from interactions, not from the parts themselves. 
This is not abstract. It means that understanding each component of a security programme in isolation tells you very 
little about how the programme will behave under pressure.

A SIEM that works well in test conditions may produce alert fatigue in production because the volume of signals 
interacts with team capacity in ways the test did not replicate. A patching programme with sound tooling may stall 
because the interactions between the development workflow, the approval process, and the deployment window create 
friction the tooling alone cannot resolve.

The security environment is not infra plus applications. It is people plus process plus technology plus incentives 
plus timing. Behaviour emerges from the whole.

## Models

A model is a mental representation of how the system works. Everyone has them. Most are incomplete, partially wrong, 
or anchored to a state the system was in several years ago.

Some common examples in security:

"The network perimeter protects us." This model predates cloud-native architectures, remote work, and SaaS-heavy 
environments. Organisations that still operate on this model are making access and exposure decisions based on an 
architecture that no longer exists.

"IAM is centrally managed." In practice, IAM in most cloud environments is distributed, partially automated, partially 
manual, and partially forgotten. The model describes a governance intention, not an operational reality.

"Developers will take the secure path if it is documented." This assumes documentation is the binding constraint on 
developer behaviour. The actual binding constraints are usually speed, familiarity, and what the tooling makes easy.

Models are not lies. They are simplifications. The problem arises when they are treated as facts, especially by people 
who have decision-making authority based on them.

## Errors

Errors in the SEM sense are not bugs or mistakes. They are the mismatches between model and reality that produce 
consequences in the system.

The important word is "recurring." A one-time error may be a genuine anomaly. An error that appears repeatedly, in 
different forms but with the same underlying shape, is evidence that the model driving decisions is wrong in a way 
that has not yet been corrected.

Security calls this pattern by various names: recurring incidents, lessons not learned, known issues. SEM offers a 
more precise diagnosis: the model is wrong, and the system is providing evidence of that fact at regular intervals.

Fixing the symptom without correcting the model is the characteristic failure mode. Permissions get tightened after a 
lateral movement incident, the model that produced the overpermissioning is unchanged, and six months later a different 
role has the same profile for the same underlying reasons.

## Related

- [Applying SEM to security](applying-sem.md)
- [SEM for defence and red teaming](for-defence.md)
- [Integrating PSL, ChangeShop, SEM, and Satir OD](../organisational-development/composite-model.md)
- [Architecture as model](../../systems-architecture/architecture-as-model.md)
