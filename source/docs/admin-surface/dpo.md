# Defensie Pijpleiding Organisatie (DPO) fuel pipeline

The Defensie Pijpleiding Organisatie operates an underground fuel network that distributes kerosene and other fuels between Dutch military facilities, with connections into NATO's Central European Pipeline System. Most of the network was laid down decades ago. It runs beneath civilian land, often inside corridors shared with civilian utilities.

Two routine documents, a municipal spatial plan and a water-board permit, between them describe a specific pipeline segment, its operating fluid, the corridor it shares with other utilities, and an active repair window. Read separately each is unremarkable. Read together they sketch a portion of national fuel logistics in concrete, geographically anchored detail.

## Data sources

### Spatial plan

The Voorst municipal spatial plan ([Section 5.13.4](https://ruimtelijkeplannen.nl/documents/NL.IMRO.0285.20140-VS00/t_NL.IMRO.0285.20140-VS00_5.13.html)) records: "in the middle of the Voorsterklei lies the DPO pipeline. It is an 8 inch line (DN200)" (*"In het midden van de Voorsterklei ligt de leiding van de DPO. Het betreft een 8" leiding (DN200)."*).

One sentence carries presence, exact diameter, and operating organisation, all written into a publicly searchable civilian planning document. The same plan situates the line alongside the corridors of TenneT (high-voltage), Gasunie (gas), Liander (regional grid), and KPN (telecoms), so the physical context arrives without anyone having to ask.

### Water permit

A Water Authority publication notice ([WSB-2024-19528](https://zoek.officielebekendmakingen.nl/wsb-2024-19528/)) records an "application of 12 September 2024 for the construction, use and relocation of a temporary discharge facility for repair works on the DPO kerosene pipeline at Grensweg in Denekamp" (*"Aanvraag omgevingsvergunning van 12 september 2024 voor aanleg, gebruik en verplaatsing tijdelijke lozingsvoorziening t.b.v. herstelwerkzaamheden aan kerosineleiding van DPO (Defensie Pijpleiding Organisatie), Grensweg te Denekamp."*).

This confirms active maintenance, names the pipeline contents (kerosene), gives the exact intervention site (a different town from Voorst, indicating a distributed network rather than a single asset), and provides operational timing: the work has a permit window in late 2024. *Lozingsvoorziening* is a temporary water-discharge installation used while pipeline sections are dewatered for repair.

## What an adversary can do with this information

What follows is reasoning available from these two sources alone, with older incident reporting (a 1995 rupture is the prominent example) and KLIC context filling in burial-depth variation. No intrusion, no access required.

### Map strategic fuel transport infrastructure

Spatial plans say where military fuel pipelines run beneath civilian land. They distinguish Defence-controlled infrastructure from the civilian utilities sharing the corridor and let an observer trace approximate routing through planning overlays and permit references. The result is a geographically anchored fuel-logistics map that nobody had to declassify.

### Identify shared vulnerability corridors

Because the line runs alongside civilian utilities, the same documents locate corridors where several critical systems are co-located, mark segments where a single disruption can affect multiple services at once, and imply that civilian works programmes have second-order effects on Defence logistics. That is the start of a co-dependent-fragility map.

### Infer maintenance cycles and operational exposure windows

Permit data names where maintenance is occurring, which segments are under repair, and where temporary discharge installations are in place. From there, an observer can infer periods of reduced redundancy, locations where the network is temporarily reconfigured, and windows where resilience depends on stand-in arrangements. The point is not direct action; it is knowing when the system is structurally less stable.

### Reconstruct system depth, routing, and legacy constraints

Historical incident reporting and KLIC context together let an observer infer pipeline-depth variation across segments, older sections with weaker burial protection, and routing decisions shaped by geography, regulation, and forced co-location with civilian networks. The picture is one of uneven physical resilience across a single ostensibly-uniform network.

### Build a system-of-systems logistics model

Combine spatial plans with permit databases, water authority records, and utility maps for gas, power, and telecoms, and the picture stops being one pipeline. It becomes interdependent corridors, shared dependency nodes across sectors, and the points at which Defence fuel logistics intersect with civilian infrastructure ecosystems. The unit of analysis is the national logistics dependency graph.

## Policy recommendation

For infrastructure classified as vital to national security, the levers most directly suggested by the spatial-data exposure pattern in this case:

* aggregation-aware review of spatial-planning disclosures
* corridor-level mapping treated as a question to answer case by case, rather than a default to publish in full
* separation of operational descriptors (exact diameter, routing) from planning-level transparency where the risk is systemic rather than local
* cross-domain reconstructability assessment of multi-agency geospatial datasets before publication

For the broader structural argument and policy frame, see [Strategic frame](strategy.md).