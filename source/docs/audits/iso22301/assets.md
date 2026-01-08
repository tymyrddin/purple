# The factory’s heartbeat

ISO 22301 – assets (Clause 8.1: Operational planning and control)

Assets are the essential cogs that make production run. From controllers to networks to supporting IT, each element 
has a direct impact on uptime, safety, and operational resilience. Any undocumented, mismanaged, or unsupported asset 
is a potential point of failure, slowing recovery and increasing risk during a disruption.

## Key asset categories

1. Industrial controllers & PLCs

   * These devices orchestrate production processes. Failure or misconfiguration can halt operations instantly.
   * Checks: Redundancy in place? Lifecycle documentation complete? Replacement procedures defined? Maintenance schedules adhered to?
   * Typical gaps: Missing spare units, unclear ownership, incomplete update or patch records.

2. SCADA servers & HMIs

   * Central monitoring and control; a single point of visibility for operators.
   * Checks: Backup routines tested? Failover procedures validated? Access controls documented?
   * Typical gaps: Outdated backup logs, undocumented failover steps, misaligned operator permissions.

3. Networks & communications

   * Segmented and monitored networks prevent a single failure from cascading across production.
   * Checks: Network diagrams current? Redundant paths verified? Monitoring and alerting in place?
   * Typical gaps: Zones not clearly defined, undocumented network changes, monitoring gaps in critical paths.

4. Field devices & sensors

   * They collect process data and trigger safety or automation functions. Faulty sensors or missing calibration can disrupt production or safety.
   * Checks: Spares available? Calibration documented and current? Monitoring of device health in place?
   * Typical gaps: Sensors missing in documentation, overdue calibration, unmonitored devices.

5. Physical infrastructure

   * Power supplies, enclosures, and environmental controls support everything else. A failure here stops the factory even if devices are functional.
   * Checks: UPS and generators tested? Cooling and environmental controls operational? Access controlled?
   * Typical gaps: Outdated maintenance logs, untested backup power, unclear responsibility for environmental systems.

6. Supporting IT systems

   * ERP, reporting, and logging systems tie OT processes into organisational operations. Their failure can prevent informed decision-making during incidents.
   * Checks: Backups tested? System dependencies documented? Logging and alerting operational?
   * Typical gaps: Disconnected IT-OT systems, incomplete logs, undocumented recovery steps.

## Executive gap‑spotting

* Comprehensive documentation: Are all critical assets recorded and mapped to continuity priorities? Missing items = blind spots.
* Ownership clarity: Does each asset have a responsible owner or custodian? Ambiguity = delayed response in disruption.
* Lifecycle completeness: Are installation, maintenance, updates, and decommissioning steps fully documented and current?
* Criticality ratings: Are assets rated by operational impact to prioritise recovery efforts? Lack of prioritisation = wasted time and resources during recovery.
* Redundancy & readiness: Are backups, spares, and failover mechanisms in place and tested?


*Walk through the factory mentally: each asset should be visible, documented, and accounted for. Anything you can’t immediately point to or explain is a gap waiting to disrupt operations.*

## Related

* [IEC 62443 Factory floor under inspection](../iec62443/assets.md)
* [NIS2 Understanding the river](../../audits/nis2/river.md)
* [ISO 27001 Risk tent](../../audits/iso27001/risk-tent.md)
* [Unseen University Power & Light Co. IT/OCS pentest](https://red.tymyrddin.dev/docs/power/)
* [What matters (asset identification)](../../risk-management/asset-identification.md)
