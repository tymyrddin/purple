# Strategic frame

The three
cases, [Radarstation Herwijnen](https://green.tymyrddin.dev/docs/threat-models/infrastructure-aggregation/herwijnen/), [Maintenance tender for secured network rooms](https://green.tymyrddin.dev/docs/threat-models/infrastructure-aggregation/netwerkruimtes/), [Defensie Pijpleiding Organisatie (DPO) fuel pipeline](https://green.tymyrddin.dev/docs/threat-models/infrastructure-aggregation/dpo/)
and the [proof-of-concept design SOS](https://green.tymyrddin.dev/docs/threat-models/infrastructure-aggregation/sos/), all point at the same finding.
None concerns leaked information. None concerns intrusion. Each is a record of how routine, individually justified
publication, when read collectively, reduces uncertainty about critical infrastructure further than the publishers appear
to have intended.

No information on those pages is sensitive in the classical sense. Each public source existed for legitimate reasons:
legal transparency, environmental and water management regulation, infrastructure coordination, public accountability.
Read together they identify operationally important nodes, expose dependency chains and constraints, and allow partial
reconstruction of system behaviour from public data alone.

In security terms, the target stops being opaque. It becomes a system that can be partly modelled from public data,
which lowers the cost of finding where resilience rests on assumption rather than redundancy. The shift appears to be
structural: distributed publication, legitimate transparency requirements, geospatially structured datasets, and a
widespread absence of aggregation awareness across domains. Each layer is
rational on its own. Together they form something more legible than any layer intended.

## Policy gap

A dependencies classification guide, naming which categories of routine public data carry aggregation risk for sensitive
sites, does not appear to exist. It is unclear whether one is in development. Political discussion of it is scarce, save a single article in the NRC. The article follows an ex-military technician who pieces together
vulnerabilities in Dutch defence infrastructure simply by combining publicly available information. Not hacking.
Not breaching. Just looking. Correlating. Thinking operationally. Common sense.

Existing classification machinery seems to treat individual documents as the unit of decision; aggregation across
documents is not on its checklist. Closing the gap is partly a writing exercise (what would such a guide actually say?)
and partly an institutional one (whose remit is it?). Both are genuinely hard questions to find answers for. Neither
is being done at the depth the cases suggest is needed.

## Framework gap

Standard security frameworks tend to focus on internal IT and physical perimeters. They rarely cover
correlated public-data exposure, because the risk does not present at the perimeter. It presents in the publication
choices of organisations that may not consider themselves part of the security stack at all: planning offices, water
boards, procurement aggregators.

An "administrative attack surface" control family, sitting alongside the existing technical and physical families, is
one shape a response could take. It would name the publication systems involved, define a correlation-risk review for
them, and require the cross-domain coordination needed to make that review meaningful. Standing this up is non-trivial,
partly because the parties whose publications carry the most risk usually do not have a security mandate.

## Tooling, with a caveat

AI is good at finding correlations at scale; that part is largely solved. A proof-of-concept design for what such a
system could look like, using Dutch public sources, is sketched in [SOS](https://green.tymyrddin.dev/docs/threat-models/infrastructure-aggregation/sos/). A working prototype could be built in a
matter of weeks.

The harder problem is interpretation. A correlation engine flags candidate dependency chains; it does not say which ones
are a problem, which are known and accepted, and which the relevant institutions can or want to act on. That judgement
is human, organisational, and political. The tooling does not remove it; it changes where it lands.

## The organisational layer

Treating this purely as a policy gap and a tooling problem misses the part that could keep it stuck. The reason
classification regimes do not catch aggregation risk is seldom chiefly technical. It is organisational, and the
foundations section of this collection has language for it.

### Three domains, not one

The rational case for an aggregation-aware classification regime is easy to make, and has been made. If it stays stuck,
this suggests the block sits elsewhere. Reading
[three layers rather than one](../foundations/problem-solving/three-domains.md), rational, emotional, political,
the problem would likely sit in the latter two.

The political layer is turf: the Ministry of Defence, the MIVD, gemeenten, water authorities, and network operators,
none of whom currently own the cross-domain question.

The emotional layer is the discomfort of being seen as adversarial inside an institution whose default posture is
defensive. Hiring systems thinkers rather than compliance auditors is a right instinct in the wrong domain. The people
are findable. The system that would have to host them is the harder bet.

### Models, errors, and the same incident in slightly different clothes

The same class of incident keeps arriving on a quarterly cycle: a document ruled wrongly published, then redacted or
taken down. Through the [systems, models, and errors frame](../foundations/system-effectiveness/core-triad.md), a
recurring error like that reads as model failure, not as something a fresh redaction fixes. Each takedown is a
symptom-fix. The model underneath still treats individual documents as the unit of decision, while the actual risk is
composed across documents. Until that model is updated, the redactions are likely to keep arriving in slightly different
clothes.

### Survival stances under classification pressure

Raise aggregation risk inside a classified-handling culture and the response tends to fall into two grooves.
[Satir's communication patterns under stress](../foundations/organisational-development/satir-core.md) name them blaming
and computing. Blaming directs fault at the journalist, the activist, the contractor, rather than at
the publication system that produced the aggregation. Computing retreats into procedure (the document was correctly
handled under regulation X) rather than engaging with what was actually exposed. Both are honest survival behaviours,
and both block the conversation that would change the model. Naming the stance is often the cheapest move available.

## Demands on practitioners

Because the block is organisational rather than technical, the people who can shift it are not the ones the technical
framing points to. The work in this section can be done by anyone with patience, technical curiosity, and the willingness
to read boring documents alongside each other. It does not require classified access. It does not require offensive tooling. It
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
