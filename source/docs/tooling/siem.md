# Building effective SIEM dashboards and telemetry pipelines

## Core objectives
- Correlate attacker tactics, techniques and procedures (TTPs) with event data across hybrid environments
- Identify visibility gaps through systematic mapping against the MITRE ATT&CK framework
- Empower security teams with actionable indicators and historical context for investigations

## Dashboard development principles

### Essential components for all platforms
- TTP correlation views - Map detection rules to ATT&CK techniques
- Process lineage visualisation - Parent/child relationships with command-line context
- Network activity overlays - GeoIP mapping and protocol analysis
- Time-bound analysis - Sliding windows for incident timeframes

---

## Platform-specific implementations

### Elastic stack (Kibana) dashboards
Recommended visualisations:
1. ATT&CK technique matrix with detection coverage gaps highlighted
2. Process creation events (Sysmon Event ID 1) with parent process context
3. Network connection maps enriched with threat intelligence feeds

Sample event schema:
```yaml
event:
  category: ["process", "network"]
  module: "powershell"
process:
  name: "powershell.exe"
  parent:
    name: "explorer.exe"
network:
  direction: "outbound"
destination:
  ip: "185.234.219.112"
```

### Splunk dashboards

Key search patterns:
```
index=sysmon (process_name=powershell.exe OR command_line="*Invoke*")
| stats count by user, host, parent_process_name, command_line
| lookup mitre_technique_lookup command_line OUTPUT technique_id, tactic
| table technique_id, tactic, count
```

Effective visualisations:
- Kill chain phase progression charts
- Notable events by severity/frequency heatmaps
- Detection rule efficacy over time

---

## Telemetry pipeline architecture

### Recommended data flows
| Source                | Collection method          | Destination          | Use case                     |
|-----------------------|----------------------------|----------------------|------------------------------|
| Endpoints (Osquery)   | Fleet Manager              | Elastic via Logstash | Host state interrogation     |
| Windows (Sysmon)      | Windows Event Forwarding   | Splunk Enterprise    | Process/network monitoring   |
| Cloud (CloudTrail)    | Kinesis Firehose          | S3 + Athena          | Cloud API activity logging   |
| Network (Zeek)        | Direct log shipping        | Grafana Loki         | Protocol-level inspection    |

### Critical enrichment steps

1. Field normalisation (ECS/CIM standards)
2. Threat intelligence lookups (MISP, Sigma)
3. ATT&CK technique tagging
4. Business context mapping (asset criticality)

---

## Threat hunting enablement

### Data retention strategy
- High-fidelity logs: 90 days minimum for endpoints/network
- Alert metadata: 12 months for trend analysis
- Enriched events: 30 days in hot storage

### Correlation improvements
```python
# Example Sigma-to-Splunk conversion logic
def convert_sigma_rule(rule):
    splunk_query = f"index={rule['logsource']} "
    splunk_query += " AND ".join(rule['detection']['conditions'])
    return {
        'search': splunk_query,
        'tags': [f"attack_{t}" for t in rule['tags']]
    }
```

---

## Tooling matrix

| Tool       | Primary strength                  | ATT&CK coverage focus           | Integration example                  |
|------------|-----------------------------------|----------------------------------|---------------------------------------|
| Kibana     | Custom visualisations             | Full framework                   | Elastic Agent → Beats → Dashboard     |
| Splunk     | Complex correlation               | Execution, persistence, exfil   | UF → Heavy Forwarder → Search Head    |
| Grafana    | Cloud/metrics visualisation       | Discovery, collection           | CloudWatch → Kinesis → Dashboard      |
| Osquery    | Endpoint state queries            | Defense evasion, discovery      | Fleet → TLS-encrypted log shipping    |
| Zeek       | Network protocol analysis         | Command and control              | Sensor → Logstash pipeline → Storage  |

---

## Common challenges and mitigation

### Visibility gaps

- Problem: Alert-centric monitoring misses stealthy activity  
- Solution: Baseline normal activity and hunt for deviations

### Schema issues

- Problem: Field name mismatches break correlations  
- Solution: Enforce ECS/CIM standards with validation checks

### Dashboard relevance

- Problem: Static views become outdated  
- Solution: Quarterly reviews against current threat intel

### Recommended improvements

1. Develop YAML-based detection rule converters
2. Integrate purple team exercise results
3. Build ATT&CK coverage scorecards
4. Implement automated detection validation

---

## Detection validation workflows

### Automated rule testing framework

```python
# Pseudocode for detection validation
def test_detection_rule(rule, test_cases):
    alerts_triggered = 0
    for case in test_cases:
        if execute_siem_query(rule.query, case.log_entry):
            alerts_triggered += 1
    efficacy_score = (alerts_triggered / len(test_cases)) * 100
    return {
        'rule_id': rule.id,
        'efficacy': f"{efficacy_score}%",
        'false_positives': run_against_benign_logs(rule.query)
    }
```

Implementation steps:
1. Atomic test case generation  
   - Create log entries matching ATT&CK techniques using tools like Caldera or Atomic Red Team
   - Example test case for T1059 (PowerShell):
     ```yaml
     log_entry:
       process.name: "powershell.exe"
       command_line: "Invoke-Mimikatz -Command '\"sekurlsa::pth /user:admin /domain:corp /ntlm:hash\""'
     ```

2. Benign activity profiling  
   - Collect 30 days of normal business activity logs
   - Use as control group for false positive measurement

3. Validation schedule  
   - Weekly: Automated atomic tests
   - Quarterly: Purple team exercises with new TTPs

---

## Storage tier cost-benefit analysis

### Financial services data retention model

| Tier | Retention | Cost/Month (GB) | Use Case              | Example Data                 |
|------|-----------|-----------------|-----------------------|------------------------------|
| Hot  | 30 days   | £0.50           | Active investigations | Raw EDR logs, alert queues   |
| Warm | 90 days   | £0.20           | Threat hunting        | Enriched events, Sysmon logs |
| Cold | 1-3 years | £0.05           | Compliance/audit      | Compressed alert metadata    |

Cost optimisation strategies:
1. Selective retention  
   - Keep full-fidelity logs only for critical assets (SWIFT terminals, DCs)
   - Sample non-critical endpoints at 20% (reduces storage by ~65%)

2. Compression benchmarks  
   - Zeek logs: 80% reduction with Zstandard
   - Windows events: 70% reduction with LZ4

3. Cloud cost controls  
   - AWS S3 lifecycle policies to auto-transition after 30 days
   - Elasticsearch cold tier with frozen indices

---

## Team competency requirements

### Cross-functional skills matrix

| Role          | SIEM Skills                   | Cloud Knowledge         | ATT&CK Proficiency    | Typical FTE Ratio   |
|---------------|-------------------------------|-------------------------|-----------------------|---------------------|
| L1 Analyst    | Splunk/ELK query syntax       | Basic AWS/GCP concepts  | TTP recognition       | 4:1 (per shift)     |
| Threat Hunter | Advanced correlation searches | Log pipeline management | Technique emulation   | 2 per 10k endpoints |
| SOC Engineer  | Dashboard development         | Infrastructure-as-code  | Detection engineering | 1 per cloud account |

Staffing consideration: A 24/5 SOC covering 50k endpoints typically requires:
- 6 L1 analysts (4 shifts)
- 3 threat hunters
- 2 SOC engineers
- €85k/year in training budget

---

## Implementation checklist

### Phase 1: Foundation (Weeks 1-4)

- [ ] Deploy log collection infrastructure
- [ ] Normalise critical field names (ECS/CIM)
- [ ] Build 5-10 core ATT&CK-aligned dashboards

### Phase 2: Validation (Weeks 5-8)

- [ ] Establish detection testing framework
- [ ] Profile benign activity baselines
- [ ] Conduct first purple team exercise

### Phase 3: Optimisation (Ongoing)

- [ ] Implement storage tiering policies
- [ ] Monthly detection efficacy reports
- [ ] Quarterly skills gap analysis
