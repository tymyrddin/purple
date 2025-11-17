# Navigating hazards

![Hazards](/_static/images/hazards.png)

The river has hazards. Incidents will happen, and the question is whether you navigate them safely or capsize. Unlike ISO 27001, where incident reporting is internal, NIS2 has strict mandatory timelines for notifying authorities. Your ability to detect, respond, and report determines compliance.

## What triggers mandatory reporting

Not every security event requires notifying regulators. First focus on incidents that cause or could cause:

* Severe operational disruption of critical services
* Significant financial losses
* Material reputational damage
* Data breaches affecting many individuals
* Compromise of network and information systems

Next, sector considerations are important. What is significant for a hospital differs from what is significant for a 
logistics company. Organisations should coordinate with their supervisory authority and sector CSIRT for guidance 
on thresholds.

## Detection happens before response

Continuous monitoring forms the foundation. Consider implementing:

* Security event logging and analysis across systems
* Intrusion detection to spot unauthorised access attempts
* Anomaly detection to flag unusual behaviour
* User behaviour analytics to identify insider threats or compromised accounts
* Threat intelligence integration to provide context

Incident classification determines the response intensity. Severity levels may range from critical to low, based on potential impact. Assess the effect on confidentiality, integrity, and availability, determine affected systems and data, and evaluate against reporting thresholds to decide if authorities must be notified.

## Response follows procedures, not panic

Immediate actions contain damage. Organisations may:

* Isolate affected systems to prevent spread
* Revoke compromised access credentials
* Preserve evidence such as logs, memory dumps, and network captures
* Assess impact and scope accurately
* Activate the incident response team with clearly defined roles

Investigation establishes what occurred. 
* Do a root cause analysis to determine how the incident happened. 
* Reconstruct timelines. 
* Identify attack vectors used. 
* Determine which assets were compromised. 
* Assess whether data was exposed and how broadly.

Remediation removes threats. 
* Remove malware and unauthorised access. 
* Restore systems from clean, verified backups.
* Apply patches or configuration changes to close vulnerabilities. 
* Reset credentials that may have been compromised.
* Validate system integrity before returning to normal operations.

Recovery restores normal operations.
* Monitor closely for recurrence.
* Document actions taken and the reasons behind them.
* Update procedures and controls based on lessons learned.
* Feed insights back into your risk assessment and control selection.

## Mandatory reporting has deadlines

Within 24 hours of awareness of a significant incident, provide an early warning to your CSIRT or competent authority. Include a basic description, suspected causes, potential impacts, indicators of compromise, and whether the incident appears malicious. Limited information is acceptable at this stage.

Within 72 hours, provide a detailed incident notification. Include updated incident details, severity and impact assessment, technical analysis, response actions taken, and current status. This notification should reflect investigation results, not speculation.

Within one month, submit a comprehensive final report. Include a detailed incident description and timeline, root cause analysis, full impact assessment, completed remediation actions, preventive measures, and lessons learned.

Provide intermediate updates if the situation changes significantly before the next scheduled notification. Timely communication is better than silence. Supervisory authorities prefer updates over discovering withheld information.

## Know your procedures before you need them

Establish clear decision processes. Decide who determines whether an incident meets reporting thresholds, who drafts notifications, who approves them, and the escalation path if normal contacts are unavailable.

Prepare templates in advance for early warning notifications, detailed 72-hour reports, final comprehensive reports, and updates for significant changes. Having templates ready reduces stress during actual incidents.

Maintain current contact lists. Verify and test national CSIRT contact details, understand supervisory authority notification procedures, identify sector-specific CSIRTs, and maintain emergency escalation contacts.

Practice through exercises. Include reporting in tabletop scenarios, test notification procedures, update contact information, and train multiple staff on processes to ensure continuity.

## Communication extends beyond authorities

Internal communication keeps the organisation aligned. The incident response team requires real-time updates. Management and board members need appropriate briefings. Affected business units should understand the impact and recovery timeline. Legal and compliance teams provide guidance.

External communication may also be necessary. Inform customers if their services or data are affected, partners and suppliers needing protective action, data protection authorities if personal data is involved, law enforcement if criminal activity is suspected, and the media if incidents affect public trust.

## Output

The output of this stage is a functional incident response plan, reporting procedures with tested templates, notification templates ready for use, tested communication channels, and an incident log documenting reporting history for compliance evidence.

```{raw} html
<div class="page-post-card__link">
    <a href="https://tymyrddin.dev/contact/">
      Contact us to discuss the hazards ahead and see if our expertise aligns with your needs.
    </a>
</div>
```
