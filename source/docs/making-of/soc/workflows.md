# Workflows and runbooks

SOC workflows are documented hypotheses about how specific categories of event should be handled. They are not procedures that, once written, can be followed mechanically; they are starting points that require human judgement and that need to be updated as experience accumulates.

## Designing workflows

The [Montessori](../../foundations/montessori/index.rst) framing is useful here: a well-designed workflow is a prepared environment for the analyst. It provides the structure and the materials for the work without removing the need for judgement. A workflow that attempts to pre-decide every branch of a complex incident is a workflow that will be abandoned the first time the incident does not follow the script.

A useful workflow for an alert category covers:

What information to gather before making a triage decision. This is where automation is most valuable: log collection, endpoint status, network context. The analyst makes better decisions with complete information, and gathering routine data does not require the analyst's judgement.

What the decision criteria are. Not "is this suspicious?" but "does this meet the threshold for X response?" The criteria need to be specific enough to apply consistently.

What the response actions are for each decision outcome. Containment steps, escalation contacts, communication requirements.

What to document, and where. The documentation that happens during the response is the input to the [post-incident](../../making-of/sirt/learning.md) review and the compliance record. If it requires a separate effort after the fact, it will be incomplete.

## Iteration as method

Workflows are wrong when they are written. Not fundamentally wrong, but wrong in detail, because they are written against a mental model of how incidents unfold that will not match every real incident. The question is not whether the workflow will need updating, but how quickly the updates happen.

Involve SOC analysts in workflow design. They are the people closest to the actual work and will see problems that are invisible from outside. A workflow designed without their input will produce frustration when the steps do not match the reality of the work.

Update workflows after incidents and after exercises. "After" means promptly, while the gap between the workflow and the real situation is still visible. The temptation to do a larger review later, incorporating multiple incidents, is temptation to a review that does not happen.

Treat each update as a small, deliberate improvement rather than a rewrite. Rewrites are expensive and often produce a new document that is similarly wrong in new ways. Targeted amendments that address specific observed gaps accumulate into a workflow that has been tested by reality.

## Automation

Automate the steps that do not require human judgement: log collection, initial enrichment, alert correlation across sources, notification routing. Do not automate decisions that require context the automation cannot have: whether a particular activity is suspicious in this specific organisational context, whether the situation warrants escalation, whether containment is appropriate given business constraints.

The goal of automation is to reduce the cognitive load on analysts during routine handling so that more attention is available for the events that genuinely require it. Automation that replaces human oversight on decisions that matter is a different thing, and a risk in its own right.

## Related

- [Detection and response](detection.md)
- [SIRT structure](../sirt/structure.md)
- [The learning loop](../sirt/learning.md)
- [Knowledge transfer: workflows](../../knowledge-transfer/workflows.md)
- [Knowledge transfer: playbooks](../../knowledge-transfer/playbooks.md)
