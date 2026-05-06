# Maintenance tender for secured network rooms

The Dutch Ministry of Defence put out a framework tender in 2022 for maintenance of installations in its secured network rooms (*Raamovereenkomst Onderhoud Installaties Netwerkruimtes Defensie*). On its face the notice is unremarkable: a multi-year maintenance contract for HVAC, power, and similar building services, scoped to network rooms at Defence locations.

Three sentences in the public notice carry more than they appear to. They name the work, the security framework the contractor is held to, and the body that supervises compliance. That combination is enough to sketch part of the access model around classified network infrastructure, without the actual contract ever being read.

## Data sources

The notice is published on the OpenProcurements aggregator: [Raamovereenkomst Onderhoud Installaties Netwerkruimtes Defensie](https://nl.openprocurements.com/tender/2022-raamovereenkomst-onderhoud-installaties-netwerkruimtes-defensie/). Three excerpts do the work.

The scope describes "inspecting, certifying and maintaining installations in secured network rooms at Defence locations" (*"inspecteren, keuren en onderhouden van installaties in beveiligde netwerkruimtes op Defensielocaties"*).

The contractor "is required to comply with the General Security Requirements for Defence Contracts 2019, ABDO 2019" (*"dient de opdrachtnemer te voldoen aan de Algemene Beveiligingseisen voor Defensieopdrachten 2019 (ABDO 2019)"*). ABDO 2019 is the standard security baseline applied to private organisations holding Defence contracts that touch classified information or restricted facilities.

Compliance is supervised: "the Industrial Security department of the MIVD oversees enforcement of the ABDO 2019 rules" (*"De afdeling Industrieveiligheid van de MIVD ziet erop toe dat de voorschriften uit ABDO 2019 worden nageleefd"*). The MIVD is the Military Intelligence and Security Service of the Netherlands; its Industrial Security unit vets and audits contractors that hold authorised access.

## What an adversary can do with this information

What follows is reasoning available from the tender notice alone. No intrusion, no access required.

### Map physical and organisational entry points

The award process is public, so the contractor's identity becomes public with it. From there an observer can name the external organisations authorised to enter secured network rooms, confirm where maintenance access into Defence environments is structurally permitted, and identify which firms sit at the boundary between civilian industry and military systems. The result is a map of legitimate entry pathways into sensitive environments.

### Infer access conditions and control frameworks

The reference to ABDO 2019 names the exact security baseline the contractor is held to: procedural conditions for access approval, the vetting and constraints applied to external personnel, and the formalised control regime around classified work. The full ABDO document is partially restricted, but its existence and applicability are anchored by the public tender. That is enough to model how access is granted, governed, and where it can be delayed or contested.

### Identify enforcement structure and escalation points

Naming the MIVD's Industrial Security unit identifies the body that validates compliance, the place enforcement authority sits in the process, and roughly how deviations would be detected and escalated. From outside the organisation, this is enough to reason about who has visibility into contractor activity and where oversight pressure points lie.

### Build a contractor-to-system dependency map

Procurement data on its own makes it possible to map which companies maintain access to sensitive environments, infer which systems depend on external maintenance cycles, and identify where operational continuity rests on third-party availability. The frame stops being "contract" and becomes "dependency relationship between state systems and private actors".

For the structural argument and where this fits into policy, see [Strategic frame](strategy.md).