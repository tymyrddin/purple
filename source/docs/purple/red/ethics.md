# Ethical boundaries and rules of engagement

Red teaming operates in a grey area: simulating attacks without causing harm, exercising techniques that resemble criminal activity without crossing into it. Clear boundaries, agreed before the engagement begins, are what keep the work on the right side of the line.

## Legal considerations

Written authorisation from an appropriate authority comes before any red team activity. Verbal assurances, even from a CEO, do not substitute for documented permission. The written record protects everyone involved when something later prompts a question.

Scope limitations are recorded explicitly. The systems, networks, and facilities in scope are named; everything outside that list is off-limits, regardless of what the engagement uncovers.

Data handling rules cover sensitive information encountered during exercises. Encryption, minimisation of collection, and destruction after the engagement are part of the rules of engagement rather than after-the-fact considerations.

Third-party systems, cloud providers, partner organisations, and other entities outside the testing organisation's authority are off-limits unless their explicit authorisation has been obtained in writing.

Criminal activity remains criminal regardless of context. Real fraud, real extortion, real destruction of property, or real harm to individuals are never acceptable, no matter what the exercise objectives suggest.

## Operational boundaries

Do-not-harm criteria define specific conditions that immediately stop the exercise: a production outage, data destruction, a safety risk, or unintended access to regulated data. These are decided in advance, not in the moment.

Communication channels for emergency contact give the red team a way to reach defenders or leadership immediately when something goes wrong. The channel is tested before the engagement begins, not when it is needed.

Disclosure timing decides when the blue team learns about the exercise. Continuous purple teaming involves real-time collaboration; traditional red teaming may wait until completion. The choice depends on the engagement's [coordination mode](../coordination.md).

Physical security boundaries name the limits on physical access attempts: tailgating, lock-picking, badge cloning, social engineering of receptionists. Each is either in or out of scope, with the boundary recorded.

Social engineering boundaries are similarly explicit. Whether employees are fair game, whether specific individuals can be targeted, and whether pretexting that causes genuine distress is acceptable are answered before the engagement, not negotiated mid-stream.

## Safety valves

A stop word or signal halts operations immediately if something goes wrong. The word and the channel are agreed in advance and known to all parties.

Regular check-ins between the red team and the exercise manager confirm that operations remain within bounds. Long silences during a complex engagement increase the risk of unobserved drift outside scope.

An observer role, sometimes filled by a third party, monitors operations to confirm compliance with the rules of engagement. The observer is not a referee; the observer is a witness with the authority to call a halt.

Post-exercise disclosure reveals all activities to defenders, including the actions that were not detected. Full transparency is what enables the blue team to learn from the engagement rather than only from the parts they noticed.

## Related

- [The red team mission](mission.md)
- [Coordinating with purple team](coordination.md)
- [Documentation and evidence collection](docs.md)
- [PSL applied to security work](../../foundations/problem-solving/in-security.md)
