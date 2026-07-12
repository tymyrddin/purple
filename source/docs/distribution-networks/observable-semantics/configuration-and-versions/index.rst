Configuration and versions
============================================

Configuration and firmware are held against a stored baseline, so the signature of an unauthorised change is
divergence: the live device against its offline baseline, or a version string that does not match the record. That
makes a single-sided change easy to flag and a hidden change expensive, since an attacker has to corrupt both the
device and its baseline at once, and a later update from the engineering tool re-imposes the baseline anyway. The
standing exposure is the interval between comparisons, the window in which an unauthorised change lives before the
next check finds it.

.. toctree::
   :maxdepth: 1

   configuration-management
   firmware-and-software-versions

The baseline itself is the weak point, so the real defence is several independent baselines: an as-found-and-as-left
record stored separately, a backup repository, the vendor's master. The version string alone is only a first-order
filter, because a capable firmware compromise reports the old version while running new code; what then catches it is
behavioural anomaly, cryptographic or hash verification, and cross-checking the deployed configuration against
version-control history. Consistency across the integrated stack is a check in its own right, since when the GIS,
the SCADA and the relay disagree on the intended configuration, that divergence is the signature.
