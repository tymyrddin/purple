# Job advertisements

![Job advertisements](/_static/images/distribution-job-advertisements.png)

Job adverts are high-yield sources precisely because they name the tools a candidate needs, and each named tool implies
its own evidence store and workflow. Stedin's own adverts demonstrate this approach: each named tool or task points to a
system's existence, the fact that someone queries it, that records are retained, and that workflows depend on it.

## The advert that moves the control-room gap

A Stedin SCADA Engineer advert for Stations Automatisering states that the Energiedistributie department owns the
applications and hardware in the OT domain, that the SCADA systems are used by control-room operators to monitor and
remotely switch the primary electricity and gas networks, and that the role connects the central EMS and DMS systems to
the outside world and builds station automation for HV, MV and gas stations, including configuring self-healing networks
in the DMS.

That single advert establishes: an EMS and a DMS exist and are operated centrally; the DMS carries automated
fault-isolation-and-restoration logic (the self-healing configuration), which emits reconfiguration and switching
events; station automation is built and versioned somewhere, so a configuration surface exists and is reviewed; and on
station-automation faults the engineer determines the cause, which only works if diagnostic evidence is retained.

The
control layer is an EMS-plus-DMS architecture with FLISR, not an unknown monolith. The vendor is not named.

## Commissioning and settings

A Junior Inbedrijfsteller (commissioning) advert lists testing, setting and delivering complex high-voltage
installations. Commissioning produces test records and as-set values, an oplevering (hand-over) sign-off exists as an
artefact, and settings are established and checked at commissioning, which implies a settings baseline held somewhere
against which later changes could be compared. Stedin's commissioning and station-automation roles are where that review
lives.

## The systems inventory, reassembled from adverts

The adverts alone have reconstructed most of the stack, each line implying its evidence store. The
Smallworld GIS Developer advert named Smallworld and Lovion and an integration to the SCADA system, so a maintained
as-built network model exists and exchanges data with the control layer. The SAP adverts named S/4HANA, C4C and Ariba,
each carrying its own change-and-audit trail. The Azure and cloud-transition adverts placed most business applications
in one hyperscaler with its logging. The Security Office adverts described a team watching IT and OT together, implying
a monitoring and event pipeline. The WV Hoogspanning and Bedieningsdeskundige adverts described writing switching plans
and operating net switches, implying switching-plan and switching-log artefacts. The Monteur Gas storingsdienst adverts
revealed the fault-duty rota.

Put together, the adverts are a systems inventory in which every named tool is also a
claim about what evidence that tool retains.

## Where the adverts stay silent

The consistent silence persists at the advert level. Even the SCADA Engineer advert, which confirms EMS, DMS, station
automation and self-healing, does not name the products behind them. That such a line has not appeared, across adverts
otherwise specific about SAP, Azure, Smallworld and Lovion, is itself informative: the enterprise and asset layers are
named freely in job postings, and the control-room platform is described only by function.

However, the control-room
vendor (Alstom e-terra, now GE Vernova) is pinned through vendor press releases and procurement announcements outside
the advert channel.

No advert surfaced naming the historian product, the protection-relay maker, or an ADMS vendor;
these remain gaps in the public employment postings.

## Where this leaves the observability picture

Adverts complete the set from the demand side, revealing which systems Stedin actually runs and staffs.

The consistent
pattern: a Smallworld-and-Lovion network model, an SAP core on Azure, IBM Maximo for assets, and a central EMS-and-DMS
control layer with FLISR and station automation, each with its implied evidence store.

The single gap remains the
identity of the control-room and protection products, defined tightly enough that one well-worded advert, or one
TenderNed control-system lot, would likely resolve it.

*Last updated: 11 July 2026*
