# The decision layer

Fixed rules have a predictable failure mode: a gap in the ruleset is a gap in coverage. AI-based
classification has a different failure mode: the decision boundary is implicit, probabilistic, and can be
moved without the organisation knowing it has moved.

## Where AI makes the call

- Fraud classifiers that score transactions using gradient-boosted trees or neural networks instead of rule thresholds. 
- Abuse detection models that classify content using embeddings and fine-tuned language models. 
- Incident triage systems that use LLM reasoning to assess severity and recommend response. 
- Risk scoring pipelines that replace deterministic decision trees with probabilistic models updated on recent outcome data. 
- Automated case routing that uses model confidence scores to decide whether a case goes to human review.

Each is a legitimate operational evolution. Each creates a decision surface that can be probed, mapped, and
influenced in ways a rule list cannot.

## From rules to decision boundaries

A rule says: if X then block. The condition is explicit. Bypassing it means satisfying the condition while
avoiding the trigger, which requires finding the specific gap in the rule logic.

A classifier says: this input has probability P of belonging to class C. The boundary between classes is
determined by the training distribution, the feature space, and the model architecture. Bypassing it means
finding a region of the input space that produces a low-risk score regardless of the underlying intent,
which does not require understanding the rule; it requires understanding the model's geometry.

That is a different kind of attack surface. Rule gaps are enumerable in principle. Decision boundary gaps
are not.

## How classifiers get probed and manipulated

*Adversarial inputs crafted to score below fraud thresholds while preserving the substance of the fraud*:
A fraudulent transaction modified to match the surface features of legitimate ones (appropriate amounts,
familiar merchant categories, timing consistent with the account's normal pattern) scores differently
than the same economic intent expressed through unusual features. The fraud does not change; the packaging
does. The classifier scores the packaging.

*Near-boundary probing to map where the decision boundary sits*: Submitting variations of a transaction,
content item, or behaviour pattern and observing which variations produce which scores reveals the
approximate location of the decision boundary without requiring access to the model. An attacker who
sends twenty variations of the same action, slightly modified each time, and observes the resulting
scores or triggered responses, has effectively mapped which features move the needle. Subsequent inputs
are calibrated to sit just below the boundary.

*Inconsistent outputs across similar cases used to identify influential features*: When a classifier
produces different scores for inputs that a human would assess as equivalent, those inconsistencies
reveal which features the model is weighting. Systematically varying surface features while holding
the underlying intent constant, and observing where inconsistency occurs, identifies which features to
modify in order to shift the score. The inconsistency is not a bug being exploited; it is information
being extracted.

*LLM reasoning producing plausible-sounding low-severity assessments for staged events*: A language
model reasoning over an incident ticket does not have independent knowledge of what happened; it reasons
over the text. An attacker who controls the framing, through manipulated log entries, misleading
context, or carefully worded descriptions, can influence the severity assessment. The result is a
confident, well-reasoned-sounding output that points the analyst in the wrong direction, with no visible
sign the input was crafted to produce that assessment.

*Model confidence scores exploited to route cases away from human review*: Many pipelines use confidence
thresholds to determine whether a case goes to automated handling or human review: high confidence goes
straight through, low confidence gets flagged. An attacker who has mapped the confidence threshold can
calibrate inputs to produce high model confidence for actions that would benefit from avoiding human
review, while keeping the actual risk below the classifier's detection threshold.

## Why classifiers get adopted before they get hardened

Adopting ML-based classification is straightforward. Evaluating whether a model's decision boundaries are
robust to adversarial input is a separate discipline that many engineering teams do not have in-house.
Models are typically assessed on accuracy against a held-out validation set, not on boundary robustness
or adversarial stability.

This means the gap between "the model is accurate" and "the model is resistant to deliberate manipulation"
is often never examined.

## Classifier and reasoning tools in context

Fraud and abuse detection platforms, ML classifiers hosted internally or via API, LLM APIs used for
reasoning and triage, and probabilistic scoring pipelines that feed downstream automation all fall into this
category.

The point is not that these tools are insecure. It is that they replace a rule surface that can be audited
with a decision surface that is harder to inspect. Knowing that a classifier achieves 94% accuracy in
production does not tell you where its boundaries are or how stable they are under adversarial pressure.

## Why classifier failures look like variance

Rules fail in ways that are visible: the rule fires incorrectly, and there is an explicit condition to
examine. Classifiers fail in ways that look like normal variance. A fraud case that scored below threshold
looks identical in the logs to a legitimate case that scored below threshold. The error is only detectable
in aggregate, by someone looking for systematic boundary exploitation rather than individual case review.

LLM reasoning failures are murkier still. The output is a plausible natural language assessment. There is
no threshold to audit, no rule to inspect, and no single field that explains why the model assessed the
incident as low severity.

## What probabilistic decisions change

The attack surface on a rule system is the ruleset. The attack surface on a decision system is the decision
surface, which is continuous, multi-dimensional, and defined by training data the organisation may not have
fully characterised.

Knowing where your rules are is feasible. Knowing where your decision boundaries are under adversarial
pressure requires deliberate, ongoing testing.

The routing decision this layer produces, whether an input triggers automated action or is sent to the
human review queue, is what the action layer acts on. That boundary, not any rule list, is the surface
the attacker is trying to move.

## Hardening the decision surface

Evaluating classifiers against adversarial inputs as a distinct exercise from accuracy testing.
Accuracy against a held-out validation set and robustness against deliberate boundary probing are
different properties, and only one is typically assessed before deployment.

Logging confidence score distributions over time to detect gradual boundary drift, not only
point-in-time accuracy metrics.

Routing cases near decision boundaries to human review rather than automated action. The boundary
region is where adversarial inputs concentrate; it is also where the model's uncertainty is highest.

Treating near-boundary probing (systematic variations of similar inputs within short time windows)
as a detectable signal pattern rather than normal variance. It is the reconnaissance phase for
boundary exploitation.

## Related

* [Attack path mapping](../threat-modelling/attack-path-mapping.md)
* [Risk scoring](../audits/supportive/risk-scoring.md)
* [The input layer](input.md)
* [The action layer](action.md)
* [The feedback layer](feedback.md)
