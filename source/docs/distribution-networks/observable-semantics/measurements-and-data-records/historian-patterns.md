# Historian patterns

The portrait's e-terra SQL Server historian records time-series process data: voltage, current, frequency, load, temperature, and
thousands of other measurements flowing from the distribution network into the control centre at high frequency (
typically one to ten samples per second). The historian is also a transaction database with edit-audit records. Its
patterns show what normal time-series data looks like, what tampering leaves behind, and how a legitimate data
correction reads differently from compromise.

## The time-series baseline

The distribution network exhibits predictable electrical patterns that appear in the historian. Voltage follows a
daily and weekly cycle: lower at night when demand is low, higher during the afternoon peak. Current reflects load:
lower at night, spiking during morning and evening peaks. Frequency shows network stress: it dips when large generators
trip offline or when demand spikes, and rises when generation exceeds load. Across seasons, summer usually shows lower
baseload (fewer space heaters in use), while winter shows higher consumption and more volatile demand.

A specific feeder or substation develops its own pattern based on what customers it serves. A residential feeder shows a
sharp morning peak (07:00-09:00) as people start showers and make breakfast, a dip midday, then an evening peak (17:00-20:00). An
industrial feeder shows demand that follows the factory's operating hours, flat and steady from 06:00-18:00, dropping
to almost zero at night. A mixed residential-commercial feeder shows layered patterns: the residential spike in the
morning, the commercial load adding throughout the day, and both dropping in the evening. These patterns are so
consistent that a skilled operator can look at the historian graphs and immediately see if a feeder is behaving
normally.

The historian baseline is constructed from weeks or months of historical data. The mean voltage for each hour of the day
is calculated, and the variation around that mean is quantified. Same for current, frequency, and other measurements.
When new data arrives, it is checked against the baseline to detect anomalies. A voltage reading that is two standard
deviations outside the expected range for that hour of the day triggers an alarm. When a protection relay trips, the
historian shows the pattern of measurements just before the trip, the instant of trip (a sudden change in voltage and
current), and the pattern just after (the faulted section is isolated, load transfers to alternate feeders). The
pre-fault, during-fault, and post-fault patterns are the signature of a legitimate protection event.

## Data editing and audit trails

The historian is a database that stores measurements as time-series records, and it is a transactional database
where changes are logged. An authorised operator or engineer can correct a value in the historian if the measurement was
erroneous (a sensor failed and reported wildly wrong values, and someone later corrected the record). When a value is
edited, the historian logs the edit: who edited it, when, what the old value was, what the new value is. This audit log
is stored in a separate audit database that is not normally accessed by the main historian queries but is available for
forensic review.

Normal corrections are rare and small. A sensor malfunctions for a few seconds and records implausible values (voltage
at 9999V, indicating a data overflow). An engineer notices this when reviewing the data, flags the bad values, and
corrects them. The historian's audit log shows a cluster of edit entries, each one corresponding to one of the bad
values, all made at the same time by the same user, with an annotation ("Sensor malfunction correction"). The corrected
values are set to the last known good value or interpolated from surrounding correct values.

Unauthorised editing is distinguished by its pattern. A single measurement value is changed from 240V to 280V without a
detectable reason, and no corresponding sensor malfunction or correction note exists. Multiple values spread across
different time periods are changed consistently (all overload alarms are reduced by 10 per cent, or all voltage dips are
smoothed out). Edits are made at odd hours with no corresponding work order. Values are deleted rather than corrected (
the entry in the time-series is removed entirely, leaving a gap in the data). Most tellingly, edits are made to values
that correspond to times when anomalous events occurred (the measurements just before and after a protection relay trip
are edited, removing evidence of the fault condition).

## Detecting archive edits

The historian keeps its archived history separately from a live current-value cache. That cache holds only the latest value of each point, not a queryable history, so it offers no independent second copy of the past to reconcile the archive against. Detecting an altered historical value rests on two things instead: the archive's own edit audit trail, and agreement with records the historian does not control.

The archive logs edits to stored values: the editing user, the timestamp, the old and new value, and an optional annotation. Whether that logging happens at all depends on the product and its configuration: some historians record every value edit, others only administrative actions, and where value-level auditing is off or absent a modified reading leaves no on-system trace, throwing detection onto the external check. A legitimate correction appears as a cluster of edits carrying an annotation and matching a
documented work order. An edited value with no corresponding audit entry, or an audit trail that has itself been
truncated, is the on-system signature of tampering. Edit timestamps carry their own tell: a cluster of edits at the same instant to the millisecond, or edits made when the historian would not normally be written to, reads as automated tampering rather than an operator's hand-correction. The stronger check is external. A stored value that no longer
agrees with the relay's COMTRADE capture or the RTU's own log has been changed, whatever the audit trail says. If the
archive shows a smooth, constant voltage (240V with no variation for an entire day) while the relay and RTU records for
the same feeder show the ordinary variation of a live network, the archived history has been overwritten with synthetic
data.

## Measurement consistency across independent systems

The distribution network has multiple independent measurement sources. The RTUs measure voltage and current at
their locations and report via IEC 60870-5-104. The protection relays measure the same electrical quantities locally and
record their measurements in their own event logs and disturbance records. The historian receives the RTU measurements
and stores them. When a fault occurs, the protection relay measures it, trips, and records the fault condition. All of
these measurements of the same electrical quantity at the same location are meant to agree.

A voltage dip on a feeder is visible in multiple places simultaneously: the RTU at that feeder records a
voltage drop, the protection relay records it (if the dip triggers protection logic), and the historian
records the RTU's measurement. If a fault occurs, all three show the same approximate instant of the fault. If the
historian shows a voltage dip at 10:00:00 UTC but the protection relay's disturbance record shows the dip occurred at
10:00:05 UTC (five seconds different), something is inconsistent. The mismatch is either evidence of a
clock-synchronisation problem (the systems are using different times) or evidence that one of the records has been
edited.

Cross-checking the historian against relay disturbance records is a powerful forensic technique. A relay's COMTRADE
file captures the waveforms at the instant of a fault, and the historian shows the same measurements at the same
time. If the two disagree, one of the records is false, and the COMTRADE capture, being harder to forge, is usually the
more trustworthy source.

## Synthetic data and unnatural smoothness

A time-series of real measurements is noisy. Voltage varies by a few volts second to second due to load fluctuations and
reactive power. Current varies with customer load changes. Frequency drifts by fractions of a Hz as the grid is
stressed. Real data has natural variation; synthetic data or smoothed data often does not. If a historian query returns
a time series that is suspiciously smooth (voltage at exactly 240.00V for hours with no variation, or current showing a
perfectly linear increase with no noise), that pattern indicates the data may be synthetic or heavily filtered.

A legitimate data-smoothing scenario occurs when an operator notices a sensor failure (a sensor reporting implausible
values) and manually corrects the time-series by replacing the bad values with synthetic estimates. If a
current sensor fails and reports zero current for an hour when actual current is nonzero, an operator might replace the
bad data with interpolated values based on surrounding correct data. This correction is documented: the audit log
shows a cluster of edits at the same time with an annotation indicating sensor correction.

An illegitimate scenario occurs when the historian is edited to hide evidence. If a fault condition existed
that the historian originally recorded, but the historian is later edited to remove or smooth out the evidence of the
fault, the edited values would appear suspiciously smooth (all fault-related measurements replaced with constant
baseline values, or a fault period replaced with an interpolated smooth transition). The difference between legitimate
correction and illegitimate editing is context: a legitimate correction is rare, documented, and affects a small time
range (seconds to minutes of bad data); an illegitimate edit affects larger time ranges (hours to days) and is
not documented.

## Event patterns and cascade analysis

The historian contains not just continuous measurements but also discrete events: timestamps when alarms are raised,
when relays trip, when operators acknowledge alarms. These events correlate with the continuous measurements.
When a relay trip event is recorded, the continuous measurements just before the trip show the fault condition (
overcurrent, overvoltage, or whatever caused the trip). When an operator acknowledges an alarm in the SCADA, that event
appears in the historian.

Normal cascade patterns are understood. When a high-voltage line trips, it redistributes power to alternate lines, which
then show increased current. Those lines may hit overload alarms (which are recorded as events), and if the current
exceeds the protection threshold, those protection relays may trip, further redistributing power. The sequence of events
and measurements forms a coherent picture: trip, redistribution, alarm, potential secondary trip.

Anomalous patterns appear when the cascade does not follow expected physics. An event records that a relay tripped, but
the measurements just before show no detectable fault condition that would trigger the relay's settings. An alarm is raised
but there is no corresponding measurement change. A cascade sequence occurs but in an unusual order (a secondary relay
trips before the primary one, which is backward). Events are recorded but measurements do not support them. These
mismatches are signatures of either data tampering or serious equipment malfunction.

## Time synchronisation and clock skew

Cross-checking the historian against other systems only works while their clocks agree. A historian timestamp that
disagrees with the relay's COMTRADE (which carries its own clock) and the RTU's event log for the same event points to
a synchronisation problem or to deliberate backdating, and the NTP logs show whether synchronisation was holding
at the time.

## Correction or cover

Every edit on this layer wears the same shape as a legitimate one, because the legitimate one is common: a failed sensor
is corrected, a cluster of bad values replaced with interpolation, all annotated and tied to a work order. The
illegitimate edit is that act without the context, unannotated, or spread across hours rather than seconds, or made when
the historian is not normally written to. The audit trail carries that distinction where value-level logging is on;
where it is off, or has itself been truncated, the archive cannot be trusted to indict itself, and the decision moves to
records the historian does not control, the relay's COMTRADE and the RTU's log holding the ordinary variation a real
network leaves. A smoothed archive beside a live capture that still shows noise is the overwrite, whatever the audit
trail says.

The measurements are never quiet, voltage and current vary second to second, which is why a smooth trace is suspect;
edits, by contrast, are rare, so a single unexplained one stands against an almost empty log. The two edits, side by
side:

    A STORED HISTORIAN VALUE, EDITED
    ────────────────────────────────
                    SENSOR CORRECTION         │  EVIDENCE-HIDING EDIT
    what changed    a few bad samples         │  a fault period
    span            seconds to minutes        │  hours to days
    annotation      "sensor malfunction"      │  none
    work order      present                   │  none
    edit timing     an operator's hand        │  one instant, to the ms
    external check  agrees with COMTRADE/RTU   │  archive now disagrees

*Last updated: 13 July 2026*
