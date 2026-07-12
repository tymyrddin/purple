# Protection relay state

Stedin's protection relays, inferred as SIPROTEC 5 and SEL-451 but not independently confirmed, record their own state continuously: thresholds, pickup settings, protection
function status, fault records, event logs, and breaker trip counts. The relay is a second independent observer of the
distribution network, and its logs are the primary forensic source for protection behaviour. Its record shows how
relay baselines are maintained, what state divergence looks like, and how legitimate maintenance reads differently from
unauthorised modification.

## Relay settings as a baseline

Each of Stedin's protection relays is configured with specific settings: thresholds for overcurrent, overvoltage,
underfrequency, and other protection functions, pickup settings that define the sensitivity of detection, and time
delays that prevent nuisance trips. These settings are stored in the relay's non-volatile memory (flash or EEPROM) and
are accessed through engineering tools (DIGSI 5 for SIPROTEC, AcSELerator QuickSet for SEL). Stedin maintains a baseline
of the settings each relay is meant to run, typically stored in a configuration repository on an engineering
workstation or a centralised database.

Normal relay operation means the settings stored in the relay match the baseline stored in Stedin's engineering system.
Periodic maintenance includes connecting to relays and performing an online-versus-offline comparison: the
engineering tool reads the current settings from the relay and compares them line by line against the stored baseline. A
match means the relay is running the expected configuration. Any divergence is documented, investigated, and corrected.
The baseline itself changes only through documented maintenance: when a relay is upgraded, when network topology changes
require different protection logic, or when the protection strategy evolves. Each such change is recorded with a
timestamp, a user ID, a work order, and often an as-found-and-as-left record documenting the old and new settings.

The baseline-maintenance practice is so fundamental that it is assumed in Stedin's operational procedures and in the
vendor documentation. The SIPROTEC and SEL manuals describe the settings files, the versioning, and the comparison
process. The maintenance procedures reference this baseline as a matter of course. The assumption is that any
divergence between the relay and the baseline is either evidence of a legitimate maintenance change (documented in a
work order) or evidence of unauthorised modification. There is no neutral category: a relay running different settings
than its baseline is running the wrong settings, and the fact of the divergence demands explanation.

## Trip records and state transitions

Each Stedin relay continuously monitors electrical quantities (current, voltage, frequency) and records the instant when
a measurement crosses a configured threshold. The relay's event log captures these trip events with microsecond
precision: the measurement value, the threshold that was exceeded, the protection function that detected it, and whether
the relay issued a trip signal to open its associated breaker. On SEL relays the Sequential Events Recorder (SER) captures user-defined logging points, triggers the engineer
configures to record specific points in the relay's decision logic; SIPROTEC relays keep an equivalent event log of
protection pickups, trips and setting changes. The number of points and the buffer depth vary by model.

Normal relay operation includes a predictable frequency of protection events. A relay protecting a high-load feeder may
trip once or twice a year due to legitimate faults (a tree branch on a conductor, a cable joint failing under thermal
stress). A relay protecting a low-load feeder may trip once every several years. The baseline is the expected rate for a
given feeder and network condition. When fault frequency spikes (a relay that normally trips annually suddenly trips
three times in a week) it can indicate either an equipment degradation problem (a cable joint that is failing
intermittently) or an external cause (unusual weather, network stress from nearby equipment failures). The signature is
the pattern, not any single trip.

Unauthorised or anomalous trips appear in the log as trips that do not match the field condition that would have caused
them. If a relay trips on overcurrent but the relay's measurement log shows it was below the configured threshold, the
relay's logic or settings have been modified. If a relay's event log shows it issued a trip signal but the associated
breaker's independent mechanical records show it did not trip, there is a communication or logic breakdown. If a relay
begins tripping in response to a specific sequence of events (for example, every time voltage briefly dips below 90
per cent of nominal), and that sequence never occurs in Stedin's normal operation, the relay may be running conditional
logic (a "dead man's switch" in compromised firmware) that is triggered by an attack-specific condition.

## Settings divergence and baselines

The core forensic signature for relay compromise is a divergence between the relay's actual settings and the expected
baseline. Standard maintenance is to perform an online-versus-offline comparison: DIGSI 5 or AcSELerator
QuickSet connects to a relay, reads the current settings, and compares them against the stored baseline. A mismatch is
immediately visible: a threshold value that is different, a protection function that is disabled when it is meant to be
enabled, a time delay that is longer than configured. The comparison tool often highlights divergences in red.

A divergence has three readings, and telling them apart is the whole task. It can be legitimate maintenance, the work
order and the as-found-and-as-left record documenting the change and the settings matching what they say. It can be a
stale baseline, where an earlier maintenance changed the relay and nobody updated the stored copy, a process failure
rather than an attack, fixed by re-recording the baseline. Or it can be an unauthorised change: no work order, no
documentation, settings that no known maintenance explains. Only the last is a compromise, and until someone checks the
paperwork it looks exactly like the second.

A comparison that shows a clean match does not fully exclude compromise. If both the relay and its stored baseline were
altered together, the online-versus-offline comparison agrees while the relay runs the wrong logic. That case surfaces
elsewhere: the relay operating anomalously under field conditions, or an independently held as-found-and-as-left record
from the previous maintenance showing the current settings diverge from what was recorded.

## Relay-specific evidence from configuration files

DIGSI 5 stores SIPROTEC relay configurations in project files with a specific format and versioning. These files are
timestamped, versioned (through Git or a similar system at Stedin), and often backed up. When an engineer loads a relay
configuration from a relay into DIGSI 5, a temporary file is created and can be compared against the stored baseline.
The comparison not only shows what settings are different but often shows when they were last modified (some project
file formats embed timestamps in the configuration). AcSELerator QuickSet similarly maintains project files for SEL
relays.

The engineering workstation's connection logs record every time DIGSI 5 or AcSELerator QuickSet connected to a relay,
what was read (a settings upload from the relay) and what was written (a settings download to the relay). This log is
typically stored in the tool's session history or in Windows event logs on the engineering workstation. An unexpected
connection to a relay outside documented maintenance windows is a red flag. A connection that results in a settings
write (a download to the relay) without a corresponding work order is particularly suspicious. If Stedin's engineering
workstation logs show that DIGSI 5 connected to a specific relay at 03:00 and wrote new settings, and no maintenance
work order documents this activity, unauthorised configuration occurred.

The challenge is distinguishing legitimate maintenance from unauthorised activity in the connection logs. If the logs
show a connection at 03:00 but Stedin's storingsdienst (fault-duty rota) was handling an emergency at that relay (a
field device failed and the relay settings had to be temporarily modified to work around the failure), the 03:00
connection is explainable. If there is no documented emergency and the connection is unexplained, it stands out. The
resolution depends on cross-referencing the engineering workstation logs against the incident records and work
orders.

## Disturbance records and oscillography

SIPROTEC 5 and SEL relays also capture disturbance data in COMTRADE format: a high-fidelity waveform of current, voltage
and frequency at the instant of a trip. It is the hardware-level record of what the relay measured, and the most direct
check on whether a logged trip corresponds to a real fault. A relay whose event log shows an overcurrent trip while its
COMTRADE shows current below threshold has faulty or altered measurement or logic. A missing COMTRADE for a trip that
would normally have generated one is the other tell.

## Breaker mechanism records

Stedin's protection relays are typically paired with circuit breakers or recloser devices that actually open the circuit
when a trip signal is issued. These breakers have mechanical counters and electronic records of their operation: how
many times they have opened, when each opening occurred, the duration the breaker was open, and the mechanical stress
accumulated. Older breakers have mechanical counters that physically increment; newer ones have electronic counters in
addition to the mechanical ones.

A relay's trip record corresponds to a breaker's operation record. If the relay's event log shows it issued a trip
signal at a specific instant, the breaker's log shows it opened at approximately the same instant (with a small
delay for signal propagation and mechanical actuation, typically tens to hundreds of milliseconds). A mismatch between
the relay's trip record and the breaker's opening record is evidence of communication failure, logic corruption, or
relay-breaker mismatch.

The mechanical counter on the breaker is a simple and direct piece of evidence: it cannot be remotely modified (it
requires physical access to the breaker), and it is independent of any electronic system. If the relay claims to have
issued fifty trip signals but the breaker's mechanical counter shows only ten openings, something is wrong: either the
relay is falsifying trip records, or the relay did not actually send trip signals despite what its event log shows. The
discrepancy is the signature. Conversely, if the breaker's mechanical counter shows significantly more operations than
the relay's trip log, the breaker may have been operated manually (by field technicians pulling the breaker open) or the
relay's event log is incomplete.

*Last updated: 12 July 2026*
