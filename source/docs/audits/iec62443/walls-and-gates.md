# Walls and gates

Zones, conduits, and security level targets.

A fortress is not one wall. It is an arrangement of courtyards, inner keeps, and gates that decide what passes
between them. IEC 62443-3-2 formalises this as zones and conduits: the system under consideration is partitioned
into zones grouping assets with common security requirements, connected by conduits, the communication channels
between them. Risk is then assessed per zone, and each zone is assigned a security level target reflecting the
adversary it needs to resist.

## Partitioning into zones and conduits

Grouping follows function and exposure, not the org chart: safety systems separated from basic control, control
separated from supervision, the industrial DMZ between OT and enterprise IT. Every path between zones is a
conduit, and a conduit that exists in the network but not in the model is a gate nobody is watching.

* Checks: Does every asset in the register belong to exactly one zone? Is every inter-zone communication path documented as a conduit with a stated purpose? Do safety-related assets sit in their own zones?
* Typical gaps: Dual-homed devices bridging zones informally, vendor remote access arriving outside any documented conduit, historians and jump hosts accumulating connections from everywhere.

## Assigning security level targets

The standard's security levels grade zones by the adversary they are meant to resist, from protection against
casual or coincidental misuse at the low end, through intentional attackers using simple means, up to
sophisticated attackers with extended resources and ICS-specific skills. Assigning a target level to a zone is a
statement about the besiegers: it names which class of attacker this part of the fortress is designed to keep
out, and implies what the controls in [locks and patrols](locks-and-patrols.md) have to achieve.

A target level set uniformly high across all zones usually signals that the exercise was skipped, not that
the estate is a citadel: uniform targets ignore the risk assessment they are meant to follow, and commit the
organisation to controls it is unlikely to sustain everywhere.

## Segmentation as deployed

Zone models live or die by whether the deployed network matches them. Network segmentation and boundary controls
(VLANs, firewalls, industrial DMZs) are the physical expression of the model.

* Gap check: Confirm that critical devices reside in the correct zones, and that firewall and segmentation rules match network diagrams. Any misaligned devices or undocumented rules are findings.

Segmentation encodes an assumption: that traffic follows the paths shown in the diagram. Whether it actually does,
against an attacker rather than an auditor, is a question for [testing the defences](testing-the-defences.md).

## Practical gap-spotting

* Model completeness: every asset zoned, every inter-zone path a documented conduit.
* Target coherence: security level targets trace back to the per-zone risk assessment, not to a default.
* Diagram fidelity: firewall rules, VLAN assignments, and the zone model tell the same story.
* Change traceability: when a device moves or a rule changes, the zone model follows, and someone signs for it.

## Output

By the end of this stage, the organisation has a zone and conduit model covering the whole system under
consideration, a security level target per zone traceable to its risk assessment, and segmentation rules
reconciled with the diagrams. The control layer is built against these targets.

## Related

* [NIS2 Building a raft](../../audits/nis2/raft.md)
* [Gap analysis](../supportive/gap-analysis.md)
* [Unseen University Power & Light Co. IT/OCS pentest](https://red.tymyrddin.dev/docs/power/)
