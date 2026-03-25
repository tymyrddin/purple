# Supply chain compromise (live injection)

* Target audience: SIRT, SOC, IT Ops, Procurement  
* Duration: 2-4 hours  
* Complexity: High  
* Format: Live injection into actual monitoring systems

## Scenario briefing

Your organisation uses a third-party monitoring tool (SaaS) that has legitimate access to your infrastructure for performance monitoring. Unknown to your team, this vendor has been compromised.

Simulation injects will mimic a supply chain attack through this trusted vendor relationship.

## Preparation (before simulation)

With vendor coordination:
- If actual vendor participates: they send "malicious" activity from their legitimate access
- If vendor unavailable: simulation team spoofs vendor behaviour in safe test environment

Simulation infrastructure:
- Isolated test environment mirroring production
- Safe "malicious" indicators (beacon traffic, fake data queries)
- Monitoring tools are live and active
- Communication channels are real

Participant briefing:
- Teams know simulation is happening today
- Teams don't know scenario or timing
- Observers are embedded with each team
- Real tools and procedures are used

## Simulation flow

Phase 1: Detection (0-30 minutes)

Inject: SOC monitoring detects unusual API calls from vendor monitoring tool. Pattern suggests data reconnaissance: queries for user lists, privilege accounts, network maps.

Reality check: Are SOC alerts properly configured? How long until someone notices?

Phase 2: Investigation (30-90 minutes)

Inject: Further investigation shows vendor account is accessing systems outside normal monitoring scope. Beacon traffic to unknown external IP detected.

Team must:
- Determine if this is legitimate vendor behaviour or compromise
- Contact vendor (simulation team plays vendor role)
- Assess what data may have been accessed
- Decide on containment without breaking production monitoring

Inject: Vendor contact (simulation) confirms "routine maintenance" but can't explain specific API calls. Vendor is slow to respond, gives vague answers.

Phase 3: Containment (90-150 minutes)

Inject: Additional analysis shows data staging: large queries packaged for exfiltration. Need immediate containment decision.

Team must:
- Revoke vendor access vs. risk of losing monitoring capability
- Find alternative monitoring solution quickly
- Prevent data exfiltration
- Preserve evidence for forensics
- Assess business impact of losing vendor service

Inject: Vendor relationship manager (business side) protests: "We need this tool! We have SLAs to meet! You can't just shut it off!"

Phase 4: Response coordination (150-180 minutes)

Inject: Public disclosure: security researcher tweets about widespread compromise of your monitoring vendor affecting multiple customers. Media picks up story.

Team must:
- Coordinate with vendor on joint response
- Determine regulatory reporting requirements
- Assess impact to other organisations
- Communicate internally and externally
- Plan recovery and alternative solutions

## Observer checklist

Observers track:
- Time to detection
- Time to containment decision
- Quality of investigation (thoroughness vs. speed)
- Communication effectiveness between teams
- Decision-making bottlenecks
- Use of playbooks and procedures
- Vendor communication handling
- Business impact considerations

## Debrief focus

Technical:
- Did monitoring detect the anomaly?
- Was investigation methodology sound?
- Were containment options understood?
- Was evidence properly preserved?

Process:
- How long did decision-making take?
- Where were handoffs unclear?
- What information was missing?
- Did escalation work?

Communication:
- Was vendor contact effective?
- Were business stakeholders kept informed?
- Was external communication coordinated?
- Were legal/compliance looped in?

```{raw} html
<div class="page-post-card__link">
    <a href="https://tymyrddin.dev/contact/">
      Talk to us about securing your supply chain
    </a>
</div>
