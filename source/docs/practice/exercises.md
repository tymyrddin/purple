# Exercises that earn their keep

"Oh no, not another tabletop" is a diagnosis worth taking seriously rather than a grumble to wave off.
An exercise exists to generate behavioural evidence safely: to show whether an organisation responds the
way its plans assume, before a real event tests the same thing at a far higher price. When the groan
arrives, the exercise has usually slipped from an instrument into a ritual.

Where [choosing an engagement](../engagement/choosing.md) settles which instrument fits a problem, this
is about running the chosen one so it repays the room's time.

## When the groan is earned

A handful of conditions turn an exercise into the thing people dread.

- It runs to satisfy an ISO, NIS2 or insurer requirement, so the textbook answer gets performed and
  little is learned.
- It is on rails. The facilitator steers towards a set ending, and the group spends the hour guessing
  the intended answer.
- It is a reading. Someone narrates an incident from slides while the room nods, and nothing said
  changes what happens next.
- The person who would make the call is absent, or the altitude is off: executives rehearsing console
  decisions, operators asked to set risk appetite. Real decisions need the decision rights in the room.
- The room is unsafe to fail in. A wrong move might surface in a report or at appraisal, so people reach
  for the safe, correct-sounding line, and the honest behaviour stays hidden.
- Last round's findings went nowhere. An exercise whose predecessor produced a report nobody acted on
  reads as futile before it begins.
- The scenario belongs to someone else: a hurricane hitting headquarters, a film-grade adversary that
  maps to none of the organisation's real dependencies. Attention drifts.

The common thread is that the tabletop has become the point. It was only ever a way of producing
evidence about how the organisation behaves under pressure.

## What a good one has

- A real decision with cost on both sides, and no obviously-right answer. The interest, and much of the
  enjoyment, sits in a hard trade-off argued in the open.
- Consequence. The facilitator responds to what the group decides, and the situation branches. This is
  the largest single difference between an exercise people tolerate and one they come back to.
- Time pressure and partial, sometimes contradictory information. Decisions get made before certainty
  arrives, which is where behaviour and stated policy come apart.
- The right people, whoever owns the call among them, and a [no-blame frame](../engagement/safety.md) the facilitator actively
  holds. Failure is the product, not the embarrassment.
- Tight scope. One plausible scenario, a decision or two deep, sixty to ninety minutes. A sharp small
  exercise often teaches more than a sprawling one.
- A neutral facilitator applying pressure, adjusting to the room as it responds, and leaving the gotchas
  alone.
- A hot [debrief](debriefs.md) in the group's own words: where "how we think we respond" diverged from
  what the scenario required, and two or three concrete fixes with owners. Next time, last round's fixes are visible, so the
  exercise is seen to change things.
- A little play. Narrative, humour, a curveball. Play lowers defensiveness, which is why a board will
  engage with [Lord Vetinari's Dilemma](../crucible/games/ankh-crisis-sim.md) where a dry risk briefing
  loses the room.

A regional hospital ran a ransomware scenario built on one decision: isolate the shared patient-records
system, protecting the data but halting admissions across three sites, or keep it running and accept the
spread. The facilitator let the choice stand and played the consequence either way. The group reached for
isolation, then found that the admissions fallback assumed a paper process last rehearsed years earlier,
and that the person who could authorise diverting ambulances dropped off the call tree after 18:00. The
scenario was fictional; the two gaps were real, and both went into the next fortnight's work.

## Other instruments

A tabletop is one instrument among several. When the groan is earned, a different one often does more than
a better-run tabletop would.

- The [loop](../purple/running-the-loop.md). Offence moves, defence responds live, and the two read the
  result together while it is warm: real detection and response, and in its continuous mode a standing
  habit rather than a yearly set-piece.
- Structured incident scenarios and capture-the-flag for technical teams, treated as prepared learning
  environments in [CTFs](../foundations/montessori/ctf-value.md). Self-correcting: the incident is either
  contained or it runs on.
- Game days and chaos drills. A controlled system is broken on purpose, a service killed or a failover
  forced, and recovery watched as it actually goes.
- Unannounced restore tests. An actual restore from backup, timed, turns "backups exist" into "recovery
  worked, in this many minutes".
- A [pre-mortem](../thirteen/foresight.md). Before a launch or a change, the failure is imagined and
  worked back to its causes: cheap, quick, and free of scenario theatre, which suits the moments a full
  exercise would be overkill.
- Dependency mapping and assumption hunts, walked across the [ecosystem](../resilience/ecosystem.md) map. The hidden
  connectors surface with no scenario at all.
- A runbook walkthrough with the person who would actually use it, timed against the clock it would face.
  That is a [manuals](../knowledge-transfer/manuals.md) test, closer to "can someone reach for this at
  3:00" than to a tabletop.
- Harvesting a real incident. A blame-free [post-incident review](../incident-response/index.rst) of an
  event that actually happened is the richest exercise available, since the stakes were real. The work
  sits in harvesting it well.

## The instrument is not the point

What the good versions share is that they produce
[behavioural evidence](../foundations/system-effectiveness/applying-sem.md), safely, owned by the people
who ran it, and carried into the next round. "Not another tabletop" is the organisation reporting that the
instrument has decayed into the ritual, and the reply is to restore the conditions or reach for a
different instrument. The same decay, an exercise kept for the certificate, hollows out awareness work
too, traced in [why simulations fail](../social-engineering/why-simulations-fail.md).

*Last updated: 2 July 2026*
