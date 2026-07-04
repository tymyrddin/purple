# The climb

![Mountain](/_static/images/mountain.png)

ISO/IEC 27001, Clauses 7 and 8: resources, competence, awareness, communication, documentation, and operation.

The route was [identified in the risk tent](risk-tent.md), the gear selected and documented in
[the gear depot](gear-depot.md). Now comes the actual climb, the operational execution that brings the ISMS to
life. A mountain expedition is only as good as its preparation: the most meticulous route plan in the world
goes nowhere if half the team forgot their boots. In ISO 27001 terms, the climb is about resources, competence,
awareness, communication, and documentation, the operational backbone that keeps the expedition safe and moving
upward.

## Resources for the climb

Clause 7.1 formalises what every climber already knows: go under-resourced, and the summit stays theoretical.
The resource plan covers five things:

* People: dedicated security staff or existing roles expanded, with the expertise to match.
* Time: hours genuinely allocated for risk reviews, incident response, training, and audits. Security work does not happen in spare time.
* Money: tools, training, consultants, testing, certification, and the ongoing costs after the initial ones.
* Information: threat intelligence, regulatory requirements, lessons from incidents in the sector.
* Equipment: SIEM, MDM, scanners, and the infrastructure they run on.

Resources adapt to the terrain: growth, new legal constraints, or incidents change what the climb needs. The
warning signs of a base camp too small for the mountain are recognisable: security tasks consistently delayed,
one person as single point of failure ("only Sarah knows how the firewall works"), incidents uninvestigated
for lack of time, training postponed quarter after quarter, documentation ageing, staff burning out, and
controls failing with nobody free to fix them.

## Competence and awareness

Clauses 7.2 and 7.3: a rope team depends on everyone knowing their knots. Competence is having the skills and
knowledge to do the job; training is how competence gets built; awareness is everyone understanding their role
in security and the consequences of their actions, whether or not they are specialists.

The distinction is relevant for evidence. Competence is not evidenced by a course completion certificate; it is
evidenced by what someone does in a realistic situation. A system administrator who has completed firewall
training has attended training; one who configures a firewall correctly under realistic conditions, with
incomplete documentation and time pressure, has demonstrated competence.

Awareness follows the same logic. It is not evidenced by a quiz score but by what people do when they encounter
an actual phishing attempt or notice something unusual. Designing the programme around observable outcomes
rather than training delivery shifts the metric from attendance to behaviour.

[CTF and roleplay exercises](../../foundations/organisational-development/roleplay.md) apply this principle
directly to technical competence: participants work through structured challenges with immediate feedback on
success or failure. The format is self-correcting by design: the flag is either captured or it isn't, and the
environment is realistic enough to produce observable behaviour rather than recalled procedure. A
technically-oriented team member who completes a network-attack scenario in a CTF has produced better
competence evidence than one who passed an examination on the same topic.

Awareness that changes behaviour works best when the learning environment is close to the actual work context.
A short briefing on a threat that appeared in the organisation's own sector that week works better than an
hour on abstract policy, because it is specific, timely, and actionable. Simulations, tabletops, and
scenario-based challenges work for the same reason: they are self-correcting. The participant experiences the
consequence of a wrong choice in a safe environment, which is more durable than being told what the right
choice is.

A logistics company running five-minute campfire briefings before shifts, built on the phishing that actually
arrived that month, watched simulated click rates drop from 18% to 5% in three months. Nobody there can quote
an ISO clause. The debrief, where people articulate what they noticed and what they would do differently, is
where the awareness is actually formed, and what the group decided there is more informative evidence than an
attendance record.

## Communication on the mountain

Clause 7.4: communication is the lifeline of any climb, and a garbled message or a missing update can be the
difference between safe progress and disaster. The working principles are unglamorous. Transparency within
security constraints. Messages tailored to the audience: technical teams need different detail than the board
or partners. Accuracy verified before sending. Promptness, especially during incidents, because silence breeds
rumours. And plain language, because a message staff do not understand might as well not have been sent.

Internal messages reach every climber who needs them; external ones reassure partners, customers, and
regulators without revealing more than is safe.

## The expedition logbook

Clauses 7.5.1 to 7.5.3: every expedition keeps a log of what was packed, what was repaired, and what went
wrong. ISMS documentation follows the same principle. Documents are identified (title, version, date, author),
controlled (reviewed, approved, versioned), accessible to authorised people when needed and protected
otherwise, and retained or disposed of with intent. The scale differs, a solo climber needs less paperwork
than a national expedition, but both need to know what decisions were made, when, and why.

The recurring documentation failures are all avoidable: documents nobody reads, policies contradicting current
practice, files hidden where nobody can find them, no version control, over-documentation that buries the
critical in the bureaucratic, and under-documentation that leaves due diligence unprovable. The test of a
healthy logbook is the regulator's question answered in minutes: who approved this policy change, when, and
with what follow-through.

## Operational planning and control

Clause 8 is the "Do" phase of the plan-do-check-act cycle, where planning becomes reality. The operational
duties: establish and monitor processes against the security objectives, keep the
[risk register](../../risk-management/risk-register.md) alive with regular reassessment, treat risks as the
Statement of Applicability documents, and record the results.

Reassessment has natural triggers beyond the annual habit: new systems and services, mergers, significant
incidents, regulatory change, supplier change, control changes that shift the risk profile elsewhere, and
sector-wide events like ransomware campaigns or supply chain compromises.

The climb itself produces evidence about which assumptions were right. When new controls arrive, the
organisation experiences increased friction before any benefit is felt. People will find workarounds, not
because they are obstructive but because the control's model does not yet fit their workflow.

A control that is consistently bypassed (a VPN disabled before working, an approval process that accumulates
rubber-stamp sign-offs without review) is not primarily a compliance failure. It is a signal that an assumption
does not match the operational environment. The question to ask before escalating enforcement is whether the
underlying model still holds. Treating bypass patterns as system information rather than individual
non-compliance is what separates a maturing ISMS from one that accumulates workarounds beneath a clean
compliance surface.

Every significant change to controls or processes goes through a disruption phase before reaching a new stable
state. [This is structural, not failure](../../foundations/organisational-development/satir-change-model.md).
When MFA is introduced, the first weeks will generate more helpdesk tickets, more complaints, and more
workarounds than the final state will. The disruption has predictable characteristics: people agree in
meetings and find workarounds in practice; performance metrics dip before they improve; early adopters grow
frustrated with everyone else. None of this is evidence that the control is wrong or the rollout has failed.

What helps: acknowledging the dip explicitly, structured support with a named contact per team and a fast
route to report friction, workarounds treated as feedback, and running the change with one team first so the
friction can inform adjustments before the rest of the organisation encounters it. The programme that designs
for this phase produces an ISMS that operates as documented. The one that suppresses the dip produces a
compliance surface that diverges from operational reality.

## Output

By the end of this stage, the organisation has resources matched to the ISMS scope, competence and awareness
evidenced by behaviour rather than attendance, communication that works on an ordinary Tuesday as well as
during an incident, a logbook that answers questions in minutes, and controls operating as documented, with
bypass patterns read as feedback.

Even with maps, ropes, and radios, it is people who make the climb; competence, awareness, and communication
are what prevent a stumble from becoming a fall. Next: [a thorough check at base camp](base-camp-check.md)
before the push to the summit.

## Related

* [NIS2 Into the current](../nis2/currents.md)
* [ISO 22301 Running the drills](../iso22301/drills.md)
* [Interview and workshop facilitation](../supportive/interview-facilitation.md)
