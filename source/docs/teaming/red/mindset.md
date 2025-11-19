# Offensive mindset and methodology

Red teamers think differently than defenders. Understanding this mindset helps both red and purple teams operate 
more effectively.

## Think like an adversary

Opportunistic: Real attackers (unless nation state) follow the path of least resistance. Don't force complex exploits 
if weak passwords get you in. Use legitimate tools if they're available. Exploit human trust before technical 
vulnerabilities.

Patient: Speed isn't always necessary. Low and slow operations evade detection better than noisy attacks, especially 
the case for targeted attacks from nation state groups. Persistence matters more than rapid exploitation.

Adaptive: When defences block one path, find another. Defenders have to stop every attack vector; attackers 
only need one successful path.

Goal-focused: Remember the objective. Stealing credentials might be more valuable than root access on one system. 
Lateral movement to target systems matters more than deep exploitation of entry points.

## The attack lifecycle

Red team operations typically follow a structured lifecycle:

1. Reconnaissance (passive and active)

Gather information about the target: public records, social media, DNS information, exposed services, organisational 
structure, technology stack, third-party relationships.

Use OSINT, network scanning, social engineering reconnaissance. Understand the environment before attempting access.

2. Initial access

Gain first foothold: phishing with credential harvesting or malware, exploiting internet-facing vulnerabilities, 
physical access to facilities, compromising third-party vendors, password spraying against authentication portals.

Entry point doesn't need to be sophisticated. Attackers use whatever works.

3. Execution and persistence

Run malicious code and maintain access: deploy implants or remote access tools, create scheduled tasks or 
services, modify startup processes, plant web shells, compromise legitimate admin tools.

Persistence ensures access survives reboots, credential changes, or initial discovery.

4. Privilege escalation

Move from low-privilege access to higher authority: exploit local vulnerabilities, abuse misconfigurations, harvest credentials from memory, leverage service account privileges, exploit trusted relationships.

Domain admin or root access opens the entire environment.

5. Credential access

Steal authentication credentials: dump password hashes from memory or disk, keylog user input, intercept authentication traffic, extract credentials from browsers or password managers, abuse Kerberos or NTLM protocols.

Credentials enable lateral movement and persistence.

6. Discovery and lateral movement

Map the network and move between systems: enumerate Active Directory, scan internal networks, identify high-value targets, move laterally using stolen credentials, pivot through compromised systems.

Find the crown jewels: sensitive data, critical systems, administrative access.

7. Collection and exfiltration

Gather target data and extract it: identify sensitive information, compress and stage data, exfiltrate through legitimate protocols (HTTPS, DNS, cloud storage), maintain operations security during transfer.

Simulate data theft to test data loss prevention controls.

8. Impact (optional in exercises)

In real attacks: ransomware deployment, data destruction, service disruption. In exercises: demonstrate capability without actually causing damage. Document what could have been destroyed or disrupted.

## Unified Kill Chain framing


| ![Lockheed Martin Kill Chain](/_static/images/ukc.png) |
|:------------------------------------------------------:|
|                   Unified Kill Chain                   |


This is a second version of the attack lifecycle, but reframed using the Unified Kill Chain’s “IN – THROUGH – OUT” structure.

### IN: Where the falcons and foxes roam

[This is the part where attackers glide past your perimeter as if it were politely holding the door open](https://red.tymyrddin.dev/docs/in/).

Reconnaissance: They collect anything not nailed down (and plenty that is): OSINT, DNS data, tech stack clues, leaked 
credentials, third-party weak points. If it exists online, it is fair game. The goal is simple: understand the 
landscape well enough to slip in unnoticed.

Initial access: Phishing. Vulnerable internet-facing systems. Third-party compromise. Password spraying. Physical entry if you have obligingly installed doors.
Attackers do not aim for elegance; they aim for success.

### THROUGH: Where the raccoons burrow and rummage

[Once inside, attackers behave like houseguests who immediately start redecorating](https://red.tymyrddin.dev/docs/through/).

Execution and persistence: They run code, drop implants, create scheduled tasks, plant web shells, or piggy-back on 
legitimate admin tools. Persistence ensures they do not get kicked out the moment someone restarts a server.

Privilege escalation: Low-level access is boring. Attackers climb the privilege ladder using vulnerabilities, 
misconfigurations, or abused service accounts. Once you are domain admin or root, the rest is housekeeping.

Credential access: Memory scraping, keylogging, browser credential theft, Kerberos games, NTLM abuse. It is all 
about gathering the keys to as many doors as possible. Credentials fuel everything that follows.

Discovery and lateral movement: They map your network like it is a weekend city break: AD structure, internal 
routing, interesting servers, juicy data stores. Then they move sideways across systems using the credentials 
you unintentionally gifted them.

### OUT: Where squirrels swipe the crown jewels

[This is the stage where intentions become consequences](https://red.tymyrddin.dev/docs/out/).

Collection and exfiltration: Attackers identify the valuables, bundle them neatly, and smuggle them out through 
whatever protocol attracts the least suspicion. HTTPS, DNS, cloud storage. Take your pick. Quiet data theft is 
the name of the game.

Impact (optional, but popular in real incidents): Ransomware, data destruction, business disruption.
In exercises, we merely point out the damage that *could* have been inflicted. Your insurance company can thank us later.

## Resources

* [Lockheed Martin Cyber Kill Chain →](https://www.lockheedmartin.com/en-us/capabilities/cyber/cyber-kill-chain.html)
* [Unified Kill Chain →](https://unifiedkillchain.com/)
* [Varonis Cyber Kill Chain →](https://www.varonis.com/blog/cyber-kill-chain/)
* [Active Directory Attack Cycle →](https://github.com/infosecn1nja/AD-Attack-Defense)
* [MITRE ATT&CK Framework →](https://attack.mitre.org/)
