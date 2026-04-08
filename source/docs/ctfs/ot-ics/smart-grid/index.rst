Smart Grid CTF Forge feasibility study
===============================================

Smart grid challenges occupy a specific layer of the power system stack: substation automation, protection
systems, and metering infrastructure. Where the OT/ICS CTF covers generic industrial protocols, this
CTF focuses on the protocols and attack paths that are particular to the power grid.

IEC 61850 is the dominant protocol family here. DLMS/COSEM covers the metering layer. DNP3 appears in
grid contexts too, but its attack surface is documented in the OT/ICS section and cross-referenced rather
than repeated.

Platform-specific packaging pages are not yet here. They depend on simulator work that does not exist yet.

.. toctree::
   :glob:
   :maxdepth: 1
   :includehidden:

   attack-surface.md
   concepts.md
   resources.md
   feasibility.md
