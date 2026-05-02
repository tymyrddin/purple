# Audit findings and reporting

A finding is an observation about what a system does, supported by evidence, that identifies a deviation from
a requirement or a risk that is not adequately controlled. Understanding what a finding is, how it is
classified, and what a well-formed one looks like is as useful for the organisation receiving findings as it
is for the auditor producing them. An organisation that can evaluate findings critically, respond to them
constructively, and communicate them to the right internal audiences is in a better position than one that
treats them as an unwelcome homework list.

## Classifying findings

Classification sets expectations for what a finding means and what response it calls for.

Under ISO 27001, findings from external audits fall into three categories:

| Category                                   | What it means                                                                                                          |
|:-------------------------------------------|:-----------------------------------------------------------------------------------------------------------------------|
| Major nonconformity                        | A required control or process is absent or systematically failing; certification is at risk without prompt remediation |
| Minor nonconformity                        | A control or process exists but has identifiable weaknesses; remediation is required within an agreed timeframe        |
| Observation or opportunity for improvement | Not a nonconformity; a noted risk or suggested improvement worth monitoring                                            |

NIS2 supervisory review does not use the ISO certification framing. Findings from national competent
authorities assess whether entities meet the requirements of Article 21 and any more detailed national
implementing measures. The practical equivalent is distinguishing between controls that are absent, controls
that are present but ineffective, and controls that are present and functioning but could be improved.

IEC 62443 audit findings map to security level gaps: the difference between what a zone's controls currently
achieve and what the security level requirement specifies. A finding is specific to a zone and a security
level, which gives it a built-in remediation direction.

## What a well-formed finding contains

Understanding what constitutes good evidence in a finding serves two purposes: it helps an organisation
prepare evidence of the right kind before the audit, and it means the organisation can ask informed questions
if a finding is under-evidenced or poorly scoped.

A well-formed finding has four parts: the requirement (what is expected), the observation (what was found),
the evidence (what demonstrates the observation), and the risk or consequence (why it warrants attention).

The evidence is the part most often abbreviated or omitted. "Password policy does not meet requirements" is
a claim. A finding supported by a specific policy document reference, a named configuration gap, and a test
result that confirmed the gap is verifiable and respondable. A finding that is only a paraphrase is a finding
that cannot be properly challenged or closed.

For organisations that have run simulation environments or penetration tests, the outputs of those exercises
can strengthen corrective action responses: "This gap was identified in our internal exercise on [date],
corrective action was taken on [date], and the subsequent exercise confirmed the gap was closed" demonstrates
active compliance management rather than reactive remediation.

## Why findings create a change challenge

The [three domains of problem solving](../../foundations/problem-solving/three-domains.md) apply to every
internal conversation about audit findings.

The rational layer is the evidence and the control gap. This is where most finding discussions begin:
correctly identified, accurately described, properly referenced. Necessary, but rarely sufficient for
producing change.

The emotional layer is how the finding lands for the team it implicates. A finding that names a department's
process as non-compliant can be heard as a judgement of that team rather than an observation about a control.
How the finding is communicated internally determines whether the conversation that follows is about the
problem or the framing.

The political layer is whether the person or team responsible for addressing the finding has the authority
and the budget to do so. A finding that requires expenditure from a team that does not benefit from the fix,
or that implicates a senior stakeholder, will encounter resistance that the rational and emotional layers
cannot resolve alone. Naming this explicitly, when the situation calls for it, is how the organisation avoids
a corrective action plan that produces nominal compliance while leaving the actual gap in place.

A finding that triggers the patterns described in [why security change stalls](../../foundations/change-management/why-change-fails.md),
deflection, over-analysis, premature solutions, or status protection, is a finding where the political and
emotional layers have not been addressed.

## Building a response that will stick

A corrective action plan without the conditions for action is documentation, not a response. Those conditions
are: a named owner who knows they own it, a realistic scope (what specifically needs to change), a timeline
achievable given the owner's actual capacity, and a clear evidence requirement so the owner knows what done
looks like.

A corrective action plan submitted to close the finding on paper while the underlying gap persists is a risk.
If the same gap appears in the next audit cycle, it will be assessed more severely. Repeated findings in the
same area signal that the management system is not functioning as required, not just that someone forgot to
act.

## How findings land in the organisation

The Satir Change Model describes what happens when findings introduce a foreign element into an organisation's
status quo. A report containing significant nonconformities is, from the organisation's perspective, a
destabilising event. The chaos phase that follows is structural, not a sign that the findings were wrong or
the auditor was unreasonable.

The organisations that work through the chaos phase are the ones that treated findings as observations about
the system rather than verdicts about people, staged the response rather than attempting to address everything
at once, and supported the people responsible for remediation through the difficult period where things look
worse before they look better.

The [Satir Change Model in practice](../../foundations/change-management/satir-change-model.md) describes
what that period looks like and why retreating from it is the more expensive option.

## Communicating findings to different internal audiences

Findings received from an external auditor or supervisory authority need to reach different internal audiences
in different forms. The same finding means different things to different people, and a report shared without
translation often produces paralysis or defensiveness rather than action.

| Audience                 | What they need from a finding                                                                                            |
|:-------------------------|:-------------------------------------------------------------------------------------------------------------------------|
| Operational teams        | Specific, testable, clearly scoped: what exactly needs to change and how they will know it has                           |
| Senior management        | Risk exposure and consequence: what the organisation is exposed to and what addressing it costs versus not addressing it |
| Board or audit committee | Material risk posture, regulatory implications, and the investment decisions required                                    |

The evidence and classification remain the same. The context, level of detail, and framing differ by audience.

An executive summary that lists control identifiers and technical jargon without business consequence is a
summary that will not be read carefully by the people who need to authorise remediation. The translation
work is part of acting on findings, not a preliminary to it.

## Related

* [Gap analysis](gap-analysis.md)
* [Risk scoring](risk-scoring.md)
* [Interview and workshop facilitation](interview-facilitation.md)
* [The three domains of problem solving](../../foundations/problem-solving/three-domains.md)
* [Why security change stalls](../../foundations/change-management/why-change-fails.md)
* [The Satir Change Model in practice](../../foundations/change-management/satir-change-model.md)
