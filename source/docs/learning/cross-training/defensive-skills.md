# Defensive skills for attackers

Red team members who understand defence operate more realistically and provide more useful feedback. Learning detection, response, and monitoring reveals where attacks are visible and how to test meaningfully.

## Why attackers need defensive skills

Realistic operations: Understand what monitoring exists to test it properly. Avoid techniques defenders can't possibly detect.

Better feedback: Provide actionable findings. "We got domain admin" is less useful than "Lateral movement via WMI wasn't detected because X."

Improved collaboration: Speak blue team's language. Understand their constraints, tools, and priorities.

Career versatility: Red teamers who understand defence make better security leaders and architects.

## Core defensive concepts

Detection layers: Network (IDS/IPS, NDR), Endpoint (EDR, AV), Application (logs, APM), Identity (authentication monitoring), Cloud (CSIEM tools).

Response procedures: Triage, containment, eradication, recovery. Understand why defenders can't just "delete the malware."

Operational constraints: 24/7 monitoring limitations, alert fatigue, false positives, competing priorities, limited resources.

Logging and visibility: What gets logged, what doesn't, log retention, SIEM query capabilities, blind spots.

## Hands-on exercises

### Exercise 1: SOC analyst for a day (8 hours)

Red team member shadows SOC analyst through full shift. Observes alert triage, investigation, escalation, response.

Activities: Review alerts, investigate suspicious events, use SIEM and EDR tools, participate in incident response, understand workload.

Learning: What detections actually work, how long investigation takes, what information helps vs. hinders, operational pressures SOC faces.

### Exercise 2: Build detection rules (4 hours)

Red team creates detection rules for techniques they use.

Activities: Map red team TTPs to MITRE ATT&CK, identify detection opportunities, write SIEM correlation rules, test rules against benign activity.

Learning: Difficulty of detection engineering, false positive challenges, data requirements, how to test realistically without triggering production alerts.

### Exercise 3: Incident response drill (3 hours)

Red team plays blue team role in tabletop exercise or simulation.

Activities: Respond to simulated attack, follow incident response playbook, coordinate with other teams, make containment decisions.

Learning: Response complexity, decision-making under pressure, communication requirements, recovery challenges.

### Exercise 4: Threat hunting (4 hours)

Red team conducts proactive threat hunt using blue team tools and methods.

Activities: Form hypothesis, search logs and telemetry, analyse findings, document hunt, create detection rules.

Learning: Hypothesis-driven investigation, data mining skills, what makes effective IOCs, hunt documentation requirements.

## Tools red team should learn

SIEM platforms: Splunk, Elastic, Sentinel - Query languages, correlation rules, dashboard creation.

EDR tools: CrowdStrike, Defender, SentinelOne - Investigation interfaces, query capabilities, response actions.

Log analysis: Understanding Windows Event Logs, Sysmon, Linux logs, cloud provider logs.

Forensics: Basic disk forensics, memory forensics, timeline analysis, evidence preservation.

Threat intelligence: TIP platforms, IOC formats, STIX/TAXII, threat actor profiling.

## Integration with offensive work

Before engagements: Review defensive capabilities. Know what monitoring exists. Plan operations that test realistic gaps.

During engagements: Consider detection opportunities. Note what should have been detected but wasn't. Document blue team visibility.

After engagements: Provide detection-focused feedback. Explain exactly where blue team could have detected activity. Help write detection rules.
