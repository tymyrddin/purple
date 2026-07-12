Measurements and data records
============================================

The historian and the metering stream are the time-series record, and their tells are statistical. Real measurements
are noisy and follow daily and seasonal cycles, so a curve that is impossibly smooth, or a consumption profile that
departs from a customer's established pattern, signals synthetic or altered data. An edit to a stored value is caught
two ways: by the archive's own edit audit trail, and by disagreement with records the historian does not control, the
relay's capture, the RTU's log, the physical state. The live current-value cache is no help here, since it holds only
the latest value and offers no second copy of the past to reconcile against.

.. toctree::
   :maxdepth: 1

   historian-patterns
   metre-data-semantics

Metering adds an accounting cross-check the process layer cannot: the sum of the meters on a feeder tracks the RTU's
measurement of what flowed into it, and a persistent gap is the signature of under-reporting, theft, or a mismeasuring
RTU. Tampering can sit at the meter, in CDMA transit, or at the platform, and each leaves a different footprint, an
individual meter out of line with physical verification, a whole concentrator moving together, or a platform audit-log
edit. The sharpest illustration is a real one: in an ACM meter-reading dispute it was Stedin's handwritten logbook of
physical read attempts that settled the question, the paper record carrying what the platform data could not.
