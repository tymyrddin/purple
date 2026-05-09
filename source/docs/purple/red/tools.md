# Red team tools and techniques

Red teamers use a mix of custom tools, open-source frameworks, and legitimate administrative tools repurposed for adversary emulation. The list below is illustrative rather than exhaustive; every category has alternatives, and the choice between them depends on the engagement, the budget, and the operational security required.

## Reconnaissance

OSINT frameworks: Maltego, Recon-ng, theHarvester, SpiderFoot.

Network scanning: Nmap, Masscan, Shodan.

DNS enumeration: DNSRecon, Fierce, SubFinder.

Organisational mapping: LinkedIn, Hunter.io.

## Initial access

Phishing frameworks: Gophish, King Phisher, Social Engineering Toolkit.

Payload generation: Metasploit, Veil, Empire, Covenant.

Exploit frameworks: Metasploit, exploit-db, nuclei templates.

Password attacks: Hydra, Medusa, CrackMapExec for spraying.

## Command and control

C2 frameworks: Cobalt Strike, Covenant, Sliver, Mythic, Havoc.

Tunnelling: Chisel, ligolo, SSF for pivoting.

Obfuscation: Invoke-Obfuscation, Donut, custom encoding.

## Post-exploitation

Credential dumping: Mimikatz, LaZagne, SharpDump, pypykatz.

Lateral movement: PsExec, WMI, RDP, PowerShell remoting.

Living-off-the-land: LOLBAS, GTFOBins, native Windows and Linux tools.

Persistence: services, scheduled tasks, WMI events, registry modifications.

## Stealth and evasion

Antivirus bypass: custom payloads, encrypted shellcode, process injection.

EDR evasion: direct syscalls, PPID spoofing, unhooking techniques.

Network evasion: domain fronting, protocol tunnelling, DNS exfiltration.

Log evasion: event log clearing, ETW tampering, SIEM blind spots.

## Related

- [Offensive mindset and methodology](mindset.md)
- [Blue team tools and capabilities](../blue/tools.md)
- [SOC detection and response](../../incident-response/soc/detection.md)
- [CTFs as learning environments](../../foundations/montessori/ctf-value.md)
