# System portrait

A plausible distribution network operator. The architecture is grounded in real-world
OSINT research into how operational utilities actually work: the systems, the vendors, the procedures, the staffing
realities, and the constraints that shape what evidence is created during normal operation. It is operationally
coherent, architecturally realistic, and emits the observable evidence patterns a working operator would.

## Scale and scope

A regional distribution operator serves a few million connections across electricity and gas networks. The estate
includes roughly 25,000 to 30,000 distribution substations converting medium to low voltage, tens of thousands of
kilometres of cable, hundreds of thousands of meters, and secondary stations housing protection and control equipment.

The operator runs a network operations centre where electricity and gas networks are monitored and switched in real
time.
High-voltage operations typically involve joint ventures with transmission operators. Metering communication runs
through separate carrier networks, often shared with other operators.

Regulation constrains the operator across multiple dimensions: economic regulation (tariffs, allowed return), safety
(gas protection systems, electrical standards), cyber resilience (NIS2-equivalent compliance), and reliability metrics.
Requirements shift frequently, driven by decarbonisation, electrification, and evolving security rules.

## Control room architecture

The control layer is typically a [SCADA suite](system-composition/vendor-platform.md) (e-terra) integrated with a
distribution
management system (DMS) coupled to a geographic information system (GIS) for network topology. An EMS layer synchronises
with the SCADA database on a periodic schedule (often weekly). An event and alarm journal captures operator actions,
acknowledgements, and switching commands.

The historian layer records process values, edits, and metadata (who changed what, when, why). Authentication runs
through centralised identity management (LDAP, Active Directory, or equivalent).

Switching authority is role-based and gated
by [formal authorisation procedures](operations-and-cadence/operational-procedures-and-change.md). Work is authorised
through documented
work plans and switching plans, created digitally before execution. These procedures are tightly constrained and
auditable.

## Field devices and protection

[Protection relays](system-composition/vendor-platform.md) (typically Siemens SIPROTEC, Schweitzer Engineering
Laboratories, or similar) deployed across
substations are configured through vendor engineering tools running on workstations. Relay commissioning produces
as-found-and-as-left records documenting the state before and after maintenance.

Remote terminal units and intelligent electronic devices in medium-voltage stations communicate using standard protocols
(IEC 60870-5-104, IEC 61850). RTUs execute switching commands and report state and measurements.
Firmware versions are tracked and compared against baselines during maintenance.

## Network model and asset management

A [geographic information system (GIS)](system-composition/vendor-platform.md) with network documentation tools holds
the as-built model, feeding an asset
register. An [asset management system](system-composition/vendor-platform.md) (typically IBM Maximo or equivalent) runs
the maintenance workflow, tracking work
orders with audit trails showing who changed what and when. The architecture is API-first and loosely coupled,
designed to wrap rather than replace legacy systems.

    SYSTEM ARCHITECTURE: Distribution Operator Estate
    ──────────────────────────────────────────────────

    ENTERPRISE LAYER (IT operations, business systems)
    ──────────────────────────────────────────────────
    
    ┌─────────────────────────────────────────────────────────────┐
    │ SAP ERP (Finance, Procurement, HCM) | Azure (Cloud apps)    │
    │ Email, identity management (AD/Kerberos, LDAP)              │
    │ Remote access, VPN                                          │
    └──────────────────────────┬──────────────────────────────────┘
                               │ Internet
                               │ (patching, remote support)


    CONTROL LAYER (SCADA, monitoring, supervision)
    ───────────────────────────────────────────────

    ┌──────────────────────────────────────────────────────────────────┐
    │ e-terracontrol SCADA/EMS/DMS (real-time network operations)      │
    │ • Centralised SCADA database                                     │
    │ • Event and alarm journal                                        │
    │ • Access control: role-based, formal authorisation               │
    │ ┌────────────────────────────────────────────────────────────┐   │
    │ │ API connections to:                                        │   │
    │ │  • Smallworld GIS (network topology)                       │   │
    │ │  • SQL Server historian (process values, audit trails)     │   │
    │ │  • IBM Maximo (asset management, work orders)              │   │
    │ │  • Central authentication (LDAP/Active Directory)          │   │
    │ └────────────────────────────────────────────────────────────┘   │
    └───────────┬──────────────────────────────────────────────┬───────┘
                │ IEC 60870-5-104, IEC 61850                   │
                │                                              │


    NETWORK MODEL & ASSET MANAGEMENT LAYER
    ───────────────────────────────────────

    ┌───────────────────────────┐      ┌──────────────────────────┐
    │ Smallworld GIS            │      │ IBM Maximo               │
    │ • Network topology        │      │ • Maintenance workflows  │
    │ • Feeder, zone, substation│      │ • Work order tracking    │
    │ • Asset register          │      │ • Audit trails (who,when)│
    │ • Asset liabilities       │      │ • Contractor assignments │
    │ (used by e-terracontrol)  │      │ • Service-level metrics  │
    └───────────────────────────┘      └──────────────────────────┘


    FIELD OPERATIONS LAYER (Protection, measurement, control)
    ───────────────────────────────────────────────────────────

    Medium-voltage substations:
    ┌──────────────────────────────────────────────────┐
    │ Smart Grid Terminals (RTUs) + Protection Relays  │
    │ • SIPROTEC 5 (Siemens)                           │
    │ • SEL-451 (Schweitzer Engineering Labs)          │
    │ • Relay maker inferred, not confirmed            │
    │ • Intelligent electronic devices (IEDs)          │
    │ • Communication: IEC 60870-5-104, IEC 61850      │
    │ • Configured via DIGSI 5 or AcSELerator          │
    │ • Emit: event logs, sequence-of-events           │
    └──────────────────┬───────────────────────────────┘
                       │ Switching commands
                       │ State polling
                       ↓

    Network elements (physical):
    ┌───────────────────────────────────────────┐
    │ Switchpoints, breakers, fuses             │
    │ Current/voltage transformers              │
    │ Power equipment (transformers, cables)    │
    │ Physical field state (energised/de-ener-) │
    └───────────────────────────────────────────┘


    METERING LAYER (Customer consumption, billing)
    ───────────────────────────────────────────────

    ┌────────────────────────────────────────────┐
    │ Smart Meters (deployed at consumers)       │
    │ • Landis+Gyr, Iskraemeco, Kaifa, Sagemcom  │
    │ • Communicate: CDMA network                │
    │ • Operator: Utility Connect (separate)     │
    │ • Metering backend (encrypted data)        │
    │ • Billing integration (SAP interface)      │
    └────────────────────────────────────────────┘


    HISTORIAN LAYER (Records, audit, forensics)
    ─────────────────────────────────────────────

    ┌─────────────────────────────────────────────────────────┐
    │ e-terra SQL Server historian                            │
    │ • Time-series data (voltage, current, frequency, temp)  │
    │ • Edit database (operator manual corrections)           │
    │ • Audit trail (who edited what, when)                   │
    │ • Event and message log (system and edit events)        │
    └─────────────────────────────────────────────────────────┘


    ENGINEERING & MAINTENANCE WORKSTATIONS (Field technician tools)
    ────────────────────────────────────────────────────────────────

    ┌────────────────────────────────────────────────────┐
    │ Contractor/technician workstations                 │
    │ • DIGSI 5 (SIPROTEC settings management)           │
    │ • AcSELerator QuickSet (SEL settings)              │
    │ • e-terracontrol client (remote SCADA access)      │
    │ • GIS viewer (Smallworld client)                   │
    │ • Maximo client (work order updates)               │
    │ • Configuration databases                          │
    │ • Baseline settings (offline copy for comparison)  │
    └────────────────────────────────────────────────────┘


    EVIDENCE PROPAGATION
    ────────────────────

    Normal operation:
      RTU measures voltage → sends to e-terracontrol → logged in historian
      Operator commands switchpoint → RTU executes → event logged in relay
      Relay setting change → documented in work order → recorded in Maximo audit trail

    Compromise entry points (where attackers can intercept):
      • Firmware supply chain (vendor → engineering workstation)
      • Engineering workstation (DIGSI, AcSELerator, e-terracontrol clients)
      • Communications (IEC 60870-5-104 frames between SCADA and field)
      • Database access (historian, Maximo, GIS configuration)
      • Historian tampering (deleting/modifying records of the attack)
      • Contractor credentials (access to multiple systems)

    Evidence leaves traces at each layer because they are loosely coupled:
      A relay settings change shows up in: relay event log, engineering tool logs,
      Maximo audit trail, baseline comparison, historian event journal

## Enterprise systems

Financial and procurement operations run through an ERP system (e.g., SAP S/4HANA or equivalent). Supplier relationships
and tendering are managed through procurement systems. Business applications have migrated toward cloud platforms (e.g.,
Microsoft Azure or equivalent), though some on-premises legacy typically remains.

## Metering

[Smart meters](system-composition/vendor-platform.md) from multiple vendors (Landis+Gyr, Iskraemeco, Kaifa, Sagemcom, or
equivalent) are deployed across the
network. Metering data flows through wireless machine-to-machine networks (e.g., CDMA or LTE-M), often shared with
other operators.

## Staffing and contractor reliance

A typical operator employs a few thousand people: internal staff performing operations, engineering, maintenance, and
administration, plus external contractors (roughly 15 to 20 per cent of the workforce) supplementing field work.
Beyond
this, [contractors perform significant physical build and maintenance work](operations-and-cadence/contractor-management.md)
under long-term framework contracts
(6-12 year terms, assigned to geographic areas).

Around 200-400 technicians keep installations in condition. Most operators
face [projected labour shortages](staffing-and-capability/staffing-realities.md) as skilled
workers retire, driving heavier reliance on contractor hiring and task deskilling.

[Contractor access is managed](operations-and-cadence/contractor-management.md) through credentials and formal
appointments recorded in access-management systems.
Personnel screening (background checks, safety training, certifications) is mandatory. Physical access is controlled
through key policies: managers can revoke keys without notice, and authorised staff lists are exchanged regularly.

## Change management and maintenance

[Maintenance follows a published schedule.](operations-and-cadence/operational-procedures-and-change.md) Planned outages
are announced days in advance to customers. Contractors
operating under framework orders submit weekly work plans to a central coordination desk. Management approves what
categories of work each contractor can do annually. Emergency work is handled through a duty roster; a responsible
manager must respond within specified time windows (typically one hour).

Change cadence is nested: daily operations through the control centre and coordination desk, weekly contractor planning,
quarterly IT release planning, annual investment cycles, multi-year ACM/regulatory cycles, and multi-decade
infrastructure masterplans.

Maintenance is transitioning from time-based to risk-and-condition-based, supported by asset-management dashboards and
field telemetry. Protection relay testing generates test reports documenting settings, results, pass/fail status, and
technician identification.

## Operational constraints

Four structural constraints shape the estate. [Capital](asset-base-and-constraints/capital-constraints.md) is regulated
and set years ahead, so imperfect-but-working plant stays in service rather than consuming slow-recovering capital.
[Legacy infrastructure](asset-base-and-constraints/legacy-constraints.md) reaches end of life in bulk, with structural
spare-part shortages and multi-year procurement, leaving a hybrid estate of decades-old plant under a thin retrofitted
digital layer. A [labour shortage](staffing-and-capability/staffing-realities.md) is structural: a large share of the
team is new, certification cannot be bought in, and out-of-hours cover is thin. And [regulatory
pressure](regulatory-and-governance/regulatory.md) pulls several ways at once, congestion rationing new connections,
decarbonisation driving peak demand past network build, and cyber rules hardening under NIS2.

## What this means for evidence

These constraints decide what evidence exists. [Contractors](operations-and-cadence/contractor-management.md) do most of
the hands-on work, so they generate most of the operational record, and the procedures around them are tightly gated and
so auditable: appointments, work authorisations, as-found-and-as-left records, work orders, switching plans. The
[vendor systems](system-composition/vendor-platform.md) emit detailed records by design, alarms and events,
sequence-of-events, asset-change history, historian edits. The catch runs through all of it: legitimate work leaves the
same trace an intrusion would, so the question the evidence answers is not whether something changed but whether it was
authorised and in scope. Access concentrates in a few people and credentials, which is why a compromised contractor
login reads as legitimate to the logs.

The system is operationally tight: safety-critical interlocks prevent certain simultaneous actions, maintenance windows
are published weeks in advance, staffing is stretched thin, and every maintenance activity leaves a paper trail in
multiple systems. It is not air-gapped: field devices reach into the network from the field, metering data flows
wireless, the control system couples with the GIS over APIs. It is not modern: the oldest plant predates digital
instrumentation, and the architecture wraps rather than replaces legacy.

This is a complex, constrained, operationally real system running under pressure. Threats that sound elegant on paper
may be impossible in practice because the configuration violates a safety interlock, the maintenance window does not
exist, or the staffing to execute it does not exist. Evidence that looks like compromise might be mismanagement under
pressure. Evidence that looks innocent might be the signature of someone who knows the system well enough to hide
inside normal operation.

*Last updated: 12 July 2026*
