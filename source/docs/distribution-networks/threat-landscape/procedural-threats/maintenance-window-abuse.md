# Maintenance window abuse

Maintenance-window abuse trades on the window's own legitimacy: running unauthorised work during a scheduled period, folding undocumented changes into authorised ones, or exploiting the reduced oversight the window provides.

Maintenance windows follow a published schedule, are announced to customers and operators in advance, and follow
documented procedures. During maintenance, work is authorised through work plans and switching plans that define what
will be done. Abuse of a maintenance window means either unauthorised work executed during it, or authorised work that
includes hidden unauthorised changes.

The distinction between legitimate and unauthorised work depends on the work plan, the switching plan, the record of
what was actually done, and whether the results match the authorisation.

## Unauthorised work during scheduled maintenance

Maintenance windows are announced well in advance and are coordinated through the Bedrijfsvoering
application. A werkplan (work plan) defines what work will be done, a bedieningsplan (switching plan) defines what
switching operations are required to isolate the work area safely, and a work order in IBM Maximo tracks the maintenance
activity and its completion. What windows are legitimate follows [the maintenance announcement rhythms, procurement schedules, and the
change cadence that gates work](../../operating-context/operations-and-cadence/operational-procedures-and-change.md).

A maintenance window creates a window of legitimacy: the network is expected to be in an altered state, equipment
is expected to be de-energised or energised in ways that would otherwise be unusual, and personnel are expected to be on
site in the maintenance area. An attacker with access to this window could execute unauthorised work alongside or
instead of the authorised work.

For instance, a scheduled maintenance activity might require opening a switchpoint to isolate a section of
network for equipment maintenance. During this window, the attacker could additionally reprogram an RTU in the same
substation, steal components, or plant monitoring equipment. The unauthorised work would occur within the scope of
the maintenance window, and the attacker could rely on the reduced oversight during maintenance to avoid detection.

An insider (a contractor or employee) with access to the maintenance window is particularly dangerous, because
they understand the work procedures and can blend in with legitimate maintenance activities. They can claim to be
part of the maintenance team, access equipment and systems during the window, and perform unauthorised actions.
Contractors make up part of the workforce and perform much of the field maintenance, working
under [how contractors are vetted and authorised](../../operating-context/operations-and-cadence/contractor-management.md)
within a [workforce structure whose thinness affects oversight](../../operating-context/staffing-and-capability/staffing-realities.md). An
external attacker would need to either impersonate maintenance personnel (which requires knowledge of the
procedures and access to the site) or coordinate with an inside accomplice.

The werkplan and bedieningsplan are documented in advance, so an attacker can study them before the maintenance
window to understand what will be happening and where attention will be focused. This allows pre-planning of the
unauthorised work.

    MAINTENANCE WINDOW TIMELINE: Opportunity for Unauthorised Work
    ──────────────────────────────────────────────────────────────

    ADVANCE PLANNING PHASE (days before)
    ────────────────────────────────────

    T-7 days: Werkplan published
      • The operator publishes maintenance schedule to customer portal
      • Attacker (insider or external with access) studies it
      • Identifies target: "Switchpoint replacement at Substation X, 15:00-16:30"

    T-3 days: Bedieningsplan finalised
      • Switching plan details: "Open switch Y to isolate zone"
      • Attacker plans: "During this 90-minute window, reprogram RTU in same zone"
      • RTU reprogramming takes about 20 minutes (firmware upload plus I/O remap); work plan covers full 90 minutes
      • Overhead: 70 minutes of documented work + 20 minutes unauthorised

    T-1 day: Contractor assigned, access granted
      • Contractor credentials activated in e-terracontrol
      • Physical site access badge enabled
      • Engineering workstation access provisioned


    MAINTENANCE WINDOW EXECUTION (day of work)
    ────────────────────────────────────────────

    14:30  | Work team arrives, site security check
           | Legitimate activity: setup, verify de-energisation
           │
    14:50  | Authorised switching begins
           | Contractor opens switch Y per bedieningsplan (documented)
           │
    14:55  | Supervision focus: switchpoint replacement (main task)
           | ← Window of opportunity: attacker has legitimate reason to access RTU
           │  RTU in same zone needs to be verified de-energised
           │
    15:00  | UNAUTHORISED WORK STARTS (hidden in scope)
           | • Attacker connects to RTU with e-terracontrol engineering tool
           | • Loads and modifies RTU firmware
           | • Adds dormant trigger code (dead man's switch)
           | • Firmware upload: takes 15 minutes
           │
    15:15  | Authorised work continues (switchpoint replacement)
           | • Main task progresses on schedule
           | • Site supervisor checks on progress
           | • RTU firmware modification complete and unobserved
           │
    15:25  | HIDDEN MALICIOUS CONFIGURATION (additional unauthorised work)
           | • Attacker modifies RTU I/O mapping
           | • Changes "Output 1 = close Switchpoint A" → "Output 1 = open Switchpoint B"
           | • Modification time: 5 minutes (hidden in switchpoint replacement activity)
           │
    15:35  | Switch Y re-closed per bedieningsplan (closing the maintenance window)
           | • Site returns to normal operational state
           | • Authorised work documented and signed off
           │
    16:30  | Team departs, site secured
           | • Unauthorised firmware modification: undetected
           | • Unauthorised I/O mapping: will only manifest when triggered
           | • Work order completion shows: "Switchpoint replaced, RTU verified"
           | • No record that RTU settings were accessed


    EVIDENCE TRAIL (what might reveal the abuse)
    ─────────────────────────────────────────────

    If an investigation follows unexpected RTU behaviour:

    Timestamp mismatch:
      • Work plan: switchpoint replacement 15:00-16:30
      • RTU event log: firmware loaded 15:03-15:18 (outside main task window)
      • Question: why was RTU firmware touched during switchpoint replacement?

    Access audit:
      • Engineering workstation log: contractor accessed e-terracontrol 15:03-15:25
      • e-terracontrol connection log: firmware upload detected
      • Contractor's claim: "only verified de-energised state"
      • But logs show: firmware read, modify, write operations

    Baseline divergence:
      • Before: RTU firmware version v2.1.0, I/O mapping documented
      • After: RTU reports v2.1.0 (attacker preserved version string)
      • But: online-vs-offline comparison flags divergence (attacker failed to update baseline)
      • Or: comparison passes because attacker corrupted baseline too

    Device behaviour:
      • Unexpected RTU state reports (false values)
      • Commands execute on wrong switchpoints
      • Autonomous actions trigger (frequency drops to 48.5 Hz, RTU opens unscheduled load)

## Hidden changes in authorised work

Authorised maintenance often requires configuration changes: updating SIPROTEC or SEL relay settings,
modifying e-terracontrol SCADA configuration, or changing Smallworld network model entries. An attacker who is part of
the maintenance team could include unauthorised changes in the authorised work.

For instance, a maintenance activity might authorise changing a relay's time delay from 100 milliseconds to
150 milliseconds. The work plan documents this change. During the maintenance, an insider could make that change, but
could also change the relay's threshold from 1200A to 1600A. The threshold change is unauthorised and is not documented,
but if the relay settings comparison is done after the maintenance without detailed record-keeping of what changed,
the two changes (the authorised and the unauthorised) might go unnoticed together.

More subtly, an insider might document the authorised change correctly but make a different change than documented. The
work plan says "change threshold to 1200A" but the insider actually changes it to 1600A. The maintenance paperwork
shows the correct change was made (the insider signs the work-order completion in Maximo), but the actual relay has the
wrong setting.

This requires the attacker to have technical knowledge of the system and access to the engineering tools (DIGSI 5
for SIPROTEC, AcSELerator QuickSet for SEL, or similar). Contractors who perform protection relay maintenance
have this knowledge and access, making them a particular risk.

## Unauthorised network access during maintenance

Maintenance windows often require granting temporary access to systems that are normally restricted. A
contractor might need access to an engineering workstation to load relay settings, or might need physical access
to a substation to replace equipment. An attacker could use a maintenance window as justification for accessing a
system, then use that access to plant malicious software or gather information.

For instance, a contractor might request access to an engineering workstation during a maintenance window to
update SIPROTEC or SEL relay firmware. The operator grants access, expecting the contractor to update one relay.
The contractor could use this access to install malware on the workstation, to compromise the settings database, or
to steal a copy of the network model from Smallworld.

Alternatively, a contractor with physical access to a substation could plant test equipment (a device that monitors
network traffic, logs relay commands, or injects false frames). The test equipment would be left in the substation after
the maintenance window ends, providing persistent access to the network even after the maintenance window closes.

Detecting unauthorised access during maintenance depends on monitoring what the contractor actually does during the
window and comparing it against what the work plan authorised. This requires on-site supervision, auditing of
system access logs, and physical inspection of equipment after maintenance.

## Observable traces

Maintenance-window abuse shows up as work orders that don't match the actual changes made, switching plans that differ
from the executed switching, configuration changes outside the maintenance scope, and unauthorised equipment or malware
left behind. The last is caught only by physical inspection and endpoint tooling after the window, since it sits in no
work record. The rest are documentary: the work plan, the
[as-found-and-as-left records](../../observable-semantics/engineering-and-change/maintenance-window-signatures.md), the
switching log, the time records and the access log, read against what was authorised, part a falsified record from an
honest one, down to the pattern of small unexplained overruns across several windows that reads as systematic abuse.

*Last updated: 13 July 2026*
