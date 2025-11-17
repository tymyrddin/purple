# Arrows and shields

CWE, CAPEC, and MITRE ATT&CK describe attacks, vulnerabilities, and tactics. ISO27001 and NIS2 describe what 
organisations must do to protect against them. In other words: one set labels the arrows, the other sets the 
shields.

## Web & application attacks

These attacks target web applications and APIs. They exploit weaknesses in code, configuration, or design to 
compromise systems or data.

| Threat                             | CWE/CAPEC/ATT&CK               | ISO 27001 Conceptual Control                           | NIS2 Conceptual Obligation                           |
|------------------------------------|--------------------------------|--------------------------------------------------------|------------------------------------------------------|
| Remote code execution              | CWE-94, CAPEC-112, T1059/T1190 | Secure development, patch management, system hardening | Protect systems, detect incidents, respond           |
| Cross-site scripting (XSS)         | CWE-79, CAPEC-86, T1059.007    | Input validation, application testing                  | Protect applications, prevent exploitation           |
| SQL injection                      | CWE-89, CAPEC-66, T1190        | Input validation, database access control              | Secure apps, prevent attacks, handle incidents       |
| Unvalidated redirects/forwards     | CWE-601, CAPEC-123, T1204      | Input validation, secure coding                        | Prevent abuse, monitor suspicious activity           |
| Remote file inclusion (RFI)        | CWE-98, CAPEC-33, T1505        | Input validation, secure coding                        | Prevent exploitation, monitor applications           |
| Local file inclusion (LFI)         | CWE-59, CAPEC-33, T1505        | Access control, input validation                       | Prevent access to sensitive files, incident response |
| Insecure deserialisation           | CWE-502, CAPEC-239, T1221      | Input validation, application hardening                | Protect against exploits, monitor applications       |
| XML external entity (XXE)          | CWE-611, CAPEC-183, T1105      | Input validation, parser hardening                     | Prevent exploitation, respond                        |
| Server-side request forgery (SSRF) | CWE-918, CAPEC-312, T1071      | Secure coding, network segmentation                    | Protect systems, respond to malicious requests       |
| Clickjacking / UI attacks          | CWE-1021, CAPEC-242, T1201     | Secure UI design, input validation                     | Prevent clickjacking, monitor usage                  |
| Cross-site request forgery (CSRF)  | CWE-352, CAPEC-62, T1059       | CSRF tokens, secure session management                 | Prevent unauthorised actions, validate requests      |
| Command injection                  | CWE-77, CAPEC-88, T1059        | Input validation, least privilege                      | Prevent command execution, monitor systems           |
| Path manipulation                  | CWE-73, CAPEC-126, T1083       | Input validation, access control                       | Prevent directory traversal, protect files           |

Web applications are often the most exposed part of your infrastructure, accessible from anywhere on the internet. 
A single vulnerability can provide initial access for attackers, making secure development and testing critical 
compliance requirements.

## Authentication and access

These attacks target how users and systems prove identity and what they're allowed to access. Successful attacks here 
often provide the initial foothold for broader compromise.

| Threat                         | CWE/CAPEC/ATT&CK              | ISO 27001 Conceptual Control              | NIS2 Conceptual Obligation                         |
|--------------------------------|-------------------------------|-------------------------------------------|----------------------------------------------------|
| Authentication bypass          | CWE-287, CAPEC-118, T1078     | Access control, identity management       | Prevent unauthorised access, assign accountability |
| Privilege escalation           | CWE-269/264, CAPEC-261, T1068 | Least privilege, access review            | Apply access control, manage oversight             |
| Lateral movement               | CWE-287/264, CAPEC-258, T1021 | Segregation of duties, monitoring         | Detect lateral attacks, prevent spread             |
| Misuse of privileged accounts  | CWE-264, CAPEC-261, T1078     | Privileged account management, monitoring | Monitor accounts, prevent abuse                    |
| Replay attacks                 | CWE-290, CAPEC-111, T1550     | Session controls, authentication          | Prevent reuse of credentials, detect abuse         |
| Credential stuffing            | CWE-307, CAPEC-210, T1110     | Password policies, MFA, monitoring        | Detect automated attacks, enforce authentication   |
| Password attacks (brute force) | CWE-307, CAPEC-49, T1110      | Strong passwords, account lockout, MFA    | Protect accounts, detect attacks, enforce policies |
| Session hijacking              | CWE-384, CAPEC-21, T1185      | Secure session management, encryption     | Protect sessions, detect unauthorised access       |
| Token manipulation             | CWE-565, CAPEC-21, T1550      | Token security, validation, expiration    | Validate tokens, detect manipulation               |

Authentication is the first line of defence. If attackers bypass or compromise authentication, all other controls 
become irrelevant. Multifactor authentication (MFA) is mandatory under NIS2 Article 21 specifically because of 
how critical this control is.

## Network & system attacks

These attacks target network infrastructure and operating systems, often aiming for availability disruption or 
establishing persistent access.

| Threat                      | CWE/CAPEC/ATT&CK          | ISO 27001 Conceptual Control               | NIS2 Conceptual Obligation                     |
|-----------------------------|---------------------------|--------------------------------------------|------------------------------------------------|
| Denial of service (DoS)     | CWE-400, CAPEC-152, T1499 | Availability management, redundancy        | Ensure continuity, detect and respond          |
| Man-in-the-middle (MITM)    | CWE-300, CAPEC-111, T1557 | Encryption, session protection             | Protect communications, detect intrusions      |
| Buffer overflow             | CWE-120, CAPEC-100, T1203 | Input validation, hardening                | Protect systems, respond to compromise         |
| Path traversal              | CWE-22, CAPEC-126, T1190  | File access controls, configuration        | Protect sensitive resources, incident response |
| Rogue device / access point | CWE-693, CAPEC-550, T1596 | Network security, asset monitoring         | Detect unauthorised devices, protect network   |
| Wireless / network attacks  | CWE-749, CAPEC-152, T1573 | Network security, encryption, segmentation | Detect intrusions, protect communications      |
| DNS attacks (poisoning)     | CWE-350, CAPEC-142, T1584 | DNS security, monitoring                   | Protect DNS, detect tampering                  |
| ARP spoofing                | CWE-300, CAPEC-603, T1557 | Network monitoring, segmentation           | Detect spoofing, protect communications        |
| Port scanning / enumeration | N/A, CAPEC-300, T1046     | Firewall rules, monitoring, IDS            | Detect reconnaissance, limit exposure          |

Network attacks often represent the reconnaissance and initial access phases of an intrusion. Detecting and 
preventing these early-stage attacks stops incidents before they escalate. NIS2's requirement for network 
segmentation (Article 21) directly addresses limiting lateral movement after initial compromise.

## Malware and advanced (persistent) threats

These attacks involve malicious software and sophisticated, often persistent campaigns. They represent some of the 
most damaging threats organisations face.

| Threat                           | CWE/CAPEC/ATT&CK          | ISO 27001 Conceptual Control                | NIS2 Conceptual Obligation                     |
|----------------------------------|---------------------------|---------------------------------------------|------------------------------------------------|
| Malware (ransomware, trojans)    | CWE-914, CAPEC-238, T1486 | Anti-malware, patching, backup & recovery   | Detect malware, isolate, restore systems       |
| Fileless malware                 | CWE-502, CAPEC-244, T1055 | Endpoint protection, monitoring             | Detect anomalous behaviour, respond            |
| Advanced persistent threat (APT) | CWE-242, CAPEC-159, T1071 | Monitoring, incident response, threat intel | Detect advanced threats, coordinate response   |
| Data exfiltration                | CWE-200, CAPEC-238, T1041 | Logging, classification, access control     | Detect breaches, protect sensitive information |
| Data manipulation / tampering    | CWE-117, CAPEC-259, T1070 | Integrity checks, logging, access control   | Detect tampering, maintain integrity, respond  |
| Rootkits                         | CWE-912, CAPEC-552, T1014 | System hardening, integrity monitoring      | Detect rootkits, rebuild compromised systems   |
| Cryptojacking                    | N/A, CAPEC-388, T1496     | Resource monitoring, endpoint protection    | Detect unauthorised use, protect resources     |
| Backdoors / remote access        | CWE-912, CAPEC-681, T1546 | Code review, monitoring, access control     | Detect backdoors, prevent persistence          |
| Zero-day exploits                | Various, Various, T1203   | Defence in depth, monitoring, patching      | Detect exploitation, rapid response            |

Ransomware is one of the most significant threats organisations face today. NIS2's requirement for tested backups 
and business continuity (Article 21) directly addresses ransomware resilience. Advanced persistent threats (APTs) 
are the reason for mandatory logging, monitoring, and incident detection requirements.

## Social engineering & supply chain

These attacks target people and trust relationships rather than technical vulnerabilities. They are often the most 
effective because they exploit human psychology and organisational dependencies.

| Threat                          | CWE/CAPEC/ATT&CK              | ISO 27001 Conceptual Control                   | NIS2 Conceptual Obligation                         |
|---------------------------------|-------------------------------|------------------------------------------------|----------------------------------------------------|
| Phishing / social engineering   | CWE-601/642, CAPEC-163, T1566 | Security awareness training, access management | Train staff, monitor incidents, respond            |
| Supply chain compromise         | CWE-1108, CAPEC-245, T1195    | Supplier assessment, change management         | Monitor vendors, implement security measures       |
| Exploit of third-party software | CWE-937, CAPEC-239, T1195     | Supplier assessment, patching                  | Monitor vendor security, remediate vulnerabilities |
| Spear phishing                  | CWE-601, CAPEC-163, T1566     | Awareness training, email security             | Train staff, detect targeted attacks               |
| Business email compromise (BEC) | CWE-601, CAPEC-163, T1566     | Email authentication, process controls         | Verify requests, detect fraud                      |
| Insider threats                 | CWE-284, CAPEC-1, T1078       | Background checks, monitoring, least privilege | Detect insider activity, enforce controls          |
| Watering hole attacks           | CWE-79, CAPEC-60, T1189       | Web filtering, monitoring, patching            | Protect users, detect compromise                   |
| Pretexting / impersonation      | N/A, CAPEC-383, T1598         | Verification procedures, awareness training    | Train staff, verify identity                       |
| Software supply chain attacks   | CWE-1357, CAPEC-437, T1195    | Software vetting, integrity checks             | Verify software, monitor supply chain              |

Social engineering bypasses technical controls by exploiting human trust. Security awareness training is mandatory 
under both ISO 27001 (Annex A.6.3) and NIS2 (Article 21) because technical controls alone cannot stop these attacks. 
Supply chain security is explicitly required in NIS2 Article 21 following high-profile incidents like SolarWinds 
and Kaseya.

## Data & privacy attacks

These attacks specifically target the confidentiality and privacy of sensitive information, often with regulatory 
implications.

| Threat                            | CWE/CAPEC/ATT&CK          | ISO 27001 Conceptual Control               | NIS2 Conceptual Obligation                      |
|-----------------------------------|---------------------------|--------------------------------------------|-------------------------------------------------|
| Data breach / unauthorised access | CWE-200, CAPEC-116, T1530 | Access control, encryption, classification | Protect data, detect breaches, report incidents |
| Privacy violations                | CWE-359, CAPEC-37, T1530  | Privacy controls, data minimisation        | Protect personal data, comply with GDPR         |
| Information disclosure            | CWE-200, CAPEC-116, T1083 | Access control, logging, classification    | Prevent disclosure, monitor access              |
| Metadata leakage                  | CWE-212, CAPEC-116, T1087 | Data sanitisation, secure configuration    | Prevent leakage, protect metadata               |
| Cloud data exposure               | CWE-668, CAPEC-116, T1530 | Cloud security, access control             | Secure cloud storage, monitor access            |

Data breaches trigger mandatory incident reporting under NIS2 Article 23 and GDPR. The intersection of cybersecurity 
and data protection regulations means data-focused attacks have both operational and legal consequences.

## Cryptographic attacks

These attacks target how organisations protect data through encryption and cryptographic controls.

| Threat                        | CWE/CAPEC/ATT&CK          | ISO 27001 Conceptual Control                 | NIS2 Conceptual Obligation               |
|-------------------------------|---------------------------|----------------------------------------------|------------------------------------------|
| Weak encryption               | CWE-327, CAPEC-20, T1573  | Cryptographic controls, key management       | Use strong encryption, protect keys      |
| Certificate attacks           | CWE-295, CAPEC-459, T1587 | Certificate management, validation           | Validate certificates, detect tampering  |
| Protocol downgrade attacks    | CWE-757, CAPEC-220, T1557 | Enforce strong protocols, monitoring         | Prevent downgrades, protect sessions     |
| Key management failures       | CWE-320, CAPEC-97, T1552  | Key lifecycle management, access control     | Protect keys, rotate regularly           |

Encryption is mandatory under NIS2 Article 21. Poor cryptographic practices render this control ineffective. 
Understanding cryptographic attacks helps you implement encryption correctly rather than just checking a compliance box.

## Physical & environmental attacks

These attacks target physical access to systems, facilities, or infrastructure, often overlooked in cybersecurity discussions but explicitly covered in compliance frameworks.

| Threat                      | CWE/CAPEC/ATT&CK          | ISO 27001 Conceptual Control        | NIS2 Conceptual Obligation              |
|-----------------------------|---------------------------|-------------------------------------|-----------------------------------------|
| Physical access intrusion   | N/A, CAPEC-396, T1200     | Physical security, access control   | Protect facilities, monitor access      |
| Media theft                 | CWE-922, CAPEC-507, T1200 | Media protection, secure disposal   | Protect media, track assets             |
| Environmental threats       | N/A, N/A, N/A             | Environmental controls, continuity  | Ensure availability, protect systems    |
| USB/removable media attacks | CWE-427, CAPEC-626, T1091 | Device control, endpoint protection | Control removable media, detect malware |

While cyberattacks dominate headlines, physical security remains foundational. Many successful breaches began with 
physical access to facilities or theft of equipment. ISO 27001 Annex A.7 and A.11 address physical security explicitly.

## Practical application

### For ISO 27001 implementation

When implementing controls from Annex A, use this mapping to understand which attack patterns each control addresses. 
For example:

- A.8.3 (Access control) addresses authentication bypass (CWE-287), privilege escalation (CWE-269), and lateral movement
- A.8.7 (Protection against malware) addresses malware (T1486), fileless malware (T1055), and ransomware
- A.8.16 (Monitoring activities) addresses APT (T1071), data exfiltration (T1041), and insider threats

### For NIS2 compliance

NIS2 Article 21 requires specific measures. This mapping shows which threats each measure addresses:

- Multifactor authentication prevents authentication bypass (CWE-287), credential stuffing (T1110), and password attacks
- Network segmentation limits lateral movement (T1021), contains breaches, and reduces attack surface
- Supply chain security addresses supply chain compromise (T1195), third-party software exploits, and vendor risks
- Incident handling responds to all attack categories but particularly critical for ransomware (T1486), data breaches (CWE-200), and APT (T1071)

### For risk assessment

Use this mapping to prioritise threats:

1. Identify which attacks are most likely in your sector (e.g., healthcare faces ransomware and data breaches; financial services face authentication attacks and fraud)
2. Check whether you have effective controls for high-priority threats
3. Document residual risk for threats where controls are incomplete or proportionately limited
4. Use attack patterns to justify security investments to leadership

### For incident response

When investigating incidents:

1. Map observed indicators to MITRE ATT&CK techniques
2. Identify related CWE/CAPEC patterns to understand the vulnerability exploited
3. Check which ISO 27001 controls should have prevented or detected the attack
4. Verify NIS2 incident reporting obligations based on impact and threat type
5. Document lessons learned to improve controls

## Additional resources

* [MITRE ATT&CK](https://attack.mitre.org/): Comprehensive knowledge base of adversary tactics and techniques based on real-world observations.
* [CWE (Common Weakness Enumeration)](https://cwe.mitre.org/): Community-developed list of software and hardware weakness types.
* [CAPEC (Common Attack Pattern Enumeration and Classification)](https://capec.mitre.org/): Comprehensive dictionary of known attack patterns used by adversaries.
* [ISO/IEC 27001:2022](https://www.iso.org/obp/ui#iso:pub:PUB100484): International standard for information security management systems.
* [NIS2 Directive (EU 2022/2555)](https://www.nis2-info.eu/): EU directive on security of network and information systems.

## Disclaimers

This mapping is conceptual and not exhaustive. Attack patterns evolve, new vulnerabilities emerge, and threat 
actors develop novel techniques. Use this as a framework for understanding relationships between threats and 
controls, not as a complete checklist.

Both ISO 27001 and NIS2 are risk-based frameworks requiring you to assess your specific threat landscape and 
implement proportionate controls. This mapping helps connect threat intelligence to compliance requirements, 
but any implementation must reflect the organisation's unique context, risks, and capabilities.
