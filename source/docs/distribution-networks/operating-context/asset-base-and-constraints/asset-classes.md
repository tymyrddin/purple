# Asset classes

Most of the published
numbers are annual flow (what was laid or built that year), not stock (what is installed in total). The stock figures
anchor modelling, and Stedin headlines them less cleanly than the flows, so several of these figures are
order-of-magnitude, with the exact value sitting in the open GIS data rather than in prose.

## Substations

The distribution layer is the well-reported stock: around 26,500 distribution substations (trafohuisjes, converting
medium to low voltage) under management as of
the [2022 report](https://www.stedingroep.nl/-/media/project/groep/files/stedin-groep-jaarverslag-2022---energiek-doorpakken-final.pdf),
growing by a few hundred a year, with the [2024 report](https://www.stedingroep.nl/-/media/project/groep/files/stedin-groep-jaarverslag-2024.pdf) recording 478 added in 2022, 266 in 2023 and 353 in 2024.

The higher-voltage stations (regional HV and HV/MV
substations) are not given a clean single count in these sources; press references to "500 stations" in a build year mix
the two tiers, so that figure is flow and mostly trafohuisjes rather than a stock of large substations.

## Transformers

No clean total is published. As a modelling proxy, transformer count roughly tracks the distribution-substation stock (
order of tens of thousands of MV/LV units, roughly one per trafohuisje) plus a smaller population of large power
transformers at the regional HV and HV/MV stations. Capacity added is reported instead of counts: 513 MVA extra in 2023,
344 MVA in 2024 (2024 report).

## Cable length

Reported almost entirely as annual flow: roughly 680 km laid in 2021, 892 km in 2023, 1,013 km in
2024 (2024 report). The total installed stock is not headlined in what these
sources give. By comparison the neighbouring operator Liander's [investment plan](https://www.liander.nl/-/media/files/financiele-communicatie/investeringsplannen/investeringsplannen-2024/investeringsplan-liander-elektriciteit-en-gas-2024.pdf) sets out nearly 40,000 km on medium voltage alone this decade,
so Stedin's electricity stock is plausibly in the low tens of thousands of km, with the exact split by voltage sitting
in the open GIS data rather than in the reports.

## Gas network length

Again mostly flow: around 242 km of mains laid in 2021, and a replacement programme of 212 km of brittle pipe (grey cast
iron, asbestos cement) removed in 2023, and the [2023 report](https://www.stedingroep.nl/-/media/project/groep/files/stedin-groep-jaarverslag-2023.pdf) targets all brittle pipe for removal before 2028.
The replacement map is downloadable, which is the better route to the stock than the prose.

## Voltage levels

The structural cut, sharpened by the Energiewet, is transmission above 110 kV (TenneT) versus distribution below 110
kV (Stedin). Within Stedin's distribution estate: low voltage at 230/400 V, medium voltage typically in the 10 to 25 kV
band, and regional high voltage up to around 50 kV feeding from TenneT's 150 kV transport. On gas, low-pressure
distribution regionally, with pipelines at 16 bar and above sitting under ILT rather than SodM for safety oversight.
Congestion in the port and surrounding regions is anchored at TenneT's 150 kV
level (2023 report).

## Control centres

One central operational control room, the Bedrijfsvoeringscentrum, running real-time monitoring of both the electricity
and gas networks. High-voltage operation and maintenance is run jointly
with TenneT through the [TensZ](https://www.stedingroep.nl/-/media/project/groep/files/stedin-groep-jaarverslag-2023.pdf) joint venture, so that
tier is shared rather than solely internal.

## Meter population

Around 2.3 to 2.4 million connections across the service area, with smart-meter penetration reported at 84.7 per cent of
households end-2022 rising to 87 per cent
end-2023 (2023 report),
and installation running in the low hundreds of thousands per year. The smart-metering data channel itself runs through
the Utility Connect joint venture with Alliander.

## EV charging growth

Reported as a low-voltage load driver rather than an asset Stedin owns. In some urban areas about 20 per cent of all
capacity being built to 2030 is consumed by street charging, and the operator frames it as a direct trade: for each
charge point switched off in the evening peak, roughly one extra new-build home could be connected, scaling to tens of
thousands of homes across a province (Stedin group press release, and
the 2024 report). The pressure sits in the evening peak, roughly 16:00 to 
21:00.

## Solar integration

More than 145,000 customers took up solar in a single year (2023), with the reverse-flow problem now visible: around
3,000 voltage complaints from inverters dropping out at midday because the street cable was saturated with solar. Cable
pooling is the mitigation for combined solar and wind connections. The stress here is midday low-voltage overvoltage,
the mirror image of the evening EV peak.

## Spatial data and modelling

Flows and stocks are distinct, and press material blurs them: a model fed annual laying
figures as if they were installed base would be wrong by an order of magnitude. The two clean stock anchors are the
roughly 26,500 distribution substations and the roughly 2.3 to 2.4 million connections; network lengths are better taken
from the spatial data than the prose.

Stedin publishes [open location data](https://www.stedin.net/zakelijk/open-data/liggingsdata-kabels-en-leidingen) as GIS
shapefiles: the low-voltage network geometry, the medium-voltage station locations, and the brittle-gas replacement map,
openable in any GIS tool. It also
publishes [aggregated small-consumer consumption open data](https://www.stedin.net/zakelijk/open-data/verbruiksgegevens)
per connection area. Between the substation stock, the connection count, the voltage structure and those two open
datasets, the realistic model has its skeleton and its spatial substrate.

*Last updated: 11 July 2026*
