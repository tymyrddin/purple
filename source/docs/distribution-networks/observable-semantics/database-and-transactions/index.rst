Database and transactions
============================================

The enterprise and asset databases, IBM Maximo and the Smallworld model, record every insert, update and delete with
who, what and when, and with the old and new values, which makes them the business backstory behind an operational
change: the work order that authorised it, the approval, the documentation. The transactions that stand out are those
that do not fit a legitimate business process, a change made outside the application interface, a work order marked
complete against an asset that shows no change, a settings-baseline update with no accompanying change order.

.. toctree::
   :maxdepth: 1

   database-transaction-logs

The database's forensic role is to close the loop between authorisation and effect. The telling discrepancies are
a database change with no corresponding operational change, or an operational change with no database record, either
of which marks work done off the auditable path. Referential integrity and retention are the quieter tells: orphaned
records, a work order pointing at an asset that was deleted, betray a partial tampering, and a retention policy
suddenly cut from ninety days to one at a time when unauthorised work is suspected is an attempt to erase the
backstory before it can be read.
