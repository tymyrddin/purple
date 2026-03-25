# A ChangeShop-informed approach to security

ChangeShop does not produce a methodology to follow. It produces a disposition toward change: one that treats resistance as data, designs for human behaviour rather than ideal behaviour, and measures what the system is actually doing rather than what it is supposed to be doing.

## Start with the system, not the solution

Before designing a control or writing a policy, ask what the system is currently rewarding.

If fast releases are rewarded and security reviews slow releases down, the system is rewarding the bypass of security reviews. No policy changes that. The incentive structure does.

If incidents are punished and near-misses are invisible, the system is rewarding underreporting. No awareness campaign changes that. What changes it is creating conditions where reporting is safe and where near-misses produce learning rather than blame.

## Use small experiments, not big rollouts

Large-scale security rollouts are high-risk because they involve too many unknowns acting simultaneously. When they fail, it is difficult to know what caused the failure.

Small experiments are informative. Pilot a control with one team, observe what friction appears, adjust before scaling. The friction is not a setback; it is the data you came for. A rollout that surfaces no friction usually means the control is not actually being used.

## Redefine what success means

Traditional security metrics measure activity: vulnerabilities closed, policies published, training completed. ChangeShop-informed metrics measure change in system behaviour.

Time-to-fix measures whether the organisation is becoming more capable of resolving issues, not just aware of them. Ownership clarity measures whether accountability has actually shifted or has only been notionally assigned. The frequency with which teams escalate issues without being asked measures whether the safety conditions for honesty exist.

These are harder to capture. They are also much more predictive of actual security posture.

## Work at leverage points, not symptoms

Deploying more tools is usually working on a symptom. The underlying question is what model, incentive, or ownership structure is producing the symptom repeatedly.

For access control sprawl: the symptom is overprivileged accounts. The leverage points are the fear of breaking production that makes teams keep permissions broad, the absence of ownership for access review, and the absence of tooling that makes the current state visible. Address the tooling alone and the problem persists. Address visibility, ownership, and the fear of safe rollback together, and the system can begin to improve itself.

## A concrete example: MFA rollout

A security mandate requires MFA everywhere. Deployment stalls, exceptions accumulate, workarounds appear.

A ChangeShop lens on this: the users find MFA more disruptive than helpful in their current workflow (emotional constraint). Leadership exempts systems classified as critical, which signals that the mandate is negotiable (political constraint). The rollout was designed without flexibility for edge cases (rational design failure).

An alternative approach: pilot with one team that has a relatively simple environment. Gather friction data from the experience, not from a survey. Adjust the rollout approach based on what actually blocked adoption rather than what the implementation plan assumed would block it. Secure leadership commitment to the exceptions policy before announcing the mandate, so exemptions do not undermine the change in progress.

Slower at the start. Much faster at the end. And the result is adoption rather than the appearance of adoption.
