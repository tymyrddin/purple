# Testing the defences

From implementation evidence to effectiveness evidence.

A fortress that has never been probed is a hypothesis with battlements. Every stage so far has produced
documentation: a survey, a threat register, a zone model, a control mapping. This stage is where the claims in
that documentation get tested against behaviour, converting implementation evidence into
[effectiveness evidence](../../foundations/system-effectiveness/applying-sem.md) before an incident or an auditor
does the converting less kindly.

## Matching tests to claims

Each adversary category from [knowing the besiegers](besiegers.md) is a scenario that can be run:

* An opportunistic attacker exploiting default credentials is a PoC against the actual device configuration.
* A targeted attacker probing segmentation is a controlled penetration test scoped to the relevant zones, checking whether the [walls and gates](walls-and-gates.md) hold where the diagram says they do.
* A malicious insider misusing privileged access is a monitored access review exercise checking whether logs would surface the behaviour.
* Protocol abuse is a targeted fuzzing run or a red team exercise scoped to OT protocols.
* The incident response chain is a tabletop under time pressure, with the people currently on shift rather than the ones who wrote the plan.

Controls that have only been mapped to adversaries, and never tested against them, are predictions about
containment, not evidence of it.

## Testing without stopping the factory

OT environments punish careless testing: a scan that a web server shrugs off can wedge a PLC. Testing choices
reflect this. Staging environments and representative targets carry the intrusive work; production systems get
passive analysis, read-only verification, and carefully scoped exercises in maintenance windows. A test plan that
could not explain, for each activity, why it cannot disrupt the process it is defending, is not ready to run.
The constraint is not a reason to skip testing; it is a reason to design it.

## Reading the results

A finding is a model correction, not just a defect. Segmentation that failed under test is telling you the zone
model and the network diverged; a detection signature that never fired is telling you the monitoring assumed a
technique the attacker did not use. Findings route back to the stage that owns the broken assumption: the zone
model, the control mapping, sometimes the threat register itself. A test report filed without changing anything
upstream has been read as a certificate rather than as feedback.

## Practical gap-spotting

* Coverage: every zone with a demanding security level target has test history against the adversary class that target names.
* Recency: tests predate the current environment by months, not hardware generations.
* Traceability: each finding maps to a corrective action, and each corrective action to a retest.
* Honesty: scopes are set to learn something, not to guarantee a clean report.

## Output

By the end of this stage, the organisation has test reports mapped to zones, threats, and controls, corrective
actions with retest status, and a body of effectiveness evidence. That body of evidence is most of what
[the inspection](inspection.md) will ask to see.

## Related

* [ISO 22301 Running the drills](../iso22301/drills.md)
* [Unseen University Power & Light Co. IT/OCS pentest](https://red.tymyrddin.dev/docs/power/)
* [Gap analysis](../supportive/gap-analysis.md)

*Last updated: 4 July 2026*
