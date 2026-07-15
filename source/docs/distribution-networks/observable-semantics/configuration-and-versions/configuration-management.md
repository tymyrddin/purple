# Configuration management

Configuration in the portrait lives in four places: the e-terra SCADA, the GE Smallworld GIS, the protection-relay
project files, and the RTUs. Changes to any of them run through change control and leave an audit trail, and every
deployed configuration has an approved baseline behind it, so an unauthorised change shows as a divergence from that
baseline with no change order to explain it.

## SCADA configuration versioning and baselines

The e-terra SCADA stores configuration data: the network model (devices, topology, dependencies), alarm thresholds,
load-shedding logic, under-frequency protection settings, and operator interface definitions. This configuration is
stored in a database and is typically backed up. Configuration changes go through a change-control process: an
engineer submits a change request, it is reviewed and approved, the engineer applies the change at a scheduled time, and
the change is documented.

Normal configuration management means the current SCADA configuration matches the approved baseline, the change was
documented, and the change history is traceable. Version control (Git or similar) for SCADA
configuration ties each version to a date, a user ID, and a change description. A complete process keeps the
approved baseline and the version actually deployed side by side, the difference between them, and the trail of who
signed off that difference and when.

An unauthorised configuration change is a divergence between the approved baseline and the current
configuration, with no corresponding approval or change order. If the SCADA's configuration history shows a change was
made at a specific time, but the change-control log shows no approval for that change at that time, the change is
unauthorised. A change that quietly weakens protection, and so lowers network resilience for no visible operational reason, reads as
the most suspicious of all.

## Smallworld GIS model consistency

The GE Smallworld GIS maintains the network model: the location and interconnections of all substations, feeders,
switchpoints, and transformers. This model is the canonical source for what the physical network is meant to be. The SCADA's
network model is derived from Smallworld: the network structure in e-terra's configuration is built from the GIS model
to ensure alignment.

A consistent model and the field agree both ways: every device in the GIS is out there in the network, and every
physical device has its GIS entry, with the topology matching. An inconsistency is either a physical change the model
never caught up with or a corrupted model, a phantom device in the GIS that is not in the field, or a real one missing
from it, and either way the model no longer describes the network the operator acts on.

Smallworld changes go through change control: a work order authorises a model change (adding a new substation, removing
a decommissioned device, changing a connection). The change is made in the GIS database by an authorised engineer, and
the change is timestamped, user-ID'd, and logged. After a change, the model can be exported to the SCADA and deployed
during a change window. A GIS model change without a corresponding work order stands out. A change made at an unusual
hour (03:00) without emergency justification is anomalous.

## Engineering workstation project files

Configuration reaches the devices from project files held on the [engineering
workstations](../engineering-and-change/engineering-workstation-artifacts.md), where the version-control history, the
file timestamps and the commit trail are the record of who proposed what and when. What is particular to configuration
management is the deployment: a change pushed to a relay with no commit behind it, or a file edited and loaded without
ever being version-controlled, is a change with no authorising trail, a gap the device-side deployment logs catch too.

## Configuration deployment and audit logs

When a configuration change is approved, it is deployed from the engineering tools to the actual devices. This
deployment leaves traces. The engineering tool logs when it connects to a device, when it uploads a configuration, the
timestamp, and the user ID. Network captures show the configuration data being transmitted. The device itself logs when
its configuration was changed, sometimes including details about the old and new configuration.

A legitimate deployment leaves a trail that joins up end to end: an approved change-control form, the engineer
connecting to the device at a scheduled time, the tool reporting the upload, and the device's own log confirming the
new configuration. Every step is documented, and each hands to the next.

An unauthorised deployment would lack documentation. An engineer connects to a relay at 03:00 and uploads a
configuration, but no change-control form exists and no maintenance window was scheduled. The deployment might succeed
technically (the relay's logs show it received new configuration), but there is no authorisation or explanation. If
multiple unauthorised deployments occur to the same relay, that pattern suggests deliberate targeted compromise.

The challenge for investigators is distinguishing legitimate maintenance deployments from unauthorised ones in
historical logs. An emergency maintenance (a relay needs reconfiguring immediately to work around a fault) might be
deployed without full advance documentation, approved verbally rather than via a paper form. Investigators separate
genuinely exceptional circumstances (documented in incident logs, with an emergency work order, and an after-action
review) from unauthorised activity (no documentation, no emergency context, and no explanation).

## Backup and master configurations

A best practice is to maintain multiple independent baselines. The primary baseline is the approved configuration on the
engineering workstation. A backup baseline might be stored on a different system (a configuration repository or a second
workstation). A master configuration is maintained by the vendor as a reference. By comparing multiple independent
baselines against the deployed configuration, an investigator can gain confidence that the baseline itself has not been
tampered with.

Three independent baselines catch what one cannot. Set the deployed relay against all three: match the primary and
backup but not the vendor's master, and the baseline was moved; primary and backup that disagree, and one of them was;
a relay that differs from all three where they agree, and it was changed after they were set. A tamper has to rewrite
every copy to stay hidden, and the copy it misses is the one that tells.

This practice is particularly important for critical relays (protection relays on the main
transmission-distribution interface, relays protecting large urban loads). The cost of maintaining multiple baselines is
modest, and the forensic benefit is significant. A relay with multiple independent baselines that all agree is
more likely to be trustworthy; a relay with a single baseline is more exposed.

Models and baselines trail the field as a matter of course, so a divergence is common and mostly benign; the telling
one has no change order, no window and no update pending behind it.

*Last updated: 13 July 2026*
