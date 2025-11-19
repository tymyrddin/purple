# Detection and response

Purple teaming turns red team attacks into blue team improvements. Build detections from observed TTPs and validate they work.

## Building detections from attacks

Start with high-fidelity indicators:
- Specific commands red team executed
- File paths, registry keys, network connections
- Process trees and parent-child relationships

Create SIEM correlation rules:
- Example: Mimikatz detection based on LSASS access + suspicious module loads
- Include context (time, user, system) to reduce false positives

Tune EDR behavioural rules:
- Focus on techniques, not specific tools
- Detect credential dumping behaviour regardless of tool used

Validate with purple team retesting:
- Red team runs technique again
- Confirm new detection triggers appropriately
- Measure detection timing and quality

## Testing detection effectiveness

Coverage testing:
- Map tested TTPs to MITRE ATT&CK
- Identify which techniques generate alerts
- Prioritise gaps based on threat relevance

True positive validation:
- Confirm alerts fire for actual malicious activity
- Reduce false positives through tuning
- Ensure alerts contain actionable information

Detection speed:
- Measure time from action to alert
- Identify delays in log processing or correlation
- Optimise for faster detection

## Response procedure validation

Playbook testing:
- Execute documented procedures during exercises
- Identify missing steps or unclear guidance
- Update playbooks based on lessons learned

Coordination testing:
- Test handoffs between SOC, IR, IT operations
- Validate escalation procedures
- Ensure communication channels work under pressure

Recovery validation:
- Test containment effectiveness
- Validate backup and restore procedures
- Ensure systems are clean before restoration

## Common detection gaps

Living-off-the-land techniques: Native Windows tools used maliciously (PowerShell, WMI, PsExec)

Cloud environments: Insufficient logging of cloud API activity, missed IAM changes

Encrypted traffic: Blind spots in HTTPS inspection, cloud services, encrypted C2

Insider threats: Legitimate account usage for malicious purposes

Supply chain: Trusted third-party access abuse
