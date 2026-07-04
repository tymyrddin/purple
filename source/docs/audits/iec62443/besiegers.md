# Knowing the besiegers

Threats, adversaries, and risk assessment.

The walls are built, the machines are running, the survey is complete. Before deciding where the walls need to be
highest, work out who might come over them and how. IEC 62443-3-2 frames this as risk assessment: an initial pass
across the system under consideration to understand what is exposed, refined later zone by zone. The output is not
a list of villains but a set of testable claims about how this environment would be attacked and what would happen.

## Threat categories to check

1. Unauthorised access: attempts to operate or reconfigure ICS devices without proper credentials. Gap check: Confirm role-based access, account management, authentication mechanisms, and evidence of regular access reviews. Any missing records or unclear access rights are findings.
2. Malware and cyber intrusion: including ICS-targeted malware, ransomware, or lateral movement from IT networks. Gap check: Ensure network segmentation, firewall rules, application whitelisting, patch management, and monitoring logs are documented. Missing or incomplete evidence is a gap.
3. Insider threats: misuse, misconfiguration, or sabotage by personnel. Gap check: Verify separation of duties, privileged account monitoring, and operator responsibilities. Ambiguous ownership or missing monitoring logs is a finding.
4. Configuration and change errors: misapplied updates, insecure defaults, or untracked changes. Gap check: Confirm configuration baselines, version-controlled firmware and software, and documented change management. Missing steps are findings.
5. Physical tampering: direct interference with controllers, sensors, or network equipment. Gap check: Confirm access controls, tamper-evident seals, surveillance coverage, and inspection logs. Any undocumented areas are gaps.
6. Supply chain and firmware risks: vulnerable or compromised devices entering the environment. Gap check: Verify device acceptance procedures, firmware validation, and vendor risk assessments. Missing documentation is a finding.
7. Network and protocol abuse: exploitation of Modbus, OPC UA, DNP3, or other OT protocols. Gap check: Ensure firewall rules, segmentation, anomaly detection, and protocol enforcement are documented. Gaps here are high priority.

## Adversary categories

1. Opportunistic attackers and script kiddies typically exploit trivial weaknesses: default credentials, exposed ports, unpatched devices. Gap check: Verify all devices have strong credentials, patching is current, network access is restricted, and monitoring logs cover unusual activity.
2. Malicious insiders: employees, contractors, or operators misusing privileges. Gap check: Ensure separation of duties, clearly assigned responsibilities, and audit logs of privileged actions. Ambiguous access or unmonitored high-risk actions are findings.
3. Targeted, skilled attackers and nation-state campaigns exploit protocol weaknesses, segmentation gaps, or supply chain vulnerabilities. Gap check: Confirm segmentation rules are enforced, critical assets are monitored, incident response is documented, and supply chain controls exist.

This ladder of capability is what security levels formalise when [walls and gates](walls-and-gates.md) assigns
targets to zones: the question "which besieger does this zone need to keep out" gets a number.

## What the rational register misses

Threat assessment works in the rational domain: map attack vectors, verify control coverage, check documentation. A
threat register built from this process alone will be systematically incomplete. 

The [emotional layer](../../foundations/problem-solving/three-domains.md) asks which
threats are difficult to name: insider threat is chronically underrepresented not because it is rare but because
naming it implicates colleagues and changes the dynamic of the session. A privileged operator whose access has never
been reviewed is a threat scenario; raising it publicly has social consequences. 

The [political layer](../../foundations/problem-solving/three-domains.md) asks whose
interests are served by particular threat framings: a protocol vulnerability in a system owned by a team under
production pressure tends toward accepted risk regardless of actual impact. An unusually high acceptance rate for a
specific threat category is worth examining for incentive misalignment before treating documentation coverage as
complete.

Each adversary category is also a hypothesis about how an attacker would behave in this environment and what the
controls would do in response. Mapping adversaries to controls confirms the documentation is coherent. Testing the
controls against realistic adversary techniques confirms the model holds in the deployed environment; that work
belongs to [testing the defences](testing-the-defences.md). Threats that exist only as documentation categories,
without any history of being tested against, are assumptions about how the ICS environment will respond under
attack, not findings.

## Practical gap-spotting

* Threat vs. control mapping: every threat wants a documented mitigation. Unmapped threats are immediate gaps.
* Evidence completeness: logs, alerts, or inspection records exist for each threat category, or their absence is a finding.
* Zone relevance: verify that threat assessment aligns with network and security zones. Threats outside documented zones indicate missing coverage.
* Incident readiness: each threat category has documented detection, response, and responsible personnel. Missing assignments or unclear procedures are findings.

## Output

By the end of this stage, the organisation has a threat register mapped to the asset inventory, adversary
categories mapped to the controls meant to stop them, an initial risk assessment across the system under
consideration, and a marked list of risk acceptances worth a second look. Zone partitioning builds directly on this.

## Related

* [ISO 22301 Storm charts](../iso22301/storm-charts.md)
* [NIS2 Understanding the river](../../audits/nis2/river.md)
* [ISO 27001 Risk tent](../../audits/iso27001/risk-tent.md)
* [Unseen University Power & Light Co. IT/OCS pentest](https://red.tymyrddin.dev/docs/power/)
* [Threat modelling as a process](../../workshops/threat-modelling.md)
* [Gap analysis](../supportive/gap-analysis.md)
