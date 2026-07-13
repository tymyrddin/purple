Observable signatures
============================================

.. image:: /_static/images/distribution-threat-landscape-signatures.png

Each threat type leaves its own mark, a replayed frame as duplicate RTU commands, a raised relay threshold as baseline
divergence, an edited historian value as a gap in the audit trail or a curve too smooth to be real, an impersonated
operator as an off-shift login or two simultaneous sessions, window abuse as a work order that does not match what
changed.

A single anomaly rarely settles anything on its own; the signature that
holds up is a divergence between records that ought to agree, the control-room command log against the RTU's
received-command log, the relay's own event log against the historian, the reported state against the physically
measured one. No one system is trusted to check itself.


.. toctree::
   :maxdepth: 1

   threat-signatures

Legitimate work leaves the same marks as an attack, so the question the evidence answers is not whether something
changed but whether it was authorised, in scope and internally consistent. That pushes detection toward baselines and
established patterns rather than events in isolation, and makes the interval between checks the real exposure. It
also makes absence a form of evidence: a relay known to have operated with no record of
the operation, maintenance with no connection log, a window with no switching record. A single gap can be malfunction,
but a pattern of missing traces across systems reads as deliberate removal rather than accident.