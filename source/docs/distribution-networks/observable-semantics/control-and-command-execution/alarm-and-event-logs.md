# Alarm and event logs

Beyond SCADA's main command and state journals, the systems generate alarm and event logs that capture anomalies,
threshold violations, and state machine transitions at granular levels. Alarms are conditions that exceed thresholds and
require operator attention. Events are state changes that are logged without necessarily triggering an alarm. The
patterns of alarms and their acknowledgement form forensic evidence of what the operators knew and when.

## Alarm thresholds and trigger criteria

The distribution network has hundreds of configured alarm conditions. An overcurrent alarm is triggered when
current exceeds a configured threshold. An overvoltage alarm triggers when voltage exceeds a maximum. An underfrequency
alarm triggers when frequency falls below a minimum. These thresholds are set based on the network's design and
operational requirements. The thresholds balance two goals: alarm often enough to catch real problems, but not so often
as to generate nuisance alarms that operators ignore.

Normal alarm behaviour shows a predictable frequency. A feeder that regularly carries near its thermal limit might
generate a few overcurrent alarms per day during peak load, which the operator acknowledges and monitors but does not
act on (normal load, not a problem). A frequency alarm might be triggered when the network is stressed (large generator
outage), and would be acknowledged and resolved when the generator restarts. The baseline is the expected alarm
frequency for normal network conditions.

Alarm suppression is a normal operational tactic. If a network section is under maintenance and will be lightly loaded,
the alarm thresholds for that section are temporarily raised or the alarms are disabled so that the maintenance work is
not interrupted by alarms. After maintenance, the thresholds are restored to normal. The suppression and restoration
are documented in the maintenance work order. An alarm that is suppressed without documentation is suspicious.

Alarm threshold changes are observable in SCADA configuration history. If a threshold has been changed (raised from
1200A to 1500A, for instance), the change is visible in version comparisons. A recent change that corresponds to no
documented work, such as a network upgrade that would require the higher threshold, is unauthorised.

## Alarm acknowledgement and operator response

Each alarm that is triggered is typically acknowledged by an operator (or acknowledged automatically if the condition
has cleared). The SCADA logs the alarm, timestamps it, shows it on the operator's display, and waits for
acknowledgement. When the operator acknowledges the alarm, that acknowledgement is logged: timestamp, operator ID, and
sometimes a text note explaining the acknowledgement ("generator tripped, recovering" or "load surge, monitoring").

Normal alarm-acknowledgement patterns show timely response: an alarm is triggered, an operator sees it within seconds (
the alert is visible on their display), and acknowledges it immediately. The acknowledgement record documents what the
operator understood about the alarm (why it happened, what action was taken or not taken). For alarms during maintenance
windows, the acknowledgement might note that the condition is expected ("planned load transfer, alarm expected,
monitoring only").

Anomalous alarm patterns include: alarms that are generated but never acknowledged (an alarm persists for hours without
an operator response), alarms that are acknowledged at unusual times (acknowledged at 03:00 when the control centre is
minimally staffed), or multiple alarms of the same type in rapid succession suggesting a degrading condition. An alarm
storm (dozens of alarms triggered within minutes) often indicates a serious fault condition or a sensor malfunction.

A specific operator's alarm-acknowledgement pattern can also be revealing. If one operator consistently acknowledges
alarms much faster than others (responding within seconds while others take minutes), they might have heightened
situational awareness or might be pre-acknowledging alarms without fully reviewing them. If an operator systematically
acknowledges alarms of certain types (all overcurrent alarms immediately, but underfrequency alarms after long delays),
that pattern reflects their priority assessment.

## Alarm silencing and notification management

The SCADA systems allow operators to silence alarms without acknowledging them: the visual alert is
dismissed but the alarm condition persists. Silencing is useful when the operator is aware of an alarm and is addressing
it, but wants to temporarily suppress the visible alert to focus on other tasks. Each silence action is logged: when it
occurred and who silenced it.

Excessive alarm silencing stands out. If an alarm condition persists but is repeatedly silenced by operators without
any corrective action, either the operators are overwhelmed and cannot address the condition, or they are deliberately
suppressing the alarm to hide the condition. A pattern of alarm silencing without corresponding corrective action during
a period when unauthorised work is occurring could indicate that alarms were suppressed to allow unauthorised activities
to proceed undetected.

## Event sequences and causal analysis

Events (as distinguished from alarms) are state changes that are logged: "Switchpoint A opened", "Transformer B thermal
sensor reported 95 degrees C", "Protection relay Q12 issued a trip signal". Each event has a timestamp and context. A
sequence of related events tells a narrative of what happened. If a fault occurs, the sequence might be: "Overcurrent
detected on feeder X", "Protection relay Q12 measured overcurrent", "Relay Q12 issued trip signal", "Switchpoint A
opened", "Load redistributed to feeder Y", "Feeder Y overcurrent alarm triggered".

Normal event sequences follow causal logic. Fault detection is followed by protection action, which is followed by load
change, which may trigger secondary alarms. The sequence makes physical sense: the cause precedes the effect. An event
sequence that is backwards (protection relay trips before a fault condition is detected) indicates either a false trip
or a log-ordering issue.

Anomalous event sequences appear when events are out of order or do not follow expected causality. A relay trips at
10:00:00 UTC, but no fault was detected beforehand. Load is redistributed at 9:59:50 UTC, five seconds before the relay
tripped, which is backward. Multiple equipment failures occur within milliseconds in geographically diverse substations,
which is statistically improbable unless there is a common cause (network-wide transient).

## Event log gaps and deletions

Like the [alarm journal](scada-observables.md), the event log is append-only, so a break in its sequence reads as
deletion: event 1000 at 10:00 UTC followed by event 1003 at 10:05 UTC, with 1001 and 1002 absent, means those events
were removed, and the gap is the evidence.

Legitimate event deletions are extremely rare and would require explicit authorisation and documentation. A sensor
malfunction might generate a flood of false events (thousands of spurious readings per second), and after the cause is
identified, the false events might be deleted from the log. Such deletion is accompanied by an incident report
explaining the deletion.

An unexplained event gap in a critical time period (the gap encompasses the time when an unauthorised work was being
performed or when an anomaly occurred) is a red flag for deliberate tampering. If events are deleted from a SCADA log,
the SCADA's audit trail shows a deletion operation with user ID, timestamp, and authorisation. Missing deletion
records alongside missing events is strong evidence of unauthorised log tampering.

## Operator workload and situational awareness

The frequency of alarms and events flowing into the SCADA is correlated with operator workload. During periods of
network stress (high load, weather events, or cascade failures), the alarm and event rate increases substantially.
During normal conditions, the rate is low. If a period of normal network conditions is suddenly interrupted by a burst
of alarms, that is notable.

An operator's ability to maintain situational awareness degrades under high alarm load. If an operator is managing
dozens of alarms simultaneously, they may miss subtle details or may prioritise incorrectly. A sequence of events where
an operator makes a decision that worsens a cascade failure might be understandable if the operator was overwhelmed with
alarms and did not fully understand the situation, versus inexplicable if the alarm load was light and the operator had
time to analyse carefully.

For forensic analysis, the alarm and event logs provide context for understanding what operators knew and when. If an
operator's decision can be reconstructed from the logs (what alarms they saw, when they saw them, what they
acknowledged), then the forensic narrative can evaluate whether their decision was reasonable given the information
available, or whether it was erroneous or suspicious.

## The documented twin

Almost everything alarming on this layer has a legitimate double. A suppressed alarm is routine when a section is under
maintenance and reckless when it hides a live condition; a raised threshold is housekeeping after an upgrade and sabotage
without one; a gap in the event log is an authorised purge or a deletion covering its tracks. What separates each pair is
the paperwork the legitimate version carries and the illegitimate one cannot forge cheaply: the work order that
authorises the suppression or the threshold change, and the deletion record a real purge leaves beside the missing
events. Suppression with no work order, a threshold moved with no work behind it, events gone with no deletion logged,
these are the same act stripped of its authorisation, and the missing authorisation is the signature.

The noise floor is high by design: hundreds of configured conditions and a few alarms a day on a busy feeder, much of it
nuisance alarms the operators acknowledge and move past, so no single alarm carries the signal and only the pattern
does. The gap, two origins:

    A GAP IN THE APPEND-ONLY EVENT LOG
    ──────────────────────────────────
                    AUTHORISED DELETION       │  TAMPERING
    deletion log    user, time, authority     │  none
    incident note   a sensor-flood report     │  none
    gap timing      a routine period          │  over a spell of unauthorised work

*Last updated: 13 July 2026*
