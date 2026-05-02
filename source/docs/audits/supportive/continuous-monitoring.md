# Continuous compliance monitoring

An audit is a snapshot. It tells you whether you were compliant on a specific day, with the evidence available
on that day, assessed by the people present. The frameworks surrounding it, ISO 27001, NIS2, IEC 62443, ISO
22301, do not require compliance on audit day. They require compliance as a maintained state.

The gap between snapshots is where things unravel. Controls degrade. Configurations drift. Staff change.
Systems are added without going through the documented process. An organisation that is genuinely compliant
on audit day and does nothing until the next one will, by the time the next audit arrives, have accumulated
gaps in several areas. The ones still compliant are the ones that kept looking.

## What monitoring covers

Continuous compliance monitoring is not a single activity. It is a set of overlapping mechanisms that keep
the compliance picture current.

Control operation monitoring: are the controls still running as designed? Automated tools can verify
configuration against a baseline, check that scheduled processes completed and produced output, and alert when
something falls outside an expected range.

Evidence generation: many controls produce evidence as a byproduct of normal operation, including access logs,
patch deployment records, and change tickets. Ensuring that evidence is retained, complete, and accessible
means that when a question is asked, the answer can be demonstrated rather than reconstructed from memory.

Vulnerability and change tracking: new vulnerabilities affect whether existing controls remain sufficient.
Changes to systems or processes affect whether the scope is still accurate and whether controls designed for
the previous configuration still apply to the current one.

Testing cycles: penetration tests, tabletop exercises, CTF scenarios, and stress tests are not one-off
activities. Run on a recurring schedule, they convert a one-time compliance assertion into repeated evidence
that a control produces its intended effect under realistic conditions. The gap between "it was tested once"
and "it is tested regularly" is significant in any audit or supervisory review.

Review processes: formal reviews of the risk register, threat register, access rights, and supplier assessments
on a defined schedule ensure that the compliance picture is updated, not merely preserved from the last time
it was checked.

## What the frameworks expect

ISO 27001 Clause 9.1 requires the organisation to determine what needs to be monitored, how, when, and by
whom, and to analyse and evaluate the results. The specific approach is left to the organisation, but the
requirement for evidence of ongoing monitoring is not. Surveillance audits between three-year recertification
cycles check that the ISMS is still operating, not just documented.

NIS2 expects that the measures required by Article 21 are maintained as an appropriate response to risk.
The proportionality principle means that what constitutes adequate monitoring depends on the entity's size,
criticality, and exposure, but the expectation of ongoing adequacy is explicit. Supervisory authorities can
inspect at any time, not only in response to incidents.

IEC 62443 addresses the maintenance phase of the security lifecycle. Security levels achieved at deployment
degrade over time without active maintenance: patch management, configuration management, and change control
are monitoring activities that sustain security level achievement. A zone assessed to SL 2 at commissioning
may drift below that target without those mechanisms in place and operating.

## Useful metrics

Metrics are not useful unless they are honest. A patch compliance metric that counts only managed systems
and excludes unmanaged devices is not a measure of patch compliance. Defining what is measured, what is
excluded, and why carries as much weight as the number itself.

| Metric | What it reveals |
|:-------|:----------------|
| Patch compliance rate | Proportion of in-scope systems patched within the policy window |
| Mean time to close access review findings | Whether access rights are being corrected, not just reviewed |
| Vulnerability age by severity | Whether high-severity findings are being remediated promptly |
| Control testing frequency and pass rate | Whether tested controls still produce their intended effect |
| Evidence completeness | Whether required records exist and are current |
| Incident detection rate | Whether security monitoring is producing alerts on genuine activity |

A metric that stays green without ever being tested is a measurement of the metric, not the control.

## When monitoring reveals a gap

Monitoring that only confirms compliance is a check on evidence retention. Monitoring that generates findings
is monitoring that is working.

A gap discovered through continuous monitoring is better than the same gap discovered by an external auditor.
The organisation has the opportunity to understand and address the root cause before it becomes a finding in
a report. The evidence of how it was discovered and what was done about it is itself compliance evidence: it
demonstrates that the monitoring is real and that the organisation responds to what it finds.

A metric that moves from green to amber over several review cycles without triggering a response is not
continuous monitoring. It is continuous observation. The response mechanism is as important as the data
collection.

## Simulation environments as ongoing evidence

Compliance evidence generated through simulation environments has a shelf life. A penetration test from
eighteen months ago that found no exploitable paths provides limited assurance if the environment has changed
substantially. A tabletop exercise that tested the incident response procedure last quarter provides more
current assurance than one from two years ago.

Scheduling simulation activities as part of the compliance calendar, rather than treating them as one-off
events, converts them into an ongoing evidence stream. The [stress-testing](../resilience/stress-testing.md)
format is designed to run on a recurring basis for exactly this reason: each run either confirms that the
previous findings were addressed or surfaces new ones, and the sequence constitutes a testable compliance
record rather than a single data point.

## Related

* [Gap analysis](gap-analysis.md)
* [Risk scoring](risk-scoring.md)
* [Findings and reporting](findings-reporting.md)
* [Stress-testing resilience](../resilience/stress-testing.md)
* [Big data and BI tools](big-data.md)
* [AI in audits](ai-in-audits.md)
