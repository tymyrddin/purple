Observable signatures
============================================

.. image:: /_static/images/distribution-threat-landscape-signatures.png

Each threat type leaves its own mark, a replayed frame as duplicate RTU commands, a raised relay threshold as baseline
divergence, an edited historian value as a gap in the audit trail or a curve too smooth to be real, an impersonated
operator as an off-shift login or two simultaneous sessions, window abuse as a work order that does not match what
changed.

Whatever the threat, its signature reduces to one shape: a divergence between two records that ought to agree, the
control-room command log against the RTU's received-command log, the relay's own event log against the historian, the
reported state against the physically measured one. No one system is trusted to check itself. What the shape alone does
not settle is whether a given divergence is worth anything, and that turns on two things: where the corroborating record
sits, and what to make of a record that is simply not there.

Records beyond the actor's reach
--------------------------------

A divergence is only as good as its second record. The decisive one is the record the actor under suspicion could not
have rewritten as part of the act: the packet capture independent of the system's own logs, the as-found-and-as-left
report, the physical measurement, the audit trail the historian does not control. Where both disagreeing records lie
within the actor's reach, the divergence proves little, because a competent actor edits both to agree. So the real
question behind every signature is not just whether two records diverge, but whether the corroborating one is
independent of the party being investigated. A signature resting on a single record the suspect could forge is a weak
one, however clear it looks, and the same estate can hold a determination robustly against an outside attacker while
being unable to make it against an insider with write access to the record.

Absence as evidence
-------------------

The hardest signature is the one that is not there. A replay on IEC 60870-5-104 can execute without an obvious log, and
an actor can clean the audit trails behind the act, so the absence of an expected trace becomes the evidence, a relay
known to have operated with no record of the operation, maintenance with no connection log, a window with no switching
record. Absence is at once the weakest evidence and, in quantity, among the strongest. Weakest, because a missing record
is at least as likely to be ordinary malfunction, a failure to log rather than a deletion, so a single gap proves almost
nothing and a false-positive floor is built in. Strongest, because coherent removal is expensive: to erase an act
cleanly an actor has to find and delete every trace of it across systems built to record independently, and a pattern of
absence, several missing logs where operations certainly happened, is far harder to pass off as accident than any single
gap.

No signature stands alone. A divergence counts only against an independent second record, and an absence counts only as
a pattern across systems built to record apart. The mark of an attack is not any single trace but the shape of the
record around it, what agrees, what does not, and what is missing where it should not be.
