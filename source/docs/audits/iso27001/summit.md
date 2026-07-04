# The summit push

![Summit](/_static/images/summit.png)

The external certification audit: Stage 1, Stage 2, findings, and what to learn from them.

With [gear checked at base camp](base-camp-check.md), the summit push is the external certification audit,
where independent auditors from a certification body verify that the ISMS meets ISO 27001 requirements. Think
of them as expert mountain guides with clipboards instead of crampons. They will not climb the entire route
with the expedition; their job is to verify the team knows which end of the rope goes where, and that the
climb does not exist on paper only.

## The certification cycle

Initial certification comes in two stages. Stage 1 is a documentation review, often remote, one or two days:
completeness, conformance, and planning for what follows. Stage 2 is on-site verification, typically two to
seven days depending on size and complexity, with one to three months between them to address Stage 1
findings. After certification, surveillance audits check in annually, sampling different areas each year, and
a full recertification audit every three years resets the cycle. Duration scales with headcount, sites, scope
breadth, and maturity; an immature ISMS takes longer to audit, which is one more argument for arriving mature.

## Stage 1: the reconnaissance

Auditors stay at base camp and pore over the maps and gear lists. The mandatory set: ISMS scope, information
security policy, risk assessment methodology and results, risk treatment plan, Statement of Applicability,
internal audit programme and results, and management review records, plus the supporting procedures the SoA
implies.

What they check is less the paperwork than its coherence. Completeness: fundamental documents missing means no
safe way to proceed. Alignment: controls and policies that match the standard rather than a different mountain.
Evidence of operation: internal audits, reviews, and assessments that verifiably happened. Consistency:
processes that do not contradict each other, two maps for one trail gets someone lost. And maturity:
documentation that shows evolution over time, because a set of documents all created last month reads as audit
theatre, and experienced auditors read dates first.

The recurring Stage 1 findings are predictable: a risk assessment more than a year old, an SoA with unjustified
exclusions or controls that appear nowhere in the treatment plan, policies referencing the previous edition of
the standard or procedures that do not exist, no management review on record, objectives that cannot be
measured. Outcomes range from proceed, through proceed with conditions, to Stage 2 postponed until the gaps
close.

## Stage 2: the verification

Now auditors move from documentation to reality: is what was documented actually happening, do the controls
work, do people understand their roles. Interviews run from top management (commitment and accountability)
through the ISMS manager, process owners, IT, HR, and a sample of general staff for awareness.

Verification covers three fronts, always with the same underlying question: does the evidence show operation
over time?

* Technical: access controls, logging, backups and their last successful restoration, patching, segmentation as documented.
* Physical: badge systems, visitor handling, clear desks observed on the walk.
* Organisational: contracts, training records, incident handling, supplier assessments, continuity test results.

The techniques are worth knowing because they are hard to fake in aggregate: "show me how you handle a suspected
phishing email right now"; "if the backup system fails at 2:00, who gets called"; "take me through exactly what
happens when an employee leaves"; a request for a year of access review records; an unannounced walk through a
work area.

What auditors actually want is not perfection; a flawless audit is itself suspicious, suggesting either a rare
maturity or effective concealment. They want honest implementation people actually follow, controls traceable
to real risks and explainable ("why this control?"), evidence with a natural date distribution, self-awareness
about weaknesses with plans attached, and visible management involvement.

The red flags mirror those exactly: theatre (perfect paper, staff who cannot explain what they do),
box-ticking without a why, "you'll have to ask Sarah", all evidence from the last thirty days, staff who do
not know the policies exist, blame culture, inconsistent stories for the same process.

## Findings and outcomes

Findings come in three weights, consistent with the internal ladder. 

* Major nonconformity: a critical
requirement missing or a systematic failure, no risk assessment, an SoA control that does not exist, no
management review for years; certification waits until it is resolved, typically within a 90-day window,
sometimes with additional audit days. 
* Minor nonconformity: partial or isolated failure, a missed review, an
incomplete record; corrective action within three to six months, closed remotely, no block to certification.
* Observation: not a nonconformity, but a note that may become one if ignored.

The outcomes follow: certification granted outright; granted with conditions once minor items close; deferred
pending a follow-up audit for major items; or, rarely, denied, an outcome an effective internal audit
programme all but rules out.

## Practicalities

Costs vary widely with size, scope, sites, sector, and certification body: total first-year cost for a typical
small to medium organisation lands somewhere in the €10,000 to €30,000 range once certification fees and
internal time are counted, with annual surveillance costs after that. The initial journey usually takes three
to six months from engaging a certification body to holding the certificate.

Preparation is mostly logistics done early: mandatory documents and supporting evidence organised so anything
can be produced in minutes, calendars blocked for the people auditors will want, a room for the auditors, and
read-only access prepared for evidence review. The behavioural preparation compresses to one instruction:
honesty. "We identified this gap and are working on it" tends to outperform pretended perfection; staff
briefed on what to expect but not scripted; findings received as information rather than insult; and no
evidence created on the spot, because freshly minted documents announce themselves.

## Learning from the summit

Reaching the summit is exhilarating, but the audit is a catalyst as well as a validation. Findings are the
scrapes and bruises of the climb, and each one has a root cause worth classifying:

* A process problem: the procedure is unclear, impractical, or ignored, and the fix is making documentation match secure reality.
* A people problem: training, awareness, or role fit.
* A tooling problem: manual steps prone to error, automation missing.
* A culture problem: security as burden, blame discouraging honest reporting.
* Or a model problem.

The model problem is the one the other four can hide. Every control encodes an assumption about the
environment it operates in. If a finding recurs despite previous corrective actions, the underlying assumption
may no longer hold: the environment changed, the threat evolved, or the control was built for conditions that
no longer exist. An access review that accumulates rubber-stamp approvals despite repeated corrective actions
is not primarily a training problem; it is evidence that the model the control was built on does not match how
access decisions actually get made.

The same reading applies to controls that are consistently bypassed even after enforcement and retraining. The
model assumed a fit between control and workflow, and persistent bypass is evidence the fit does not hold.
Asking what made the workaround feel necessary is more diagnostic than escalating enforcement.

## Output

The output of this stage is, with preparation, a certificate, and with or without one, a findings report worth
more than it cost: corrective actions with owners and dates, lessons classified down to the model level, and
an audit preparation process improved for the next cycle. The certificate marks the summit, and mountains
change. [Keeping the flag flying](flag.md) is its own discipline.

## Related

* [NIS2 Reaching the far bank](../nis2/bank.md)
* [What the auditor walks into](../what-the-auditor-walks-into.md)
* [Gap analysis](../supportive/gap-analysis.md)
* [Standards reference](../supportive/standards.md)
