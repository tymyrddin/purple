# Gap analysis

A gap analysis compares the current state of security controls, documentation, and practices against a defined
requirement: a standard, a regulatory obligation, or an organisation's own stated policy. The result is a
structured list of what is present, what is absent, and what is partially in place. The method applies across
all compliance frameworks covered in these audit sections.

## When to use it

A gap analysis is useful at any stage of an audit programme:

* Before implementation: to scope the work and prioritise effort before committing resources
* Mid-cycle: to verify that remediation actions have closed previously identified findings
* Before external audit: to identify remaining gaps before an auditor does
* After an incident or exercise: to check whether the event exposed something not previously visible

## Gap categories

Gaps fall into four categories:

| Category          | What it means                                                                           | Example                                                                       |
|:------------------|:----------------------------------------------------------------------------------------|:------------------------------------------------------------------------------|
| Documentation gap | A required policy, procedure, or record does not exist or is outdated                   | No incident response procedure covering supply chain compromise               |
| Control gap       | A required technical or organisational control is absent or not functioning as intended | MFA policy exists but is not enforced on remote access                        |
| Evidence gap      | A control exists and runs, but no record of its operation is retained                   | Patch management process runs; no patch compliance logs kept                  |
| Process gap       | A control is documented and evidenced, but actual practice diverges from the procedure  | Change management policy requires dual approval; single approvals are routine |

Evidence gaps and process gaps are typically discovered later than documentation and control gaps, because they
require observation rather than document review. A process gap is also a model signal: the documented procedure
encodes an assumption about how work gets done, and the gap is evidence that the assumption no longer fits the
current environment.

## Framework entry points

Each framework brings its own vocabulary and timing. The underlying method is the same.

| Framework  | Typical entry point                                                     | Primary focus                                                                      |
|:-----------|:------------------------------------------------------------------------|:-----------------------------------------------------------------------------------|
| ISO 27001  | Before Stage 1 documentation review; between surveillance audits        | SoA completeness, risk treatment coverage, evidence of operation                   |
| NIS2       | On entering scope; before supervisory review                            | Article 21 mandatory measures; missing vs. ineffective control distinction         |
| ISO 22301  | After business impact analysis; after each exercise or disruption event | Continuity procedure gaps, evidence of tested recovery, single-person dependencies |
| IEC 62443  | Post-deployment; before external ICS audit                              | Zone-aligned control coverage, asset register alignment, threat-to-control mapping |
| Resilience | Cross-framework review                                                  | Coverage unique to each standard; dependencies not captured in any single register |

For IEC 62443, zone relevance is an additional check: a control may exist and be evidenced but applied to the
wrong zone, leaving the actual zone unprotected. That is a different finding from a missing control.

For NIS2, the gap analysis explicitly distinguishes missing controls (the control does not exist) from
ineffective controls (the control exists but does not produce its intended effect under realistic conditions).
Compliance evidence built on implementation alone covers only the first category.

## Structuring the assessment

A gap analysis works most cleanly as a table: requirement on one side, current state on the other, a gap
rating, and a remediation owner. That four-column structure is the minimum to make findings actionable.

Severity ratings can be kept simple:

* Critical: no control or evidence in place; likely to generate an audit finding
* Partial: some control or evidence exists but insufficient to satisfy the requirement
* Minor: control and evidence exist but documentation or practice needs adjustment

## Prioritising what to close

Not all gaps carry equal weight. Gaps in controls protecting the most sensitive assets or supporting the most
critical processes take priority. Gaps that would be immediate audit findings (absent documentation, absent
evidence for a mandatory control) come before gaps that would generate improvement observations.

A gap that reappears in successive review cycles is worth examining differently from a new finding. Closing the
documented gap is a corrective action. Asking why it recurs is the question that prevents it reappearing.
Recurring gaps in the same area are usually a signal that an assumption in the control design does not fit the
operating environment, not that people keep forgetting to do the same thing.

## Recording and following up

Each identified gap needs an owner, a target closure date, and a note on what evidence will confirm it is
closed. Without these, a gap list becomes a backlog with no exit condition. The gap analysis output feeds into
the risk treatment plan and the corrective action log.

## Related

* [ISO 27001 Risk tent](../iso27001/risk-tent.md)
* [ISO 27001 Base camp check](../iso27001/base-camp-check.md)
* [ISO 27001 The gear depot](../iso27001/gear-depot.md)
* [NIS2 Understanding the river](../nis2/river.md)
* [ISO 22301 The factory's emergency systems](../iso22301/controls.md)
* [ISO 22301 The resilience dossier](../iso22301/evidence.md)
* [IEC 62443 Threats to the factory](../iec62443/threats.md)
* [IEC 62443 The factory's defensive mechanisms](../iec62443/controls.md)