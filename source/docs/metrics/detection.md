# Detection coverage metrics

## Mapping to MITRE ATT&CK

Objective: Measure % of ATT&CK techniques covered by detections.

| Metric	                | Calculation	                                                   | Target |
|------------------------|----------------------------------------------------------------|--------|
| Technique Coverage	    | (Detected Techniques / Total Relevant Techniques) * 100	       | ≥80%   |
| Subtechnique Coverage	 | (Detected Subtechniques / Total Relevant Subtechniques) * 100	 | ≥70%   |
| Tactic Coverage	       | (Covered Tactics / Total Tactics) * 100	                       | 100%   |

## Tools

Attack Navigator Heatmaps example

```json
{"techniques": [{"techniqueID": "T1059.003", "color": "#ff6666", "comment": "Detected by Sigma rule #123"}]}
```

Automation: [Panther](https://panther.com/) or [Anomali](https://www.anomali.com/) for ATT&CK alignment.