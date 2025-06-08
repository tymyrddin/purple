# Logs literacy (3-hour war games)

Format: Competitive red team/blue team exercise with live attack simulation and forensic analysis  

---

## Workshop Structure  

Duration: 3 hours (1.5 hours attack, 1.5 hours defence & debrief)  

Teams:  
- Red Team – Attackers using living-off-the-land (LOTL) techniques  
- Blue Team – Defenders analysing logs and hardening detection  

---

## Phase 1: Red Team attack (90 min)

Objective: Maintain stealthy access for 1 hour using only: 

* Signed binaries (e.g., `msbuild.exe`, `7z.exe`)  
* Default OS utilities (PowerShell, WMI, certutil)  
* No malware, no exploits, just "normal" tools  

Rules:  

- Must evade standard EDR/SIEM alerts  
- Must leave forensic traces (intentionally) for Blue Team to find  

Attack Scenario:  

1. Initial access via a "legit" document (e.g., ISO file with hidden script)  
2. Privilege escalation via scheduled tasks or service abuse  
3. Data exfiltration using built-in compression/encoding  

Deliverable:  

- A documented attack chain with:  
  * Which IR playbook steps their attack bypassed  
  * The one log source that *should* have caught them  

---

## Phase 2: Blue Team forensics (90 min)  

Objective: Analyse logs to:  

1. Explain why defences failed (e.g., email gateway missed attachment, EDR didn’t flag LOLBin usage)  
2. Propose 1 process + 1 technical fix (e.g., "Block ISO files at email gateway" + "Monitor `msbuild.exe` spawning `cmd.exe`")  

Provided Data:  

- Full attack chain logs (email, EDR, process execution, network)  
- Red Team’s attack notes (revealed after initial analysis)  

Competition:  

- Teams present fixes in a 5-min "incident review"  
- Red Team votes: Which fixes would *actually* stop their attack?  

---

## Resources provided  

* Pre-configured VM with logging enabled (Sysmon, EDR, firewall)  
* Sample malicious document (ISO/LNK with embedded script)  
* Cheat sheet for common LOLBin attack patterns  
* Log analysis checklist (what to look for in PowerShell/WMI events)  

---

## Why this works

- Red Team learns stealthy attack methods *without malware*  
- Blue Team practises log analysis on *realistic* attack data  
- Competitive element keeps engagement high  
- No "perfect" defence – reinforces that security is iterative  

Outcome: Every participant leaves knowing where logs lie—and how attackers hide.  

*(Inspired by real-world LOTL attacks like SolarWinds & Lazarus Group operations.)*