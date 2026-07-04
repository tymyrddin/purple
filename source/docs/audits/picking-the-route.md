# Picking the route

Four journeys live in this section: a mountain, a river, a fortress, and a factory. Choosing which to walk, and
in what order, is a strategic decision that rarely gets made strategically. In practice, it is made by
whichever standard arrives first: a customer questionnaire, a regulator's letter, a consultant with a favourite
slide deck. The arrival order of paperwork is not a strategy. (These pages are, admittedly, also a consultant's
slide deck. At least this one names the routes it is not selling.)

## What each route is for

* The [ISO 27001 expedition](iso27001/index.rst) builds a general-purpose information security management system and
  ends in a certificate. Organisations climb it for market access at least as often as for security; both are legitimate
  reasons, and it helps to be honest internally about which one is paying for the trip.
* The [NIS2 crossing](nis2/index.rst) is law. An entity in scope does not choose whether to cross, only how well.
  Deadlines, mandatory reporting timelines, and personal liability for management bodies remove most of the discretion
  the other routes allow.
* The [IEC 62443 fortress](iec62443/index.rst) is for estates where the crown jewels are operational: plants, grids,
  water, anything where a compromised controller is a physical event.
* The [ISO 22301 factory](iso22301/index.rst) is for organisations where downtime is the risk that keeps the board
  awake. It cares less about who broke the line than about how fast the line restarts.

They overlap heavily, which is both the good news and the trap. Risk assessment, asset knowledge, incident
response, and evidence discipline recur on every route. Walked in a sensible order, each journey inherits from
the last. Walked carelessly, the same ground gets surveyed four times by four different consultancies.

## Routes not drawn on this map

The four journeys here are the ones with full playbooks, not the whole atlas. Audits come in more flavours than
standards do. First-party, the organisation checking itself; second-party, a customer or supplier auditing
across a contract, increasingly common as supply chain clauses propagate; third-party, a certification body;
and supervisory, a regulator with statutory powers, of which the NIS2 crossing is the local example. 

Beyond
this section's four sit others an executive is likely to meet: SOC 2 where customers, often American ones, ask
for an assurance report rather than a certificate; DORA for financial entities, with its own ICT risk and
resilience testing expectations; data protection audits under GDPR; sector schemes such as TISAX in automotive.

Penetration tests and red team exercises are not audits at all, though they produce the effectiveness evidence
audits increasingly want to see. And a [rapid resilience review](../resilience/rapid-resilience-review.md) does
some of an audit's sensing without the ceremony. The choosing logic is the same everywhere: what the obligation
actually is, who is asking, and who will carry the work.

## Orders that work, orders that punish

Law goes first when law applies. A NIS2 deadline outranks a certification ambition, and supervisory authorities
are less patient than certification bodies.

For the rest, an ISO 27001 spine tends to make the others cheaper. Its management system, risk register, and
evidence habits map heavily onto NIS2's mandatory measures, so the crossing becomes an overlay: reporting
obligations, supply chain formalisation, governance documentation. Building in the other direction, a scrambled
NIS2 compliance push followed by a certification attempt, usually means redoing the governance layer that the
scramble skipped.

On an OT estate, the fortress and the factory pair naturally: one secures the estate, the other keeps it
running, and they share an asset survey and most of a threat register. Doing either without the other leaves a
plant that is defended but brittle, or resilient but open.

And one at a time. A management system is carried by attention, not by documents, and attention does not shard
well across two simultaneous certification programmes.

## Failure modes worth naming

* Certificate collecting. Audits acquired as trophies, each with its own binder, none changing how anyone works. The
  wall gets fuller, the organisation does not get safer, and everyone quietly knows it.
* The one exhausted person. Every standard in this section assumes an organisation carries it. When a single coordinator
  carries all of it, the programme's real single point of failure is on the payroll, and no business continuity plan
  mentions them.
* The consultant's favourite. The standard chosen because the adviser knows it well, rather than because the risk asks
  for it. A fluent guide up the wrong mountain is still the wrong mountain.
* The tidy scope. Certifying the well-behaved corner of the estate, headquarters and its IT, while the factory floor
  stays feral. The certificate is real; its relevance is not. Scoping decisions deserve the scrutiny that usually goes
  to control decisions, and [scope definition](supportive/scope-definition.md) is where that scrutiny lives.

## The deciding constraint

None of the above is technical. Which route, what order, and how fast are questions about the organisation:
who will carry the work, how much change it can absorb while doing its actual job, and whether leadership
attention will still be there in year two, when the novelty is gone and the surveillance audits begin. The
standards themselves assume this layer exists and works; the [second foundation](../asimov/second-foundation.md)
is a name for why that assumption is the one most worth checking first. An organisation that picks its route by
its own carrying capacity, rather than by the brochure, tends to arrive.
