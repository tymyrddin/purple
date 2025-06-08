# Supply chain attack defence for developers  

**Course description:** 

This interactive course teaches developers how to identify and mitigate risks from third-party vendors, compromised 
software updates, and dependency hijacking. Through real-world case studies, hands-on exercises, and roleplay, 
participants will learn to verify downloads, detect suspicious behaviour, and respond to supply chain threats. The 
focus is on practical, engaging learning—no dry theory or exams.  

*This course description is open source. Feel free to use it.*  

---  

## Course outline  

**Duration:** 1 day (6 hours, including breaks)  

**Format:** In-person or virtual (adaptable for both)  

**Audience:** Software developers, devops engineers, and security-conscious tech teams.  

---  

## Timetable  

**Session 1: introduction to supply chain attacks (60 mins)**

- What is a supply chain attack? How dependencies and vendors become threats.  
- Real-world cases: the 2023 "double supply chain attack", npm and pip package hijacking.  
- Activity: "spot the rogue update" – quick quiz on legitimate vs. suspicious software changes.  

**Session 2: how attackers compromise the chain (90 mins)**

- Common techniques: typosquatting, dependency confusion, poisoned updates.  
- Hands-on demo: inspecting package metadata for signs of tampering.  
- Verification best practices: checksums, signatures, and secure sourcing.  

**Break (15 mins)**  

**Session 3: defending your pipeline (90 mins)**  
- Secure development practices: lockfiles, pinned versions, and automated audits.  
- Tool walkthroughs: sbom (software bill of materials) generators, vuln scanners.  
- Roleplay: "the unexpected update" – team debates whether to trust a sudden patch.  

**Lunch (30 mins)**  

**Session 4: the big exercise – red team vs. blue team (120 mins, optional)**  
- Based on a real attack (e.g., the solarwinds breach or a recent npm compromise).  
- Red team: plants a malicious "update" in a demo project.  
- Blue team: detects, contains, and reports the breach.  
- Debrief: key mistakes and defences.  

**Session 5: building a resilient workflow (45 mins)**  
- Creating a team "action plan" for supply chain threats.  
- Fun quiz: "can you stop the breach?" – spot the vulnerabilities in a mock CI/CD pipeline.  
- Q&A and wrap-up.

---  

## Resources required  

- Sample compromised packages (safe, demoware versions).  
- Real-world case study slides (solarwinds, recent npm/pip attacks).  
- Demo CI/CD pipeline with intentional vulnerabilities.  
- Roleplay cards for "unexpected update" scenario.  
- Printed/digital cheat sheets on verification steps.  

---  

## Key activities explained  

1. **"Spot the rogue update" quiz**  
   - Participants review code diffs or changelogs to guess which were malicious.  
   - Highlights subtle warning signs (e.g., unusual maintainer changes).  

2. **Roleplay: the unexpected update**  
   - A "vendor" (played by a participant) pushes an urgent, unverified patch.  
   - Teams must decide whether to deploy it, using verification protocols.  

3. **Red team vs. blue team exercise**  
   - *Scenario:* A popular open-source library gets compromised (like ua-parser-js in 2021).  
   - Red team: adds stealthy malware to a demo package.  
   - Blue team: uses tools like `npm audit` or `snyk` to find it.  

---  

## Takeaways  

- A team "action plan" for vetting third-party code.  
- Hands-on experience with auditing tools.  
- Awareness of real-world attack patterns.  
- A completion certificate (no pass/fail).  

---  

## Notes for facilitators  

- Emphasise collaboration over competition in exercises.  
- Use humour carefully—keep focus on practical learning.  
- For virtual delivery, pre-share demo repos for hands-on sections.  

This course proves that even serious topics like supply chain security can be engaging—because developers learn best 
by *doing*, not just listening.
