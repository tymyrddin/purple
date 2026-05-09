# Offensive mindset and methodology

Red teamers think differently from defenders. Understanding the mindset helps both red and purple teams operate more effectively.

## Thinking like an adversary

Opportunism. Real attackers, unless nation-state level, follow the path of least resistance. Forcing a complex exploit when weak passwords already work is a luxury most adversaries do not bother with. Legitimate tools that are already available make better entry points than custom malware. Human trust gives way before technical vulnerabilities, often by quite a margin.

Patience. Speed is rarely necessary. Low-and-slow operations evade detection better than noisy attacks, especially in targeted operations from nation-state groups. Persistence outweighs rapid exploitation.

Adaptability. When defences block one path, an attacker finds another. Defenders have to stop every attack vector; attackers need only one successful path.

Goal-focus. The objective is what determines success, not the technique used to reach it. Stealing credentials may be more valuable than gaining root on one system. Lateral movement to target systems outweighs deep exploitation of entry points.

## The attack lifecycle

Red team operations typically follow a structured lifecycle.

Reconnaissance, both passive and active, gathers information about the target: public records, social media, DNS information, exposed services, organisational structure, technology stack, third-party relationships. OSINT, network scanning, and social-engineering reconnaissance build the picture before any access attempt.

Initial access establishes the first foothold: phishing with credential harvesting or malware, exploitation of internet-facing vulnerabilities, physical access to facilities, compromise of third-party vendors, or password spraying against authentication portals. The entry point does not need to be sophisticated; whatever works.

Execution and persistence run malicious code and maintain access: implants, remote access tools, scheduled tasks or services, modified startup processes, planted web shells, or compromised legitimate admin tools. Persistence ensures access survives reboots, credential changes, or initial discovery.

Privilege escalation moves from low-privilege access to higher authority through local vulnerabilities, misconfigurations, credentials harvested from memory, service-account privileges, or trusted relationships. Domain admin or root access opens the entire environment.

Credential access steals authentication credentials: password hashes from memory or disk, keystroke captures, intercepted authentication traffic, browser or password-manager extraction, or abuse of Kerberos and NTLM protocols. Credentials enable lateral movement and persistence.

Discovery and lateral movement maps the network and moves between systems: Active Directory enumeration, internal scanning, identification of high-value targets, lateral movement using stolen credentials, pivots through compromised systems. The targets are sensitive data, critical systems, and administrative access.

Collection and exfiltration gathers target data and extracts it: identification of sensitive information, compression and staging, exfiltration through legitimate protocols (HTTPS, DNS, cloud storage), with operational security maintained during transfer. The exercise simulates the data theft to test data-loss prevention controls.

Impact, which appears in real attacks but is usually omitted from exercises, would be ransomware deployment, data destruction, or service disruption. In exercises the team demonstrates capability without actually causing damage and documents what could have been destroyed or disrupted.

## Unified Kill Chain framing

| ![Lockheed Martin Kill Chain](/_static/images/ukc.png) |
|:------------------------------------------------------:|
|                   Unified Kill Chain                   |

A second take on the same lifecycle, reframed using the Unified Kill Chain's "IN, THROUGH, OUT" structure.

### IN: where the falcons and foxes roam

[The part where attackers glide past your perimeter as if it were politely holding the door open](https://red.tymyrddin.dev/docs/in/).

Reconnaissance: collecting anything not nailed down (and plenty that is): OSINT, DNS data, tech-stack clues, leaked credentials, third-party weak points. If it exists online, it is fair game. The goal is simple: understand the landscape well enough to slip in unnoticed.

Initial access: phishing, vulnerable internet-facing systems, third-party compromise, password spraying, physical entry through obligingly installed doors. Attackers do not aim for elegance; they aim for success.

### THROUGH: where the raccoons burrow and rummage

[Once inside, attackers behave like houseguests who immediately start redecorating](https://red.tymyrddin.dev/docs/through/).

Execution and persistence: running code, dropping implants, creating scheduled tasks, planting web shells, or piggy-backing on legitimate admin tools. Persistence ensures they do not get kicked out the moment someone restarts a server.

Privilege escalation: low-level access is boring. Attackers climb the privilege ladder using vulnerabilities, misconfigurations, or abused service accounts. Once domain admin or root, the rest is housekeeping.

Credential access: memory scraping, keylogging, browser credential theft, Kerberos games, NTLM abuse. Gathering keys to as many doors as possible. Credentials fuel everything that follows.

Discovery and lateral movement: mapping the network like a weekend city break: AD structure, internal routing, interesting servers, juicy data stores. Then moving sideways across systems using credentials unintentionally gifted to them.

### OUT: where squirrels swipe the crown jewels

[The stage where intentions become consequences](https://red.tymyrddin.dev/docs/out/).

Collection and exfiltration: identifying the valuables, bundling them neatly, smuggling them out through whatever protocol attracts the least suspicion. HTTPS, DNS, cloud storage. Take your pick. Quiet data theft is the name of the game.

Impact (optional, but popular in real incidents): ransomware, data destruction, business disruption. In exercises, we merely point out the damage that *could* have been inflicted. Your insurance company can thank us later.

## Resources

* [Lockheed Martin Cyber Kill Chain](https://www.lockheedmartin.com/en-us/capabilities/cyber/cyber-kill-chain.html)
* [Unified Kill Chain](https://unifiedkillchain.com/)
* [Varonis Cyber Kill Chain](https://www.varonis.com/blog/cyber-kill-chain/)
* [Active Directory Attack Cycle](https://github.com/infosecn1nja/AD-Attack-Defense)
* [MITRE ATT&CK Framework](https://attack.mitre.org/)

## Related

- [The red team mission](mission.md)
- [Adversary emulation vs. vulnerability testing](adversary.md)
- [SEM for defence and red teaming](../../foundations/system-effectiveness/for-defence.md)
- [Crafting scenarios](../../threat-modelling/crafting-scenarios.md)
