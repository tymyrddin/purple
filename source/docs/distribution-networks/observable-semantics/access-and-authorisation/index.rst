Access and authorisation
============================================

Access is the identity layer: who connected, with what authority, against which appointment, key or badge. Because a
valid credential makes an attacker's actions look authorised, the signature of compromise is deviation rather than the
action itself, an off-pattern endpoint or hour, an authority exceeded, an authentication failure followed by a success,
two simultaneous sessions, a badge recorded in two places at once. The record establishes not that something happened
but whose identity it happened under.

.. toctree::
   :maxdepth: 1

   access-control-and-key-management

The strong check is the correlation of physical and logical access. Someone physically at a substation but logged into
nothing is not doing authorised work; a badge swipe with no one on the camera means the badge was cloned or the log was
faked; an Operator role or a person without the Schakelbevoegd flag that nonetheless executes engineer-level changes
is either an access-control failure or a compromised account. Contractor and third-party access is the standing
exposure, time-limited by design and dangerous when a badge outlives the contract, which is why the physical and
logical trails carry weight only when they agree with each other.
