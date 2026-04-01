# SOC maturity

Maturity in a SOC context is most usefully understood as a direction rather than a level. The question is not "what level are we at?" but "in which direction are we moving, and what is currently limiting our movement in that direction?"

This matters because maturity level frameworks tend to produce compliance with the description of a level rather than the underlying capability. An organisation can credibly claim to be at a given level while its actual detection and response capability is weaker than a lower-rated organisation that takes its model seriously and updates it continuously.

## What movement in the right direction looks like

More accurate detection: the detection model more closely matches the actual threat environment, with fewer rules that fire on irrelevant activity and fewer gaps that adversaries can operate in undetected. Movement here requires active maintenance of detection logic, feedback from SIRT investigations, and [purple team exercises](../../purple/index.rst) that test coverage honestly.

More consistent process: analysts make similar decisions in similar situations, and those decisions are traceable to documented criteria. Inconsistency is a sign that the process is implicit and person-dependent rather than explicit and transferable. Movement here requires documenting the criteria that currently live in experienced analysts' heads.

Faster feedback loops: the gap between an incident and the process update that results from it is shorter. Longer gaps mean more exposure to the same pattern of event before the response improves. Movement here requires a review process that is lightweight enough to happen promptly.

Better learning integration: findings from the SOC inform the broader security posture, and findings from other security activities feed back into SOC detection and process. Purple team exercises, risk assessments, and audit findings all contain information relevant to the SOC model.

## What limits movement

Analyst attrition: experienced analysts carry significant implicit knowledge about the environment, about what is normal, and about how to apply the documented criteria in situations the documentation does not fully cover. When they leave, that knowledge needs to be made explicit or it is lost. SOCs with high turnover often have detection and triage capability that looks intact on paper but degrades in practice.

Alert volume: a SOC that is handling more alerts than its analysts can meaningfully process is not monitoring. It is reacting to a random sample of alerts, which is worse than having a smaller, more carefully maintained set of detection rules. Managing alert volume, including suppressing rules that generate noise without signal, is maintenance work that takes time but directly improves the quality of what analysts can do.

The no-blame condition: the same [Satir](../../foundations/organisational-development/satir-core.md) dynamic that applies in SIRT [post-incident](../../making-of/sirt/learning.md) review applies in SOC learning. Analysts who expect blame for missed detections will underreport near-misses and borderline calls. Underreporting means the organisation does not learn from its near-misses, which means the same gaps persist. A SOC that has become politically safe to be honest in will surface more of what it needs to improve.

## Related

- [Why a SOC exists](purpose.md)
- [Detection and response](detection.md)
- [Applying SEM to security](../../foundations/system-effectiveness/applying-sem.md)
- [Purple team coordination](../purple-team/coordination.md)
- [Resilience and system effectiveness](../../audits/resilience/stress-testing.md)
