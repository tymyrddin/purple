# Building defensive depth

No single control stops a determined attacker. Layered defences force an attacker to defeat several obstacles, each of which is an opportunity for detection.

## Prevention controls

Identity and access management. Multi-factor authentication, least privilege access, privileged access management, just-in-time access. The aim is to reduce the value of any single credential.

Patch management. Critical vulnerabilities prioritised, patches deployed systematically, tested before production deployment, with an asset inventory that lets the team know what was patched and what was missed.

Endpoint hardening. Application allow-listing, unnecessary services disabled, exploit protections enabled (ASLR, DEP), local admin rights removed.

Network segmentation. Sensitive systems separated, lateral movement restricted, micro-segmentation for critical assets, inter-segment traffic monitored.

Email security. Anti-phishing tools, attachment sandboxing, link analysis, SPF, DKIM, and DMARC, security awareness training. The combination addresses both the technical and human sides of phishing.

## Detection controls

SIEM. Centralised logs from all sources, correlated events across systems, alerts on suspicious patterns, with an investigation interface that supports the analyst's workflow.

EDR. Endpoint activity monitored, malicious behaviours detected, rapid response enabled, forensic visibility maintained.

NDR. Network traffic monitored, lateral movement detected, command-and-control identified, exfiltration patterns surfaced.

Deception technology. Honeypots, honey tokens, decoy credentials. Attackers interacting with decoys generate high-confidence alerts, because legitimate users have no reason to touch them.

Threat intelligence platforms. External threat feeds aggregated, alerts enriched with context, known-bad infrastructure identified.

## Response capabilities

An incident response team with defined roles, documented procedures, regular training and exercises, and 24/7 availability for critical incidents.

Forensic capabilities: tools and skills for investigation, secure evidence handling, timeline reconstruction, root-cause analysis.

Automation and orchestration through SOAR. Common response tasks automated, cross-tool workflows orchestrated, time-to-respond reduced for known scenarios.

Communication plans for internal stakeholder notification, customer communication, regulatory reporting, media handling, and executive briefings.

## Resilience measures

Backup and recovery. Regular backups, offline or immutable copies, restore procedures that have been tested, documented recovery time objectives.

Business continuity planning. Alternative work processes, failover systems, manual procedures when automated systems are unavailable.

Disaster recovery. Rebuild procedures, backup sites, recovery prioritisation, regular testing of the disaster recovery plan rather than exercises that confirm its existence on paper.

## Related

- [The blue team mission](mission.md)
- [Detection, response, and recovery](detect-recover.md)
- [Building blue team capability](capability.md)
- [Continuity through a foundations lens](../../continuity/foundations.md)
