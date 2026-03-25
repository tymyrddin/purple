# Building defensive depth

No single control stops determined attackers. Layered defences force attackers to defeat multiple obstacles, increasing detection chances.

## Prevention controls

Identity and access management: Multi-factor authentication, least privilege access, privileged access management (PAM), just-in-time access.

Patch management: Prioritise critical vulnerabilities, deploy patches systematically, test before production deployment, maintain asset inventory.

Endpoint hardening: Application whitelisting, disable unnecessary services, enable exploit protections (ASLR, DEP), remove local admin rights.

Network segmentation: Separate sensitive systems, restrict lateral movement, enforce micro-segmentation for critical assets, monitor inter-segment traffic.

Email security: Anti-phishing tools, attachment sandboxing, link analysis, SPF/DKIM/DMARC, security awareness training.

## Detection controls

SIEM (Security Information and Event Management): Centralise logs from all sources, correlate events across systems, alert on suspicious patterns, provide investigation interface.

EDR (Endpoint Detection and Response): Monitor endpoint activity, detect malicious behaviours, enable rapid response, provide forensic visibility.

NDR (Network Detection and Response): Monitor network traffic, detect lateral movement, identify command and control, detect data exfiltration patterns.

Deception technology: Honeypots, honey tokens, decoy credentials. Attackers interacting with decoys generate high-confidence alerts.

Threat intelligence platforms: Aggregate external threat feeds, enrich alerts with context, identify known-bad infrastructure.

## Response capabilities

Incident response team: Defined roles, documented procedures, regular training and exercises, 24/7 availability for critical incidents.

Forensic capabilities: Tools and skills for investigation, secure evidence handling, timeline reconstruction, root cause analysis.

Automation and orchestration (SOAR): Automate common response tasks, orchestrate cross-tool workflows, reduce time to respond for known scenarios.

Communication plans: Internal stakeholders notification, customer communication, regulatory reporting, media handling, executive briefings.

## Resilience measures

Backup and recovery: Regular backups, offline/immutable backups, tested restore procedures, documented recovery time objectives.

Business continuity planning: Alternative work processes, failover systems, manual procedures when systems unavailable.

Disaster recovery: Rebuild procedures, backup sites, recovery prioritisation, regular disaster recovery testing.
