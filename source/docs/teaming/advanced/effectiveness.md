# Measuring effectiveness

Metrics demonstrate purple team value and drive continuous improvement.

## Detection coverage metrics

ATT&CK coverage: Percentage of relevant ATT&CK techniques that generate alerts.

Calculation: (Techniques with working detections / Techniques tested) × 100

Trend: Should increase over time as detection engineering improves.

Coverage by tactic: Break down by reconnaissance, initial access, execution, etc.

## Response time metrics

Mean time to detect (MTTD): Average time from attack action to alert generation.

Mean time to respond (MTTR): Average time from detection to containment.

Mean time to recover (MTTR2): Average time from containment to full operational recovery.

Trend: All should decrease as detection and response improve.

## Adversary simulation metrics

Objective achievement rate: Percentage of red team objectives achieved despite blue team.

Attack path diversity: Number of different techniques needed to achieve objectives.

Detection rate per objective: How many steps of attack path were detected.

Trend: Over time, fewer objectives should be achieved, more steps should be detected.

## Maturity indicators

Detection sophistication: Progression from signature-based to behaviour-based detection.

Response automation: Percentage of response actions automated vs. manual.

Proactive vs. reactive: Ratio of threat hunting to incident response time.

Coverage completeness: Percentage of MITRE ATT&CK framework covered by detections.

## Reporting to stakeholders

Executive dashboards: High-level metrics, trend lines, risk reduction demonstrated.

Technical reports: Detailed findings, detection gaps, technical improvements implemented.

Board reporting: Business risk context, investment effectiveness, maturity progression.
