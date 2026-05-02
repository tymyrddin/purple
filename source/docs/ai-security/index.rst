Threat analysis of AI in security operations
========================================================

.. image:: /_static/images/ai-pipeline.png
  :alt: Eight chambers in sequence connected by pipes and belts, each lit by a single amber light source and containing a distinct object: a wax seal press, an alchemist's bubbling flask, a brass balance scale with two exits.

In most startups and scale-ups, security operations are not a separate SOC system sitting beside the product.
They are embedded inside it: authentication flows, abuse detection, fraud prevention, platform monitoring,
incident response automation, and support and trust and safety workflows.

When AI enters those flows, it sits between incoming signals, interpretation, and operational response. Each
insertion point is a place where attacker-controlled input can influence system behaviour. Not hypothetically.
In production flows that already exist.

The argument is narrow but consequential: adding AI to security operations increases attack surface because
it introduces a decision layer that is probabilistic, distributed, and shaped by untrusted inputs at multiple
stages of an operational pipeline. That is a different kind of exposure than the environments those AI systems
are meant to defend.

Ten pages map where that influence takes hold, eight forming a sequential chain, two cutting across it.

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
