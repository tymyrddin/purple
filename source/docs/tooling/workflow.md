# Visual reference — automation workflow

```text
  +---------------------+       +---------------------+       +---------------------+
  |                     |       |                     |       |                     |
  |   RED TEAM TOOLS    |------>|   DETECTION ENGINE  |------>|   SIEM / DASHBOARDS |
  | (CALDERA, Atomic,   |       | (Sigma, YARA,       |       | (Elastic, Splunk,   |
  |  C2 Frameworks)     |<------|  EDR Rules)         |<------|  Grafana)           |
  |                     |       |                     |       |                     |
  +----------+----------+       +----------+----------+       +----------+----------+
             |                             |                             |
             |                             |                             |
             v                             v                             v
  +----------+----------+       +----------+----------+       +----------+----------+
  |                     |       |                     |       |                     |
  |  ATTACK SIMULATION  |       |  RULE VALIDATION    |       |  THREAT HUNTING     |
  |    (Emulate TTPs)   |       |   (MTTD/MTTR)       |       |    (Proactive       |
  |                     |       |                     |       |     Detection)      |
  +----------+----------+       +----------+----------+       +----------+----------+
             |                             |                             |
             |                             |                             |
             +--------------+--------------+                             |
                            |                                            |
                            v                                            v
  +---------------------+   |  +---------------------+       +---------------------+
  |                     |   |  |                     |       |                     |
  |   FEEDBACK LOOP     |<----+|   AUTOMATED         |<------|   CONTINUOUS        |
  |  (Jira, Reports,    |      |   REMEDIATION       |       |   IMPROVEMENT       |
  |   Purple Meetings)  |----->|  (SOAR, Playbooks)  |       |  (Metrics, Maturity)|
  |                     |      |                     |       |                     |
  +---------------------+      +---------------------+       +---------------------+
```