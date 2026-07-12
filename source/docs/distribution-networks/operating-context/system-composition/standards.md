# Standards

![Standards](/_static/images/distribution-standards.png)

A standard read semantically rather than as build instructions is the a priori taxonomy of every observable a conformant
system can emit. The product's internal documentation is unnecessary for enumerating the event vocabulary; the standard
already defines it. Since Stedin's stack is standards-based throughout, IEC 60870-5-104 today moving to IEC 61850, IEC
62443 in procurement, a CIM-based model under e-terra, those taxonomies are Stedin's observable vocabulary directly.

## IEC 61850 as an event taxonomy

Mined for semantics, 61850 is close to a complete answer to what events exist in a substation. Its data model decomposes
every function into logical nodes with data objects and attributes, and it defines the reporting machinery explicitly:
buffered and unbuffered report control blocks, log control blocks, datasets, and a fixed set of trigger conditions, data
change, quality change, data update, integrity and general interrogation. That trigger set is itself a taxonomy of why
an event is emitted.

Status changes carry quality attributes (validity, source, test, operator-blocked), so the standard
models not just the event but its trustworthiness.

GOOSE defines the fast peer-to-peer event messages, trips and
interlocks, between devices, and sampled values the measurement stream.

The control model's originator is the detail:
every control action carries an originator category with enumerated values, bay-control, station-control,
remote-control, automatic-bay, automatic-station, automatic-remote, maintenance, process. This is the standard defining,
in advance, a taxonomy of who or what caused an action.

SCL, the configuration language, defines the
model-and-configuration artefacts (the ICD, SCD and CID files), so the standard also specifies the shape of the
configuration-history evidence.

## IEC 62351 as a security-event taxonomy

62351 layers security onto that same model and, read semantically, enumerates the security events. Its role-based access
control part defines the roles and the access decisions, so it specifies the authentication-and-authorisation event
space.

Its network-and-system-management part defines an abstract data model for monitoring the health and security of
the communications, effectively a catalogue of security-relevant conditions, authentication failures, certificate
issues, integrity violations, unexpected traffic, expressed as data objects that can themselves be reported through
61850 mechanisms.

A dedicated part addresses security event logging, and the certificate-management parts define the
lifecycle events around keys and certificates.

So where 61850 answers what operational events exist, 62351 answers what
security events exist, using the same reporting substrate, which is why the two compose rather than compete.

## NERC CIP as an evidence-retention taxonomy, and its European equivalents

CIP is the one to read for retention semantics, with the caveat that it is a North American regime and does not bind a
Dutch DSO. Its value here is that it is unusually explicit about evidence: it enumerates which events are logged (its
system-security-management standard specifies security event logging, successful and failed access, malicious-code
detection), it specifies retention (event logs on the order of ninety days available, compliance evidence retained
across the audit cycle), and its configuration-change standard defines a baseline configuration, operating system,
installed software, logical ports, patches, plus the change-tracking and verification evidence against it, and its
incident standard defines the incident evidence and response records.

As a taxonomy, CIP answers what evidence is
retained and for how long, and what a baseline record contains.

For Stedin the binding equivalents carry the same retention semantics under different names. NIS2, transposed as the
Cyberbeveiligingswet, sets the incident-reporting taxonomy and timeline, the early warning, notification and final
report at twenty-four hours, seventy-two hours and one month.

The ENTSO-E and EU DSO Network
Code on Cybersecurity is building the sector version. IEC 62443's management-system parts and ISO 27001 define the
logging and evidence-retention controls that a Dutch DSO's ISMS actually implements.

So the retention-taxonomy concept
transfers cleanly; only the instrument changes from CIP to NIS2-plus-62443.

## The ones Stedin runs, as taxonomies

Two more are worth naming because they are Stedin's current semantics. IEC 60870-5-104, its present telecontrol
protocol, defines information objects with CP56Time2a time tags and a cause-of-transmission field whose enumerated
values, spontaneous, interrogated, cyclic, background and so on, are a compact taxonomy of why a message was sent, the
pre-61850 version of the same idea.

And COMTRADE is the standardised evidence format for fault
records, so the disturbance capture has a defined schema independent of the relay maker.

Above the model sits CIM, on
which e-terra's source modelling is built, defining the network-and-asset semantics that the inventory and topology
evidence conform to.

## The standard as semantic layer

The standard is the semantic layer beneath all of it. From 61850 alone the operational events and their originator 
categories are listable; from 62351 the security events; from the retention regime what is kept and for how long, 
before ever identifying a single product.

For Stedin,
the observable vocabulary is largely determined by knowing it runs 60870-5-104 moving to 61850, procures against 62443,
and models in CIM, because those standards fix the taxonomy. The product, now known to be e-terra, only decides which
slices of it are switched on.

The standard defines the space of possible observables, but which triggers are enabled, which reports are configured,
what retention is set and whether a given logical node is even instantiated are deployment choices that live in Stedin's
configuration and its member-restricted requirement documents, not in the public standard. The standard tells the full
taxonomy; it does not tell which entries Stedin ticked. That last gap is configuration, and configuration stays private
by design.

*Last updated: 11 July 2026*
