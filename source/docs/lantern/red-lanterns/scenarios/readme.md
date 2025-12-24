# Writing the scenario README

Use the README to frame learning, not to celebrate cleverness.

Reference [the existing ROA poisoning README](https://raw.githubusercontent.com/ninabarzh/red-lantern-sim/refs/heads/main/simulator/scenarios/advanced/roa_poisoning/README.md). 

Control-plane playbook scenarios needs similar treatment.

## What belongs in the README

### Scenario overview

What kind of incident does this represent?

```markdown
# The Poisoned Registry

## Scenario overview

This scenario simulates a control-plane attack where RPKI infrastructure
itself is compromised. Unlike data-plane hijacks that manipulate routing
announcements, this attack modifies the authoritative systems that define
routing legitimacy.

Difficulty: Hard
Duration: 15 minutes (simulated time)
Prerequisites: Understanding of RPKI, BGP, audit log analysis
```

One paragraph. Don't tell the whole story here. That comes later.

### Attacker perspective

Condensed from the playbook. Not the entire playbook, just enough to understand the structure.

```markdown
## Attacker perspective
(Condensed from [Scarlet Semaphore operational documentation](https://red.tymyrddin.dev/docs/scarlet/op-red-lantern/roa_poisoning))

Phase 1 (t=0 to t=300): Establish presence
- Reconnaissance of victim's RPKI deployment
- Creation of legitimate ROA for attacker's own resources
- Appear as normal RPKI-aware network operator

Phase 2 (t=300 to t=600): Poison the registry
- Compromise RIR portal credentials
- Create fraudulent ROA authorising attacker's AS for victim's prefix
- Wait for RPKI validation propagation (30-90 minutes compressed to simulation time)

Phase 3 (t=600 to t=900): Exploit poisoned infrastructure
- Announce victim's prefix from attacker's AS
- RPKI validation returns VALID (due to fraudulent ROA)
- Intercept traffic whilst appearing legitimate
- Generate noise to mask detection

Key operational detail: This is a multi-week operation compressed to 15 minutes
for tabletop exercise purposes. Real attacks of this type require sustained
access and operational security over weeks.
```

This gives defenders context without spoiling the exercise. They know the structure but still must detect it.

### Defender perspective

Condensed from Silent Stability observations (or, if not available, from realistic defensive posture).

```markdown
## Defender perspective
(Based on typical network operator capabilities)

What you should see:

Early phase (t=0 to t=300):
- Minimal suspicious activity
- Routine RPKI queries (thousands happen daily, unlikely to alert)
- Legitimate ROA creation from established network operator

Mid phase (t=300 to t=600):
- ROA creation log entry (IF collecting RIR audit logs)
- Unusual: ROA created for prefix not allocated to that account
- Challenge: Most organisations don't monitor RPKI audit trails actively
- Validation state changes propagate slowly (30-90 minutes)

Late phase (t=600 to t=900):
- BGP announcement of more-specific prefix
- RPKI validation returns VALID (confusingly, because fraudulent ROA exists)
- Traffic pattern changes (IF monitoring NetFlow)
- Service degradation alerts
- High volume of unrelated route flapping (attacker-generated noise)

Detection challenges:

- RPKI validation says "VALID" for attacker announcement
- Standard BGP hijack detection rules won't trigger
- Requires correlation between ROA audit logs and BGP announcements
- Requires understanding control-plane vs data-plane attack distinction
- Alert fatigue from deliberately generated noise
```

Be honest about what defenders realistically have. If most networks don't monitor RPKI audit logs, say so.

### Likely failure modes

Where teams commonly jump to wrong conclusions.

```markdown
## Common failure modes

Failure mode 1: Trusting RPKI validation
Team sees announcement validates as VALID, concludes it's legitimate.

Why wrong: RPKI was poisoned. Validation system is compromised.

How to avoid: Cross-reference RPKI state with other data sources (IRR, WHOIS, 
historical routing patterns). Don't treat RPKI as single source of truth.

Failure mode 2: Missing the ROA audit log
Team focuses on BGP announcement at t=600, misses ROA creation at t=300.

Why wrong: Control-plane attack happened 5 hours earlier (in real time). 
By t=600, compromise is complete.

How to avoid: Implement RPKI audit log monitoring. Alert on ROA creation for 
prefixes not allocated to account. Correlation is key.

Failure mode 3: Blaming configuration error
Team sees ROA creation, assumes operator mistake during maintenance.

Why wrong: Timing, IP address, and subsequent exploitation suggest deliberate.

How to avoid: Check actor IP (TOR exit node suspicious), verify with account 
owner, correlate with subsequent BGP announcements.

Failure mode 4: Alert fatigue paralysis
Team overwhelmed by route flapping noise, misses actual attack signal.

Why wrong: Noise is deliberate. Attacker exploiting monitoring system weakness.

How to avoid: Filter high-volume low-significance alerts. Focus on correlated 
events (ROA change + BGP announcement + traffic shift).

Failure mode 5: Assuming defender visibility
Team expects to see all attacker actions in logs.

Why wrong: Phase 1 is nearly invisible. Credential compromise might have 
happened weeks earlier via phishing (not in scope of this scenario).

How to avoid: Understand that reconnaissance and initial access may not be logged.
Focus on detecting exploitation phase (t=600+) if earlier phases missed.
```

List the mistakes you expect defenders to make. The ones that make you say "but why didn't they check X?" Those are 
failure modes.

### Discussion prompts

What should be argued about afterwards?

```markdown
## Post-exercise discussion prompts

Detection timing:
- At what point could this have been detected?
- What data sources were critical?
- Which alerts/logs were red herrings?

Control-plane vs data-plane:
- How is this different from standard BGP hijack?
- Why didn't RPKI validation catch it?
- What does "poisoning the registry" mean operationally?

Operational improvements:
- Should we monitor RPKI audit logs?
- How do we correlate RPKI changes with BGP announcements?
- Do we need alerting on unexpected ROA creation?
- How do we handle validation systems that might be compromised?

Attribution challenges:
- Could we identify attacker's AS? (Yes, it's in BGP path)
- Could we identify individuals? (Harder, compromised credentials)
- Could we prove intent? (Very hard, might look like automation error)
- What evidence would we need for prosecution?

Cascading effects:
- If RPKI is compromised, what else fails?
- How do we verify control-plane integrity during incident?
- What's our recovery process if validation system can't be trusted?

Prevention:
- Four-eyes principle for ROA changes
- Hardware keys for RIR portal access
- Out-of-band ROA verification
- Monitoring for unusual RPKI activity

These questions have no single correct answer. The discussion is the learning.
```

Questions, not answers.

## What does NOT belong in README

### Complete attack walkthrough

NO:

```markdown
## Timeline
t=300: Attacker creates fraudulent ROA
t=330: ROA propagates to validators
t=600: Attacker announces prefix
t=660: Traffic is intercepted
```

This is reference material for facilitators, not documentation for defenders.

### Step-by-step detection guide

NO:

```markdown
## How to detect
1. Check ROA audit logs at t=300
2. Correlate with BGP announcement at t=600
3. Query WHOIS to verify ownership
```

Let defenders figure out detection methodology. That's the exercise.

### All playbook details

NO:

```markdown
## Attacker used these tools
- FRRouting 8.4 for BGP announcements
- TOR for RIR portal access
- Custom scripts for route flapping
```

Tool details are in playbook, not scenario doc. Defenders don't need this.

### Expected exercise outcomes

NO:

```markdown
## Success criteria
Defenders should detect attack at t=300 by monitoring ROA audit logs.
```

Facilitators track this, not README.

## The internal memo voice

The README should sound like a document you'd receive from an incident response team after cleanup:
*"This is what happened. This is why it worked. This is what you should argue about so it doesn't happen again. Good luck."*

Not: *"Welcome to exciting training scenario! We will learn about RPKI! Follow these steps to win!"*. Although, in some 
contexts :)

Voice matters. Make it sound like lived experience. Not homework.

## Cross-referencing Scarlet and Silent Stability

Always link to source material.

```markdown
## Related documentation

Scarlet Semaphore operational details:
- [The Poisoned Registry operation](https://red.tymyrddin.dev/docs/scarlet/op-red-lantern/roa_poisoning)
- [ROA manipulation techniques](https://red.tymyrddin.dev/docs/scarlet/op-red-lantern/roa_poisoning#roa-manipulation-techniques)
- [Operational cover planning](https://red.tymyrddin.dev/docs/scarlet/op-red-lantern/roa_poisoning#operational-cover-planning)

Silent Stability observations:
- [Control-plane forensics challenges](https://blue.tymyrddin.dev/docs/shadows/red-lantern/roa-poisoning-defence)
- [RPKI audit log analysis](https://blue.tymyrddin.dev/docs/shadows/red-lantern/rpki-monitoring)

Attack tree reference:
- [BGP hijacking attack patterns](https://red.tymyrddin.dev/docs/in/network/roots/ip/bgp-hijacking)
- [Control-plane vs data-plane distinction](https://purple.tymyrddin.dev/docs/lantern/red-lanterns/control-vs-data-plane)
```

This anchors simulation in documented operational reality, not invented threat theatre.

## Example README structure

Complete example for control-plane playbook scenario:

```markdown
# The Poisoned Registry

## Scenario overview
Control-plane attack targeting RPKI infrastructure itself.
Difficulty: Hard | Duration: 15 minutes | Prerequisites: RPKI knowledge

## Attacker perspective
(Condensed from Scarlet Semaphore op documentation)
- Phase 1: Establish legitimate RPKI presence
- Phase 2: Poison validation infrastructure
- Phase 3: Exploit whilst appearing valid

## Defender perspective
Early phase: Nearly invisible
Mid phase: ROA audit log anomaly (if collected)
Late phase: Confusing (RPKI says VALID but traffic patterns wrong)

## Common failure modes
1. Trusting RPKI validation blindly
2. Missing ROA audit log signal
3. Blaming configuration error
4. Alert fatigue from noise
5. Assuming complete visibility

## Discussion prompts
- Detection timing and data sources
- Control-plane vs data-plane distinction
- Operational improvements needed
- Attribution challenges
- Cascading effects if trust infrastructure compromised

## Related documentation
- [Scarlet Semaphore: ROA Poisoning](https://red.tymyrddin.dev/docs/scarlet/op-red-lantern/roa_poisoning)
- [Attack tree: BGP hijacking](https://red.tymyrddin.dev/docs/in/network/roots/ip/bgp-hijacking)
- [Control-plane attacks](https://purple.tymyrddin.dev/docs/lantern/red-lanterns/control-vs-data-plane)
```

Concise. Honest. Links to operational documentation. Frames learning without spoiling exercise.

That's what good scenario READMEs accomplish.