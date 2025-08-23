# Adversary simulation metrics

## Key Performance Indicators (KPIs)

| Metric	                      | Formula	                                                     | Target                 |
|------------------------------|--------------------------------------------------------------|------------------------|
| Mean Time to Detect (MTTD)	  | Σ(Time from attack start to alert) / Total tests	            | <30 minutes            |
| Mean Time to Respond (MTTR)	 | Σ(Time from alert to containment) / Total tests	             | <60 minutes            |
| Alert Fidelity	              | (True Positives / (True Positives + False Positives)) * 100	 | ≥90%                   |
| Detection Efficacy	          | (Detected Attacks / Total Attacks) * 100	                    | ≥95% for critical TTPs |

## Tools

* CALDERA plugins for automated metric collection.
* Elastic Security or Splunk ES for response time tracking.