# Detection, response, and recovery

These three capabilities define effective blue teaming. Each has internal trade-offs, and each works best when designed alongside the others rather than in isolation.

## Detection strategies

Different detection strategies catch different things. None is sufficient on its own.

Signature-based detection catches known malware signatures, exploit patterns, or attack indicators. It is fast and accurate for what it knows about, and blind to anything novel.

Anomaly-based detection baselines normal behaviour and alerts on deviations. It catches unknown attacks at the cost of more false positives, and it requires a reliable understanding of what "normal" looks like in the environment being defended.

Behaviour-based detection focuses on attacker techniques rather than specific tools. A rule that detects credential-dumping behaviour catches the technique whether the tool is Mimikatz, a custom binary, or a procedure that has not yet been named. This kind of rule is more resilient to evasion than signature-based equivalents.

Threat-intelligence-driven detection incorporates external indicators of compromise and TTPs from threat feeds. It catches known adversary infrastructure and techniques, with the limitation that it depends on the intelligence being current.

User and entity behaviour analytics (UEBA) uses machine-learning models to identify unusual user activity, lateral movement patterns, and compromised accounts based on historical behaviour. It is most useful for insider-threat scenarios where rule-based detection has nothing to match against.

## Detection layers

Detection works best at multiple layers simultaneously.

Network-level detection covers traffic analysis, IDS/IPS, DNS monitoring, proxy logs, and netflow data. The targets are command-and-control communications, lateral movement, and data exfiltration patterns.

Endpoint-level detection covers EDR tools, process monitoring, file integrity monitoring, and registry monitoring. The targets are malware execution, persistence mechanisms, and credential theft.

Application-level detection covers application logs, authentication events, and database activity monitoring. The targets are account compromise, data access abuse, SQL injection, and web attacks.

Cloud and identity detection covers cloud provider logs (AWS CloudTrail, Azure Monitor), identity provider logs (Azure AD, Okta), and API activity monitoring. The targets are cloud resource abuse and identity attacks.

## Response procedures

Response unfolds in stages, each with its own objective.

Triage and validation determines whether an alert represents a real threat or a false positive, gathers initial evidence, and assesses scope and severity.

Containment isolates affected systems to prevent spread: disconnection from the network, account disablement, blocking malicious infrastructure at firewall or proxy.

Eradication removes attacker presence completely: malware deletion, persistence mechanisms removed, compromised credentials revoked, exploited vulnerabilities closed.

Evidence preservation maintains chain of custody for forensics: memory images, disk images, logs, and complete documentation for investigation and potential legal action.

Recovery restores systems from known-good backups, rebuilds compromised systems from scratch where necessary, and validates that attacker presence is eliminated before reconnection.

## Recovery priorities

Critical systems come first. Business-critical services and the systems supporting essential operations recover before less important ones.

A clean rebuild is preferable to a quick fix when a system has been compromised. Cleaning attacker artefacts off a compromised system leaves the risk of incomplete eradication; rebuilding from scratch eliminates the question.

Validation precedes restoration. Recovered systems are tested in isolated environments before reconnection to production, with verification that no reinfection or persistence remains.

Enhanced monitoring on recovered systems catches any remaining attacker presence quickly during the period when reinfection is most likely.

## Playbooks

- [Golem Trust Computing Ltd. Startup Playbooks](https://blue.tymyrddin.dev/docs/org/startup/playbooks)
- [Golem Trust Computing Ltd. Scale-Up Playbooks](https://blue.tymyrddin.dev/docs/org/scale-up/playbooks)

## Runbooks

- [The Home for Bewildered Beasts of Legend Security Awareness Runbooks](https://blue.tymyrddin.dev/docs/ngo/awareness/runbooks)
- [The Home for Bewildered Beasts of Legend Incident response runbooks](https://blue.tymyrddin.dev/docs/ngo/data/runbooks)
- [Golem Trust Computing Ltd. Enterprise Runbooks](https://blue.tymyrddin.dev/docs/org/enterprise/runbooks)
- [Golem Trust Computing Ltd. Scale-Up Runbooks](https://blue.tymyrddin.dev/docs/org/scale-up/runbooks)
- [Golem Trust Computing Ltd. StartUp Runbooks](https://blue.tymyrddin.dev/docs/org/startup/runbooks)
