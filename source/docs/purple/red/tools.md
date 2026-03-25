# Red team tools and techniques

Red teamers use a mix of custom tools, open-source frameworks, and legitimate administrative tools.

## Reconnaissance tools

- OSINT frameworks: Maltego, Recon-ng, theHarvester, SpiderFoot
- Network scanning: Nmap, Masscan, Shodan
- DNS enumeration: DNSRecon, Fierce, SubFinder
- Social media: LinkedIn, Hunter.io for organisational mapping

## Initial access

- Phishing frameworks: Gophish, King Phisher, Social Engineering Toolkit
- Payload generation: Metasploit, Veil, Empire, Covenant
- Exploit frameworks: Metasploit, exploit-db, nuclei templates
- Password attacks: Hydra, Medusa, CrackMapExec for spraying

## Command and control

- C2 frameworks: Cobalt Strike, Covenant, Sliver, Mythic, Havoc
- Tunneling: Chisel, ligolo, SSF for pivoting
- Obfuscation: Invoke-Obfuscation, Donut, custom encoding

## Post-exploitation

- Credential dumping: Mimikatz, LaZagne, SharpDump, pypykatz
- Lateral movement: PsExec, WMI, RDP, PowerShell remoting
- Living-off-the-land: LOLBAS, GTFOBins, native Windows/Linux tools
- Persistence: Services, scheduled tasks, WMI events, registry modifications

## Stealth and evasion

- Antivirus bypass: Custom payloads, encrypted shellcode, process injection
- EDR evasion: Direct syscalls, PPID spoofing, unhooking techniques
- Network evasion: Domain fronting, protocol tunneling, DNS exfiltration
- Log evasion: Event log clearing, ETW tampering, SIEM blind spots
