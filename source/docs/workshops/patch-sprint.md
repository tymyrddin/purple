# Patch sprint

A patch sprint is a time-boxed, focused effort to clear a backlog of known vulnerabilities, misconfigurations, or deferred security work. It treats patching as a collaborative event rather than an ongoing background obligation that nobody owns and everybody deprioritises.

The premise is that most patch backlogs are not primarily a technical problem. The vulnerabilities are known. The fixes are often straightforward. What is missing is the protected time, the clear ownership, and the conditions that make it safe to apply changes without fear of breaking something that cannot be quickly recovered. A patch sprint creates those conditions deliberately rather than hoping they will emerge from normal workflow.

## Why the backlog exists

Understanding why patching falls behind is the prerequisite for designing a sprint that actually works.

The usual reasons are a combination of capacity (patching competes with delivery and loses), fear (applying a patch in a production system that lacks good rollback mechanisms is genuinely risky), ownership gaps (the system that needs patching belongs to no single team), and incentive misalignment (nobody is rewarded for reducing risk that has not yet materialised as an incident).

A patch sprint that does not address at least the capacity and fear problems will produce a week of nominal activity followed by a rapid return to the previous backlog growth rate. The sprint is a [ChangeShop](../foundations/change-management/index.rst)-style intervention: it temporarily alters the conditions that make patching hard. Lasting improvement requires changing those conditions permanently, which is a different piece of work that the sprint can inform but cannot replace.

## Preparing the sprint

The preparation matters more than the sprint itself.

Triage the backlog before the sprint begins. Not everything in a vulnerability backlog warrants the same urgency or the same approach. Group items by owner, by risk, and by complexity. Identify the items that are straightforwardly fixable within the sprint and the ones that require architectural work, co-ordination with other teams, or decisions that need to happen before the technical fix can proceed.

Prepare the environment. Rollback mechanisms should be in place or explicitly understood before the sprint starts. A patch sprint where people are afraid to apply fixes because they cannot safely test them is a sprint where nothing will actually be applied to the systems that matter.

Agree on scope and success criteria. What counts as done? A patch applied to all affected systems, or applied to the highest-risk tier? A vulnerability remediated or a vulnerability mitigated with a documented plan for full remediation? Being explicit about this before the sprint prevents the common pattern of declaring success on the basis of tickets closed rather than risk reduced.

## Running the sprint

Keep the duration short enough that it feels contained and achievable: two to five days works well. Longer sprints tend to lose focus as normal work reasserts itself.

Start each day with a brief standup focused on blockers, not status. The useful question is not "what are you working on?" but "what is stopping you from applying this patch?"

Make the blockers visible and address them in real time. If a patch cannot be applied because the test environment does not reflect production, that is a finding about the environment, not just a sprint blocker. Record it.

End each day with a short retrospective using the rapid retrospective format. What got unblocked? What is still blocked and why? What will we do differently tomorrow?

## After the sprint

The sprint produces two outputs: the patches applied, and the map of what made patching hard.

The second output is often more valuable than the first. A record of every blocker encountered during the sprint is a diagnostic of the conditions that produce patch backlog. Some of those conditions can be changed: clearer ownership, better rollback tooling, a standing time allocation for security maintenance. Others reflect genuine trade-offs that require a decision by someone with the authority to make it.

Document the blockers and bring them to whoever can act on them. A patch sprint that produces only applied patches and no systemic learning has addressed the symptom without touching the model that produced it.
