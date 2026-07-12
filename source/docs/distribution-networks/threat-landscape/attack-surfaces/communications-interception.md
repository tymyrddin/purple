# Communications interception

Threats to the network and communications layer: eavesdropping on control messages, protocol manipulation,
man-in-the-middle attacks on SCADA communications, metering data interception, and telecontrol protocol compromise.

This layer includes telecontrol protocols between the control room and field devices, SCADA-to-GIS communications,
metering data channels, network segmentation, and the boundaries between IT and OT networks.

## Protocol vulnerabilities

Telecontrol communication between Stedin's control room and field devices runs over IEC 60870-5-104 (a TCP-based
protocol for SCADA) with a transition in progress toward IEC 61850 (which adds richer information and is still being
integrated with e-terracontrol and the Smallworld GIS). IEC 60870-5-104 was designed assuming perimeter security 
(electric utilities do not trust the network), not message-level authentication. A frame travelling from the control 
room to an RTU in one of the medium-voltage stations carries a command (Open, Close, SetPoint) but does not
cryptographically sign that command. If an attacker with network access can inject, modify or replay a frame, the
protocol provides no defence.

In the connected network (where e-terracontrol SCADA communicates with Smallworld GIS for network-model updates,
with the historian for data logging, and with remote access for field engineers), the telecontrol traffic shares network
segments with other applications. An attacker who compromises an engineering workstation or gains access to the
control-room network segment through phishing or supply-chain compromise can eavesdrop on telecontrol frames. IEC
60870-5-104 sends commands in plaintext, so observing the traffic reveals what switching operations are being commanded.
More dangerously, an attacker can capture a frame (say, a command to Close a switchpoint at a specific
substation), replay it later, and cause the same switching operation again without the operator's knowledge.

Understanding what Stedin systems communicate, how they integrate, and what network paths carry critical data is the threat surface, and [the map of systems and communication boundaries](../../operating-context/system-composition/vendor-platform.md) shows where interception is possible and what observable traces it leaves in field device logs.

Stedin's smart meters (Landis+Gyr, Iskraemeco, Kaifa, and Sagemcom units) communicate over a CDMA machine-to-machine
network operated by Utility Connect. Metering data is encrypted in transit, but the encryption key is held in the meter
device and in Utility Connect's backend. If the encryption scheme is weak or the key-generation process is predictable,
an attacker might derive the key and decrypt traffic. If the key-provisioning infrastructure (the system that generates
and distributes keys to the new meters) is compromised, an attacker could generate fraudulent keys and either
intercept and decrypt metering data or inject false metering reports. ENCS runs independent cyber audits of meter
manufacturers, and the smart-meter tenders in the Netherlands include security review, but the actual key-management
architecture for Stedin's millions of deployed meters is not publicly visible.

## Telecontrol message manipulation

    NORMAL FLOW (IEC 60870-5-104)
    ─────────────────────────────────────────

    e-terracontrol         Network segment        RTU            Field device
    (SCADA)                (TCP/IP)               
         │                                        │              │
         ├─ Close Switchpoint A ─────────────────>│              │
         │  (plaintext, unsigned)                 │              │
         │                                        ├─ Close ─────>│ (actual physical)
         │                                        │              │ relay coil
         │<──── ACK: Closed ──────────────────────┤              │
         │                                        │              │
         └─ Read state ──────────────────────────>│              │
            (polling)                             │              │
                                           Closed <──────────────┤
                                                  |

    Operator sees: Switchpoint A = CLOSED ✓ (correct)


    ATTACK 1: Command Manipulation (man-in-the-middle)
    ──────────────────────────────────────────────────

    e-terracontrol         [ATTACKER HERE]             RTU         Field device
    (SCADA)                (network access)       
         │                       │                      │              │
         ├─ Close Switchpoint A ─┤                      │              │
         │                       ├─ INTERCEPT           │              │
         │                       ├─ MODIFY to           │              │
         │                       │  "Open B"            │              │
         │                       ├─ RETRANSMIT          │              │
         │                       └─ Open Switchpoint B  │─────────────>│
         │                                              │              │ (wrong device!)
         │                                              ├── OPEN ─────>│ (relay opens)
         │                       ┌─ RTU reports: B opened
         │                       ├─ INTERCEPT ACK       │              │
         │                       ├─ SPOOF REPLY         │              │
         │<──── FALSE ACK: A Closed ────────────────────┤              │
         │  (attacker lies: says A closed, actually B opened)
         
    Operator sees: Switchpoint A = CLOSED (thinks it worked)
    Reality: Switchpoint B is now OPEN (unintended consequence)
    Result: Network configuration mismatches switching plan
            Fused load energises, protection zone fails


    ATTACK 2: State Report Spoofing
    ───────────────────────────────────────────────

    e-terracontrol         [ATTACKER HERE]             RTU        Field device
    (SCADA)                (network access)       
         │                        │                     │              │
         ├─ Read state ──────────>│                     │              │
         │  (poll for current)    │                     │              │
         │                        ├─── Read ───────────>│              │
         │                        │         Actual state: CLOSED       │
         │                        │  (RTU knows truth)                 │
         │                        │                     │              │
         │                        ├─── INTERCEPT        │              │
         │                        │ (RTU reports: CLOSED)              │
         │                        ├─── SPOOF reply      │              │
         │                        │ (change to: OPEN)   │              │
         │<──── FALSE: OPEN ──────┤                     │              │
         │                                              │              │

    Operator sees: Switchpoint = OPEN (false belief!)
    Reality: Switchpoint is CLOSED (unprotected)
    Result: Operator makes unsafe decisions based on false mental model
            E.g., "de-energise this zone" when it's already energised
            E.g., "protection is working" when it's actually disabled


An attacker with network access can do more than eavesdrop: modify frames. An RTU expects commands in a specific 
sequence and format. An attacker intercepts a command (Close switchpoint A), modifies it (Open switchpoint B), and retransmits. The RTU 
executes the modified command. The operator sees no problem: they issued Close A, the system acknowledges, the RTU 
opens B.

The field operation now mismatches operator intent. Planned switching sequence to isolate a fault gets corrupted en 
route. One device opened when it should close. Network configuration no longer matches the switching plan. A fused 
load energises. A protection zone isn't isolated. A device enters an unsafe state. The operator detects this through 
state reports: a switchpoint they commanded to Open still reports Closed. But the delay is seconds. If multiple 
commands are corrupted, the operator might attribute it to RTU malfunction rather than attack.

A more sophisticated attack modifies not the command but the state report coming back from the RTU. An attacker who can
inject frames into the telecontrol path could make the control room believe that a switchpoint is Open when it is
actually Closed, or that a fault has been cleared when it has not. The operator makes decisions based on the reported
state. If the reported state is false, the operator's decisions are based on a corrupted mental model of the network.
This attack is particularly dangerous because the operator might take actions that are safe in the actual network state
but dangerous in the believed state.

## Metering data interception

Smart meters deployed across Stedin's service area report consumption data across CDMA networks to the billing system. 
An attacker with access to the CDMA infrastructure or the metering backend could intercept and modify consumption 
data. The customer's meter would report low consumption, reducing their invoice and, over time, producing significant 
financial fraud.

The attack requires either access to the CDMA network (operated by Utility Connect, separate from the operator's own network),
access to the metering backend (hosted by Stedin or by a service provider), or physical
access to a meter to reprogram it. If a reprogrammed meter can be installed (or an existing meter physically replaced),
the compromised meter will under-report consumption. Because meters are deployed in high volumes and scattered across
the network, discovering a compromised meter requires either comparing meter readings against expected consumption
profiles, or continuous physical inspection of meter devices.

A related attack targets the metering data before it reaches billing. If an attacker can modify the provisioning keys or
the authentication mechanism used by meters, they could inject false meter readings into the stream before billing
processing. This would be harder to detect than a physical meter compromise, because the false readings would appear to
come from legitimate meters.

## Network segmentation bypass

Stedin's architecture includes SCADA (e-terracontrol for SCADA/EMS and e-terra distribution for DMS), a GIS network
model (Smallworld with Lovion integration), an asset-management system (IBM Maximo), and connection to field devices (
RTUs, protection relays, meters). These systems are typically on separate network segments with firewalls and air
gaps between them. Network segmentation is implemented to prevent compromise of one layer from spreading to another.

An attacker who breaches Stedin's IT network (SAP, Azure, email) is not immediately able to reach SCADA, because
e-terracontrol sits on a separate segment. But e-terracontrol and Smallworld GIS are integrated through APIs, and the IT
and OT networks both have internet access for patches and for remote engineering. If an attacker can compromise an
engineering workstation (which has access to both IT and OT networks, or alternately has access to one and then jumps to
another), they can cross the segmentation boundary. Alternatively, an attacker who compromises a software supply-chain
update (SIPROTEC or SEL relay firmware, engineering tools like DIGSI 5 or AcSELerator QuickSet, or e-terracontrol
patches) can insert malicious code that runs with the privileges of the application that executes it. If that
application has access to both network segments, the malicious code inherits that access.

Vendor remote-access sessions for maintenance and support are a known bypass vector. When a vendor connects to engineer
a relay or update SCADA software, that connection often requires elevated access to parts of the network that would
normally be firewalled. If an attacker can compromise the vendor's infrastructure or intercept the vendor's connection 
(through compromised credentials or network interception), they can use that session to cross segmentation.

## Observable traces

What communication interception might look like in logs and network evidence.

Telecontrol traffic interception and modification leaves traces in several places. First, the RTU has state-transition
logs: it records when a command arrived, what command it was, and whether it executed successfully. If a command was
received but does not match what Stedin's control room operator intended (the operator commanded Close but the RTU log
shows it received Open), that divergence is evidence of manipulation. Second, the control room records commands
issued and state reports received in e-terracontrol. If the control room log shows "Issued Close to Switchpoint A,
received confirmation" but the field device log shows "Received Open to Switchpoint B", the mismatch is evidence of a
frame being corrupted in transit. Third, if a replay attack occurs (the same switching command executed twice in quick
succession), the device logs will show two identical commands arriving very close together without an intervening
command from the operator.

Metering fraud leaves traces in consumption profiles. If a large industrial customer's metered consumption suddenly
drops without a corresponding change in their business operations, that can trigger investigation. Similarly, if many
meters in a geographic area suddenly show reduced consumption, that can indicate systematic meter reprogramming.
The metering audit processes in Stedin's billing system compare current readings against historical profiles and flag
anomalies.

Network segmentation bypass attempts leave traces in the network logs and firewall records. An engineering
workstation attempting to communicate with e-terracontrol SCADA infrastructure while also communicating with the
internet is unusual and out of pattern. Vendor remote-access sessions typically require logging of the connection
time, duration, what systems were accessed, and what was changed. An unusually long session, access to unexpected
systems, or changes that diverge from the stated purpose of the session are warning signs for Stedin's security
operations. Defenders who understand [when and how network access is permitted for maintenance](../../operating-context/operations-and-cadence/operational-procedures-and-change.md)
can distinguish legitimate engineer activity from anomalous access.

The most difficult traces to detect are false state reports sent by a compromised RTU or injected by an attacker who has
compromised the e-terracontrol SCADA gateway. If an RTU is reporting false state, the operator's state view is
corrupted, and the operator's decisions are made on the basis of false information. The evidence of this would appear
only after the fact, when comparing e-terracontrol's historical log of reported state against the actual field device
state, or when an expected alarm does not trigger because the condition the alarm is supposed to monitor was masked by
false reporting.

*Last updated: 10 July 2026*
