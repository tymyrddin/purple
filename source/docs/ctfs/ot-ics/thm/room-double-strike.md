# Room design: Double Strike

Based on the Sandworm operation against a Ukrainian high-voltage substation in April 2022:
Industroyer2 (IEC-104 protocol attack) deployed alongside CaddyWiper (disk wiper, timed to
execute hours after the substation attack to destroy forensic evidence and operator workstations).

The chain starts with a corporate credential, moves through the IT/OT boundary, manipulates the
substation via IEC-104, and ends with a simulated wiper that the participant has to detect and
partially recover from. The room is accurate to the documented incident while staying within the
constraints of a single VM.

Difficulty: intermediate to advanced.
Techniques covered: 8 (trust exploitation), 10 (initial access and lateral movement), 2
(intelligence gathering), 1 (unauthorised state manipulation), destructive payload.
Simulator: power-and-light-sim, IEC-104 complete on port 2404, single-process, no Docker.
Prerequisites: familiarity with port scanning and basic web application interaction. Room 1
("Dead Reckoning") is useful but not required.

## Background context for room text

On 12 April 2022, Ukrainian defenders disrupted a Sandworm operation targeting a high-voltage
transmission substation. The attackers had been inside the network for weeks. Their toolkit:
Industroyer2, a purpose-built executable communicating directly via IEC 60870-5-104, and
CaddyWiper, a disk wiper set to execute hours after the substation attack to destroy operator
workstations and delay restoration. The Industroyer2 binary had specific substation IP addresses,
port numbers, and IEC-104 information object addresses hardcoded into it. That level of detail
does not come from a single recon session. Ukrainian defenders detected and disrupted the
operation before execution. This room models what would have happened if they had not.

References: ESET analysis of Industroyer2, Cisco Talos CaddyWiper advisory, MITRE ATT&CK
for ICS technique T0855 (Unauthorised Command Message).

## Tasks

### Task 1: Introduction

Background reading. No flag.

Cover:
* The April 2022 operation: what Industroyer2 is, how it differs from the 2016 original,
  what CaddyWiper does and why it was deployed hours after the main payload
* What IEC 60870-5-104 is and why substations use it
* What the participant will be doing and why the sequencing matters: the wiper is not the
  attack, it is the cover. The attack happened first.

Questions (knowledge check, no flag):
* What protocol did Industroyer2 use to communicate with protection relays?
* What was the purpose of CaddyWiper in the April 2022 operation?
* Why would an attacker delay wiper execution by several hours?

### Task 2: The way in

The VM hosts a simulated corporate web portal on port 8080. It looks like an internal utility
intranet. The login page has default credentials that were never changed after commissioning.

The portal, once accessed, contains internal maintenance documents. One document references the
operational network and includes a note about the substation management interface.

Tools: browser, `curl`, `gobuster` or equivalent.

Questions:
* What are the default credentials for the portal? (discoverable via source comment or
  response header)
* What IP range does the internal document reference for the substation network?

Flag 1: returned in the authenticated session response header. Not visible without valid credentials.

Learning outcome: the initial access vector for the Ukraine 2015 and 2022 operations was the
corporate network, reached via spear-phishing and credential compromise. The OT network was
not directly internet-exposed. The IT/OT path was the attack surface.

### Task 3: Find the substation

Scan the IP range referenced in the internal document. Identify the IEC-104 outstation.

IEC-104 listens on port 2404. A general port scan will find it alongside any other services.
The outstation responds to a STARTDT (start data transfer) command with a STARTDT_CON
confirmation, which confirms it is an IEC-104 device and not something else on the same port.

Tools: `nmap`, any IEC-104 client (`iec104client`, python `lib60870` bindings, or raw TCP
with the APDU framing documented in the room text).

Questions:
* What port does IEC-104 use?
* What is the APDU type identifier for a STARTDT_CON response?
* How many data objects does the outstation report in response to a general interrogation?

Flag 2: returned as a structured string inside one of the spontaneous data objects reported
during general interrogation. It is present in the data, not in a file. Participants who issue
an interrogation command and read every response object will find it.

Learning outcome: IEC-104 general interrogation (type C_IC_NA_1) is the equivalent of a
Modbus function code 3 scan across all addresses. It reveals every data object the outstation
is managing. In a real substation this reveals the entire breaker and measurement topology.

### Task 4: Read the state

Read the current state of the controlled objects. Understand what each information object
address represents before sending any commands.

The outstation exposes:
* Binary inputs (type M_SP_NA_1): breaker status, alarm states
* Measured values (type M_ME_NA_1): voltage, current, frequency
* Single command objects (type C_SC_NA_1): the write surface

The information object addresses map to specific equipment. The mapping is not provided; it is
in the spontaneous data responses and can be inferred from the measured values and their
relationship to the physics engine outputs.

Questions:
* What is the current state of breaker object at information object address *to be determined
  during VM build*?
* What voltage is reported on the feeder measurement object?
* Which information object address accepts write commands?

Flag 3: a specific measured value object contains a flag string encoded in its quality
descriptor field. It is there without any write operation; finding it requires reading every
data object carefully rather than jumping straight to exploitation.

Learning outcome: Industroyer2 had specific information object addresses hardcoded. The
attackers knew which objects controlled which equipment before execution. This task models
the reconnaissance phase that produced that knowledge.

### Task 5: Issue the command

Send a C_SC_NA_1 (single command) to the appropriate information object address to trip the
breaker. Observe the physics engine respond: voltage drops, the breaker status object changes
state, the measurement objects reflect the loss of load.

This is a single APDU. No authentication. No confirmation required beyond the ACT_CON
(activation confirmation) from the outstation.

Questions:
* What IEC-104 type identifier is used for a single point command?
* What cause of transmission value signals that the command was accepted?
* What does the voltage measurement read after the breaker trips?

Flag 4: written to a data object by the physics engine when the breaker trips and the feeder
goes offline. Readable via another interrogation after the command. Not present beforehand.

Learning outcome: Industroyer2 sent exactly this sequence. Open the breaker, confirm the trip,
issue trip-prevention commands to the relay (the relay bypass is covered in the smart-grid room
design, not here). The physical consequence is real and immediate. There is no authentication
step to bypass, no vulnerability to exploit. The protocol does what it was designed to do.

### Task 6: The wiper

CaddyWiper was set to execute hours after Industroyer2. Its job: overwrite configuration files,
event logs, and engineering workstation data to delay forensic analysis and manual restoration.

In the simulation: a wiper script is present on the VM, dormant. It targets power-and-light-sim
configuration files and event logs. It is not triggered automatically. The participant finds it
during post-exploitation exploration of the filesystem, understands what it does, and triggers
it manually to see the effect.

After the wiper runs: the power-and-light-sim configuration is overwritten. The simulator
restarts with a blank state. The event log showing the breaker trip is gone.

A backup copy of the original configuration was written to a non-obvious location during VM
build, simulating an offline backup. The participant has to find it to prove the prior state
existed.

Questions:
* What files does the wiper target? (requires reading the script, not running it blindly)
* After the wiper runs, what is the new state of the breaker object?
* Where is the backup configuration file?

Flag 5: inside the backup configuration file. Not accessible unless the participant found it
before running the wiper, or can infer its path from the wiper script logic.

Learning outcome: the wiper is not the attack. It is the cover. The actual damage was done in
task 5. CaddyWiper's role was to deny defenders the forensic trail they needed to understand
what happened and to slow manual restoration. This task models why incident response in OT
environments requires offline backups and out-of-band logging.

### Task 7: What defenders saw (or did not)

Post-exploitation reflection. No new flag.

Cover:
* how Ukrainian defenders detected the April 2022 operation before execution: anomalous
  network traffic from Industroyer2 pre-positioning, ICS-specific detection signatures
  developed after the 2016 Industroyer incident
* what the IEC-104 traffic looks like to a network monitor during normal operation versus
  during an attack: the command APDUs are not encrypted, are fully readable, and a
  C_SC_NA_1 from an unexpected source at an unexpected time is distinguishable from normal
  polling, if anyone is watching
* impact of what would have happened: a forced substation outage under wartime grid load,
  followed by CaddyWiper destroying the workstation state needed for manual restoration.
  ESET's analysis noted Industroyer2 had specific IP addresses and information object
  addresses hardcoded, indicating reconnaissance that preceded execution by weeks or months.

Defence:
* IEC-104 TLS (IEC 62351): encrypts and authenticates the APDU stream; a C_SC_NA_1 from
  an unauthenticated source would be rejected
* strict network segmentation between IT and OT: removes the pivot path used in task 2
* continuous OT network monitoring with ICS-aware detection: what Ukrainian defenders
  actually had
* offline backups and out-of-band logging: the wiper cannot destroy what it cannot reach

Questions (knowledge check, specific answers required):
* What network-level control prevents unauthenticated IEC-104 command injection?
* What would an anomaly detection system see differently during task 5 versus normal operation?
* Name the MITRE ATT&CK for ICS technique used in task 5.

Reflection (no answer needed):
* Ukrainian defenders detected this operation before execution. What does that require
  operationally that most OT environments do not currently have in place?
* Industroyer2 had specific information object addresses hardcoded into the binary. What does
  that imply about the timeline and level of access required before the payload was deployed?

No flag. The knowledge-check questions require reading. The reflection prompts have no
required answer.

## Flag summary

| Flag | Location                                   | Technique           | How earned                                             |
|:-----|:-------------------------------------------|:--------------------|:-------------------------------------------------------|
| 1    | Authenticated session response header      | 8                   | Default credential login to corporate portal           |
| 2    | IEC-104 data object, general interrogation | 10                  | Pivot from corporate to OT, issue interrogation        |
| 3    | Measured value quality descriptor field    | 2                   | Read every data object before touching anything        |
| 4    | Data object written by physics engine      | 1                   | Correct C_SC_NA_1 command, breaker trips               |
| 5    | Backup configuration file                  | Destructive payload | Wiper understood and located before or after execution |

## VM specification

Base: Debian 8 compatible, BIOS boot, DHCP.
RAM target: functional at 512 MB, comfortable at 1 GB.

Services at startup:
* Corporate web portal (lightweight Flask app) on port 8080
* power-and-light-sim via systemd, IEC-104 outstation on port 2404, physics engines active
* Wiper script present on filesystem, not running as a service

Ports exposed: 8080, 2404. Nothing else.

No internet dependency. All dependencies vendored during VM build. The Flask portal app is
ten lines and a template; it adds negligible RAM overhead.

The wiper script is a short Python or bash file that overwrites a known set of config paths
and clears the event log directory. It is findable via normal filesystem exploration after
gaining any foothold. Running it is irreversible within the session (reboot restores the VM).

## Room title options

* Double Strike (two payloads, sequenced)
* Pivnichna (the substation)
* April 2022
* Lights Out, No Logs

The room text references the real incident directly. The tone stays factual. The scenario is
educational, not sensationalised: Sandworm nearly took a Ukrainian transmission substation
offline; Ukrainian defenders stopped it. The room lets participants understand exactly how.

## References to include in room text

* [Industroyer: Biggest threat to industrial control systems since Stuxnet](https://www.welivesecurity.com/2017/06/12/industroyer-biggest-threat-industrial-control-systems-since-stuxnet/), 2017
* [Industroyer: ICS protocols were developed decades ago with no security in mind](https://www.welivesecurity.com/2017/06/19/industroyer-interview-ics-developed-decades-ago-no-security-mind/), 2017
* [Industroyer2: Industroyer reloaded](https://www.welivesecurity.com/2022/04/12/industroyer2-industroyer-reloaded/), 2022
* [Cisco Talos CaddyWiper advisory](https://blog.talosintelligence.com/threat-advisory-caddywiper/)
* [Industroyer2, Software S1072 | MITRE ATT&CK®](https://attack.mitre.org/software/S1072/)
* [MITRE ATT&CK for ICS T0855](https://attack.mitre.org/techniques/T0855/) (Unauthorised Command Message)
* [MITRE ATT&CK for ICS T0809](https://attack.mitre.org/techniques/T0809/) (Data Destruction, for the wiper task)
* [IEC 60870-5-104 APDU structure reference](https://scadaprotocols.com/iec104-asdu-structure/) (SCADA protocol)
