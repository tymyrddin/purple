# Who could sneak into the factory?

You have built walls and patrols, but attackers exist. This page is not theory; it is practical: confirming that your 
controls and evidence cover realistic threat actors. Every adversary listed should map to mitigations, documented and 
verifiable.

## Key adversary categories

1. Opportunistic attackers / script kiddies typically exploit trivial weaknesses: default credentials, exposed ports, unpatched devices. Gap check: Verify all devices have strong credentials, patching is current, network access is restricted, and monitoring logs cover unusual activity. Any missing control is a gap.
2. Malicious insiders: Employees, contractors, or operators misusing privileges. Gap check: Ensure separation of duties, clearly assigned responsibilities, and audit logs of privileged actions. Ambiguous access or unmonitored high-risk actions are findings.
3. Targeted, skilled attackers / nation-state campaigns exploit protocol weaknesses, segmentation gaps, or supply chain vulnerabilities. Gap check: Confirm segmentation rules are enforced, critical assets are monitored, incident response is documented, and supply chain controls exist. Any undocumented weak points are gaps.

Each adversary category is also a hypothesis about how an attacker would behave in this environment and what the controls would do in response. Mapping adversaries to controls confirms the documentation is coherent. Testing the controls against realistic adversary techniques confirms the model holds in the deployed environment. An opportunistic attacker exploiting default credentials is a scenario that can be run as a PoC against the actual device configuration. A targeted attacker probing segmentation is a scenario for a controlled penetration test scoped to the relevant zones. A malicious insider misusing privileged access is a scenario for a monitored access review exercise checking whether logs would surface the behaviour. Controls that have only been mapped to adversaries, and never tested against them, are predictions about containment, not evidence of it.

## Practical gap‑spotting approach

* For each adversary, map the threats they could realistically exploit to existing controls. Unmapped threats are critical findings.
* Confirm that logs, monitoring, and incident response procedures would detect or contain attempted exploits. Missing evidence is a gap.
* Validate that ownership is assigned for each control and response. Unclear responsibility is a finding.
* Ensure all zones and network segments are considered. Threats crossing undocumented or unmonitored zones indicate gaps.

## Related 

* [ISO 22301 Potential storms and saboteurs](../iso22301/adversaries.md)
* [Unseen University Power & Light Co. IT/OCS pentest](https://red.tymyrddin.dev/docs/power/)
* [Gap analysis](../supportive/gap-analysis.md)

