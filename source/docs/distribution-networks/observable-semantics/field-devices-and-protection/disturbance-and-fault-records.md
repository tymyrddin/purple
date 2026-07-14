# Disturbance and fault records

The protection relays (inferred as SIPROTEC 5 and SEL-451, not independently confirmed yet) record disturbance data: high-fidelity waveforms captured at the
instant a protection event is detected. These recordings, stored in COMTRADE format (IEEE C37.111 / IEC 60255-24),
are the highest-confidence forensic evidence available for understanding what the relay actually measured and why it
operated.

## COMTRADE format and contents

COMTRADE (Common Format for Transient Data Exchange) is a standardised binary format for recording waveform data from
power-system equipment. A COMTRADE file contains: the sampled values of currents, voltages, and status signals at high
frequency (specified in samples per cycle, commonly 16 to 256 per cycle at 50 Hz, so from under a kilohertz to over ten kilohertz), the timestamp of when sampling started, and the
configuration data specifying what signals were recorded and their scaling factors.

When a relay detects a fault condition, it initiates a disturbance recording. The sampling had been running
continuously or on demand, and when the fault is detected, the relay captures the waveforms surrounding the fault:
a pre-fault window (seconds before the fault is detected), the fault window (seconds during which the fault
persists), and a post-fault window (seconds after the fault is cleared). The relay stores the recording in its memory,
and the recording is later extracted via engineering tools or via a gateway connected to the relay.

A COMTRADE file is the most objective evidence available because it is a hardware-level capture. The relay's
analogue-to-digital converter sampled the actual voltage and current waveforms from sensors (current transformers,
potential transformers, analogue circuits). The digital recording reflects what the hardware measured, not what any
software deduced. Falsifying a COMTRADE file would require either: modifying the hardware's measurement at the instant
the waveform was recorded (impossible, the hardware samples what is present), or forging the COMTRADE file after the
fact (which would require detailed knowledge of the waveform format and the discipline to keep every altered sample
internally consistent with the physics of the event).

## COMTRADE interpretation and physical validity

A COMTRADE file is interpreted by plotting the sampled waveforms and inspecting them for the signatures of faults. An
overcurrent fault appears as a sudden increase in current. An overvoltage fault appears as a sudden increase in voltage.
An underfrequency condition appears as the frequency calculated from the voltage waveform (by counting zero-crossings)
dropping below the nominal 50 Hz.

For a legitimate fault, the waveforms show clear physical signatures. An overcurrent fault shows current amplitude
increasing suddenly, and in three-phase systems, the three current phases may show an imbalance (depending on the fault
type: line-to-line, line-to-ground, etc.). The transient is visible: a sudden jump from the pre-fault steady-state to
the fault condition. After protection operates (after the relay's trip signal opens a breaker), the current drops back
toward normal (or to zero if the faulted section is fully isolated).

Anomalous or unphysical waveforms in a COMTRADE file are red flags. A COMTRADE showing perfectly sine-wave voltage and
current with no noise is suspicious (real power systems have continuous variation and noise). A COMTRADE showing a fault
condition that appears to violate physical laws (current flowing backward when it should flow forward, or unbalanced
three-phase currents that sum to a non-zero value when they should sum to zero) indicates either sensor malfunction or
forged data.

## COMTRADE file integrity

COMTRADE carries little integrity protection of its own. The original editions define no checksum at all, and the 2013
edition added only an optional CRC that covers the ASCII configuration file, not the binary waveform samples. Most
records in the field carry no checksum, so a clean-looking file proves nothing about whether the waveform was altered.

Integrity rests elsewhere. A forged COMTRADE has to keep every altered sample internally consistent, across the
pre-fault, fault and post-fault windows and across all three phases, with the physics of the event it claims to record.
That is difficult to do convincingly by hand. The stronger check is external: the waveform is compared against
independent measurements of the same event (the RTU's readings, the historian's stored values, a second relay's
capture). A relay whose firmware has been modified to emit synthetic waveforms defeats any file-level check, because the
false data is generated at source. Only physical-plausibility analysis and cross-source comparison catch that case.

## Cross-checking COMTRADE against other measurement sources

The power-system measurements in a COMTRADE file are consistent with other independent measurement sources when nothing
has gone wrong. A SIPROTEC relay that recorded a COMTRADE showing an overcurrent fault at a location has, as its
corroboration, the RTU at that location reading increased current at approximately the same time and the historian
holding the same measurements. The three independent sources agree.

If the COMTRADE shows a fault at 10:00:00.000 UTC with a measured current of 1500A, the RTU's log carries high current
at approximately 10:00:00 UTC (clock drift stays small with NTP synchronisation) and the historian the same current at
that time. The three sources align.

A divergence is forensic evidence of tampering or malfunction. If the COMTRADE shows a fault at 10:00:00 UTC but the
historian shows normal current at 10:00:00 UTC and high current at 10:05:00 UTC, either the COMTRADE's timestamp is
wrong, or the historian's measurements are wrong, or one of the systems is falsifying data. The investigation would
proceed by examining clocks, NTP synchronisation, and other evidence to determine which source is trustworthy.

## Relay event log and COMTRADE correlation

A relay's event log (separate from the COMTRADE) records when faults are detected and when protection operates, with
timestamps. The event log carries an entry for a fault detection at the instant the COMTRADE begins recording the
fault, and the event log timestamp matches the COMTRADE's start timestamp (allowing for clock synchronisation
differences).

If the event log shows a relay trip at 10:00:10 UTC but the COMTRADE shows the fault beginning at 10:00:05 UTC, the
timing divergence requires explanation. Possible explanations include: the relay's clock drifted by 5 seconds (clock
synchronisation issue), or the COMTRADE was misdated (timestamped incorrectly), or the event log is incomplete (the
relay detected and began recording the fault 5 seconds before it officially recorded the trip event).

## Missing COMTRADE files

If a relay's event log shows it detected a fault and tripped, a COMTRADE file recording that event is normally stored on
the relay. If the COMTRADE file is not found (either the relay's memory is full and old COMTRADE files were overwritten,
or the file is missing for another reason), that is forensically significant.

A missing COMTRADE for a significant event is hard to explain innocently. A relay that claims to have detected and responded to a major
fault, but has no COMTRADE recording of that fault, is missing the hardware record a real trip would leave. The COMTRADE would normally be automatically
generated; its absence suggests either the relay was operating in a mode where COMTRADE recording was disabled, or the
COMTRADE was deliberately deleted, or the fault-detection event was recorded but the actual fault did not occur (the
event log was falsified).

## Disturbance playback and simulation

Some SCADA systems can play back COMTRADE files to understand how a relay would have responded to a historical fault.
This capability is useful for forensic analysis: if a COMTRADE from a fault is available, the relay can be taken offline
and the COMTRADE can be played back through a relay simulator to verify that the relay would indeed respond as it did
during the actual event.

If the replay shows the relay would not have responded as documented (for instance, the replay shows the relay's
threshold was not exceeded, but the relay's event log shows it tripped), then either the COMTRADE is not representative
of the actual fault, or the relay's settings were different during the actual event than they are now, or the event log
is falsified.

This testing method provides independent validation of a relay's response. If the relay is suspected of having been
compromised (settings changed, firmware modified), the relay testing provides evidence of the compromise. A relay that
would not trip to a known fault condition is not functioning as configured.

## Fault sequences and protection coordination

When multiple relays protect the same fault point (primary protection and backup protection), their COMTRADE files
show the same fault sequence, with similar measured values (current, voltage), and with the primary relay
responding before the backup relay (if protection coordination is working correctly).

If the primary relay's COMTRADE shows a fault at 10:00:00 UTC and the relay tripped immediately, the backup relay shows
the same fault at 10:00:00 UTC. If the backup relay's COMTRADE shows the fault at 10:00:05 UTC (5 seconds later),
the timing divergence indicates either clock skew, or one of the relays is measuring at a different location and is
seeing a delayed version of the fault propagation, or one of the COMTRADE files is unreliable.

Proper protection coordination is verified by examining the COMTRADE files: the primary relay detects and responds, the
backup relay detects the same fault but does not trip (because the primary relay already cleared it). The COMTRADE files
document this sequence and allow auditors to verify that the protection system operated as designed.

## Evidence of relay malfunction versus compromise

A relay's COMTRADE files can distinguish between malfunction and compromise. A malfunctioning relay might produce
erratic COMTRADE files (garbled data, inconsistent timestamps, impossible waveforms), indicating a hardware or software
bug. A compromised relay may instead produce normal COMTRADE files that correctly record real faults (because the compromise
is selective: only under specific conditions does the relay misbehave), or emit false COMTRADE files (if the
attacker modified the firmware to generate synthetic waveforms).

Systematic analysis of COMTRADE files over time can reveal patterns. If all COMTRADE files from a relay are suspicious (
implausibly smooth waveforms, no noise, physically implausible), the relay is likely compromised or malfunctioning. If
most COMTRADE files appear normal but a few are anomalous (corresponding to the times when unauthorised work is
suspected to have occurred), the relay may have been conditionally compromised (malicious code activated only under
specific conditions).

## Genuine capture or forgery

A COMTRADE either records a fault that happened or dresses up one that did not, and the file alone cannot always tell
which: its integrity protection is thin, so a clean-looking record proves little. What decides is corroboration. The
waveform is set against the RTU's reading, the historian's stored values and a second relay's capture of the same event,
and against the physics the event would have to obey; a forgery has to stay coherent across all of them, which is hard
by hand. The case the cross-check cannot reach is a relay whose own firmware emits synthetic waveforms, since the false
data is generated at source; there only physical-plausibility and the wider independent record remain, and a fault the
relay claims but leaves no COMTRADE behind is the absence that gives it away.

A COMTRADE is written only when a relay trips, so the record is sparse; a capture present with no fault, or missing where
a trip claims one, stands against a quiet backdrop. The capture, two origins:

    A COMTRADE FILE FOR A LOGGED TRIP
    ─────────────────────────────────
                    GENUINE FAULT             │  FORGED, OR NO FAULT
    RTU + historian  agree with the waveform  │  disagree
    second relay    same fault, same time     │  no matching capture
    physics         balances across phases    │  inconsistent, unless built with care
    the file        present                   │  may be missing for a claimed trip

*Last updated: 13 July 2026*
