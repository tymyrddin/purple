# Moving beyond manuals that nobody reads

An incident response plan that lives in a dusty 50-page PDF is not a plan. It's a liability. Manuals only matter if they can be used in moments of stress, distraction, and partial information. The aim is to move from comprehensive to comprehensible so that, when something breaks, people reach instinctively for the right aid.

The test is simple: can someone who's never seen it before use it successfully at 3am? If not, it's documentation theatre, not operational guidance.

## What types of manuals will actually be read?

Readable manuals behave like tools. They're designed for exactly one moment of need, not for theoretical completeness.

### The "flashlight in a blackout"

A single page covering the first fifteen minutes of a suspected breach. It answers two questions: whom do I call, and what do I do right now.

What it contains:
- Three phone numbers (incident lead, backup, external help)
- Five immediate actions in order
- Decision point: escalate now or investigate first
- Nothing else

Example:
```
SUSPECTED SECURITY INCIDENT

1. Don't panic. Don't shut anything down yet.
2. Note the time and what you observed.
3. Call: [Name] [Mobile] [Email]
   Backup: [Name] [Mobile] [Email]
4. If ransomware/active attack: Isolate affected systems NOW
   If suspicious but unclear: Preserve evidence, investigate
5. Follow [link to relevant playbook]

Do not email. Do not post in Slack. Call.
```

Where it lives: Printed and laminated at every desk. Phone home screen. Pinned message in every team channel.

### The "pilot's pre-flight checklist"

Laminated lists for repeated, high-risk situations such as ransomware detection, leaked credentials, or DDoS disruption. They stop people skipping steps when adrenaline spikes.

What it contains:
- Checkbox format (physical checking prevents skipping)
- Time expectations for each step
- "Stop and escalate if..." decision points
- No explanations, just actions

Example ransomware checklist:
```
☐ Take photo of ransom note (don't touch files)
☐ Disconnect network cable / disable WiFi
☐ Note affected systems (list them)
☐ Call incident lead [number] (now, don't wait)
☐ Check backups accessible (don't restore yet)
☐ List last known good backup date: _______
☐ Stop others accessing shared drives
☐ Preserve one infected machine for forensics
```

Where it lives: Laminated card in server room. Printed copy in incident response folder. Digital version in team wiki with "print this" link.

### The "translation guide"

Short references that focus on what someone actually has to do with a given tool. For a SIEM, list the five most important queries. For secure communication, provide the one approved channel and the button that launches it.

What it contains:
- Tool-specific quick reference
- Only the queries/commands actually used
- Screenshots of where to click
- Common problems and fixes

Example SIEM quick reference:
```
SIEM INCIDENT QUERIES

1. Find all activity from suspicious IP:
   source_ip="x.x.x.x" earliest=-24h

2. Identify lateral movement from host:
   source_host="HOSTNAME" service=(RDP OR SSH OR SMB)

3. Check for data exfiltration:
   bytes>100000000 dest_type="external"

4. Authentication failures then success:
   event_type="auth_failed" | followed by event_type="auth_success"

5. Access dashboard: [URL]
   Login: Use your normal AD credentials
   If locked out: Call [IT helpdesk]
```

Where it lives: Stuck to the wall next to the SOC analyst workstation. Shortcut on desktop. Bookmarked in browser.

### The "understudy playbook"

Role-specific guidance for when the usual lead is unavailable. It names the systems to check and the people to notify, in the correct order.

What it contains:
- "You're now the incident lead because [Name] isn't available"
- Systems you're responsible for checking
- Decisions you can make vs. must escalate
- Who to hand off to when the primary returns

Example deputy security lead guide:
```
YOU'RE DEPUTY INCIDENT LEAD

Primary lead unavailable? You're in charge.

Your authority:
✓ Activate this playbook
✓ Isolate systems
✓ Disable user accounts
✓ Call external support
✗ Approve ransom payment (escalate to CEO)
✗ Notify customers (escalate to Director)

Systems you're responsible for:
- SIEM: [URL] - check for alerts
- Email security: [URL] - check quarantine
- Firewall: [URL] - check blocks/alerts
- Endpoint protection: [URL] - check detections

Escalation order:
1. CTO [mobile]
2. External IR firm [number] [account ID]
3. CEO (only if CTO unavailable) [mobile]

Hand-off: When primary returns, brief them and transfer logs/notes.
```

Where it lives: Sealed envelope in secure location. Encrypted file on designated backup's laptop. Card in incident response folder.

## How to make them readable

Readability is not about literary polish. It comes from structure, constraint, and brutal prioritisation.

### 1. Use the one-page rule

If the procedure cannot fit on one page or screen, it's a policy, not a job aid. Shrinking it forces decisions about what genuinely matters in the moment.

What fits on one page:
- Ransomware first response: yes
- Complete ransomware investigation, remediation, and recovery: no (that's a playbook)
- Emergency contacts and first call actions: yes
- Complete escalation procedures with approval workflows: no (that's a process document)

When you exceed one page: You're either trying to cover too much or including background that can be linked to elsewhere. The one-page version gets you started; the linked playbook provides detail once you've contained the immediate crisis.

### 2. Lead with visuals

People under stress process images faster than text.

Flowcharts for decisions:

```
Alert fires
    ↓
Is service down?
    ↓ No              ↓ Yes
Investigate    →  Isolate system immediately
    ↓                      ↓
Severity?         Activate DR plan
High → Escalate   
Low  → Document
```

This beats three paragraphs explaining when to escalate vs. investigate every time.

Icons and colour cues:
- 🔴 Red for immediate actions requiring no approval
- 🟡 Yellow for "stop and get approval" points
- 📞 Phone for who to contact
- 🖥️ Computer for systems to check
- ⚠️ Warning for common mistakes

Visual consistency matters: Use the same icons and colours across all manuals. People learn to recognise red = urgent action without reading.

### 3. Write for scanning, not reading

Under pressure, people don't read. They scan for relevant information and skip the rest.

Format for scanning:

Bad (wall of text):
```
When you discover a potential security incident, it's important to first 
assess the situation to determine if immediate action is required or if 
you should gather more information. Contact the incident response lead 
at the number provided in the contact list, or if they're unavailable, 
contact the backup lead. Document what you observed including the time 
and any relevant details.
```

Good (scannable):
```
DISCOVERED INCIDENT

1. Note time and what you saw
2. Call incident lead: [Name] [Number]
   Backup: [Name] [Number]
3. If active attack: Isolate NOW
   If suspicious: Investigate first
4. Document everything
```

Writing tactics:
- Bold critical actions so they jump out
- Number steps that must happen in sequence
- Bullet points for options or information
- Short sentences. Five words. Ten maximum. Never more than fifteen.
- No adjectives. No adverbs. No qualifiers. No padding.
- Active voice only. "Disconnect the cable" not "The cable should be disconnected"

### 4. Make them living and accessible

Manuals age. They need exercise, updating, and distribution.

Test them in exercises:
- Hand someone the manual during a tabletop exercise
- Watch where they hesitate, get confused, or ignore instructions
- Ask "what would make this clearer?"
- Update immediately based on feedback

Version clearly:
```
Version: 2.1
Last updated: 17 November 2025
Next review: 17 May 2026
Owner: [Name]
```

This visible dating builds trust that the content is current. If the last update was three years ago, nobody believes the phone numbers still work.

Place them where work happens:

Digital locations:
- Pinned Slack/Teams message in security channel
- Bookmarked in every team member's browser
- Shortcut on desktop of relevant systems
- QR codes linking to manuals in server rooms

Physical locations:
- Laminated cards at workstations
- Printed copies in incident response folder
- Posted on walls in server room and SOC
- Sealed envelopes for "break glass" procedures

Accessibility under duress:
If your manuals live behind a VPN and the VPN is down because of the incident you're responding to, they're useless. Host critical manuals somewhere accessible even when infrastructure fails: personal devices, printed copies, external hosting.

## Common failures

### The comprehensive compendium

Some organisations produce 200-page incident response manuals covering every conceivable scenario in exhaustive detail. Nobody reads them. They sit in SharePoint gathering dust while people improvise during actual incidents.

The problem: Trying to be complete instead of useful. Confusing documentation with operational guidance.

The fix: Separate policy documents (comprehensive, stored, rarely read) from job aids (minimal, accessible, frequently used).

### The stale manual

Phone numbers are wrong. Tools have changed. Procedures reference systems you no longer use. The manual was perfect when written three years ago; now it's worse than useless because following it wastes time.

The problem: No maintenance process. No ownership. No testing.

The fix: Assign owners. Schedule reviews. Test in exercises. Update immediately after incidents.

### The locked manual

The incident response manual is in a secure document management system requiring three levels of authentication and manager approval to access. When you need it at 2am, good luck.

The problem: Treating manuals like sensitive secrets instead of operational necessities.

The fix: Job aids should be accessible. They don't contain sensitive data (no credentials, no architecture diagrams). If you think they need locking away, you're including the wrong content.

### The theoretical manual

Written by people who've never responded to an incident, describing idealised procedures that assume perfect conditions, available resources, and calm decision-making.

The problem: No connection to operational reality.

The fix: Write manuals with input from people who actually respond to incidents. Test them. Update based on what works, not what should work in theory.

### The hidden manual

Exists somewhere on the wiki. Someone knows where. They're on holiday.

The problem: Discoverability. If people don't know it exists or can't find it quickly, it might as well not exist.

The fix: Multiple distribution points. Search keywords. Regular reminders. Print physical copies.

## The usability test

Before declaring a manual "done," test it honestly:

Can someone unfamiliar with the procedure follow it successfully? Hand it to a junior team member who's never used it. Watch them try. Where do they get stuck?

Can it be used at 3am? Tired, stressed, distracted. Does it still work? Or does it require clear thinking and careful reading?

Can it be used when primary systems are down? If the incident took out your infrastructure, can you still access the manual?

Does it answer "what do I do next" at every step? Or does it leave people guessing, interpreting, or hunting for information?

Has it been used successfully in practice? Not theory, not exercises (though those help), but actual incidents? If not, you don't know if it works.

If the answer to any of these is no, it's not done. Keep simplifying, testing, and refining until it passes all five tests.

## What success looks like

When manuals work, you see:
- People reference them during incidents instead of improvising
- New team members can follow procedures without extensive training
- exercises complete faster with fewer mistakes
- Post-incident reviews show people followed documented procedures
- Updates happen regularly based on lessons learned
- Physical copies are worn from actual use

When manuals fail, you see:
- "We didn't have time to look at the manual during the incident"
- "I didn't know we had a manual for that"
- "The manual was wrong/outdated so we ignored it"
- "I read the manual but didn't understand what to do"
- Senior staff making decisions from memory while ignoring documented procedures

The goal: Manuals become instinctive tools, not optional references. When something breaks, reaching for the manual is automatic, not an afterthought.

## Principles

A good manual is not something people read. It's something people use, reliably, on the worst day of the year.

If your manual requires calm, time, and concentration to be useful, you've built the wrong thing. Build for chaos instead. Build for 3am. Build for the moment when everything is on fire and someone needs to know exactly what to do next.

That's not a manual. That's a lifeline.

```{raw} html
<div class="page-post-card__link">
    <a href="https://tymyrddin.dev/contact/">Ready to turn dusty PDFs into lifelines? Get in touch.</a>
</div>
```
