# Case studies and examples

Real-world scenarios demonstrate how purple teaming works in practice.

## Case study: Ransomware simulation

Scenario: Test organisation's ability to detect and respond to ransomware attack.

Red team approach:
- Initial access via phishing
- Credential dumping with Mimikatz
- Lateral movement to file servers
- Simulated encryption (test files only)

Blue team response:
- Missed phishing, user clicked link
- EDR detected Mimikatz, generated alert
- SOC investigated within 15 minutes
- Containment blocked lateral movement
- Response prevented encryption spread

Findings:
- Email filtering needs improvement
- EDR detection worked well
- Response was fast and effective
- Backup procedures untested during exercise

Improvements implemented:
- Enhanced email security training
- Tested backup restore procedures
- Added lateral movement detection rules
- Updated ransomware response playbook

Outcome: Next exercise showed faster detection, prevented lateral movement entirely.

## Case study: Insider threat detection

Scenario: Test ability to detect malicious insider with legitimate access.

Red team approach:
- Used provided credentials (simulating insider)
- Accessed systems within normal job function
- Gradually escalated to sensitive data access
- Staged data for exfiltration

Blue team response:
- Normal activity went undetected initially
- UEBA flagged unusual data access patterns
- Investigation revealed systematic collection
- Response team contained account within 2 hours

Findings:
- Baseline behavioural analytics working
- Manual investigation skills strong
- Response time acceptable but could improve
- Data access monitoring had gaps

Improvements implemented:
- Enhanced data access logging
- Created insider threat hunt playbooks
- Automated alert for bulk data access
- Added DLP controls

Outcome: Subsequent testing detected anomalies much faster.

## Example engagement: Supply chain compromise

Setup: Red team simulated compromised vendor account with legitimate access to infrastructure.

Execution:
- Used vendor credentials to access monitoring systems
- Reconnaissance of network from trusted position
- Attempted to leverage vendor access for broader compromise

Detection:
- Network anomaly detection flagged unusual API calls
- SOC investigation revealed access outside vendor's normal scope
- Vendor contact confirmed suspicious activity
- Access revoked, credentials reset

Learning:
- Third-party access monitoring effective
- Vendor communication procedures worked
- Baseline of "normal" vendor behaviour crucial
- Need better vendor account lifecycle management

Improvements:
- Enhanced third-party access monitoring
- Documented vendor access baselines
- Strengthened vendor security requirements
- Added vendor incident reporting to contracts

## Common findings across organisations

Universal gaps:
- Living-off-the-land technique detection weak
- Cloud environment visibility insufficient
- Supply chain security inconsistent
- Incident response coordination needs practice

Effective controls:
- EDR catches most malware
- MFA prevents credential stuffing
- Network segmentation limits lateral movement
- Security awareness training reduces phishing success

Cultural observations:
- Blameless culture enables faster improvement
- Regular exercises build team confidence
- Metrics demonstrate progress to leadership
- Purple teaming catches gaps before audits do
