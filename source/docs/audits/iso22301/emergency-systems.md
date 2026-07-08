# The factory's emergency systems

ISO 22301, Clause 8.3: business continuity strategies and solutions.

Controls are the structures that keep the factory running when things go wrong. Think of them as backup
generators, failover networks, spare parts, trained personnel, and pre-arranged suppliers. The goal is not
theoretical protection, but real, tested resilience that can be executed under pressure. Strategies are chosen
against the recovery priorities from the [storm charts](storm-charts.md): a solution that does not trace back
to an impact analysis is equipment bought for a storm nobody forecast.

Each continuity control encodes a model assumption. Redundancy assumes the failover path is tested and reachable
when the primary fails. Recovery arrangements assume the team is trained, the documentation is accessible, and
the escalation contacts are current. Business continuity plans assume the impact analysis reflects current
operational reality. When a control fails during an actual disruption, the first question worth asking is not
whether the procedure was followed but whether the assumption the control was built on still held at the time.

## Core continuity measures

1. Redundancy and failover
   * Spare devices, redundant networks, and alternative power sources prevent a single failure from halting production.
   * Checks: Are backups tested? Is failover automatic or documented manual? Are critical assets covered?
   * Typical gaps: Single points of failure, untested spares, undocumented failover steps.

2. Recovery arrangements for critical functions
   * Each function with a recovery time objective needs a solution capable of meeting it: standby equipment, alternative production paths, manual workarounds, or arrangements with third parties.
   * Checks: Does each recovery objective from the impact analysis have a matched solution? Has the solution been costed and resourced?
   * Typical gaps: Recovery objectives with no corresponding solution, solutions that assume resources shared with the function they are meant to replace.

3. Supply chain continuity
   * Missing parts, delayed maintenance, or vendor outages can extend downtime.
   * Checks: Are critical suppliers identified? Are alternative vendors pre-approved? Is stock of spares sufficient?
   * Typical gaps: Reliance on single suppliers, undocumented supply chain risks, missing contingency stock.

4. People
   * Cross-training, documented handovers, and coverage for critical roles are continuity solutions as much as any generator.
   * Checks: Can each critical role be covered by more than one person? Are role-specific skills documented and refreshed?
   * Typical gaps: Single-person dependencies surfacing only when the person is unavailable, training records that stop at attendance.

## Executive gap-spotting

* Coverage: Are all critical OT and supporting IT operations addressed by a continuity solution?
* Traceability: Does each solution map back to a recovery objective in the impact analysis?
* Resource alignment: Are staff, spares, and backup systems adequate for critical function recovery?
* Supply chain alignment: Are vendor and parts dependencies mapped, with alternatives in place?

*Walk the factory mentally during a disruption. Can operations continue if a critical PLC fails? If the network
goes down? If a key supplier is delayed? Anything you hesitate on is a continuity gap needing attention.*

Solutions on their own are hardware and contracts. What turns them into a capability is the [drill book](drill-book.md)
that tells people how to use them, and the [drills](drills.md) that confirm they work.

## Output

By the end of this stage, each critical function has a selected continuity strategy with the resources to carry
it: redundancy where the impact analysis justifies it, pre-approved alternative suppliers, contingency stock, and
cover for critical roles. Each solution is owned, costed, and traceable to a recovery objective.

## Related

* [IEC 62443 Locks and patrols](../iec62443/locks-and-patrols.md)
* [NIS2 Building a raft](../../audits/nis2/raft.md)
* [ISO 27001 The gear depot](../../audits/iso27001/gear-depot.md)
* [Gap analysis](../supportive/gap-analysis.md)
* [Unseen University Power & Light Co. IT/OCS pentest](https://red.tymyrddin.dev/docs/power/)

*Last updated: 4 July 2026*
