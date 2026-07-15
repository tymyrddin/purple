# Database transaction logs

The portrait's enterprise and operational databases hold the record of what the network is supposed to be. IBM Maximo
carries the asset inventory and the work-order history, GE Smallworld holds the GIS network model, and the e-terra
historian sits on a SQL Server store. Each records its own changes as transactions, an insert, an update, a delete,
stamped with who made the change, when, and the value before and after. On its own that trail says only that the record
changed. Its forensic weight comes from setting each change against an independent account of what happened in the field:
the SCADA journal, the device's own settings, the access logs, the physical asset.

## What a normal change leaves

A legitimate change moves through a business process, and the transactions follow that process step by step. A Maximo
work order is raised as an insert, approved as a status update from Submitted to Approved, assigned, worked as In
Progress, and closed, each transition its own row with a timestamp and an author. Read end to end, the rows tell one
coherent story: a work order raised, authorised, worked, and signed off, in that order, across a plausible span of time.
The baseline is that coherence. Every status the record passed through is accounted for, every change carries an actor,
and the actor held the authority the change required.

An asset attribute moves the same way. When a relay is re-rated or a transformer replaced, the asset record is updated
and both values are kept, model, serial, condition, the settings baseline. A normal attribute change sits inside a work
order, references it, and matches what the work order authorised.

## Work-order records against the operational record

A work order is a claim: work of a stated scope happened on a stated asset, at a stated time, by a named person. Each
element of that claim has an independent witness elsewhere in the estate, and the forensic move is to line the two up.

If a work order records switching on a feeder between 08:00 and 12:00, the
[SCADA journal](../control-and-command-execution/scada-observables.md) holds the commands that switching would have
produced. A work order marked Completed with no matching commands in the journal is a claim with no corroboration: the
work was not done as recorded, or it was done through a channel that left no operational trace. The reverse is as
telling, switching in the journal that no work order authorises is activity outside the documented process. And a work
order naming an asset the [access and key logs](../access-and-authorisation/access-control-and-key-management.md) show no
one attending describes a job whose worker was never on site.

The cross-check reaches what the work changed. A work order that authorises a relay setting change leaves the relay
carrying the new setting and nothing more. If the asset record shows the overcurrent threshold moved from 1200A to 1600A
but the [relay's own settings](../field-devices-and-protection/protection-relay-state.md), read back online, still hold
1200A, the database and the device disagree, and one was changed without the other. From the database side that
divergence is a transaction in the asset log with no answering change on the relay, or a relay changed with no
transaction to authorise it.

## Attribute changes with no work behind them

The signature that repays the most attention is an asset record that changed with no work to explain it. A settings
baseline updated with no work order referencing it. A transformer's condition moved from Healthy to Degraded with no
inspection behind the move, or reversed from Degraded to Healthy with no maintenance to justify it. Each is a change to
the record of what the network is, made outside the process meant to change it. The transaction log gives the edit, its
author, and its timing; the absence of a work order, an inspection, or an approval beside it is what turns an ordinary
edit into a question.

## Direct modification that bypasses the application

Changes are meant to reach the database through an application, Maximo's interface, the engineering tool, the GIS editor,
and each application leaves its own session record. A legitimate transaction therefore has two witnesses: the database's
audit row and the application log of the session that produced it. A transaction in the database log with no application
session behind it points to a direct write, someone editing the store over a database connection rather than through the
workflow the application enforces. Direct writes slip past the application's own checks,
[authorisation](../access-and-authorisation/access-control-and-key-management.md), referential validation, field
constraints, which is exactly where those checks would otherwise have left a trace. The audit row may be all that
survives, so whether the store's own auditing is comprehensive decides whether the bypass is visible at all.

## The GIS model as a record under cross-check

The Smallworld GIS holds the topology of record, which feeder connects where, which switch sits between which sections,
and its transaction log shows who edited the model and when. A topology edit is legitimate when a documented
reconfiguration accounts for it and the edit follows the physical change rather than leading it by weeks. The GIS model
set against the SCADA's live [network model](../configuration-and-versions/configuration-management.md) and the physical
substation is the stronger reading; from the database side, the signal is a model edit whose timing and author no
reconfiguration explains.

## Deletions, gaps, and retention

Transaction logs accumulate, so a gap reads the way a gap in any append-only record reads, as something removed. A run of
transactions that stops and resumes with a block missing, or an asset whose history jumps across a change that left no
transaction, is a deletion, and the deletion is the evidence. A legitimate purge is rare, authorised, and itself logged,
who removed what, when, and under what authority; missing records with no deletion record beside them is the harder case
to account for.

Retention sets how far back any of this can be read. A store that keeps detailed transaction history for ninety days and
archives for years leaves a deep record; one cut to a few days has lost the evidence of anything older. Retention is an
ordinary setting until it changes at a telling moment: a cut from ninety days to one, made while unauthorised work is in
question, removes the very transactions an investigator would reach for, and the policy change is itself a transaction
with an author and a time.

## Backups as an independent copy of the past

A backup taken before a suspected compromise is an independent copy of the database as it stood, and its use is direct:
recover the earlier state and compare it against the current one to see which records changed. The comparison holds only
if the backup sits where the same actor could not reach it; a backup on the compromised system may have been altered
along with everything else. The backup catalogue is a record in its own right, a scheduled backup absent from it, on a
date that counts, points to a copy deleted to prevent exactly that comparison.

The work-order lifecycle alone keeps a steady stream of inserts and updates flowing, so a single transaction is
unremarkable, and it is the change with no business process behind it that does not belong.

*Last updated: 13 July 2026*
