# Measuring effectiveness

The metrics in [measurements](measurements.md) describe what to look for. This page goes into the specific calculations and what they reveal, with the caveat from the other page firmly in mind: every metric is a hypothesis about capability, and the interesting question is not whether the number improved but what its movement reveals about the model that produced it.

## Detection coverage

Coverage is calculated as the percentage of relevant techniques that produce an alert when tested. The arithmetic is simple: techniques with working detections divided by techniques tested, multiplied by 100.

The trap is in the denominator. Coverage of techniques tested can rise to 100% while coverage of techniques actually used by adversaries remains low, because the tested set was drawn from what the team can already detect rather than from current threat intelligence. Breaking coverage down by ATT&CK tactic, reconnaissance, initial access, execution, and the rest, prevents the single number from hiding the structure underneath it.

## Response time

Three time-based metrics describe different stages of the response.

Mean time to detect (MTTD) measures the gap between attack action and alert generation. It is sensitive to logging latency, correlation interval, and how busy the analyst queue happened to be when the alert appeared.

Mean time to respond (MTTR) measures the gap between detection and containment. It depends on triage time, escalation paths, and whether the analyst has the authority to act on what they have found, or has to wait for someone who does.

Mean time to recover (sometimes labelled MTTR2) measures the gap from containment to operational recovery, which is often longer than the response phase itself and is where the cost of skipped backup-and-restore testing becomes visible.

All three fall as the programme matures. A flat or rising trend on any of them, despite increasing investment, is information about a constraint other than capability.

## Adversary simulation

Three metrics describe what the red team produced relative to what the blue team caught.

Objective achievement rate is the percentage of red team objectives reached despite blue team detection and response. A falling rate over time suggests the defences are improving relative to the techniques being used.

Attack path diversity counts the number of distinct techniques required to achieve objectives. Rising diversity means the defences are forcing simulators into more creative paths.

Detection rate per objective measures how many steps of an attack path were detected. A rising rate indicates that even when objectives are achieved, the path is increasingly visible.

Each of these is informative only in the context of the others. A rising objective achievement rate can mean the defences are weakening; it can also mean the exercises are getting closer to realistic threat models.

## Maturity indicators

Some metrics describe the shape of the programme rather than its outputs.

Detection sophistication: progression from signature-based detection to behaviour-based detection, with the latter being more resilient to technique variation.

Response automation: percentage of response actions that run without manual intervention. Higher automation reduces MTTR but increases the risk of automated wrong answers; the trade-off is worth tracking explicitly.

Proactive ratio: time spent on threat hunting versus time spent on incident response. A balance toward hunting suggests the programme is reaching forward rather than reacting backward.

Coverage completeness: percentage of relevant ATT&CK framework covered. The denominator does the work here, as in coverage testing more broadly: completeness against the relevant set is informative; completeness against the entire framework is a number that does not earn its place.

## Reporting to stakeholders

Different audiences need different framings of the same data.

An executive dashboard works best when limited to a few headline metrics with trend lines, and an explicit risk-reduction narrative that connects activity to the things the executive is held accountable for.

A technical report covers the detailed findings, the gaps that remain, and the specific improvements implemented since the last report. The audience here is people who can act on the detail.

A board-level summary translates the same data into business-risk language: which exposure has been reduced, which remains, what investment effectiveness has looked like, and how the maturity progression compares to peer organisations.

## Related

- [Measurements and early success](measurements.md)
- [Coordination models](../coordination.md)
- [SOC maturity](../../incident-response/soc/maturity.md)
- [Risk register](../../risk-management/risk-register.md)
