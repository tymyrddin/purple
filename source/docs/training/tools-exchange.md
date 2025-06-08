# Tool exchanges (2-day capture the flag)  

Format: Hands-on red team/blue team exercises with competitive scoring  

---

## Day 1: Red team - C2 framework internals  

Lab 1: Mythic agent customisation 

Objective: Modify an existing command and control (C2) agent to evade detection 

Tasks:  

- Implement sleep masking (e.g., Ekko-style ROP chains to hide memory patterns)  
- Add custom traffic encryption (beyond default TLS)  
- Deliverable: Functional agent that successfully exfiltrates test data without triggering alerts  

Provided tools:  

- Mythic C2 community edition  
- Sample agents (Python, C#, or C variants)  
- Memory analysis cheat sheet  

Scoring criteria:  

1. Successful data exfiltration (30%)  
2. Evasion of static/dynamic analysis (40%)  
3. Code readability and documentation (30%)  

---

Lab 2: Defensive countermeasures  

Objective: Attack other teams' C2 infrastructure while hardening your own  

Tasks:  

- Identify and exploit a vulnerability in another team's C2 (e.g., agent impersonation, weak authentication)  
- Document the attack vector  
- Propose and implement a mitigation for your own C2  

Scoring criteria:  

1. Successful exploitation (50%)  
2. Quality of proposed mitigation (30%)  
3. Clear documentation (20%)  

---

## Day 2: Blue team - Sigma rule mastery  

Challenge 1: Anomaly hunt  

Objective: Write effective Sigma rules to detect advanced attacks  

Provided data:  

- Stripped-down SIEM logs from red team activities  
- List of suspicious patterns to target  

Detection focus areas:  

- Stealthy persistence (WMI subscription mutations, rogue scheduled tasks)  
- Lateral movement (RDP session hijacking, unusual service creation)  

Scoring criteria:  

1. Rule accuracy (tested against red team data)  
2. Logical detection conditions  
3. Clear rule documentation  

---

Challenge 2: False positive gauntlet  

Objective: Refine rules to reduce false positives while maintaining coverage 

Constraints:  

- Rules must not flag approved admin tools (e.g., PDQ Deploy, Lansweeper)  
- Must accommodate business-critical anomalies (legacy ERP systems, odd but legitimate batch jobs)  

Scoring criteria:  
1. False positive reduction (40%)  
2. Maintained detection rate (40%)  
3. Rule efficiency (20%)  

---

## Workshop resources  

Provided to all teams:  
- Pre-configured Mythic C2 instances  
- Sample attack datasets for testing  
- Sigma rule writing guide  
- Common false positive scenarios  

Technical requirements:  
- Laptops with 8GB+ RAM  
- Virtualisation software (VMware/VirtualBox)  
- Python/PowerShell basics  

Outcome: Participants gain practical experience in both offensive tooling and defensive detection, with immediate feedback through competitive testing.  

*(Inspired by real-world red team engagements and MITRE ATT&CK evaluations.)*