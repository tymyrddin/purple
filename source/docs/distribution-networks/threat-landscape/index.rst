Threat landscape
============================================

.. image:: /_static/images/distribution-threat-landscape.png

Reading threats to critical infrastructure at distribution scale from the defender's side: not what an attacker would
set out to do, but what those actions leave in the observable record, and what a defender can look for.

Threat models for distribution networks account for scale, cyber-physical coupling, regulatory constraints, and the
gap between what an attacker might theoretically do and what they can actually do given organisational reality. A
threat that looks elegant on paper may be impossible in practice because the configuration that enables it violates
a safety interlock, or the maintenance window it requires doesn't exist, or the operator has a union rule against
that kind of simultaneous work.

So the through-line is not the catalogue of what could happen but the harder question underneath it: given a record,
what tells deliberate compromise apart from mismanagement, operator error, or a cascade that simply ran its course?

.. toctree::
   :maxdepth: 2

   threat-actors-and-capabilities/index
   attack-surfaces/index
   procedural-threats/index
   observable-signatures/index

Throughout, the protection-relay estate is taken as Siemens SIPROTEC and Schweitzer Engineering Laboratories, inferred
from engineering-tool usage (DIGSI and AcSELerator) rather than independently confirmed by a procurement or vendor
source. The historian is e-terracontrol's own SQL Server historian.
