#  Open Source Intelligence (OSINT)

The point of this exercise is not intrusion. It is to map the dependencies an adversary could infer from records that were never sensitive in isolation. Permits, tenders, job ads, planning portals; each published for legitimate reasons, each routine. Combined, they can describe a site's quiet supports in surprising detail.

The examples below are in Dutch (context).

## A working process

A narrow, repeatable loop tends to work better than a broad sweep. Pick the smallest interesting target, follow the dependency chain, and stop when the picture stabilises.

1. Pick an anchor. A single site, narrowly defined: a radar station, an ammunition depot, a logistics hub.
2. List its critical services. Electricity (typically medium voltage), cooling water, data connectivity, fuel supply, physical access, waste handling.
3. For each service, find the public footprint.
   - Electricity: search Ruimtelijke Plannen for *transformatorhuisje* near the site, then trace which grid node feeds it.
   - Fuel: pipeline permits crossing nearby land, often filed as *buisleiding brandstoffen*.
   - Cooling: water-extraction permits via the local waterschap.
   - Data: fibre routes on PDOK, or municipal civil-works permits where new ducts are dug.
4. Identify third-party dependencies. Tenderned awards for *onderhoud hoogspanning* or similar at the location, contractor LinkedIn tags ("worked at site X doing generator testing"), service-provider case studies.
5. Build a dependency graph. A spreadsheet is enough: asset, service, provider, public source, observable weakness (e.g., "permit shows pipeline runs under public road, no evident redundancy").
6. Run the adversarial reframe. If the goal were to interrupt this site's primary function for 48 hours, which single points does the public record already expose?
7. Note what was never visible without aggregation. The structural finding tends to be the dependency chain, not any single document. This step is the one most often skipped, and the one that connects the work to the administrative attack surface as a whole.

## Breadcrumb categories

Useful categories when scanning:

- Physical dependencies. Power feeds, water and sewer, gas pipelines, district heating, fibre routes, backup generators, UPS locations.
- Third-party dependencies. Maintenance contractors, cleaning, catering, security guards (and shift patterns), waste disposal, IT service desks, HVAC servicing.
- Temporal patterns. Permit application dates, planned outages, roadworks near sites, vibration monitoring near pipelines (often used for leak detection but also a useful schedule signal).
- Overlapping infrastructure. Military cables sharing a conduit with civilian lines, a radar installation and a factory drawing from the same substation.
- Personnel hints. Job postings tied to a named site (e.g., "electrician for Volkel Air Base"), LinkedIn profiles of contractors, social media check-ins near sensitive locations.
- Environmental data. Satellite imagery (free Sentinel-2) of construction pits, pipeline markers, substations inside restricted areas.

## Dutch public sources

*Spatial planning and permits*

- [Ruimtelijke Plannen](https://www.ruimtelijkeplannen.nl/home), permits for new buildings, pipeline routes, utility corridors. The portal remains available but is no longer being updated.
- [Omgevingsloket](https://omgevingswet.overheid.nl/home), the successor under the Omgevingswet. Coverage is incomplete and the new viewer (*Regels op de kaart*) does not yet match the old plan map for usability. The transition period runs to 2032, so during this window both portals are in scope and neither is canonical on its own.
- [Overheid.nl](https://overheid.nl/), publication platform for environmental permits, exemption decisions, and tender notices.
- [Tenderned](https://www.tenderned.nl/cms/nl), tender notices and awards, including maintenance and works contracts.

*Underground assets*

- KLIC (Kabels en Leidingen Informatie Centrum). The detailed registry is restricted, but the public viewer is enough to indicate cable-density areas.

*Geodata*

- [PDOK](https://www.pdok.nl/) (Publieke Dienstverlening Op de Kaart), base maps, soil data, infrastructure layers.
- OpenStreetMap, user-contributed power lines, substations, pipelines, often unusually detailed in the Netherlands.

*Water*

- [Rijkswaterstaat](https://www.rijkswaterstaat.nl), with searchable [pumping stations](https://www.rijkswaterstaat.nl/zoeken?keyword=pomp), [flood defences](https://www.rijkswaterstaat.nl/zoeken?keyword=overstroming), and [bridge maintenance schedules](https://www.rijkswaterstaat.nl/zoeken?keyword=brug&root=Wegen).
- Local waterschappen, water-extraction permits and operational reports.

*Airspace and radar*

- [Luchtverkeersleiding Nederland](https://www.lvnl.nl/) (LVNL), with [primary radar surveillance](https://eaip.lvnl.nl/web/eaip/AIRAC%20AMDT%2002-2026_2026_02_19/eAIP/EH-ENR%201.6-en-GB.html#ENR-1.6), the [radar coverage map](https://www.defensie.nl/documenten/2019/04/30/milieu-rsh-radarverstoringsgebieden), [NOTAMs](https://www.ead.eurocontrol.int/cms-eadbasic/opencms/en/ead-operations/data-maintenance/), [MilAIPs](https://english.defensie.nl/topics/m/milaip-military-aeronautical-information-publication#content-wrapper), and [frequency lists](https://scramble.nl/forum/viewtopic.php?p=361134&sid=3ea6fc67f62417438be1633e549ecec7).

*Labour market*

- LinkedIn and Indeed, job ads specifying backup-generator maintenance, UPS battery replacement, or security-cleared electricians, often with a named location.

*Visual reconnaissance*

- Google Maps and Street View, fence lines, camera positions, manhole covers, utility markers.
- Company websites, where local technical service providers occasionally note "MoD contracts" alongside site photos.

For a worked example using a small subset of these sources, see [Radarstation Herwijnen](herwijnen.md).