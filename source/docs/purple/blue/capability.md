# Building blue team capability

Defensive maturity develops progressively. A small team without dedicated security staff can build the foundations described below; a larger team builds on top of those foundations rather than starting somewhere different.

## Foundational capabilities

Visibility basics come first: centralised logging from critical systems, authentication logs, network traffic metadata, endpoint activity. What cannot be logged cannot be detected; logging is the precondition for everything that follows.

Core detections come next. Known-bad signatures (malware, exploit attempts), authentication failures and anomalies, privileged account usage. None of these are sophisticated; all of them are the baseline that more advanced detection layers depend on.

Basic response capability covers the rest. A defined incident response team, documented procedures for common scenarios, communication templates, and evidence collection practices. The capability does not need to be elaborate, but it needs to exist before more advanced work makes sense.

## Developing capabilities

Enhanced monitoring adds dimensions the foundational capabilities did not cover. EDR on endpoints, network traffic analysis, cloud activity monitoring, application-level logging. Each is a layer that catches what the others miss.

Improved detection moves from signature-based to correlation-based. Rules that span systems, behavioural analytics, threat intelligence integration, custom detection engineering tailored to the specific environment. The detection model becomes more accurate as it becomes more specific.

Tested response replaces theoretical procedures with exercised ones. Regular incident response exercises, purple team engagements, playbook refinement based on what the exercises surface, cross-team coordination practice. A procedure that has been tested behaves differently from one that has only been documented.

Threat hunting begins. A dedicated capability, hypothesis-driven searches, documented findings, hunts converted into automated detection. Hunting reaches forward in a way that detection alone cannot.

## Advanced capabilities

Continuous validation runs automated purple team testing against the detection model, with continuous tuning and a coverage map updated regularly against MITRE ATT&CK.

Predictive defence uses threat intelligence to drive proactive hardening, models that identify likely attack paths before they are taken, and pre-emptive defensive actions where the evidence supports them.

Autonomous response uses SOAR-driven automatic containment, orchestrated response workflows, and human oversight combined with machine execution speed. The trade-off between speed and the risk of acting on a wrong reading is set deliberately.

Purple team integration becomes continuous rather than periodic. Real-time feedback loops between offensive and defensive teams, shared responsibility for security outcomes, and the practice embedded in the daily flow rather than scheduled as discrete events.

## Related

- [Building red team capability](../red/capability.md)
- [Defensive skills for attackers](../../foundations/montessori/defensive-skills.md)
- [Rotation programmes](../../foundations/montessori/rotation.md)
- [Building a purple team programme](../purple-team/team.md)
