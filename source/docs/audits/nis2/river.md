# Understanding the river

![River](/_static/images/river.png)

NIS2, Articles 20, 21 and 23: the regulatory current, the organisation's own hazards, and the gap between them.

NIS2 expects measures that are appropriate and proportionate. That means understanding two things: what the law
requires, which is the regulatory current, and what the organisation's own risks demand, which are the hazards
in this particular crossing. The right vessel cannot be built until both are understood.

## Legal requirements

[Article 21](https://www.nis2-info.eu/article-21-cybersecurity-risk-management-measures/) sets out mandatory minimum
measures for every entity within scope. These are not optional and not something to postpone. They include risk
analysis and security policies, incident handling capabilities, business continuity and crisis management,
supply chain security, secure development practices, assessment of control [effectiveness](../../foundations/system-effectiveness/applying-sem.md), encryption,
human resources security, access control and asset management, multifactor or continuous authentication,
and secured communications, including emergency systems where relevant.

[Article 20](https://www.nis2-info.eu/article-20-governance/) adds governance requirements. These include board
approval and oversight of security measures, management accountability for failures, training for leadership and
staff, and participation in coordinated vulnerability disclosure programmes.

[Article 23](https://www.nis2-info.eu/article-23-reporting-obligations/) defines incident reporting timelines.
The law requires an early warning within 24 hours of becoming aware of an incident, a detailed notification
within 72 hours, and a final report within one month. These are legal obligations with specific deadlines.

Some sectors have additional expectations beyond this baseline. Energy may need operational technology controls,
healthcare may have patient safety considerations, and digital infrastructure providers may have availability
guarantees. The supervisory authority is the source for sector-specific requirements.

## Hazards

Once the legal current is mapped, the organisation's own hazards want charting. The most likely threats vary by
sector: ransomware in healthcare, DDoS attacks on infrastructure, supply chain compromises in manufacturing.
The charting covers which assets are most critical, what would cause severe disruption, and where the single
points of failure sit, in systems and in personnel.

Likelihood and impact belong together in the analysis. A theoretical, low-impact threat can be noted, but a
probable threat with cascading consequences requires immediate attention. Dependencies deserve the same
attention: what breaks when a single system fails, and what a vendor outage does downstream.

Risk entries are starting hypotheses, not conclusions. A likelihood of "High" for ransomware reflects a belief about the organisation's current exposure; a "Low" for insider threat may reflect a belief about team trust rather than evidence. Some of those beliefs will be wrong, and some can be tested before an incident tests them. Treating risk scenarios as assumptions to verify, rather than facts to document, is what makes risk analysis useful rather than decorative.

Risk analysis works in the rational domain: identify threats, estimate likelihood and impact. A register built
from this process alone will be systematically incomplete in predictable ways.

The [emotional layer](../../foundations/problem-solving/three-domains.md) asks which risks are difficult to
name. Insider threat is chronically underrepresented not because it is rare but because naming it implicates
colleagues. A long-standing dependency on an under-resourced individual is a risk; raising it publicly has
social consequences.

The [political layer](../../foundations/problem-solving/three-domains.md) asks whose interests are served by a
particular outcome. A risk whose treatment creates work for one team while the benefit accrues to another
tends toward acceptance regardless of its score. An unusually high proportion of accepted risks in one area is
worth examining for political incentive before finalising the register. When a treatment stalls despite
agreement, or the same risk is accepted with unchanged justification in successive cycles, the constraint is
usually in the political or emotional layer rather than the technical one.

Treatments map risks to controls. NIS2 mandatory measures cover many common risks; where the baseline is
insufficient, proportionate additions close the difference, and residual risks that are consciously accepted
get documented as such.

## Current state against requirements

A structured [gap analysis](../supportive/gap-analysis.md) covers three areas.

Technical gaps reveal missing or weak controls: insufficient monitoring or logging, weak or absent
authentication, inadequate encryption of sensitive data, incomplete or untested backup and recovery. Specific
beats general here. "No MFA on administrative accounts" is far more actionable than "authentication needs
improvement".

Organisational gaps highlight missing or outdated policies and procedures, insufficient governance or unclear
responsibilities, untested incident response capabilities, poor security awareness, and incomplete asset
inventories that leave uncertainty about what is being protected.

Compliance gaps focus on NIS2-specific requirements: missing incident reporting procedures, incomplete
supply chain security assessments, inadequate documentation to demonstrate compliance, insufficient board
oversight or evidence of governance.

The gap analysis covers two distinct categories. The first is missing controls: the control does not exist.
The second is ineffective controls: the control exists but does not produce its intended effect under
realistic conditions. A backup procedure exists but restoration has never been tested under conditions that
resemble an actual incident. MFA is in place but a bypass path through a legacy system is unmanaged.
Monitoring is active but alerts are not reviewed.

Compliance evidence built on implementation alone covers the first category. Covering the second requires
testing.

Remediation gets prioritised by risk and effort, and lands in a roadmap with realistic timelines and
dependencies.

## Output

By the end of this stage, the organisation has a regulatory requirements matrix, a [risk register](../../risk-management/risk-register.md), a gap analysis, and
a prioritised remediation plan.

## Related

* [ISO 27001 Risk tent](../iso27001/risk-tent.md)
* [ISO 22301 Storm charts](../iso22301/storm-charts.md)
* [IEC 62443 Knowing the besiegers](../iec62443/besiegers.md)
* [Threat modelling as a process](../../workshops/threat-modelling.md)
