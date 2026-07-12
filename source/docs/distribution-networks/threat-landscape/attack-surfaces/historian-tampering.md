# Historian tampering

Threats to the historical record: deleting or modifying event logs, erasing incident traces, altering process values to
hide what actually happened, or corrupting the audit trail that shows who changed what and when.

A compromised historian can hide evidence of other attacks, mask operational anomalies, or create a false record of
events. But historian systems maintain edit logs and integrity checks; changes leave traces in the database audit and
the reconciliation layer.

## Event log deletion

Stedin's historian, e-terra's SQL Server historian, maintains time-series records of process values (voltages, currents,
frequencies, transformer temperatures) and system events (alarms, operator commands, device state changes). These
records are the forensic trace of what happened on Stedin's network. Incident investigation typically starts by pulling
event logs from the historian and examining the sequence of events preceding the failure. The historian's audit capabilities determine how a compromise is detected and what evidence remains.

An attacker who can delete or modify the historian records could erase evidence of their actions. For instance, if
an attacker commands a SIPROTEC or SEL protection relay to increase its current threshold (a configuration change that
disables protection), a resulting fault that should have been caught by that relay might propagate to a wider area of
the network. An incident investigation would examine the relay's settings before and after the fault, and the
historian logs of the fault itself. If the attacker has deleted the historian log of the fault (or modified it to show
false current values), the investigator might conclude that the fault was smaller than it actually was, or might not see
evidence that the relay failed to trip when it should have.

Event log deletion requires access to Stedin's historian database at a privilege level that allows modification. This is
typically the historian administrator's privilege. An attacker could achieve this by compromising the historian
application server (through remote code execution in the historian software itself), or by obtaining database
credentials and connecting directly to the historian database. The historian system typically runs on a dedicated
server in Stedin's OT network, with restricted access.

## Process value tampering

Process values are the measurements that come from field devices: a voltage at a Stedin substation, a current through a
feeder, a temperature in a transformer. These values are collected by RTUs, sent to e-terracontrol SCADA
through IEC 60870-5-104, and logged in the historian. An attacker who can modify historical process values could
misrepresent what Stedin's network state was at a particular time.

A common use of tampering is to hide evidence of a fault condition. If an attacker causes a transient fault (a brief
over-voltage or over-current condition) as cover for an attack, they might delete or modify Stedin's historian records
to erase evidence that the fault occurred at all. An investigator looking at the historian data would see normal
conditions throughout, and would not recognise that there was a window when the network was stressed.
[What falsified data looks like](../../observable-semantics/measurements-and-data-records/historian-patterns.md) is the pattern such an investigation has to recognise.

More subtly, an attacker could modify process values to create a false narrative. For instance, if a fault occurred and
the SIPROTEC or SEL relay that should have protected the zone did not trip (because the relay settings were corrupted by
the attacker), the historian would record the fault current as it actually occurred. But if the attacker modifies
Stedin's historian to show a lower current (below the relay's threshold), it would appear that the relay was correctly
set and should have tripped, but the fault was too small. This would hide evidence that the relay settings were changed.

Modifying historical data requires access to the historian's archive, through its API or direct database
access. The historian maintains edit logs that record modifications to archived data, but those logs can also be deleted if the
attacker has sufficient privilege.

## Audit trail corruption

The historian maintains an audit trail that records who accessed data, when, and what they did. If a value was edited,
the audit trail records who edited it, when, what the old value was, and what the new value is. This audit trail is
meant to provide accountability and to detect unauthorised changes.

An attacker who can modify the audit trail can delete evidence of tampering. If they edit a historical value, and then
delete the audit trail entry that records the edit, it will appear that the value was never changed. The operator's
investigation tools, which typically rely on the audit trail to detect modifications, will not show the edit.

The audit trail is typically stored in the same database system as the historical data, so compromising one means
compromising both. But some historian implementations maintain a separate, write-once log of changes, which is harder to
modify. Even if such a log exists, an attacker with sufficient database privilege might be able to truncate the log or
bypass the write-once protection.

## Value edit erasure

In addition to Stedin's historian's normal process-value storage, historians often have an "edit database" that records
values that have been manually edited by operators. This is separate from the real-time values collected from
field devices. Stedin's operators might edit a value if they know it is incorrect (sensor malfunction, known bad
reading) and need to replace it with a corrected value. The edit database maintains a record of the original value, the
edited value, who edited it, and when.

An attacker who can delete entries from the edit database would erase evidence that values were ever corrected. If
an operator discovered a corrupted value and edited it, and the attacker then deletes the edit record, it would
appear that the value was never edited. An investigator examining Stedin's historian would see only the corrected value,
and might not recognise that the original value was bad.

More dangerously, an attacker could edit values themselves and then delete the edit records, leaving the false values in
the historian. An investigator would see the false values as part of the normal historical record, with no
indication that they were modified.

## Observable traces

What historian tampering looks like in database audit logs and cross-system value consistency checks.

Tampering with Stedin's historian data leaves several traces. First, the historian's archive logs edits to stored values:
the editing user, the timestamp, and the old and new value. An edited value with no matching audit entry, or an audit
trail with gaps, is the on-system signature. The live current-value cache holds only current values, so it is no help in reconstructing
an altered past.

Second, historian records are often integrated with other system logs. If an RTU sent a particular value to
e-terracontrol SCADA at a particular time, that value should appear in e-terracontrol's event log at approximately the
same time it appears in the historian. If an investigator finds a discrepancy (the event log shows a value that
does not match the historian record, or vice versa), that can indicate tampering.

Third, missing audit trail entries are themselves evidence. If Stedin's historian's audit logs suddenly have a gap (
records 1000 to 2000 are present, but records 2001 to 2050 are missing), that suggests the audit log was edited.
Similarly, if the audit trail should show an edit to a particular value but does not, that is evidence that the audit
trail was tampered with.

Fourth, process-value inconsistency with physical reality provides evidence. If Stedin's historian shows that a voltage
was steady at 240V throughout the night, but a SIPROTEC or SEL protection relay at that location has an event log
showing it measured 280V (an over-voltage condition) at that same time, the discrepancy indicates that one of the
records is false. A sophisticated attacker would need to corrupt all related records to maintain consistency, which is
difficult and leaves a larger forensic footprint.

Fifth, timestamps can reveal tampering. Historian databases typically record the timestamp when a value was inserted or
edited. If an investigator finds many edits that occurred at the same instant (to the millisecond), or edits that
occurred at times when the historian system was not expected to be modified, that can indicate automated tampering
rather than manual operator correction.

The difficulty with detecting historian tampering is that it requires proactive forensic investigation, not passive
monitoring. An operator who simply queries the historian for recent values will see only the current state of the
database, not evidence that it was modified. Detection requires comparing Stedin's historian against other independent
records (relay event logs from SIPROTEC and SEL relays, e-terracontrol SCADA transaction logs, real-time field device
state) and looking for discrepancies, and it requires examining the historian's own audit logs for evidence of
modifications. Knowing [how historians are used to reconstruct network events](../../operating-context/evidence-and-incident-traces/incident-analysis-and-forensics.md) helps defenders
recognise when those data have been tampered with. A historian compromise that is well-executed (modifying values,
editing audit logs, maintaining reconciliation between subsystems) might not be detected unless the investigator is
specifically looking for it.

*Last updated: 11 July 2026*
