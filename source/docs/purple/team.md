# Building your purple team

Purple teaming is a practice. The shape of the team that runs it varies with the size of an organisation, the maturity
of the security function, and the people available to do the work.

## Small organisations

In a small organisation, the same people may play offensive and defensive roles at different times. An IT staff member
with security responsibilities can simulate an attack one week and validate the resulting detection the next. A single
person cannot fully embody both sides simultaneously, but rotation through them is often instructive on its own.

External assistance can fill the offensive side when internal capacity is missing. A consultant, a service provider, or
a partner organisation can run a simulation while internal staff work on detection and response. A risk with such an
arrangement is that the offensive and defensive sides operate on different timelines, the gap purple teaming was
designed to close. Tight coordination during and immediately after the exercise is what keeps the model intact.

Cadence is usually scheduled rather than continuous: quarterly or semi-annual exercises focused on the most likely
attack paths and the detections an organisation has built. Continuous purple teaming requires resources a small
organisation usually has elsewhere.

## Medium organisations

A medium organisation can separate red and blue roles, even if the teams remain small. A dedicated tester or small red
team simulates attacks; security analysts handle detection and response. The separation creates conditions for honest
exchange that combined roles cannot.

A facilitator role appears at this scale. One person, often a security manager or senior analyst, coordinates exercises,
checks that both sides have prepared adequately, runs the exercise reflection, and tracks what changes as a result. A
facilitator's work is not a content role; it is a conditions role. What it makes possible is harder to see than what the
offensive and defensive sides do, and is often what determines whether the programme produces learning.

The cadence shifts to monthly or quarterly, and tooling investment that supports more sophisticated validation, such as
SIEM, EDR, and frameworks like Atomic Red Team, becomes worth the cost.

## Large organisations

In a large organisation, full red and blue functions can exist alongside a coordination function whose specific job is
the purple work. The exercises are part of an ongoing cycle rather than discrete events: threat hunting integrated with
red team intelligence, automated adversary simulation, formal coverage maps, defined maturity progressions.

A risk at scale is that the programme becomes a process rather than a learning practice. The exercises produce reports,
the reports produce action items, the action items produce metric updates, and the underlying purpose, finding what the
defences are not catching, can get lost in the operational rhythm. The conditions that prevent this are the same as in
smaller organisations, but the political layer is harder to attend to because more stakeholders have views about what
the programme is for.

## The roles, in three layers

Role clarity is easier to think about through the [PSL framing](../foundations/problem-solving/index.rst): each side of
the practice has a rational layer, an emotional layer, and a political layer. The rational layer is what most
descriptions of the role cover; the other two are often where programmes fail.

A red team's rational work is to plan and execute attack simulations within agreed scope, to document what was done, and
to share the techniques with the blue team. The emotional work involves tolerating the discomfort of finding things and
naming them honestly, especially when a finding implicates a colleague's work. The political work is staying inside the
rules of engagement and making the findings useful rather than score-keeping.

A blue team's rational work is to monitor, detect, and respond. The emotional work involves receiving findings without
defensiveness, which is easier said than done when a finding lands as a personal failure. The political work is
converting findings into change, which requires either authority that a blue team often lacks, or relationships with the
people who do.

A facilitator's role spans all three layers without being primarily about any of them. The facilitator coordinates the
rational work, holds the emotional conditions during the reflection, and represents the programme to the political layer
outside it. A purple team programme without this role can drift back into red-versus-blue, even when the named structure
says otherwise.

## Related

- [Purple teaming](mission.md)
- [Readiness](readiness.md)
- [Coordination models](coordination.md)
- [Building a purple team programme](purple-team/team.md)
