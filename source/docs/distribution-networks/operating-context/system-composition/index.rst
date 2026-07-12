System composition
============================================

.. image:: /_static/images/distribution-system-composition.png

The stack splits cleanly into a confident half and an operational-technology heart. The confident half is well
attested from procurement, careers pages and adverts: an SAP core on Azure for enterprise and market, GE Smallworld
with Lovion and IBM Maximo for the network model and asset register, and a Landis+Gyr, Iskraemeco, Kaifa and Sagemcom
metering base over Utility Connect's CDMA network. The heart took longer to pin but now resolves: Alstom's e-terra
runs SCADA, EMS and DMS, now under GE Vernova, with e-terracontrol's own SQL Server historian. What stays open is
narrower than it was, the protection-relay maker is inferred as Siemens SIPROTEC and Schweitzer Engineering
Laboratories from engineering-tool usage rather than independently confirmed, and the OT-monitoring product is
unnamed in public sources.

.. toctree::
   :maxdepth: 1

   vendor-platform
   procurement-documents
   job-advertisements
   standards

The reason to map the stack at all is that each named tool is also an evidence store. Adverts name the tool,
procurement specifications enumerate the observables a system emits by design, and the technical standards,
IEC 60870-5-104, IEC 61850, IEC 62443 and 62351, COMTRADE and CIM, supply the a priori vocabulary for those
observables. So the composition can be read as a map of what evidence normal operation creates and where it lives.
