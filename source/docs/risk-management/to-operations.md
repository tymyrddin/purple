# From exercises to operations

You have built a risk register and documented a process. The question now is whether that work will change how the organisation operates, or whether it will describe how the organisation should operate while actual operations continue unchanged.

This is the [ChangeShop](../foundations/change-management/index.rst) question. The exercises produced accurate analysis. The register documents decisions. Whether those decisions produce change depends on conditions that the exercises themselves cannot create: ownership that is real rather than nominal, authority to implement treatments, protected time and budget, and the trust and communication conditions that allow people to be honest about progress and blockages.

## Integration points

With ISO 27001: the risk register feeds control selection from Annex A. The risk assessment documentation satisfies clause 6.1. Treatment plans become the implementation roadmap. Risk reviews inform the management reviews required by clause 9.3. These connections are straightforward once the underlying risk work is done honestly; they become problematic when the risk work is done primarily to satisfy the audit rather than to understand the actual exposure.

With NIS2: critical assets identified in the exercises map to the Article 21 risk analysis requirement. The risk assessment supports the "appropriate and proportionate" standard for security measures. Treatment plans address the mandatory security measures. The register demonstrates systematic risk management to supervisory authorities.

With incident response: known risks should have documented response procedures. When an incident occurs in a risk category that was assessed and given a treatment plan, the response should be faster and more effective than if the risk had not been thought through. When an incident reveals a risk that was not in the register, that gap is a finding that requires both an incident response and a risk register update.

With business continuity: asset dependencies identified in the exercises inform continuity plans. Impact assessments determine recovery priorities. The register identifies single points of failure that continuity planning needs to address. These connections mean that risk management and continuity planning should be coordinated, not run as parallel exercises that duplicate effort and sometimes produce inconsistent conclusions.

## Maturity as a realistic trajectory

Rather than a fixed maturity model with defined levels, think of maturity as a direction. The starting point is wherever the organisation is. The direction is toward risk management that is:

More proactive: risks identified and addressed before they materialise as incidents, rather than discovered through incidents.

More integrated: risk thinking embedded in how decisions are made, rather than conducted as a separate exercise.

More accurate: risk assessments that reflect the actual environment, updated when conditions change, rather than documents that describe the environment as it was when the last workshop was run.

More owned: treatment decisions that belong to people who have the capacity and authority to implement them, rather than action items assigned to whoever was in the room.

Progress along this trajectory is uneven and non-linear. A significant incident can reveal that the risk model was substantially wrong in ways that require rebuilding rather than updating. A leadership change can affect the political conditions for implementing treatments. An organisational restructuring can invalidate ownership assignments. These are not failures of the risk management process; they are the reasons the process needs to be continuous rather than episodic.

## What operations looks like

Monthly: review critical risks, check treatment progress against the committed timeline, update the register based on any incidents or significant changes.

Quarterly: review high and medium risks, report to relevant stakeholders in a format matched to what they need to know, adjust treatment priorities based on progress and any changes in the risk landscape.

Annually: refresh the full risk assessment, validate that the likelihood and impact criteria still reflect the organisation's actual context, review the process itself for whether it is producing useful outputs, update risk appetite if organisational circumstances have changed.

As needed: when any of the triggers documented in the risk model fire.

The resources for going deeper into quantitative risk modelling and framework alignment are ISO 31000 (risk management principles), ISO 27005 (information security risk management), NIST SP 800-30 (risk assessment guidance), and FAIR (Factor Analysis of Information Risk) for organisations that need to quantify risk in financial terms.

## Related

- [The risk register](risk-register.md)
- [Building your risk model](risk-model.md)
- [What ChangeShop is](../foundations/change-management/what-it-is.md)
- [SOC maturity](../making-of/soc/maturity.md)
