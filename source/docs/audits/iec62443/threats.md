# Threats to the factory

The walls are built, the machines are running, the asset register is complete. Now it is about checking the weak 
points, confirming that every credible threat has a corresponding defence, and spotting gaps before an auditor does.

## Threat categories to check

1. Unauthorised access – Attempts to operate or reconfigure ICS devices without proper credentials.

   * Gap check: Confirm role-based access, account management, authentication mechanisms, and evidence of regular access reviews. Any missing records or unclear access rights are findings.

2. Malware and cyber intrusion – Including ICS-targeted malware, ransomware, or lateral movement from IT networks.

   * Gap check: Ensure network segmentation, firewall rules, application whitelisting, patch management, and monitoring logs are documented. Missing or incomplete evidence is a gap.

3. Insider threats – Misuse, misconfiguration, or sabotage by personnel.

   * Gap check: Verify separation of duties, privileged account monitoring, and operator responsibilities. Ambiguous ownership or missing monitoring logs is a finding.

4. Configuration and change errors – Misapplied updates, insecure defaults, or untracked changes.

   * Gap check: Confirm configuration baselines, version-controlled firmware/software, and documented change management. Missing steps are automatic findings.

5. Physical tampering – Direct interference with controllers, sensors, or network equipment.

   * Gap check: Confirm access controls, tamper-evident seals, surveillance coverage, and inspection logs. Any undocumented areas are gaps.

6. Supply chain and firmware risks – Vulnerable or compromised devices entering the environment.

   * Gap check: Verify device acceptance procedures, firmware validation, and vendor risk assessments. Missing documentation is a finding.

7. Network and protocol abuse – Exploitation of Modbus, OPC UA, DNP3, or other OT protocols.

   * Gap check: Ensure firewall rules, segmentation, anomaly detection, and protocol enforcement are documented. Gaps here are high priority.

## Practical gap‑spotting

* Threat vs. control mapping – Every threat must have a documented mitigation. Unmapped threats are immediate gaps.
* Evidence completeness – Logs, alerts, or inspection records must exist for each threat category.
* Zone relevance – Verify that threat assessment aligns with network/security zones. Threats outside documented zones indicate missing coverage.
* Incident readiness – Each threat category should have documented detection, response, and responsible personnel. Missing assignments or unclear procedures are findings.


*Treat this page as a checklist for post-deployment inspection: if a threat exists without documented 
mitigation, monitoring, or ownership, it is a gap that must be closed before anyone audits the system.*

