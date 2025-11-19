# Threat hunting

Proactive search for threats that evade automated detection. Hunters assume adversaries are already present and look for evidence.

## Hunting approaches

Hypothesis-driven: Form specific hypothesis about how an attacker might operate in your environment. "If attackers compromised a developer workstation, they would access production databases." Search for evidence of that behaviour.

Intelligence-driven: Use threat intelligence about specific adversaries or campaigns. "APT29 uses WMI for persistence. Let's search for unusual WMI subscriptions."

Anomaly-driven: Identify unusual patterns in baseline telemetry. "This service account normally only accesses three servers, but today it touched 50. Investigate."

Tool and technique-driven: Search for specific attack tools or techniques. "Let's hunt for all instances of Mimikatz artifacts or credential dumping activity."

## Hunting process

1. Hypothesis formation: Based on threat intel, past incidents, or understanding of attacker TTPs, form a specific hypothesis about what you're hunting for.

2. Data collection: Gather relevant logs, telemetry, and data sources needed to test hypothesis. May require enabling additional logging.

3. Analysis: Search data for indicators supporting or refuting hypothesis. Use queries, visualisations, statistical analysis.

4. Investigation: When something looks suspicious, dig deeper. Is it malicious, benign, or misconfiguration?

5. Response: If threat is confirmed, escalate to incident response. If not, document findings and refine hypothesis.

6. Documentation: Record hunts, findings, and new detection rules created. Build organisational knowledge.

## What to hunt for

Credential abuse: Unusual authentication patterns, lateral movement with single account, service accounts used interactively.

Persistence mechanisms: Unusual scheduled tasks, WMI event subscriptions, registry run keys, services, startup folders.

Command and control: Beaconing behaviour, unusual DNS queries, connections to suspicious IPs, encrypted tunnels.

Data staging: Large file transfers, unusual compression activity, access to sensitive data by unexpected accounts.

Privilege escalation: Unexpected elevation events, exploitation of vulnerable services, abuse of sudo or privilege escalation tools.
