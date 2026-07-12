# Database transaction logs

Stedin's enterprise and operational systems maintain databases: IBM Maximo (asset management), GE Smallworld (GIS
network model), e-terra's SQL Server historian, and asset databases. These databases record transactions: inserts, updates, and
deletes of records, with audit trails showing who changed what, when, and the old and new values.

## Transaction-level audit trails

Modern database systems support transaction logging and audit trails. When a record is created, modified, or deleted,
the operation is logged: the timestamp, the user who made the change, the operation type (insert/update/delete), the
table and record ID, and crucially, the old value and new value. For example, if a Maximo maintenance record's status is
changed from "Pending" to "In Progress", the audit log shows: timestamp, user ID, table (work_order), operation (
update), field (status), old_value ("Pending"), new_value ("In Progress").

Normal database operations show a clear audit trail of legitimate business transactions. A work order is created (
insert), approved (status update), executed (status update), and closed (status update). Each transaction is timestamped
and user-attributed. The sequence of transactions forms a coherent narrative of the work order lifecycle.

Unauthorised database modifications would appear as transactions that are not part of any legitimate business process. A
transaction that updates a relay's settings baseline without a corresponding change order, or a transaction that deletes
historical records without a retention policy authorisation, would be anomalous. A transaction that is made outside 
any application interface (a direct database modification, bypassing the normal application workflow) would leave a
signature in the audit log if the database's audit trail is comprehensive.

## Maximo asset and work-order tracking

Stedin's IBM Maximo system tracks assets, maintenance work orders, and asset change history. Each asset (transformer,
switchpoint, relay) has a record with attributes (location, serial number, model, condition). Work orders describe
planned maintenance or emergency repairs. When a work order is executed, the asset's attributes can be updated (a new
transformer is installed, a relay's settings are changed).

Normal Maximo operations show work orders that follow a lifecycle: created, approved, assigned to a technician,
executed, and closed. Each step is logged. Upon completion, the work order's outcome (parts replaced, settings changed,
measurements recorded) is documented, and the asset's record is updated to reflect the new state.

Unauthorised Maximo modifications would appear as asset attribute changes with no corresponding work order, or work
orders that are marked completed without any actual work being performed (a work order is marked "Completed" but the
asset shows no changes). A work order that is marked "Closed" but is later reopened (a status transition from Closed
back to In Progress) would be unusual and would need explanation.

## Role-based database access and privilege enforcement

Database systems implement role-based access control: a database user (application user, not necessarily a person) has
permissions to perform specific operations on specific tables. Stedin's database systems enforce that only
authorised applications and users can modify sensitive records.

For example, a SCADA application user may have permission to read from the historian but not to modify historical
data. An engineer's account can update relay settings in the asset database, but only through the approved engineering
tool. A contractor's account carries read-only access to specific substation data, but not write access.

If a database operation occurs with insufficient privilege (a user with read-only access successfully performs a write),
that is evidence of either: a privilege-escalation vulnerability in the application, a misconfiguration of database
permissions, or an attacker exploiting a vulnerability to bypass access controls.

## Transaction consistency and referential integrity

Databases enforce referential integrity: relationships between tables are maintained so that a record in one table
cannot reference a non-existent record in another table. For example, a Maximo work order must reference an existing
asset. If a transaction creates a work order pointing to a non-existent asset (or an asset that is deleted before the
work order is completed), the database's referential integrity would be violated.

Detecting integrity violations requires database consistency checks. A query that looks for orphaned records (work
orders with no corresponding asset, or SCADA devices with no asset record) would identify database corruption. Such
corruption is forensic evidence of either database malfunction or unauthorised modification.

## Log retention and archival policies

Database systems typically implement log retention: old audit logs and transaction logs are archived or deleted
according to retention policies. A typical policy might retain detailed transaction logs for 90 days and archived logs
for up to 7 years.

If an investigator needs to examine database transactions from months ago, the logs must still be available. A system
with poor log retention (keeping only 30 days of logs) might have lost the evidence of old unauthorised modifications.
Conversely, a system with good long-term archival (7-year retention) provides investigators with a deep historical view.

If the retention policy is changed, that change itself is logged: who
changed the policy, when, and what the old and new retention periods were. A sudden change in log retention policy (from
the standard 90-day retention to 1-day retention) made at a time when unauthorised work is suspected would be
suspicious.

## Database backup and recovery metadata

Stedin's databases are backed up regularly for disaster recovery. The backup metadata (when each backup was taken, what
was included, the backup verification status) is also forensic evidence. If a database is suspected of having been
compromised, one approach is to recover the database from a backup taken before the suspected compromise, and then
compare the current database against the recovered version to see what was changed.

The backup process itself leaves logs: when the backup started and finished, whether it succeeded, and any errors
encountered. If a backup is missing (a backup that was due on a specific date is not in the backup
catalogue), that could indicate an attacker deliberately deleted the backup to prevent recovery and forensic comparison.

The integrity of backups is important. A backup that is old enough to predate the suspected compromise, stored in a
location where an attacker cannot access it, is a trusted source for forensic comparison. A backup that is stored on the
same system that is suspected of being compromised could itself be corrupted.

*Last updated: 12 July 2026*
