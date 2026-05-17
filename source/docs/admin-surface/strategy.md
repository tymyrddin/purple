# Strategic frame

The three
cases, [Radarstation Herwijnen](herwijnen.md), [Maintenance tender for secured network rooms](netwerkruimtes.md), [Defensie Pijpleiding Organisatie (DPO) fuel pipeline](dpo.md)
and the [proof-of-concept design SOS](sos.md), all point at the same finding.
None concerns leaked information. None concerns intrusion. Each is a record of how routine, individually justified
publication, when read collectively, reduces uncertainty about critical infrastructure to a degree the publishers did
not intend.

No document on those pages is sensitive in the classical sense. Each public source existed for legitimate reasons: legal
transparency, environmental and water management regulation, infrastructure coordination, public accountability. Read
together they identify operationally important nodes, expose dependency chains and constraints, and allow partial
reconstruction of system behaviour from public data alone.

In security terms the problem space shifts from an unknown structure to a partially modelled operational system. That is
what does the work, because it lowers the cost of finding the places where resilience depends on assumption rather than
redundancy. The shift is a structural effect of distributed publication, legitimate transparency requirements,
geospatially structured datasets, and a near-complete absence of aggregation awareness across domains. Each layer is
rational on its own. Together they form something more legible than any layer intended.

## Policy gap

A dependencies classification guide, naming which categories of routine public data carry aggregation risk for sensitive
sites, does not appear to exist. It is unclear whether one is in development. Existing classification machinery treats
individual documents as the unit of decision; aggregation across documents is not on its checklist. Closing the gap is
partly a writing exercise (what would such a guide actually say?) and partly an institutional one (whose remit is it?).
Both are genuinely hard. Neither is being done at the depth the cases suggest is needed.

## Framework gap

Standard security frameworks focus on internal IT and physical perimeters. They do not cover
correlated public-data exposure, because the risk does not present at the perimeter. It presents in the publication
choices of organisations that may not consider themselves part of the security stack at all: planning offices, water
boards, procurement aggregators.

An "administrative attack surface" control family, sitting alongside the existing technical and physical families, is
one shape a response could take. It would name the publication systems involved, define a correlation-risk review for
them, and require the cross-domain coordination needed to make that review meaningful. Standing this up is non-trivial,
partly because the parties whose publications carry the most risk do not, in current frame, have a security mandate.

## Tooling, with a caveat

AI is good at finding correlations at scale; that part is solved. A proof-of-concept design for what such a system could
look like, using Dutch public sources, is sketched in [SOS](sos.md). A working prototype is technically feasible in
weeks.

The harder problem is interpretation. A correlation engine flags candidate dependency chains; it does not say which ones
are a problem, which are known and accepted, and which the relevant institutions can or want to act on. That judgement
is human, organisational, and political. The tooling does not remove it; it changes where it lands.

## The organisational layer

Treating this purely as a policy gap and a tooling problem misses the part that actually keeps it stuck. The reason
classification regimes do not catch aggregation risk is not chiefly technical. It is organisational, and the foundations
section of this collection has language for it.

### Three domains, not one

Gerald Weinberg's [three domains of problem solving](../foundations/problem-solving/three-domains.md) are rational (
facts, analysis, tools), emotional (fear, trust, ego, psychological safety), and political (influence, authority, hidden
agendas). Most stuck problems are stuck in the second or third while everyone keeps investing in the first.

The rational case for an aggregation-aware classification regime is easy to make and has been made. The political layer
is where it sits: turf between the Ministry of Defence, the MIVD, gemeenten, water authorities, and network operators,
none of whom currently own the cross-domain question. The emotional layer is the discomfort of being seen as adversarial
inside an institution whose default posture is defensive. Hiring systems thinkers rather than compliance auditors, is
a right instinct in the wrong domain. The people are findable. The system that would have to host them is the harder
bet.

### Models, errors, and the same incident in slightly different clothes

The [systems, models, and errors frame](../foundations/system-effectiveness/core-triad.md) treats recurring
errors as evidence of model failure. When the same class of incident appears on a quarterly cycle, suppressing the
symptom does not fix the model; only correcting the model does. Each "this document was wrongly published" episode that
ends in a redaction or a takedown is a symptom-fix. The recurrence is the system telling you that the underlying model
treats individual documents as the unit of decision while the actual risk is composed across documents. Until the model
is updated, the redactions will keep arriving in slightly different clothes.

### Survival stances under classification pressure

Satir's [communication patterns under stress](../foundations/organisational-development/satir-core.md) name
four survival stances: placating, blaming, computing, and distracting. In classified-handling cultures, blaming and
computing tend to dominate. Blaming directs fault outward (the journalist, the activist, the contractor) rather than at
the publication system that produced the aggregation. Computing retreats into procedure (the document was correctly
handled under regulation X) rather than engaging with what was actually exposed. Both are honest survival behaviours,
and both block the conversation that would change the model. Naming the stance is the cheapest move available.

## Demands on practitioners

The work in this section can be done by anyone with patience, technical curiosity, and the willingness to read boring
documents alongside each other. It does not require classified access. It does not require offensive tooling. It
requires systems literacy and the social licence to apply it across domains that do not normally talk to each other.

The uncomfortable possibility that closes the [broomstick essay](https://broomstick.tymyrddin.dev/posts/perhaps/), that
institutions need this kind of thinking and may not always like the people who do it, is the institutional version of
the same survival pattern. The job is not to prove institutions wrong. It is to make the work legible enough that the
rational, emotional, and political domains can be engaged at once, instead of pretending only the first is doing the
work.

## Concrete moves

The three-domain frame has a way of collapsing back into "we wrote a good analysis and nobody acted." A few moves keep
that from happening:

- Pair the analysis with a venue. A correlation finding accompanied by "here is the working group that would have to
  act on this" lands differently from one that just says "here is what we found." If no such group exists, building it
  is part of the work, not preparatory to it.
- Name the political layer in the document itself. A reader can react to a stated political fact. A reader forced to
  infer one tends to react to the analysis instead.
- Pre-name the survival stances. "This is likely to read as an attack on the publication system. It is not, and here is
  why." Naming what is about to happen tends to defuse the reaction it predicts.

None of this removes the discomfort. The point is to make the discomfort discussable rather than letting it route the
response.

## Related

* [The Broomstick Brief: The administrative attack surface](https://broomstick.tymyrddin.dev/posts/perhaps/)