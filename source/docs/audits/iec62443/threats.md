# Threats to the factory

The walls are built, the machines are running, the asset register is complete. Now it is about checking the weak 
points, confirming that every credible threat has a corresponding defence, and spotting gaps before an auditor does.

## Threat categories to check

1. Unauthorised access – Attempts to operate or reconfigure ICS devices without proper credentials. Gap check: Confirm role-based access, account management, authentication mechanisms, and evidence of regular access reviews. Any missing records or unclear access rights are findings.
2. Malware and cyber intrusion – Including ICS-targeted malware, ransomware, or lateral movement from IT networks. Gap check: Ensure network segmentation, firewall rules, application whitelisting, patch management, and monitoring logs are documented. Missing or incomplete evidence is a gap.
3. Insider threats – Misuse, misconfiguration, or sabotage by personnel. Gap check: Verify separation of duties, privileged account monitoring, and operator responsibilities. Ambiguous ownership or missing monitoring logs is a finding.
4. Configuration and change errors – Misapplied updates, insecure defaults, or untracked changes. Gap check: Confirm configuration baselines, version-controlled firmware/software, and documented change management. Missing steps are automatic findings.
5. Physical tampering – Direct interference with controllers, sensors, or network equipment. Gap check: Confirm access controls, tamper-evident seals, surveillance coverage, and inspection logs. Any undocumented areas are gaps.
6. Supply chain and firmware risks – Vulnerable or compromised devices entering the environment. Gap check: Verify device acceptance procedures, firmware validation, and vendor risk assessments. Missing documentation is a finding.
7. Network and protocol abuse – Exploitation of Modbus, OPC UA, DNP3, or other OT protocols. Gap check: Ensure firewall rules, segmentation, anomaly detection, and protocol enforcement are documented. Gaps here are high priority.

Threat assessment works in the rational domain: map attack vectors, verify control coverage, check documentation. A 
threat register built from this process alone will be systematically incomplete. The [emotional layer](../../foundations/problem-solving/three-domains.md) asks which 
threats are difficult to name: insider threat is chronically underrepresented not because it is rare but because 
naming it implicates colleagues and changes the dynamic of the session. A privileged operator whose access has never 
been reviewed is a threat scenario; raising it publicly has social consequences. The [political layer](../../foundations/problem-solving/three-domains.md) asks whose 
interests are served by particular threat framings: a protocol vulnerability in a system owned by a team under 
production pressure tends toward accepted risk regardless of actual impact. An unusually high acceptance rate for a 
specific threat category is worth examining for incentive misalignment before treating documentation coverage as 
complete.

Each threat category is also a test scenario. Unauthorised access can be tested through credential validation 
exercises and access review spot-checks against live systems. Malware and intrusion can be tested through controlled 
PoC execution against representative targets in a staging environment. Protocol abuse can be tested through targeted 
protocol fuzzing or a red team exercise scoped to OT protocols. Threats that exist only as documentation categories, 
without any history of being tested against, are assumptions about how the ICS environment will respond under attack, 
not findings.

## Practical gap‑spotting

* Threat vs. control mapping – Every threat must have a documented mitigation. Unmapped threats are immediate gaps.
* Evidence completeness – Logs, alerts, or inspection records must exist for each threat category.
* Zone relevance – Verify that threat assessment aligns with network/security zones. Threats outside documented zones indicate missing coverage.
* Incident readiness – Each threat category should have documented detection, response, and responsible personnel. Missing assignments or unclear procedures are findings.

*If a threat exists without documented mitigation, monitoring, or ownership, it is a gap that must be closed before anyone audits the system.*

## Related

* [ISO 22301 Storms on the factory floor](../iso22301/threats.md)
* [NIS2 Understanding the river](../../audits/nis2/river.md)
* [ISO 27001 Risk tent](../../audits/iso27001/risk-tent.md)
* [Unseen University Power & Light Co. IT/OCS pentest](https://red.tymyrddin.dev/docs/power/)
* [Threat modelling as a process](../../workshops/threat-modelling.md)
* [Gap analysis](../supportive/gap-analysis.md)
