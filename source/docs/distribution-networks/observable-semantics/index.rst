Observable semantics
============================================

What evidence exists in a distribution network, and what it means. Not the internal state of the SCADA system or the
power flowing through copper, but the observable layer: logs, alerts, configuration changes, metre data, network
traffic, engineering records, equipment state transitions, and the patterns that indicate normal operation.

The expensive part of OT simulation is reproducing the physics. The comparatively cheap part is reproducing the
evidence. An abstraction layer built around observable semantics rather than vendor-specific implementations lets
a complex infrastructure be modelled without owning a substation in the back garden.

.. toctree::
   :maxdepth: 2

   control-and-command-execution/index
   field-devices-and-protection/index
   measurements-and-data-records/index
   configuration-and-versions/index
   engineering-and-change/index
   access-and-authorisation/index
   network-and-time/index
   database-and-transactions/index
