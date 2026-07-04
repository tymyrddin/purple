# Exploring and planning a crossing

![Explore](/_static/images/explore.png)

NIS2, Articles 2 and 3 with Annexes I and II: scope, current position, and the people who will carry the crossing.

Before entering the water, three questions want answers. Is the crossing mandatory? What does the journey
require? What resources exist to make it? Getting scope wrong means either wasting effort on unnecessary
compliance or facing penalties for ignoring mandatory obligations.

## Scope

NIS2 applies to "essential" and "important" entities in specific sectors. The distinction is consequential:
essential entities face stricter supervision and higher penalties.

Essential entities are the critical core: energy, transport, banking, healthcare, drinking water, digital
infrastructure, ICT management, public administration, space. Electricity grids and hospitals, cloud providers
and airports, managed service providers and government systems. If it breaks, society notices immediately.

Important entities are significant but contained: postal services, waste management, chemicals, food
production, manufacturing, online marketplaces, search engines, research organisations. Disruption has more
regional than systemic impact.

Size is a factor, but not the whole story. Medium and large enterprises (50 or more employees, or over €50M
turnover) typically fall in scope. Small and micro companies usually get a pass unless they are the sole
provider of something critical or national rules say otherwise. The classic edge case: a tiny software company
managing security for banks may be in scope regardless of size.

Five scope questions that come up in practice:

"We serve banks, but we're tiny: are we really in scope?"
If the work involves their security-critical systems as a managed service provider, possibly yes.

"We manufacture electronics: general or critical?"
Depends on what is made and who uses it. Medical devices? Probably in. Consumer gadgets? Probably out.

"Our clinic has 8 people: surely we're exempt?"
Healthcare is essential, but size exemptions may apply unless the clinic is the only provider in its area.

"We're an online B2B platform: does 'marketplace' include us?"
Probably not. NIS2 typically means consumer-facing platforms connecting multiple sellers.

"We use AWS: does that make us a cloud provider?"
No, but AWS becomes part of the supply chain obligations if the organisation is in scope for other reasons.

Grey areas remain after all of that. The national supervisory authority exists to be asked; documenting the
reasoning either way costs an afternoon, and regulators would rather clarify early than penalise later.

## Current position

Scope confirmed, the next job is understanding what is already there before building anything new.

The scope in one paragraph. A simple statement covering sector, size, classification, services, authorities,
and deadline. For example: *"Acme Logistics operates 120 trucks across NL/BE/DE. 180 employees, €35M turnover.
Important entity in transport (road). Lead authority: Dutch regulator. Deadline: October 2024."* One paragraph
forces clarity. A scope that cannot be written down is a scope not yet understood.

The landscape in three lists:

* Critical systems: what IT keeps the organisation running, where the single points of failure sit, what breaks operations immediately if compromised.
* Current security: policies, a security officer, controls like MFA, monitoring, backups, an incident response plan, certifications. What actually exists, not what is supposed to exist.
* Supply chain: the ten to twenty critical suppliers, who has system access, who could break the organisation by failing.

The gaps in plain language. No MFA on critical systems. No monitoring. Untested backups. No incident plan. No
training programme. One person with all the access. Systems unpatched for months. Suppliers never assessed.
Documentation that does not exist. The honest version of this list is the only useful one, and it is rarely
flattering.

The maturity in eight scores. A one-to-five self-rating on governance, risk management, policies, technical
controls, incident response, business continuity, supply chain security, and awareness, where 1 means nothing
exists and 5 means mature and validated. Mostly ones and twos points at 12 to 24 months of work. Mostly threes
and fours, 9 to 18 months of gap-filling. Mostly fives means either genuine readiness or overconfidence, and
external validation settles which.

Validation means testing, not attestation. A 5 on incident response backed by tabletop exercises and a
penetration test is different evidence from a 5 backed by documentation being in place.

The timeline in months, worked backward from the member state's deadline. High maturity (an ISO 27001
certificate, say) leaves 6 to 12 months of NIS2-specific work: incident reporting, supply chain formalisation,
governance documentation. A deadline under 12 months combined with low scores is a resource problem, and the
honest responses are external help, ruthless prioritisation, and documented reasoning a regulator can follow.

## Stakeholders

NIS2 makes security a board-level governance issue with personal liability. It stops being an IT project and
becomes an organisational one, which changes who needs to be in the room.

The board carries consequences: personal liability in some member states, penalties up to €10M or 2% of global
turnover, mandatory approval and oversight duties that cannot be delegated away. A board briefing covering
scope, gaps, costs, and timeline, with budget approval and quarterly reporting minuted, is evidence regulators
ask for. Boards tend to ask the same five questions: what does this cost, what happens if we don't, how do we
compare, what are our biggest risks, who is accountable. Arriving with answers shortens the meeting.

IT and security implement the technical reality, and know what is possible versus theoretical. The predictable
pushback ("we're already ISO 27001 compliant", "no budget", "this will slow everything down", "we're
understaffed") each has an answer: close but gaps exist, escalate because it is legally mandatory, find
proportionate approaches, prioritise or get help.

The rest of the room each carry a piece. Operations owns continuity and knows what actually keeps services
running. Legal and compliance track national implementation variations, supplier contracts, reporting
procedures, and liability. Procurement operationalises supply chain security through requirements,
questionnaires, and contract amendments. HR builds the culture: awareness training, onboarding and
offboarding, management training.

Structure holds it together: an executive sponsor with authority and board reporting, a programme owner for
day-to-day coordination, a core team across functions, and a governance rhythm that makes clear who decides,
who implements, and who gets informed.

## Output

By the end of this stage: scope clarity written in one paragraph, a current-state picture (systems inventory,
controls summary, maturity scores, supplier list, gaps), stakeholder alignment with the board briefed and
budget approved, a basic roadmap with milestones, and a governance structure with a named sponsor and owner.
This is the launch point. Rushed past, the current finds the raft without a map, a crew, or a destination.

## Related

* [ISO 27001 The map room](../iso27001/map-room.md)
* [Scope definition](../supportive/scope-definition.md)
* [Picking the route](../picking-the-route.md)
