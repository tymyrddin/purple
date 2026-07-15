# Vendor platform

![Vendor platform](/_static/images/distribution-vendor-platform.png)

Vendor families come from procurement records, careers pages, job adverts and supplier notices. Confidence varies by item, and two of the eight vendor families did not pin to a named product.

Vendor documentation is the other half of the picture, because it enumerates the observability surface: the layer that
makes incident reports possible in the first place.

## Vendor ecosystem

The families divide into a firmly-pinned enterprise-and-metering half and a harder-won operational-technology heart,
taken one at a time below.

### ERP

The clearest of the set. The core is SAP, migrated to S/4HANA, with SAP Cloud for Customer (C4C) as
the CRM, SAP Ariba and the SAP Business Network on procurement, and SAP BTP as the integration layer, all named on the [Stedin IT careers page](https://werkenbij.stedin.net/it-en-data), with further module detail on S/4HANA and C4C in Stedin adverts surfaced on a job aggregator. The IT team "Services & Markt" is named as the operator of the SAP
estate. So the administrative and market-facing digital core is a fairly pure SAP stack.

### Cloud providers

The cloud is Microsoft Azure. Stedin describes having migrated the greater part of its business applications to the
Azure Public Cloud, with a Solution Architect Cloud Transitie role and a hybrid Azure-plus-on-premises posture (Stedin job-board adverts), an emphasis consistent across its IT careers page and security vacancies. No evidence of AWS or
Google as a primary platform surfaced. Security certifications sought are Azure-oriented, which reinforces a
single-hyperscaler reading.

### GIS

GE Smallworld is paired with Lovion for network documentation and work management, feeding the asset
register (found in a Stedin Smallworld GIS Developer advert on a technical job board). The product family is the
utility-standard [GE Vernova Smallworld](https://www.gevernova.com/software/products/geospatial-network-management-smallworld-gis)
geospatial network model. The same advert notes an API-first, loosely-coupled target architecture and, usefully, an
integration from Smallworld into the SCADA system, which places GIS as the as-built network backbone.

### Asset management platforms

IBM Maximo, set up and optimised with an implementation partner, runs the maintenance chain and moves
toward risk-based maintenance with condition dashboards (from the implementation partner's case study). This sits under
the Asset Management owner function, with Smallworld and Lovion as the register side and Maximo as the
maintenance-execution side.

### Smart meter suppliers

The fullest procurement trail of the set. Historically Landis+Gyr and the Flonidan and Iskraemeco consortium won
a joint tender across Liander, Stedin, DELTA and Westland (around three million meters, with options to extend; trade-press reports, perishable),
and Stedin's installed base visibly includes Landis+Gyr units (model manuals on stedin.net) and Kaifa, including a
Stedin CDMA electricity-meter lot awarded to Shenzhen Kaifa (a tender aggregator, perishable).

For the new modular DSMR6
meter, the joint award splits the measurement sensor between Sagemcom of France and Kaifa of China, with the operators
stressing the sensor is not internet-connected and carries no switch,
per [Netbeheer Nederland](https://www.netbeheernederland.nl/artikelen/zo-werkt-het/toelichting-op-de-aanbesteding-vernieuwde-slimme-meter)
and [Liander](https://www.liander.nl/over-ons/nieuws/2025/toelichting-op-de-aanbesteding-vernieuwde-slimme-meter).
Independent cyber-audits of the meter makers run through ENCS.

The metering communication layer is the CDMA
machine-to-machine network operated by Utility Connect, the Alliander and Stedin joint venture (Utility Connect
security-officer advert via a job board).

### Network monitoring vendors

Two readings, both partial. On grid telemetry, the [2020 report](https://www.stedin.net/-/media/project/groep/files/investor-relations/financiele-jaarverslagen/jaarverslag-stedin-groep-2020.pdf) describes Stedin rolling out a new generation of smart sensors and Smart Grid Terminals into medium-voltage stations for remote measurement and switching, though without a named platform vendor.

On security monitoring, a central SOC watches IT and OT, sitting under a
Security Office of around fifteen people in the CIO/CISO
Office (a Stedin security-architect vacancy), but
the specific OT-monitoring product (the Nozomi, Claroty, Forescout family) did not surface in public sources. Not
pinned.

### SCADA, EMS and DMS

The OT heart resolves to Alstom Grid's e-terra platform (now part of GE Vernova following GE's 2015 acquisition of Alstom Grid).

The primary record is Alstom Grid's own 2012 announcement that it was selected to upgrade Stedin's distribution management system to the e-terra distribution solution, noting in passing that Alstom had also provided Stedin's existing SCADA and Energy Management System, so all three control-room layers are the same e-terra family ([Alstom Grid press release, 2012](https://www.alstom.com/press-releases-news/2012/3/alstom-grid-selected-to-upgrade-distribution-management-system-for-stedin-in-the-netherlands)).

Stedin deployed Alstom's Integrated Distribution Management System (iDMS), based on the e-terra platform, as part of its
grid modernisation programme. Alstom identifies Stedin as an iDMS customer in
its [2013/14 Alstom Registration Document (pdf)](https://www.alstom.com/sites/alstom.com/files/2014/07/01/ALSTOM%20REGISTRATION%20DOCUMENT%202013-14.pdf).

A separate Alstom corporate overview lists Stedin among customers for Alstom EMS and (i-)DMS
systems: [Alstom in the Netherlands (pdf)](https://www.alstom.com/sites/alstom.com/files/2014/06/25/Alstom_in_the_Netherlands.pdf).

A [PACW 2023 distribution-automation case study](https://www.pacw.org/full-scale-distribution-automation-roll-out-at-dutch-dso)
describes Stedin's distribution automation rollout and states that replacing the existing SCADA system was not justified
solely because of limited IEC 61850 support, indicating continued use of the incumbent SCADA platform during the
transition.

- Alstom confirms iDMS.
- Alstom confirms EMS/(i-)DMS customer relationship.
- PACW confirms continued incumbent SCADA architecture during IEC 61850 transition.

The 2012 selection predates the 2015 GE acquisition of Alstom Grid; the lack of any rip-and-replace record since then,
combined with the 2023 architecture description pointing to the same EMS-DMS-SCADA suite, indicates Stedin still runs
e-terra, now under GE Vernova branding.

The e-terracontrol product documentation enumerates the observability surface: alarm
processing and filtering, alarm acknowledgement and deletion, equipment and device tagging, event and alarm logging,
audible annunciation, and an SQL Server historian, with e-terratrust providing access control and integration with
enterprise identity services. For example LDAP, Active Directory or similar; role-based access control, LDAP, RADIUS 
and single sign-on are described across 
[GE automation security material (pdf)](https://www.gae.id/userdata/uploads/independent_pdf/GE_Advanced_Automation_Applications.pdf).

The e-terra suite has since been folded into GE Vernova's GridOS grid-software line, so no standalone e-terracontrol
product page remains public.

### Protection relay manufacturers

Inferred, not independently confirmed. The primary clue is DIGSI, Siemens' engineering tool for SIPROTEC relays, used at Stedin for protection-relay settings and commissioning, which points to SIPROTEC; DIGSI and AcSELerator QuickSet both appear as the relay-configuration tools, and relay-testing courses name the SEL-421 and Siemens 7SA8x, together suggesting a multivendor SIPROTEC-and-SEL estate. No procurement record or vendor reference names the relay maker directly, though, so it stays the least-confirmed part of the OT heart alongside the OT-monitoring tool. The relay-emission surface below assumes SIPROTEC 5 and SEL-451 on that basis.

## Evidence emission

Vendor documentation enumerates the observability surface by design. A forensic investigator reconstructs a millisecond
sequence because the relay, the SCADA and the historian emit records the vendor manuals specify in advance.

### Relay user guides

The richest per-device source. Siemens [SIPROTEC 5 documentation](https://www.siemens.com/en-us/products/siprotec/) sets out fault records, a sequence-of-events log, and dedicated fault and disturbance recorders exporting in COMTRADE, plus device self-monitoring, LED and alarm indications, with the 7KE85 and 7SE20 recorder manuals Siemens-hosted.

The [SEL-451 data sheet](https://selinc.com/api/download/7413/) is even more explicit about what the device emits: a Sequential Events Recorder driven by user-assigned SER points, as many as 66 alarm points, fault records with element response, streaming synchrophasor disturbance data, and breaker-and-battery monitoring that records electrical and mechanical operating times per operation and flags contact wear.

From the user guide alone, before touching a
substation, an investigator can list the event log, the alarm set, the state records for breakers and battery, and the
disturbance capture the relay produces.

### Engineering workstation manuals

The tools that configure those relays, DIGSI 5 for SIPROTEC and AcSELerator QuickSet for SEL, document their own
evidence: connection records, the loading of a planned configuration onto a device, and settings comparison and version handling. 
This is the configuration-history and operator-action surface: who connected, what settings group was active, what was 
written to the device and when.

### Asset management systems

This one maps directly onto Stedin's confirmed stack, IBM Maximo. IBM's own [Maximo audit-trail documentation](https://www.ibm.com/docs/en/masv-and-l/maximo-ref/cd?topic=security-audit-trails) describes attribute-level e-audit that logs who changed a record, what changed, when, and whether it was an insert, update or delete, capturing old and new values, with a separate note on [enabling e-audit](https://www.ibm.com/support/pages/tracking-changes-made-using-e-signature-and-e-audit).

Alongside it, e-signature can require authentication and a stated reason recorded in the trail, and the suite tracks login attempts, failures and status changes, plus asset and work-order status transitions, per [IBM support notes on audit tracking](https://www.ibm.com/support/pages/audit-tracking-maximo).

One documented detail has evasion-relevance in the other direction: standard e-audit records the change without 
prompting the user, so the actor is not signalled that the change is being logged. That is a precise statement of what 
evidence a Maximo deployment emits during ordinary maintenance recording.

### Historian documentation

The time-series layer carries an audit surface too. A historian records not only the process values themselves but an
edit audit trail: which stored value was changed or deleted, the old and new value, the user, and the time, held in the
historian's own database rather than in the archive being edited. The specific edit-logging behaviour of e-terracontrol's
SQL Server historian is not public in the way a general-purpose historian's is, so the exact fields are inferred from how
time-series archives log edits generally. Either way, that audit trail of edits is exactly the tamper-and-change evidence
an investigator would look for.

### SCADA operator manuals

The genre is equally documented. Alarm and event journals, sequence-of-events lists, and operator action logging with
acknowledgements are standard chapters in the operator manuals of the SCADA and ADMS families (GE, Schneider, Survalent
and similar).

The distinct ADMS product, and the e-terra operator-manual detail (the exact journal format and operator-audit
fields), did not surface publicly, so those fields cannot be pinned to Stedin's deployment. The category is well-documented; the particular manual is
the gap.

## The observability substrate

The asset and work-management layer (Maximo, confirmed) emits attribute-level change trails, e-signature records and
login tracking across assets and work orders.

The historian emits process values plus a value-edit audit trail.

The protection layer (relay makers inferred as SIPROTEC and SEL, not independently confirmed) emits
sequence-of-events logs, fault and disturbance records and breaker state records.

The control layer (e-terracontrol SCADA and e-terra EMS confirmed; ADMS function present but distinct product not 
pinned) emits alarm and event journals, operator action logs, and SQL Server historian records. The e-terra data sheet 
advertises e-terratrust as the authentication layer, though its use at this operator is not independently confirmed. The 
ADMS vendor remains unconfirmed.

These manuals describe the evidence the system emits by design, specified in advance of any incident and independent of
any narrative about one. The incident reports are the material trace after the fact; the vendor documentation is the
same trace specified before the fact, the observability substrate that determines what can later be reconstructed at
all.

The annual reliability report shows an operator's fault statistics, the outage investigation shows what happened
once, and the vendor documentation shows, at the level of the record type, what every ordinary switching operation,
setting change and work-order edit leaves behind.

*Last updated: 11 July 2026*
