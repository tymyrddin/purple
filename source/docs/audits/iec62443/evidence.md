# The paper trail under inspection

You have assets, threats, and controls mapped. Now the question is: can you prove it? Auditing is not about theory; 
it is about evidence. Every control, every mitigation, every claimed security measure must be traceable and verifiable. 
Gaps in documentation are as fatal as gaps in configuration.

Evidence divides into two categories. Implementation evidence confirms controls are in place: logs are collected, 
configurations are documented, policies are approved, access rights are assigned. [Effectiveness evidence](../../foundations/system-effectiveness/applying-sem.md) 
confirms controls produce their intended effect under realistic conditions: a penetration test result showing that 
network segmentation held under a realistic attack path, an anomaly detection exercise confirming the signature 
fired against the expected technique, a tabletop result showing the incident response chain operated within acceptable 
time bounds. An audit drawing only on implementation evidence documents that controls exist. Effectiveness evidence 
documents that they work.

## Evidence types to check

1. Logs
   * System logs (controllers, SCADA, HMIs)
   * Network device logs (firewalls, switches, segmentation devices)
   * Security monitoring / SIEM alerts
   * Gap check: Missing logs, incomplete retention periods, or unassigned log owners are findings. Confirm logging covers all critical assets and events relevant to IEC 62443 requirements.

2. Device configurations
   * Baseline settings, secure defaults, firmware versions
   * Change history and configuration snapshots
   * Gap check: Untracked or undocumented changes, missing version records, or unmanaged devices are immediate gaps.

3. Network diagrams
   * Logical and physical topology, VLANs, zones, firewalls, and segmentation
   * Mapping of assets to zones
   * Gap check: Devices in the register not on diagrams, discrepancies between diagrams and deployed topology, or undocumented segmentation rules are findings.

4. Maintenance and lifecycle records
   * Updates, patches, preventative maintenance schedules
   * Decommissioning steps for retired assets
   * Gap check: Any lifecycle step not documented is a vulnerability. Confirm records exist for all controllers, sensors, and field devices.

5. Training and personnel documentation
   * Evidence of operator/engineer training, role awareness, incident response rehearsals
   * Gap check: Missing or outdated training records, unclear role responsibilities, or untested response procedures are findings. Attendance records are implementation evidence. Exercise performance records are [effectiveness evidence](../../foundations/system-effectiveness/applying-sem.md): a drill where operators restored a system under time pressure, a tabletop that walked through the incident response procedure with current staffing, a scenario exercise where teams had to apply a procedure they had not recently practised.

6. Policy and procedure documentation
   * Asset management, change management, access control, network management, incident response
   * Gap check: Controls claimed in IEC 62443 mappings must have supporting policies. Missing or inconsistent documentation is a finding.

## Practical gap‑spotting approach

* Walk through each control and threat: is there documented evidence for it?
* Ask: if an auditor asked for proof tomorrow, could you produce it immediately?
* Cross-check assets ↔ controls ↔ logs/records ↔ diagrams. Anything missing is a gap.
* Verify ownership: each piece of evidence should have a responsible party. Ambiguity is a finding.

*If a threat exists without documented mitigation, monitoring, or ownership, it is a gap that must be closed before anyone audits the system.*

## Related

* [ISO 22301 The resilience dossier](../iso22301/evidence.md)
* [NIS2 Reaching the far bank](../../audits/nis2/bank.md)
* [ISO 27001 Base camp check](../../audits/iso27001/base-camp-check.md)
* [Unseen University Power & Light Co. IT/OCS pentesting](https://red.tymyrddin.dev/docs/power/)
