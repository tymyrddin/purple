# Risk scoring

A risk score translates two estimates into a single rating: how likely is this threat to materialise, and how
bad would it be if it did? The result drives prioritisation, treatment decisions, and the language used to
communicate risk to people who will not sit through the full assessment.

The gap this page addresses is between the threat register (which captures what could go wrong) and the gap
analysis severity rating (which measures how serious a control shortfall is). Both depend on a consistent,
honestly calibrated risk score. Without that calibration, severity ratings drift toward whatever rating is most
comfortable for the people in the room.

## The basic matrix

A 3x3 likelihood-impact matrix is sufficient for most contexts:

| | Low impact | Medium impact | High impact |
|---|---|---|---|
| High likelihood | Medium | High | Critical |
| Medium likelihood | Low | Medium | High |
| Low likelihood | Low | Low | Medium |

For contexts where finer resolution is genuinely needed, a 5x5 matrix adds gradations. The value of the extra
resolution is modest unless the organisation is disciplined enough to define and apply five likelihood gradations
and five impact gradations consistently. A 3x3 matrix that is honestly populated is more useful than a 5x5 that
defaults to the middle or flatters.

The methodology behind the matrix, including the political dynamics that make rating discussions uncomfortable,
is covered in depth in the [risk assessment exercise](../../risk-management/risk-assessment.md), which runs
this process as a facilitated workshop.

## Defining the scales

Generic scale definitions produce inconsistent ratings. The aim is definitions concrete enough that two
different people assessing the same risk independently would arrive at the same cell.

Likelihood definitions are worth anchoring to something observable: frequency ("could occur multiple times per
year"), effort required ("requires minimal skill or access"), and sector evidence ("consistent with incidents at
comparable organisations"). "Plausible" is not a likelihood definition; most threats are plausible.

Impact definitions are worth covering the categories that matter: operational continuity, financial exposure,
regulatory consequences, and safety implications where relevant. Organisations that define impact only in
financial terms will underrate risks to continuity and safety.

Both scales work best when defined for the specific context. A healthcare provider's definition of high impact
is not the same as a software company's, and importing a generic template without adaptation produces ratings
that reflect the template rather than the organisation.

## How the frameworks differ

### ISO 27001

The standard does not prescribe a risk scoring methodology. It requires that the organisation establishes its
own criteria for assessing risk and applies them consistently. The scoring approach, the scale, and the
definitions are the organisation's to choose. The requirement is that the choices are documented and applied
uniformly, not that they are a particular kind.

This flexibility is useful for organisations that already have an established risk methodology. It is a trap for
organisations that take the flexibility to mean they can avoid defining the methodology at all.

### IEC 62443

In OT environments, IEC 62443 uses security levels (SL 1 to SL 4) to express the required security capability
in relation to the threat environment. SL 1 addresses incidental or unintentional violations; SL 4 addresses
state-sponsored actors with sophisticated capabilities and strong motivation.

Risk scoring in this context maps onto the security level requirements for each zone: the risk from a given
threat in a given zone determines what security level the zone's controls need to achieve. A risk that would
require SL 3 controls in a zone currently designed to SL 2 is a finding with a specific remediation direction,
which is more useful than a generic "high" rating without context.

### NIS2

NIS2 uses proportionality as its framing: measures need to be appropriate to the risk, taking into account the
size of the entity, its exposure, and the likelihood and severity of incidents. There is no prescribed scoring
method, but the proportionality principle means that a small entity assessing a low-probability risk with
limited impact is expected to reach different conclusions than a large essential entity assessing the same risk.

Risk scores used for NIS2 compliance are worth connecting demonstrably to the entity's actual exposure and
context, rather than being imported wholesale from a generic template.

## Calibrating against evidence

A risk score that was never challenged by a test result or an incident is a rating built entirely on
assumptions. Exercises, penetration tests, CTF environments, and incident reviews are calibration tools.

When a tabletop exercise reveals that a scenario assessed as low likelihood materialised faster than expected,
the likelihood rating is worth revisiting. When a penetration test demonstrates that a high-impact path is
accessible with less effort than the original assessment assumed, both the scoring and the control assessment
need to update. When an incident produces impact outside the rated range, the impact definition itself is
worth examining.

The direction of calibration tends to be one-way in organisations that do not test: ratings drift lower over
time as accepted risks accumulate without re-evaluation. Simulation environments push back against this drift
by introducing evidence that does not depend on the willingness of the people in the room to acknowledge
uncomfortable truths.

## Related

* [Threat register](threat-register.md)
* [Gap analysis](gap-analysis.md)
* [Risk assessment exercise](../../risk-management/risk-assessment.md)
* [Risk register](../../risk-management/risk-register.md)