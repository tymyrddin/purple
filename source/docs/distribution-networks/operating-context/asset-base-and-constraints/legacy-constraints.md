# Legacy constraints

Legacy constraints explain the architecture better than any design document would.

## Equipment reaching end of life

Openly reported. The 2022 station programme in Amersfoort, described in
the [2022 report](https://www.stedingroep.nl/-/media/project/groep/files/stedin-groep-jaarverslag-2022---energiek-doorpakken-final.pdf),
removes or replaces outdated components and renews a 50/10 kV transformer station to secure quality and add capacity,
three of the four stations finished that year.

This sits alongside two end-of-life populations: brittle gas mains (grey cast iron and asbestos cement) and the ageing
cable-and-joint stock whose internal-defect failures dominate the fault statistics. So end-of-life is running across gas
mains, cables and station primary plant at once.

## Spare part shortages

Framed as structural material scarcity rather than incidental. In 2022 part of the planned network-driven investment
slipped partly on material scarcity at contractors, with prices rising from that scarcity, and the network-driven scope
came in at 93 per cent for electricity and 96 per cent for gas rather than complete (2022 report).

Stedin's [investment plan for 2024](https://www.stedin.net/-/media/project/online/files/jaarverslagen-en-publicaties/investeringsplan-stedin-2024-inclusief-zienswijzen.pdf)
names the scarcity explicitly as sitting in technicians, in space, and in materials such as cables, lines and
transformers. Transformers in particular are the item where scarcity and lead time compound.

## Long procurement lead times

Quantified in a study the operators commissioned jointly. A high-to-medium-voltage station runs three to seven years
from proposal to commissioning, of which materials ordering alone is around a year and construction one and a half to
two, with environmental and permitting the largest and most variable slice; a medium-to-medium-voltage transformer
station runs two and a half to three years, per a McKinsey 2020 study in a [VNG guidance document](https://vng.nl/sites/default/files/2023-07/handreiking_ruimtelijke_inpassing_van_energie-infra_20230621.pdf).

Stedin's own framing is that a transport-network adaptation has a lead time of many years, and that permitting
trajectories are long, which is why connection lead times have lengthened and why it now says it would build more than
it can, from its [new-connection page](https://www.stedin.net/aansluiting/ik-wil-een-nieuwe-aansluiting) and
its [2050 study release](https://www.stedin.net/over-stedin/pers-en-media/persberichten/studie-integraal-energiesysteem-2050-biedt-kompas-bij-urgente-keuzes-energietransitie).
A one-year transformer order against a three-to-seven-year station is the constraint that sets planning horizons.

## Multi-decade replacement programmes

Two horizons run in parallel. The near, hard deadline is brittle gas removal before 2028. The far horizon is the
Masterplan 2050: Stedin split its area into 18 zones and built a masterplan per zone with a scope to 2050, precisely
because a transport-network change takes many years to realise and has to be started early against uncertain demand (
2022 report).

The strategic investment plan reaches to 2037, and the alternatives are compared on a minimal-regret principle to avoid
stranded spend under deep uncertainty. So the replacement estate is governed on a multi-decade planning cadence, not a
rolling annual one.

## Mixed analogue and digital environments

Acknowledged in the operator's own words, that it is putting ever more IT-like components into a traditional technical
landscape, which helps steer more precisely but raises complexity (from Stedin's public security account).

Concretely, smart sensors and Smart Grid Terminals are retrofitted into existing medium-voltage stations rather than
deployed on a clean build, and on metering roughly 87 per cent of households had a smart meter by end-2023, which is
also to say a non-trivial analogue remainder persisted alongside successive DSMR digital generations. The estate is
genuinely hybrid: decades-old primary plant instrumented with a thin, newer digital layer.

## Brownfield integration

This is where the constraints become visible as design choices. The GIS and asset-register modernisation is explicitly
aimed at a loosely-coupled, API-first architecture to reduce the management burden on the legacy application estate (
Smallworld and Lovion), rather than a rip-and-replace (from a Stedin GIS-developer recruitment advert).

The station work is retrofit into live brownfield sites, and the security posture leans on island mode so critical,
older operational technology can keep running detached from external connections.

The enterprise side shows the same brownfield pattern in migration form: an SAP move to S/4HANA and the shift of most
business applications into Azure, both legacy-carrying transitions rather than greenfield builds.

## Legacy constraints as architecture drivers

Taken in sequence, the legacy constraints account for the architecture more cleanly than the technology choices do on
their own.

The loosely-coupled, API-first target is a rational response to a fixed legacy application core (Smallworld, Lovion,
SAP) that cannot be replaced wholesale, so integration is designed to wrap it rather than remove it. Island mode is a
rational response to a mixed analogue-digital OT estate where much of the plant predates network security, so isolation
is the compensating control where modern authentication cannot be assumed. The standardised and clustered station design
and the wijk-by-wijk "production caravan" delivery model are a response to the lead-time and materials constraints,
since uniformity is what lets scarce components and scarce crews be scheduled and reused. And the Masterplan 2050 with
its minimal-regret rule is a response to procurement lead times measured in years against demand no one can forecast, so
early, low-regret commitments substitute for accurate prediction.

The through-line is that Stedin's architecture is shaped less by what is technically ideal than by what a brownfield
estate under materials scarcity and multi-year lead times permits. None of this is architecture freely chosen. The scarce, slow,
end-of-life physical layer sets the terms, and the API-first integration, the island-mode segmentation, the standardised
stations and the 2050 masterplans are what building around it looks like, design decisions on the page and forced moves
on the ground.

*Last updated: 11 July 2026*
