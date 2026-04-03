# Rules of engagement

Rules of engagement are the conditions under which honest testing can happen. Their function is not bureaucratic compliance; it is to create structural protection for everyone involved so that the exercise produces real findings rather than careful performances.

[Satir's work on communication under pressure](../foundations/organisational-development/satir-core.md) is directly relevant. Without rules that establish genuine safety, people default to survival stances: testers become cautious about what they attempt, defenders become cautious about what they escalate, and the exercise produces documentation of what everyone agreed to do rather than evidence of what the system actually does under realistic conditions. The rules are the prepared environment that makes honest engagement possible.

## Authorisation

Written authorisation from the appropriate authority, naming the specific activities permitted, is not optional. The scope of the authorisation needs to match the scope of the engagement, and both need to exist before any testing begins. Verbal agreements and implied permissions create ambiguity that tends to resolve badly when something unexpected happens.

Legal review is warranted wherever the engagement touches regulated environments, involves third-party systems, or uses techniques that have legal implications in the relevant jurisdiction. This is not a reason to avoid testing; it is a reason to document clearly before starting.

## Technical boundaries

Define the conditions that immediately stop testing: production service disruption, data corruption, unintended access to highly sensitive data, safety system effects. These are not failure conditions for the engagement; they are the boundaries that make it possible to run the engagement at all.

Define what tools are permitted and which are not. Some tools leave artefacts that are difficult to remove or create operational impact that outweighs their testing value. Define what the team does if they encounter a critical vulnerability outside the agreed scope: how to report it, to whom, and on what timeline.

## Operational guidelines

Establish communication channels before the engagement begins. Who does the testing team contact if something unexpected happens? Who does the defending team contact if they are uncertain whether what they are seeing is part of the exercise? What is the emergency stop signal and who can invoke it?

Define working hours explicitly. An engagement that assumes round-the-clock testing may be placing demands on on-call staff that were not agreed with them or their management. The engagement's resource assumptions need to match the organisation's actual capacity.

## Social engineering

Define clearly whether social engineering is in scope, which employees are eligible targets, and which techniques are permitted. The purpose of social engineering in an engagement is to surface the gap between what the organisation believes its staff will do and what they actually do under realistic pressure.

The limits on social engineering exist because [Satir's survival stances](../foundations/organisational-development/satir-core.md) are activated by genuine stress, and an exercise that produces significant distress teaches people to protect themselves from future exercises rather than to engage honestly with them. The goal is to create conditions where real behaviour is visible, not to test how much pressure people can absorb.

## Related

- [Scope](scope.md)
- [Safety and risk management](safety.md)
- [Coordination and communication](coordination.md)
- [Core ideas of Satir systems OD](../foundations/organisational-development/satir-core.md)
