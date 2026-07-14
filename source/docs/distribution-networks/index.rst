Distribution networks
============================================

.. image:: /_static/images/distribution.png
  :alt: A vast underground network of pipes, cables, and tunnels beneath a city, with junction boxes, monitoring equipment, and control stations at intervals. The network stretches into darkness in all directions.

This is a fictional distribution system operator, but not an invented one. It is assembled from open-source intelligence
about a real Dutch operator, its vendors, procedures and constraints drawn from job adverts, procurement records, vendor
manuals and annual reports into one company with real problems. Its job is to keep electricity and gas flowing from the national
grid to the last mile, at a scale where the work is cyber-physical: a protection relay opening fifty milliseconds early
is the difference between a contained fault and half a feeder gone, regulation and safety do not bend, legacy equipment
refuses to retire, and budgets rarely stretch to doing things properly. Every substation, relay, RTU, SCADA server and
historian leaves a trace as it runs, and defending the estate turns on knowing what that trace looks like when the
system works as designed, and what changes when something goes wrong or someone is moving quietly through it.

The evidence is the point, and it works two ways. Read through a defender's lens, it shows what each system emits and
where a legitimate change and an intrusion part company. In a testbed, it is what gets reproduced, not the physics
behind it, a distribution estate to interrogate without a substation in the garden. And it opens a question the record
has to answer: NIS2 asks an operator to say, inside a day, whether an incident is suspected to be malicious, which
presupposes the estate can tell a malicious change from its legitimate twin at all. Evidentiary capability is that
precondition, a property of the record measurable before anything happens.

Observable infrastructure:

.. toctree::
   :maxdepth: 1
   :includehidden:
   :caption:

   operating-context/index.rst
   threat-landscape/index.rst
   observable-semantics/index.rst

Evidentiary capability?

.. toctree::
   :maxdepth: 1

   evidentiary-capability
   evidentiary-capability-core-design
   evidentiary-capability-as-audit
   evidentiary-capability-as-training

Building the design:

.. toctree::
   :maxdepth: 1

   simulation-substrate
   feasibility

Open questions, caveats, and risks:

.. toctree::
   :maxdepth: 1

   evidentiary-capability-limits

*Last updated: 12 July 2026*
