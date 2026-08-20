# Systems, models, and errors

Three things are in play whenever a security operation works, and the same three when it stops working: the system
itself, the models people hold of it, and the errors thrown off where the two disagree.

## Systems

A system is a set of interconnected parts whose behaviour emerges from interactions rather than from the parts
themselves. A component understood thoroughly in isolation still says very little about how the programme around it
behaves under pressure.

A SIEM that performs well in test can produce alert fatigue in production, because the volume of signals meets team
capacity in a way the test did not replicate. A patching programme with sound tooling can stall because the development
workflow, the approval process and the deployment window between them generate friction the tooling alone does not
resolve.

A security environment is not infra plus applications. It is people plus process plus technology plus incentives plus
timing. Behaviour emerges from the whole.

## Models

A model is a mental representation of how a system works. Everyone carries them, and many are incomplete, partly wrong,
or anchored to a state the system left behind some time ago.

"The network perimeter protects us" is a model that
[predates cloud-native architectures](../../systems-architecture/architecture-as-model.md), remote work and SaaS-heavy
environments. An organisation still operating on it is making access and exposure decisions about an architecture that
no longer exists.

"IAM is centrally managed" describes a governance intention. IAM in many cloud environments is distributed, partly
automated, partly manual and partly forgotten.

"Developers will take the secure path if it is documented" makes documentation the binding constraint on developer
behaviour. The binding constraints are more often speed, familiarity, and whatever the tooling makes easy.

Models are not lies. They are simplifications, and the trouble usually starts when they get
[treated as facts](for-defence.md) by people whose decisions rest on them.

## Errors

Errors in the SEM sense are neither bugs nor mistakes. They are the mismatches between model and reality that produce
consequences, and the interesting ones repeat. A single error may be a genuine anomaly. An error that turns up again and
again, in different forms but with the same shape underneath, is evidence that the model driving decisions is wrong and
has not yet been corrected.

Security has its own names for that pattern: recurring incidents, lessons not learned, known issues. SEM puts it more
precisely. The model is wrong, and the system is filing evidence to that effect at regular intervals.

[Fixing the symptom and leaving the model alone](applying-sem.md) is a characteristic failure. Permissions get tightened
after a lateral movement incident, nothing touches the model that produced the overpermissioning, and six months later a
different role carries the same profile for the same reasons. The ticket closes. The mechanism does not.

*Last updated: 11 August 2026*
