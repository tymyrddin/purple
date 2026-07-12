Evidence structure
============================================

.. image:: /_static/images/distribution-evidence-structure.png

Between them, open code and conference material make the form of the evidence public while the content stays private.
Open repositories turn the standards' taxonomy into inspectable files, a full IEC 61850 substation model with its CILO
interlock, libiec61850's literal trigger codes, synchrophasor tooling such as openPDC, so the schema, naming and event
vocabulary of an artefact can be opened, parsed and diffed even where no specific deployment is exposed, and they
double as the corpus a parser is developed against. The Dutch tie is concrete: Alliander's Grid eXchange Fabric and the
RTE-and-Alliander CoMPAS project publish the same substation-configuration and device-integration structures in
European public code.

Conference material supplies the other half, the assembled system rather than the file: CIRED and PAC World talks are
often the one place an architecture diagram, a vendor name and a live screenshot appear together, and the Stedin
examples run to real detail, the distribution-automation rollout with its IEC 60870-5-104 SCADA link and
real-time-versus-historian split, the eSmart image inventory of more than 22,000 secondary substations.

.. toctree::
   :maxdepth: 1

   public-repositories
   utility-presentations

The conclusion is the same split, a highly legible periphery around a guarded core: everything from the standard
down to the example file is public, while what Stedin specifically ticked, enabled and retained stays inside its own
configuration.
