# Supply chain and third-party risk

Every organisation's security boundary includes a layer it does not control: the suppliers, vendors, integrators,
and software components that enter the environment from outside. Supply chain compromise is consistently one of
the highest-impact attack vectors in current threat reporting, not because it is technically clever but because
it exploits trust that has already been extended and access that has already been granted.

From an audit perspective, supply chain risk cuts across all major frameworks. The question is not whether an
organisation uses third parties. It is whether the risk those relationships introduce is visible, assessed, and
managed with the same discipline applied to internal risks.

## What the frameworks require

### NIS2

Article 21(2)(d) explicitly lists supply chain security as one of the mandatory measures essential entities and
important entities are required to implement. This covers security in the relationships with direct suppliers and
service providers, and consideration of the security practices of each supplier's own supply chain.

The obligation covers security arrangements in contracts, assessments of supplier security measures, and
monitoring of supplier-related incidents. The NIS2 framing treats supply chain security as an ongoing practice,
not a one-time due diligence check at contract signing.

### ISO 27001:2022

Two controls address this directly. A.5.21 covers managing information security in the ICT supply chain:
identifying and implementing controls to address information security risks associated with the supply of products
and services. A.5.22 covers monitoring, review, and change management of supplier services: regularly reviewing
and managing changes to supplier-provided services and maintaining the agreed level of information security.

The 2022 revision strengthened supply chain controls significantly relative to the 2013 version, reflecting the
maturation of supply chain attacks over that period.

### IEC 62443-2-1

In operational technology environments, supply chain risk carries additional weight because many ICS components
were not designed with security in mind and patching cycles are constrained by operational requirements.
IEC 62443-2-1 addresses supply chain security through requirements for procurement processes, component vetting,
and the documentation of security properties for acquired components.

The zone-and-conduit model adds a spatial dimension to supply chain risk: a compromised component or software
update can introduce a threat from outside a zone boundary in a way that bypasses the network controls designed
to protect it.

## Scoping the supply chain

Not all suppliers carry the same risk. The scoping question is which supplier relationships create meaningful
exposure to the organisation's critical assets or services.

A useful starting taxonomy:

| Category | What it covers | Typical risk profile |
|:---------|:---------------|:---------------------|
| Technology and software providers | SaaS platforms, cloud infrastructure, licensed software | Code execution, data residency, credential federation, update channels |
| Service providers with system access | Managed security services, IT support, outsourced operations | Privileged access, monitoring coverage, incident response interface |
| Component and hardware suppliers | OT components, network equipment, firmware | Embedded vulnerabilities, counterfeit risk, update integrity |
| Professional services | Consultants, auditors, system integrators | Temporary access, credential handling, data exposure during engagement |
| Fourth parties | Suppliers' own dependencies | Indirect exposure, often invisible until an incident |

Fourth-party risk is the boundary that is most consistently underestimated. An organisation that has strong
supplier contracts and assessments can still be exposed through a dependency two steps removed that nobody
mapped.

## Assessing supplier security posture

Initial assessment at onboarding covers the minimum security baseline expected of a supplier. This typically
involves questionnaires, review of certifications (ISO 27001, SOC 2), and contractual obligations. None of these
activities produces evidence about what the supplier actually does. They produce evidence about what the supplier
claims and what it has agreed to.

Evidence of actual practice is harder to obtain but more valuable. Relevant sources include:

* Audit rights clauses exercised, not just contracted
* Penetration test results shared under NDA
* Incident disclosure history
* Independent certification body reports
* Observed integration behaviour: access patterns, data flows, configuration of supplier-managed components

The last of these is the most grounded. A supplier whose integration behaviour is observable in the
organisation's own logs, network traffic, and configuration management can be assessed against that evidence
rather than against their claims about it.

For OT environments, factory acceptance testing and integration testing before deployment offer a practical
opportunity to assess component security properties in a controlled environment before they enter the operational
network.

## Maintaining visibility as things change

The risk a supplier represents at contract signing is not the risk they represent twelve months later. Changes
that can alter the picture include:

* Supplier acquisition, merger, or restructure
* Changes in the supplier's own technology stack or subcontractors
* Changes in the scope of the supplier's access to the organisation's environment
* Incidents affecting the supplier's systems, whether disclosed or discovered independently
* New vulnerabilities in software or components the supplier provides

A contractual right to be notified of material changes is a starting point. An operational practice of
monitoring for signals that those changes have occurred is more reliable. Threat intelligence feeds that include
supplier names, sector-specific advisories, and disclosure monitoring for critical software components can
surface changes that supplier notification processes miss.

## Building the evidence record

A policy that says "suppliers are security-assessed" is a documentation control. The evidence that counts
is what each assessment produced and what changed as a result.

Evidence worth preparing includes:

* Completed assessments with dates, scope, and outcomes
* Supplier contracts with security obligations specified
* Records of ongoing monitoring: review meetings, incident reports, service level data
* Evidence of remediation when assessments identified gaps
* Configuration records for supplier-managed access: accounts, permissions, session logging

In simulation environments, purple team exercises that include a supply chain compromise scenario reveal
whether detection and response capabilities extend to that threat vector. A CTF scenario using a simulated
rogue software update, a compromised vendor credential, or a malicious component tests whether controls are
calibrated against that attack path. Where an exercise reveals detection gaps, those gaps can be addressed
before an external review, and the corrective actions documented as evidence of a proactive and tested
security posture.

## Related

* [Arrows and shields](arrows-shields.md)
* [EU regulations](eu-regulations.md)
* [ISO/IEC standards reference](standards.md)
* [OT standards reference](ot-standards.md)
* [Threat register](threat-register.md)
* [Gap analysis](gap-analysis.md)
