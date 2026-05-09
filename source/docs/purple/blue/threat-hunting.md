# Threat hunting

Threat hunting is the proactive search for threats that evade automated detection. Hunters operate on the assumption that adversaries are already present and look for evidence rather than waiting for an alert.

## Hunting approaches

Hypothesis-driven hunting forms a specific hypothesis about how an attacker might operate in the environment, then searches for evidence of that behaviour. "If attackers compromised a developer workstation, they would access production databases" is a hypothesis; the hunt is the search for evidence of that pattern.

Intelligence-driven hunting uses threat intelligence about specific adversaries or campaigns. "APT29 uses WMI for persistence" leads to a hunt for unusual WMI subscriptions that match the technique.

Anomaly-driven hunting identifies unusual patterns in baseline telemetry. A service account that normally accesses three servers but today touched fifty is the kind of anomaly worth investigating.

Tool-and-technique-driven hunting searches for specific attack tools or techniques. A hunt for Mimikatz artefacts or credential-dumping activity falls into this category.

## Hunting process

A hunt typically follows six steps.

Hypothesis formation. Based on threat intelligence, past incidents, or understanding of attacker TTPs, the hunter forms a specific hypothesis about what is being looked for.

Data collection. Relevant logs, telemetry, and data sources are gathered to test the hypothesis. Some hunts require enabling additional logging before they can run.

Analysis. The data is searched for indicators that support or refute the hypothesis. Queries, visualisations, and statistical analysis are the usual tools.

Investigation. When something looks suspicious, the hunter digs deeper. The question is whether the activity is malicious, benign, or a misconfiguration.

Response. If a threat is confirmed, the hunt escalates to incident response. If not, the findings are documented and the hypothesis refined for next time.

Documentation. Hunts, findings, and any new detection rules are recorded. The accumulating record is what turns hunting from event to capability.

## Hunt targets

Credential abuse: unusual authentication patterns, lateral movement with a single account, service accounts used interactively.

Persistence mechanisms: unusual scheduled tasks, WMI event subscriptions, registry run keys, services, startup folders.

Command and control: beaconing behaviour, unusual DNS queries, connections to suspicious IPs, encrypted tunnels.

Data staging: large file transfers, unusual compression activity, access to sensitive data by unexpected accounts.

Privilege escalation: unexpected elevation events, exploitation of vulnerable services, abuse of sudo or other privilege escalation tools.

## Related

- [The blue team mission](mission.md)
- [Detection, response, and recovery](detect-recover.md)
- [Working with purple team for improvement](purple.md)
- [SOC detection](../../incident-response/soc/detection.md)
