# Telemetry deep dives (4-hour adversarial lab) 

Format: Rotating team exercises with hands-on telemetry analysis  

---

## Red team track: "How we beat your EDR"  

Exercise 1: API call obfuscation 

Objective: Modify malicious PowerShell scripts to evade endpoint detection  

Tasks:  

- Break process tree relationships (e.g., spawning via WMI instead of direct child processes)  
- Bypass memory scanning using:  
  - Reflective DLL injection variations  
  - Module stomping techniques  

Tools provided:  

- Process Monitor for call tracing  
- Custom EDR emulator with basic detection rules 

Success metrics: 

- Script executes without triggering process tree alerts  
- No memory scanning detection for ≥3 minutes  

Exercise 2: Heuristic bypass challenge 

Objective: Develop payload that evades modern EDR solutions  

Constraints:  

- Must score 0/10 on VirusTotal static analysis  
- Must maintain execution for >5 minutes in monitored environment  

Testing environment:  

- Pre-configured VM with:  
  - CarbonBlack trial  
  - SentinelOne demo  
  - Sysmon logging  

Scoring criteria:  

- Time until detection (longer = better)  
- Stealth of execution method  

---

## Blue team track: "Building better detections"  

Exercise 1: Telemetry archaeology  

Objective: Reconstruct attack chains from limited data 

Provided materials: 

- Anonymised EDR logs from red team exercises  
- MITRE ATT&CK Navigator for mapping  

Tasks:  

- Identify key API call sequences revealing malicious activity  
- Pinpoint the single biggest telemetry gap that allowed evasion  

Tools:  

- Elastic SIEM instance  
- Timeline analysis cheat sheet  

Deliverable: 

- Attack chain diagram with critical detection points marked  

Exercise 2: Signature tuning  

Objective: Improve detection rules for stealthy attacks  

Focus areas:  

- Behavioural detection of obfuscated PowerShell:  
  - Unusual .NET reflection patterns  
  - Anomalous script block logging  
- Living-off-the-land binary abuse:  
  - Certutil fetching executable content  
  - Msiexec with suspicious command lines  

Dataset: 

- Atomic Red Team test cases  
- Real-world attack samples  

Success metrics:  

- Reduced false positives on legitimate admin activity  
- Maintained detection rate for malicious samples  

---

## Workshop flow  

1. Initial briefing (30 mins)  
- Overview of modern EDR evasion techniques  
- Explanation of telemetry sources and limitations  

2. Team rotations (3 hours)  
- Groups alternate between red/blue exercises  
- Facilitators provide hints as needed  

3. Final debrief (30 mins)  
- Red teams demonstrate successful evasion techniques  
- Blue teams present detection improvements  
- Group discussion of key takeaways  

---

## Technical requirements  

For participants:  
- Basic PowerShell/Python knowledge  
- Familiarity with security concepts (process injection, LOLbins)  

Provided infrastructure:  
- Cloud-hosted SIEM instances  
- Pre-attacked endpoint images  
- Cheat sheets for:  
  - Common API call patterns  
  - Sigma rule best practices  

Outcome:  
Participants gain practical experience in both attacking and defending modern endpoints, with emphasis on telemetry blind spots.  

*(Content aligned with MITRE ATT&CK techniques T1059, T1620, and T1055.)*  

--- 

Note: All exercises use isolated lab environments with no external connectivity. Sample malicious code is neutered and used for educational purposes only.