# Obtainability

A record that would tell a malicious change from its legitimate twin is worth nothing if it cannot be retrieved when the
question is asked. Under NIS2 the operator has to say, inside a day, whether an incident is suspected malicious, so the
evidence has to be not only discriminating but present and reachable inside that clock. Obtainability is that property,
and it is the one most easily assumed: the other pages describe what a record would show and quietly take for granted
that someone can get it.

## Retention sets the floor

Evidence exists only as long as its retention keeps it. The [historian](measurements-and-data-records/historian-patterns.md)
archives for years, though its value-level edit audit may not be on; [database transaction
history](database-and-transactions/database-transaction-logs.md) may run to ninety days; a field device's own log is
often a small ring buffer that overwrites itself; a [relay's COMTRADE sits in its memory until that
fills](field-devices-and-protection/disturbance-and-fault-records.md) and the oldest captures are lost. The
deep-history classes and the short-window ones differ by orders of magnitude, and a question asked after a window has
closed cannot be answered however good the record would have been. A retention policy [cut at a telling moment](database-and-transactions/database-transaction-logs.md) is itself a
signature; a retention window simply too short is a quieter failure that leaves the same hole.

## Existing is not reaching

Getting a record is not the same as its existing. The tool-mediated accounts, the SCADA journal and the historian, are
queryable from the control room. The independent records that carry the forensic weight are, by their nature, elsewhere:
an [RTU's own log](field-devices-and-protection/rtu-behaviour.md), where the device keeps one at all; a relay's
sequence-of-events and disturbance capture; a [gas station's datalogger, or the latched state of its safety
valve](gas-network-evidence/station-telemetry.md); a mechanical counter read off the plant. Reaching them means
connecting a vendor tool, pulling an archive on a schedule, or sending someone to the field. The very independence that
makes them trustworthy is what puts them out of easy reach.

## The clock does not keep office hours

Retrieval that needs a field visit, a vendor tool, a specialist, or an engineer on the [storingsdienst
rota](../operating-context/staffing-and-capability/staffing-realities.md) runs straight into the estate's thin
out-of-hours cover. The artefact that would settle the question at three in the morning may not be obtainable until the
working day, and by then the day-long clock has spent much of itself. Obtainability is not a fixed property of a record
but a function of when the question is asked and who is available to answer it.

## The determination runs on a subset

So at the moment a determination is due, the record actually in hand is a subset of the record that exists: the
retained, tool-mediated part, with the independent, physical and field-held parts possibly still out of reach. A call
made on that subset can read differently from one made on the full record days later, when the field logs have been
pulled and the counters read. This is why the honest answer can be [unknown](../evidentiary-capability.md) even where
the evidence was, in the end, perfectly good: not because the record could not discriminate, but because it could not be
got in time.

## Four properties, not one

"The record would show it" is therefore not the end of the sentence. Discriminating, independent, present, and
obtainable inside the clock are four separate properties of a piece of evidence, and evidentiary capability needs all
four at once. A record can hold the first three and fail on the fourth, and the determination fails with it.

*Last updated: 14 July 2026*
