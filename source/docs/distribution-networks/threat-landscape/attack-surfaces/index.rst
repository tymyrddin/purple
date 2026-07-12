Attack surfaces
============================================

Two findings.

The telecontrol protocols and field devices were built for a trusted perimeter, not message-level
authentication: IEC 60870-5-104 carries commands in plaintext and unsigned, so an attacker with network access can
inject, modify or replay a switching command, or spoof the state that comes back. The most dangerous variants corrupt
the operator's picture rather than a single device, a false state report
that has the control room acting on a network that is not there, or dormant firmware in an RTU that behaves normally
until a trigger pattern wakes it.

The second finding is what limits all of it. Every layer, relay settings, SCADA configuration, the Smallworld model,
RTU firmware, the historian, is held against a stored baseline, so a single-sided change is flagged by
online-versus-offline comparison and a later update from the engineering tool re-imposes the baseline. To stay
hidden an attacker has to corrupt both the live device and its baseline at once, or spoof consistently across
independent records.

.. toctree::
   :maxdepth: 1

   communications-interception
   configuration-attacks
   historian-tampering
   rtu-compromise
   protection-relay-manipulation

The catch is that legitimate maintenance produces exactly the same logs, settings diffs and
connection records. What is left as the standing exposure is time: the interval between baseline checks is the window in
which a two-sided change sits undetected, and the shorter that interval, the smaller the gap an attacker has to hide
in.
