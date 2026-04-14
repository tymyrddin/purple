# Smart grid attack surface reference (technique-based)

This layer abstracts protocol specifics into attacker techniques. The protocol reference (IEC 61850,
DLMS/COSEM, IEEE C37.118.2) remains the toolbox. This is the playbook.

Where a technique has no confirmed real-world incident against live infrastructure, this is noted.
Theoretically validated means peer-reviewed research has established the method is sound; it does not
mean it has been deployed in the wild.

## 1. Unauthorised state manipulation

Issue commands that directly change physical state.

What it looks like:

* Open or close breakers via IED protocol access
* Disconnect a meter remotely
* Send shutdown commands to edge devices (EV chargers, inverters)
* Write to Modbus registers on heating or substation controllers

Protocols involved:

* IEC 61850 MMS
* DLMS/COSEM (disconnect command)
* Modbus TCP
* IEC 60870-5-104

Incident anchors: FrostyGoop (Lviv, January 2024) sent Modbus write commands to ENERCON heating
controllers across 600 apartment buildings. The Ukraine 2016 attack sent shutdown commands to
serial-to-Ethernet converters at distribution substations using their native protocol; no exploit
required.

Design angle: The interesting surface is not the command. It is whether the consequence is visible in
the simulation. A meter disconnect that changes nothing teaches nothing. DLMS/COSEM mass disconnect is
underappreciated: an attacker with head-end access can reach every meter on the network with one command.

## 2. Process intelligence gathering

Map the system before touching it.

What it looks like:

* Enumerate IEDs and their data models via MMS
* Read PMU streams to reconstruct grid state
* Passively capture GOOSE traffic to map the protection scheme
* Read meter data without issuing commands

Protocols involved:

* IEC 61850 MMS (IED enumeration, log access)
* IEEE C37.118.2 (PMU stream capture)
* IEC 61850 GOOSE (passive layer 2 capture)
* DLMS/COSEM (read-only meter access)

Design angle: Reconnaissance before action. The Industroyer2 binary had specific substation IP
addresses, port numbers, and information object addresses hardcoded into it. That level of detail does
not come from guessing. Passive GOOSE capture is a specific technique worth including: the protection
scheme of a substation is visible in GOOSE traffic without sending a single packet.

## 3. Data integrity manipulation and false data injection

Lie to the operator or the control system.

What it looks like:

* Inject false telemetry readings to SCADA or the historian
* Feed incorrect current or voltage measurements to a protection relay via spoofed SV streams
* Falsify PMU data to corrupt grid state estimation at the control centre
* Replay frozen values during a destructive operation to mask it

Protocols involved:

* IEC 61850 GOOSE and SV
* IEEE C37.118.2
* DLMS/COSEM

Incident anchors: Stuxnet fed pre-recorded centrifuge speed data back to operators at Natanz for
months while the machines were being destroyed. Industroyer replayed frozen network state data to mask
its own actions during the 2016 Ukraine blackout. A 2009 paper by Liu, Ning, and Reiter demonstrated
mathematically that an attacker who knows the network topology can manipulate multiple meter readings
simultaneously in a way that passes every consistency check the control system performs.

Design angle: The Stuxnet and Industroyer replay techniques are incident-proven. SV stream injection
into a live protection relay is theoretically validated and the standard provides no mechanism to prevent
it, but has no confirmed real-world incident. The Liu-Ning-Reiter result covers state estimation; direct
SV injection into a protection IED is a related but distinct surface. The best attacks do not break the
system. They convince it everything is fine while it quietly breaks itself.

## 4. Replay and timing attacks

Reuse valid traffic to reproduce effects or desynchronise systems.

What it looks like:

* Capture a GOOSE trip message and replay it within the timing window
* Feed frozen SCADA data during a destructive phase
* Exploit GPS timestamp dependency in PMU synchronisation

Protocols involved:

* IEC 61850 GOOSE (layer 2, timing-critical retransmission model)
* IEEE C37.118.2 (GPS-synchronised timestamps)

Incident anchor: Stuxnet used replay of recorded monitoring data to show normal operation to the
control room while centrifuges were being damaged.

Design angle: GOOSE replay requires a layer 2 network environment. A plain IP-only Docker network does
not work, which is a constraint worth solving before building the challenge, not during. The GPS
timestamp dependency in PMU synchronisation is a real surface but has no confirmed real-world
exploitation; it is worth teaching as context for why time integrity matters in wide-area protection.

## 5. Demand and load manipulation

Exploit the grid's trust in its own demand signals.

What it looks like:

* Falsify consumption data to distort energy management system dispatch
* Coordinate simultaneous switching of large controllable loads (EV chargers, smart thermostats)
* Abuse demand-response aggregation platforms to create artificial load spikes

Protocols involved:

* DLMS/COSEM (tariff register manipulation)
* EV charger management APIs

Research anchors (no confirmed real-world attack): A 2018 Princeton study estimated that coordinating
simultaneous switching of a few percentage points of grid demand could trigger frequency deviations
large enough to trip generation. A 2022 ACM paper demonstrated that coordinated switching of a large EV
charger fleet could create demand fluctuations sufficient to destabilise the local grid, with no
vulnerability required, only access to the charger management APIs. Both results are theoretically sound
and have informed utility threat modelling; neither represents a confirmed attack.

Design angle: The attack surface is the aggregation layer, not individual devices. A single switched
device is noise. A thousand switched simultaneously is a grid event. Worth including in CTF design as
a theoretically grounded scenario, framed honestly as such.

## 6. Grid frequency and synchronisation attacks

Manipulate the signals that govern whether the grid stays balanced.

What it looks like:

* Inject false phasor data to corrupt state estimation at the control centre
* Spoof GPS signals to shift PMU timestamps and corrupt synchronisation-dependent calculations
* Replay historical PMU data to mask a real grid event

Protocols involved:

* IEEE C37.118.2 (phasor data streams, GPS timestamp dependency)

Incident anchors (consequence demonstrated by natural events, not cyberattacks): In November 2006, a
single line trip in Germany caused a cascade that split the European synchronous grid into three islands;
frequency dropped to 49.0 Hz in the western island and rose to 50.6 Hz in the eastern one. In August
2019, two simultaneous generator trips dropped UK grid frequency to 48.88 Hz and triggered automatic
load disconnection affecting nearly a million customers. Both demonstrate that the protective systems
themselves are the mechanism through which a frequency anomaly becomes an outage. No cyberattack has
confirmed PMU false data injection or GPS spoofing against live grid infrastructure.

Design angle: GPS spoofing is not easily reproducible in a lab. False data injection into a PMU
receiver is more tractable and theoretically validated. The challenge works when the consequence
(incorrect state estimate, wrong control action) is observable in the simulation. Frame this honestly:
the technique is plausible and the consequence is real, but it has not been confirmed in the wild.

## 7. Protection relay bypass

Disable the automatic safety switches before triggering the fault.

What it looks like:

* Send commands via IED protocol access to disable protection functions
* Issue trip-prevention commands to prevent automatic reclosure after a forced outage
* Alter relay settings to change trip thresholds or operating times

Protocols involved:

* IEC 61850 MMS
* IEC 60870-5-104

Incident anchor: Industroyer/CRASHOVERRIDE (Ukraine, December 2016) contained a dedicated module that
communicated directly with protection relays using IEC 61850 and issued trip-prevention commands,
preventing them from automatically reclosing and restoring supply. Without that bypass, the grid's
reclosers would have restored power within seconds. The module was written to understand the operational
logic of the protection equipment, not simply to crash it.

Design angle: The bypass is what separates a momentary outage from a sustained one. A challenge that
sequences relay bypass followed by a fault is teaching something real.

## 8. Safety instrumented system attacks

Remove the last automatic barrier before triggering the hazardous condition.

What it looks like:

* Take SIS controllers offline while they appear operational
* Put controllers into program mode, disabling safety response logic
* Confirm the SIS is inactive before initiating the primary attack

Incident anchor: Triton/TRISIS (Tasnee, Saudi Arabia, 2017) exploited a zero-day in Schneider Electric
Triconex firmware to put safety controllers into program mode. In that mode, they do not execute safety
response logic. From outside, they appeared operational. The attack was discovered by accident: a logic
error in the malware caused two controllers to enter fail-safe state independently, triggering an
automatic plant shutdown and prompting the investigation that found it.

Design angle: Triton was discovered because of a bug. Had it worked cleanly, no one would have known
until the hazardous condition developed with no automated response. The sequencing, SIS offline then
fault triggered, is the kill chain worth teaching.

## 9. Physical consequence engineering

Use protocol access to cause physical damage, not just operational disruption.

What it looks like:

* Cycle equipment operating parameters outside mechanical tolerances (thermal stress)
* Reconnect a generator out of phase with the grid (Aurora-style phase mismatch)
* Hold protective systems inactive while physical damage accumulates

Incident anchors: Stuxnet modified centrifuge rotor speed commands to cause the machines to spin
intermittently at speeds outside their designed tolerances, while intercepting monitoring communications
and replaying normal values to the operators. The Aurora Generator Test (Idaho National Laboratory,
March 2007) used open and close commands on a circuit breaker to repeatedly reconnect a 2.25 MW
generator out of phase with the grid. The electromagnetic forces destroyed the machine in under two
minutes. Every large generator has a remotely operable breaker. Aurora abuses that feature, not a
vulnerability. The remediation is well understood and has been slow to deploy across ageing
infrastructure; the attack surface remains broadly present.

Design angle: Aurora requires no exploit. It requires remote breaker access and deliberate mis-timing.
That is both the simplicity and the point.

## 10. Destructive payloads

Overwrite or encrypt systems to maximise recovery time and destroy evidence.

What it looks like:

* Wiper malware targeting historian databases, configuration files, firmware images, and event logs
* Ransomware on engineering workstations and SCADA applications at the IT/OT boundary
* Timed payload execution set to fire hours after the primary attack, when defenders are already
  responding

Incident anchors: After the 2015 Ukraine blackout, KillDisk overwrote operator workstation master boot
records, delaying restoration. In April 2022, Sandworm deployed Industroyer2 against a Ukrainian
high-voltage substation alongside CaddyWiper, a disk-wiping tool timed to execute several hours later
to destroy forensic evidence. Colonial Pipeline (May 2021) shut down 45% of US East Coast fuel supply
after DarkSide ransomware infected the IT network; the OT systems were not compromised, but operating a
5,500-mile pipeline without reliable IT support was considered too risky. The initial access vector was
a VPN credential with no multi-factor authentication.

Design angle: Wipers are the clean-up crew. The interesting CTF angle is sequencing: what did the
attacker achieve before deploying the payload, and how much can a participant reconstruct from what
survives?

## 11. Trust exploitation and misconfiguration abuse

Abuse the assumption that everything inside the network is authorised.

What it looks like:

* Authenticate with default or guessed DLMS keys to access or disconnect meters
* Access MMS interfaces without authentication to read logs or write relay settings
* Reach Modbus-enabled devices directly from the internet, no pivot required

Protocols involved:

* DLMS/COSEM (default keys, unauthenticated meter access)
* IEC 61850 MMS (unauthenticated IED access)
* Modbus TCP (internet-exposed endpoints)

Incident anchor: FrostyGoop investigators noted that the target devices were accessible from the
internet. Shodan routinely indexes tens of thousands of Modbus-enabled devices with no firewall between
them and the public internet.

Design angle: This is the bridge to reality. Most confirmed ICS incidents do not start with a zero-day.
They start with a credential, a default password, or an exposed port that nobody noticed was listening.

## 12. Initial access and lateral movement through the IT/OT boundary

Reach the OT environment from adjacent systems that span the divide.

What it looks like:

* Compromise an engineering workstation with legitimate protocol access to IEDs and protection relays
* Abuse vendor remote access channels: persistent VPN or remote desktop sessions installed for
  maintenance, rarely monitored
* Pivot via the SCADA or energy management system historian: often dual-homed, running standard Windows,
  and protected adequately by neither the IT nor OT team
* Use the HMI as a command-issuing endpoint: it has full protocol access to the substation or metering
  network and is often the most accessible Windows machine in the OT zone

Incident anchors: Triton/TRISIS was installed on an engineering workstation that had legitimate access
to the Triconex safety controllers. Industroyer and BlackEnergy (Ukraine 2015) both reached OT systems
through prior compromise of the corporate IT network. Colonial Pipeline's initial access was a VPN
credential with no multifactor authentication.

Design angle: The initial access layer is almost entirely absent from published CTF challenges, which
typically drop the participant already inside the OT network. Including even a simple EWS-to-IED pivot
teaches something most participants have never practised, and reflects how the vast majority of real
grid incidents actually begin.

*"Disconnect power to building 7 without triggering an alert in the SCADA dashboard"* gives options: 
direct disconnect command (loud, obvious), meter data falsification first (subtle), relay bypass then 
fault (persistent consequence). Learning happens.
