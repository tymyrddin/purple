# Communications interception

The network and communications layer draws several kinds of attack: eavesdropping on control messages, protocol manipulation,
man-in-the-middle attacks on SCADA communications, metering data interception, and telecontrol protocol compromise.

## Protocol vulnerabilities

Telecontrol between a control room and field devices probably runs over
[IEC 60870-5-104](https://blue.tymyrddin.dev/docs/ot/protocols/iec60870-5-104), a protocol built for a trusted perimeter
rather than message-level authentication: a frame carrying a command (Open, Close, SetPoint) is not cryptographically
signed, so an attacker with network access can inject, modify or replay it and the protocol offers no defence.

In a connected network where e-terracontrol SCADA communicates with Smallworld GIS for network-model updates,
with a historian for data logging, and with remote access for field engineers, the telecontrol traffic shares network
segments with other applications. An attacker who compromises an engineering workstation or gains access to the
control-room network segment through phishing or supply-chain compromise can eavesdrop on telecontrol frames. IEC
60870-5-104 sends commands in plaintext, so observing the traffic reveals what switching operations are being commanded.
More dangerously, an attacker sitting in the traffic can replay a captured command frame, a Close to a specific
switchpoint, and cause the same operation again without the operator's knowledge. That needs a man-in-the-middle
position on the link: 104 runs over a TCP session with send-and-receive sequence numbers, so a frame
merely captured and resent later falls out of sequence and is dropped.

Understanding what systems communicate, how they integrate, and what network paths carry critical data is the 
threat surface, and 
[a map of systems and communication boundaries](../../operating-context/system-composition/vendor-platform.md) shows 
where interception is possible and what observable traces it leaves in field device logs.

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

    Operator sees: Switchpoint A = CLOSED (correct)


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
    Result: the field no longer matches the switching plan, the intended
            close never happened and an unrelated switchpoint has opened,
            de-energising a section no one meant to


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

    Operator sees: Switchpoint = OPEN (false belief)
    Reality: Switchpoint is CLOSED, the line is still live
    Result: the operator acts on a false picture, treating a live section
            as dead, for instance clearing a crew to work a line the
            report calls open while it is actually energised


Attackers with network access can do more than eavesdrop. They can modify frames. An RTU expects commands in a specific 
sequence and format. If these are known, an attacker can intercept a command (Close switchpoint A), modify it 
(Open switchpoint B), and retransmit. The RTU then executes the modified command. The operator sees no problem: they 
issued Close A, the system acknowledges, the RTU opens B.

The field operation now mismatches operator intent. The planned switching sequence to isolate a fault gets corrupted en 
route. A device opens where a close was commanded, the field no longer matches the switching plan, and a section meant to be
isolated stays live while another goes dark. The operator detects this through 
state reports: a switchpoint they commanded to Open still reports Closed. But the delay is seconds. And if multiple 
commands are corrupted, the operator might attribute it to RTU malfunction rather than attack.

A more sophisticated attack modifies not the command but the state report coming back from the RTU. An attacker who can
inject frames into the telecontrol path could make the control room believe that a switchpoint is Open when it is
actually Closed, or that a fault has been cleared when it has not. The operator makes decisions based on the reported
state. If the reported state is false, the operator's decisions are based on a corrupted mental model of the network.
This attack is particularly dangerous because the operator might take actions that are safe in the actual network state
but dangerous in the believed state.

## Metering data interception

Smart meters deployed across [the portrait's service area](../../operating-context/system-portrait.md) report 
consumption data across CDMA networks to the billing system. An attacker with access to the CDMA infrastructure or the 
metering backend could intercept and modify consumption data. The customer's meter would report low consumption, 
reducing their invoice and, over time, producing significant financial fraud.

The attack requires either access to the CDMA network (operated by Utility Connect, separate from the operator's own 
network), access to the metering backend (hosted by a service provider), or physical
access to a meter to reprogram it. If a meter can be reprogrammed (or physically replaced) to report figures the attacker 
chooses, the compromised meter will start under-reporting consumption. Because meters are deployed in high volumes
and scattered across the network, a compromised one hides until its readings part from its
[consumption profile, or the feeder measurement they should sum to](../../observable-semantics/measurements-and-data-records/metre-data-semantics.md).

A related attack targets the channel rather than the meter. The CDMA traffic is generally encrypted, but the key sits in
the meter and in Utility Connect's backend: a weak scheme or a predictable key-generation process lets an attacker derive
it and read the traffic, and a compromised key-provisioning infrastructure lets them mint fraudulent keys to decrypt the
stream or inject false readings before billing, harder to catch than a physical compromise because the forged readings
appear to come from legitimate meters. How robust the key-management really is stays uncertain: ENCS audits the meter
manufacturers and the Dutch smart-meter tenders include security review, but the architecture across millions of deployed
meters is not publicly visible.

## Network segmentation bypass

The portrait's architecture includes SCADA (e-terracontrol for SCADA/EMS and e-terra distribution for DMS), a GIS network
model (Smallworld with Lovion integration), an asset-management system (IBM Maximo), and connection to field devices 
(RTUs, protection relays, meters). These systems are on separate network segments with firewalls and air
gaps between them. Network segmentation is implemented to prevent compromise of one layer from spreading to another.

An attacker who breaches the IT network (SAP, Azure, email) is not immediately able to reach SCADA, because
e-terracontrol sits on a separate segment. But e-terracontrol and Smallworld GIS are integrated through APIs, and the IT
and OT networks both have internet access for patches and for remote engineering. If an attacker can compromise an
engineering workstation (which has access to both IT and OT networks, or alternatively has access to one and then jumps to
another), they can cross the segmentation boundary.

Alternatively, an attacker who compromises a software supply-chain
update (SIPROTEC or SEL relay firmware, engineering tools like DIGSI 5 or AcSELerator QuickSet, or e-terracontrol
patches) can insert malicious code that runs with the privileges of the application that executes it. If that
application has access to both network segments, the malicious code inherits that access.

Vendor remote-access sessions for maintenance and support are a known bypass vector. When a vendor connects to engineer
a relay or update SCADA software, that connection often requires elevated access to parts of the network that would
normally be firewalled. If an attacker can compromise the vendor's infrastructure or intercept the vendor's connection 
(through compromised credentials or network interception), they can use that session to cross segmentation.

## Observable traces

Telecontrol interception shows up as a divergence between records that should agree. A received command that differs
from the one the control room issued, or a reported success the field device's state contradicts, sits in the
[RTU's own logs](../../observable-semantics/field-devices-and-protection/rtu-behaviour.md); a frame replayed twice in
quick succession, or a segmentation crossing, an engineering workstation talking to both the OT network and the
internet, or a vendor session reaching past its stated purpose, sits in the
[packet capture and firewall record](../../observable-semantics/network-and-time/communications-evidence.md).

Metering fraud shows in the
[consumption profile](../../observable-semantics/measurements-and-data-records/metre-data-semantics.md): a large
customer's metered draw dropping with no change in their operations, or a whole area's readings falling together, read
against the profile and the wholesale-versus-metered balance the billing platform tracks.

The hardest to catch is a false state report, from a compromised RTU or injected at the SCADA gateway, because it
corrupts the operator's picture without any single record looking wrong. It surfaces only after the fact, when the
reported state is set against the field device's actual state, or when an alarm that should have fired never does.

*Last updated: 13 July 2026*
