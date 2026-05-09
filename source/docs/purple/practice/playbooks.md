# Attack playbooks

Purple team exercises need realistic attack scenarios. Playbooks provide structured techniques mapped to MITRE ATT&CK so that the same ground can be tested consistently across exercises.

## Using playbooks well

The playbooks below are starting points, not finished products. Adapting them to a specific technology stack, user behaviour, and threat model is part of using them. Generic playbooks tested against a generic environment produce generic findings, which are usually less useful than the specific findings the practice is meant to produce.

Complexity is something to add gradually. Starting with the simplest techniques the existing detections are most likely to catch produces calibration; adding sophistication once those pass turns each exercise into a meaningful test rather than a brochure for advanced capability.

The point of testing is the techniques relevant to threats an organisation faces, not full ATT&CK coverage for its own sake. A coverage map is a useful artefact, but a coverage percentage is a metric that decouples easily from defensive value.

## Initial access

Phishing scenarios cover credential harvesting (a fake login page, tracking submissions), malware delivery (macro-enabled documents, testing EDR and email filtering), and link-based delivery (shortened URLs, testing web proxy and user awareness).

External vulnerability exploitation covers unpatched internet-facing services, weak authentication amenable to password spraying, and misconfigured services such as exposed admin panels.

Supply chain vectors cover compromised vendor accounts and malicious update paths.

## Credential access and privilege escalation

Credential theft includes Mimikatz execution against LSASS, registry credential extraction from the SAM database, and browser password harvesting.

Privilege escalation includes kernel exploitation, service-misconfiguration abuse, token manipulation, and scheduled-task hijacking.

## Lateral movement and persistence

Lateral movement covers pass-the-hash, RDP and PSRemoting, WMI and DCOM, and file share enumeration.

Persistence covers registry run keys, scheduled tasks, WMI event subscriptions, and service creation.

## Data exfiltration simulation

Staging and collection covers large file transfers, compression of sensitive data, and access to sensitive shares.

Exfiltration covers HTTPS uploads, DNS tunnelling, and cloud storage abuse.

## Playbooks

- [From access to staged data](https://red.tymyrddin.dev/docs/out/collection/playbooks)
- [Cloud initial access playbooks](https://red.tymyrddin.dev/docs/in/cloud/playbooks)
- [API attack playbooks](https://red.tymyrddin.dev/docs/in/api/playbooks)
- [Web application attack playbooks](https://red.tymyrddin.dev/docs/in/app/playbooks)
- [Attack chain playbooks for network operations](https://red.tymyrddin.dev/docs/in/network/playbooks)
- [Attack chain playbooks for endpoint operations](https://red.tymyrddin.dev/docs/in/endpoint/playbooks)
- [Evasion playbooks](https://red.tymyrddin.dev/docs/through/evasion/playbooks)
- [Social engineering playbooks](https://red.tymyrddin.dev/docs/in/real/playbooks)

## Runbooks

- [Step-by-step attack runbooks](https://red.tymyrddin.dev/docs/in/real/runbooks)
- [Reverse engineering runbooks](https://red.tymyrddin.dev/docs/through/reverse-engineering/runbooks)
- [Steganography runbooks](https://red.tymyrddin.dev/docs/through/steganography/runbooks)
- [Crypto-attack runbooks](https://red.tymyrddin.dev/docs/through/crypto-attacks/runbooks)
- [Buffer overflow runbooks](https://red.tymyrddin.dev/docs/through/buffer-overflow/runbooks)
- [Evasion runbooks](https://red.tymyrddin.dev/docs/through/evasion/runbooks)
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
