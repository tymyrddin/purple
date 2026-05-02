Threat analysis of AI in security operations
========================================================

In most startups and scale-ups, security operations are not a separate SOC system sitting beside the product.
They are embedded inside it: authentication flows, abuse detection, fraud prevention, platform monitoring,
incident response automation, and support and trust and safety workflows.

When AI enters those flows, it sits between incoming signals, interpretation, and operational response. Each
insertion point is a place where attacker-controlled input can influence system behaviour. Not hypothetically.
In production flows that already exist.

The argument is narrow but consequential: adding AI to security operations increases attack surface because
it introduces a decision layer that is probabilistic, distributed, and shaped by untrusted inputs at multiple
stages of the operational pipeline. That is a different kind of exposure than the environments those AI systems
are meant to defend.

Eight layers form a sequential chain, each passing a concrete artifact to the next. The input layer
assigns a classification label. The context layer adds enrichment to produce a risk score. The decision
layer evaluates the risk score to produce a routing decision. The action layer converts that into a
state change. The human layer receives a summary and produces an escalation or dismissal. The identity
layer executes that decision through service account credentials. The feedback layer receives outcome
labels and updates the model boundary, feeding back into the decision layer. The policy layer evaluates
whether each output is permitted before it reaches a user or triggers a downstream action.

Each layer emits a named state artifact, which is usually informational (label, score), operational
(routing decision, execution event), or control-oriented (model boundary update, policy gate
determination), depending on where in the pipeline the transition occurs.

Two layers cut across that chain rather than occupying a step in it. The integration layer determines
how far a state change propagates: an error bounded in one system reaches every connected system. The
external dependency layer determines how much of the context and decision transitions the organisation
actually controls: vendor-produced scores enter the pipeline as trusted inputs from models the
organisation cannot audit.

.. toctree::
   :glob:
   :maxdepth: 1
   :includehidden:

   input
   context
   decision
   action
   human
   identity
   feedback
   integration
   external
   policy
