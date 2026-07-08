# Watching the tributaries

![Currents](/_static/images/tributaries.png)

NIS2, Article 21: supply chain security.

The river has tributaries feeding into it. Suppliers and partners bring their own risks into the environment,
and NIS2 explicitly requires managing them, because incidents such as SolarWinds, Kaseya, and Log4j have shown
how supplier compromises cascade to customers. Weakness upstream can pull an organisation under even when its
own defences are strong.

## The obligations

In-scope entities take appropriate measures to manage supply chain risks, consider vulnerabilities specific to
each supplier, include security requirements in contracts, and monitor supplier security posture over time.
Suppliers who are themselves in scope have their own compliance requirements; coordination prevents duplication
while ensuring nothing falls through the gaps.

## Mapping and classifying the supply chain

Identification comes first: IT systems and software including SaaS, cloud infrastructure, and managed services;
network and telecommunications providers; hardware and equipment suppliers; system integrators and consultants
with access to the environment; outsourced business processes such as payroll, customer support, or logistics.

Classification by risk and criticality follows. Critical suppliers are single points of failure, hard to
replace quickly, hold access to critical systems or sensitive data, or are essential for service delivery.
Important suppliers have significant impact if compromised and can be replaced, with disruption. Standard
suppliers have limited access or impact and provide commodity services.

## Security requirements, set and enforced

Minimum standards may include:

* Security certifications such as ISO 27001 or SOC 2 for critical suppliers. These are implementation evidence: they confirm a management system passed an audit at a point in time. They are not [effectiveness evidence](../../foundations/system-effectiveness/applying-sem.md) that the supplier's controls produce their intended effect in the context of this specific integration.
* Security questionnaires demonstrating baseline controls.
* Incident notification obligations, so supplier incidents surface.
* Audit rights and regular reporting.
* Data protection measures meeting the organisation's standards.
* Business continuity capabilities, so supplier failures do not become the organisation's failures.

Contracts formalise the expectations: baseline security requirements, incident notification timelines aligned
with the organisation's own obligations, the right to audit or request evidence, approval for subcontractors
with flow-down of requirements, clear data handling terms, termination rights for serious breaches, liability
and indemnification, and reference to NIS2 compliance where suppliers are also in scope.

## Monitoring continuously, not just at onboarding

Regular assessment provides ongoing assurance: annual security reviews for critical suppliers as a minimum,
questionnaires updated to capture control changes, certifications verified as current, supplier posture watched
through threat intelligence and industry reports, and supplier incidents tracked for emerging risk.

Red flags call for immediate action: supplier incidents affecting the organisation's data or services, lost
certifications, significant ownership changes altering the risk profile, financial distress threatening
continuity, repeated SLA breaches, non-compliance with security contract terms.

## Contingency and failure

Alternatives identified before they are needed: relationships with backup vendors, tested failover, documented
transition procedures. Exit strategies built into relationships: data extraction procedures, knowledge transfer
plans that avoid dependency on supplier expertise, realistic transition timelines, protective termination
clauses. Resilience measures reduce the dependency itself: a diverse supplier portfolio, no over-reliance on
single vendors for critical functions, geographic distribution, multi-cloud where appropriate.

## Being someone else's tributary

An organisation that supplies in-scope customers meets the same machinery from the other side: their NIS2
obligations arrive as security requirements, evidence requests, and reporting expectations. The collaborative
version works better than the adversarial one: shared threat intelligence with trusted suppliers, coordinated
incident response when incidents affect multiple parties, participation in sector information sharing, and
security partnerships built on transparency rather than only on contract clauses.

## Output

The output of this stage is a supplier inventory with risk classifications, a security requirements matrix
mapping controls to supplier tiers, an assessment schedule with results tracking, contractual templates for
new suppliers, monitoring procedures that detect problems early, and contingency plans for critical supplier
failures.

## Related

* [ISO 22301 The factory's emergency systems](../iso22301/emergency-systems.md) (supply chain continuity)
* [IEC 62443 Locks and patrols](../iec62443/locks-and-patrols.md) (supply chain and vendor controls)

*Last updated: 4 July 2026*
