Threat analysis of AI in security operations
========================================================

.. image:: /_static/images/threat-analysis-ai.png

In many startups and scale-ups, security operations are not a separate SOC system sitting beside the product.
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

The attacks that target the model itself, evasion, poisoning, extraction, inference, and prompt
injection, can be found as red tradecraft in
`learned models <https://red.tymyrddin.dev/docs/through/learned-models/>`_. The defensive use of AI as a
detection method, distributed across the attacker techniques it counters rather than gathered under one
heading, can be found in the blue notes:
`behavioural detection <https://blue.tymyrddin.dev/docs/counter/evasion/behavioural-detection/>`_,
`UEBA tuning <https://blue.tymyrddin.dev/docs/counter/collection/ueba-tuning/>`_, and
`detecting AI stego <https://blue.tymyrddin.dev/docs/counter/exfiltration/detecting-ai-stego/>`_.

.. toctree::
   :glob:
   :maxdepth: 1
   :includehidden:

   input.md
   context.md
   decision.md
   action.md
   human.md
   identity.md
   feedback.md
   integration.md
   external.md
   policy.md

*Last updated: 4 July 2026*
