# Documentation and evidence collection

Red team operations require meticulous documentation. Blue team needs complete visibility into what happened to build better defences.

## What to document

Every action: Commands executed, tools used, files created or modified, network connections made, credentials obtained, 
systems accessed.

Timestamps: Precise timing helps blue team correlate with their logs and alerts. 
"13:42:15 GMT: Executed Mimikatz on WORKSTATION-042"

Success and failure: What worked, what was detected, what was blocked. Failures reveal effective controls. Successes reveal gaps.

Artefacts created: Payloads, scripts, modified files, registry keys, scheduled tasks. Blue team needs these for detection engineering.

Screenshots and videos: Visual evidence helps during debriefs. Show exactly what red team saw and did.

## Documentation formats

Real-time logging: Maintain operational notes during engagement. Use structured formats (JSON, CSV) for later analysis.

Attack timeline: Chronological sequence of events from initial access through objectives achieved.

TTP mapping: Match activities to MITRE ATT&CK framework for standardised reporting.

Evidence package: Collect all artefacts, logs, screenshots, and malware samples used during exercise.

Executive summary: High-level findings for leadership. Focus on business impact and risk, not technical minutiae.

Technical report: Detailed walkthrough for blue team and security practitioners. Include detection opportunities, defensive gaps, remediation recommendations.
