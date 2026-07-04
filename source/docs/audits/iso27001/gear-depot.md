# The gear depot

![Gear depot](/_static/images/gear-depot.png)

ISO/IEC 27001, Clause 6.1.3 and Annex A: controls, the risk treatment plan, and the Statement of Applicability.

With [a reliable framework for risk management](risk-tent.md) in place, the gear depot is where security
controls get selected and maintained: the tools and equipment that protect the expedition on the climb. Just as
climbers choose gear based on the route ahead, organisations select controls based on identified risks. Not
every climb needs ice axes, and not every organisation needs the same controls.

## Controls

Controls are the practical technical, physical, and organisational measures that protect assets and operations:
what actually gets done about the risks identified. They are selected as part of risk treatment; ISO/IEC 27001
Annex A provides a comprehensive catalogue, and organisations can define additional controls to suit their
context. Controls mainly serve risk modification; avoidance needs no controls (the activity is simply not
undertaken), retention needs a documented acceptance, and sharing pushes controls onto suppliers and insurers
through contracts and SLAs.

Two classification dimensions describe how controls work:

| Control type | Goal                                   | Examples                                                                                                    |
|--------------|----------------------------------------|-------------------------------------------------------------------------------------------------------------|
| Preventive   | Stop incidents before they happen      | Security policy, confidentiality agreements, cryptography, environment segregation, access control software |
| Detective    | Identify incidents quickly             | Audit logs, intrusion detection systems, monitoring, alarms, video surveillance, reconciliation checks      |
| Corrective   | Minimise impact and prevent recurrence | Patching, backup recovery, incident investigation, business continuity plan activation, system restoration  |

| Control type | Goal                                                    | Examples                                                                                       |
|--------------|---------------------------------------------------------|------------------------------------------------------------------------------------------------|
| Management   | Align ISMS with organisational strategy                 | Risk management, management reviews, continual improvement, policy definition                  |
| General      | Baseline security mechanisms for all systems            | Annual review of user access, baseline security controls from ISO/IEC 27001 Annex A            |
| Specific     | Controls embedded in individual applications or systems | Application authentication, transaction validation, access mechanisms for specific ERP systems |

A single control often spans categories: antivirus is preventive, detective, and corrective at once; an annual
access review is detective by function and general by scope. The layering is the point. A control strategy
relying solely on prevention fails the day prevention is bypassed, so a resilient set mixes prevention,
detection, and correction deliberately, defence in depth rather than a single wall. And however carefully the
gear is chosen, it reduces risk without eliminating it; the mountain will always have rocks.

Selection stays honest through a few habits: every control ties to a risk or treatment decision in the
register, proportionate to the threat rather than exhaustive; costs are weighed against what the control
actually buys; and the reasoning gets written down as it happens, because the Statement of Applicability will
ask for it later.

Every control encodes a model assumption about the environment it operates in. MFA assumes users have reliable
access to a second factor and sufficient time to use it. Annual access reviews assume that ownership of the
review process is clear and that someone is accountable for acting on the findings. A SIEM assumes the threat
profile is anomalous relative to a stable baseline.

When a control is technically present but behaviourally ineffective, the model is usually the culprit: the
assumption does not fit the operational reality. Before selecting a control, it is worth asking what the
control assumes, and whether those assumptions hold in this environment.

## The risk treatment plan

Clause 6.1.3c requires a documented plan bridging "we know the risks" and "we've implemented controls": the
climbing schedule, showing which routes come first, what equipment is needed, who leads each pitch, and when
each checkpoint is expected. The plan specifies five things:

* The actions to be taken: specific controls, not vague intentions.
* The resources required: budget, people, time.
* Who is responsible: control owners, project leads, approvers.
* When it will be completed: dates, milestones, dependencies.
* How residual risk will be evaluated afterwards.

The format is free: treatment columns added to the [risk register](../../risk-management/risk-register.md), a
standalone plan, or a project board. What separates a working plan from a decorative one is specificity.
"Implement security controls" fails every test that "deploy MFA for Office 365, IT Manager, €1,500, complete
by 15 March, verified by simulated bypass attempt" passes.

Prioritisation is triage: high risks and quick wins first, complex treatments staged, resources matched to
budget cycles and staff capacity, contractual and legal deadlines respected. Not everything can be treated at
once, and a plan that pretends otherwise treats nothing well.

Before rolling out a control across the organisation, running it with one team first reveals friction the
design did not anticipate. If a change approval process adds three steps to a deployment that previously took
one, the organisation will discover this either during a controlled pilot or during a frustrated workaround
that quietly bypasses the control entirely.

Friction observed in a pilot is system information: it describes the gap between the model the control was
designed for and the environment it is entering. Adjusting before scaling is far less costly than discovering
the gap after the rollout has produced a compliance posture that diverges from actual practice.

The plan lives: monthly status updates, quarterly reprioritisation, an annual refresh aligned with the updated
risk assessment, and triggered reviews after incidents, business changes, or failed implementations. A plan
still showing last year's dates is not a plan; it is a fossil.

## The Statement of Applicability

The Statement of Applicability (SoA) is the central record of which Annex A controls (and any additional ones)
have been implemented, which have been excluded, and why. It links every control to the risks it addresses,
tracks implementation status, and serves as the single reference point for auditors, regulators, and
management. It is created once risk treatment decisions exist, usually owned by the CISO or security manager,
and reviewed at least annually or when something significant changes.

A typical row carries the control reference, applicability, implementation status, the risk references it
addresses, the justification, and evidence. Exclusions want thoughtful justification: the activity is avoided,
the risk is formally accepted, the control is managed by a third party under contract, or it genuinely does
not apply at this size and context, with compensating controls named where they exist. "Too hard" and "no
budget" are not on that list.

The Evidence column records both implementation evidence (the control is in place) and [effectiveness evidence](../../foundations/system-effectiveness/applying-sem.md) (the
control produces its intended effect). Where a control is fully implemented, effectiveness evidence takes the
form of a repeatable scenario: a quarterly access review that finds and removes something, a detection test
confirming an alert fires within minutes, a remote wipe drill with timings, a phishing click rate that moved
after training.

That kind of evidence is more durable than a deployment log, and during audits both kinds will be asked for:
that the control exists, and that it achieves its purpose.

## Output

By the end of this stage, the organisation has a control set layered across prevention, detection, and
correction, each control traceable to a risk; a risk treatment plan with owners, dates, resources, and success
criteria; and a Statement of Applicability justifying every inclusion and exclusion, with space reserved for
the effectiveness evidence the climb will generate. [Now theory meets altitude](climb.md).

## Related

* [NIS2 Building a raft](../nis2/raft.md)
* [ISO 22301 The factory's emergency systems](../iso22301/emergency-systems.md)
* [IEC 62443 Locks and patrols](../iec62443/locks-and-patrols.md)
* [Gap analysis](../supportive/gap-analysis.md)
