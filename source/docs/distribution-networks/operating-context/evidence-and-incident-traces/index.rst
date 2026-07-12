Evidence and incident traces
============================================

.. image:: /_static/images/distribution-evidence-and-incident-traces.png

The central finding is a gap between what a conformant system is supposed to record and what actually survives an
incident. The DFIR literature is candid that ICS devices lack forensic-grade logging, that engineering traces are
tool-mediated and device-heterogeneous, and that the richest residue sits on the engineering workstations and in the
tool logs rather than on the device, thinner and more workstation-resident than the standards imply. The incident
record is the empirical companion to that claim: the 2022 Flevoland event, the GB 2019 report, the ENTSO-E Iberia
panel, TenneT's running fault log and the Ukraine 2015 attack show, at the level of the relay that operated and the
frequency that fell, what utilities actually capture and publish as a matter of routine.

.. toctree::
   :maxdepth: 1

   incident-analysis-and-forensics
   video

Video adds the one layer the written record omits, the embodied sequence of which screen, which soft-key and which
physical handle, in what order, and which action the system refuses. The generic workflow is on film in abundance,
relay testing, evidence retrieval through DIGSI, commissioning interlock checks and control-room walkthroughs, while
the specific switching sequence and the e-terra screens stay inside the control room. The two halves make one point:
the standard describes the intended record, and the material trace that remains is consistently less than
the paperwork promises.
