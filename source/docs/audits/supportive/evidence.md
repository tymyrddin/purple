# Evidence

All four frameworks eventually converge on the same request: show me. The playbooks each have a
stage where the showing happens, the [resilience dossier](../iso22301/dossier.md), the
[inspection](../iec62443/inspection.md), the [far bank](../nis2/bank.md), the
[base camp check](../iso27001/base-camp-check.md). Underneath all four sits the same craft: what counts
as evidence, where it comes from, and how to keep it so that any question can be answered in minutes rather
than reconstructed from memory. The strategic argument for why the craft is worth the effort sits in
[Making it legible](../legible.md).

## Two kinds of evidence

The distinction that runs through every audit page on this site applies here in its most practical form.

|                     | Implementation evidence                                                          | Effectiveness evidence                                                                                                                                               |
|:--------------------|:---------------------------------------------------------------------------------|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| What it shows       | The control exists and runs                                                      | The control produced its intended effect under realistic conditions                                                                                                  |
| Typical artefacts   | Approved policy, configuration export, training attendance, patch deployment log | Penetration test showing segmentation held, restoration drill with timings, phishing click-rate trend, tabletop report that surfaced a gap and its corrective action |
| Where it comes from | Normal operation                                                                 | Tests, exercises, and incidents                                                                                                                                      |
| What it cannot do   | Demonstrate the control works                                                    | Demonstrate the control is governed and documented                                                                                                                   |

Both kinds are needed, and audit preparation historically over-collects the first. An evidence base that is
all policies and no test results documents intentions. The [SEM](../../foundations/system-effectiveness/applying-sem.md) material covers the reasoning;
the practical consequence is that every test, exercise, and incident is an evidence-generating event, and
throwing away its outputs is throwing away the expensive kind.

## Evidence as residue

A control that genuinely runs leaves traces without being asked: change tickets, access review outputs, backup
job logs, exercise notes, incident timelines, monitoring dashboards, procurement records. Much of what an
auditor wants already exists as this residue; it is merely scattered, unlabelled, and living in inboxes.

The craft is routing, not writing. Deciding, per control, where its residue lands and what it gets called
costs far less than producing documentation about the control after the fact, and it avoids the two-realities
failure where the paperwork describes an organisation the evidence does not show. Manufactured evidence also
has a tell: artefacts clustered in the weeks before the audit, where genuine operation produces a natural date
distribution. Auditors read dates first.

## The chain from requirement to artefact

Traceability is what turns a pile into an evidence base. The chain runs: requirement, the control that
addresses it, the owner, the artefacts that show it, and where they live. One thin index carries the whole
thing; in an ISO 27001 context the Statement of Applicability's evidence column already is that index, and the
other frameworks can borrow the shape.

The test is retrieval time. If an auditor, a supervisor, or a new security manager asks about any requirement,
the walk from requirement to current artefact takes minutes when the chain exists and days when it does not.
Findings work the same way in reverse: a [well-formed finding](findings-reporting.md) cites its evidence, and
an organisation whose own evidence is chained can verify or challenge a finding instead of absorbing it.

## Attributes of a usable artefact

An artefact earns its place when it is:

* Dated, so it can be placed in a review cycle.
* Attributed: who produced it, and who approved it where approval is the point.
* Specific: which system, which scope, which population.
* Reproducible: how it was generated, so the same query or export can be run again.
* Tied to a control reference, so it can be found from the chain.

The recurring antipatterns are the same everywhere: screenshots with no date or context, exports nobody can
regenerate, records that exist only on one person's laptop, and evidence written for the audit rather than by
the work.

## Storage, naming, and hygiene

One repository, or one index over several locations, beats artefacts scattered across drives and inboxes.
Predictable naming (control reference plus date) makes retrieval boring, which is the goal. Two hygiene points
carry more weight than they look:

* Access and retention. Evidence often contains personal data: access logs with usernames, incident reports naming individuals, training records. It needs role-based access and a retention schedule of its own, or the evidence base becomes its own GDPR finding.
* Superseded material. Old versions kept alongside current ones without marking produce the two-maps problem during an audit. Archive, do not accumulate.

Where collection can be automated cheaply, scheduled exports and report jobs, automation also improves the
date distribution: evidence generated on a rhythm looks like what it is. Dashboards and their underlying
queries are covered in [the tooling page](ai-in-audits.md).

## Sampling and coverage

Auditors sample, so the organisation can sample first. For high-frequency controls, keeping the full run but
spot-checking a sample each quarter catches quality drift (empty reviews, rubber-stamp approvals) before an
external sample does. Coverage runs the other way: every control claimed in the SoA or its equivalent has at
least one current artefact, and the controls protecting the most critical assets carry effectiveness evidence
first, which is also the order a proportionality argument wants.

## Framework notes

* ISO 27001: Clause 9.1 (monitoring, measurement, analysis and evaluation) requires the results to be documented; the SoA evidence column is the natural chain index; recertification asks for a three-year story, which only an evidence base with history can tell.
* NIS2: the supervision model follows the entity classification. Essential entities face ex-ante as well as ex-post supervision and can be asked at any time, not only after incidents; important entities are supervised ex post, on indications of non-compliance. Either way, the proportionality defence is built from evidence of actual exposure and actual testing, and incident reporting records with timestamps are themselves compliance evidence.
* IEC 62443: evidence organises naturally by zone, and the recurring question is whether diagrams and deployed state still match; test reports map to the security level targets they were meant to validate.
* ISO 22301: exercise and drill reports are the core effectiveness stream, and near-miss records are evidence many organisations already have and do not file.

## Freshness

Evidence ages the way the models it documents age. A penetration test from eighteen months ago says little
about an environment that has changed twice since; a policy approval that predates the reorganisation approves
a different organisation. Refresh cadences belong with the control review cycles they document, and the
machinery for noticing staleness is the subject of [continuous compliance monitoring](continuous-monitoring.md).

## Related

* [Making it legible](../legible.md)
* [ISO 22301 The resilience dossier](../iso22301/dossier.md)
* [IEC 62443 The inspection](../iec62443/inspection.md)
* [NIS2 Reaching the far bank](../nis2/bank.md)
* [ISO 27001 Base camp checks](../iso27001/base-camp-check.md)
* [Gap analysis](gap-analysis.md)
* [Audit findings and reporting](findings-reporting.md)
* [Continuous compliance monitoring](continuous-monitoring.md)
* [Applying SEM to security](../../foundations/system-effectiveness/applying-sem.md)

*Last updated: 8 July 2026*
