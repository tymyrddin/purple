# Factory floor under inspection

All controllers, sensors, and networks are deployed. This is about spotting blind spots and confirming every 
asset is covered, accounted for, and properly controlled. Treat this as a practical lens for shoring up 
defences post‑deployment.

## Critical asset types

* Industrial controllers: PLCs, DCS, RTUs. Confirm configuration, firmware, and lifecycle documentation.
* Sensors and actuators: Verify mapping to controllers, inclusion in maintenance records, and segmentation by zones.
* SCADA servers and HMIs: Ensure patching, access control, and logging are documented.
* Industrial networks: Confirm segmentation, VLANs, and firewall rules. Compare to asset register.
* Workstations / engineering laptops: Check authorised users, role-based access, and secure configuration. Control removable media.
* Embedded field devices/IoT equipment: Document identity, firmware, and monitoring.
* Physical infrastructure: Power supplies, racks, enclosures, environmental sensors. Verify redundancy, access, and monitoring coverage.

## Gap‑spotting checks

1. Asset register vs. network diagram: Any device that exists in one but not the other is a gap.
2. Lifecycle documentation: Installation, updates, maintenance, and decommissioning must all be recorded. Missing steps are findings.
3. Ownership clarity: Each asset must have a responsible operator or custodian. Ambiguity is a red flag.
4. Zone mapping: Critical devices must reside in defined security zones consistent with segmentation requirements. Misaligned assets are gaps.

*Use this page as a checklist for post‑work inspection: if it is missing, misaligned, or undocumented, it is something to fix before an auditor sees it.*

Asset documentation is a model of the ICS environment at a point in time. 
[The model ages](../../foundations/system-effectiveness/for-defence.md): devices are replaced, 
firmware is updated, zone assignments shift, and network segments change without the documentation following. When 
the registered state and the deployed state diverge, the gap is not primarily a record-keeping failure: it is evidence 
that the process maintaining alignment between documentation and reality has a mismatch. Controls that depend on the 
asset model (firewall rules aligned to zone assignments, monitoring scoped to registered devices, incident response 
procedures referencing current system owners) will operate against the documented reality rather than the deployed one.

## Related

* [ISO 22301 The factory’s heartbeat](../iso22301/assets.md)
* [NIS2 Understanding the river](../../audits/nis2/river.md)
* [ISO 27001 Risk tent](../../audits/iso27001/risk-tent.md)
* [Unseen University Power & Light Co. IT/OCS pentest](https://red.tymyrddin.dev/docs/power/)
* [Risk management as a process](../../workshops/risk-management.md)
* [Gap analysis](../supportive/gap-analysis.md)

