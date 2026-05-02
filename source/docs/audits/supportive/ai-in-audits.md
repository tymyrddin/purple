# Use of AI in audits

AI tooling is entering audit and compliance workflows faster than the governance frameworks for using it have
matured. That gap is worth acknowledging before picking tools. The sections below cover where AI genuinely
adds value in audit work, what to watch for when deploying it in a compliance context, and EU-specific
considerations including the AI Act.

## Where AI adds value

AI tools address different problems from BI and analytics tools. BI surfaces what happened in data you already
have. AI can interpret unstructured data, identify patterns too subtle or numerous for manual review, and
generate outputs at a scale that human analysts cannot match. In audit work, the most productive current uses
are:

* Log and event analysis: ML-based anomaly detection in SIEM platforms, identifying unusual behaviour patterns
  in access logs, authentication events, and network traffic. Reduces alert fatigue by prioritising signals
  rather than presenting every event.

* Document and evidence review: NLP for classifying and extracting information from policy documents,
  contracts, and supplier questionnaires. Useful for initial gap analysis across large document sets, or for
  checking whether policy language covers required control areas.

* Continuous control testing: automated comparison of configuration snapshots against baselines, identifying
  configuration drift between review cycles without requiring manual comparison.

* Risk scoring and prioritisation: ranking assets, vulnerabilities, or findings by modelled risk, particularly
  useful when asset inventories are large enough that manual prioritisation becomes inconsistent.

* Phishing and awareness simulation: AI-generated phishing scenarios that reflect current attack patterns and
  adapt to the target organisation's communications context, producing more realistic tests than template-based
  approaches.

* Supplier and third-party screening: automated analysis of public information, questionnaire responses, and
  certifications to flag vendors whose profile merits deeper review.

## Limitations worth naming

AI tools encode model assumptions in the same way any other control does. Where those assumptions do not hold,
the tool will produce outputs that look authoritative while being wrong.

Hallucination in document review is the most immediate risk: a tool summarising a 40-page policy may report
that a control is covered when the coverage is partial or conditional. Outputs from AI document review warrant
spot-checking against source material, especially for findings that will appear in compliance evidence.

Explainability is a practical audit problem. A finding based on anomaly detection needs to be explainable to
an auditor or supervisory authority. If the reasoning behind a risk score or control gap cannot be articulated
in human terms, the finding has limited value as evidence, regardless of how accurate the underlying model is.

Training data bias affects risk scoring: models trained on historical incident and vulnerability data may
systematically underweight novel threat patterns or attack techniques that have not yet appeared in the
training corpus. A risk score that does not recognise a current attacker technique is not a conservative
risk score; it is a gap dressed as a number.

Over-reliance follows naturally from how useful these tools are when they work. AI-assisted gap analysis
supplements human judgement and does not replace it. Outputs from any AI tool in this workflow need to be
evaluated against specific organisational context before being used as compliance evidence: the model
identifies candidates; the person reviewing decides whether they are findings.

## EU AI Act (Regulation 2024/1689)

The EU AI Act entered into force in August 2024, with obligations phasing in through 2025 and 2026. It
classifies AI systems by risk level and applies requirements accordingly.

AI systems used in security-relevant contexts may fall under the high-risk category in Annex III, particularly
those used for critical infrastructure management, access control, or biometric identification. High-risk AI
systems require:

* A conformity assessment before deployment
* Transparency documentation (technical documentation and instructions for use)
* Human oversight measures ensuring that a human can intervene, override, or halt the system
* Logging of operation to support post-event auditing
* Registration in the EU database of high-risk AI systems

For compliance tooling specifically: an AI system that automates risk decisions or generates outputs used
directly in regulatory evidence may attract closer scrutiny under the Act than one that assists a human
reviewer exercising independent judgement. The distinction between AI as decision support and AI as decision
maker is consequential for how the organisation's compliance evidence is characterised under the Act.

The full regulation is available at [eur-lex.europa.eu](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX%3A32024R1689)

## Data residency and GDPR

Audit data often contains personal data (access logs with usernames, incident reports naming individuals,
training records) or commercially sensitive operational detail. Sending this data to a US-hosted AI service
for analysis raises GDPR and data transfer questions that need to be addressed before deployment, not after.

Practical options include EU-hosted deployments of open-weight models, on-premises inference, or EU-hosted
cloud AI services from providers with adequacy or appropriate safeguards in place. The European Data
Protection Board has published guidance on AI and personal data; supervisory authorities in several member
states have issued enforcement decisions relevant to AI data processing.

## EU-leaning tools

Several open-source or EU-anchored tools are in use for AI-assisted audit and security monitoring:

* [Elastic Security](https://www.elastic.co/security) (open source, self-hostable): ML-based anomaly
  detection and SIEM capabilities. Deployable on EU infrastructure. Widely used for log analysis and
  behavioural anomaly detection in compliance-heavy environments.

* [Wazuh](https://wazuh.com/) (open source): security monitoring, intrusion detection, and compliance
  reporting platform with rule-based and ML-assisted detection. Self-hosted, EU deployable, no data
  residency concerns.

* [OpenSearch Security](https://opensearch.org/docs/latest/security/) (open source, AWS-neutral fork):
  search and analytics with security plugins. Deployable on EU infrastructure, used for log aggregation
  and pattern analysis.

For document review and AI-assisted policy analysis, deployment model counts for more than product choice:
most capable LLMs have EU-hosted API options or can be deployed locally with open-weight models, and the
choice between them depends primarily on the sensitivity of the documents being processed.

## Related

* [Use of big data in audits](big-data.md)
* [Continuous compliance monitoring](continuous-monitoring.md)
* [EU regulations reference](eu-regulations.md)
* [Gap analysis](gap-analysis.md)
* [ISO 27001 Base camp check](../iso27001/base-camp-check.md)
* [ISO 27001 Flag](../iso27001/flag.md) (ongoing monitoring and surveillance cycle)
* [NIS2 Staying afloat](../nis2/afloat.md) (continuous monitoring metrics where AI tooling applies directly)
* [IEC 62443 The paper trail under inspection](../iec62443/evidence.md) (AI-assisted evidence collection in OT environments)
* [NIS2 Building the vessel](../nis2/raft.md) (AI-generated phishing simulations covered in the people and culture section)
