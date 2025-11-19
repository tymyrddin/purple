# Scoping engagements

Scope defines what's in bounds and what's off limits. Clear scope prevents accidents and focuses testing on objectives.

## Technical scope

Systems in scope: Which networks, systems, applications, cloud environments can be tested? Be specific. "Production environment" is too broad. "Production web application running on servers A, B, C" is clear.

Systems out of scope: What must not be touched? Payment processing systems? Medical devices? HR systems containing sensitive data?

Attack vectors allowed: Social engineering? Physical access? Supply chain? Constrain to relevant threats and available resources.

Time windows: When can testing occur? Avoid critical business periods, change freezes, major events.

## Organisational scope

Teams involved: Who participates? Just SOC? Include IT operations? Security engineering? Communications team?

Stakeholders informed: Who needs to know exercise is happening? Leadership? Legal? Communications? All staff?

Geographic scope: Single office? Multiple locations? Remote workforce? Cloud infrastructure?

Third parties: Can testing involve vendors, partners, or customers? Usually not without their explicit consent.

## Depth and intensity

Reconnaissance: How deep can red team probe? Active scanning? Just passive OSINT?

Exploitation: Can vulnerabilities be exploited? Or just identified and reported?

Post-exploitation: How far can red team go after initial access? Full domain compromise? Exfiltration simulation?

Impact: Can operations be disrupted? Usually not in production. Testing must stay safe.
