# Readiness

Purple teaming makes sense once an organisation has the basic ingredients of a defensive function and the willingness to learn from its gaps. Started earlier, it surfaces problems the team has no way to act on; started later, it produces less than it could, because the gaps it would have surfaced have already become incidents.

## Technical conditions

A purple team exercise tests detection and response. Both have to exist before they can be tested, even in a small form. An organisation without basic visibility, centralised logging, endpoint monitoring, network traffic visibility, has nothing for the exercise to land against. The exercise will surface this absence rather than anything else, which is informative once but not the kind of finding the practice was designed for.

A defensive owner is the other minimum: someone responsible for monitoring, detection, and response, even if part-time and even in a small organisation. Without that role, findings have nowhere to go. The exercise produces observations and the observations sit in a folder.

A safe environment for testing earns more attention than it sometimes gets. An exercise that disrupts production teaches the team that exercises are dangerous, which is the opposite of the lesson the practice intends. An isolated test environment, or production testing with carefully scoped safety limits, keeps the conversation focused on what was learned rather than what was broken.

A red team capability is the offensive minimum. The capability does not require elite operators; it requires someone who understands adversary techniques well enough to simulate them realistically and who can operate inside agreed safety boundaries. External help can fill this role early on, with the caveats covered in [Building your purple team](team.md).

## Cultural conditions

Technical readiness is the easier half. The harder half is whether an organisation can do anything useful with what the exercise reveals.

The political layer is frequently missing. Someone needs the authority to require that findings are acted on, not just acknowledged. In organisations where security sits below the line at which resource allocation decisions are made, findings from purple team exercises become a list everyone agrees is important and no one has time to address. The exercise runs, the report lands, and six months later the same gaps are rediscovered. This is not a purple teaming problem. It is a political layer problem that purple teaming cannot solve by itself.

Communication conditions are worth attention too. [Satir's work on communication patterns](../foundations/organisational-development/satir-core.md) under stress applies directly here: teams under pressure default to placating (telling the exercise facilitator what they want to hear), computing (responding to every finding with a process or policy rather than a capability change), or blaming (identifying the individual who missed the alert rather than the system that made missing it likely). None of these produce learning. A purple team exercise in an organisation where these patterns are established will surface them rather than solve them, which is useful information but calls for a different intervention than more exercises.

A practical question, before investing in purple teaming, is whether there is a realistic path from finding to fix. Not a theoretical one. Who, specifically, can require that a finding from next month's exercise results in a changed control or a reallocated budget? If the answer is unclear, that is the first problem to address.

## Patterns that argue for waiting

A few patterns suggest preparatory work is worth doing before starting the practice.

A blue team without procedures for responding to detected threats: purple teaming reveals problems but cannot help fix them, because the response side has nothing to test.

A purely compliance-driven security function. Purple team findings sit awkwardly with control attestations: an exercise that bypasses an authentication control in five minutes contradicts the audit evidence that the same control was "implemented and effective". Either the exercise becomes the trusted reading of capability and the compliance posture is in question, or the exercise becomes the unreliable one and the practice becomes theatre of a different kind. Neither option is comfortable, and neither resolves itself without leadership willing to say which reading is the operative one.

An adversarial culture between offensive and defensive functions. If the red team views the blue team as incompetent, or the blue team views the red team as annoying, collaboration fails before the exercise begins. The cultural work comes first; the practice can support it but cannot create it.

No protected time for follow-through. Purple team exercises take preparation, execution, and follow-up. Half-hearted efforts produce findings that are never converted into change, which trains everyone involved to treat the exercise as theatre.

## Related

- [What purple teaming is](mission.md)
- [Quick wins: the first exercises](practice/quick-wins.md)
- [Readiness for purple teaming](purple-team/readiness.md)
- [Why security change stalls](../foundations/change-management/why-change-fails.md)
- [Organisational conditions for change](conditions.md)
