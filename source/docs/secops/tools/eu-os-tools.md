# European SecOps architectures using open source

## Core objectives

* Threat detection and response: Spot and react to incidents fast.
* Intelligence-driven operations: Use structured threat intelligence for context.
* Compliance and auditability: Meet GDPR and EU data sovereignty rules.
* Automation without overreach: Reduce repetitive work, keep humans in the loop.

## Core components

### A. Security Information and Event Management (SIEM)

* Wazuh: Log collection, integrity monitoring, alerting, and compliance.
* Alternative EU-friendly options: OSSEC, ELK stack (Elastic only if hosted self-managed in EU).
* Function: Centralised log analysis, correlation rules, automated alert generation.

### B. Threat Intelligence Platform

* MISP (Malware Information Sharing Platform):

  * Central hub for structured threat intelligence (IOCs, campaigns, TTPs).
  * Supports collaboration with EU CERTs and peer organisations.
* Function: Feed alerts and enrich log events in SIEM, automate IOC ingestion.

### C. Security Orchestration, Automation, and Response (SOAR)

* TheHive + Cortex (European-friendly open source SOAR):

  * TheHive: Case management, incident tracking, workflow enforcement.
  * Cortex: Automated enrichment of observables (IP, hash, domain) using MISP and other sources.
* Function: Triage, automate repetitive enrichment, provide auditable workflows.

### D. Endpoint Detection and Response (EDR)

* Wazuh agents on endpoints and servers:

  * Collect file integrity, rootkit detection, log events.
  * Send alerts to Wazuh manager, integrate with SOAR for automated response.

### E. Network Security Monitoring

* Zeek (Bro) for network traffic analysis.
* Optional European-friendly IDS: Suricata.
* Function: Detect lateral movement, suspicious traffic, anomalies. Feed into SIEM.

### F. Vulnerability Management

* OpenVAS / Greenbone:

  * Regular scans, EU-hosted CVE data.
  * Feed findings into TheHive for prioritised remediation actions.

### G. Automation & Orchestration Layer

* Ansible / StackStorm for procedural response tasks:

  * Blocking IPs, quarantining endpoints, enriching logs.
  * Controlled by SOAR workflows.

### H. Dashboards & Reporting

* Wazuh Kibana dashboards, Grafana visualisation.
* Compliance reports, SOC/SIRT KPIs, MISP enrichment stats.

## Data flows (high-level)

1. Endpoints and network devices → Wazuh / Zeek / Suricata → SIEM.
2. SIEM events → Correlation engine → Alerts → TheHive (cases).
3. Cases → Cortex → MISP enrichment → Update case context.
4. SOAR automation → Ansible/StackStorm → Response actions (containment, notifications).
5. Vulnerability scans → OpenVAS → TheHive → Remediation tickets.
6. Dashboards → SOC/SIRT review → Continuous improvement loop.

## Integration highlights

* Wazuh ↔ MISP: Automated IOC enrichment.
* TheHive ↔ Cortex ↔ MISP: Rapid observable enrichment and response.
* OpenVAS ↔ TheHive: Automated ticketing for patchable vulnerabilities.
* Zeek / Suricata ↔ Wazuh: Centralised alert correlation.

## Considerations

* Self-hosted only to stay GDPR compliant.
* Data localisation: Keep MISP, logs, and dashboards within EU jurisdictions.
* Strong access control: Role-based permissions in Wazuh, TheHive, and MISP.
* Encryption at rest & in transit (TLS 1.3 for all internal comms).
* Open-source support via European communities to avoid vendor lock-in.

## Suggested deployment pattern

* Core SIEM & SOAR: On-premises or EU cloud (private cloud).
* MISP instance: On-premises, with federated sharing (peer orgs only).
* Endpoint agents: On corporate endpoints and servers.
* Network sensors: Inline or tap mode, minimal latency.
* Automation nodes: Isolated network segment, controlled playbooks.

## Examples

* [Small organisation SecOps stack](small-stack.md): 1–50 employees, limited IT staff, low budget, but still wants structured security.
* [Medium organisation SecOps stack](medium-stack.md): Scope: 50–500 employees, dedicated IT/Security staff, need more visibility and automation.

```{raw} html
<div class="page-post-card__link">
    <a href="https://tymyrddin.dev/contact/">
      Explore the tools that make your security work
    </a>
</div>
```

