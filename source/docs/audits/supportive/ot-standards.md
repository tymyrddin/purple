# OT/ICS standards

These standards cover security for operational technology and industrial control systems. They are distinct from
the ISO/IEC 27000-series in scope (physical processes, safety-critical systems, real-time constraints) and in
structure. Most are purchasable rather than freely available.

For information security management standards (ISO 27001 series), see [ISO/IEC information security standards](standards.md).
For EU regulatory instruments (NIS2, DORA, CER), see [EU regulations reference](eu-regulations.md).

## IEC 62443 series

The IEC 62443 series is the primary international standard family for industrial automation and control system
(IACS) security. It is also published as ISA-62443 by the International Society of Automation, with identical
content under different numbering.

The series is organised into four groups:

### Series 1: General

Foundation documents covering terminology, concepts, and the IACS security lifecycle.

* IEC 62443-1-1: *Terminology, concepts, and models*
  Defines the vocabulary and conceptual model used across the series, including the zone-and-conduit model for
  segmenting ICS environments.
* IEC 62443-1-2: *Master glossary of terms and abbreviations*
  Reference glossary for the series.
* IEC 62443-1-3: *System security conformance metrics*
  Defines how to measure conformance with the series requirements.
* IEC 62443-1-4: *IACS security lifecycle and use cases*
  Describes the full lifecycle from design through decommissioning and provides use cases for applying the series.

### Series 2: Policies and procedures

Requirements and guidance for the organisations operating or supplying IACS environments.

* IEC 62443-2-1: *Requirements for an IACS security management system*
  Defines what an asset owner needs to establish and maintain security for an IACS environment. The closest
  equivalent to ISO 27001 for OT.
* IEC 62443-2-2: *Operating an IACS security programme*
  Guidance for day-to-day operation of IACS security processes.
* IEC 62443-2-3: *Patch management in the IACS environment*
  Specific requirements for patching in environments where downtime is costly and update cycles are long.
* IEC 62443-2-4: *Requirements for IACS service providers*
  Security requirements for system integrators and service providers working on IACS environments.

### Series 3: System

Requirements and guidance at the system and architecture level.

* IEC 62443-3-2: *Security risk assessment for system design*
  Risk assessment methodology specific to IACS, including how to assign security levels to zones and conduits.
* IEC 62443-3-3: *System security requirements and security levels*
  Defines four security levels (SL 1 to SL 4) and the system requirements corresponding to each. The central
  reference for scoping controls against a defined threat capability.

### Series 4: Component

Requirements at the individual device and software component level.

* IEC 62443-4-1: *Product security development lifecycle requirements*
  Secure development lifecycle requirements for manufacturers of IACS components. Relevant for procurement
  decisions and vendor assessments.
* IEC 62443-4-2: *Technical security requirements for IACS components*
  Defines component-level security capabilities required to meet each security level. Used to evaluate whether
  individual devices meet the security level assigned to their zone.

## Related OT security standards

### ISO 27019:2017

*Information security controls for the energy utility industry*

An extension of ISO 27002 tailored to the energy sector, covering control systems, smart metering, and
communications infrastructure. Useful for energy utilities seeking to align ISO 27001 controls with OT-specific
requirements.

### IEC 62351 series

*Power systems management and associated information exchange: data and communications security*

A family of standards covering security for power system communications protocols (IEC 60870, IEC 61850,
DNP3). Addresses authentication, encryption, and access control at the protocol level for energy sector SCADA
systems.

### NERC CIP

*Critical Infrastructure Protection standards*

Mandatory reliability standards for the North American electric grid, published by the North American Electric
Reliability Corporation. Legally enforceable for bulk power system owners and operators in North America.
Covers cybersecurity, physical security, personnel, and supply chain for critical assets. Not an ISO or IEC
standard; compliance is enforced by regional entities under FERC oversight.

### NIST SP 800-82

*Guide to Operational Technology Security*

Published by the US National Institute of Standards and Technology. Freely available. Covers threats,
vulnerabilities, and recommended controls for OT environments including SCADA, DCS, and PLCs. Widely referenced
outside North America as practical ICS security guidance even where it carries no legal weight. Appendices
include ICS-specific security controls and a mapping to NIST SP 800-53.

## Access and cost

IEC standards, like ISO standards, are not freely available in full. They are purchasable through IEC
([webstore.iec.ch](https://webstore.iec.ch)) or through national standards bodies. NIST SP 800-82 is freely
available at [csrc.nist.gov](https://csrc.nist.gov). NERC CIP standards are freely available at
[nerc.com](https://www.nerc.com/pa/Stand/Pages/CIPStandards.aspx).

## Related

* [IEC 62443 Factory floor under inspection](../iec62443/assets.md)
* [IEC 62443 Threats to the factory](../iec62443/threats.md)
* [IEC 62443 The factory's defensive mechanisms](../iec62443/controls.md)
* [ISO/IEC information security standards](standards.md)
* [Scope definition](scope-definition.md)
