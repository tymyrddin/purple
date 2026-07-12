# RTU behaviour

Stedin's Smart Grid Terminals and older RTUs deployed in medium-voltage and low-voltage stations communicate with
e-terra SCADA via IEC 60870-5-104 telecontrol protocol. They accept commands from the control centre, execute them on
field devices, and report measurements and state back. The RTU's firmware, configuration, and I/O logs are the
observable layer through which RTU behaviour can be validated.

## Firmware version

Each Stedin RTU runs firmware implementing the IEC 60870-5-104 protocol, and reports its version when queried. An RTU
reporting a version other than the one Stedin holds on record is a first-order red flag, with the caveat that version
reporting is itself software and a naive comparison only catches naive tampering.

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
lost in transmission or never sent.

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
raised. False measurement reporting is detectable if independent measurements are available: a technician at the site
physically measures the voltage with a meter and compares it to the RTU's report, or a protection relay at the same
location measures the same electrical quantity and its measurement is compared to the RTU's report.

The risk of misreporting is that it can persist undetected for extended periods if no one cross-checks the RTU's report
against independent measurements. An RTU that reports false state only under specific conditions (for example, reporting
Open for a switchpoint only when that switchpoint is being actively controlled, but reporting Closed at all other times)
might evade detection for months if the SCADA operator never has a reason to verify the state when no active control is
happening.

## Configuration consistency

An RTU's configuration specifies the mapping between logical commands (Close switchpoint A) and physical I/O (energise
relay coil 1). The configuration also specifies device addresses, communication parameters, and the interpretation of
measurements.

A remapped I/O table is the case worth noting. If the configuration that normally maps Output 1 to switchpoint A is
altered to map it to switchpoint B, a command the SCADA sends to A is executed on B, and the RTU still acknowledges
success. The operator believes A is closed while B is. Nothing in the command exchange reads as wrong; only a
configuration comparison or a field check exposes it.

Stedin's RTU configurations are typically stored in the RTU's non-volatile memory (flash) and are also stored in
engineering tool project files on the engineering workstation. Like relay settings, RTU configurations are versioned and
baselined. A periodic maintenance check involves reading the RTU's configuration and comparing it against the baseline.
A divergence points to unauthorised modification. The configuration is static between firmware updates (a new
firmware version might come with a default configuration that then needs updating), so a configuration change outside a
firmware update or documented maintenance window stands out.

The challenge is that RTU configuration is often opaque. Unlike protection relay settings, which are typically
human-readable (e.g. "Overcurrent threshold: 1200A"), RTU configuration files are often binary or proprietary formats
that require the vendor's engineering tool to interpret. That opacity slows an investigator reading the configuration as
much as anyone altering it.

## Anomalous behaviour patterns

Over time, an RTU develops a behavioural pattern that is observable even without detailed log analysis. An RTU that
operates correctly most of the time but occasionally exhibits anomalous behaviour (failing to execute a command
correctly, reporting false state for a brief interval, then resuming normal operation) might be running compromised
firmware with conditional logic. A "dead man's switch" compromise would cause the RTU to operate normally 99 per cent of
the time, only becoming malicious when triggered by a specific condition (a sequence of commands, a specific network
state, or a time-based trigger).

Conditional activation is harder to detect in logs because the normal operation events far outnumber the anomalous
events. However, pattern analysis can reveal it. If anomalies occur only under specific conditions (only when voltage
exceeds a certain level, or only when a specific protection relay has recently tripped), that pattern suggests
intentional logic rather than random malfunction. A random hardware failure is equally likely under any condition; a
deliberate conditional trigger is not. Statistical analysis of the timing and conditions under which anomalies occur can
reveal patterns that suggest deliberate compromise.

Behavioural baselines are useful for this analysis: how often an RTU normally executes commands successfully,
how often it reports state changes, how often measurement values change. A sudden deviation from this baseline (
significantly fewer successful command executions, measurement values that stop changing or change too frequently) is
anomalous. A gradual degradation over time might indicate hardware ageing; an abrupt shift suggests a change in firmware
or configuration.

*Last updated: 12 July 2026*
