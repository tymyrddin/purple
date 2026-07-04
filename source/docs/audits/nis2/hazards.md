# Navigating hazards

![Hazards](/_static/images/hazards.png)

NIS2, Article 23: detection, response, and mandatory reporting.

The river has hazards. Incidents will happen, and the question is whether they get navigated safely or capsize
the raft. Unlike ISO 27001, where incident reporting is internal, NIS2 has strict mandatory timelines for
notifying authorities. The ability to detect, respond, and report determines compliance.

## Mandatory reporting triggers

Not every security event requires notifying regulators. The first filter is incidents that cause or could
cause severe operational disruption of critical services, significant financial losses, material reputational
damage, data breaches affecting many individuals, or compromise of network and information systems.

Sector context carries weight beyond that. What is significant for a hospital differs from what is significant
for a logistics company, and the supervisory authority and sector CSIRT are the sources for threshold guidance.

## Detection happens before response

Continuous monitoring forms the foundation: security event logging and analysis across systems, intrusion
detection for unauthorised access attempts, anomaly detection for unusual behaviour, user behaviour analytics
for insider threats and compromised accounts, and threat intelligence for context.

Incident classification determines response intensity. Severity levels may range from critical to low based on
potential impact: the effect on confidentiality, integrity, and availability, the systems and data affected,
and whether the reporting thresholds are met.

## Response follows procedures, not panic

Immediate actions contain damage: isolating affected systems, revoking compromised credentials, preserving
evidence (logs, memory dumps, network captures), assessing impact and scope accurately, and activating the
response team with clearly defined roles.

Investigation establishes what occurred: root cause analysis, timeline reconstruction, attack vectors used,
assets compromised, and whether data was exposed and how broadly.

Remediation removes the threat: malware and unauthorised access removed, systems restored from clean and
verified backups, patches or configuration changes closing the vulnerabilities, credentials reset, and system
integrity validated before returning to normal operations.

Recovery restores normal operations: close monitoring for recurrence, documented actions and the reasons
behind them, procedures and controls updated from lessons learned, and insights fed back into the risk
assessment and control selection.

When the same class of incident recurs after a corrective action was verified as complete, the corrective action addressed the surface condition but left an assumption intact. The question worth asking is not why the corrective action failed but what the organisation believed about this control that made the recurrence seem impossible. That belief is what needs to be corrected.

## Mandatory reporting has deadlines

Within 24 hours of awareness of a significant incident, an early warning goes to the CSIRT or competent
authority: a basic description, suspected causes, potential impacts, indicators of compromise, and whether the
incident appears malicious. Limited information is acceptable at this stage.

Within 72 hours, a detailed incident notification follows: updated details, severity and impact assessment,
technical analysis, response actions taken, current status. This notification reflects investigation results,
not speculation.

Within one month, a comprehensive final report: detailed description and timeline, root cause analysis, full
impact assessment, completed remediation, preventive measures, lessons learned.

Intermediate updates fill the gaps when the situation changes significantly. Timely communication beats
silence; supervisory authorities prefer updates over discovering withheld information.

## Knowing the procedures before they are needed

Clear decision processes settle in advance who determines whether an incident meets reporting thresholds, who
drafts notifications, who approves them, and the escalation path if normal contacts are unavailable.

Templates prepared in advance, for the early warning, the 72-hour report, the final report, and significant
updates, reduce stress during actual incidents. Contact lists stay current and tested: national CSIRT details,
supervisory authority procedures, sector-specific CSIRTs, emergency escalation contacts. Exercises keep it all
honest: reporting included in tabletop scenarios, notification procedures tested, several staff trained on the
process so it survives absences.

## Communication extends beyond authorities

Internally, the response team needs real-time updates, management and board appropriate briefings, affected
business units the impact and recovery timeline, and legal and compliance a seat at the table. Externally,
customers whose services or data are affected, partners and suppliers needing protective action, data
protection authorities where personal data is involved, law enforcement where criminal activity is suspected,
and the media where public trust is at stake.

## Output

The output of this stage is a functional incident response plan, reporting procedures with tested templates,
notification templates ready for use, tested communication channels, and an incident log documenting reporting
history for compliance evidence.

## Related

* [ISO 22301 The drill book](../iso22301/drill-book.md)
* [Corrective action](../supportive/corrective-action.md)
* [Incident response](../../incident-response/index.rst)
