# Procurement documents

![Procurement documents](/_static/images/distribution-procurement-documents.png)

A tender specification has a property none of the other sources do: it is an authoritative, pre-committed list of what
the delivered system will be required to emit, written by the buyer. For a Dutch DSO the richest examples sit in the
European security-procurement requirements the sector uses, and in Stedin's own OT platform tenders.

For a Dutch DSO it is also unusually accessible, because
the sector shares its procurement requirement sets openly and Stedin is inside the body that writes them.

## The sector-shared requirement sets

Stedin is a member of ENCS, the European Network for Cyber Security, the party
that audits its meter suppliers. ENCS publishes [procurement security requirement documents](https://encs.eu/resources/security-requirements/) that read as observable security checklists, several of them public, SA-301 and the distribution-automation set among them, while the risk assessments and architectures behind them stay member-restricted.

The set maps straight onto the stack: SA-301 for procuring substation gateways, SA-302 for procuring IEDs, SA-303 for procuring HMI software, DA-211 for distribution-automation systems, and, tellingly, a [draft SC-311](https://encs.eu/resources/drafts/) for procuring SCADA, EMS and (A)DMS applications, which is the procurement specification for precisely the e-terra control-room layer.

Above ENCS sits the EU-level version now being formalised under the Network Code for Cybersecurity: the EU DSO Entity and ENTSO-E have produced a [Substation Gateway Cybersecurity Profile](https://eudsoentity.eu/wp-content/uploads/2025/10/Annex-I-Gateway-security-profile.pdf) for procurement, organised strictly around IEC 62443.

## Observable checklists built on IEC 62443

These documents read as observable checklists because they are built on the [seven Foundational Requirements of IEC 62443](https://www.isa.org/standards-and-publications/isa-standards/isa-iec-62443-series-of-standards).

User authentication is Foundational Requirement 1, identification and authentication control. Audit logging, change
tracking and time synchronisation fall under Use Control, which specifies auditable events, audit storage capacity,
response to audit-processing failures and timestamps as discrete requirements. Configuration management sits under
System Integrity. Asset inventory appears as the control-system component inventory requirement under Resource
Availability. Alarm management and whether the system noticed and recorded events live under Timely Response to Events.

A tender that adopts these requirement sets mandates the observables line by line: an audit log that exists, is
accessible, has defined storage and failure handling; timestamps from a synchronised source; an enumerable component
inventory; authenticated, manageable accounts.

## The specifications also say how each observable is proven

The part that makes procurement documents stronger than a feature list is that they attach an evaluation activity to
each requirement. The public [ENCS SA-301 gateway document](https://encs.eu/wp-content/uploads/2021/09/Security-requirements-for-procuring-substations-gateways.pdf), for instance, pairs its authentication requirements with concrete checks: a documentation review of the authentication measures, plus functional tests verifying that accounts can be modified, that identifiers can be changed, and that authenticators can be changed.

That converts the requirement from an assertion into a demonstrated observable: the specification does not merely say an
audit log should exist, it defines the test that confirms it exists and works.

A tender is therefore a list of
observables that the vendor had to prove present before acceptance.

## Closing the control-room loop

The draft SC-311 covers procurement of SCADA, EMS and (A)DMS applications, the category Stedin's e-terra suite occupies.

The procurement layer is what required e-terra's
authentication, audit trail, event-and-alarm logging and inventory to be present in the first place, the same features
the e-terracontrol data sheet later advertises as alarm acknowledgement, event and alarm logging, an SQL Server
historian and e-terratrust authentication.

The vendor documentation describes the observables the product emits; the
procurement specification is the buyer-side document that demanded them and defined how they would be verified.
Together, they bracket the same evidence surface from the supply and demand sides.

## Where Stedin's own tenders sit

Stedin's specific tender documents live on TenderNed as EU procurements, and the 2023 distribution-automation write-up
confirmed that its secondary-substation automation platform was specified using a system-engineering methodology and a
requirement-management tool, with an EU tender process, which is exactly where the ENCS distribution-automation and
gateway requirement sets would be incorporated.

The sector requirement documents are the public, reusable core; the
Stedin-specific tender is that core plus its own use cases, and it would be the place a named product, a specific
audit-retention period or a particular time source would be pinned down.

The procurement document sits at the head of the chain: the only source written in advance and in mandatory terms, which is why it functions as the authoritative list of what evidence the system was built to produce.

*Last updated: 11 July 2026*
