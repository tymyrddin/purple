# Controlled attack scenario framework

```
  +---------------------+     +---------------------+     +---------------------+
  |                     |     |                     |     |                     |
  |   Threat Intel      |---->|  Select ATT&CK      |---->|  Existing Coverage? |
  |     Report          |     |   Technique         |     |      +-----+        |
  +----------+----------+     +----------+----------+     |      | Yes |        |
             |                          |                 |      +-----+        |
             |                          |                 |           |         |
             v                          v                 |           v         |
  +----------+----------+     +----------+----------+     |  +--------+-------+ |
  |                     |     |                     |     |  | Test Detection | |
  |  MITRE Navigator    |     |  Threat Model       |     |  |     Efficacy   | |
  |   (Prioritization)  |     |  (OWASP/D3FEND)     |     |  +--------+-------+ |
  +----------+----------+     +----------+----------+     |           |         |
             |                          |                 |           v         |
             |                          |                 |  +--------+-------+ |
             +--------------------------+                 |  | Execute Atomic | |
                                                          |  |      Test      | |
                                                          |  +--------+-------+ |
                                                          |           |         |
                                                          |           v         |
                                                          |  +--------+-------+ |
  +---------------------+     +---------------------+     |  | Analyze        | |
  |                     |     |                     |     |  |   Telemetry    | |
  |  Develop New        |<----+      No Coverage    |     |  +--------+-------+ |
  |   Detection         |     |        Found        |     |           |         |
  +----------+----------+     +---------------------+     |           v         |
             |                                            |  +--------+-------+ |
             |                                            |  | Generate       | |
             v                                            |  | Findings Report| |
  +----------+----------+                                 |  +----------------+ |
  |                     |                                 |                     |
  |  Sigma/YARA         |                                 |                     |
  |   Rule Creation     |                                 |                     |
  +---------------------+                                 +---------------------+
```

## Toolchain integration

| Phase	     | Red Team Tools	           | Blue Team Tools                |
|------------|---------------------------|--------------------------------|
| Planning	  | MITRE Navigator	          | Threat Model (OWASP, D3FEND)   |
| Execution	 | Atomic Red Team, Caldera	 | SIEM (Splunk, Elastic)         |
| Analysis	  | VECTR, C2 Logs	           | EDR (CrowdStrike, SentinelOne) |
| Reporting	 | Jira, Confluence	         | Sigma/YARA Hub                 |