# Signaal opsporings systeem (SOS)

## Possible architecture

The system's goal is to automatically identify potential 'choke points' in critical infrastructure. It reuses my earlier three-phase concept but replaces placeholder APIs with actual Dutch government services.

The architecture comprises four layers:

- Ingestion Layer: Data acquisition from PDOK APIs, Overheid.nl catalogue, scheduled scraping, and manual uploads.
- Storage & Processing Layer: A "Data Lake" stores all raw data, which is then processed by Python scripts to extract structured information into a relational database.
- Correlation & Analysis Layer: The structured data is fed into a graph database like Neo4j. As data arrives, the system's logic queries this graph to identify dependency chains.
- Presentation Layer: A dashboard for visualisation and an alerting module that sends notifications when new correlations are found.

## Data Source catalogue

While some data is available through APIs, some of the most operationally useful intelligence comes from static documents, downloadable datasets, planning archives, and administrative records that can be collected, parsed, and correlated over time.

The significance rarely lies in a single source. It emerges through accumulation, cross-referencing, and temporal correlation across otherwise unrelated publication systems.

### Active (API) sources

#### TenderNed API

Real-time authenticated XML API containing Dutch public procurement notices.

The API exposes procurement metadata in European TED XML format and requires substantial parsing to extract operationally useful fields such as:

* contracting authority
* assignment title
* maintenance scope
* geographic references
* contractor relationships
* award values

Relevant examples include:

* maintenance contracts
* infrastructure upgrades
* physical security systems
* network facility maintenance
* energy continuity systems

API endpoint:
[https://www.tenderned.nl/papi/tenderned-rs-tns/v2/publicaties](https://www.tenderned.nl/papi/tenderned-rs-tns/v2/publicaties)

#### PDOK Locatieserver

Geocoding and spatial search API used to translate addresses and place references into geographic coordinates for correlation and mapping.

Useful for:

* geocoding contractor locations
* locating infrastructure references
* correlating textual procurement records with spatial datasets

Modern API portal:
[https://api.pdok.nl/](https://api.pdok.nl/)

Locatieserver documentation:
[https://api.pdok.nl/bzk/locatieserver/search/v3_1/ui/](https://api.pdok.nl/bzk/locatieserver/search/v3_1/ui/)

#### Ruimtelijkeplannen.nl API

Official Dutch spatial planning API containing zoning plans, infrastructure references, permit overlays, and planning annotations.

Operationally valuable because planning documentation frequently exposes:

* utility corridors
* defence-related infrastructure references
* construction sequencing
* environmental constraints
* dependency relationships

API endpoint:
[https://api.ruimtelijkeplannen.nl/](https://api.ruimtelijkeplannen.nl/)

#### Overheid.nl Open Data Catalog API

Metadata catalogue for discovering datasets published across Dutch government domains.

Useful as a discovery layer for:

* infrastructure datasets
* planning archives
* environmental reviews
* permit registries
* geospatial publications

### Passive (bulk/static) sources

#### TenderNed bulk datasets

Twice-yearly bulk releases containing historical procurement records and awarded contracts.

Operational value comes from longitudinal analysis:

* recurring contractors
* maintenance concentration
* repeated infrastructure references
* dependency relationships over time

Available through:
[https://www.tenderned.nl/](https://www.tenderned.nl/)

#### Nationaal Georegister (NGR)

Central discovery platform for official Dutch geospatial datasets.

Contains:

* municipal datasets
* water authority publications
* infrastructure overlays
* environmental mapping
* utility references

Portal:
[https://nationaalgeoregister.nl/](https://nationaalgeoregister.nl/)

#### Copernicus Data Space Ecosystem and Sentinel services

Satellite imagery and remote sensing datasets useful for:

* construction monitoring
* infrastructure development tracking
* terrain analysis
* change detection over time

Particularly useful when correlated with:

* permits
* planning procedures
* procurement timelines

#### Bellingcat SAR Interference Tracker

A public analytical tool using SAR interference signatures to identify possible radar activity locations.

Useful for:

* radar correlation
* electromagnetic footprint analysis
* comparison with planning and procurement datasets

Google Earth Engine application:
[https://ollielballinger.users.earthengine.app/view/bellingcat-radar-interference-tracker](https://ollielballinger.users.earthengine.app/view/bellingcat-radar-interference-tracker)

## Ingestion strategy: APIs and scrapers

This layer moves raw administrative, geospatial, and procurement data into structured storage for correlation and analysis.

The challenge is not acquisition alone, but normalisation across incompatible publication formats and fragmented government systems.

### Automated API ingestion

#### TenderNed ingestion

Scripts perform authenticated API calls to:

* identify new tenders
* filter defence-related procurement
* detect infrastructure and maintenance contracts
* monitor contractor relationships over time

Examples:

* UPS maintenance
* secure network room maintenance
* perimeter security systems
* backup power infrastructure
* OT/ICS support contracts

#### PDOK enrichment

The PDOK Locatieserver can be used to:

* geocode addresses
* resolve location ambiguity
* spatially correlate textual procurement references
* enable graph-based infrastructure mapping

This transforms administrative text into spatially analysable entities.

### Scraping static portals

Some of the most operationally useful datasets remain partially structured or document-based.

#### Ruimtelijkeplannen.nl

Scheduled retrieval of:

* zoning plans
* environmental appendices
* utility overlays
* infrastructure references
* permit attachments

These frequently expose:

* utility corridors
* infrastructure co-location
* maintenance dependencies
* construction phasing

#### TenderNed bulk archive ingestion

Semi-annual bulk datasets are downloaded automatically and processed for:

* historical contractor analysis
* recurring infrastructure references
* dependency evolution over time

This enables temporal analysis rather than merely static observation.

#### Overheid.nl catalogue crawling

Daily crawling identifies:

* newly published datasets
* permit archives
* planning decisions
* environmental reviews
* geospatial additions

The objective is continuous discovery of administratively distributed infrastructure information.

### Manual and semi-automated upload

Some operationally significant information exists only in:

* PDFs
* scanned appendices
* hearing documents
* WOO disclosures
* contractor documentation
* engineering reports

This layer provides ingestion support for:

* WOO request documents
* manually collected permits
* network operator publications
* infrastructure diagrams
* archived technical documentation

Examples include:

* TenneT
* Stedin
* Enexis
* water authority appendices
* local planning records

## Correlation engine

This is the analytical core of the system.

The purpose is not merely storing datasets, but reconstructing relationships between:

* infrastructure
* organisations
* maintenance dependencies
* spatial co-location
* operational timing
* governance structures

### Text and data extraction

Unstructured and semi-structured sources are processed using:

* entity extraction
* geospatial parsing
* XML parsing
* document analysis
* metadata correlation

Examples include:

* military site references
* utility infrastructure identifiers
* contractor names
* permit locations
* maintenance activities
* operational keywords

### Geospatial correlation

Spatial analysis combines:

* planning coordinates
* utility overlays
* geocoded addresses
* infrastructure corridors
* satellite imagery

This enables reconstruction of:

* shared dependency zones
* corridor co-location
* infrastructure concentration
* physical support relationships

### Knowledge graph and dependency modelling

A graph database such as Neo4j links:

* contractors
* military facilities
* substations
* pipelines
* permits
* maintenance cycles
* utility operators
* oversight organisations

Example:

A maintenance contractor is linked through TenderNed records to:

* secure network rooms
* backup power systems
* specific military locations

Spatial planning data then reveals:

* shared utility corridors
* single-substation dependencies
* overlapping civilian infrastructure support

The graph transforms isolated publications into operational dependency chains.

### Risk scoring and resilience analysis

The system evaluates:

* redundancy
* concentration risk
* shared infrastructure exposure
* contractor centralisation
* maintenance bottlenecks
* operational fragility

Examples:

* facilities dependent on single substations
* logistics routes lacking redundancy
* shared corridors supporting multiple critical systems
* repeated contractor dependencies across sensitive locations

The focus is not vulnerability scanning.

It is systemic dependency analysis.

## Validation with data sources

The system is designed around real administrative and operational datasets from the start.

Its purpose is not theoretical modelling alone, but validation against observable infrastructure relationships.

### TenderNed procurement data

Historical TenderNed datasets reveal:

* recurring contractors
* infrastructure maintenance relationships
* physical access pathways
* operational outsourcing patterns

Example:
A single contractor repeatedly appears in maintenance contracts for:

* access control systems
* secure network rooms
* backup power systems

This exposes dependency concentration and contractor centrality within sensitive operational environments.

### Ruimtelijkeplannen.nl spatial planning data

Spatial planning records expose:

* utility corridor alignment
* Defence Pipeline Organisation (DPO) infrastructure
* infrastructure co-location
* environmental dependencies

A historical dike relocation plan explicitly references:

* location
* diameter
* routing context

of a DPO fuel pipeline.

Correlated with:

* utility maps
* permits
* water authority records
* maintenance disclosures

This allows reconstruction of parts of a defence logistics dependency network through entirely public information.

## Feasibility 

Building the S.O.S. system is technically feasible using existing open data, graph analysis tooling, geospatial systems, and document processing techniques.

The complexity lies less in collection than in:

* correlation
* temporal accumulation
* infrastructure interpretation
* dependency modelling

A limited but operational prototype could likely be assembled within weeks using:

* public procurement data
* spatial planning archives
* geospatial APIs
* graph databases
* standard parsing pipelines

The resulting system would not “discover secrets”. It would reveal how fragmented administrative transparency 
gradually accumulates into operationally meaningful infrastructure visibility.

In that sense, the modern attack surface is less purely technical. It is increasingly administrative, distributed, 
and assembled through correlation over time.
