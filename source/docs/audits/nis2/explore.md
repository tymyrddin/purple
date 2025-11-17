# Exploring and planning a crossing

![Explore](/_static/images/explore.png)

Before entering the water, answer three questions: Must we cross? What does the journey require? What resources do we need? Getting scope wrong means either wasting effort on unnecessary compliance or facing penalties for ignoring mandatory obligations.

## Are you in scope?

NIS2 applies to "essential" and "important" entities in specific sectors. The distinction matters: essential entities face stricter supervision and higher penalties.

### Essential entities (the critical core)

If you operate in energy, transport, banking, healthcare, drinking water, digital infrastructure, ICT management, public administration, or space, you're likely looking at essential entity status. This means electricity grids and hospitals, cloud providers and airports, managed service providers and government systems. Think: if it breaks, society notices immediately.

### Important entities (significant but contained)

Postal services, waste management, chemicals, food production, manufacturing, online marketplaces, search engines, and research organisations fall here. Still important, but disruption has more contained impacts: regional rather than systemic.

### Size matters, but not always

Medium and large enterprises (50+ employees or €50M+ turnover) typically fall in scope. Small and micro companies usually get a pass unless they're the sole provider of something critical or national rules say otherwise. The classic edge case: a tiny software company managing security for banks might be in scope regardless of size.

### Five questions to test your scope

"We serve banks but we're tiny: are we really in scope?"  
If you're handling their security-critical systems as a managed service provider, possibly yes.

"We manufacture electronics: general or critical?"  
Depends on what you make and who uses it. Medical devices? Probably in. Consumer gadgets? Probably out.

"Our clinic has 8 people: surely we're exempt?"  
Healthcare is essential, but size exemptions may apply unless you're the only provider in your area.

"We're an online B2B platform: does 'marketplace' include us?"  
Probably not. NIS2 typically means consumer-facing platforms connecting multiple sellers.

"We use AWS: does that make us a cloud provider?"  
No, but AWS becomes part of your supply chain obligations if you're in scope for other reasons.

Still uncertain? Contact your national supervisory authority, document your reasoning, and review your member state's implementing legislation. Grey areas exist, and regulators would rather clarify early than penalise later.

## Assess your current position

You're in scope. Now what? Understand what you're working with before building anything new.

### Your scope in one paragraph

Write a simple statement covering your sector, size, classification, services, authorities, and deadline. Example: *"Acme Logistics operates 120 trucks across NL/BE/DE. 180 employees, €35M turnover. Important entity in transport (road). Lead authority: Dutch regulator. Deadline: October 2024."* One paragraph forces clarity. If you can't write it, you don't understand your scope yet.

### Your landscape in three lists

Critical systems: What IT keeps you running? Where are single points of failure? What breaks operations immediately if compromised? Draw dependencies if it helps visualise.

Current security: Policies? Security officer? Controls like MFA, monitoring, backups? Incident response plan? Certifications? List what actually exists, not what should exist.

Supply chain: Top 10-20 critical suppliers. Who has system access? Who could break you if they failed? Cloud providers, software vendors, managed service providers: list them now.

### Your gaps in plain language

Stop pretending. Where are you possibly weak?

* No MFA on critical systems. 
* No monitoring. 
* Untested backups. 
* No incident plan. 
* No training programme. 
* One person has all the access. 
* Systems haven't been patched in months. 
* Suppliers have never been assessed. 
* Documentation doesn't exist.
* etc.

Write the list. These are just possible starting points.

### Your maturity in eight scores

Rate yourself 1-5 on governance, risk management, policies, technical controls, incident response, business continuity, 
supply chain security, and awareness. Be honest: 1 means nothing exists, 5 means mature and validated.

Mostly 1-2? Plan for 12-24 months of work. Mostly 3-4? You've got 9-18 months to fill gaps. Mostly 5? Either you are 
already compliant or you are overconfident: validate externally.

### Your timeline in months

Check your member state's deadline. Then work backward based on where you scored.

Low maturity needs 12-24 months with dedicated resources. Medium maturity needs 9-18 months focussing on gaps. High maturity (like ISO 27001 certified) needs 6-12 months for NIS2-specific items: incident reporting, supply chain formalisation, governance documentation.

If your deadline is under 12 months and you scored low, you have a resource problem. Get external help, prioritise ruthlessly, document what you're doing and why, and prepare to explain proportionality to regulators.

## Engage your stakeholders

NIS2 makes security a board-level governance issue with personal liability. This stops being an IT project and becomes an organisational one.

### The board needs to understand consequences

Personal liability in some member states. Penalties up to €10M or 2% of global turnover. Mandatory approval and oversight responsibilities. Cannot delegate everything to IT and hope for the best.

Schedule a board briefing. Present scope, gaps, costs, timeline. Get budget approval and quarterly reporting established. Make management take basic security training. Document everything in meeting minutes: board oversight is not optional under NIS2, and regulators will ask for evidence.

The board will ask: What does this cost? What happens if we don't? How do we compare to others? What are our biggest risks? Who's accountable? Have answers ready.

### IT and security implement the technical reality

They build the controls, run daily operations, respond to incidents, and know what's actually possible versus theoretical. Give them the requirements, let them map to current capabilities, estimate effort and costs, identify quick wins, and form a working group.

Expect pushback: "We're already ISO 27001 compliant." (Close, but gaps exist.) "We don't have budget." (Escalate: it's legally mandatory.) "This will slow everything down." (Find proportionate approaches.) "We're understaffed." (Prioritise or get external help.)

### Operations owns continuity and knows what's critical

Business continuity plans, recovery procedures, operational risk. Often manages OT/ICS if you have industrial systems. Critical for understanding what actually keeps services running and what breaks them.

Run joint sessions with IT to map critical systems, conduct business impact analysis, review and test continuity plans, integrate security into change processes.

### Legal and compliance handle the regulatory framework

Track national implementation variations, review supplier contracts for security requirements, establish incident reporting procedures with templates, assess liability and insurance implications, coordinate with supervisory authorities.

NIS2 is legal compliance with penalties, not just technical best practice. Legal needs to be involved early and stay involved.

### Procurement manages supplier risk

Create security requirements for new supplier RFPs, develop assessment questionnaires, classify existing suppliers by criticality, plan contract amendments for critical suppliers. Supply chain security is mandatory: procurement needs to operationalise it.

### HR builds security culture

Mandatory awareness training for everyone. Security integration into onboarding and offboarding. Management training on obligations. Possibly background checks for privileged roles. Security isn't just technology: it's people and process.

### Structure matters

Assign an executive sponsor (CEO, COO, CISO) with authority and board reporting responsibility. Designate a programme owner (often CISO or compliance lead) for day-to-day coordination. Form a core team across IT, operations, legal, procurement, HR, and finance.

Establish governance: steering committee monthly, working group weekly, board updates quarterly. Make it clear who decides, who implements, who gets informed.

## Output

Don't rush into implementation. Get these foundations right first.

Scope clarity: Which sector, essential or important, what services, which authority, what deadline. Write it down in one clear paragraph.

Current state: Systems inventory, controls summary, maturity scores, supplier list, gaps identified. Know what you have and what you don't.

Stakeholder alignment: Board briefed and budget approved, core team formed, responsibilities assigned (RACI), everyone understands their role.

Basic roadmap: Deadline, phased approach, major milestones, resource needs. Not detailed yet: just enough to start planning properly.

Governance structure: Sponsor assigned, owner designated, committees formed, reporting schedule set. Who's actually running this programme?

This is your launch point. Get this right, and the crossing becomes navigable. Rush past it, and you'll find yourself in the current without a map, a crew, or a clear destination.

```{raw} html
<div class="page-post-card__link">
    <a href="https://tymyrddin.dev/contact/">
      Arrange a free conversation to examine your landscape and see if our river crossing methods fit your journey.
    </a>
</div>
```
