# The factory’s defensive mechanisms

The walls are up, the machines are running, threats are mapped. Controls are the locks, patrols, and safety routines that keep the factory resilient. This is about verifying that every defence is in place, documented, and effective, so gaps can be shored up before an auditor arrives.

Each control encodes a model assumption about the ICS environment it is designed to protect. Network segmentation assumes traffic follows the paths shown in the diagram. Authentication controls assume credential management is enforced at every access point, including legacy devices with limited capability. Monitoring assumes alerts are reviewed and actioned, not suppressed by alert fatigue. When a control fails during an incident or penetration test, the first question worth asking is not whether the control was documented but whether the assumption it encoded still held in the environment as deployed.

## Control categories to check

1. Device lifecycle controls – Installation, configuration, maintenance, and decommissioning. Gap check: Each device must have complete lifecycle documentation. Missing updates, incomplete decommissioning records, or unclear ownership are findings.
2. Access control – Role-based access, separation of duties, authentication, and authorisation. Gap check: Verify documented privileges for controllers, HMIs, engineering workstations, and servers. Ambiguous or outdated access rights are gaps.
3. Network segmentation and boundary controls – VLANs, firewalls, and industrial DMZs. Gap check: Confirm that critical devices reside in the correct zones, and that firewall/segmentation rules match network diagrams. Any misaligned devices or undocumented rules are findings.
4. System integrity and configuration management – Baselines, patching, version control, and secure defaults. Gap check: Ensure documented baselines, firmware/software versions, and change management logs exist. Deviations or undocumented changes are gaps.
5. Monitoring and detection – Logging, anomaly detection, and alerting. Gap check: Confirm all critical assets are monitored, logs are collected and retained, and alerts have assigned owners. Missing logs or unclear responsibilities are findings.
6. Incident response and recovery – Plans, responsibilities, and rehearsals. Gap check: Each threat category should have a documented detection and response procedure. Missing plans, unclear roles, or untested procedures are gaps.
7. Physical security controls – Access locks, surveillance, tamper-evident seals. Gap check: Verify physical access is controlled and monitored. Missing seals, surveillance blind spots, or unclear inspection schedules are findings.
8. Supply chain and vendor controls – Device acceptance, firmware validation, vendor risk management. Gap check: Confirm documented processes exist for all incoming devices and firmware. Gaps here are high-risk audit findings.

## Practical gap‑spotting

* Control-to-threat mapping: Every threat must have a corresponding control. Missing mappings are critical findings.
* Evidence completeness: For each control, ensure logs, records, or inspection evidence exist.
* Ownership clarity: Controls without a responsible owner or custodian are gaps.
* Consistency: Policies, procedures, and physical or network configurations must match documented controls. Deviations are findings.

*Check that each threat has a documented, effective, and owned control. Any gap is a place to shore up before the auditor arrives.*

A control that is documented and owned is implementation evidence. A control that produces its intended effect under 
realistic conditions is [effectiveness evidence](../../foundations/system-effectiveness/applying-sem.md). The two are 
not the same: a firewall rule exists in configuration and on paper; whether it actually contains lateral movement 
under a realistic attack path is a different question. Penetration testing, PoC exercises, and tabletop walkthroughs 
against specific threat scenarios are the mechanisms that convert implementation evidence into effectiveness evidence. 
When a control has never been tested against the threat it is designed to address, it is a prediction, not a finding.

## Related

* [ISO 22301 The factory’s emergency systems](../iso22301/controls.md)
* [NIS2 Building a raft](../../audits/nis2/raft.md)
* [ISO 27001 The gear depot](../../audits/iso27001/gear-depot.md)
* [Unseen University Power & Light Co. IT/OCS pentest](https://red.tymyrddin.dev/docs/power/)
* [Gap analysis](../supportive/gap-analysis.md)

