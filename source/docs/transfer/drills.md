# Crisis response drills: from panic to protocol  

**Course description:** 

This immersive course transforms ransomware and data breach response into an engaging, hands-on experience. Developers will practise containment, communication, and recovery through realistic simulations, roleplay, and team challenges—no dry theory, just actionable skills wrapped in collaborative gameplay.  

*This course description is open source. Feel free to use it.*  

---  

## Course outline  

**Duration:** 1 day (6 hours, including breaks)  

**Format:** In-person or virtual (adaptable for both)  

**Audience:** Developers, devops engineers, and tech leads responsible for incident response.  

---  

## Timetable  

**Session 1: crisis response fundamentals (60 mins)**  

- Anatomy of a breach: how ransomware spreads (e.g., Clop’s MOVEit exploitation , ESXiArgs attacks ).  
- The 3 C’s: containment, communication, recovery.  
- Activity: "outbreak or outlier?" – teams analyse system logs to identify false alarms vs. real incidents.  

**Session 2: hands-on containment (90 mins)**  

- Isolation tactics: segmenting networks, freezing pipelines, revoking credentials.  
- Real-world case: replay the 2023 City of Oakland Play ransomware attack .  
- Roleplay: "the midnight alert" – teams race to contain a simulated breach while managing stakeholder panic.  

**Break (15 mins)**  

**Session 3: communication under fire (90 mins)**  

- Crafting clear alerts for internal teams, customers, and regulators.  
- Activity: "the press conference" – teams roleplay explaining a breach to journalists (with feedback on clarity and transparency).  
- Quiz: "who needs to know?" – prioritise notification lists based on data sensitivity.  

**Lunch (30 mins)**  

**Session 4: red team vs. blue team (120 mins, optional)**  

- Based on the 2024 Change Healthcare breach (impacting 100M records ).  
- Red team: deploys ransomware in a sandboxed environment, exfiltrates mock patient data.  
- Blue team: contains the attack, preserves evidence, and drafts a recovery plan.  
- Debrief: compare strategies with real-world outcomes.  

**Session 5: recovery & resilience (45 mins)**  

- Restoring systems: backups, patching, and post-mortems.  
- Fun quiz: "rebuild or retreat?" – evaluate recovery options for fictional scenarios.  
- Takeaways: personalised "crisis cheat sheet" for participants.  

**Certificates:** Awarded to all participants.  

---  

## Resources required  

- Sandboxed AWS/Azure environments for attack simulations.  
- Sample breach scenarios (e.g., stolen credentials, encrypted databases).  
- Roleplay cards for stakeholders (CEO, PR, legal).  
- Mock press release templates.  
- Quiz slides with real breach timelines .  

---  

## Key activities explained  

1. **"The midnight alert" roleplay**

   - Teams receive a simulated alert about unusual database activity. They must:  
     - Identify if it’s a false positive or breach.  
     - Draft a 5-minute Slack/email update for leadership.  

2. **Red team vs. blue team exercise**  

   - *Scenario:* Attackers exploit a vulnerable file-transfer tool (like Cleo MFT ) to encrypt HR data.  
   - Red team uses phishing lures to gain access.  
   - Blue team deploys log analysis and backup restoration.  

3. **"Press conference" challenge**

   - Teams face tough questions from "journalists" (played by others) about data loss. Graded on transparency and calmness.  

---  

## Takeaways  

- A laminated "crisis cheat sheet" with key steps and contacts.  
- Experience with containment tools (e.g., network segmentation scripts).  
- Confidence in communicating technical issues to non-tech audiences.  
- Completion certificate.  

---  

## Notes for facilitators  

- For virtual delivery, use breakout rooms for roleplay and shared docs for collaborative tasks.  
- Encourage creative solutions (e.g., "how would you contain an attack without internet access?").  
- Highlight real-world parallels (e.g., "this is how MedusaLocker disrupted hospitals ").  

This course turns crisis response into a game—where losing a round just means laughing and learning.  

*Design inspired by Dragos’ ransomware simulations  and Verizon’s incident response frameworks .*