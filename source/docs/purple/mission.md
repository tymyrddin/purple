# Purple teaming

Purple teaming is a way of working. The offensive and defensive sides of an organisation's security work happen in the
same loop, with shared context and real-time communication, rather than running as separate exercises whose findings
arrive in reports nobody reads.

## Beyond red plus blue

A red team operating alone tests defences and produces a report. The defenders, who are the people who would benefit
from the testing, often learn what failed but rarely learn why, because the report arrives weeks after the exercise and
the context that produced the finding is no longer available.

A blue team operating alone builds detections against the threats it can imagine. The threats it cannot imagine are
likely to evade those detections, and the team has no mechanism for finding out which assumptions are wrong before an
actual incident reveals them.

Purple teaming closes this gap by running the offensive and defensive activity in contact with each other. The red team
shares techniques as it uses them, or shortly after. The blue team tests detection and response against the actual
simulated attack rather than against an account of it. Both sides learn continuously rather than episodically, and the
conditions under which detections fail become visible while the people who can fix them are still in the room.

## Recognisable effects

The work has several effects that emerge over time rather than appearing in the first exercise.

Detection coverage that reflects what tools actually detect, not what they were configured to detect. Configuration
intent and operational behaviour [drift apart over time](../foundations/system-effectiveness/core-triad.md), and a
purple team exercise is one of the few mechanisms that surfaces the gap before an incident does.

A shared vocabulary across the offensive and defensive sides. Frameworks like MITRE ATT&CK help, but the more useful
effect is that the two sides start describing the same events in compatible terms, which makes the rest of the security
conversation possible.

Investment decisions grounded in what the organisation has been shown to be exposed to, rather than in what the security
industry is currently selling. The exercise output tends to be more concrete than a vendor pitch and harder to argue
with.

A cultural shift away from the offence-versus-defence framing that some security teams treat as their primary identity.
The shift is incremental and reversible: a single mishandled finding can undo months of trust. The conditions that allow
it, are addressed in [Satir's work on communication patterns](../foundations/organisational-development/satir-core.md)
and in [organisational conditions](conditions.md).

## Related

- [Building a purple team](team.md)
- [Readiness](readiness.md)
- [Common antipatterns and pitfalls](practice/antipatterns.md)
- [Building a purple team programme](purple-team/team.md)
