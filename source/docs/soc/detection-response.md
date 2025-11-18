# SOC detection and response

Detection without coordinated response is useless. A SOC’s main goal is to identify threats quickly and pass them to the right people for action, while maintaining situational awareness across the organisation.

## Key actions

* Monitor intelligently: Use a combination of monitoring tools such as SIEM, EDR, and network analysis to detect unusual or risky activity. Focus on actionable alerts, not noise.
* Triage alerts: Assign risk levels to alerts based on potential impact and urgency. Avoid overwhelming analysts with low-value signals.
* Escalate promptly: Critical alerts are immediately routed to the SIRT or responsible business units. Define clear criteria for escalation.
* Coordinate with SIRT: Communication channels, responsibilities, and protocols between SOC and SIRT must be well understood. Regular joint exercises help maintain smooth handoffs.

## Tips

* Map alert categories to pre-defined response workflows before an incident occurs.
* Automate simple, repetitive tasks (e.g., log aggregation, initial checks) to free analysts for high-value decisions.
* Regularly review detection rules to adapt to evolving threats.

## Example scenario

If a phishing email is detected targeting finance staff, SOC analysts triage the alert, escalate to SIRT for 
investigation, and initiate containment procedures while recording all actions for post-incident learning.
