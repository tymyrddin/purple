# Historian tampering

Tampering with the historical record takes a few forms: deleting or modifying event logs, erasing incident traces, altering process 
values to hide what actually happened, or corrupting the audit trail that shows who changed what and when.

A compromised historian can hide evidence of other attacks, mask operational anomalies, or create a false record of
events. But historian systems maintain edit logs and integrity checks; changes leave traces in the database audit and
the reconciliation layer.

## Event log deletion

The portrait's historian, e-terra's SQL Server historian, maintains time-series records of process values (voltages, 
currents, frequencies, transformer temperatures) and system events (alarms, operator commands, device state changes). 
These records are the forensic trace of what happened on the network. Incident investigation typically starts by 
pulling event logs from the historian and examining the sequence of events preceding the failure. The historian's 
audit capabilities determine how a compromise is detected and what evidence remains.

An attacker who can delete or modify the historian records could erase evidence of their actions. For instance, if
an attacker commands a SIPROTEC or SEL protection relay to increase its current threshold (a configuration change that
disables protection), a resulting fault that should have been caught by that relay might propagate to a wider area of
the network. An incident investigation would examine the relay's settings before and after the fault, and the
historian logs of the fault itself. If the attacker has deleted the historian log of the fault (or modified it to show
false current values), the investigator might conclude that the fault was smaller than it actually was, or might not see
evidence that the relay failed to trip when it should have.

Event log deletion requires access to the historian database at a privilege level that allows modification. This is
the historian administrator's privilege. An attacker could achieve this by compromising the historian
application server (through remote code execution in the historian software itself), or by obtaining database
credentials and connecting directly to the historian database. The historian system usually runs on a dedicated
server in the OT network, with restricted access.

## Process value tampering

Process values are the measurements that come from field devices: a voltage at a substation, a current through a
feeder, a temperature in a transformer. These values are collected by RTUs, sent to e-terracontrol SCADA
through IEC 60870-5-104, and logged in the historian. Modifying historical process values lets an attacker
misrepresent the network's state at a chosen time.

A common use of tampering is to hide evidence of a fault condition. If an attacker causes a transient fault (a brief
over-voltage or over-current condition) as cover for an attack, they might delete or modify the historian records
to erase evidence that the fault occurred at all. An investigator looking at the historian data would see normal
conditions throughout, and would not recognise that there was a window when the network was stressed.
[What falsified data can look like](../../observable-semantics/measurements-and-data-records/historian-patterns.md) is the pattern such an investigation has to recognise.

More subtly, an attacker could modify process values to create a false narrative. For instance, if a fault occurred and
the SIPROTEC or SEL relay that should have protected the zone did not trip (because the relay settings were corrupted by
the attacker), the historian would record the fault current as it actually occurred. But if the attacker modifies
the historian to show a lower current (below the relay's threshold), it would appear that the relay was correctly
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
investigation tools, which rely on the audit trail to detect modifications, will not show the edit.

The audit trail is often stored in the same database system as the historical data, so compromising one means
compromising both. But some historian implementations maintain a separate, write-once log of changes, which is harder to
modify. Even if such a log exists, an attacker with sufficient database privilege might be able to truncate the log or
bypass the write-once protection.

## Value edit erasure

In addition to the historian's normal process-value storage, historians often have an "edit database" that records
values that have been manually edited by operators. This is separate from the real-time values collected from
field devices. Operators might edit a value if they know it is incorrect (sensor malfunction, known bad
reading) and need to replace it with a corrected value. The edit database maintains a record of the original value, the
edited value, who edited it, and when.

Deleting entries from the edit database erases the evidence that values were ever corrected. If
an operator discovered a corrupted value and edited it, and the attacker then deletes the edit record, it would
appear that the value was never edited. An investigator examining the historian would see only the corrected value,
and might not recognise that the original value was bad.

More dangerously, an attacker could edit values themselves and then delete the edit records, leaving the false values in
the historian. An investigator would see the false values as part of the normal historical record, with no
indication that they were modified.

## Observable traces

Tampering with the historian rarely surfaces in a passive query. The tells are an edited value with no matching entry
in the [archive's edit log](../../observable-semantics/measurements-and-data-records/historian-patterns.md), or a gap in
that log; a stored value that no longer agrees with the RTU's log or a relay's COMTRADE for the same instant; a curve
too smooth to be real. A well-executed compromise that edits the values, trims the audit trail and keeps the subsystems
reconciled may pass unless an investigator goes looking.

*Last updated: 13 July 2026*
