Cloud security
============================================

.. image:: /_static/images/cloud-security.png

Modern cloud security comes down mostly to four things: visibility problems, control-plane warfare,
automation trust, and identity-centric compromise. They overlap more than they separate. The pages that follow
work through the specific problems, from the shared-responsibility fiction that sets the terms to the one-click
blast radius that ends them.

Framing each angle as a cross-vector problem is a way of finding a place where attack and defence meet. The
attacker's tradecraft for the same ground is in the red notes on
`cloud <https://red.tymyrddin.dev/docs/in/cloud/>`_; the hardening and detection work is in the blue
notes on `countering cloud attacks <https://blue.tymyrddin.dev/docs/counter/cloud/>`_.

.. toctree::
   :maxdepth: 1
   :includehidden:

   shared-responsibility.md
   attack-surface.md
   identity-collapse.md
   metadata-abuse.md
   cicd-exposure.md
   multi-cloud-trust.md
   cloud-detection.md
   saas-dependency.md
   operational-fragility.md
