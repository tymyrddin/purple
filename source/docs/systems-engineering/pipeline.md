# Introducing a proper pipeline

Imagine you are introducing a proper deployment pipeline on a self-hosted provider such as Hetzner: infrastructure
as code using Terraform and Ansible, CI/CD through GitHub Actions or GitLab CI, hardened images, logging, and
monitoring. The whole grown-up setup.

Previously, the practice was: SSH into the server, adjust things until they behave, hope no one notices. Knowledge
lives in one person's head. Security is aspirational. Nothing is on fire, so nothing changes.

This is a classic late status quo. Fragile but familiar. And because it is familiar, the disruption of replacing it
follows the Satir arc with impressive fidelity.

## Late status quo

Systems work, in the sense that they have not visibly failed recently. What "work" means in practice: someone
with access knows which undocumented steps to take in which order, and that knowledge is not written down because
writing it down would reveal how fragile it is.

Security is described in policy documents and addressed in infrastructure only when an incident forces the
conversation. Access controls are broader than they need to be because tightening them would require understanding
what everything actually does. Deployments are manual because automating them would require making the process
legible, and making the process legible would surface the parts of it that are embarrassing.

No urgency. No budget. No appetite.

## Resistance

You introduce pipelines, immutable infrastructure, and proper access controls. Reaction follows quickly.

"This is over-engineered." Possibly. The person saying it is describing a real mismatch between the complexity
of the new system and the complexity of the problem as they currently understand it. The mismatch is real even
if the conclusion is wrong.

"Why can't I just SSH?" Because that is how the previous state persisted. But that is not an answer that lands
well at this stage, and explaining it prematurely produces defensiveness rather than understanding.

"It was faster before." It was not, but it felt faster because the costs were invisible: the time spent
diagnosing servers whose state was unknown, the incidents that occurred because a configuration change was applied
to production without being tested, the person on holiday who was the only one who knew why something was set up
the way it was. Invisible costs are not experienced as costs.

Performance dips slightly because people are now forced to think in ways the previous system did not require.

## Chaos

Pipelines fail for reasons that are not immediately clear. Permissions break deployments that worked fine the last
time someone touched them manually. Someone wipes a staging environment. Logs exist but are in a location no one
has checked before.

Classic symptoms: pipelines re-run without understanding why they failed, YAML debugged at unreasonable hours,
emergency SSH access quietly reintroduced "just temporarily" to unblock something urgent. The temporary exception
is the most dangerous moment of the transition. It is the point at which the organisation can most easily
rationalise returning to the previous state: "we still need the escape hatch, we are not ready, let us slow
down."

Confidence drops faster than performance. People experience not only the friction of the new system but the
loss of competence they had in the old one. Someone who could confidently manage a server by hand now cannot
confidently explain why a pipeline step is failing. That experience is real and should not be dismissed.

This is the moment organisations abandon the effort.

## Integration

Gradually, pipelines stabilise. Teams develop the habit of reading logs before re-running. Access patterns
become understood. The security controls that felt like punishment start to feel like a description of reality:
this account does not need access to that system, and the pipeline enforces that without requiring a conversation
every time.

The key shift is that people stop fighting the system and start using it. The system becomes legible. The
previous state, in retrospect, starts to look as fragile as it actually was.

## New status quo

Repeatable deployments. Traceability. Reduced single-person dependency. Security that exists in the
infrastructure rather than in policy documents. Fewer surprises, not zero, but fewer, and the ones that
occur are diagnosable.

The knowledge that used to live in one person's head now lives in code that can be read, reviewed, and
changed deliberately. This is not only an operational improvement. It is a security improvement, because the
previous state was a risk that the organisation had simply learned not to see.

## What determines whether the transition succeeds

Not tooling selection. Not the technical quality of the pipeline design. Whether the organisation survives the
chaos phase without retreating.

That requires a few specific things. Accepting that performance will drop and communicating this before it
happens, not after. Removing the emergency SSH backdoor when it is reintroduced, rather than letting it
persist because the moment of crisis has passed and no one wants another argument. Supporting the people who
are experiencing the competence loss rather than treating their frustration as obstruction. Identifying the
early adopters and making their experience visible to the rest of the team.

The organisations that reach the new status quo did not get there because the transition was smooth. They got
there because they did not mistake the chaos phase for evidence that the direction was wrong.

## Related

- [The Satir Change Model](../foundations/organisational-development/satir-change-model.md)
- [The Satir Change Model in practice](../foundations/change-management/satir-change-model.md)
- [On-premises DevSecOps](https://blue.tymyrddin.dev/docs/dev/devsecops/on-prem/)
