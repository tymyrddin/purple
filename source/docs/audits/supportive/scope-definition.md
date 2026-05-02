# Scope definition

Before any audit, assessment, or compliance programme proceeds, the boundary question needs an answer: what
exactly is in scope? The boundary determines what is assessed, which controls apply, what evidence is required,
and what the certification or compliance statement actually covers.

Scope definition is simultaneously a technical decision, an organisational decision, and a strategic one.
A narrow scope is defensible if the rationale is honest. A broad scope is achievable if the organisation has the
capacity to sustain it. A scope that excludes the inconvenient parts while claiming to cover everything tends
not to survive the first serious question from an auditor.

## What the frameworks expect

### ISO 27001

Clause 4.3 requires the organisation to determine the boundaries and applicability of the ISMS. The inputs are
the internal and external issues identified under Clause 4.1 and the requirements of interested parties under
Clause 4.2. In practice this means the scope follows from a deliberate analysis of context, not a default to
"the whole organisation" without examination.

Exclusions from scope are permitted, but require justification. An exclusion is only valid where the excluded
element does not affect the organisation's ability to achieve the intended outcomes of the ISMS or fulfil its
obligations. Excluding a legacy system because bringing it into compliance would be difficult is not a valid
exclusion if that system processes or stores information assets the ISMS is designed to protect.

The Statement of Applicability documents which Annex A controls apply, with justification for inclusions and
exclusions. Controls can be excluded only where the scope definition and risk assessment jointly support the
exclusion; not all of the 93 controls in the 2022 version will apply to every ISMS, but the reasoning needs
to be on record.

### NIS2

For NIS2, scope is largely determined by law: which sector the entity operates in and whether it meets the
size thresholds for essential or important entity classification. The organisation does not choose whether it
is in scope.

Within that legal scope, the entity still needs to define which systems, services, and processes the Article
21 measures apply to. Where an entity delivers multiple services, only some of which fall under NIS2, the
practical question is: which services are essential or important within the meaning of the Directive, and which
systems are necessary for delivering those services?

### IEC 62443

In OT environments, scope definition uses the zone-and-conduit model. Assets are grouped into security zones
based on similar security requirements and similar levels of trust. A conduit is the path through which
communication between zones passes, and it is treated as a boundary that requires explicit security control.

Defining zones requires identifying the assets in the environment, understanding how they communicate, and
grouping them in a way that reflects the risk profile and the operational requirements for connectivity. The
security level target for each zone drives which controls apply to that zone; a zone with a higher target has
stricter requirements than one with a lower target.

The zone-and-conduit model is covered in more detail in the [OT standards reference](ot-standards.md).

### ISO 22301

For business continuity, scope covers the products and services the organisation commits to maintaining and
the activities, resources, and dependencies that support them. The scope determines which processes are subject
to business impact analysis and which recovery time objectives apply.

The ISO 22301 scope often differs from the ISMS scope. Not all IT systems in the ISMS scope will be
necessary to sustain the in-scope products and services, and some that are critical to continuity may have
been excluded from the ISMS scope for other reasons.

## The boundary as an interface

A scope boundary is not a wall. It is an interface. Everything that crosses it, including data flows, network
connections, accounts, and physical access, needs to be accounted for, because the interface is where the
scope statement is tested.

A system excluded from scope that holds credentials for in-scope systems effectively collapses the boundary.
A cloud service excluded from scope that processes in-scope data creates an unaccounted-for data flow. The
exclusion may be legitimate for practical reasons; the question is whether the interface is controlled and
whether the risk it introduces is addressed somewhere in the risk treatment plan.

Working through the scope from the operational environment outward tends to produce more honest boundaries than
working from the organisational chart inward. Starting with the critical assets, identifying which systems hold
or process them, then which systems those depend on, and which external parties have access tends to surface
the real boundary rather than the convenient one.

## Documenting the scope

The scope statement needs to be specific enough to be testable. "All information systems of the organisation"
is not specific: it does not identify which locations, which legal entities, which services, or which systems
are covered. The scope statement is specific enough when an auditor can determine, for any given system or
process, whether it is in scope or not.

A useful scope statement includes:

* The products, services, or operational areas covered
* The locations, physical and logical, that are covered
* Any explicit exclusions and their justification
* The interfaces at the boundary and how they are controlled

Exclusion justifications that reference operational convenience rather than a reasoned risk rationale are a
finding waiting to happen.

## Maintaining the scope

A scope that was accurate when defined may not be accurate six months later. New systems, new services,
acquisitions, outsourcing arrangements, and changes in what third parties can access all affect the boundary
without necessarily triggering a formal review.

Common triggers for revisiting scope:

* Significant changes to the organisation's products, services, or structure
* New systems or platforms that process in-scope data
* Changes in third-party access arrangements or cloud service use
* Incidents that reveal assets or data flows not captured in the documented scope
* Preparation for a surveillance audit, recertification, or supervisory review

## Related

* [ISO/IEC standards reference](standards.md)
* [OT standards reference](ot-standards.md)
* [EU regulations](eu-regulations.md)
* [Supply chain and third-party risk](supply-chain.md)
* [Gap analysis](gap-analysis.md)
