# Detection Priorities

Based on the likelihood and impact in the threat landscape, detection priorities ranked from highest to lowest.

## Priority 1: Detect what is actually happening now

| Technique                               | What to detect                                                                                                       | How                                                                                                                              |
|:----------------------------------------|:---------------------------------------------------------------------------------------------------------------------|:---------------------------------------------------------------------------------------------------------------------------------|
| IT/OT boundary lateral movement         | Unusual logins on EWS, historian, HMI from unexpected IT subnets; vendor VPN connections outside maintenance windows | Network flow logs between IT and OT zones; EWS authentication logs; VPN session monitoring                                       |
| Trust exploitation and misconfiguration | Anonymous OPC UA access; default credentials in use; traffic crossing zone boundaries that should be blocked         | Passive protocol monitoring (OPC UA, Modbus, S7) for unauthenticated sessions; periodic credential audits; firewall rule reviews |
| Reconnaissance                          | Scans on OT ports (502, 20000, 2404, 102, 4840, 1883) from IT or vendor networks                                     | OT-aware IDS/IPS (e.g., Snort with ICS rules); netflow monitoring to OT zones                                                    |

## Priority 2: Detect what has high impact even if less frequent

| Technique                   | What to detect                                                                                               | How                                                                                                            |
|:----------------------------|:-------------------------------------------------------------------------------------------------------------|:---------------------------------------------------------------------------------------------------------------|
| Denial of control           | Loss of telemetry from field devices; unexpected CPU stops on PLCs; communication session resets             | Heartbeat monitoring from critical PLCs/RTUs; controller status polling; alert on "loss of view" conditions    |
| Control logic manipulation  | Unexpected program uploads to PLCs (especially S7, Modicon); changes to alarm thresholds or setpoints        | Change detection on PLC logic (baseline and checksum); historian trend analysis for subtle drift               |
| Data integrity manipulation | Sensor readings that disagree with physical models or redundant sensors; replayed values that repeat exactly | Physical process cross-checking (e.g., flow in equals flow out plus accumulation); redundant sensor comparison |

## Priority 3: Lower likelihood, monitor for completeness

| Technique                          | What to detect                                                                                                            | How                                                                                        |
|:-----------------------------------|:--------------------------------------------------------------------------------------------------------------------------|:-------------------------------------------------------------------------------------------|
| Data exfiltration                  | Large or unusual data transfers from historian to corporate network; OPC UA or MQTT subscriptions from unexpected clients | Historian egress monitoring; netflow to and from historian; unusual OPC UA browse patterns |
| Protocol abuse and malformed input | Protocol parsing errors; unexpected PLC crashes or restarts                                                               | PLC health monitoring; error logs on protocol gateways; crash-and-recovery alerts          |
| Replay and timing attacks          | Sequence number anomalies (where supported); unexpected command repetition                                                | DNP3 sequence number tracking (challenging); command logging with timestamps               |

## Detection feasibility by technique

| Technique                   | Detection Feasibility | Primary Detection Layer                | Notes                                             |
|:----------------------------|:----------------------|:---------------------------------------|:--------------------------------------------------|
| IT/OT lateral movement      | High                  | Network and authentication logs        | Well-understood; needs visibility at boundary     |
| Trust exploitation          | Medium                | Network and configuration audits       | Anonymous access is easy to detect once you look  |
| Reconnaissance              | Medium                | Network                                | Scans are noisy but OT teams rarely watch         |
| Denial of control           | Medium                | Process and controller health          | Loss of view is detectable; slow loss is harder   |
| Control logic manipulation  | Low-Medium            | Change detection and process behaviour | Logic changes are invisible to network monitoring |
| Data integrity manipulation | Low                   | Physical process cross-checking        | Requires domain knowledge and redundant sensors   |
| Data exfiltration           | Low                   | Historian egress                       | Looks like normal traffic without baselining      |
| Protocol abuse              | Low                   | Controller health and error logs       | Crash is detectable; cause rarely is              |
| Replay attacks              | Very Low              | Sequence number tracking               | Most legacy protocols lack sequence protection    |

## The gap

The techniques with the highest likelihood (IT/OT lateral movement, trust exploitation, reconnaissance) are also the most 
detectable, if you are looking. Most European operators are not looking at the OT boundary with sufficient visibility.

The techniques with the highest impact (control logic manipulation, data integrity manipulation, denial of control) are 
often the hardest to detect, often requiring physical process knowledge or redundant sensors.

The hard truth: you cannot detect what you cannot see. Most European OT environments lack the network monitoring, 
authentication logging, or change detection required for even the Priority 1 detections above.
