# Threat register

A threat register is a structured record of the threats an organisation has identified as relevant to its
systems, services, and operations. It is the input side of risk management: the register captures what could
go wrong, so that the risk assessment can evaluate likelihood and impact, and controls can be selected and
mapped against each threat.

## What to capture per entry

A minimal entry includes:

| Field                 | What it captures                                                |
|:----------------------|:----------------------------------------------------------------|
| Threat ID             | A reference for tracking and cross-referencing                  |
| Threat description    | What the threat is, in plain language                           |
| Threat category       | Class of threat (e.g. malware, insider, supply chain, physical) |
| Affected assets       | Which systems, data, or services are exposed                    |
| Relevant threat actor | Nation-state, organised crime, opportunistic attacker, insider  |
| Current controls      | What is already in place to address this threat                 |
| Residual risk rating  | Low, medium, high, or critical after controls are considered    |
| Owner                 | Who is responsible for the entry and for tracking treatment     |

Threat categories are typically drawn from the relevant framework: ISO 27001 Annex A, IEC 62443, or MITRE
ATT&CK. The category drives which controls are evaluated during risk assessment.

## Populating the register

Sources for threat identification include:

* Risk assessment workshops and stakeholder interviews
* Threat intelligence: sector-specific reporting, CSIRT alerts, vendor advisories
* Findings from penetration tests and vulnerability assessments
* Post-incident reviews: what actually happened, not only what was anticipated in advance
* Regulatory guidance: supervisory authorities for many sectors publish relevant threat scenarios

A register populated only from workshops and standard framework templates will be systematically incomplete in
predictable ways. The threats easiest to list are those with clear technical profiles and unambiguous ownership.
The threats hardest to list are those whose naming creates social or political difficulty: insider threat is
chronically underrepresented not because it is rare but because naming a colleague as a plausible threat actor
changes the atmosphere of the room. Running the identification phase with anonymous input, or separating
identification from the ownership discussion, creates space for these threats to surface. The
[three domains of problem solving](../../foundations/problem-solving/three-domains.md) describe why a rational
identification process alone leaves predictable categories out.

## Connecting threats to controls

A threat without a documented control is an open gap, not a managed risk. The threat register and the control
set should cross-reference: every register entry should map to at least one control in the Statement of
Applicability or control catalogue, and every control should trace back to the threats it addresses. Unmapped
threats and orphaned controls are both findings.

## Maintaining the register

A threat register that is not reviewed is a snapshot frozen at the point it was last updated. Threat actors
change their techniques. New vulnerabilities change which systems are most exposed. Business changes create new
attack surfaces. The register needs a review cycle tied to the broader risk assessment schedule, and a process
for incorporating new intelligence as it arrives.

When a threat appears on the register as accepted risk for multiple consecutive cycles without evidence of
re-evaluation, the acceptance is worth scrutinising. It may reflect a genuine and current risk appetite
decision. It may reflect that the cost of treatment falls on a team that does not benefit from the fix.

## Related

* [ISO 27001 Risk tent](../iso27001/risk-tent.md)
* [NIS2 Understanding the river](../nis2/river.md)
* [IEC 62443 Threats to the factory](../iec62443/threats.md)
* [ISO 22301 Storms on the factory floor](../iso22301/threats.md)
* [Arrows and shields](arrows-shields.md)
* [Attack path mapping](../../threat-modelling/attack-path-mapping.md)
* [Adversary persona workshop](../../threat-modelling/adversary-persona-workshop.md)
* [Risk scoring](risk-scoring.md)
* [Interview and workshop facilitation](interview-facilitation.md)