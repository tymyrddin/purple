# Measuring SIRT performance

Metrics help a SIRT understand its efficiency, identify bottlenecks, and continuously improve. A lean, agile SIRT focuses on actionable measures rather than generating endless reports. The following table summarises the most important metrics and what they mean in practice.

| Metric                           | Definition                                                                                                           | Meaning                                                                                                                                                                                                                          |
|:---------------------------------|:---------------------------------------------------------------------------------------------------------------------|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Detection success                | Number of alerts by department, team, or site.                                                                       | Shows how effective your detection solutions are. If the SOC is not generating the majority of alerts, your SIRT may be missing inputs or relying on inadequate sources.                                                         |
| Detection to decision            | Time taken for activity to be detected and processed through the system to determine if action is required.          | Measures the efficiency of analysts, detection tools, and SIEM. Shorter times indicate smoother alert handling and more responsive incident recognition.                                                                         |
| Decision speed                   | Time taken to make a decision, including coordination and gathering relevant stakeholders.                           | Decision-making depends on queue length and complexity of investigation. Faster decisions reduce risk exposure but require clear roles and pre-planned processes.                                                                |
| False positive rates             | Percentage of alerts that, upon investigation, are revealed not to be valid threats.                                 | High false positives erode confidence in tools, distract analysts, and can hide true issues. Feedback loops to reduce false positives are essential. The only thing worse than a false positive is an overlooked false negative. |
| Time to mitigation / containment | Time from detection to identifying impact, determining response, and implementing mitigation or containment actions. | Trends over time reveal strengths and weaknesses. These numbers guide investment in automation, remediation tools, and additional protective measures.                                                                           |

## Tips

* Track metrics consistently: regular reporting, even in small teams, builds awareness and accountability.
* Focus on trends rather than single incidents: variations are normal, patterns reveal actionable insights.
* Combine quantitative metrics with qualitative observations: analyst experience, workflow bottlenecks, and tool limitations are just as important.
* Use metrics to drive improvement, not punishment: a lean SIRT thrives on learning and iteration.

## Example

If your decision speed is consistently slow for certain alert types, you might improve it by refining workflows, adding playbook steps, or pre-identifying stakeholders for faster escalation.


```{raw} html
<div class="page-post-card__link">
    <a href="https://tymyrddin.dev/contact/">
      Improve your SIRT metrics with our help
    </a>
</div>
```

