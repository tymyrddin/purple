# The factory’s emergency systems

ISO 22301 – continuity measures / controls (Clause 8.3: Business continuity strategies and solutions)

Controls are the structures that keep the factory running when things go wrong. Think of them as backup generators, 
failover networks, spare parts, trained personnel, and documented procedures. The goal is not theoretical protection, 
but real, tested resilience that can be executed under pressure.

## Core continuity measures

1. Business Impact Analysis (BIA)

   * Identifies critical functions, determines maximum tolerable downtime (MTD), recovery time objectives (RTOs), and recovery point objectives (RPOs).
   * Checks: Has every OT function been assessed for operational and financial impact? Are priorities clear?
   * Typical gaps: Outdated BIAs, missing RTO/RPO definitions, no linkage to recovery plans.

2. Redundancy & failover

   * Spare devices, redundant networks, and alternative power sources prevent a single failure from halting production.
   * Checks: Are backups tested? Is failover automatic or documented manual? Are critical assets covered?
   * Typical gaps: Single points of failure, untested spares, undocumented failover steps.

3. Incident response & recovery procedures

   * Step-by-step procedures reduce reaction time and errors during disruptions.
   * Checks: Are procedures accessible and understood? Are responsibilities clearly assigned? Are escalation paths defined?
   * Typical gaps: Outdated or missing procedures, unclear roles, incomplete escalation plans.

4. Testing & exercises

   * Plans that are never exercised often fail in real scenarios.
   * Checks: Are drills and simulations conducted regularly? Are results documented and follow-up actions tracked?
   * Typical gaps: No test schedule, exercises not documented, lessons not applied to plans.

5. Supply chain continuity

   * Missing parts, delayed maintenance, or vendor outages can extend downtime.
   * Checks: Are critical suppliers identified? Are alternative vendors pre-approved? Is stock of spares sufficient?
   * Typical gaps: Reliance on single suppliers, undocumented supply chain risks, missing contingency stock.

6. Communication plans

   * Coordinated communication ensures timely decisions and reduces confusion.
   * Checks: Are internal notifications, vendor communications, and executive reporting protocols documented?
   * Typical gaps: Unclear contact lists, missing escalation steps, inadequate communication for remote teams.

## Executive gap‑spotting

* Coverage: Are all critical OT and supporting IT operations included in continuity plans?
* Responsibility clarity: Are every procedure, system, and recovery action assigned to a named role?
* Testing evidence: Have all continuity measures been exercised, with documented follow-up?
* Resource alignment: Are staff, spares, and backup systems adequate for critical function recovery?
* Supply chain alignment: Are vendor and parts dependencies mapped, with alternatives in place?
* Communication readiness: Can stakeholders be informed and coordinated efficiently in a disruption?

*Walk the factory mentally during a disruption. Can operations continue if a critical PLC fails? If the network goes down? If a key supplier is delayed? Anything you hesitate on is a continuity gap needing attention.*

## Related

* [IEC 62443 The factory’s defensive mechanisms](../iso22301/controls.md)
* [NIS2 Building a raft](../../audits/nis2/raft.md)
* [ISO 27001 The gear depot](../../audits/iso27001/gear-depot.md)
* [Unseen University Power & Light Co. IT/OCS pentest](https://red.tymyrddin.dev/docs/power/)
