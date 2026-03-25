# Detection, response, and recovery

These three capabilities define effective blue teaming.

## Detection strategies

Signature-based detection: Known malware signatures, exploit patterns, or attack indicators. Fast and accurate for known threats but blind to novel attacks.

Anomaly-based detection: Baseline normal behaviour and alert on deviations. Catches unknown attacks but generates more false positives. Requires understanding of what "normal" looks like.

Behaviour-based detection: Focus on attacker techniques rather than specific tools. Detects credential dumping behaviours even if the tool changes. More resilient to evasion.

Threat intelligence: Incorporate external IOCs (indicators of compromise) and TTPs from threat feeds. Detect known adversary infrastructure or techniques.

User and entity behaviour analytics (UEBA): Machine learning models identify unusual user activity, lateral movement patterns, or compromised accounts based on historical behaviour.

## Detection layers

Network level: Traffic analysis, IDS/IPS, DNS monitoring, proxy logs, netflow data. Detect command and control communications, lateral movement, data exfiltration.

Endpoint level: EDR tools, process monitoring, file integrity monitoring, registry monitoring. Detect malware execution, persistence mechanisms, credential theft.

Application level: Application logs, authentication events, database activity monitoring. Detect account compromise, data access abuse, SQL injection, web attacks.

Cloud and identity: Cloud provider logs (AWS CloudTrail, Azure Monitor), identity provider logs (Azure AD, Okta), API activity monitoring. Detect cloud resource abuse, identity attacks.

## Response procedures

Triage and validation: Determine if alert is real threat or false positive. Gather initial evidence. Assess scope and severity.

Containment: Isolate affected systems to prevent spread. Disconnect from network, disable accounts, block malicious infrastructure at firewall/proxy.

Eradication: Remove attacker presence completely. Delete malware, remove persistence mechanisms, revoke compromised credentials, close exploited vulnerabilities.

Evidence preservation: Maintain chain of custody for forensics. Capture memory images, disk images, logs. Document everything for investigation and potential legal action.

Recovery: Restore systems from known-good backups. Rebuild compromised systems from scratch if necessary. Validate that attacker presence is eliminated before reconnection.

## Recovery priorities

Critical systems first: Business-critical services and systems supporting essential operations recover before less important systems.

Clean rebuild over quick fix: Don't trust compromised systems. Rebuild from scratch rather than trying to "clean" attacker artifacts.

Validation before restoration: Test recovered systems in isolated environment before reconnecting to production. Verify no reinfection or persistence.

Enhanced monitoring: Temporarily increase logging and monitoring on recovered systems to catch any remaining attacker presence quickly.
