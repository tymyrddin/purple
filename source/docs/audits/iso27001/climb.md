# The climb

![Mountain](/_static/images/mountain.png)

You have [identified your route in the risk tent](risk-tent.md) (risk assessment), and selected your gear 
(controls), and documented what you're taking (Statement of Applicability) in [the gear depot](gear-depot.md). 
Now comes the actual climb, the operational execution that brings your ISMS to life.

A mountain expedition is only as good as its preparation. You can have the most meticulous route plan in the world, 
but if half your team forgets their boots, you are not going anywhere. In ISO 27001 terms, "The Climb" is about 
resources, competence, awareness, communication, and documentation: the operational backbone that keeps the expedition 
safe and moving upward.

## Resources for the climb

*ISO/IEC 27001 clause 7.1; ISO/IEC 27003 clause 7.1*

Every expedition needs the right combination of people, time, money, information, and equipment. ISO 27003 simply formalises what every climber already knows: go under-resourced, and you will not reach the summit.

### Determining resource needs

People: Who needs ISMS responsibilities in their role? Do you need dedicated security staff, or can existing roles expand to cover security tasks? Consider technical expertise, management oversight, and operational support.

Time: How many hours per week or month are needed for risk reviews, incident response, training delivery, internal audits, and management reviews? Security work cannot happen in people's "spare time."

Money: Budget for security tools, staff training, external consultants, penetration testing, and certification costs. Include ongoing operational costs, not just initial implementation.

Information: Access to threat intelligence, industry best practices, legal and regulatory requirements, and lessons from security incidents in your sector.

Equipment: Security tools (SIEM, MDM, firewalls, vulnerability scanners), infrastructure for secure operations, and physical security measures.

### Adapting to changing conditions

Resources are not static. They must adapt to the terrain. If conditions worsen (the organisation grows, faces new legal constraints, or experiences incidents) the resource plan should adjust too.

Example: 
A mid-sized research institute assigns one day per month for its security officer to review logs, train staff, and update incident records. As the institute adds cloud infrastructure, it budgets for a part-time systems engineer and subscribes to a cloud security posture management tool at €8.000 annually. The expedition expands its base camp before climbing higher.

### Warning signs of under-resourcing

If you see these signs, your base camp is too small for the mountain you're climbing:

- Security tasks consistently delayed or skipped
- One person becoming a single point of failure ("only Sarah knows how the firewall works")
- Incidents not properly investigated due to time constraints
- Training postponed repeatedly ("we'll do it next quarter")
- Documentation falling out of date
- Staff burnout in security roles
- Controls failing but no one has time to fix them

## Building competence and awareness

*ISO/IEC 27001 clause 7.2-7.3; ISO/IEC 27003 clause 7.2-7.3*

A rope team depends on everyone knowing their knots. The same goes for an ISMS. The organisation must ensure that those whose work affects information security are competent, trained, and aware of their role in the ascent.

### Understanding the distinctions

Competence: People have the skills and knowledge to do their jobs effectively (gained through education, training, or experience). Example: A system administrator knows how to configure firewalls securely.

Training: Developing competence through formal programmes, workshops, mentoring, or on-the-job learning. Example: Sending the administrator to a network security course.

Awareness: Everyone understands their role in information security and the consequences of their actions, even if they're not security specialists. Example: All staff recognise phishing attempts and know how to report them.

A rope team depends on everyone knowing their knots (competence), learning new techniques when the route demands it (training), and understanding when to tighten the rope (awareness).

The distinction is relevant for evidence. Competence is not evidenced by a course completion certificate; it is evidenced 
by what someone does in a realistic situation. A system administrator who has completed firewall training has attended 
training; one who configures a firewall correctly under realistic conditions, with incomplete documentation and time 
pressure, has demonstrated competence. Awareness is not evidenced by a quiz score; it is evidenced by what people do 
when they encounter an actual phishing attempt or notice something unusual. Designing the programme around observable 
outcomes rather than training delivery shifts the metric from attendance to behaviour.

[CTF and roleplay exercises](../../foundations/organisational-development/roleplay.md) apply this principle directly to 
technical competence: participants work through structured 
challenges with immediate feedback on success or failure. The format is self-correcting by design: the flag is either captured 
or it isn't, and the environment is realistic enough to produce observable behaviour rather than recalled procedure. 
A technically-oriented team member who completes a network-attack scenario in a CTF has produced better competence 
evidence than one who passed an examination on the same topic.

### Building security awareness

Awareness is not a slide deck once a year; it is a steady rhythm of reminders, briefings, and habits that reinforce secure behaviour.

Awareness that changes behaviour works best when the learning environment is close to the actual work context. A short briefing on a threat that appeared in the organisation's own sector that week works better than an hour on abstract policy, because it is specific, timely, and actionable. Simulations, tabletop exercises, and scenario-based challenges work for the same reason: they are self-correcting. The participant experiences the consequence of a wrong choice in a safe environment, which is more durable than being told what the right choice is. Designing awareness around exercises that reflect what people actually encounter, rather than policy content delivered in isolation, is the mechanism that moves click rates and keeps them there.

Example: 
During phishing season (which seems to be all year), a logistics company runs five-minute "campfire briefings" before shifts. Workers learn what suspicious messages look like and how to report them. No one expects them to quote the ISO clause, they just need to hold the line when it counts. After three months, click rates on simulated phishing tests drop from 18% to 5%.

The facilitator's role in security awareness is to create conditions where people encounter realistic situations and have to make real decisions, not to deliver content. A briefing that presents a real recent incident from the sector and asks "what would you have done?" produces more durable learning than one that explains the correct procedure. The debrief after a simulation exercise, where people articulate what they noticed and what they would do differently, is where the awareness is actually formed. What the group discussed and decided in that debrief is more informative evidence than an attendance record.

## Communication on the mountain

*ISO/IEC 27001 clause 7.4; ISO/IEC 27003 clause 7.4*

Communication is the lifeline of any climb. A garbled message or a missing update can be the difference between safe progress and disaster. ISO 27003 encourages a deliberate communication strategy that reaches the right people at the right time with the right message.

### Communication principles

Transparency: Be honest about what's happening, within security constraints. Don't sugarcoat incidents, but don't reveal details that could make things worse.

Appropriateness: Tailor the message to the audience. Technical teams need different details than the board or external partners.

Credibility: Ensure information is accurate and from trusted sources. Verify facts before communicating, especially during incidents.

Responsiveness: Communicate promptly, especially during incidents. Silence creates uncertainty and rumours.

Clarity: Use plain language; avoid jargon when possible. If staff don't understand the message, it might as well not have been sent.

### Internal and external communication

Internal messages must reach every climber who needs them. External messages must reassure partners, customers, and regulators without revealing more than is safe or appropriate.

Example: 
After a malware incident, the IT lead sends an internal alert explaining what happened, how it was contained, and what staff should do differently (check email attachments carefully, report suspicious activity immediately). The public statement comes later, crafted for partners and donors: "We experienced a security incident on 12 November, contained it within two hours, and have implemented additional safeguards. No customer data was compromised." Everyone hears what they need to know, in language they understand.

## The expedition logbook

*ISO/IEC 27001 clauses 7.5.1–7.5.3; ISO/IEC 27003 clause 7.5*

Every expedition keeps a log. It records what was packed, what was repaired, and what went wrong. The same principle applies to the ISMS.

### Documentation requirements

Documents should be:

* Identified: Title, version, date, author, document reference code
* Controlled: Reviewed before release, approved by appropriate authority, versioned to track changes
* Accessible: Available when needed (to authorised people), protected when not (from unauthorised access)
* Retained or disposed of: With intent and in accordance with legal, regulatory, and business requirements

Documentation levels differ by organisation. A solo climber needs less paperwork than a national expedition, but both must know what decisions were made, when, and why.

### Common documentation mistakes

Avoid these pitfalls:

- Documentation for documentation's sake: Creating documents no one reads or uses
- Outdated documents: Policies that contradict current practice, making compliance impossible
- Hidden documents: Stored where people can't find them when needed
- No version control: Leading to confusion about what's current and who approved what
- Over-documentation: Burying critical information in bureaucracy; if everything is "critical," nothing is
- Under-documentation: No record of decisions, making it impossible to demonstrate due diligence

Example: 
A regional energy cooperative keeps its ISMS policies, risk assessments, audit reports, and corrective actions in a secure repository with version tracking and role-based access. When regulators ask who approved a change to the data-retention policy, they can trace it in minutes, showing the policy was reviewed on 15 March 2025, approved by the board on 22 March, and implemented on 1 April with staff notification and training completion tracked. The audit trail demonstrates governance, not just compliance theatre.

## Operational planning and control

*ISO/IEC 27001 clauses 8.1, 8.2, 8.3; ISO/IEC 27003 clause 8*

Clause 8 represents the "Do" phase of the PDCA (Plan-Do-Check-Act) cycle:

- Plan: Risk assessment, control selection (covered in previous sections)
- Do: Implement and operate controls (this section)
- Check: Monitor and measure performance (clause 9)
- Act: Improve and adapt (clause 10)

This is where planning becomes reality, turning all that preparation into a controlled, observable climb.

### What operational planning requires

Organisations must:

* Establish and monitor processes to meet information security objectives
* Assess risks regularly and maintain the [risk register](../../risk-management/risk-register.md)
* Reassess when conditions change (new systems, incidents, regulatory changes)
* Treat risks with appropriate controls, as documented in the Statement of Applicability
* Document results of both risk assessments and treatment decisions

### When to assess or reassess risks

Regularly: At least annually, or as defined in your ISMS scope and risk management procedures. Don't wait for problems to force a review.

After major changes: New systems or services, mergers or acquisitions, significant security incidents, regulatory changes affecting your operations, major supplier changes.

When controls change: Adding, removing, or significantly modifying security controls. A change in one control can affect the risk profile elsewhere.

When new threats emerge: Significant cybersecurity events affecting your sector (ransomware campaigns, zero-day vulnerabilities, supply chain compromises).

When assumptions change: Growth, downsizing, changes in business model, shifts in threat landscape, new legal obligations.

The climb itself produces evidence about which assumptions were right. When new controls arrive, the organisation 
experiences increased friction before any benefit is felt. People will find workarounds, not because they are 
obstructive but because the control's model does not yet fit their workflow. A control that is consistently bypassed 
(a VPN disabled before working, an approval process that accumulates rubber-stamp sign-offs without review) is 
not primarily a compliance failure. It is a signal that an assumption does not match the operational environment. The 
question to ask before escalating enforcement is whether the underlying model still holds. Treating bypass patterns 
as system information rather than individual non-compliance is what separates a maturing ISMS from one that 
accumulates workarounds beneath a clean compliance surface.

### The chaos phase

Every significant change to controls or processes goes through a disruption phase before reaching a new stable state. 
[This is structural, not failure](../../foundations/organisational-development/satir-change-model.md). When MFA is introduced, the first weeks will generate more helpdesk tickets, more 
complaints, and more workarounds than the final state will. When an access review process is formalised, it will 
initially take longer and feel more burdensome than the informal practice it replaced.

The disruption has predictable characteristics: people will agree in meetings and find workarounds in practice; 
performance metrics will dip before they improve; early adopters will be frustrated that others have not adapted. 
None of this is evidence that the control is wrong or that the rollout has failed. It is evidence that the transition 
is underway.

What helps during this phase: acknowledge the dip explicitly rather than treating it as deviation; provide 
structured support, such as a named point of contact in each team and a fast route to report friction; treat 
workarounds as feedback rather than non-compliance; and run the change with one team first so the friction can 
inform adjustments before the rest of the organisation encounters it. The programme that designs for this phase 
produces an ISMS that operates as documented. The one that treats the dip as a problem to suppress produces a 
compliance surface that diverges from operational reality.

### Example: Risk reassessment before major change

Before moving its case files into a new document management system, a humanitarian NGO reassesses risks. Data residency laws, encryption options, and access policies are reviewed. The risk assessment (RA-2025-03) identifies three High risks and seven Medium risks. Treatment plans are documented, approved by the Director on 15 February, and implemented over six weeks.

High-risk mitigations include:
- End-to-end encryption for data at rest and in transit
- Multifactor authentication for all access
- Data residency in EU-compliant infrastructure
- Automated access logging and quarterly reviews

Only after verification that all High-risk mitigations are operational does the migration proceed on 1 April. The complete risk assessment, treatment decisions, verification evidence, and migration results are stored in the ISMS repository. Not for decoration, but because it proves the expedition knows where it stands and can demonstrate due diligence to donors and regulators.

## Why the climb works at all

Even with maps, ropes, and radios, it is people who make the climb. Competence, awareness, and communication are what prevent a stumble from becoming a fall.

### What operational excellence looks like

In practice, this means:

- Security training isn't a tick-box exercise. It changes behaviour and is measurable in incident rates and user responses
- Communication flows naturally, not just during crises, creating a culture where people feel safe reporting problems
- Documentation supports work rather than creating busywork; people actually use policies because they're relevant and accessible
- Resources match ambitions, preventing burnout and dangerous shortcuts
- Risk management becomes routine, not an annual ordeal; teams anticipate and address issues before they become incidents
- Everyone understands their role in security, from reception to the board

### The human element

Security culture is not enforced through memos; it grows through repetition, trust, and shared responsibility. When everyone understands *why* the rules exist, they stop seeing them as red tape and start treating them as oxygen. Invisible, vital, and entirely necessary for the altitude ahead.

The climb succeeds not because the route is easy, but because every team member knows their role, has the tools they need, trusts their rope partners, and understands that reaching the summit requires each person to hold the line under pressure.

Ready for [a thorough check at the final stage base camp](base-camp-check.md) before the push to the summit?

