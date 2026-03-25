Creating labs and environments
===============================================

Labs are prepared environments in the Montessori sense: the design of the environment shapes what can be discovered in it, and the assumptions encoded in the design determine what the learner encounters and what remains invisible. A lab that only exposes the attack paths the designer expected will produce learners who are calibrated to those paths and nothing else.

The SEM framing applies to the infrastructure as well. Attack infrastructure is a model of adversary behaviour. It encodes assumptions about operational security, about detection evasion, about how adversaries move through target environments. Those assumptions are accurate when built and drift as the threat landscape and detection capabilities evolve. Infrastructure that is not maintained as a living model becomes training for a past adversary rather than a current one.

The CTF design materials here were developed for Root-Me. The attack infrastructure materials document the IaC approach used to build ephemeral red team environments. Both sections are starting points, not finished artefacts.

.. toctree::
   :glob:
   :maxdepth: 2
   :includehidden:

   cloud/index
   iac/index