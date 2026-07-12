Network and time
============================================

The network layer is where cross-system correlation is built or broken. IEC 60870-5-104 defines no application-level
checksum and carries commands in plaintext, so an attacker with network access can inject, modify or replay one, and
the packet capture is the most objective record precisely because it is independent of any system's own logs; a capture
that contradicts a system's log is strong evidence that one of them was tampered with. The network signatures are
concrete: an unexpected connection to an RTU's port 2404, a traffic burst at 03:00 against a quiet baseline, a command
the RTU answers for the wrong device.

.. toctree::
   :maxdepth: 1

   communications-evidence
   timing-and-synchronisation-anomalies
   state-machine-transitions

Time is the other half, because correlation only holds while the clocks agree. Everything is meant to be
NTP-synchronised, so a lost-synchronisation entry or an unexplained manual clock adjustment just before an
unauthorised change is itself a signature, and backdating an event into a legitimate window is a known move that
independent records expose, since the grid frequency and several systems' timestamps cross-verify the true order.
State transitions tie the two together: a relay that trips with no fault in the historian, a switchpoint that
oscillates faster than a mechanism can move, a transition timestamped out of order, a work order that jumps from
Submitted to Closed, each is a change that no physical or procedural reality supports.
