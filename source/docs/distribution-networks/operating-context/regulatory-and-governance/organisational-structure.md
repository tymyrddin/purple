# Organisational structure

![Organisational structure](/_static/images/distribution-organisational-structure.png)

## Corporate partition

At the top sits [Stedin Holding N.V.](https://www.stedingroep.nl/), trading as Stedin
Groep, with three separate subsidiaries: the regulated grid operator Stedin Netbeheer B.V., plus the unregulated
NetVerder B.V. and DNWG Groep N.V. DNWG Groep in turn holds the (now-merged) grid operator Enduris and the
infrastructure company DNWG Infra B.V.

The group's own definitions treat these as distinct legal persons. This separation is not cosmetic. It descends from
the [Wet Onafhankelijk Netbeheer](https://wetten.overheid.nl/BWBR0020608), which since 2011 has required
utilities to hive the regulated network activity into a separate company under a group prohibition, the reason Stedin
was split from Eneco in the first place.

In access terms, the group prohibition is an access control regime expressed through company law. It dictates which
legal entity may operate the regulated gas and electricity networks and separates the regulated network operator from
commercial activities. Dutch law also requires regulated gas and electricity network activities to be kept separate from
other energy infrastructures such as steam, biogas, CO₂ and heat. Stedin therefore transferred those activities into the
separate [NetVerder](https://www.stedingroep.nl/pers-en-media/persberichten/netverder-een-nieuwe-naam-bij-stedin-groep) 
brand in 2019.

### The access-and-confidentiality regime

As network operator, Stedin runs the market administration and is obliged to keep its
networks [accessible to every energy supplier on equal terms](https://www.stedin.net/-/media/project/groep/files/gedragscode-stedin-groep.pdf),
which pins non-discrimination and data confidentiality onto the same boundary.

The division of labour over metering data
is instructive: an
earlier [ACM dispute decision](https://www.acm.nl/nl/publicaties/geschilbesluiten-consumenten-stedin-over-meterstanden)
established that under the Informatiecode it is the supplier that collects meter readings for billing, while the
operator measures on the supplier's behalf rather than for the consumer directly. The entitlement to customer
consumption data is split by role, not held wholly by the operator.

Under the Energiewet this hardens further through
the [new data-exchange entity](https://energiedatawijzer.nl/kennismaken-met-data-delen/gegevensuitwisseling-energiewet/)
that mediates energy data between operators, suppliers and end users, and through the metering and data-security
supervision the RDI picks up.

### Seams in the partitions

Access deliberately crosses the boundaries the unbundling regime draws. Three crossings show up in public filings.

The first is shared services. When Enduris was folded into Stedin from 1 January 2022, the Zeeland network operator [took the Stedin name and more
than 600 staff moved across](https://www.stedingroep.nl/pers-en-media/persberichten/stedin-wordt-netbeheerder-voor-gas-en-elektra-in-zeeland),
merging two operators' staff functions and grid operations under one name. That is a single operational and system
estate spanning what were two operators.

The second is DNWG Infra,
which [performs maintenance and management on networks entrusted to it by other operators](https://www.stedingroep.nl/-/media/project/groep/files/stedin-groep-jaarverslag-2023.pdf),
naming Evides Waterbedrijf, Stedin and TenneT, and acts as a recognised metering-responsible party. An unregulated group
subsidiary holding operational and metering access to third-party regulated networks is a notable cross-entity
entitlement.

The third is the joint ventures. [Utility Connect B.V.](https://www.utilityconnect.nl/), a
JV with Alliander's network group, runs its own wireless telecommunications network to read smart-meter data and
communicate with smart-grid applications, a shared metering-data channel co-owned with a different DSO
group. [TensZ B.V.](https://www.stedingroep.nl/-/media/project/groep/files/stedin-groep-jaarverslag-2023.pdf) is the fifty-fifty vehicle with TenneT
for managing high-voltage networks. Both put operational access to grid assets and data into entities jointly controlled
with outside parties.

### Decision rights

Above the operating layer, control is exercised through a [two-tier board](https://managementscope.nl/bedrijf/stedin), a
raad van bestuur running the group and answerable to a raad van commissarissen.

Shareholder power is concentrated but
capped: the Energiewet's predecessor
required [public-only ownership](https://wetten.overheid.nl/BWBR0023536),
so the register is [61 municipalities, two provinces and the Dutch State](https://www.stedingroep.nl/aandeelhouders),
the State having taken 11.8 to 11.9 per cent for 500 million euro in December 2023.
The [largest holders](https://www.stedingroep.nl/aandeelhouders) are Rotterdam, The Hague, the State and Dordrecht.

Day-to-day shareholder interaction runs through a twelve-member aandeelhouderscommissie representing all shareholders,
with relations set out in the statutes and a shareholder covenant. This is who can direct the entity, as distinct from
who can operate its systems.

## Functional organisation

### Business units

The operating organisation is described less as product divisions than as a set of "ketens" (chains) and business lines.
Stedin's careers pages list Asset Management as the owner function, Engineering split into electricity and gas, a
Zakelijk Complex chain holding the high-voltage and large-connection work, Supply Chain Management, and IT & Data. Above
these, at group level, the regulated operator Stedin Netbeheer sits alongside NetVerder and DNWG. Staff functions
visible in the same material include Compliance & Juridische Zaken, Internal Audit and Business Control.

### OT versus IT separation

Stedin frames IT and OT as a single risk domain rather than two separate worlds. A KPN write-up of a Stedin conference
talk describes one security operations centre monitoring both, strict network segmentation, access rights held to a
minimum, and critical systems able to run in island mode cut off from external connections.

Structurally, though, OT
lives in its own vakgroep OT Infrastructuur & Telecom, OTI&T, which places it inside the Zakelijk Complex chain and
lists teams for Netautomatisering, OT-platforms and telecom networks. The OT estate itself is described as applications,
services, OT platforms, a telecom network and "IT for OT". IT proper is a separate agile organisation with 35 DevOps
teams moving to BizDevOps, plus a Netwerk & Infra function.

The public story is convergence at the risk and monitoring
layer over a real organisational and network split beneath it.

### Network operations centre

The Bedrijfsvoeringscentrum is described as the beating heart of the operator, where the electricity and gas networks
are watched in real time on large screens, with operational specialists using those feeds to look ahead and head off
overload through flexible capacity and congestion measures. High-voltage management and maintenance is run jointly with
TenneT through the [TensZ](https://www.stedingroep.nl/-/media/project/groep/files/stedin-groep-jaarverslag-2023.pdf) joint venture, so that slice of
operations is shared rather than wholly internal.

### Asset management

Asset Management reads as the owner function rather than an execution one. A Business Control vacancy has it acting as
the asset manager that commissions other departments to realise infrastructure works and projects, and developing the
policy through which the targets are met.

Its own careers material
describes [specifying components and setting long-horizon policy](https://werkenbij.stedin.net/asset-management),
some of it reaching decades ahead, staffed by strategic and tactical asset managers, net
specialists and fault specialists. It is the function that decides what gets built and maintained, and hands the doing
to others.

### Maintenance

Maintenance runs through a Ketenteam Onderhoud. A Gemba vendor case study describes around 300 fitters keeping the gas
and electricity installations in condition, working in IBM Maximo, and moving from static supplier-defined intervals to
risk-based maintenance with Gemba consultants embedded in the chain team. The chain covers low-voltage, medium-voltage
and gas, with high-voltage being folded in, and the work is commissioned by Asset Management, consistent with the
owner-executor division.

### Engineering

Engineering is presented as the bridge from customer demand to net calculations, advice and design, split into
electricity and gas engineering, with a separate Engineering Gas line reflecting the hydrogen and green-gas transition.
It sits between the technical estate and the customer-facing plans.

### Cybersecurity

The security function is anchored in a central CISO within a CIO/CISO office. OT security specialists sit in a team of
about twelve inside OTI&T, operationalising a central Stedin cybersecurity policy, working to IEC 62443 and ISO 27001,
reviewing configurations and logs, hardening, guiding pentests and applying security by design, with work located partly
at high-voltage stations and datacentres.

Supplier risk is assessed, contractually fixed and technically tested, with
the stated view that certification alone is not enough and products are tested before they go into the network.

Personnel screening is heavy, with a VOG and full screening required before starting and self-employed contractors
excluded from these roles.

### Procurement

As a contracting authority Stedin
is [bound by the Aanbestedingswet 2012](https://www.stedin.net/over-stedin/inkoop-en-aanbesteding) and publishes
European tenders through TenderNed, running procurement and supplier management on SAP Ariba, with a Vendor Management
function setting per-tender KPIs and a raw-materials passport tracking component circularity.

External hiring runs
through a separate Dynamisch Aankoopsysteem and a Stedin Inleensysteem.

Two governance threads run through procurement: the governance code Veilige Energienetten extended to chain partners, and OECD-based human-rights and environmental due diligence across the supply chain.

### Architecture

Architecture appears as a layered function: enterprise architects and solution architects at the centre, with OT domain
architects who align the network and platform structures for OT with those enterprise and solution architects. Within
OTI&T there is a dedicated Security & Architectuur team, so security and architecture are treated as one grouping on the
OT side rather than kept apart.

### Innovation groups

The visible innovation work centres on algorithms and AI built into the networks. Stedin has [described geographic AI
models](https://www.dutchitchannel.nl/news/220948/stedin-stroomlijnt-energietransitie-met-geografische-ai-modellen),
trained on data going back to 2013, that estimate both the failure probability of an infrastructure component and the
impact of a fault, combining location data, satellite imagery and subsurface data into a risk model that steers
maintenance and replacement toward incidents before they happen. The delivery model is DevOps and BizDevOps, with
collaborations alongside startups, universities and market parties. Embedding decision logic in the nets carries its own
exposure: a design fault in an algorithm that plans or steers the network could propagate, which places this work on the
same risk boundary as the OT estate it informs.

## The unlit interior

Public sources fix the legal boundaries, the regulatory access separation, the shared-service and JV crossings, and the
governance chain, and they describe which functions exist and roughly how they hand work to each other. What they do
not reveal is the internal role model, the segmentation between IT and OT, the contractor and supplier access
arrangements, or the identity infrastructure that turns those entitlements into live permissions. The corporate map
tells which entities are entitled to reach which assets; it does not tell how tightly that entitlement is enforced,
which is the gap between an org chart and an access-control finding.

*Last updated: 11 July 2026*
