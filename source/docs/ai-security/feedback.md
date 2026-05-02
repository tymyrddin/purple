# The feedback layer

Machine learning models improve by learning from outcomes. In security operations, outcomes are the labels
applied to decisions: blocked, escalated, cleared, false positive. Those labels are worth shaping if you
have time and patience. Some attackers do.

## Where learning loops exist in security operations

- Fraud classifiers retrained on recent transaction outcomes. 
- Abuse detection models fine-tuned on reviewed moderation decisions. 
- Anomaly detection thresholds adjusted based on false positive and false negative rates. 
- Content classifiers updated when human reviewers override model decisions. 
- Risk scoring pipelines where outcome feedback is automatically incorporated into the next training run.

These loops are a genuine operational benefit. A model that updates on recent outcomes adapts to new
patterns faster than a static rule set. The same property that makes it adaptive makes it shapeable.

## From static rules to trainable surfaces

A static rule set fails when the rule is wrong. The failure is visible and specific: the rule fires, or
it does not. Fixing it requires changing the rule.

An adaptive model fails when the training data is wrong. The failure is not visible at any single point.
It is distributed across a retraining cycle. No individual event is anomalous. The model is doing what
it is designed to do: learning from the data it has been given.

This means the feedback layer converts a sufficient volume of shaped activity into a model update. The
attack is the training run.

The AI function here is retraining: the classifier ingests outcome-labelled events from the review queue
and produces an updated model. The concrete state change is the decision boundary itself, which shifts
in the direction of the training signal, updating future classification outputs for equivalent inputs. A threshold that cleared a certain transaction profile before
the retrain may flag it after, or the reverse, with no announcement and no audit trail pointing to why.

## How feedback loops get corrupted

*Slow-burn poisoning that shifts what the model considers normal*: A model retrained on recent outcomes
adjusts its sense of normal behaviour based on what it observes in the training window. An attacker who
generates repeated benign-looking events, none of which individually triggers review, is contributing
to the training distribution. If those events push the distribution in a particular direction, the next
model version will treat that direction as more normal than the previous version did. The effect is
proportional to volume and time, and produces no anomalous signal at any point during the campaign.

*False positive seeding to teach the model that an attack pattern is benign*: If a model produces false
positives on certain input types, human reviewers will clear those cases and label them as benign. That
label feeds back into training. An attacker who can reliably cause false positives on inputs resembling
their intended attack pattern can, over time, teach the model that pattern is safe. The human reviewer
is not making an error; they are correctly labelling a false positive. The correction itself becomes
the vulnerability.

*Classification drift through attacker-shaped transaction labels*: A fraud model whose threshold for
clearing transactions is influenced by the distribution of cleared cases will drift if that distribution
is shaped deliberately. An attacker who runs a volume of transactions designed to be cleared as
legitimate, whose profile resembles the intended fraud pattern in structurally important ways, is moving
the boundary toward their attack. The drift is not uniform; it moves in the direction the attacker
shaped it.

*Threshold manipulation across retraining cycles*: Outcome labels that cluster near the boundary between
action tiers influence where the boundary sits in the next model version. Pushing outcome labels
systematically toward the no-action side, through volume and calibrated inputs, widens the no-action
band over successive retraining cycles. The change per cycle falls within expected model variance. The
cumulative change across many cycles does not.

*Detection sensitivity reduction achieved purely through product interaction*: None of the above requires
access to the model, the training pipeline, or the infrastructure. It requires only the ability to
interact with the product at sufficient volume with calibrated inputs. The feedback loop designed to
improve the model's accuracy is the same loop that enables its degradation.

## Why training pipelines are lightly governed

Retraining pipelines in startups are often automated and lightly supervised. The pipeline runs, the
metrics look acceptable, and the updated model is deployed. Whether the training signal has been shaped
deliberately is not a question that automated pipelines ask.

Data governance around feedback labels is also often immature. Who labelled what, and whether those
labels are reliable, is not always auditable. A human reviewer who consistently clears certain input
types, because they seem low-risk based on surface features, is contributing to the training signal
whether or not their clearance decisions were sound.

## MLOps and feedback infrastructure

MLOps pipelines, model training and registry infrastructure, human review and labelling queues, and
outcome logging systems that feed back into classifier training all fall into this layer.

The relevant question for each component is: can the inputs that influence the training signal be shaped
by parties external to the organisation? For any system where user behaviour is an input to the feedback
loop, the answer is yes. The question then becomes whether the organisation monitors for the pattern
that shaping would produce.

The specific field that matters is the outcome label on a reviewed decision event in the labelling queue.
That label, assigned by a human reviewer, is the field that tells the model whether the input was
correctly classified. It is the most influential field in the retraining pipeline, and it is generated by
a process that can be shaped without accessing the pipeline directly.

## Why training signal corruption is slow to surface

Feedback poisoning does not produce anomalous signals at the event level. The events look normal. The
reviews look normal. The model metrics look acceptable. The detection window is the aggregate, across
enough training cycles to see the boundary move.

That requires monitoring model behaviour over time rather than monitoring individual decisions, which
is a different operational discipline and a less common one.

## What a trainable system means for durability

A model that learns from outcomes can be taught the wrong lessons by someone willing to invest the time
to teach them.

The feedback layer is not a distinct attack surface in the sense that input injection is. It is a slow
corruption of the surface itself.

## Protecting the learning loop

Monitoring classifier decision distributions across retraining cycles, not only point-in-time accuracy.
Gradual boundary drift is only visible in aggregate, across multiple cycles, with a baseline to compare
against.

Version-controlling deployed models and maintaining the ability to compare decision boundaries across
versions. A model that changed between two training runs in ways that shift how a specific input
population is classified is auditable; one that was silently updated is not.

Reviewing training signal sources periodically with attention to whether any input population is
contributing systematically to boundary drift. Automated pipelines do not ask whether the signal has
been shaped deliberately.

Including feedback loop integrity in security review for any ML pipeline that learns from
user-generated outcomes. The improvement mechanism is also the degradation path.

## Related

* [Continuous compliance monitoring](../audits/supportive/continuous-monitoring.md)
* [Risk scoring](../audits/supportive/risk-scoring.md)
* [The decision layer](decision.md)
