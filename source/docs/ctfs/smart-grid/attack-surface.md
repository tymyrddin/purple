# Smart grid attack surface reference

This covers the protocols specific to the power grid stack. DNP3 appears in grid deployments but its attack
surface is documented in the OT/ICS section. The consequence framing differs: DNP3 in grid contexts is
overwhelmingly substation-to-control-centre telemetry and control, not PLC interaction.

## IEC 61850

The substation automation standard. Three sub-protocols with distinct attack surfaces.

### GOOSE (Generic Object Oriented Substation Event)

Multicast, no authentication, no encryption. Used for protection signalling between IEDs (breaker trip, relay
pickup, inter-trip commands). Timing is critical: GOOSE messages are retransmitted with increasing intervals,
and a replay within the timing window is indistinguishable from a legitimate message.

Attack surface:

* Replay a captured GOOSE trip message to cause a false breaker operation
* Inject a GOOSE message with a spoofed source MAC to impersonate a protection relay
* Suppress legitimate GOOSE messages to prevent protection from operating (blocking a trip)
* Capture and analyse GOOSE traffic to map the substation protection scheme

What breaks in CTF design: GOOSE operates at layer 2 (Ethernet), not IP. Challenges need a network
environment that handles layer 2 multicast correctly. A plain IP-only Docker network does not work.

### Sampled Values (SV)

Continuous multicast streams of current and voltage measurements from merging units, consumed by protection
IEDs. No authentication.

Attack surface:

* Inject false SV streams to feed incorrect measurements to a protection relay
* Corrupt magnitude or phase angle values to desensitise or misoperate protection functions
* Replay SV from a fault condition to trigger protection during normal operation

What breaks in CTF design: SV challenges require a receiving IED that responds to the stream. Without a
realistic protection model on the receiving end, the consequence is invisible.

### MMS (Manufacturing Message Specification)

Client/server protocol for engineering workstation access to IEDs: reading logs, downloading relay
configuration files, uploading settings.

Port 102/tcp (via ISO/OSI stack) or directly encapsulated.

Attack surface:

* Unauthenticated or weakly authenticated access to relay configuration files
* Read event logs to reconstruct protection history
* Write relay settings to alter protection thresholds (desensitise overcurrent, change trip times)
* Enumerate IED data models to map the substation

What breaks in CTF design: MMS library support is limited. libiec61850 is the practical option. Challenges
that require participants to build their own MMS client are too heavy unless tooling is provided.

## DLMS/COSEM

The smart meter protocol. Used by AMI head-end systems to read meters, set tariffs, and issue disconnect
commands. Authentication exists but is frequently misconfigured or using default keys.

Port 4059/tcp (DLMS over TCP), also serial and HDLC.

Attack surface:

* Authenticate with default or guessed DLMS keys to access meter data
* Issue a remote disconnect command to cut supply to a meter
* Mass disconnect: if the head-end can reach many meters, a crafted command reaches all of them
* Read consumption data without authorisation (privacy impact, or intelligence for targeted attack)
* Tamper with tariff registers to manipulate billing

What breaks in CTF design: DLMS is less widely known than Modbus. Participants need a pointer to a client
library (gurux-dlms is the main open source option). The disconnect consequence needs to be made visible in
the simulation, otherwise the flag is just "command sent".

## IEEE C37.118.2

Synchrophasor protocol for Phasor Measurement Units (PMUs). Used for wide-area monitoring and, increasingly,
protection and control. GPS-synchronised timestamps are integral to the protocol.

Port 4712/tcp (also UDP).

Attack surface:

* Inject false phasor data to corrupt grid state estimation at the control centre
* GPS spoofing to shift PMU timestamps and corrupt synchronisation-dependent calculations
* Replay historical PMU data to mask a real grid event

What breaks in CTF design: GPS spoofing is not easily reproducible in a CTF environment. False data injection
into a receiver is more tractable. Challenges in this area work best when the consequence (incorrect state
estimate, wrong control action) is made observable.
