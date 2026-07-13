# Configuration management

The portrait's configuration-management surfaces span the e-terra SCADA, the GE Smallworld GIS, protection relay project
files, and RTU configuration. Configuration changes flow through change-control processes that leave audit trails. Those audit trails distinguish
authorised configuration from unauthorised modification, and baseline configurations can be established for forensic
comparison.

## SCADA configuration versioning and baselines

The e-terra SCADA stores configuration data: the network model (devices, topology, dependencies), alarm thresholds,
load-shedding logic, under-frequency protection settings, and operator interface definitions. This configuration is
stored in a database and is typically backed up. Configuration changes go through a change-control process: an
engineer submits a change request, it is reviewed and approved, the engineer applies the change at a scheduled time, and
the change is documented.

Normal configuration management means the current SCADA configuration matches the approved baseline, the change was
documented, and the change history is traceable. Version control (Git or similar) for SCADA
configuration ties each version to a date, a user ID, and a change description. A complete
configuration-management process stores: the approved baseline version, the current deployed version, the difference
between them (what changed), and the approval trail (who approved the change and when).

An unauthorised configuration change would appear as a divergence between the approved baseline and the current
configuration, with no corresponding approval or change order. If the SCADA's configuration history shows a change was
made at a specific time, but the change-control log shows no approval for that change at that time, the change is
unauthorised. A change that quietly weakens protection, and so lowers network resilience for no visible operational reason, reads as
the most suspicious of all.

## Smallworld GIS model consistency

The GE Smallworld GIS maintains the network model: the location and interconnections of all substations, feeders,
switchpoints, and transformers. This model is the canonical source for what the physical network is meant to be. The SCADA's
network model is derived from Smallworld: the network structure in e-terra's configuration is built from the GIS model
to ensure alignment.

A consistent network model means: every device in the GIS model is accounted for in the physical network, every physical
device has a corresponding GIS model entry, and the GIS topology matches the physical topology. Inconsistencies point to
either a physical change never reflected in the model or a corrupted one: a phantom device present in the GIS but not
the field, or a real device missing from it. Either way the model no longer describes the network the operator acts on.

Smallworld changes go through change control: a work order authorises a model change (adding a new substation, removing
a decommissioned device, changing a connection). The change is made in the GIS database by an authorised engineer, and
the change is timestamped, user-ID'd, and logged. After a change, the model can be exported to the SCADA and deployed
during a change window. A GIS model change without a corresponding work order stands out. A change made at an unusual
hour (03:00) without emergency justification is anomalous.

## Engineering workstation project files

The engineering tools (DIGSI 5, AcSELerator QuickSet, SCADA engineering suites) maintain project files on the
engineering workstation. These files are the source truth for configuration changes: they are edited,
version-controlled, and then deployed to devices. The files themselves are forensically significant: file timestamps
show when they were modified, file contents show what configuration is proposed, and file version history shows how the
configuration evolved.

Normal project-file management means files are in a version-control system (Git), each change is committed with a
message, and the commits are timestamped and user-attributed. An engineer modifying a relay project would check out the
current version, edit it, test it, and commit it with a message like "Updated overcurrent threshold for relay Q12 per
work order WO-2025-05432". The commit history provides a complete audit trail of who changed what and when.

Unauthorised project-file modifications would appear as edits without version-control commits, edits by users not meant
to have access to the project, or edits that are not reflected in any deployment history. If a project file for a
critical relay is edited but never deployed (never loaded onto the actual relay), the edit is a draft. If a file is
edited and deployed without being version-controlled, the change is not documented. If multiple versions of a project
file exist (on the engineering workstation's hard drive in different directories) without clear labelling, confusion
arises about which is the authoritative version.

## Configuration deployment and audit logs

When a configuration change is approved, it is deployed from the engineering tools to the actual devices. This
deployment leaves traces. The engineering tool logs when it connects to a device, when it uploads a configuration, the
timestamp, and the user ID. Network captures show the configuration data being transmitted. The device itself logs when
its configuration was changed, sometimes including details about the old and new configuration.

A legitimate deployment shows: an approved change control form, the engineer connecting to the device at a scheduled
time, the tool uploading the configuration, logs on the engineering tool showing the upload succeeded, and logs on the
device showing the configuration was updated. The entire sequence is documented and can be traced end-to-end.

An unauthorised deployment would lack documentation. An engineer connects to a relay at 03:00 and uploads a
configuration, but no change-control form exists and no maintenance window was scheduled. The deployment might succeed
technically (the relay's logs show it received new configuration), but there is no authorisation or explanation. If
multiple unauthorised deployments occur to the same relay, that pattern suggests deliberate targeted compromise.

The challenge for investigators is distinguishing legitimate maintenance deployments from unauthorised ones in
historical logs. An emergency maintenance (a relay must be reconfigured immediately to work around a fault) might be
deployed without full advance documentation, approved verbally rather than via a paper form. Investigators separate
genuinely exceptional circumstances (documented in incident logs, with an emergency work order, and an after-action
review) from unauthorised activity (no documentation, no emergency context, and no explanation).

## Backup and master configurations

A best practice is to maintain multiple independent baselines. The primary baseline is the approved configuration on the
engineering workstation. A backup baseline might be stored on a different system (a configuration repository or a second
workstation). A master configuration is maintained by the vendor as a reference. By comparing multiple independent
baselines against the deployed configuration, an investigator can gain confidence that the baseline itself has not been
tampered with.

If the primary baseline and the deployed relay settings match, but the vendor's master configuration shows different
settings, someone modified the baseline. If the primary and backup baselines diverge, one has been modified. If all
baselines match but the deployed configuration differs from all of them, the relay was modified after the baselines were
created. Multi-level baseline comparison provides defence against attackers who compromise a single system.

This practice is particularly important for critical relays (protection relays on the main
transmission-distribution interface, relays protecting large urban loads). The cost of maintaining multiple baselines is
modest, and the forensic benefit is significant. A relay with multiple independent baselines that all agree is
more likely to be trustworthy; a relay with a single baseline is more exposed.

*Last updated: 13 July 2026*
