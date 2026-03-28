# Attack playbooks

Purple team exercises need realistic attack scenarios. These playbooks provide structured TTPs mapped to MITRE ATT&CK for consistent testing.

## Using playbooks effectively

Customise for your environment: Generic playbooks are starting points. Adapt for your technology stack, user behaviour, and threat model.

Progressive complexity: Start with basic techniques, add sophistication as defensive capabilities mature.

Test what matters: Focus on techniques relevant to threats your organisation actually faces.

## Initial access playbook

Phishing scenarios:
- Credential harvesting: Fake O365 login page, track submissions
- Malware delivery: Macro-enabled documents, test EDR and email filtering
- Link-based: Shortened URLs, test web proxy and user awareness

External vulnerability exploitation:
- Unpatched internet-facing services: Test vulnerability management
- Weak authentication: Password spraying, test account lockout and monitoring
- Misconfigured services: Exposed admin panels, test attack surface management

Supply chain vectors:
- Compromised vendor account: Simulate trusted third-party access abuse
- Malicious updates: Test software supply chain controls

## Credential access and privilege escalation

Credential theft:
- Mimikatz execution: Test EDR detection and response
- LSASS dumping: Test process protection and monitoring
- Registry credential extraction: SAM database access testing
- Browser password harvesting: Test endpoint monitoring

Privilege escalation:
- Exploit kernel vulnerabilities: Test patching and exploit protections
- Service misconfiguration abuse: Weak service permissions testing
- Token manipulation: Test for privileged token detection
- Scheduled task hijacking: Test for persistence detection

## Lateral movement and persistence

Lateral movement:
- Pass-the-hash: Test NTLM monitoring and prevention
- RDP and PSRemoting: Test legitimate admin tool abuse detection
- WMI and DCOM: Test lateral movement via Windows management protocols
- File share enumeration: Test for reconnaissance detection

Persistence:
- Registry run keys: Test startup process monitoring
- Scheduled tasks: Test task creation alerting
- WMI event subscriptions: Test for WMI persistence detection
- Service creation: Test for malicious service detection

## Data exfiltration simulation

Staging and collection:
- Large file transfers: Test DLP and unusual volume detection
- Compression of sensitive data: Test for data staging behaviours
- Access to sensitive shares: Test data access monitoring

Exfiltration techniques:
- HTTPS uploads: Legitimate protocol abuse testing
- DNS tunnelling: Test for DNS exfiltration detection
- Cloud storage: Test for unauthorised cloud service usage

## Playbooks

- [From access to staged data](https://red.tymyrddin.dev/docs/out/collection/playbooks)
- [Cloud initial access playbooks](https://red.tymyrddin.dev/docs/in/cloud/playbooks)
- [API attack playbooks](https://red.tymyrddin.dev/docs/in/api/playbooks)
- [Web application attack playbooks](https://red.tymyrddin.dev/docs/in/app/playbooks)
- [Attack chain playbooks for network operations](https://red.tymyrddin.dev/docs/in/network/playbooks)
- [Attack chain playbooks for endpoint operations](https://red.tymyrddin.dev/docs/in/endpoint/playbooks)
- [Evasion Playbooks](https://red.tymyrddin.dev/docs/through/evasion/playbooks)
- [Social engineering playbooks](https://red.tymyrddin.dev/docs/in/real/playbooks)

## Runbooks

- [Step-by-step attack runbooks](https://red.tymyrddin.dev/docs/in/real/runbooks)
- [Reverse engineering Runbooks](https://red.tymyrddin.dev/docs/through/reverse-engineering/runbooks)
- [Steganography Runbooks](https://red.tymyrddin.dev/docs/through/steganography/runbooks)
- [Crypto-attack Runbooks](https://red.tymyrddin.dev/docs/through/crypto-attacks/runbooks)
- [Buffer Overflow Runbooks](https://red.tymyrddin.dev/docs/through/buffer-overflow/runbooks)
- [Evasion Runbooks](https://red.tymyrddin.dev/docs/through/evasion/runbooks)
- [Persistence runbooks](https://red.tymyrddin.dev/docs/through/persistence/runbooks)
- [Finding and pulling the data](https://red.tymyrddin.dev/docs/out/collection/runbooks)
- [Moving the data](https://red.tymyrddin.dev/docs/out/exfiltration/runbooks)
- [Execution and concealment](https://red.tymyrddin.dev/docs/out/impact/runbooks)
- [Cloud recon runbooks](https://red.tymyrddin.dev/docs/in/cloud/runbooks)
- [API recon and attack runbooks](https://red.tymyrddin.dev/docs/in/api/runbooks)
- [Web application attack runbooks](https://red.tymyrddin.dev/docs/in/app/runbooks)
- [Operational procedures for network attacks](https://red.tymyrddin.dev/docs/in/network/runbooks)
- [Operational procedures for endpoint attacks](https://red.tymyrddin.dev/docs/in/endpoint/runbooks)
- [Operational procedures for OT attacks](https://red.tymyrddin.dev/docs/in/ot/runbooks)