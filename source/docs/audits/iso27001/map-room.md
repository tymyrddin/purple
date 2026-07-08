# The map room

![Map room](/_static/images/map-room.png)

ISO/IEC 27001, Clauses 4 and 5: context, interested parties, scope, and leadership.

Every great climb begins with an argument about which mountain to attempt. Before anyone laces up their boots,
the expedition team needs to agree on the target, understand the terrain, know who will celebrate success or
complain if things go wrong, and ensure the expedition sponsor is genuinely committed. This is where the map
room comes in.

## Understanding the terrain

Clause 4.1 asks for an analysis of the external and internal issues that can affect the information security
management system. In plain terms: know the environment before setting out. Risks cannot be assessed properly
in an unexamined context; that is preparing for a summer hike when the season calls for winter mountaineering.

The external terrain covers five familiar weather systems, plus a new one:

* Regulatory and legal: which laws apply, how enforcement is shifting, which jurisdictions are involved.
* Market: customer security expectations, and what competitors certify against.
* Technological: cloud adoption, the current threat picture, dependencies on connectivity and power.
* Social: talent availability, remote and hybrid working patterns.
* Economic: budget pressure, cyber insurance requirements.
* Climate, made explicit by the 2024 amendment: flooded server rooms and heat-stricken data centres are now officially part of the conversation, not optional extras.

The internal terrain is the organisation itself:

* Structure, and how decisions actually get made.
* Culture, and the real attitude to risk and to mistakes.
* Resources and current security maturity.
* Strategic objectives and the initiatives in flight.
* The information assets held, and where they live.
* Existing commitments: contracts, prior certifications.

The practical approach is unexciting and works: gather perspectives beyond IT through workshops and interviews
(SWOT and PESTLE earn their keep here), document the issues and how they influence scope, risk assessment, and
control selection, and review at least annually or when something major changes.

A context document captures what the organisation believes about its environment. Those beliefs are
assumptions, and some will be wrong. The analysis may describe a stable regulatory environment while
enforcement patterns have quietly shifted; the culture assessment may describe security as a core value while
the incident log tells a different story.

Treat the context document as a set of propositions to test over time, not settled background information.
When a risk materialises that the context analysis did not anticipate, that is not bad luck; it is evidence
that a model was wrong, and the review cycle is the mechanism for correcting it.

## Knowing who cares

Clause 4.2 asks who has an interest in the ISMS and what they expect from it: the people who will cheer the
expedition on, fund it, use its results, or file a complaint if it falls off the mountain. Their requirements
shape the controls, their concerns become risk priorities, and some of them can impose obligations with teeth.

Externally that usually means regulators (demonstrable compliance, incident reporting), customers
(certifications, questionnaires, notification commitments), shareholders and investors (risk visibility,
governance), suppliers and partners, the certification body itself, and insurers, who increasingly behave like
auditors with premiums.

Internally: top management, who need risk visibility and justified resource requests; process and system
owners, whose operations the controls land on; IT, HR, and the security function itself; and employees, who
have to live with whatever gets designed and will route around it if it is unusable. Works councils may hold
consultation rights, particularly around monitoring.

The requirements worth documenting are both the explicit kind (contracts, regulations) and the implicit kind
(expectations, norms), together with what happens if they are not met. Parties and requirements change, so the
list gets reviewed, not framed.

## Choosing the right mountain

Clause 4.3 is where the argument finally ends: defining the scope of the ISMS, the official boundary of which
systems, processes, locations, and data fall under it. Over-scoping means climbing several mountains at once;
under-scoping means ignoring the avalanche danger on the slope actually being climbed.

A scope statement covers organisational boundaries (locations, departments, legal entities), products and
services with the information they process, the technology estate, and the interfaces where the boundary meets
suppliers, customers, and cloud providers. Three approaches recur: minimalist (core business first, expand
later), comprehensive (everything, at a price), and the pragmatic middle that many organisations land on, with
a documented expansion plan.

Exclusions need justification. Defensible ones: genuinely not applicable, managed by a third party under
contract with its own certification, outside organisational control, or staged for later inclusion with a
date. The ones that fail audits: too difficult to secure, no budget, legacy, or "only used internally". None
of those makes a risk go away.

A scope statement describes intent. The actual ISMS boundary is wherever information flows, systems connect,
and third parties handle data, and those may not match the diagram. A supplier assumed to be out of scope may
have direct database access. A development environment assumed to be isolated may share credentials with
production. A cloud service adopted by one team may process customer data that the scope document does not
mention.

Before finalising scope, tracing actual data flows and access paths against what the architecture documents
claim turns those gaps into explicit decisions rather than audit findings.

Scope also evolves: new services, new offices, acquisitions, exclusions that stop being justified. A scope
change ripples through the risk assessment, the Statement of Applicability, and the certification body's audit
plan, which is a reason to design the initial scope with the foreseeable expansion in mind.

## The expedition sponsor

Clause 5 places accountability with top management: fund the climb, endorse the route, ensure the team has
oxygen, and demonstrate that information security carries strategic weight. Day-to-day ISMS work is delegated;
accountability is not. Without genuine support, the expedition never leaves base camp: security becomes "IT's
problem", resources are not allocated, and certification attempts fail.

The commitments have specific shapes:

* A policy appropriate to the organisation, providing a framework for measurable objectives, committing to applicable requirements and continual improvement, documented, communicated, and actually reviewed.
* Roles, responsibilities, and authorities assigned and understood, from the CISO or security manager through process owners to every member of staff, with the authority matching the responsibility.
* Integration into business processes, so security appears in strategic decisions and project planning rather than after them.
* Resources: budget, skilled people, and time, allocated before being begged for.

The warning signs of a sponsor in name only are recognisable:

* Budget requests consistently cut.
* The security manager overruled, or unable to enforce policy.
* Management reviews attended by delegates without decision authority.
* Policies bypassed "for business reasons" without risk acceptance.
* No consequences for repeated violations.

Where these patterns persist, ISMS failure and certification difficulty usually follow.

The distinction between stated and observable commitment is consequential for the ISMS. A signed policy is
evidence of intent. Observable commitment appears in resource allocation decisions when security competes with
other priorities, in whether the security manager has actual authority to stop activities that create
unacceptable risk, and in how the organisation responds to repeated policy violations.

When the documented commitment pattern diverges from the observed behaviour pattern, that divergence is itself
a finding. It belongs in the management review, not just the warning signs list.

## Output

Leaving the map room, four foundational questions have answers, in writing:

* What environment are we operating in? Context documented, climate included, review scheduled.
* Who cares? Interested parties and their requirements identified, mapped to controls.
* What exactly is being protected? Scope defined, exclusions justified, boundary checked against observed data flows.
* Who is accountable and committed? Policy approved and communicated, roles assigned with authority, resources allocated.

These outputs feed everything that follows. Context tells the [risk tent](risk-tent.md) which risks are
plausible, interested parties define what acceptable risk means, scope defines what gets assessed, and
leadership determines what can be done about any of it.

## Related

* [NIS2 Exploring and planning a crossing](../nis2/explore.md)
* [ISO 22301 The floor walk](../iso22301/floor-walk.md)
* [Scope definition](../supportive/scope-definition.md)
* [Picking the route](../picking-the-route.md)

*Last updated: 4 July 2026*
