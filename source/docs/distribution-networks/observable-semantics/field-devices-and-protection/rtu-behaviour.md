# RTU behaviour

Smart Grid Terminals and older RTUs in medium-voltage and low-voltage stations communicate with
e-terra SCADA via IEC 60870-5-104 telecontrol protocol. They accept commands from the control centre, execute them on
field devices, and report measurements and state back. The RTU's firmware, configuration, and I/O logs are the
observable layer through which RTU behaviour can be validated.

## Firmware version

Each RTU runs firmware implementing the IEC 60870-5-104 protocol and reports its version when queried. The version
string is the weakest of the firmware records, since the same code that would be altered also answers the query, so a
version other than the one on record catches only tampering that did not trouble to fake the reply. The firmer checks
sit beside it: the [firmware image's hash or signature](../configuration-and-versions/firmware-and-software-versions.md)
read back from the device against the vendor's published value, and the running firmware's behaviour against what the
recorded version is known to do. For an RTU those behavioural tells are specific, a protocol quirk the recorded version
does not implement, a response timing that shifts, an information object the device begins to emit or stops emitting. An
RTU whose reported version matches the baseline but whose behaviour does not is the case the version string cannot reach,
and it is read by setting the device's I/O and protocol behaviour against the record of what that version does, not by
trusting the number it returns.

## I/O command and response logs

An RTU's primary function is to receive commands from the control centre (Close switchpoint A, Open breaker B) and
execute them on field devices, then report back whether the command succeeded. The SCADA system logs each command
it sends to an RTU, and the RTU logs each command it receives. These two logs correspond: a command issued by the
SCADA appears in the RTU's received-command log moments later.

Normal I/O operation shows clean correspondence. The SCADA logs show "Operator XYZ issued Close to Switchpoint A at
10:34:22.456 UTC", and the RTU's event log shows "Received command Close to Output 1 at 10:34:22.501 UTC". The slight time
difference is the network propagation delay (typically 10-500 milliseconds). The RTU then physically energises the coil
connected to Output 1, and when the switchpoint mechanically closes, the RTU reads the feedback contact and reports
success back to the SCADA ("Command executed, Output 1 is now Closed, feedback confirmed at 10:34:22.712 UTC"). The
SCADA logs the success. The sequence is traceable through three independent logs: SCADA command log, RTU event log, and
RTU feedback log.

Anomalies appear as mismatches between these logs. An RTU that receives a Close command but its event log shows an Open
command was received indicates either network corruption or command injection. If the mismatch is consistent (multiple
commands consistently received inverted or redirected to the wrong output), it suggests deliberate tampering rather than
a random glitch. An RTU that reports successful command execution but the actual field device (observed by a technician,
or measured by independent sensors) remains in the original state is evidence of false reporting. If the SCADA command
log shows a command was issued but the RTU event log shows no corresponding received command, the command was either
lost in transmission or never sent. That the mismatch shows at all is assumed, not guaranteed: some RTUs log each command
received and its result in enough detail to expose a received-Open-against-issued-Close mismatch, others record little
beyond state changes, and older substation units may keep nothing queryable, so where the device is thin the mismatch
has to be caught upstream at the SCADA master or in a separate sequence-of-events recorder, if at all.

Replay attacks manifest as duplicate commands in the RTU event log arriving in rapid succession. If the RTU receives
"Open switchpoint A" at 10:34:22.501 UTC and then again at 10:34:23.105 UTC (exactly one second later), and only one
command was issued from the control centre, the second command is a replay. The RTU's event log may record both
commands, or it may filter out the second one if it is smart enough to detect and suppress replays. The presence of
duplicate commands with no corresponding duplicate in the SCADA's command log is the signature.

## State discrepancies and misreporting

An RTU continuously reports its state to the SCADA: the state of each input (is the switchpoint Open or Closed), the
state of each output (is the relay coil energised), and the values of continuous measurements (voltage, current,
frequency). Over time, the SCADA builds a model of the network's current state based on these RTU reports. An RTU that
misreports its state causes the SCADA's model to diverge from physical reality.

Normal state reporting is stable. If a switchpoint is mechanically closed, the RTU reads the feedback contact (a dry
contact that closes when the switchpoint closes) and reports the state as Closed. If the state is queried repeatedly,
the RTU reports the same value consistently. When a command causes a state change, the RTU reports the new state. The
state is observable and stable.

Misreporting can be subtle or dramatic. A subtle misreport: the RTU reports a switchpoint as Open when it is actually
Closed. An operator at the SCADA sees Open and believes the switchpoint is de-energised, and may proceed with
maintenance work, but the actual switchpoint is still energised, creating a safety hazard. A dramatic misreport: the RTU
begins reporting false measurements (voltage shown as 240V when actually 280V, current shown as 0A when actually 1000A).
The SCADA's alarms are based on these false values, so protections meant to trigger do not, or false alarms are
raised. False reporting is caught only against a record the RTU does not produce. The strongest is the protection relay in the
same bay: it measures the same current and voltage off the same instrument transformers through its own acquisition
path, so a relay reading 1000A while the RTU reports 0A places the fault in the RTU, not the primary plant. A field
meter held against the terminals does the same for a spot check. The historian is no help here, since it stores the
RTU's own series and inherits whatever the RTU reported. Where a switchpoint's position is in doubt, the co-located
relay's [sequence-of-events record](protection-relay-state.md) of the same contact, or a technician's eyes on the
mechanism, is the independent word against the RTU's.

A misreport survives for as long as nothing forces that comparison. An RTU that falsifies state only while a switchpoint
is under active control, and reports truthfully the rest of the time, gives the operator no reason to look and can hold
the gap for months. What breaks it is a scheduled reconciliation rather than a prompted one: the RTU's reported states
and measurements read against the relay and the field on a cadence, so the check happens whether or not anything looked
wrong.

## Configuration consistency

An RTU's configuration specifies the mapping between logical commands (Close switchpoint A) and physical I/O (energise
relay coil 1). The configuration also specifies device addresses, communication parameters, and the interpretation of
measurements.

A remapped I/O table is the case worth noting. If the configuration that normally maps Output 1 to switchpoint A is
altered to map it to switchpoint B, a command the SCADA sends to A is executed on B, and the RTU still acknowledges
success. The operator believes A is closed while B is. Nothing in the command exchange reads as wrong; only a
configuration comparison or a field check exposes it.

RTU configurations are stored in the RTU's non-volatile memory (flash) and are also stored in
engineering tool project files on the engineering workstation. Like relay settings, RTU configurations are versioned and
baselined. A periodic maintenance check involves reading the RTU's configuration and comparing it against the baseline.
A divergence points to unauthorised modification. The configuration is static between firmware updates (a new
firmware version might come with a default configuration that then needs updating), so a configuration change outside a
firmware update or documented maintenance window stands out.

The challenge is that RTU configuration is often opaque. Unlike protection relay settings, which are usually
human-readable (e.g. "Overcurrent threshold: 1200A"), RTU configuration files are often binary or proprietary formats
that require the vendor's engineering tool to interpret. That opacity slows an investigator reading the configuration as
much as anyone altering it.

## Anomalous behaviour patterns

Over time, an RTU develops a behavioural pattern that is observable even without detailed log analysis. An RTU that
operates correctly most of the time but occasionally exhibits anomalous behaviour (failing to execute a command
correctly, reporting false state for a brief interval, then resuming normal operation) might be running compromised
firmware with [conditional logic](../../threat-landscape/attack-surfaces/rtu-compromise.md) that stays dormant until a
trigger fires.

Conditional activation hides in the ratio: the dormant intervals far outnumber the triggered ones, so the anomaly reads
as an occasional glitch rather than a pattern. What separates it from a glitch is the trigger. Ageing hardware fails
without regard to the state of the network; a planted condition fires on a cue, a measured quantity crossing a set
point, a particular command arriving, a date reached, a neighbouring relay tripping. So the tell is not that an RTU
misbehaved but that it misbehaved each time the same cue was present and never otherwise, and pinning that down means
holding the anomalous moments against the network state recorded around them and asking what they share.

Correlation across the estate sharpens it. An RTU is one of many carrying the same vendor firmware build, so a fault
seeded in that build is shared by every device running it, while a worn coil or a corroded contact is one device's own
problem. Several RTUs of the same build turning anomalous within one window point past coincidence to the build they
have in common; the same behaviour confined to a single unit, tracking its age and duty, reads as hardware.

Behavioural baselines are useful for this analysis: how often an RTU normally executes commands successfully,
how often it reports state changes, how often measurement values change. A sudden deviation from this baseline (
significantly fewer successful command executions, measurement values that stop changing or change too frequently) is
anomalous. A gradual degradation over time might indicate hardware ageing; an abrupt shift suggests a change in firmware
or configuration.

*Last updated: 13 July 2026*
