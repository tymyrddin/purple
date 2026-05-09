# Quick wins for starting small

The first few exercises target one technique, one detection, one response procedure. They do less than the comprehensive programme that comes later, which is the point: a [prepared environment](../../foundations/montessori/prepared-environment.md) for one capability at a time produces clearer learning than a complex scenario in which several things might have failed.

The progression below is one possible sequence, from a single technique against a single detection up to a multi-stage scenario. Each step is designed to surface the gap most likely to inform the next.

## Week 1: phishing simulation

A red team sends realistic phishing emails to a small group and tracks who clicks links or submits credentials. The blue team monitors email security alerts, authentication logs, and unusual web traffic, and practises responding to compromised credentials.

What the exercise teaches is whether the existing security awareness training and email filtering produce the effects they were meant to produce. Whether the blue team can detect a credential submission as it happens. How quickly a compromised account can actually be disabled, as opposed to how quickly the policy says it can be disabled.

The exercise is small because the technique is single-step. The conditions it needs are minimal: an email security tool, authentication logging, and a way to disable an account. If those are missing, the exercise will surface that absence first, which is itself the most useful thing it could surface.

## Week 2: Atomic Red Team test

A red team runs pre-built [Atomic Red Team](https://www.atomicredteam.io/) tests for common techniques such as credential dumping or persistence mechanisms. The blue team monitors EDR and SIEM, investigates what fires, and responds.

The exercise teaches what the EDR actually detects, as distinct from what its marketing material suggests it detects. Which MITRE ATT&CK techniques produce alerts, and which pass through silently. Where the visible blind spots are.

This is often the first exercise that produces concrete findings about tooling, and the findings are sometimes uncomfortable. A purchase that was made on the basis of broad detection claims can turn out to detect a narrower set of things in practice. That is information worth having before the budget conversation, not after.

## Week 3: lateral movement simulation

A red team simulates an attacker with a compromised account attempting lateral movement to additional systems. The blue team monitors authentication attempts, unusual access patterns, and account usage across multiple systems.

The exercise teaches whether the team can detect lateral movement at all, how quickly, and what network segmentation or access controls actually limit attacker options. The earlier exercises tested point-in-time detections; this one tests whether multiple events across multiple systems can be correlated into a single picture.

## Month 2: assumed-breach scenario

Starting with provided credentials, simulating a successful phishing outcome from week 1, a red team attempts privilege escalation and access to sensitive data. The blue team monitors for privilege escalation attempts, sensitive data access, and suspicious account behaviour.

The exercise teaches how far an attacker can travel from initial access given current detections. It also tests post-compromise visibility, which is often weaker than initial-access visibility because the attention has historically gone to the perimeter rather than to what happens inside it.

## Quarter 2: full engagement

A multi-stage exercise from initial access through objectives, including data exfiltration, system persistence, and an impact demonstration that does not actually cause damage. The blue team runs full incident response: detection, containment, eradication, recovery.

The exercise teaches whether the complete defensive programme works end-to-end, and what breaks under sustained pressure rather than at a single decision point. The findings from this exercise are typically structural rather than tactical: gaps in handover between functions, delays at decision points that nobody owns clearly, the documentation that was never written because no incident has yet required it.

The progression from week 1 to quarter 2 is not mandatory. Some organisations remain at week-3 complexity for a year and produce excellent results, because the conditions support the learning at that level. Others reach for the quarter-2 exercise prematurely and produce findings the programme cannot yet act on. The choice is covered in [readiness](../readiness.md) and [conditions](../conditions.md).

## Related

- [Readiness](../readiness.md)
- [Coordination models](../coordination.md)
- [Measurements and early success](measurements.md)
- [Building a phishing programme that actually works](../../social-engineering/phishing-programme.md)
