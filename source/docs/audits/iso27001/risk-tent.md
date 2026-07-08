# The risk tent

![Risk tent](/_static/images/risk-tent.png)

ISO/IEC 27001, Clause 6: risk assessment and risk treatment.

Having [agreed on which mountain](map-room.md), the risk tent is the shelter of structured risk management.
Without a reliable framework, a risk assessment collapses under pressure; a sound methodology is the support
structure that keeps the assessment standing even when conditions change.

## Choosing a risk map

Before assessing risk, the expedition needs a method everyone can follow without getting lost: one that
identifies potential impacts, evaluates likelihood, produces consistent results, and stays reliable as things
change. Several established methods reach that goal by different paths.

* [OCTAVE](https://pecb.com/en/whitepaper/risk-assessment-with-octave) is a self-directed method focused on aligning risks with organisational goals. It looks beyond technology to strategy, culture, and practices, and suits organisations that want business stakeholders directly involved in identifying and prioritising risks rather than leaving it to IT. The most accessible starting point for organisations without a dedicated risk team.
* [MEHARI](https://www.jabis.ro/2012/4/0304042012.pdf) is a modular European framework that integrates neatly with other management systems and offers quantitative scoring, useful where the board wants numbers and the risk register feeds existing reporting.
* [EBIOS](https://www.egerie.com/en/resources/blog/methode-ebios) defines security needs and objectives before diving into technical risks, ensuring every control serves a stated purpose. Well suited to regulated environments, and it aligns naturally with EU frameworks including NIS2.

Tooling exists across the spectrum, from open-source GRC platforms such as
[eramba](https://www.eramba.org/) and [CISO Assistant](https://intuitem.com/) to method-specific suites such as
[Agile Risk Manager](https://www.all4tec.com/en/ebios-risk-manager-certified-solution-agile-risk-manager/) for
EBIOS RM. The method shapes the register more than the tool does; choosing the tool first is buying boots
before choosing the mountain.

## What any method produces

Whatever the framework, register entries are starting hypotheses, not verdicts. A likelihood of "High" for
phishing susceptibility reflects the organisation's current belief about its staff and its threat environment.
A likelihood of "Medium" for lateral movement reflects a belief about network segmentation and monitoring
effectiveness. Some of those beliefs will be wrong, and some can be tested before an attacker tests them.
Treating risk scenarios as assumptions to verify, rather than facts to document, is what makes risk assessment
useful rather than decorative.

All the methodologies work in the rational domain: identify threats, estimate likelihood, estimate impact.
This is necessary, but a risk register built solely from this process will be systematically incomplete in
predictable ways.

The [emotional layer](../../foundations/problem-solving/three-domains.md) asks which risks are difficult to
name. Insider threat is chronically underrepresented in risk registers not because it is rare but because
naming it implicates colleagues and changes the atmosphere of the session. A senior employee's access profile
that has not been reviewed in four years is a risk scenario; raising it in a workshop has social consequences.

The [political layer](../../foundations/problem-solving/three-domains.md) asks whose interests are served by a
particular outcome. If treating a risk creates work for one team while the benefit accrues to another,
acceptance becomes the path of least resistance regardless of the risk score.

The methodology provides the structure for a rational assessment. That structure is most useful when the
people using it have also asked: which risks are we unlikely to surface because naming them is uncomfortable,
and whose interests are served by the current picture? Running identification with some form of anonymity, or
separating the identification session from the ownership discussion, gives the awkward risks room to surface.

## Risk treatment

ISO/IEC 27005 names four treatment strategies, each right for different risks:

* Avoidance eliminates the risk by not engaging in the activity: no BYOD at all rather than an elaborate BYOD control stack, an on-premises store rather than a cloud provider whose misconfiguration risk outweighs its savings.
* Modification reduces likelihood or impact through controls, which is where most of the register's entries land: segmentation and detection against open ports, a patching schedule against ageing software.
* Retention accepts a risk after informed assessment, sensibly reserved for cases like brief tolerable outages where full redundancy costs more than the disruption it prevents.
* Sharing spreads consequences to other parties: cloud backups under an SLA with insurance, vendor contracts specifying liability and recovery obligations, escrow for the supplier that might vanish.

Treatment decisions are not immune to the dynamics above. Risk acceptance in particular is politically shaped:
if the cost of treating a risk falls on one team and the benefit accrues to another, acceptance is the outcome
of least resistance regardless of the risk score. An unusually high proportion of accepted Medium or High
risks in one area of the business is worth examining before the register is finalised.

When a treatment that was agreed and resourced stalls repeatedly, or when the same risk is accepted with
unchanged justification in successive cycles, the constraint is usually in the
[political or emotional layer](../../foundations/problem-solving/three-domains.md) rather than the technical
one. Practical signals: a remediation that has not progressed despite being resourced for two review periods;
a risk accepted for the third consecutive year; a treatment plan where the responsible team consistently cites
competing priorities.

The diagnostic question is not whether the risk score is accurate but whether the incentive structure makes
treatment worthwhile for the team responsible for delivering it.
[Escalating to whoever controls those incentives](../../foundations/problem-solving/psl-approach.md) is often
more effective than refining the score.

## Testing risk assumptions before treatment

Risk treatment decisions are based on estimates of likelihood and impact that may not match the environment. Before committing resources to a treatment, some of those estimates can be tested directly. A simulated phishing exercise checks whether the likelihood assigned to social engineering is accurate. A tabletop exercise reveals whether the incident response plan's assumptions about escalation speed and decision authority hold under realistic pressure. A lateral movement test in a controlled environment checks whether the network segmentation model actually contains what it is supposed to contain.

These are not supplementary assurance activities. They are the mechanism by which the risk register moves from
a set of beliefs about the environment to a set of claims grounded in observed behaviour, a sounder basis for
treatment decisions than belief alone.

## Output

By the end of this stage, the organisation has a chosen and documented methodology, a risk register whose
entries are understood as testable hypotheses, a treatment plan with owners and dates, and documented
acceptances that would survive a second look. The register decides what gets packed in
[the gear depot](gear-depot.md).

## Related

* [NIS2 Understanding the river](../nis2/river.md)
* [ISO 22301 Storm charts](../iso22301/storm-charts.md)
* [IEC 62443 Knowing the besiegers](../iec62443/besiegers.md)
* [Threat register](../supportive/threat-register.md)
* [Risk scoring](../supportive/risk-scoring.md)
* [Risk management as a process](../../workshops/risk-management.md)

*Last updated: 4 July 2026*
