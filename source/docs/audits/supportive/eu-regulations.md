# EU regulations reference

These are legal instruments, not technical standards. They are freely available as published EU law, carry
mandatory obligations rather than guidance, and are enforced by national competent authorities rather than
certification bodies. Compliance is not a certificate you earn; it is a state you maintain under ongoing
supervisory oversight.

For purchasable technical standards (ISO 27001 series), see [ISO/IEC information security standards](standards.md).
For OT/ICS standards (IEC 62443 and related), see [OT/ICS standards](ot-standards.md).

## NIS2 Directive (2022/2555)

*Directive on measures for a high common level of cybersecurity across the Union*

Replaces NIS1 (2016/1148). Significantly broader in scope, covering more sectors and entity types, with
harmonised minimum penalties and direct obligations on management bodies.

Key features:

* Applies to essential and important entities in sectors defined in Annexes I and II
* Requires risk management measures under Article 21, including supply chain security, incident handling,
  cryptography, access control, and vulnerability management
* Mandates incident reporting to national CSIRTs or competent authorities within defined timelines (24-hour
  early warning, 72-hour notification, final report within one month)
* Places direct accountability on management bodies, who can be held personally liable for non-compliance
* Requires entities to register with national competent authorities in most member states

National transposition: Each EU member state was required to transpose NIS2 into national law by October 2024.
The Directive sets minimum requirements; member states may impose stricter obligations. Supervisory authority,
penalties, and specific sector thresholds vary by country. Check the national implementing legislation for the
relevant member states where your organisation operates.

The full text is available on EUR-Lex: [eur-lex.europa.eu](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX%3A32022L2555)

## DORA (2022/2554)

*Digital Operational Resilience Act*

Applies specifically to financial sector entities: banks, insurance companies, investment firms, payment
institutions, crypto-asset service providers, and their critical ICT third-party providers.

Where NIS2 and DORA overlap for financial entities, DORA takes precedence as the more sector-specific instrument.
DORA requirements for ICT risk management, incident reporting, digital operational resilience testing, and ICT
third-party risk broadly align with NIS2 Article 21 measures but are more prescriptive and include direct
regulatory oversight of critical third-party ICT providers by the European Supervisory Authorities (ESA).

Full text: [eur-lex.europa.eu](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX%3A32022R2554)

## CER Directive (2022/2557)

*Directive on the resilience of critical entities*

The physical resilience counterpart to NIS2. Where NIS2 addresses cybersecurity, CER addresses physical
resilience: natural hazards, terrorist attacks, insider threats, and sabotage affecting critical infrastructure.

CER applies to entities in the same sectors as NIS2, creating a paired framework. An energy operator, for
instance, faces NIS2 obligations for its network and information systems and CER obligations for its physical
infrastructure. The two directives share the same supervisory architecture and were designed to be implemented
in parallel.

Full text: [eur-lex.europa.eu](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX%3A32022L2557)

## Cyber Resilience Act (2024/2847)

*Regulation on horizontal cybersecurity requirements for products with digital elements*

Where NIS2 regulates organisations, the CRA regulates products: hardware and software with digital elements
placed on the EU market, from consumer devices to industrial components. The obligations fall primarily on
manufacturers, and they follow the product rather than the operator.

Key features:

* Essential cybersecurity requirements applied through conformity assessment and CE marking, with stricter
  assessment routes for products classed as important or critical
* Security by design and by default, including a defined support period during which manufacturers provide
  security updates
* Vulnerability handling obligations, including coordinated disclosure and a software bill of materials as
  part of the technical documentation
* Reporting of actively exploited vulnerabilities and severe incidents to the designated CSIRT and ENISA,
  with a 24-hour early warning followed by a 72-hour notification
* Penalties up to €15 million or 2.5 per cent of worldwide annual turnover

Timeline: entered into force in December 2024; the reporting obligations apply from September 2026 and the
main obligations from December 2027.

For audit work, the CRA changes the supply chain question. NIS2 Article 21 asks entities to manage supplier
and product risk; the CRA makes product-level security claims checkable, since a product with digital elements
carries conformity documentation an assessment can ask for. Procurement and supplier assessments can reference
CRA conformity the way they reference ISO certificates today, with the familiar caveat that conformity is
implementation evidence, not effectiveness evidence.

Full text: [eur-lex.europa.eu](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX%3A32024R2847)

## AI Act (2024/1689)

*Regulation laying down harmonised rules on artificial intelligence*

A risk-based framework for AI systems placed on the EU market or put into service: prohibited practices,
high-risk systems listed in Annex III (including safety components of critical infrastructure and biometric
systems), transparency obligations for limited-risk uses, and a separate regime for general-purpose AI models.

Key features:

* High-risk AI systems require conformity assessment, technical documentation, human oversight measures,
  operational logging, and registration before deployment
* Obligations fall on providers and on deployers; an entity operating a high-risk AI system has its own
  duties around use, oversight, and monitoring, whether or not it built the system
* Penalties up to €35 million or 7 per cent of worldwide annual turnover for prohibited practices, with lower
  tiers for other infringements
* Phased application: entered into force in August 2024, with prohibitions applying from February 2025,
  general-purpose model obligations from August 2025, and most high-risk obligations from August 2026

The intersection with security work runs both ways: AI systems inside an essential entity's operations may
carry high-risk obligations alongside the NIS2 measures, and AI tooling used in audit and compliance
workflows raises its own questions, covered in [Use of AI in audits](ai-in-audits.md).

Full text: [eur-lex.europa.eu](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX%3A32024R1689)

## GDPR (2016/679)

*General Data Protection Regulation*

Applies to any organisation processing personal data of EU residents, regardless of where the organisation is
based. Directly applicable in all member states without transposition.

Relevant intersection with NIS2:

* Article 33 of GDPR requires notification of personal data breaches to supervisory authorities within 72 hours,
  which overlaps with NIS2 incident reporting for incidents that also involve personal data
* Security of processing (Article 32) requires appropriate technical and organisational measures, which
  overlaps substantially with NIS2 Article 21 risk management measures
* Where an incident triggers both GDPR and NIS2 reporting obligations, both sets of requirements apply
  independently and to different authorities (data protection authority vs. NIS competent authority)

Full text: [eur-lex.europa.eu](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX%3A32016R0679)

## How these interact

| Regulation | Primary scope                                 | Enforcer                                          | Overlap with NIS2                                   |
|:-----------|:----------------------------------------------|:--------------------------------------------------|:-----------------------------------------------------|
| NIS2       | Cybersecurity of essential/important entities | National NIS competent authority                  | Core framework                                       |
| DORA       | Financial sector ICT resilience               | ESA (EBA, EIOPA, ESMA)                            | Lex specialis for financial entities                 |
| CER        | Physical resilience of critical entities      | National CER competent authority                  | Parallel physical layer                              |
| CRA        | Security of products with digital elements    | National market surveillance authorities          | Product layer under Article 21 supply chain security |
| AI Act     | AI systems on the EU market or in service     | Market surveillance authorities; EU AI Office     | High-risk AI within essential entities' operations   |
| GDPR       | Personal data protection                      | National data protection authority                | Incident reporting, Article 32 measures              |

An organisation subject to multiple instruments does not get a choice between them. Each applies within its
own scope simultaneously. Where requirements overlap, the more specific instrument typically provides the
operative obligation, but the others still apply to their respective domains.

## Related

* [NIS2 Understanding the river](../nis2/river.md)
* [NIS2 Staying afloat](../nis2/afloat.md)
* [Use of AI in audits](ai-in-audits.md)
* [Supply chain and third-party risk](supply-chain.md)
* [ISO/IEC information security standards](standards.md)

*Last updated: 4 July 2026*
