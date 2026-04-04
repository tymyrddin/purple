Cloud CTF Forge feasibility study
===============================================

Cloud hacking challenges require actual API surface to be meaningful: IAM misconfigurations, overprivileged roles,
exposed storage, and service-to-service pivot paths only teach something when the participant has to interact with
something that behaves like a real cloud environment. Simulated or Docker-wrapped approximations can work for
beginner-level concepts, but fall apart at the intermediate tier.

The design state here is active. The platform assessment comes first, because it determines what the rest is
building toward.

.. toctree::
   :glob:
   :maxdepth: 1
   :includehidden:

   platform.md
   vulns.md
   design.md
   infra.md
   template.md
   safety.md
