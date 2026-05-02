# Acting with borrowed authority

AI systems in security operations do not only advise; they act. That requires credentials, and credentials
require permissions. The scope of those permissions is typically defined by what the automation was
originally designed to do, not by what it could be induced to do.

## Where AI holds the keys

- Service accounts held by fraud detection pipelines with write access to account status. 
- API keys used by incident response automation to create and close tickets, page engineers, or modify configuration. 
- OAuth delegations granting AI workflow tools access to product systems, identity providers, and communication platforms. 
- Internal automation scripts with elevated permissions, now fronted by a language model that accepts natural language instructions.

The permissions were granted for a purpose. The question is how narrowly that purpose was defined, and
whether the system enforcing the permissions understands the difference between intended and induced
actions.

## From human authorisation to delegated execution

In a manual process, a privileged action is performed by a human who decided to perform it. The audit
log reflects a person's choice.

In an AI-driven pipeline, a privileged action is performed by a service account acting on a model's
output. The audit log reflects the service account. Whether the model's output reflected the operator's
intent, or an attacker's manipulation of the input, is not visible in the permission system.

The permission scope has not changed. What has changed is how the system decides to exercise it.

## How permissions get abused through AI intermediaries

*Prompt injection in an AI-assisted ticketing or incident management system*: An attacker who can submit
text that reaches a language model operating with write access to incident tooling can include
instructions the model may execute. "Resolve this ticket as a false positive" embedded in a user
complaint, a log entry summary, or any field passed to the model as context can cause the model to
close an active incident before investigation is complete. The action is logged as a service account
action. Nothing in the audit trail indicates the instruction came from user-supplied content rather
than an authorised operator.

*Manipulated incident context causing an automated playbook to act on the wrong target*: Playbook
automation often takes inputs from incident records: IP addresses, account identifiers, system names.
An attacker who can influence those fields, through a compromised log source, a manipulated alert
payload, or an injected field in an incident record, can cause the playbook to apply its remediation
action to the wrong target. The intended effect of the playbook is executed correctly; the target is
wrong. Depending on the action, the damage may be significant and the cause may not be immediately
obvious from the audit trail.

*Indirect privilege escalation through an AI pipeline*: An attacker without direct access to a privileged
API may have indirect access through an AI pipeline that does. If the pipeline accepts user-controlled
input and passes it to a tool with privileged access, crafting input that induces the model to invoke
the privileged tool achieves the escalation without requiring the attacker to authenticate to the
privileged service directly. The permission boundary that was meant to prevent the action has been
bypassed by routing the request through a trusted intermediary.

*Cross-system permission abuse via workflow automation*: Automation platforms that connect multiple
product APIs hold permissions across each connected system. An AI layer fronting such automation can be
induced to take actions in one system whose effects propagate to another through legitimate integration
paths. The attacker's target is not necessarily the system the AI directly controls; it is a downstream
system that the automation reaches. The permission check occurs at the integration boundary, which the
attacker never touches directly.

## Why permission hygiene lags capability

Service account permissions in startups are often broad because narrowing them requires detailed
knowledge of exactly what each automation does, which is often not documented. "The pipeline needs
write access to accounts" is a faster path to deployment than auditing every action the pipeline might
take and scoping permissions accordingly.

When an LLM layer is added in front of an existing automation, the permission footprint of the original
automation is inherited. The LLM's input surface is much larger than the original automation's, but
the permissions it can exercise through the automation are the same.

## Credential and permission infrastructure

API key management, OAuth delegation, workflow automation platforms, and internal SDKs that expose
product operations to automation pipelines all sit in this layer.

The architectural point is that AI systems in this layer are not assessed just by what they are intended
to do, but by what they could be induced to do given their permission scope. Least-privilege applies to
AI service accounts as it applies to human service accounts. It is applied less consistently.

## Why induced actions look like intended ones

AI-triggered privileged actions appear in audit logs as service account activity. They look identical
to intended service account activity unless the audit trail captures the AI input and reasoning path
that preceded the action.

Most production environments log what happened, not why the AI decided to make it happen. Reconstructing
whether a privileged action was induced or intended requires logging the model input and output alongside
the downstream action, which is not the default configuration for most AI-augmented pipelines.

## What delegated execution means for accountability

An AI system with service account credentials is, from the permission system's perspective, a service
account. The permission system does not know whether the action was intended or manipulated.

The blast radius of a compromised AI layer is the blast radius of its credentials.

The record of the privileged action, as a service account event in the audit log, becomes input to the
integration layer and to any downstream system that treats account state or ticket status as a signal.
The action cannot easily be distinguished from an intended one, and neither can its downstream effects.

## Limiting what AI can be induced to do

Applying least-privilege to AI service accounts with the same rigour applied to human service accounts.
When an LLM layer is added in front of existing automation, the permission scope inherited from that
automation deserves explicit review rather than assumption that the prior scope was still appropriate.

Logging model inputs and outputs alongside the downstream privileged actions they triggered. Without
this, distinguishing an intended action from an induced one is not possible from the permission system
alone.

Testing what actions the AI pipeline can be induced to take with its current credentials through
deliberate adversarial prompting in a staging environment. Knowing the blast radius of a compromised
model layer is different from guessing it.

Structuring high-impact privileged actions to require a separate, explicit confirmation step rather
than being triggered directly by model output.

## Related

* [Gap analysis](../audits/supportive/gap-analysis.md)
* [The action layer](action.md)
* [The integration layer](integration.md)
