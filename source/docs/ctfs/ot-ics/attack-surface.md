# OT/ICS attack surface reference

Knowing that Modbus has no authentication does not tell you what an attacker does with that fact. This reference organises sixteen attack techniques into two groups: how attackers arrive and establish position, and what they do to OT systems once they are there.

Protocols (Modbus, DNP3, IEC-104, OPC UA, S7, MQTT) feature throughout, but they are not the whole picture. Credential abuse, supply chain compromise, phishing, and physical access are also covered, because in practice those are how OT environments get into trouble. The focus throughout is on what attackers achieve, why consequences matter more than commands, and where the gaps are between published CTF scenarios and actual incident patterns.

Where a technique has no confirmed real-world incident, that is noted. "Theoretically validated" means peer-reviewed research has established the method is sound, not that it has been deployed against live infrastructure. The distinction matters, and this document tries to hold it.

## Access and persistence

How attackers arrive, establish position, and stay undetected. These techniques precede OT-layer exploitation in every major real-world incident. Most published CTF challenges skip this group entirely and drop participants directly inside the OT network.

### Spear phishing and social engineering

Establish a foothold in the IT environment through targeted human compromise.

#### Human-layer entry methods

- Spear phishing emails targeting engineers, operators, and IT staff with OT system access
- Malicious document attachments exploiting readers on engineering workstations
- Pretexting calls to extract VPN credentials or system configuration details
- Fake vendor portals harvesting credentials
- Watering hole attacks targeting ICS vendor sites or industry forums

Protocols involved: Not applicable. The attack surface is email, web, and human behaviour.

#### The step before the pivot

The lateral movement section covers the IT/OT crossing in detail. This is how an attacker gets into IT in the first place. A challenge that starts with a harvested credential or a simulated phishing compromise teaches the full kill chain. The connection between "opened an attachment" and "tripped a substation breaker" is where the real lesson lives.

#### The canonical entry point

BlackEnergy's initial compromise of Ukrainian utilities in 2015 began with [spear phishing emails carrying malicious
Word documents](https://www.csidb.net/csidb/incidents/a743f9ac-2fe8-48a0-a331-bd1e7342c4ae/).
[Sandworm](https://attack.mitre.org/groups/G0034/)'s operations against European energy targets have consistently used spear phishing as the
IT entry vector. Social engineering is not a soft-skills footnote to OT security; it is how the majority of serious
OT incidents begin.

### Credential attacks and authentication abuse

Gain access by targeting authentication rather than protocols.

#### Authentication attack methods

- Password spraying against VPN, RDP, VNC, and web-based SCADA endpoints
- Default credential exploitation on HMIs, engineering software, and remote access tools
- Credential reuse from IT compromise into OT-facing services
- Theft of saved credentials from engineering workstations (browser stores, config files)
- Brute-force of web dashboards and historian interfaces

Protocols involved: Not applicable at the OT protocol layer. The attack surface is the authentication layer above it: RDP, VNC, SSH, HTTP/HTTPS, and proprietary remote access tools.

#### The simplest path

Most OT-facing systems were never designed to defend against credential attacks. VNC without passwords, Telnet with factory defaults, and RDP exposed to the corporate network are recurring findings in European operator assessments. This is not a sophisticated technique; it is often the first thing a persistent attacker tries, and frequently the last thing a defender checks.

#### Before the protocol exploit

Colonial Pipeline (2021) was compromised via a legacy VPN account with no multifactor authentication. No ICS protocol exploitation required. ENISA's assessments of European operators consistently identify default credentials and weak authentication as primary findings. Credential abuse often bypasses the protocol attack surface entirely by granting legitimate access to systems that themselves have full protocol access.

### Supply chain and third-party compromise

Compromise OT systems through trusted vendors, integrators, or software update mechanisms.

#### Supply chain entry points

- Trojanised vendor software updates pushed to engineering workstations
- Malicious firmware signed with legitimate vendor certificates
- Compromised credentials belonging to system integrators with standing remote access
- Rogue updates injected into PLC programming software or historian clients
- Hardware implants introduced during manufacturing, shipping, or maintenance

Protocols involved: Not applicable at the OT protocol layer. The attack surface is software update mechanisms, vendor
access channels, and the trust relationships built into the procurement and maintenance lifecycle.

#### Trust by design

Supply chain attacks work because they exploit trust that is deliberate. A firmware update from the vendor is supposed
to be installed. A remote session from the integrator is supposed to have access. The attacker inherits legitimacy.
Detection is difficult because the malicious action is indistinguishable from routine maintenance.

#### The ENISA priority

ENISA identifies supply chain attacks as one of the highest-priority threats to European critical infrastructure. NIS2
includes dedicated supply chain risk management obligations precisely because of this.

- [COSMICENERGY (2023)](https://cloud.google.com/blog/topics/threat-intelligence/cosmicenergy-ot-malware-russian-response/) was found in the context of a contractor's emergency response tooling.
- [SolarWinds (2020)](https://www.csidb.net/csidb/incidents/bfa2b078-ce4a-48a8-b1e5-ce49b3d42c25/) reached OT-adjacent systems at multiple European operators.

Supply chain compromise is the current delivery mechanism for the most capable adversaries operating against European OT.

### Physical access and insider threat

Compromise OT systems through direct physical interaction or through personnel with legitimate access.

#### Physical and insider vectors

- USB drops targeting engineering workstations or HMIs
- Rogue devices connected to field bus segments or control panels during maintenance
- Keyloggers or hardware implants installed on EWS or HMI hardware
- Personnel with legitimate protocol access issuing malicious commands
- Contractor or maintenance access used beyond its authorised scope or timeframe

Protocols involved: Not applicable at the network layer. Physical access bypasses network controls entirely.

#### The airgap problem

"Airgapped" OT networks are rarely airgapped in practice. They are connected to USB drives, maintenance laptops,
handheld configuration tools, and occasionally an engineer's phone used to photograph a screen.
[Stuxnet](https://spectrum.ieee.org/the-real-story-of-stuxnet) was the
canonical demonstration: it crossed physical isolation via removable media and reached centrifuges that had never
touched the internet. Physical access is difficult to simulate in a CTF, but worth representing because it is
responsible for the most consequential act of OT sabotage on record.

#### Low-tech, high-impact

Stuxnet's propagation via USB to air-gapped Iranian centrifuges remains the most documented physical vector case.
In European OT environments, insider threat is operationally more common: disgruntled employees, poorly managed
contractor access, and uncontrolled removable media feature in multiple European incident reports. ENISA highlights
insider threat as a persistent concern in OT environments where physical access controls are often weaker than their
IT equivalents.

### Initial access and lateral movement through the IT/OT boundary

Reach the OT environment from adjacent systems that span the divide.

#### Entry and pivot paths

- Compromise an engineering workstation (EWS): it has legitimate protocol access to every PLC and IED it manages, and is often a standard Windows machine on a shared or adjacent network
- Abuse vendor remote access channels: persistent VPN or remote desktop sessions installed for maintenance, rarely monitored, sometimes active permanently
- Pivot via the SCADA historian: often dual-homed between IT and OT networks, running standard Windows, and treated as IT infrastructure by IT teams and OT infrastructure by OT teams, adequately protected by neither
- Reach OT systems through Active Directory or shared authentication infrastructure extended into the OT zone
- Use the HMI as a command-issuing endpoint: it has full protocol access to the process and is often the most accessible Windows machine in the OT zone

#### The missing layer

The initial access layer is almost entirely absent from published CTF challenges, which typically drop the participant already inside the OT network. Including even a simple EWS-to-PLC pivot teaches something most participants have never practised, and reflects how the vast majority of real incidents actually begin.

#### The dominant pattern

Confirmed as the dominant pattern in every major European OT incident.

The historical record is clear:

| Incident                                | IT-to-OT path                                                                                              |
|:----------------------------------------|:-----------------------------------------------------------------------------------------------------------|
| BlackEnergy / Sandworm (Ukraine, 2015+) | Corporate IT compromise → OT access                                                                        |
| Industroyer (Ukraine, 2015)             | Prior IT-network compromise → IEC-104 commands                                                             |
| Triton / TRISIS                         | Engineering workstation with legitimate access to Triconex safety controllers                              |
| NotPetya (2017)                         | Ukrainian accounting software (IT) → OT-adjacent systems at Maersk, Saint-Gobain, and others across Europe |

The European structural reality: Remote access to OT via unmonitored VPN or vendor connections is endemic across European operators. The dual-homed historian is the classic orphan asset: IT teams treat it as OT infrastructure, OT teams treat it as IT infrastructure, and neither owns its security.

What NIS2 acknowledges: The supply chain provisions of NIS2 (implemented October 2024) exist precisely because of this pattern. Vendor remote access, system integrator credentials, and shared authentication between IT and OT are not edge cases, they are the primary delivery mechanism for OT compromise.

What CTF designers miss: Almost every published OT CTF drops the participant inside the OT network. That teaches protocol exploitation and PLC manipulation, but it skips the step that matters most in reality: *getting there*. An EWS-to-PLC pivot, even a simple one, would teach something most participants have never practised.

IT-to-OT lateral movement is not a niche technique. It is the default path in every major European OT incident on record. The engineering workstation, the historian, the HMI, and the vendor VPN are not exotic targets, they are the front door.

### Trust exploitation and misconfiguration abuse

Abuse the fact that OT networks assume everything inside is friendly.

#### Misconfiguration entry points

* Anonymous OPC UA access
* Default MQTT credentials
* Flat network movement between zones
* Blind trust between SCADA and field devices
* Protocol gateway and converter devices at zone boundaries: they translate between Modbus, DNP3, and IP, are often poorly secured, and sit between network segments by design

Protocols involved: all of them, frankly.

#### The realistic gap

This is the bridge to reality. Most real incidents are not zero-days; they are "why is
this open to the entire network".

Protocol gateways are a specific and underappreciated gap. Security teams rarely own them clearly. They often
fall between IT (network) and OT (operations) responsibility. They are accessible from both sides of the boundary
they sit on by design. A gateway that translates Modbus to DNP3 and exposes both interfaces to both networks is a
pivot point an adversary only needs to compromise once.

#### The most consistent finding

The most consistently relevant technique in European OT environments.

ENISA's OT threat landscape reports consistently identify weak segmentation, default credentials, and unauthenticated
protocol access as recurring findings across European operator assessments. These are not hypotheticals, they are audit
findings.

The [NIS2 Directive (implemented October 2024)](https://purple.tymyrddin.dev/docs/audits/nis2/tributaries) directly
addresses supply chain and access control gaps. The linked guide on supply chain risk management correctly identifies
that "weaknesses upstream can pull you under even if your own defences are strong". And that includes the integrator
who installed that protocol gateway with default credentials.

- Compliance with NIS2 is ongoing, and compliance is *not* a guarantee of actual security
- Smaller operators are certainly not there yet
- NIS2 mandates risk management processes, not the elimination of misconfigurations

The gap that remains is that a compliant operator can still have an anonymous OPC UA server, a flat control network,
and a gateway with default passwords. NIS2 requires that they *document* the risk assessment that decided those were
acceptable. That is not the same as fixing them.

Trust exploitation and misconfiguration abuse are not emerging threats. They are the *current reality* of European OT
security. Protocol gateways are the most dangerous version because no one owns them, everyone needs them, and they
sit exactly where you would put a backdoor if you were designing one.

### Living-off-the-land and long-term pre-positioning

Establish and maintain covert persistent access to OT-adjacent systems for months or years, using only legitimate tools, in preparation for a future destructive action triggered by an external event.

#### Pre-positioning methods

- Use native OS tools (WMI, PowerShell, certutil, netsh) to avoid malware-based detection
- Enumerate network topology, connected OT systems, and historian configurations without deploying payloads
- Maintain access via legitimate remote management tools already present on the target
- Create or quietly abuse legitimate accounts with minimal footprint
- Map OT-adjacent systems and document control logic and process configurations for future use
- Avoid any contact with OT systems directly until a trigger instruction is received

Protocols involved: Not applicable. The defining characteristic of this technique is the deliberate avoidance of
any OT protocol interaction. All activity is confined to IT and IT/OT boundary systems using legitimate administrative
channels.

#### The waiting game

Living-off-the-land pre-positioning is architecturally distinct from every other technique in this reference. The
objective is not to compromise anything now; it is to be ready to compromise something later. No malware means no
detection by antivirus or endpoint tools. No unusual protocol traffic means no OT-layer alerts. The attacker looks
like a legitimate administrator. The threat model implication is uncomfortable: you may already be hosting an
adversary who is waiting for an instruction you will never see coming.

#### Already inside

[Volt Typhoon](https://attack.mitre.org/groups/G1017/), disclosed May 2023, demonstrated five years of persistent
access across US and Guam infrastructure using exclusively legitimate tools. CISA assessed the objective as
pre-positioning for potential destructive action during a Taiwan-related crisis, not intelligence collection.

European equivalents have not been disclosed at the same level of detail, but ENISA's threat landscape explicitly
identifies state-actor pre-positioning in European critical infrastructure as an active and growing concern. The
defining characteristic, and the reason it belongs in this reference, is that standard OT security monitoring does
not detect it. The absence of OT protocol anomalies is not evidence of safety.

## OT-layer techniques

What attackers do once they have a position inside the OT environment. These techniques act directly on industrial protocols, controllers, and process data.

### Process intelligence gathering

Build an internal model of the system before touching it.

#### Intelligence collection methods

* Enumerate registers, nodes, data points
* Map relationships between sensors and actuators
* Identify safety limits and control loops
* Passively observe process behaviour over time
* Subscribe to MQTT topic `#` to receive every message on the broker without credentials

Protocols involved: OPC UA (namespace browsing), Modbus (read functions), DNP3 and IEC-104 (interrogation, unsolicited responses), MQTT (wildcard topic subscription)

#### Challenge design note

Skilled attackers do this first. Like nation-state groups. Good challenges reward patience here instead of rushing to
"press the red button". The MQTT wildcard is an underappreciated intelligence vector in environments that
use it for sensor telemetry: one command and every reading on the broker is visible.

#### Systematically underdetected

Highly relevant and systematically underdetected. OPC UA is standard in European
industrial installations and [anonymous access persists in older deployments](https://blogs.cisco.com/security/how-does-triton-attack-triconex-industrial-safety-systems).

[ENISA's 2025 Threat Landscape report](https://www.enisa.europa.eu/publications/enisa-threat-landscape-2025) covers a
wide range of attacks and threats, and does not focus on OT per se. It does state that 18.2% of threats observed
during the study period were aimed at these types of systems, after mobile threats, which accounted for 42% of attacks,
and web threats, which accounted for 27%. And *"Operational technology threats represent 18.2%, reflecting the growing
exposure of industrial and critical systems as they continue being increasingly connected and targeted"*.

ENISA's OT threat landscape reports identify reconnaissance and environment mapping as common precursors in attack
chains, yet most European operators have no OT-layer visibility to detect it.

### Data exfiltration

Extract process data, often quietly.

#### Exfiltration paths

* Read sensor values and historian feeds
* Subscribe to telemetry streams
* Pull configuration or program logic from PLCs

Protocols: Modbus, DNP3, IEC-104 (reads), OPC UA (variable access), MQTT (subscriptions), and S7 (program block and DB upload)

#### Making exfiltration meaningful

Make the data meaningful. Stealing "register 40001 = 123" is pointless. Stealing "reactor
pressure approaching critical threshold" is a decision point. Pulling an S7 program block is a full
blueprint of what the process is doing and where the limits are.

#### The visibility gap

[Nordex (March 2022)](https://www.nordex-online.com/en/2022/04/nordex-group-impacted-by-cyber-security-incident/) and
[Encevo/Creos Luxembourg (July 2022)](https://www.encevo.eu/press/2022-communique-de-presse-data-breach-2/) both
involved intrusions reaching corporate networks connected to OT environments. Public reporting does not clearly
confirm OT data exfiltration as a distinct objective. This lack of confirmation may reflect:

- Poor detection visibility: Most European operators cannot see data leaving their OT historian or telemetry streams
- Attacker stealth: Using legitimate protocols (OPC UA, MQTT, S7 reads) and valid credentials leaves no obvious footprint
- Under-reporting: Victims may not know, or may not disclose what they cannot prove

The historian as a dual-homed exfiltration target in the simulator reflects real European network architectures. An
adversary who reaches the corporate network, as both incidents demonstrate, is positioned to quietly read sensor values,
subscribe to telemetry, and pull program logic without ever manipulating a PLC or triggering an alarm.

The relevance is not what we know happened. The relevance is what we cannot yet see happening.

### Replay and timing attacks

Reuse valid traffic to reproduce effects or desynchronise systems.

#### Replay and timing methods

* Capture and replay control messages
* Delay or reorder packets
* Exploit deterministic response patterns

Protocols: DNP3 (classic replay), Modbus (predictable transactions), IEC-104 (sequence manipulation)

#### Teaching value

These are low-effort, high-impact in poorly defended environments. Also a good place to
introduce detection challenges.

#### Present and exploitable

Confirmed in Europe, but often as a *capability* rather than a *headline technique*. The public record shows:

- [Norwegian dam (2025)](https://on2it.net/blog/the-norwegian-dam-cyberattack/): Russian-linked attackers manipulated a discharge valve for four hours undetected. The access method (exposed interface, weak credentials) is precisely the condition that enables replay attacks.
- [COSMICENERGY malware (discovered 2023)](https://thehackernews.com/2023/05/new-cosmicenergy-malware-exploits-ics.html): Built to send IEC-104 commands to RTUs in European power grids. The malware does not need advanced exploits, it abuses protocol features by design.
- Confirmed vulnerabilities: [CVE-2017-6034](https://euvd.enisa.europa.eu/vulnerability/CVE-2017-6034) (Modbus replay of run/stop/upload/download) and [CVE-2022-45789](https://euvd.enisa.europa.eu/vulnerability/CVE-2022-45789) (Modicon authentication bypass by capture-replay) affect equipment deployed across Europe.

Why replay may be under-represented in incident reporting:

- Replay attacks are indistinguishable from legitimate commands in most OT logs. Without sequence numbers or cryptographic integrity checks, replayed traffic looks *identical* to normal operations.
- Attribution is ambiguous: a replayed "open valve" command may be attributed to operator error, system glitch, or unsophisticated access, not forensic discovery of a packet capture.
- Attackers who have sufficient access for replay also have access for direct writes. The *choice* between them depends on objectives (stealth vs. precision), not technical capability.

The operational reality:

Replay attacks are not "niche." They are a direct consequence of legacy protocol design with no authentication, no
sequence protection, no integrity checking. In European OT environments still running Modbus, DNP3, and IEC-104
without compensating controls, replay is:

- Low effort: Capture and replay requires basic networking skills, not protocol expertise
- Hard to detect: No alert triggers when a valid command repeats
- High impact: Replaying "close breaker" or "open valve" has physical consequences

Treat replay as a *present and exploitable* threat in European OT, not primarily a teaching concept. The absence of
public incident attribution reflects detection gaps and the difficulty of distinguishing replayed commands from
legitimate ones, not the apparent absence of the technique in the wild.

### Unauthorised state manipulation

Change the physical process by issuing control commands.

#### Command-level operations

* Flip coils, write registers, operate breakers, toggle actuators
* Start or stop PLC execution
* Override setpoints (temperature, pressure, flow)
* Send breaker-open commands paired with concurrent trip-prevention signals to block automatic grid restoration

Protocols involved: Modbus (writes), DNP3 (CROB), IEC-104 (single/double commands), S7 (DB writes, CPU control), and
OPC UA (write nodes)

#### Consequence over command

The write itself is dull. The consequence is where things get interesting. Does the pump
cavitate, does the grid destabilise, does the safety system trip?

#### In the wild and confirmed

Confirmed and active. The Ukraine 2015 and 2016 power outages used IEC-104 and
other proprietary or vendor-specific control protocols to trip breakers directly
([SANS/E‑ISAC analysis of the Ukraine grid attack](https://archive.org/details/lee-et.-al.-e-isac-sans-ukraine-duc-5)
demonstrates protocol‑level manipulation in a real outage).
[Industroyer2](https://www.welivesecurity.com/2022/04/12/industroyer2-industroyer-reloaded/) (April 2022) targeted
a Ukrainian transmission substation using hard-coded IEC-104 configuration including IOAs and target device parameters.
European energy infrastructure uses the same protocols and the same vendors. Industroyer/CRASHOVERRIDE (2016)
went further: its protection relay module sent trip commands alongside concurrent trip-prevention signals,
blocking automatic restoration and extending the outage deliberately. That is not just a write command; it
requires domain knowledge of how the target substation's protection logic works.

### Data integrity manipulation

Lie to the operator or control system.

#### Deception and spoofing methods

* Inject false sensor readings
* Mask real sensor values by serving pre-recorded normal readings to the operator
* Spoof responses from field devices
* Poison historian data
* Inject false demand data into Energy Management Systems or demand-response platforms to drive grid frequency deviation

Protocols: DNP3 (replay, unsolicited responses), IEC-104 (response injection), MQTT (publish fake telemetry), Modbus (spoofed replies)

#### The subtlety angle

This is where subtlety lives. The best attacks do not break the system, they convince it
everything is fine while it quietly breaks itself.

#### Narrowing the gap

No confirmed European OT incident where data integrity manipulation was the primary and publicly attributed technique,
but the gap is narrowing.

The [ENISA ICS Threat Landscape report](https://www.enisa.europa.eu/publications/enisa-threat-landscape-2025) identifies
"active manipulation" attacks aimed at sabotaging physical systems as a growing concern, with threat actors deploying
tailored ICS malware capable of manipulating control commands. [Canadian water systems were publicly compromised in
late 2025](https://www.swidch.com/resources/blogs/when-public-systems-go-dark-even-air-gaps-are-not-enough), with
attackers falsifying tank level alarms and manipulating pressure valves. The pattern is established. Europe is not
immune.

Why the public record probably stays quiet:

- Integrity attacks are harder to confirm than ransomware. No encrypted files, no ransom note, just sensors reading wrong.
- Operators may attribute manipulated readings to equipment failure, not adversary action.
- Victims who detect it may not disclose a technique that exposes detection gaps.

The operational difficulty argument is likely overstated. Hacktivists, not elite adversaries, successfully executed
manipulation in the Canadian incidents. The barrier may be lower than assumed; the detection barrier is the real
constraint.

Bottom line: Data integrity manipulation is not theoretical. ENISA tracks it as observed, not just a scenario. The
lack of European public attribution likely reflects detection and disclosure gaps, not absence of capability or intent.

Demand-response manipulation is a grid-specific variant: compromised demand-response platforms or falsified EMS
data cause grid frequency deviation by misleading the systems that balance load. No confirmed European incident
exists, but Princeton research demonstrated that coordinated false demand injection across a sufficiently large
fleet of smart devices could trigger dangerous frequency deviations. As demand-response programmes expand across
European smart grids, this surface grows.

### Control logic manipulation

Change how the system behaves, not just its current state.

#### Logic and setpoint targets

* Upload modified PLC logic
* Change function blocks or ladder logic
* Alter alarm thresholds or control loops
* Adjust a single setpoint by a small increment, staying within normal operating range but nudging the
  process toward a fault condition over time

Protocols involved: S7 (program upload/download) and OPC UA (method calls, configuration writes)

#### Persistence in OT

This is persistence in OT clothing. The system keeps betraying itself long after the
attacker leaves. Subtle setpoint changes are more realistic for stealth operations than dramatic logic
rewrites: they stay within normal operating parameters, avoid triggering alarms, and are considerably
harder to attribute.

#### Hard to see, harder to prove

Confirmed in Europe, but the line between "control logic manipulation" and "command injection" is blurrier than taxonomy suggests.

What the public record shows:

- Industroyer2 (2022): Hardcoded IEC-104 IOAs targeting Ukrainian high-voltage substations. The malware did not upload new logic. It issued commands against existing IOAs that attackers had mapped in advance. This is command injection, not logic manipulation. The effect (open breakers) and the prerequisite (detailed knowledge of the target's control configuration) overlap significantly with what logic manipulation achieves.
- Canadian water systems (late 2025): Hacktivists manipulated pressure valve settings and falsified tank level alarms. Not logic changes, but value manipulation with identical operational impact.
- Supply chain risk (current): ENISA reports increasing attacks through compromised firmware, vendor software, and third-party tools. These can alter controller logic "without leaving a trace in logs or triggering alerts". This is actual logic manipulation, happening via trusted channels that bypass traditional detection.

The detection problem:

Full logic rewrites are almost invisible to network monitoring. No unusual packets. No authentication failures. Just a controller that behaves differently. Most OT devices at Levels 0 and 1 lack the logging to detect whether their logic has been changed. The absence of public European attribution reflects:

- Forensic impossibility (how do you prove logic changed after the fact?)
- Detection gaps (no alerts triggered during the change)
- Attribution ambiguity (operators blame hardware failure)

What this means:

- Confirmed technique in the wild: Industroyer2, Incontroller, and supply chain compromises demonstrate capability and intent.
- Confirmed in Europe: Indirectly, Ukrainian infrastructure targeted; European vendors (Siemens, Schneider, ABB) affected by relevant CVEs; ENISA tracking "active manipulation" attacks against OT.
- Likely under-represented: Logic manipulation is hard to detect and even harder to publicly attribute. Absence from incident reports is weak evidence of absence.

Control logic manipulation is not theoretical. The technical capability exists, European vendors have confirmed
vulnerabilities, and supply chain attacks provide a delivery mechanism. Subtle setpoint manipulation may be the
more realistic stealth variant, but the distinction between "changed logic" and "issued commands against existing
logic" matters less to the operator than the physical outcome. Detection at the physical process layer is where it counts.

### Denial of control and safety disruption

Prevent operators or systems from controlling the process safely.

#### Disruption and denial methods

- Stop PLC CPU
- Flood communication channels
- Break protocol sessions
- Trigger fail-safe or fail-open states

Protocols involved: S7 (CPU stop), IEC-104 and DNP3 (session abuse), MQTT (broker flooding)

#### Slow and quiet

Not all outages are loud. A slow loss of visibility can be far more dangerous than an immediate shutdown. Operators watching seemingly normal telemetry while the process drifts outside safe parameters may not realise they have lost effective control until physical consequences occur.

MQTT broker flooding is theoretically plausible as a denial-of-service on the publish/subscribe layer but has no confirmed real-world incident in OT environments as of 2026.

#### IT disruption, OT consequences

Relevant, with confirmed precedent:

- KillDisk and related wiper activity (2015) deliberately disrupted operator visibility, a loss of control without immediate shutdown.
- S7 CPU stop has a documented Metasploit module. The capability is public, low-complexity, and weaponizable.

European incidents more frequently involve IT-layer disruption cascading into OT downtime than deliberate OT-layer denial of control. Examples include:

- [Norsk Hydro (2019)](https://www.csidb.net/csidb/incidents/5b033bb0-0e5f-4307-bde7-37273e36fe0e/): ransomware disrupted IT, production halted as a safety-driven consequence, not direct OT manipulation
- [Varta (2024)](https://www.csidb.net/csidb/incidents/280edfbc-4bc4-42c0-b039-9cbb1773f1da/) seems to display a similar pattern: IT encrypted, OT stopped because operators could not manage orders or logistics

These are *denial of control* in effect, but not in mechanism. The distinction matters for detection and defence.

What remains theoretical in Europe (as of 2026):

- MQTT broker flooding in OT: no confirmed real-world incident
- Deliberate, targeted OT-layer CPU stops or session abuse as primary attack techniques in European critical infrastructure

Denial of control is real. The 2015 KillDisk incident proves attackers understand the value of blinding operators while
keeping the process running. But the dominant European pattern remains IT disruption with OT consequences, not
OT-native denial-of-control techniques. Detection of the former is the priority; preparation for the latter is worthwhile.

### Safety system targeting and SIS bypass

Target the safety layer specifically, removing the last automated defence between an attacker and physical damage.

#### Safety system attack methods

- Enumerate and map Safety Instrumented System (SIS) architecture and safety function assignments
- Access the SIS engineering workstation, typically a separate, higher-security host from the process control EWS
- Overwrite safety controller firmware or modify safety logic to disable protective responses
- Maintain the appearance of normal SIS operation while the protection is inactive
- Time the primary destructive action for when the safety system cannot intervene

Protocols involved: SIS proprietary protocols
([Triconex TriStation](https://cloud.google.com/blog/topics/threat-intelligence/totally-tubular-treatise-triton-and-tristation/),
[Schneider Safety Suite](https://blog.se.com/sustainability/2024/04/29/what-is-a-safety-instrumented-system/));
sometimes reachable via S7 or OPC UA where safety and process controllers share network access.

#### The last line removed

Most OT attacks assume the safety system remains intact and active. Targeting the SIS before triggering the primary
destructive action removes the last automated protection. The process can then be pushed far beyond safe operating
parameters without automatic shutdown. This is significantly harder to execute than process control manipulation,
but the consequence is categorically different: physical destruction rather than disruption.

#### Confirmed and targeted

[Triton/TRISIS (2017)](https://i.blackhat.com/us-18/Wed-August-8/us-18-Carcano-TRITON-How-It-Disrupted-Safety-Systems-And-Changed-The-Threat-Landscape-Of-Industrial-Control-Systems-Forever-wp.pdf) is the only publicly attributed cyberattack specifically designed to disable a Safety
Instrumented System. It targeted a Schneider Electric Triconex SIS at a petrochemical facility in Saudi Arabia,
accessed via an engineering workstation with legitimate TriStation protocol access. A logic error in the malware
caused the SIS to fail-safe, the only reason the attack was discovered at all. The intended outcome was continued
operation with the SIS silently disabled, leaving the facility open to a subsequent destructive action with no
automatic protection remaining. [Triton is the world's most murderous malware, and it's spreading (reported in 2019)](https://www.technologyreview.com/2019/03/05/103328/cybersecurity-critical-infrastructure-triton-malware/).

The [INCONTROLLER/Pipedream framework (2022)](https://www.securityweek.com/video-deep-dive-pipedreamincontroller-ics-attack-framework/)
includes SIS-targeting components. European petrochemical, water treatment, and energy facilities use Triconex and
equivalent systems from the same vendor set.

### Protocol abuse and malformed input

Break or stress implementations rather than using them as intended.

#### Protocol stress methods

- Send malformed frames or APDUs
- Trigger edge-case parsing behaviour
- Fuzz protocol handlers

Protocols involved: IEC-104 (APDU crafting), S7 and Modbus (implementation quirks)

#### CTF design caution

Easy to get wrong in a CTF. If overused, it turns into "guess the crash input" rather than learning anything useful. The line between disciplined fuzzing and blind packet throwing is wide, and most discussions fall on the wrong side of it.

#### Known vulnerability class

Relevant, but the relevance has multiple layers that are often conflated.

At the vendor research level: Absolutely relevant. Siemens, Schneider Electric, and ABB are European vendors whose products dominate OT estates across the continent. All three have published significant ICS CVEs involving malformed input and memory corruption in protocol handlers. Examples include:

- Schneider Electric Modicon ([CVE-2018-7847](https://euvd.enisa.europa.eu/vulnerability/CVE-2018-7847), [CVE-2018-7846](https://euvd.enisa.europa.eu/vulnerability/CVE-2018-7846), [CVE-2018-7842](https://euvd.enisa.europa.eu/vulnerability/CVE-2018-7842)): CVSS 9.8, improper input validation leading to crashes or arbitrary code execution
- Ongoing [Patch Tuesday advisories](https://www.securityweek.com/topics/ics-patch-tuesday/) affecting Siemens, Schneider, ABB, and Phoenix Contact products

Fuzzing is a standard vulnerability discovery method used by both researchers and attackers. These are not CTF hypotheticals, they are patched vulnerabilities in deployed European equipment.

At the operational attack level: Niche, but the barrier is lower than "targeted operations only."

- Public exploit code exists for several of these CVEs. An adversary who can reach the protocol endpoint does not necessarily need "substantial prior access and device-specific knowledge", just a known CVE and a way to send packets.
- Crashing a PLC is loud. Unlike data exfiltration or subtle setpoint manipulation, a successful malformed input attack will likely cause a visible disruption. Most European threat actors observed to date (hacktivists, ransomware operators) have not shown a preference for this trade-off. The technique is rarely observed in the wild, but the vulnerabilities exist and public exploit code is available.

At the operational reliability level (the underdiscussed layer): Accidental malformed input is a real operational risk. 
A misconfigured monitoring tool, a buggy firmware update, or a corrupted configuration file can trigger the same 
parsing edge cases as an intentional attack. The operator does not care about intent, the PLC crashes either way.

Three distinct use cases:

| Phase                                               | Relevance        | Who cares?                                                                   |
|:----------------------------------------------------|:-----------------|:-----------------------------------------------------------------------------|
| Discovery (fuzzing to find new vulnerabilities)     | High             | Researchers, well-resourced adversaries                                      |
| Exploitation (using known malformed input CVEs)     | Low-to-moderate  | Any attacker who can reach the protocol endpoint and has public exploit code |
| Accidental trigger (misconfiguration or corruption) | Moderate-to-high | Every operator, regardless of adversary intent                               |

In a CTF context: This technique is fine, even expected. CTFs reward finding the exact malformed packet that crashes the service. That is a valid skill, but it does not map cleanly to most operational OT environments, where defenders care about sustained availability, not single-packet crash conditions.

Bottom line for a threat model: Protocol abuse and malformed input are a *known and documented* vulnerability class in European-vendor equipment, with public proof-of-concept code available. As an *observed adversarial technique in European OT incidents*, it is rare. As an *operational reliability risk*, it is non-trivial. Do not dismiss it entirely, but do not treat it as a primary threat vector either.

## Playbooks

This becomes the playbook.

For example, *"Manipulate the cooling system so the reactor overheats, without triggering alarms"*

A participant has options: direct write (loud, obvious), data spoofing (subtle), logic manipulation
(persistent). Learning happens. Most likely.
