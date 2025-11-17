# Playbooks that actually work

Playbooks bridge the gap between abstract policy and real-world action. They answer: *“What do we do when this happens?”*  

## Types of playbooks

### Detection playbooks

These define how suspicious activity is spotted in the first place. They bundle SIEM queries, correlation rules, anomaly thresholds, and alert triggers. The goal is simple: fewer false positives, fewer blind spots, and fewer Tuesday mornings spent grumbling about alert fatigue.

Most detection playbooks start with ambitious coverage and gradually evolve toward "things that actually matter and don't cry wolf constantly." This evolution is not failure; it's learning.

### Response playbooks

These translate "We have a problem" into focused action. They outline how to investigate, contain, eradicate, and recover without tripping over each other. Expect clear steps, roles, timings, and a refusal to rely on heroic guesswork.

Response playbooks fail when they assume everything will go perfectly and everyone will remember their training. Build in plan B. The primary tool might be offline, the key person might be unreachable, and Tuesday afternoon might suddenly become a very long week.

### Escalation playbooks

The human side. Who must be informed, in what order, by which channel, and with what degree of panic. These keep legal teams, executives, regulators, and unfortunate comms people looped in without creating an accidental stampede.

Escalation playbooks reveal organisational dysfunction faster than anything else. If your escalation tree has 12 layers and requires three committees to approve a weekend callout, the problem isn't the playbook. But you still need one that works within your dysfunctional reality.

## Format

Every playbook follows a common structure designed for speed under pressure.

### Trigger

The condition that starts everything. An alert firing, a pattern match, an anomaly spike, a panicked message from 
an analyst, or the sudden silence of a critical service.

Good triggers are specific: "SIEM alert: 5+ failed admin logins from single IP within 2 minutes" 
Bad triggers are vague: "Something seems wrong"

### Steps

The precise sequence of actions, mapped to roles. Who collects logs, who isolates the host, who checks lateral 
movement, who updates stakeholders. No "someone should probably..." statements.

Structure steps by timeframe and role:
- Immediate actions (0-5 minutes): assess and contain
- Investigation (5-30 minutes): collect evidence and scope
- Containment (30 minutes-2 hours): isolate and revoke
- Eradication (2-8 hours): remove threats and validate
- Recovery (8-24 hours): restore services and monitor

### Decision points

Clear forks in the road. When to contain immediately, when to hold back and gather evidence, when to escalate to 
legal or management, and when to call in external muscle.

Format as yes/no questions with clear consequences:

Is this ransomware actively encrypting files?

→ Yes: Immediate network isolation. Notify executives within 1 hour.
→ No: Continue investigation.

### Tools

The practical bits: command snippets, SIEM queries, automated scripts, dashboards, checklists, forensic templates, 
and anything else the team shouldn't be hunting for mid-incident.

Include ready-to-use examples, pre-filled queries, dashboard links, and communication templates. If someone needs 
to log in, find the right module, and figure out what to search for, you've added friction where you need speed.

## Keeping playbooks alive

Playbooks age fast. They must be exercised, challenged, and broken on purpose. Every incident, exercise, tabletop 
exercise, or chaotic Friday afternoon can feed updates back into the documents. A playbook that never changes 
is not a sign of perfection. It's a sign that nobody actually uses it.

### Warning signs your playbooks are dead

* Nobody references them during actual incidents. Either the playbooks are wrong or nobody knows they exist. Both problems need fixing.
* Every incident reveals steps that don't work. Tools have changed, contacts are wrong, procedures assume resources you don't have.
* The playbooks assume perfect conditions. Procedures fall apart when the primary SIEM is down, the incident lead is on holiday, or it's 3am on a Sunday.
* They're comprehensive but useless. Your phishing playbook is 40 pages and requires reading three other documents. That's not a playbook; that's procrastination formatted as documentation.
* Tribal knowledge fills the gaps. Only senior analysts know how things really work. Your playbooks document the process you wish you had, not the one you actually use.

### Making them work

* Test with junior staff. If someone with six months' experience can't follow your playbook during an exercise, it's not clear enough.
* Time the procedures. If your playbook says "immediately isolate" but it actually takes 20 minutes, document the reality.
* Include failure modes. What happens when the primary tool is offline? When the first contact doesn't answer? Document plan B.
* Keep them short. Two pages maximum. If it's longer, you're writing an encyclopaedia, not an operational guide.
* Make them accessible under pressure. If your playbooks live behind a VPN and the VPN is down because of the incident, you've failed.

## Examples

Essential (build something like these first):
- [Ransomware response playbook (NGO, 20 staff)](playbook-examples/ransomware-ngo.md)
- [Phishing campaign response playbook (SME, 50-250 staff)](playbook-examples/phishing-sme.md)
- Compromised credentials playbook
- Data breach
- Service outage

Important (build these next):
- DDoS attack
- Insider threat
- Supply chain compromise
- [Compromised AWS credentials playbook (development environment)](playbook-examples/aws-credentials.md)

Build them, test them, break them, fix them. That's the cycle. Anyone promising you stable, unchanging, perfect 
playbooks is selling you documentation theatre, not operational capability. Playbooks are designed [to be tested in 
exercises and updated with each iteration](../learning/incident-response/choreography.md).

```{raw} html
<div class="page-post-card__link">
    <a href="https://tymyrddin.dev/contact/">
      Want playbooks your team will actually follow? Let’s build them.
    </a>
</div>
```
