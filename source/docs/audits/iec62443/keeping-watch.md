# Keeping watch

Operating, maintaining, and catching drift.

A fortress is not defended once. Devices are replaced, firmware is updated, vendors come and go, and every change
nudges the deployed environment away from the documented one. The survey, the zone model, and the control mapping
are all models, and [models age](../../foundations/system-effectiveness/for-defence.md). Keeping watch is the
standing work of noticing the divergence before an attacker or an auditor does.

## Change is the main gate

Much of the drift arrives through legitimate change: a replaced controller inheriting a rule exception, a temporary
vendor connection that outlives the project, a firmware update that resets a hardened configuration. Change
management is therefore a security control, not an administrative one. Each change to the system under
consideration wants a corresponding update to the asset register and, where it crosses zones, to the conduit
model. A change record that does not name the zone it touches was reviewed by someone without the map open.

* Checks: Do change records reference assets and zones? Are temporary accesses given expiry dates that actually expire? Does decommissioning remove the asset from monitoring scopes and firewall rules, not just from the floor?
* Typical gaps: Vendor remote access that became permanent by inertia, spare devices swapped in without configuration baselines, rules nobody dares remove because nobody remembers their purpose.

## Watching the watchers

Monitoring itself drifts. Alert thresholds tuned for last year's traffic go quiet or go hoarse; log retention
lapses when a disk fills; the person who reviewed the anomaly alerts changes roles and the queue becomes an
archive. Periodic checks that the monitoring still covers the current asset register, and that someone still
reads what it produces, are cheaper than discovering the gap during an incident investigation.

Patching in OT runs on maintenance windows and vendor qualification rather than monthly cycles, which makes the
compensating story part of the evidence: for each deferred patch, what contains the exposure in the meantime,
and does that containment actually hold in the current zone model?

## Reassessing on purpose

Risk assessment is not a founding document. Reassessment is worth scheduling, and worth triggering early when the
environment changes shape: new equipment classes, new remote access paths, a change in what the plant produces, a
credible new adversary in the sector. When a finding from a previous cycle reappears after its corrective action
was closed, the corrective action addressed the surface condition but left an assumption intact. The question worth
asking is not why the corrective action failed but what the organisation believed about this control's operating
conditions that made the recurrence seem impossible.

## Practical gap-spotting

* Currency: the asset register, zone model, and diagrams describe the environment as deployed this quarter, not as commissioned.
* Expiry discipline: temporary access, rule exceptions, and deferred patches all carry dates, and the dates bite.
* Monitoring fitness: alert queues are read, retention holds, and coverage tracks the register.
* Reassessment triggers: defined, and at least one has fired since the last audit, because environments that never trigger one are not stable, they are unobserved.

## Output

The output of this stage is continuous rather than terminal: change records tied to the zone model, monitoring
that tracks the current environment, scheduled and triggered reassessments, and documentation that an auditor,
or an incident, would find no more than one change cycle out of date.

## Related

* [ISO 22301 After the storm](../iso22301/after-the-storm.md)
* [NIS2 Staying afloat](../../audits/nis2/afloat.md)
* [Unseen University Power & Light Co. IT/OCS pentest](https://red.tymyrddin.dev/docs/power/)

*Last updated: 4 July 2026*
