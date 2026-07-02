# Cadence

A single run of anything, an exercise, an audit, a restore test, a control check, tells an organisation
where it stands once. What changes things is running it again. The first pass is a snapshot; the value
compounds on repetition, when the same probe shows whether last time's fix held and whether the gap is
widening or closing.

A few things follow from treating practice as a cadence rather than a single event.

- Repetition turns a discovery into verification. A finding closed after one run is a claim; the same run
  a quarter later, passing where it failed, is evidence the fix survived contact. Recurrence is what keeps
  [debriefs](debriefs.md) and [acting on findings](acting-on-findings.md) paying out past the first round.
- It makes the trend legible. One reading cannot separate drift from noise; a series can. The assumptions
  a control encodes age quietly, and re-testing on a schedule is what catches the moment the
  [model](../foundations/system-effectiveness/core-triad.md) and the environment part company.
- It lowers the cost of each run. The first exercise pays for the scenario, the tooling and the nerves,
  and the next reuses most of that with a team already fluent in how the thing works.
- It embeds the practice as habit. Security an organisation runs on a rhythm it owns begins to
  internalise, which is the shift the [loop](../purple/running-the-loop.md) makes in its continuous mode,
  offence and defence working in contact between set-pieces.

Cadence has a failure mode of its own: cadence for its own sake. A model reviewed on the scheduled annual
date whether or not anything has changed is close to the worst schedule there is, since it spends the
effort without catching the drift it was meant to catch. Useful cadence is paced by change as much as by
the calendar, with [triggers](../threat-modelling/bringing-it-together.md) for an off-cycle run when a new
system lands or an incident rhymes with the scenario. Set too fast for the culture to absorb, it can
produce fatigue rather than capability, which is its own signal worth reading.

A regional bank set its ransomware tabletop to a quarterly rhythm. The first run found that the incident
bridge had no number for the outsourced SOC, so the first hour went to hunting a contact; the fix was
logged and owned. The second, same scenario, reached the SOC in minutes, so that finding closed on
evidence rather than assurance. The third surfaced what the first two could not: the bridge now worked,
but a payment gateway outsourced since the last run had no place in the runbook at all. The value was not
in any single quarter. It was in the line the three drew.
