# Controlled attack scenario framework

A methodical approach to test, validate, and enhance defensive controls without causing unplanned mayhem. This 
framework helps red and blue teams work from the same playbook, using threat intelligence to drive focused, 
measurable emulations — and turn chaos into actionable outcomes.

```
  +---------------------+     +---------------------+     +---------------------+
  |                     |     |                     |     |                     |
  |   Threat Intel      |---->|  Select ATT&CK      |---->|  Existing Coverage? |
  |     Report          |     |   Technique         |     |      +-----+        |
  +----------+----------+     +----------+----------+     |      | Yes |        |
             |                          |                 |      +-----+        |
             |                          |                 |           |         |
             v                          v                 |           v         |
  +----------+----------+     +----------+----------+     |  +--------+-------+ |
  |                     |     |                     |     |  | Test Detection | |
  |  MITRE Navigator    |     |  Threat Model       |     |  |     Efficacy   | |
  |   (Prioritization)  |     |  (OWASP/D3FEND)     |     |  +--------+-------+ |
  +----------+----------+     +----------+----------+     |           |         |
             |                          |                 |           v         |
             |                          |                 |  +--------+-------+ |
             +--------------------------+                 |  | Execute Atomic | |
                                                          |  |      Test      | |
                                                          |  +--------+-------+ |
                                                          |           |         |
                                                          |           v         |
                                                          |  +--------+-------+ |
  +---------------------+     +---------------------+     |  | Analyze        | |
  |                     |     |                     |     |  |   Telemetry    | |
  |  Develop New        |<----+      No Coverage    |     |  +--------+-------+ |
  |   Detection         |     |        Found        |     |           |         |
  +----------+----------+     +---------------------+     |           v         |
             |                                            |  +--------+-------+ |
             |                                            |  | Generate       | |
             v                                            |  | Findings Report| |
  +----------+----------+                                 |  +----------------+ |
  |                     |                                 |                     |
  |  Sigma/YARA         |                                 |                     |
  |   Rule Creation     |                                 |                     |
  +---------------------+                                 +---------------------+
```

## Framework walkthrough

### 1. Start with threat intelligence

* **Input:** Recent threat reports (e.g. FS-ISAC, Mandiant, CISA Alerts)
* **Goal:** Extract threat actors, observed TTPs (tactics, techniques, procedures), and sectors targeted

Typical sources:

* External: Mandiant reports, Microsoft Threat Intelligence, Recorded Future
* Internal: Incident response logs, SOC escalations, past compromise investigations

---

### 2. Select an ATT\&CK technique

Use [MITRE ATT\&CK Navigator](https://attack.mitre.org/resources/navigator/) to prioritise relevant techniques:

* Map threat actor TTPs to ATT\&CK techniques
* Prioritise by prevalence, asset exposure, and potential impact

Also consider adversary emulation plans from MITRE, Red Canary, or even CISA’s [Adversary Emulation Library](https://github.com/cisagov/Adversary-Emulation-Plans).

---

### 3. Review threat model context

Tie the selected technique into your organisation’s threat model:

* Use [OWASP Threat Modelling](https://owasp.org/www-community/Threat_Modeling) to assess business risk
* Cross-reference with [MITRE D3FEND](https://d3fend.mitre.org/) for mitigation coverage and telemetry insights

At this stage you’re asking: **"If we simulate this, is it relevant, and where would we catch it (if at all)?"**

---

### 4. Check for existing detection coverage

Here’s the decision point:

* **Yes, we have coverage:**

  * → Move to *test detection efficacy*

* **No, we don’t have coverage:**

  * → Initiate *develop new detection logic*

---

### 5A. Test existing detection efficacy (if coverage is claimed)

Use a controlled technique simulation, e.g.:

* **Atomic Red Team** tests
* **Caldera** plugin execution
* **Invoke-AtomicRedTeam** PowerShell tooling
* **Stratus Red Team** for cloud-centric techniques (AWS/Azure)

Verify that alerts trigger in SIEM, EDR, or other detection layers. Log everything. Assume nothing.

---

### 5B. Build new detection logic (if no coverage exists)

For new or under-detected techniques:

* Identify observable behaviours (parent-child processes, script execution, network anomalies)
* Use endpoint telemetry or logs from testbeds
* Build detection using:

  * **Sigma rules** for SIEM platforms
  * **YARA** for binary and file-based pattern matching
  * **Kusto** queries for Microsoft Defender or Sentinel

Tip: Prioritise behavioural detections. If your logic keys on “lolbin.exe,” it’s already a few steps behind.

---

### 6. Execute atomic test

Run the controlled simulation in a test or purple team environment:

* Confirm success of simulated technique execution
* Ensure safety controls are in place (e.g. containment, segmentation, monitoring)
* Record process trees, logs, and command executions

**Tools to consider:**

* [Atomic Red Team](https://github.com/redcanaryco/atomic-red-team) (wide technique coverage)
* [MITRE Caldera](https://github.com/mitre/caldera) (plugin-based campaigns)
* [Stratus Red Team](https://github.com/DataDog/stratus-red-team) (cloud-native ATT\&CK)
* [Invoke-Adversary](https://github.com/FortyNorthSecurity/Invoke-Adversary) (PowerShell-based simulation)

---

### 7. Analyse telemetry

Feed logs into:

* SIEM (Splunk, Elastic, Sentinel)
* EDR dashboards (CrowdStrike, SentinelOne, Defender)
* Log analytics platforms (Humio, Graylog)

Look for:

* Missed detections
* Delayed response
* Detection evasion signs
* Incomplete log data (gaps in process chain, missing network flows)

---

### 8. Generate findings report

Summarise the test using a consistent format:

* Technique tested (ID, name, expected impact)
* Detection status (pass/fail/partial)
* Logs and alerts captured
* Recommendations for tuning, rules, or visibility improvements
* Ownership for remediation

Output into:

* **Jira** ticket with attachments
* **Confluence** for documentation
* **PowerPoint** if you must present it to leadership (but do it ironically)

---

## Toolchain integration

This shows how red and blue teams can collaborate using appropriate tools for each phase of the framework:

| Phase         | Red team tools                               | Blue team tools                          |
| ------------- | -------------------------------------------- | ---------------------------------------- |
| **Planning**  | MITRE ATT\&CK Navigator, Threat reports      | OWASP Threat Model, MITRE D3FEND         |
| **Execution** | Atomic Red Team, Caldera, Stratus Red Team   | SIEM (Splunk, Elastic, Sentinel)         |
| **Analysis**  | VECTR, Caldera C2 logs, Invoke-Atomic output | EDR (CrowdStrike, Defender, SentinelOne) |
| **Reporting** | Jira, Markdown, Confluence, AAR templates    | Sigma rule repos, Detection dashboards   |

---

## Alternatives and extensions

* **Threat mapping tools:**

  * [VECTR](https://github.com/SecurityRiskAdvisors/VECTR) for scenario tracking
  * [ThreatMapper](https://github.com/deepfence/ThreatMapper) for runtime visibility

* **Detection-as-code pipelines:**

  * Integrate with CI pipelines using [Sigma CLI](https://github.com/SigmaHQ/sigma-cli)
  * Validate new detections in [DetectionLab](https://github.com/clong/DetectionLab)

* **Cloud-focused additions:**

  * [CloudKatana](https://github.com/microsoft/CloudKatana) for Azure
  * [AWSGuardDuty Tester](https://github.com/Barqawiz/AWSGuardDuty-Tester)

* **Formal testing standards:**

  * Align with [NIST SP 800-53A](https://csrc.nist.gov/publications/detail/sp/800-53a/rev-5/final)
  * Use [PurpleSharp](https://github.com/mvelazc0/PurpleSharp) for adversary simulation on Windows domains
