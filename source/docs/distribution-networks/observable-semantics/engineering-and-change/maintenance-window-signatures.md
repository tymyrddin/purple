# Maintenance window signatures

Stedin's maintenance windows are planned periods when scheduled work is performed on the distribution network. The
evidence is dense: work orders, werkplannen (work plans), bedieningsplannen (switching plans), as-found-and-as-left
records, key-management logs, and post-work commissioning tests. Normal maintenance and unauthorised work leave
different signatures in this evidence.

## The planned maintenance framework

Stedin's maintenance planning cycle starts with the meldpunt (central dispatch), which receives weekly contractor work
plans and publishes maintenance announcements. Each planned maintenance activity is documented in a work order that
specifies what will be done, who will do it, when (the scheduled maintenance window), where (which substations or
network sections), and what authority is needed (switching authority, access keys, approvals). Before work begins, a
werkplan details the step-by-step process and a bedieningsplan specifies the switching sequence for any de-energisation
or line operation.

The bedieningsplan is the detailed safety and operational plan for switching. It specifies which switches must be opened
in what sequence, how the load will be transferred to alternate feeders, and which sections will be de-energised for the
duration of work. The plan is prepared in advance, reviewed and approved, and then executed step-by-step during the
maintenance window. Stedin's Bedrijfsvoering application (the operations management system) holds the plan, and
operators follow it precisely. Each step is logged: when the switch was operated, who operated it, what the command was,
and whether it succeeded.

The maintenance window has a defined start time and end time. For a planned interruption, the start time is announced to
customers with minimum notice (three days). For framework-contract work (the buurtaanpak contractor teams), weekly
schedules are submitted and approved. The start and end times define a boundary: switching operations outside this
window are not authorised as part of this maintenance activity.

## Work order and scope verification

A complete maintenance audit starts with the work order. It specifies the scope (what will be done), the affected
assets (which substations, which feeders), the technical justification (why this work is necessary), and the
authorisation (which manager approved it and when). A legitimate maintenance activity has a work order number, a scope,
and an approval trail showing the chain of authority.

After maintenance, the work order has completion evidence: a completion certificate (or tekening af), records of
what was actually done, any issues encountered, and sign-off from the Installatieverantwoordelijke (Installation
Responsible Authority) or equivalent. If a work order shows it was approved for 08:00-17:00 and actual work occurred
from 08:00 to 23:00, the scope diverged from the plan and the extension needs justification and approval.

Unauthorised work would appear as activities that lack a work order, or as activities that diverge significantly from
the authorised scope. If the work order authorises access to one specific substation but access logs show a technician
visited five substations, the scope was violated. If the work order is for "inspecting transformer Q12" but switching
operations are performed that affect multiple feeders downstream of Q12, the work scope has been exceeded and
unauthorised operations occurred.

## As-found-and-as-left records

Before and after any maintenance involving protective equipment, Stedin documents the equipment state. As-found records
document what condition the equipment was in when the maintenance crew arrived. As-left records document what condition
it was in when they departed. The records are specific: for a protection relay, the as-found record lists all settings (
threshold values, pickup currents, time delays); the as-left record shows the same settings after maintenance. For any
changed settings, the record documents the old value and new value.

Normal as-found-and-as-left records show: what was found (equipment in expected condition, or a specific defect noted),
what was done (settings changes, equipment replacement, cleaning, calibration), and what was left (equipment in working
condition, all settings restored or changed per the work plan). The records are signed by the technician and often
reviewed and approved by the Werkverantwoordelijke (Work Responsible) or supervisor.

Falsified as-found-and-as-left records are a signature of unauthorised work disguised as legitimate maintenance. If the
as-left record shows all relay settings unchanged, but the relay's actual settings diverge from the as-found settings
documented, someone falsified one of the records (either the as-found, the as-left, or both). If the relay's internal
timestamp records show settings were changed during the maintenance window, but the as-left record shows settings
unchanged, the as-left record was falsified.

Missing or incomplete as-found-and-as-left records are also hard to explain. If a maintenance activity is documented (a work
order was issued and signed off), but no as-found-and-as-left records are filed, the documentation is incomplete and
raises questions about what actually happened.

## Switching plan execution and verification

For maintenance that involves de-energising sections of the network, a bedieningsplan specifies the sequence of switch
operations. The plan is prepared in advance, specifies which switches in which order, and is often drawn as a diagram
with numbered steps. During execution, the operator at the SCADA (the Bedieningsdeskundige) follows the plan step by
step, issuing commands and verifying that each step completes before proceeding to the next.

The SCADA logs show the commands issued and the field-device responses. A normal execution shows commands that match the
bedieningsplan: if the plan says "Step 1: Open switch A", the SCADA log shows a command to open switch A followed by a
report that it opened successfully. Each step matches the plan, and the sequence is followed in order.

Deviations from the plan are red flags. If the bedieningsplan specifies switches are to be opened in order A, B, C, D,
but the SCADA log shows they were opened in order A, C, B, D (out of sequence), the execution diverged from the plan.
The divergence could be due to an operational issue (switch C had to be opened before B to avoid unintended load
shifts), which would be documented in an incident report. An undocumented divergence stands out.

Unauthorised operations during a maintenance window would appear as switching operations that were not in the
bedieningsplan. If the plan authorises switching on feeder 1 only, but the SCADA log shows switches were also operated
on feeder 2, unauthorised work occurred. If the bedieningsplan shows 20 planned switch operations but the SCADA log
shows 50, extra unauthorised operations occurred.

## Configuration changes during maintenance

Maintenance windows sometimes involve configuration changes: updating SCADA settings, modifying relay protection logic,
or changing the network model in the GIS. These changes are all documented in the work order and the werkplan.
After maintenance, the configuration matches what the work order authorised.

Normal configuration changes have approval. The engineer submits a change request, it is reviewed and approved (often by
a second engineer), the change is applied during the maintenance window, and the change is documented
as-found-and-as-left (what the configuration was before, what it is after). For protection relay settings, the as-left
record explicitly lists each setting value.

Unauthorised configuration changes would appear as changes not listed in the work order, or changes that are more
extensive than authorised. If the work order authorises changing the overcurrent threshold on one relay, but as-left
records show thresholds were changed on five relays, unauthorised changes occurred. If the work order authorises no
configuration changes (pure hardware maintenance), but the as-left record shows relay settings were changed,
unauthorised configuration work occurred.

## Testing and commissioning

After maintenance, equipment is tested and commissioned. For protection relays, this includes verifying that settings
are as documented, testing that the relay responds correctly to a simulated fault condition, and verifying that the
relay's communication with the SCADA is functioning. For switching operations, this includes verifying that all
de-energised sections are properly isolated and that load is transferred correctly to alternate feeders.

The testing results are documented. A relay test report (if one is generated) shows what test was performed, what the
expected result was, and what the actual result was. A voltage-verification report documents that de-energised sections
are indeed de-energised (zero voltage measured with a meter). A load-transfer report documents that load has shifted to
the expected alternate feeder.

Incomplete or missing test results are suspicious. If a maintenance activity on a critical relay is completed but no
test results are documented, it is unclear whether the relay is functioning correctly. If test results are documented
but show anomalies (a relay failing a test, or a test result that is unexpected), those anomalies are worth a closer
look before the maintenance is signed off.

## Maintenance window anomalies and patterns

Over time, a baseline for maintenance activity at Stedin becomes apparent. The number of maintenance activities per
month, the typical duration, the affected equipment classes, and the personnel involved all follow patterns. Anomalies
in these patterns are forensic clues.

A sudden spike in unscheduled maintenance (emergency work outside the normal maintenance windows) could indicate a
deterioration in network condition or an attack causing unusual failures. A geographic clustering of maintenance (many
activities concentrated in one area over a short period) could indicate a coordinated upgrade effort or a problem
affecting that area. A change in the personnel performing maintenance (a new contractor or team) introduces new
personnel and new patterns.

Maintenance timing anomalies are also observable. Stedin's maintenance is generally scheduled during daytime working
hours and business days. Maintenance at 03:00 on a weekend is unusual and would carry a justification. If a pattern
emerges of multiple maintenance activities at unusual hours without documented emergency circumstances, that pattern
suggests either an operational crisis (the network is in critical condition requiring emergency work) or unauthorised
activity disguised as maintenance.

*Last updated: 12 July 2026*
