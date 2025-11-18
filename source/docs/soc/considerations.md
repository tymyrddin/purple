
# SOC & SIRT considerations

Building and operating a SOC and SIRT is not just about tools, roles, or processes. Some nuances and trade-offs influence how your teams function, interact, and stay effective over time. This page outlines key considerations to guide your decisions.

## Detection vs. response

* The line between detecting threats and responding to them is often blurry.
* Threat hunting, for example, identifies risks proactively but frequently overlaps with response activities.
* Lean SOCs and agile SIRTs benefit from understanding this overlap, so that teams collaborate smoothly without stepping on each other’s toes.

## Tooling and automation

* Both SOC and SIRT leverage Security Orchestration, Automation, and Response (SOAR) tools  to streamline workflows.
* Automation can speed up routine tasks, like alert triage or data collection, freeing analysts and responders for higher-value work.
* However, tools are only as effective as the processes and human oversight behind them—don’t rely solely on automation.

## Team structure and job rotation

* Tier 1 SOC work, monitoring dashboards, alerts, and logs, can be repetitive and exhausting, especially during nights and weekends.
* Combined SOC + SIRT teams can rotate roles, giving analysts exposure to more interesting incident response tasks, helping maintain motivation and skill development.
* Some argue that keeping SOC and SIRT separate allows each team to focus on its core objectives, but overly rigid separation can reduce overall effectiveness.

## Multi-site operations

* Organisations with multiple locations often benefit from distributed SOCs at each site for local monitoring.
* A centralised SIRT coordinates cross-site incidents, ensures consistency, and supports complex investigations.
* This hybrid model balances responsiveness with strategic oversight.

## Resources for further reading

* [Pros and Cons of Outsourced SOC](https://computertech.com/blog/pros-cons-outsourced-soc) – overview of advantages and disadvantages of outsourcing security operations.
* [Pros and cons of an outsourced SOC vs. in-house SOC](https://www.techtarget.com/searchsecurity/tip/In-house-vs-outsourced-cybersecurity-operations-center-capabilities) – detailed comparison for organisations evaluating SOC models.


```{raw} html
<div class="page-post-card__link">
    <a href="https://tymyrddin.dev/contact/">
      Sort out your SOC–SIRT relationship with us?
    </a>
</div>
```

