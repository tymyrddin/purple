# Storms on the factory floor

ISO 22301 – threats & risks (Clause 8.2: Business impact analysis and risk assessment)

Even a well-run factory can face disruptions. Threats range from equipment failures to human mistakes to supply chain interruptions. Understanding these “storms” lets you prioritise continuity measures and reduce downtime risk.

## Key risk categories

1. Technical failures

   * Controllers, networks, servers, and sensors can fail. A single PLC or SCADA outage can halt production.
   * Checks: Are hardware redundancies and failover systems documented? Are critical updates applied?
   * Typical gaps: Single points of failure, undocumented device replacements, missed patch cycles.

2. Environmental & physical incidents

   * Power outages, floods, fires, HVAC failures, or extreme temperatures can stop operations regardless of the systems themselves.
   * Checks: Are backup power systems tested? Are environmental monitoring and alerts operational? Are evacuation or shutdown procedures documented?
   * Typical gaps: Untested UPS/generator systems, missing environmental logs, unclear responsibility for physical safety.

3. Human errors

   * Misconfiguration, procedural mistakes, or absence of key personnel can cause downtime or unsafe conditions.
   * Checks: Are procedures documented and understood? Is cross-training in place for critical roles?
   * Typical gaps: Outdated procedures, single-person dependencies, incomplete training records.

4. Supply chain interruptions

   * Spares, maintenance contracts, and vendor services are often outsourced; delays can directly impact recovery time.
   * Checks: Are critical suppliers identified? Are alternative vendors or stockpiles planned?
   * Typical gaps: Dependencies on a single supplier, missing spare parts, undocumented vendor recovery times.

5. Cyber incidents affecting OT

   * Malware, ransomware, or misconfigurations in OT or connected IT can stop production or compromise safety.
   * Checks: Are cyber resilience and recovery integrated into continuity planning? Are incidents mapped to operational impact?
   * Typical gaps: IT/OT continuity not aligned, lack of response procedures for cyber events, missing evidence of testing.

## Executive gap‑spotting

* Impact analysis: Are all threats assessed in terms of operational, safety, and financial impact?
* Recovery priorities: Are critical functions clearly identified and prioritised for rapid restoration?
* Cross-dependencies: Are IT, OT, supply chain, and vendor dependencies mapped to avoid cascading failures?
* Historical lessons: Are past incidents and near-misses documented and used to improve resilience planning?
* Residual risk: Are threats with high likelihood or impact mitigated, and is any remaining risk understood by management?


*Picture each “storm” hitting your factory. Could your operations continue? Could your teams act quickly and 
effectively? Anything you hesitate on is a gap that must be addressed.*

## Related

* [IEC 62443 Factory floor under inspection](../iec62443/assets.md)
* [NIS2 Understanding the river](../../audits/nis2/river.md)
* [ISO 27001 Risk tent](../../audits/iso27001/risk-tent.md)
* [Unseen University Power & Light Co. IT/OCS pentest](https://red.tymyrddin.dev/docs/power/)
* [Threat modelling & preparation](../../threat-modelling/index.rst)
