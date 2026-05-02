# The human-in-the-loop layer

Human operators are not outside the AI pipeline in modern security operations; they are the final stage of
it. What they see, and what they conclude, is shaped by the AI summaries placed in front of them.

## Where humans meet AI-mediated reality

- Security analysts reviewing AI-generated incident summaries before investigating. 
- Trust and safety reviewers working through a queue where each item includes an AI-generated recommendation. 
- Support staff handling escalations that arrive pre-summarised by a ticket copilot. 
- On-call engineers paged with AI-drafted incident context. 
- SOC teams working in SIEM environments where alert enrichment is AI-generated. 
- Operations managers reviewing dashboards where anomaly explanations are produced by a language model.

In each case, the human is making a decision. What they are deciding on is an AI-mediated version of the
underlying signal.

## From reading signals to reading summaries

An analyst reading raw logs, events, and alerts is forming an interpretation from source data. The
interpretation may be wrong, but it is their interpretation, grounded in what they observed directly.

An analyst reading an AI-generated summary is responding to a pre-formed interpretation. The summary
already contains implicit judgements about relevance, severity, and causality. Those judgements are not
labelled as uncertain or potentially wrong; they are presented as description.

The cognitive load reduction is real. So is the cognitive anchoring effect. Analysts tend to investigate
in the direction the summary points, because that is the efficient thing to do, and because the summary
looked authoritative.

## How framing shapes investigation

*AI-generated incident summaries that omit the relevant event*: When a summarisation system condenses a
large alert payload, it makes implicit relevance judgements. An attacker who stages a surrounding context
of lower-priority events can cause the summariser to treat the actual incident as background. The analyst
receives a summary of the noise. The significant event does not appear in it, and the analyst has no
reason to go looking for what was omitted.

*False causal narratives injected via attacker-controlled input*: An attacker who can write text that ends
up in the incident context, through a support ticket, a log entry, or any user-supplied field that
reaches the summarisation layer, can introduce a misleading explanation that the AI incorporates and
presents as description. "User reports this was triggered by a routine account migration" reads as
context in a summary, not as an unverified user claim. The analyst reads the summary as an account of
what happened, not as a compilation of claims some of which came from the subject of the incident.

*Summaries expressing high confidence in a low-severity assessment*: A language model that produces a
confident, well-structured, low-severity summary is more likely to be taken at face value than one that
expresses uncertainty. Confidence is a surface feature, not an accuracy indicator. An attacker who can
influence the framing of the input can influence the confidence level of the output. Analysts working
through a high-volume queue give less scrutiny to cases that arrive with a confident low-severity label.

*Alert queues flooded with generated noise to bury real signals*: Alert fatigue is a well-documented
problem in security operations. AI-generated noise amplifies it: if the system can be induced to produce
a high volume of plausible-looking low-priority alerts, analyst attention is distributed across a larger
number of items. The real signal is still there, but it is competing with a much larger volume of
manufactured distraction. The analyst does not miss the real alert because they ignored it; they miss
it because they ran out of time before reaching it.

*Emotionally manipulative language inflating ticket priority*: Support and trust and safety queues are
often prioritised using classifiers that respond to linguistic urgency. A user who learns that language
associated with legal complaints or personal distress produces faster responses can exploit that to route
low-severity items to high-value review capacity. The capacity consumed by the inflated ticket is not
available for the cases that warranted it.

*Hypothesis anchoring from a manipulated summary*: Once an analyst has read a summary that proposes a
causal explanation, their subsequent investigation is shaped by that frame. They tend to look for
evidence that confirms or rules out the proposed explanation rather than approaching the data fresh.
An attacker who can plant the wrong explanation in the summary can direct hours of investigative work
toward a dead end, and the analyst's activity will look entirely rational given what they were told
at the start.

## Why thin teams are more vulnerable to this

Thin security teams with high operational load have a strong incentive to rely on AI assistance. When
one analyst is covering what would be a four-person function elsewhere, anything that compresses
decision time is attractive. The dependency tends to deepen quietly, without a formal decision being
made about how much autonomous weight the AI output is receiving.

The moment at which an analyst stops verifying the summary against the underlying data and starts
treating the summary as the data is difficult to identify in advance. It is easy to identify in
retrospect, after an incident where the summary was wrong.

## AI-assisted analyst tooling

LLM-powered incident summarisers embedded in SIEM and SOAR platforms, copilot features in support
ticketing systems, AI-enhanced alert enrichment, and dashboards where anomaly explanations are generated
automatically all create this dynamic.

The concern is the structural one: human review that occurs downstream of AI interpretation is not the
same as human review that occurs upstream of it. The human is reviewing the AI's reading of the situation,
not the situation.

## Why manipulated framing rarely gets caught

Manipulation through AI-mediated framing is hard to detect because the human actions that follow look
rational. The analyst investigated what the summary pointed to. The analyst escalated at the priority
the queue assigned. The analyst did not look at the underlying data because the summary was clear and
the queue was long.

Tracing an incorrect investigation outcome back to a manipulated AI summary requires deliberately
reconstructing what the summary said, what the underlying data actually showed, and where the divergence
occurred. That forensic chain is rarely assembled unless the outcome was significant enough to trigger
a formal review.

## What mediated perception costs

The attack surface extends into human judgement by way of machine-generated framing.

An analyst who is deceived directly requires a convincing lie. An analyst who is deceived via their
tooling requires a convincing summary. One of those is harder for the attacker to construct and easier
for the organisation to detect. The other is not.

## Protecting the analyst from the pipeline

Periodically spot-checking AI-generated summaries against the underlying raw data, particularly for
cases that were escalated or dismissed without further investigation. If an analyst has never found a
summary that diverged meaningfully from the source data, the check is either working or not being done.

Requiring raw data review rather than summary review above a defined severity threshold. High-consequence
decisions warrant the friction.

Logging what summary an analyst received alongside their subsequent actions. This enables forensic
review of cases where the investigation direction may have been shaped by a manipulated summary, which
is otherwise not reconstructible.

Training analysts on cognitive anchoring as part of operational security awareness. Understanding that
the first explanation encountered tends to structure investigation does not eliminate the effect, but
it makes analysts more likely to notice when they have not looked outside the initial frame.

## Related

* [Adversary persona workshop](../threat-modelling/adversary-persona-workshop.md)
* [Interview and workshop facilitation](../audits/supportive/interview-facilitation.md)
* [The input layer](layer-input.md)
* [The decision layer](layer-decision.md)
