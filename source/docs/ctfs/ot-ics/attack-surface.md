# OT/ICS attack surface reference

These are the protocols in scope for the simulation environments. Each entry covers what the protocol does,
what it exposes, and what an attacker can do with it. This is the reference layer for challenge design: if a
technique does not appear here, the simulation environments probably do not support it.

## Modbus

Port 502/tcp. No authentication. No encryption. Designed for serial communication in the 1970s and never
meaningfully updated for network environments.

Attack surface:

* Read coils and registers without any credential check (FC01, FC02, FC03, FC04)
* Write coils and registers to force physical state changes (FC05, FC06, FC15, FC16)
* No audit trail at the protocol level
* Responses are deterministic and easy to spoof

What breaks in CTF design: Modbus function code attacks are simple to demonstrate but easy to make too obvious.
The interesting design space is in the consequence, not the write itself. What happens to the physical model when
the coil flips?

## DNP3

Port 20000/tcp (also serial). Designed for SCADA communications in electric utilities. Secure Authentication v5
exists but is rarely deployed. Base DNP3 has no authentication.

Attack surface:

* Unauthenticated control relay output block (CROB) messages to operate breakers and switches
* Read analog and binary inputs to exfiltrate process data
* Replay attacks: captured control messages re-sent to reproduce an effect
* Spoofed unsolicited responses to inject false data into the SCADA historian

What breaks in CTF design: DNP3 object variations are not intuitive without a protocol reference. Challenges
that require participants to decode object group/variation pairs need a clear resource pointer or the challenge
becomes a documentation scavenger hunt rather than a technique exercise.

## IEC 60870-5-104 (IEC-104)

Port 2404/tcp. The network adaptation of IEC 60870-5-101, used widely in European utilities and grid control.
No authentication in the base standard.

Attack surface:

* Inject control commands (type identifier C\_SC\_NA\_1 for single commands, C\_DC\_NA\_1 for double commands)
* Read process information spontaneously or by interrogation
* Force a general interrogation to map all data objects on the outstation
* Craft malformed APDUs to test outstation error handling

What breaks in CTF design: IEC-104 is less familiar than Modbus to most participants. Challenges work better
when the protocol framing is part of the learning, not an obstacle to it.

## OPC UA

Port 4840/tcp. The current standard for OT/IT integration. Has a security model, but anonymous access is
commonly enabled and certificates are frequently self-signed or bypassed.

Attack surface:

* Anonymous browsing of the node namespace reveals process structure, variable names, and live values
* Read and write process variables where the security policy allows
* Credential sniffing when running without TLS (OPC UA Basic128Rsa15 or None security mode)
* Node enumeration to map the entire information model before touching anything

What breaks in CTF design: OPC UA's security model means the challenge design has to make a deliberate choice
about what is misconfigured and why. A well-designed OPC UA challenge teaches configuration review, not just
tool use.

## Siemens S7

Port 102/tcp. Proprietary Siemens protocol for communicating with S7-series PLCs. No authentication in S7comm.
S7comm-plus (used in newer firmware) has partial protection but has been partially broken.

Attack surface:

* Read and write data blocks (DBs) without authentication
* Start and stop PLC CPU execution
* Enumerate firmware version and hardware configuration
* Upload and download program blocks

What breaks in CTF design: S7 attacks require snap7 or equivalent. Participants without prior Siemens exposure
may spend most of their time on tooling rather than the technique. Works better as an advanced challenge with
explicit tool documentation.

## MQTT

Port 1883/tcp (unencrypted), 8883/tcp (TLS). Publish/subscribe protocol designed for constrained IoT devices.
Authentication is optional and frequently disabled or set to default credentials.

Attack surface:

* Subscribe to wildcard topic `#` to receive all messages on the broker
* Publish false sensor readings to poison the data feed
* Enumerate retained messages to recover historical state
* Broker access with default or no credentials

What breaks in CTF design: MQTT is easy to interact with and produces visible results quickly. The risk is that
challenges become trivially solvable with a single `mosquitto_sub -t '#'`. The interesting design space is in
what the injected data causes downstream.
