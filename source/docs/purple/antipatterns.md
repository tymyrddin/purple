# Common anti-patterns and pitfalls

## Competitive rather than collaborative

Red and blue teams view purple teaming as competition. Red team tries to "win" by evading detection. Blue team
feels defensive about gaps discovered.

This is the default state of separated teams, not a character flaw. Teams that have operated independently have
built identity around their respective expertise: the red team's identity is finding things, the blue team's
identity is stopping things. Bringing them into the same room and asking them to collaborate does not dissolve
that dynamic. It surfaces it. The antipattern persists because the organisational conditions that created it are
still present.

The direction of change is shared goals rather than shared exercises. Red team success means the organisation
learns about gaps before real adversaries exploit them. That reframe has to be genuine and supported visibly by
whoever commissioned the programme, not just stated in a kick-off meeting and then forgotten.

## No follow-through on findings

Purple team exercises reveal gaps but nothing gets fixed. The same weaknesses are discovered at the next
exercise, and the one after that, while the findings backlog grows quietly in a spreadsheet.

This is almost always a political layer problem rather than a motivation problem. The people who ran the exercise
want to fix things. The people who would need to allocate time or budget to fix them have competing priorities
and no particular reason to treat security findings as urgent until something goes wrong. The exercise produces
information. It does not produce the authority to require that information is acted on.

Treating findings like vulnerabilities (assigning owners, setting timelines, tracking remediation) is correct
process. But process without authority produces well-documented stagnation. The question is who can require
action, and whether that person is genuinely invested in the outcome.

## Overly complex scenarios

The first exercise attempts to emulate a sophisticated nation-state adversary across a hybrid cloud environment.
This is optimistic about current capability and produces a great deal of chaos from which it is difficult to
extract learning.

Start with the simplest attack paths and the most common defensive gaps. Complexity is a reward for maturity,
not a substitute for it.

## Inadequate preparation

Red team does not document actions clearly. Blue team has not prepared monitoring or response procedures. The
exercise runs and generates activity, but the debrief has little to work with because no one can reconstruct
what actually happened.

Good documentation is not bureaucracy. It is what makes the difference between an exercise that produces a
learning event and one that produces a vague sense that things could be better.

## Blame culture

Gaps discovered during exercises lead to finger-pointing. The analyst who missed the alert is identified. The
team that left the system unpatched is named. The debrief becomes a retrospective accountability exercise with
no one coming away eager to participate in the next one.

Purple teaming reveals organisational weaknesses, not personal failures. The analyst who missed the alert was
operating in a system that produced too many alerts to triage, with tooling that made the relevant one hard to
distinguish from noise. Fixing the individual (through additional training, or more pointed feedback) without
fixing the system produces a slightly more anxious version of the same vulnerability.

Blameless post-mortems are not softness. They are the condition under which people will tell you what actually
happened rather than what they wish had happened.

## Related

- [What purple teaming actually is](mission.md)
- [When you're ready for purple teaming](readiness.md)
- [Coordination models](coordination.md)
- [Organisational conditions for change](conditions.md)
- [Why simulations fail](../social-engineering/why-simulations-fail.md)
