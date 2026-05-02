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

The ten layers below map where that influence takes hold.

.. toctree::
   :glob:
   :maxdepth: 1
   :includehidden:

   layer-input
   layer-context
   layer-decision
   layer-action
   layer-human
   layer-identity
   layer-feedback
   layer-integration
   layer-external
   layer-policy
