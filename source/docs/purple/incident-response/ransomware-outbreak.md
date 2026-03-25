# Ransomware outbreak (tabletop)

* Target audience: SIRT, SOC, IT operations, management  
* Duration: 90-120 minutes  
* Complexity: Medium  
* Format: Tabletop with timed decision rounds

## Scenario briefing

Monday, 06:15 GMT

SOC receives multiple alerts: endpoint detection showing file encryption patterns across 15 workstations in Finance 
department. Initial investigation shows encrypted files with .locked extension and ransom note demanding 50 Bitcoin 
payment within 72 hours.

Affected systems include file servers with shared drives containing financial records, HR data, and customer 
contracts. Email system appears unaffected. Initial scope unclear.

## Objectives

- Practise containment decision-making under time pressure
- Test escalation procedures and role clarity
- Navigate trade-offs between containment and business continuity
- Manage internal and external communications
- Exercise incident logging and evidence preservation

## Setup (15 minutes)

Roles:
- Incident Commander (SIRT lead)
- SOC Analyst (detection and investigation)
- IT Operations (containment and recovery)
- Communications Lead (internal and external comms)
- Business Liaison (Finance department representative)
- Legal/Compliance (regulatory and legal implications)
- Observers (facilitator + note-takers)

Ground rules:
- All decisions are logged with timestamp
- No real systems are touched
- Teams use actual communication channels (Slack, email, etc.) in simulation mode
- Unknown information must be requested from facilitator
- 5-minute decision rounds with facilitator injects

## Round-by-round play

Round 1 (0-15 minutes): Initial response

Facilitator provides: Initial alert details, affected systems list, preliminary indicators

Team must decide:
- Who takes incident command?
- What's the immediate containment action?
- Who needs to be notified immediately?
- What investigation steps happen first?

Facilitator inject: "While you're discussing, three more systems in Marketing show encryption. The file server is now showing high CPU usage."

Round 2 (15-30 minutes): Scope assessment

Facilitator provides: Investigation shows lateral movement from compromised VPN account. Attacker appears to still have access. Backup server was also compromised but backups encrypted only partially.

Team must decide:
- Do we shut down network segments? Which ones?
- Do we disable VPN access for all users?
- What's our communication to staff?
- Do we contact law enforcement?
- What's the business impact of our containment choices?

Facilitator inject: "CEO calls. Major client presentation is scheduled for 10:00. Finance needs access to client contracts. What do you tell them?"

Round 3 (30-50 minutes): Crisis management

Facilitator provides: Network analysis shows 47 systems affected. Attacker used valid credentials. Ransomware variant is recent, no public decryptor available. Local media has picked up the story (staff member posted on social media).

Team must decide:
- Do we pay the ransom?
- How do we communicate externally?
- What's our recovery strategy?
- What regulatory notifications are required? (GDPR? NIS2?)
- How do we prevent reinfection during recovery?

Facilitator inject: "Ransomware group posts your company on their leak site claiming they exfiltrated 500GB of data before encryption. They threaten to publish in 48 hours if ransom isn't paid."

Round 4 (50-70 minutes): Recovery planning

Facilitator provides: Containment successful, attacker access terminated. Partial backups available (3 days old for most systems). Some critical data may be lost. Forensics shows initial compromise was phishing email 10 days ago.

Team must decide:
- What's the recovery priority order?
- How long will recovery take?
- What interim workarounds for critical business functions?
- What changes to prevent recurrence?
- How do we communicate recovery timeline?

Facilitator inject: "Insurance company needs detailed incident report for claim. Legal wants to know if we must report data exfiltration to regulators. Finance wants impact assessment for Q3 reporting."

## Debrief and retrospective (30 minutes)

What worked:
- Which decisions were made quickly and confidently?
- Where was communication clear?
- What procedures worked as expected?

What surprised us:
- What information did we need but didn't have?
- Where did escalation stall or confusion happen?
- What dependencies weren't obvious until now?

Immediate improvements:
- Which playbook sections need updating?
- What tools or access are missing?
- Which roles need clearer definition?
- What training gaps exist?

## Outputs

- Timestamped decision log
- Identified gaps in procedures, tools, or authority
- Updated escalation matrix
- Communication templates refined
- 3-5 priority improvements with owners

```{raw} html
<div class="page-post-card__link">
    <a href="https://tymyrddin.dev/contact/">
      Discuss handling ransomware scenarios with us
    </a>
</div>
