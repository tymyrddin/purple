# When you're ready for purple teaming

Purple teaming requires certain foundational capabilities. Starting too early wastes effort and causes frustration.

## Prerequisites

Red team capability: Need someone who can simulate attacks realistically. Doesn't require elite hackers but does need understanding of adversary TTPs and ability to operate safely.

Blue team capability: Need monitoring, detection, and incident response foundations. Can't validate detections that don't exist or test responses without procedures.

Willing participants: Both sides must want to collaborate. Adversarial red team or defensive blue team that views testing as criticism won't produce useful outcomes.

Executive support: Purple teaming takes time and resources. Leadership must understand value and accept that exercises will reveal uncomfortable gaps.

Safe environment: Need ability to test without breaking production. Isolated test environments or very controlled production testing with safety limits.

## You're not ready if

No logging or monitoring: Can't run purple team exercises if blue team is blind. Build visibility first.

No incident response capability: If blue team doesn't have procedures for responding to detected threats, purple teaming reveals problems but can't help fix them.

Purely compliance-driven: If security exists only to check regulatory boxes, purple teaming's honest assessment of real defensive effectiveness won't align with compliance theatre.

No time or resources: Purple team exercises require planning, execution time, and follow-through on findings. Half-hearted efforts waste everyone's time.

Adversarial culture: If red team views blue team as incompetent or blue team views red team as annoying, collaboration fails. Fix culture before attempting purple teaming.

## You're ready when

Basic visibility exists: Centralised logging, endpoint monitoring, network traffic visibility. Doesn't need to be perfect but must exist.

Someone owns defence: Clear responsibility for monitoring, detection, and response. Even small teams can designate an owner.

Curiosity about effectiveness: Genuine interest in "do our defences actually work?" Not defensive about discovering gaps.

Ability to act on findings: Can allocate time and resources to implement improvements discovered through purple teaming.

Psychological safety: Teams can discuss failures and gaps without blame. Learning mindset over perfection mindset.

## Organisational readiness

Technical readiness is the easier half. The harder half is whether the organisation is structured to do anything
useful with what purple teaming reveals.

The political layer is frequently missing. Someone needs the authority to require that findings are acted on, not
just acknowledged. In organisations where security sits below the line at which resource allocation decisions are
made, findings from purple team exercises become a list that everyone agrees is important and no one has time to
address. The exercise runs, the report lands, and six months later the same gaps are rediscovered. This is not a
purple teaming problem. It is a political layer problem that purple teaming cannot solve by itself.

The communication conditions matter too. Satir's work on communication patterns under stress is directly
applicable here: teams under pressure default to placating (telling the exercise facilitator what they want to
hear), computing (responding to every finding with a process or policy rather than a capability change), or
blaming (identifying the individual who missed the alert rather than the system that made missing it likely).
None of these produce learning. A purple team exercise in an organisation where these patterns are well established
will surface them rather than solve them, which is useful information but requires a different intervention than
more exercises.

The practical question, before investing in purple teaming, is whether there is a realistic path from finding to
fix. Not a theoretical one. Who, specifically, can require that a finding from next month's exercise results in a
changed control or a reallocated budget? If the answer is unclear, that is the first problem to address.

## Related

- [What purple teaming actually is](mission.md)
- [Quick wins: the first exercises](quick-wins.md)
- [Readiness for purple teaming](../making-of/purple-team/readiness.md)
- [Why security change stalls](../foundations/change-management/why-change-fails.md)
- [Organisational conditions for change](conditions.md)
