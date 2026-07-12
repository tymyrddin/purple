Field devices and protection
============================================

Field devices keep an account of their own, independent of the control room: the RTU's I/O and state logs, the relay's
live settings, its microsecond sequence-of-events, the COMTRADE disturbance capture, and the breaker's mechanical
counter. Because they measure the same quantities locally, they are the check against a corrupted control-room picture,
a switchpoint that reports closed while the RTU shows it open, a fault the historian smoothed away that the relay
still recorded. Two of these records are especially hard to forge: the hardware-level COMTRADE waveform, whose altered
samples have to stay consistent with the physics of the fault and with the configuration, and the breaker's mechanical
counter, which needs physical access and cannot be changed remotely.

.. toctree::
   :maxdepth: 1

   rtu-behaviour
   protection-relay-state
   disturbance-and-fault-records

The recurring test is a baseline read against independent sources. Relay settings are held against a stored baseline,
and the divergence is the first signature, with no neutral category: a relay running non-baseline settings is running
the wrong settings until a work order explains it. To hide a change an attacker has to corrupt both the relay and its
baseline at once, and even then the deception surfaces elsewhere, in a relay that will not trip to a known fault, or
against an as-found-and-as-left record stored separately from the baseline. The hardest case is conditional logic, a
dead man's switch that behaves normally until triggered, and it is caught not by any single record but by pattern,
because anomalies that appear only under a specific condition read as deliberate rather than as random failure.
