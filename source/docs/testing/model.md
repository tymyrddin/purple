# Threat-modelled adversary emulation framework

## Step 1: Develop a threat profile

*Know thy enemy (and their favourite toys)*

This stage is about identifying who’s most likely to target your organisation, what they’re after, and how they tend to go about it.

**Industry focus:** Financial services

**Primary threat actors:**

1. **FIN7** (organised cybercrime group)

   * **Tactics & techniques:**

     * **T1078:** Valid account exploitation
     * **T1059:** Command-line and scripting abuse
     * **T1204:** User execution (usually through phishing)

2. **Lazarus Group** (state-sponsored APT)

   * **Tactics & techniques:**

     * **T1053:** Scheduled task manipulation
     * **T1547:** Boot/startup persistence mechanisms
     * **T1021:** Abuse of Remote Desktop Protocol (RDP)

**Critical assets at risk:**

* SWIFT terminals (lovely honeypots for financial attackers)
* Trader workstations (access to juicy credentials)
* Core account management systems (where the real damage gets done)

**Output**

Create an internal threat profile document that includes:

* Known TTPs (tactics, techniques, and procedures)
* Assets linked to threat groups
* Risk ratings for each asset based on exposure and criticality

---

## Step 2: Build the emulation plan

*Attack like they do — but without getting sacked*

The goal is to simulate realistic scenarios that reflect adversary behaviour without crossing operational red lines.

### Example emulation scenario (FIN7)

```yaml
# fin7-emulation.yaml  
techniques:  
  - T1078.004:  # Valid account compromise  
    steps:  
      - "Phish service account credentials"  
      - "Create persistence via scheduled tasks"  
      - "Maintain access for 72 hours"  

  - T1059.005:  # Visual Basic script  
    steps:  
      - "Deliver macro-enabled Excel document"  
      - "Establish command and control channel"  
      - "Perform lateral movement"
```

### Setup instructions

1. Choose an emulation platform: [MITRE Caldera](https://github.com/mitre/caldera), [Atomic Red Team](https://github.com/redcanaryco/atomic-red-team), or [Vectr](https://github.com/SecurityRiskAdvisors/VECTR)
2. Deploy agents in a segregated test environment (not prod — unless you *really* want a new job)
3. Use your YAML file or Caldera plugin to define the scenario

### Planning tips

* Align every action to a MITRE ATT\&CK technique ID
* Reference real-world breaches in your sector to prioritise emulation paths
* Use detection evasion methods sparingly to avoid false negatives hiding real gaps

---

## Step 3: Execute with operational constraints

Safety first — then break things. A red team simulation is not an excuse for chaos. Constraints matter.

### Execution command (Caldera example)

```bash
python3 server.py --insecure --plugins threat_emulation/fin7 --constraints realism.yaml
```

### Key operational constraints

1. **Time limits:**

   * Max 4 hours for achieving initial access
   * Wrap up the full scenario in under 24 hours

2. **Technical boundaries:**

   * No interference with live SWIFT traffic
   * Trader workstations are read-only (yes, really)

3. **Safety mechanisms:**

   * All testing in a segmented environment
   * Live monitoring from the SOC with a break-glass procedure to halt emulation if needed

### Required artefacts

* Full activity logs (agent, C2, system, and SIEM)
* Detection results matched to each ATT\&CK ID
* Gap analysis comparing expected vs. actual blue team response

---

## Step 4: Detection tuning

*Turn your logs into something other than noise*

Once the emulation's run, use the output to fine-tune your detections.

**Recommendations:**

* Correlate emulated activity with SIEM alerts (false negatives = blind spots)
* Focus on noisy techniques (e.g., T1059 scripting) for signature tuning
* Use Sigma or Splunk queries to build detections for missed behaviour
* Prioritise behavioural over IOC-based detection — these attackers recycle tooling like bad office jokes

---

## Step 5: Debrief and after-action review

*Not just ‘what broke’, but *why*, and *how to fix it**

Use a structured AAR (after-action review) template to keep the conversation focused and productive.

### AAR template (example)

**1. Summary of objectives**

- Simulate FIN7-style attack targeting account systems using valid credential access and macro delivery.

**2. Scenario walkthrough**

- Describe major phases (initial access, persistence, lateral movement), and timeline of execution.

**3. Successes**

- Blue team detected scheduled task creation
- SIEM correlated abnormal login locations

**4. Failures / blind spots**

- No alert on command-line VBScript
- Lateral movement via RDP went undetected

**5. Lessons learned**

- Need deeper endpoint visibility on trader machines
- Scheduled task detection is good — expand to cover at job creation time

**6. Remediation plan**

- Write and deploy Sigma rules for VBScript execution
- Tune alert thresholds on authentication anomalies

**7. Follow-up**

- Schedule re-run in 90 days with new threat profile updates

---

## Optional extras

* **Share with execs:** Condense the AAR into a 1-page “what this means for us” briefing
* **Include screenshots:** A picture of a successful payload might actually scare them into funding
* **Document lessons in a threat logbook** to inform next quarter’s tabletop exercises
