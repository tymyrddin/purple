# The floor walk

ISO 22301, Clauses 4, 5 and 8.1: context, leadership, and operational planning.

Every continuity plan rests on knowing what the factory is. Before charting storms or building emergency
systems, walk the floor: establish what the business continuity management system covers, who answers for it,
and what is actually running out there. A plan scoped around an out-of-date picture of the factory protects
the factory that used to exist.

## Scope and leadership first

Clause 4 asks for context: which products, services, and sites the continuity system covers, which interested
parties depend on them, and what the organisation has decided is in and out of scope. A scope statement that
can be read aloud in one paragraph, without anyone in the room frowning, is a reasonable test.

Clause 5 places responsibility with top management: an approved continuity policy, roles and responsibilities
assigned, and resources committed. Continuity that lives entirely inside the operations team, without
board-level ownership, is a gap auditors notice early, and disruptions notice earlier.

## The factory's heartbeat

Assets are the essential cogs that make production run. From controllers to networks to supporting IT, each
element has a direct impact on uptime, safety, and operational resilience. Any undocumented, mismanaged, or
unsupported asset is a potential point of failure, slowing recovery and increasing risk during a disruption.

1. Industrial controllers and PLCs
   * These devices orchestrate production processes. Failure or misconfiguration can halt operations instantly.
   * Checks: Redundancy in place? Lifecycle documentation complete? Replacement procedures defined? Maintenance schedules adhered to?
   * Typical gaps: Missing spare units, unclear ownership, incomplete update or patch records.

2. SCADA servers and HMIs
   * Central monitoring and control; a single point of visibility for operators.
   * Checks: Backup routines tested? Failover procedures validated? Access controls documented?
   * Typical gaps: Outdated backup logs, undocumented failover steps, misaligned operator permissions.

3. Networks and communications
   * Segmented and monitored networks prevent a single failure from cascading across production.
   * Checks: Network diagrams current? Redundant paths verified? Monitoring and alerting in place?
   * Typical gaps: Zones not clearly defined, undocumented network changes, monitoring gaps in critical paths.

4. Field devices and sensors
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

## Executive gap-spotting

* Comprehensive documentation: Are all critical assets recorded and mapped to continuity priorities? Missing items are blind spots.
* Ownership clarity: Does each asset have a responsible owner or custodian? Ambiguity means delayed response in disruption.
* Lifecycle completeness: Are installation, maintenance, updates, and decommissioning steps fully documented and current?
* Criticality ratings: Are assets rated by operational impact to prioritise recovery efforts? Without prioritisation, recovery wastes time and resources.
* Redundancy and readiness: Are backups, spares, and failover mechanisms in place and tested?

*Walk through the factory mentally: each asset wants to be visible, documented, and accounted for. Anything you
cannot immediately point to or explain is a gap waiting to disrupt operations.*

Asset documentation is a model of the factory's operational state at a point in time. The model ages: assets are
upgraded, replaced, moved, or taken offline without the documentation following. When the documented state and the
actual state diverge, the gap is not primarily a record-keeping failure: it is evidence that the process maintaining
alignment between documentation and reality has a mismatch. Recovery procedures that depend on stale asset
documentation will fail at the moment they are most needed.

## Output

By the end of this stage, the organisation has a scope statement for the continuity system, an approved policy
with named roles and board-level ownership, and an asset register mapped to continuity priorities with owners,
criticality ratings, and current lifecycle records. This is the map the storm charts are drawn on.

## Related

* [IEC 62443 Surveying the fortress](../iec62443/survey.md)
* [NIS2 Understanding the river](../../audits/nis2/river.md)
* [ISO 27001 Risk tent](../../audits/iso27001/risk-tent.md)
* [Unseen University Power & Light Co. IT/OCS pentest](https://red.tymyrddin.dev/docs/power/)
* [Risk management as a process](../../workshops/risk-management.md)
* [Gap analysis](../supportive/gap-analysis.md)

*Last updated: 4 July 2026*
