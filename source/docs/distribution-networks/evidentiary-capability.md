# Evidentiary capability

Under NIS2, an operator of an essential service files an early warning within twenty-four hours of becoming
aware of a significant incident. Article 23(4)(a) asks that the warning indicate whether the incident is
suspected to be caused by an unlawful or malicious act. The bar is suspicion, not proof, and "unknown" is a
permitted answer; the fuller account follows in the seventy-two hour notification and the final report. The
Dutch transposition, the Cyberbeveiligingswet, carries the obligation into national law, with a commencement
date still to be confirmed.

The early warning rests on something the text leaves unspoken. To say whether malice is suspected, the
operator has to be able to tell a malicious change from its legitimate twin, and it has to do so from the
record it kept and can retrieve inside the day. Evidentiary capability is the name for that precondition:
whether the estate's own evidence can support the determination the law asks for. It is a property of the
record rather than of any incident, and it is fixed before anything happens. An operator can hold it or lack
it on a quiet Tuesday, with no attacker in sight.

That framing sits underneath [observable semantics](observable-semantics/index.rst) rather than beside it.
Observable semantics catalogues what evidence a working estate emits and what tampering disturbs; operating
context and the threat landscape establish the estate and the moves against it. Evidentiary capability is the
question they make askable: given this record, is the Article 23 determination reachable, or is the honest
answer already "unknown" before the first packet?

## Neighbours that answer a different question

The direction is easy to mistake for tools that already exist, so it helps to place it against them.

Detection products, the Nozomi and Claroty class of passive OT monitoring, watch the wire and raise an alert
when traffic departs from a learned baseline. They answer "is something happening now". Evidentiary
capability asks a prior and quieter question: if something did happen, would the record afterwards let anyone
tell what kind of thing it was. A site can run detection well and still be unable to distinguish an insider's
authorised-looking change from routine maintenance once the alert has aged into an investigation.

Cyber ranges and red-team engagements exercise people and defences against a live adversary. They answer "can
we withstand this attack". They rarely measure whether the estate's ordinary record, afterwards, would have
supported the malice-or-not call under the twenty-four hour clock, because the range is instrumented far
beyond anything a production estate retains.

Logging-maturity assessments, the SIEM-coverage and log-retention audits familiar from IT security, count
sources and check retention windows. Their question is whether enough is being collected. Evidentiary capability is
downstream of coverage: two estates with identical log inventories can differ sharply in whether those logs,
taken together, separate the benign explanations from the malicious one for a given class of incident.
Coverage is necessary and not sufficient; the discrimination is the thing being measured.

The closest neighbour is forensic readiness, the older discipline of arranging in advance to collect and
preserve evidence that will stand up later. Evidentiary capability shares its instinct and narrows it: not
"can we preserve evidence" but "can the evidence we preserve separate malice from its legitimate twins",
computed as a property of the architecture rather than assessed by a reviewer's judgement. The novelty is
narrow, and better named than dressed up: the discrimination among competing benign explanations, and the treatment
of ordinary operational disorder as the substrate the determination has to survive.

*Last updated: 12 July 2026*
