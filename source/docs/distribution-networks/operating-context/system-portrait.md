# System portrait

Nothing here is invented: the systems, vendors, procedures,
staffing and constraints are drawn from the OSINT record and assembled into a single estate that is coherent to run and
emits the evidence a working operator would.

## Scale and scope

The operator serves a few million connections across electricity and gas. The estate runs to
[tens of thousands of distribution substations](asset-base-and-constraints/asset-classes.md) converting medium to low
voltage, tens of thousands of kilometres of cable, and a few million meters. A network operations centre monitors and switches both networks in real time.
High-voltage operation is shared with the transmission operator through a joint venture, and metering traffic runs over
a separate carrier network shared with other operators.

Regulation presses from several sides at once: economic, through tariffs and allowed return; safety, through gas
protection and electrical standards; cyber resilience under NIS2; and reliability targets. The requirements shift often,
pushed by decarbonisation, electrification and tightening security rules.

## Control room

The control layer is an [e-terra SCADA suite](system-composition/vendor-platform.md) with a distribution-management
system, coupled to a geographic information system for network topology. An event and alarm journal records operator
actions, acknowledgements and switching commands; the historian keeps process values, edits, and the metadata of who
changed what and when. Authentication runs through a central directory. Switching authority is role-based and gated by
[formal authorisation](operations-and-cadence/operational-procedures-and-change.md): work moves through documented work
plans and switching plans, drawn up digitally before anything is touched, tightly constrained and auditable.

## Field devices and protection

The [protection relays](system-composition/vendor-platform.md), inferred as Siemens SIPROTEC and Schweitzer Engineering
Laboratories but not independently confirmed, sit across the substations, configured through vendor engineering tools on
workstations. Relay commissioning leaves as-found-and-as-left records of the state before and after each visit. Remote
terminal units and intelligent electronic devices in the medium-voltage stations speak IEC 60870-5-104 and IEC 61850,
executing switching commands and reporting state and measurement. Firmware versions are tracked against baselines at
maintenance.

## Network model and asset management

A [Smallworld GIS](system-composition/vendor-platform.md) holds the as-built model and feeds the asset register; an
[IBM Maximo](system-composition/vendor-platform.md) asset-management system runs the maintenance workflow, tracking work
orders with audit trails of who changed what and when. The architecture is API-first and loosely coupled, built to wrap
the legacy estate rather than replace it. That loose coupling is what leaves a change recorded in more than one place: a
single relay setting change surfaces in the relay's own event log, the engineering-tool log, the Maximo audit trail, the
offline baseline it no longer matches, and the historian.

## Enterprise systems and metering

Finance and procurement run through an [SAP ERP](system-composition/vendor-platform.md), with business applications
largely migrated to cloud while some on-premises legacy remains. [Smart meters](system-composition/vendor-platform.md)
from several vendors (Landis+Gyr, Iskraemeco, Kaifa, Sagemcom) report over a wireless machine-to-machine network
(Utility Connect) shared with other operators, feeding a metering back-end that hands billing to the SAP interface.

## Staffing and contractors

The operator employs a few thousand people across operations, engineering, maintenance and administration, with
hired-in staff making up roughly a fifth of the direct headcount; beyond that, much of the physical build and
maintenance runs through [framework contractors](operations-and-cadence/contractor-management.md) assigned to geographic
areas. A core of specialist technicians keeps the installed base in condition. A [labour shortage](staffing-and-capability/staffing-realities.md) runs
underneath: skilled workers are retiring, certification cannot be bought in at short notice, and out-of-hours cover is
thin, which deepens the reliance on contractors. Contractor access runs through credentials and formal appointments in
the access-management systems; screening is required, and physical access is governed by a key policy that lets managers
revoke keys without notice.

## Cadence and constraints

Change is nested by tempo: daily operations through the control centre and coordination desk, weekly contractor
planning, quarterly IT releases, annual investment cycles, multi-year regulatory rounds, and multi-decade infrastructure
masterplans. Maintenance is moving from time-based to risk-and-condition-based, and relay testing leaves reports of
settings, results, pass or fail, and the technician's identity.

Four structural constraints shape what the estate can do and, with it, what evidence exists.
[Capital](asset-base-and-constraints/capital-constraints.md) is regulated and set years ahead, so imperfect-but-working
plant stays in service rather than consuming slow-recovering money.
[Legacy plant](asset-base-and-constraints/legacy-constraints.md) reaches end of life in bulk against spare-part
shortages and multi-year procurement, leaving a hybrid estate of decades-old equipment under a thin retrofitted digital
layer. The labour shortage is structural rather than cyclical. And
[regulation](regulatory-and-governance/regulatory.md) pulls several ways at once: congestion rationing new connections,
decarbonisation driving peak demand past the pace of network build, and cyber rules hardening under NIS2.

## The record the estate keeps

These constraints decide what the record contains. [Contractors](operations-and-cadence/contractor-management.md) do
most of the hands-on work and so generate most of the operational record, and because the procedures around them are
tightly gated they are also auditable: appointments, work authorisations, as-found-and-as-left records, work orders,
switching plans. The [vendor systems](system-composition/vendor-platform.md) emit detailed records by design. The catch
runs through all of it: legitimate work leaves the same trace an intrusion would, so the question the evidence answers is
not whether something changed but whether the change was authorised and in scope. Access concentrates in a few people
and a few credentials, which is why a compromised contractor login reads as legitimate to the logs.

The estate is operationally tight, safety interlocks bar certain simultaneous actions and every activity leaves a paper
trail across several systems, but it is neither air-gapped nor modern: field devices reach in from the field, metering
flows wirelessly, the control system couples to the GIS over APIs, and the oldest plant predates digital
instrumentation. So a threat that reads elegantly on paper may be impossible in practice because the configuration
violates an interlock, the maintenance window does not exist, or the staffing to run it does not exist. Evidence that
looks like compromise may be mismanagement under pressure; evidence that looks innocent may be someone who knows the
estate well enough to hide inside normal operation.

*Last updated: 13 July 2026*
