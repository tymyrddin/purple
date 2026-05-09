# Documentation and evidence collection

Red team operations require meticulous documentation. The blue team needs complete visibility into what happened so that detections, playbooks, and defensive improvements can be built from the engagement.

## Items to record

Every action: every command executed, every tool used, every file created or modified, every network connection made, every credential obtained, every system accessed. Skipping any of these because they seemed routine at the time is the most common cause of detail missing during the post-exercise reflection.

Timestamps with sufficient precision to correlate against blue team logs. "13:42:15 GMT: Executed Mimikatz on WORKSTATION-042" is the right level of specificity. "Around 14:00, ran credential dumping" is not.

Both successes and failures. What worked, what was detected, what was blocked. Failures reveal effective controls and are at least as informative as successes, which the documentation pattern sometimes underweights because the team is focused on what it achieved.

Artefacts created during the engagement: payloads, scripts, modified files, registry keys, scheduled tasks. The blue team needs these to build detection engineering against the actual indicators rather than against generic patterns.

Visual evidence. Screenshots and screen recordings show the blue team exactly what the red team saw and did, which is harder to misinterpret than a textual description after the fact.

## Documentation formats

Real-time logging during the engagement, in a structured format such as JSON or CSV that supports later analysis. The structure pays for itself when the post-exercise reflection needs to filter or correlate events from a large engagement.

A chronological attack timeline from initial access through to objectives achieved, ordered by timestamp and annotated with techniques used at each step.

TTP mapping that links each documented activity to the relevant entry in the MITRE ATT&CK framework. The mapping is what makes the documentation portable across organisations and useful for benchmarking.

An evidence package collects all artefacts, logs, screenshots, and malware samples used during the exercise into a single deliverable. The package is the audit trail and the input to detection engineering.

An executive summary translates the technical findings into business-impact and risk language. The audience is leadership; the purpose is decision-making, not technical detail.

A technical report covers the detailed walkthrough for the blue team and security practitioners: detection opportunities, defensive gaps, remediation recommendations, with specific enough detail that the engineering work can begin from the report rather than from a follow-up conversation.

## Related

- [Coordinating with purple team](coordination.md)
- [Knowledge transfer: playbooks](../../knowledge-transfer/playbooks.md)
- [Knowledge transfer: manuals](../../knowledge-transfer/manuals.md)
- [Incident response choreography](../../incident-response/choreography.md)
