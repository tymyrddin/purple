# The rule that interprets itself

Rules enforce deterministically. Guardrails interpret probabilistically. That distinction has operational
consequences that are easy to underestimate when the system is working as intended, and hard to miss when
it is not.

## Where constraints are expressed as instructions

- System prompts that instruct an LLM what it is and is not permitted to do, relied on as a security boundary. 
- Moderation thresholds that define what score triggers a content removal. 
- Content policy classifiers that categorise inputs against defined violation types. 
- Fallback logic that routes low-confidence AI outputs to human review. 
- Guardrail layers in internal tooling that are meant to prevent AI from taking actions outside its intended scope.

In each case, the constraint is expressed as an instruction to a model that interprets it, not as a
condition enforced by a runtime that cannot be argued with.

## From enforcement to interpretation

A rule is a conditional. If the condition is met, the enforcement fires. The condition is precise and
the enforcement is not negotiable.

A guardrail is an instruction. If the model interprets the instruction as applying to the input, the
constraint is observed. If the model interprets the instruction as not applying, or if the input is
framed in a way that places it outside the scope of the instruction as the model understands it, the
constraint is not observed.

This is not a gap in specific guardrail implementations. It is a property of instruction-following
systems. The constraint is only as robust as the model's understanding of when it applies.

The AI function here is evaluation: the model assesses whether the current input falls within the scope
of the instruction-defined constraint. The concrete state change is a gate determination: an input
assessed as permitted passes through; one assessed as prohibited is suppressed or redirected. That gate
determination is the policy layer's output and the last opportunity to intercept a violation before it
reaches a user or triggers a downstream action.

## How guardrails get bypassed

*Jailbreaks that satisfy the literal content of a system prompt while violating its intent*: A system
prompt that says "do not provide instructions for harmful activities" is a constraint expressed in
natural language. The model interprets what "harmful activities" means. An input framed as academic
research, historical documentation, or fictional narrative will often produce outputs the prompt's
author would clearly recognise as a violation, because the model's interpretation of "harmful" does
not include those framings. The constraint was not circumvented; it was interpreted out of scope.

*Role-play and hypothetical framing*: Repositioning a prohibited request inside a fictional or hypothetical
context exploits the model's tendency to treat the framing as a signal about how the constraint applies.
"If a character in a story needed to explain how to do X, how might they describe it?" does not ask the
model to explain how to do X; it asks the model to generate a fictional description of someone explaining
it. Whether the constraint applies to fictional descriptions is a question about the model's understanding
of the policy, not about the policy's text.

*Policy gaps between defined categories*: Violation classifiers define categories. The space between those
categories is undefended. An input that conveys prohibited content through implication, through a
sequence of individually benign statements, through culturally specific encoding, or through context only
meaningful to a specific reader, may score below all defined violation categories while achieving the
intended effect. The classifier is not wrong; the classification space was not designed to cover that
form of expression.

*Inconsistent enforcement across model versions*: The same system prompt interpreted by different model
versions may produce meaningfully different behaviour. A constraint reliably enforced in one version may
be significantly less reliable in another, because the model's instruction-following behaviour or its
interpretation of the constraint's scope differs. An attacker who has probed multiple versions can target
requests to whichever enforces the relevant constraint less reliably, if the API allows version selection.

*Context injection that repositions the constraint's applicability*: A model that receives a system prompt
also processes the context surrounding the current request. Providing background information that reframes
the nature of the interaction can cause the model to assess the violating input as permitted under its
reading of the policy. Context that establishes the requester as a professional in a relevant field, a
researcher with stated credentials, or a user in a specific operational scenario, shifts the model's
interpretation of what the policy permits, without changing the policy text.

## Why policy layers are often retrofitted

Guardrails are often retrofitted after deployment rather than designed alongside the system. The initial
focus is on capability: does the model do what it is intended to do? Constraint robustness is assessed
later, if at all. System prompts are frequently treated as configuration rather than security controls,
updated by engineering teams without a security review process equivalent to what a rule change would
receive.

The team that writes the policy and the team that deploys the model are often different, and the
gap between what the policy intends and what the model infers from the prompt is rarely systematically
tested.

## Guardrail and moderation tooling

LLM system prompts and guardrail layers, moderation APIs, content policy classifiers, and
human-review escalation thresholds all fall here.

The architectural concern is not any specific tool. It is the nature of instruction-following
enforcement: constraints that are expressed as instructions to a model that interprets them are
different in kind from constraints expressed as conditions that a runtime enforces. Treating the
former as equivalent to the latter is the source of most guardrail failures.

## Why successful bypasses leave no trace

A guardrail bypass that succeeds quietly produces no error signal. The output looks like a normal
model response. There is no threshold that was crossed, no rule that fired incorrectly, no anomalous
log entry. The only signal is the content of the output itself, which requires someone to read it and
recognise that the constraint was not observed.

Inconsistencies across model versions or deployments are only visible through systematic testing
across those configurations. In production environments with multiple AI-assisted workflows, that
testing is rarely comprehensive.

## What interpretive constraints change about enforcement

Policy constraints expressed as instructions to a model enforce what the model understands the
policy to mean.

What the model understands the policy to mean is not fully determined by what the policy says. It is
also determined by the model's training, the surrounding context, and how the input is framed. That
makes the enforcement boundary interpretive, variable across model versions, and testable only through
deliberate adversarial probing rather than configuration review.

## Making constraints testable

Treating system prompts as security controls subject to change review processes, not as configuration.
A system prompt that defines what a model is permitted to do is a policy control; it warrants the same
review rigour as a firewall rule.

Testing guardrail enforcement systematically across category boundary inputs and common bypass framings,
not only against direct violations. The enforcement boundary is where the constraint is most likely to
fail; it is also where testing is most commonly skipped.

Having policy authors and model deployers review guardrail behaviour together against adversarial test
cases before deployment. The gap between what the policy intends and what the model infers from it is
not visible to either party working in isolation.

Testing enforcement consistency across model versions when the provider releases updates. Constraints
reliable in one version may degrade in another without announcement.

## Related

* [Gap analysis](../audits/supportive/gap-analysis.md)
* [Audit findings and reporting](../audits/supportive/findings-reporting.md)
* [The decision layer](decision.md)
