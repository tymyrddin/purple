# Infrastructure domains

Each domain represents a combination of physical assets, digital systems, outsourced services, and human processes.

## Energy supply

Includes:

* Power generation (including the experimental "Geomantic Resonator" in the University)
* Substations and switching nodes
* Distribution networks (both above and below ground)
* Smart meters and household connections

Building types: `power_source` (generating stations, one per district; the cascade root for all energy-dependent failures)

Energy underpins almost every other domain.

## Water and sanitation

Includes:

* Water treatment (the famous Ankh-Morpork Water Company)
* Pumping stations
* Distribution networks
* Wastewater handling and processing

Building types: `water_source` (communal pumps and pumping stations: critical for low-wealth districts; failure here cascades to brewery, healthcare, and fire service)

Public tolerance for water disruption is extremely low.

## Communications

Includes:

* Semaphore relays and clacks towers
* The new "Talking Drums" mobile network
* Emergency communications
* Coordination systems used by public services

Building types: `clacks_tower` (relay nodes, the backbone); `communications_office` (Grand Trunk Company, Talking Drums HQ, coordinate the network); `media` (Ankh-Morpork Times shapes narrative and acts as a detection mechanism); `hackerspace` (Scarlet Semaphore does informal resilience and vulnerability research)

Loss of communication amplifies every other incident.

## Transport and movement

Includes:

* Bridges (including the unreliable Brass Bridge)
* Traffic control (watchmen on point duty, experimental automated gates)
* Public transport coordination (horse-drawn omnibuses, canal barges)
* Logistics routes to the docks and the Sto Plains

Building types: `transport` (bridges and major chokepoints: structural degradation hides; closure is immediate and isolating)

Transport failures have visible, immediate impact on daily life and business.

## Public services

Includes:

* Lady Sybil Free Hospital and other care facilities
* City Watch and emergency services
* Fire posts and emergency pump stations
* Municipal administration (the Patrician's Palace)
* Enforcement and safety services (the Guilds, the Watch)

Building types: `healthcare` (hospitals: catastrophic sensitivity; failure is instantaneous trust collapse); `security` (Watch posts and Dept. of Silent Stability: very high sensitivity; absence enables cascading criminal interference); `fire_service` (fire posts: invisible failure until a fire; without them, workshop fires become district fires)

Failures here are politically sensitive and hard to recover from reputationally.

## Commercial and industrial sites

Includes:

* Food production and storage (the slaughterhouse district, the cheese caves)
* Markets and retail (the Shambles, the Saturday Market)
* Brewing and distribution
* Finance and payments (the Royal Bank of Ankh-Morpork, the Guild of Merchants)
* Workshops and small manufacturers
* IT and data contractors

Building types: `food_supply` (markets and warehouses: just-in-time; shortages visible fast); `brewery` (single point of failure for the city's beer supply; cultural and social cascade); `workshop` (artisan production: individually minor, collectively the industrial backbone; industrial fire risk); `tech_business` (Golem Trust, Purple Lantern: invisible until compromised; vendor monoculture risk)

Disruption here translates quickly into economic and political pressure.

## Residential areas

Includes:

* Homes and tenements
* Apartment buildings (especially in the more respectable parts of the city)
* Small businesses operating out of dwellings
* Local utility connections

Building types: `slum_dwelling` (Shades, Cockbill Street: extreme sensitivity; no margin for error); `middle_class_housing` (Isle of Gods, Small Gods residences: high sensitivity; vocal and politically connected); `civic_amenity` (museums, theatres: low crisis priority but high cultural significance)

Residential impact is where abstract failures become personal.