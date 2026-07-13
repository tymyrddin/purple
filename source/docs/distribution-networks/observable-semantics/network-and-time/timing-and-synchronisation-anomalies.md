# Timing and synchronisation anomalies

Clocks across the SCADA, historian, protection relays, RTUs and engineering workstations are meant to stay synchronised
via NTP (Network Time Protocol), so that events can be precisely correlated by timestamp. Clock
synchronisation failures or deliberate tampering with timestamps create visible anomalies that are forensic signatures.

## NTP synchronisation and system clocks

All systems that record events (SCADA server, historian server, protection relays, RTUs, engineering
workstations) are meant to have their clocks synchronised to UTC via NTP, pulling from a master NTP server (which
itself is synchronised to an atomic clock or GNSS). The synchronisation is usually within a few hundred milliseconds,
and the tolerance for a system's clock drift before it is considered out of sync is on the order of minutes or
more.

Normal NTP operation shows all systems maintaining approximately the same time. When events are correlated across
systems (a relay trip at time T, a SCADA command at time T, historian measurements at time T), the times are close (
within milliseconds or a second, accounting for network propagation delays). The correlation allows precise
reconstruction of sequence-of-events.

A system with a clock that has drifted significantly out of sync is observable. An engineering workstation's clock might
be several minutes ahead or behind the SCADA's clock if it is not syncing properly. The drift is visible if timestamps
from different systems are compared: a log entry on the engineering workstation shows "10:00:15" while the corresponding
SCADA log entry shows "09:59:45" (30 seconds difference). Large clock divergences (minutes or hours) are more obvious
and indicate either a serious NTP failure or a system that has been offline and its clock has drifted.

NTP logs (the logs from the NTP client/server interactions) show when systems synchronised and when synchronisation was
lost. If the SCADA's NTP logs show synchronisation was lost for an hour at the exact time when unauthorised
modifications were made, that timing is suspicious. Without NTP synchronisation, a system's clock can be manually set to
any value, and an attacker could use this to manipulate event timestamps.

## Timestamp manipulation and evidence ordering

Event timestamps serve two purposes: they allow correlation between systems, and they establish a definitive ordering of
events. If event A occurs at 10:00:00 and event B occurs at 10:00:05, then A preceded B. Manipulating timestamps can
reverse this order or create artificial gaps.

Backdating leaves a signature. When a system's clock has drifted and is manually adjusted, the adjustment is recorded in
the system logs and might be explainable. But if there is no explanation for the clock adjustment, and timestamps show
events being recorded at times that contradict other systems' clocks, timestamp manipulation is suspected.

Forensic recovery of true timestamps relies on independent corroboration. If multiple independent systems recorded an
event, the timestamps from all systems provide cross-verification. If the SCADA records an event at 10:00:00 UTC and the
protection relay records the same event at 10:00:25 UTC (25 seconds difference), and the historian shows measurements
consistent with the event at 10:00:00 UTC, the SCADA and historian timestamps are more credible than the relay's
timestamp. The relay's clock may have been drifting or manually adjusted.

## Event ordering and cascade timing

When a cascade failure occurs (a fault triggering protection, which causes a switchpoint to open, which redistributes
load, which may trigger secondary protections), the precise timing of each transition is observable. The fault appears
in the historian measurements, the protection relay detects and responds, the switching command is issued, the
switchpoint responds, and the load redistribution is visible in measurements. The whole sequence takes
milliseconds to seconds.

An anomaly would be if the sequence is reversed (a switchpoint opens before a protection relay detects the fault), or if
the timing is implausibly long (20 seconds between a protection relay detecting a fault and the switchpoint opening,
when the expected response time is less than one second). Such timing anomalies indicate either system malfunction or
deliberate manipulation of logs.

Similarly, if two independent protection relays are protecting the same fault point (providing backup protection), they
detect the fault within milliseconds of each other. If one relay is recorded as detecting the fault five seconds
before the other, and no explanation exists for the delay (one relay's settings have a longer detection time), that
timing anomaly stands out.

## Clock-speed anomalies and frequency shifts

The systems record frequency (the AC grid frequency, nominally 50 Hz in Europe). Frequency is a direct observable
property of the grid's physical state and is independent of any system's internal clock. A system's clock speed can be
inferred from the frequency measurements it records: if a system is recording frequency as stable at 50 Hz while other
systems record frequency oscillating between 49.5 Hz and 50.5 Hz, the first system's clock (and its timestamp recording)
may be running slow or fast.

In forensic analysis, if a system's recorded timestamps are questioned, the frequency measurements can provide
validation. A system that is recording timestamps but its frequency measurements are implausibly smooth or constant is
suspect.

## Synchronisation logs and NTP audit trails

The NTP clients log successful synchronisations and synchronisation failures. An NTP log that shows
synchronisation was lost at a critical time (during or just before unauthorised work) is forensic evidence. The log
might show: "Lost synchronisation with primary NTP server at 23:45 UTC", followed by "Manual time adjustment at 23:52
UTC", followed by "Resynchronised at 00:15 UTC". Such a log entry indicates the system's clock was not synchronised, was
manually adjusted, and then was resynchronised.

Compromise of NTP itself (a service reporting incorrect time) would be visible in audit logs: the NTP process showing
unusual resource usage or unusual log entries, or the configuration pointing to an unexpected time-server.

## Multi-system timestamp correlation

For forensic reconstruction, timestamps from multiple independent systems are correlated. A protection relay's COMTRADE
file (disturbance record) contains high-resolution timestamps showing exactly when the relay measured a fault. The
SCADA's log shows when the relay issued a trip command. The engineer workstation's log shows when the engineer connected
to the relay. The historian shows measurements at each of these times.

If all the timestamps align (the relay's COMTRADE shows a fault at 10:00:00.000 UTC, the SCADA log shows the trip signal
50 milliseconds later at 10:00:00.050 UTC, the historian shows the measurements supporting the fault at 10:00:00 UTC),
then the timestamps are internally consistent and credible.

If there are divergences (the COMTRADE shows a fault at 10:00:00 UTC, but the SCADA log shows the trip signal an hour
earlier at 09:00:05 UTC), then something is wrong: one of the systems' clocks was wrong, or one of the logs is
falsified.

## Granularity and precision in timestamps

Different systems record timestamps at different precision levels. The historian samples its time-series to sub-second
resolution (a reading every 100 milliseconds to one second), the SCADA journal stamps events to millisecond precision,
and a protection relay's COMTRADE file records at microsecond precision. When correlating timestamps, each system's
precision sets what a match can prove.

An impossibly high-precision correlation (claiming that two events occurred at exactly the same nanosecond when the
systems only record to millisecond precision) is a red flag suggesting that timestamps have been artificially aligned in
logs. Realistic correlations account for the precision limitations: two events recorded by different systems are
considered synchronised if their timestamps agree within the precision of the less precise system.

## Daylight saving time and time zone handling

The operator works across time zones (though most operations are in the Netherlands, which uses CET/CEST). Time zone and
daylight saving time transitions are potential sources of timestamp anomalies. Systems that are not properly configured
to handle timezone changes can record timestamps that are off by one hour at the instant of the transition.

If a daylight saving time transition occurred (typically in March and October in Europe) and a system's recorded events
show a one-hour gap or duplication at that moment, the system failed to properly handle the transition. This is a system
configuration issue, not evidence of tampering, but it does mean that timestamps around the transition time require
careful interpretation.

A DST-related discrepancy is evident in multiple systems' records: if only one system shows a DST-related timestamp
error, that system is misconfigured. If all systems show the same error, it indicates a common configuration issue.

## File metadata as corroborating evidence

For critical investigations, obtaining the original raw logs (not copies, but the original files from the systems, with
their metadata intact) is essential. File timestamps, modification times, and creation times are additional sources of
evidence. A log file that shows a modification date later than the events it contains indicates the file was edited
after the events were recorded.

*Last updated: 13 July 2026*
