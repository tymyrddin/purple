# Locks and patrols

The control layer.

The walls are up, the gates are mapped, the besiegers are named. Controls are the locks, patrols, and safety
routines that make the zone model mean something: IEC 62443-3-3 organises them as system requirements grouped
under seven foundational requirements, from identification and authentication through use control and system
integrity to resource availability, with the stringency scaling to each zone's security level target. This stage
verifies that every defence is in place, documented, and owned, so gaps can be shored up before an auditor arrives.

Each control encodes a model assumption about the ICS environment it is designed to protect. Authentication
controls assume credential management is enforced at every access point, including legacy devices with limited
capability. Monitoring assumes alerts are reviewed and actioned, not suppressed by alert fatigue. When a control
fails during an incident or penetration test, the first question worth asking is not whether the control was
documented but whether the assumption it encoded still held in the environment as deployed.

## Control categories to check

1. Device lifecycle controls: installation, configuration, maintenance, and decommissioning. Gap check: Each device wants complete lifecycle documentation. Missing updates, incomplete decommissioning records, or unclear ownership are findings.
2. Access control: role-based access, separation of duties, authentication, and authorisation. Gap check: Verify documented privileges for controllers, HMIs, engineering workstations, and servers. Ambiguous or outdated access rights are gaps.
3. System integrity and configuration management: baselines, patching, version control, and secure defaults. Gap check: Ensure documented baselines, firmware and software versions, and change management logs exist. Deviations or undocumented changes are gaps.
4. Monitoring and detection: logging, anomaly detection, and alerting. Gap check: Confirm all critical assets are monitored, logs are collected and retained, and alerts have assigned owners. Missing logs or unclear responsibilities are findings.
5. Incident response and recovery: plans, responsibilities, and rehearsals. Gap check: Each threat category has a documented detection and response procedure, or its absence is a gap. Unclear roles and untested procedures count.
6. Physical security controls: access locks, surveillance, tamper-evident seals. Gap check: Verify physical access is controlled and monitored. Missing seals, surveillance blind spots, or unclear inspection schedules are findings.
7. Supply chain and vendor controls: device acceptance, firmware validation, vendor risk management. Gap check: Confirm documented processes exist for all incoming devices and firmware. Gaps here are high-risk audit findings.

Boundary and segmentation controls have their own stage in [walls and gates](walls-and-gates.md); they are listed
in the zone model, not here, precisely because they are structural rather than procedural.

## Practical gap-spotting

* Control-to-threat mapping: every threat from [knowing the besiegers](besiegers.md) has a corresponding control. Missing mappings are critical findings.
* Target alignment: controls in each zone are proportionate to its security level target. A zone with a demanding target and commodity controls is a finding waiting to be written.
* Evidence completeness: for each control, logs, records, or inspection evidence exist.
* Ownership clarity: controls without a responsible owner or custodian are gaps.
* Consistency: policies, procedures, and physical or network configurations match documented controls. Deviations are findings.

*Check that each threat has a documented, effective, and owned control. Any gap is a place to shore up before the
auditor arrives.*

A control that is documented and owned is implementation evidence. A control that produces its intended effect under
realistic conditions is [effectiveness evidence](../../foundations/system-effectiveness/applying-sem.md). The two are
not the same: a firewall rule exists in configuration and on paper; whether it actually contains lateral movement
under a realistic attack path is a different question. [Testing the defences](testing-the-defences.md) is the stage
that converts the first kind of evidence into the second.

## Output

By the end of this stage, the organisation has a control-to-threat mapping with no unmapped threats, controls
proportionate to each zone's security level target, named owners, and documentation consistent with what is
deployed. What remains is to find out whether any of it works.

## Related

* [ISO 22301 The factory's emergency systems](../iso22301/emergency-systems.md)
* [NIS2 Building a raft](../../audits/nis2/raft.md)
* [ISO 27001 The gear depot](../../audits/iso27001/gear-depot.md)
* [Unseen University Power & Light Co. IT/OCS pentest](https://red.tymyrddin.dev/docs/power/)
* [Gap analysis](../supportive/gap-analysis.md)
