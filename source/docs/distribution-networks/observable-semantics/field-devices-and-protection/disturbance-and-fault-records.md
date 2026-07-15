# Disturbance and fault records

When a protection event fires, the relay (inferred as SIPROTEC 5 and SEL-451, not independently confirmed yet) captures
a high-fidelity waveform of the instant it operated, stored in COMTRADE format (IEEE C37.111 / IEC 60255-24). It is
close to a photograph of the fault: what the relay actually measured, and why it tripped.

## COMTRADE format and contents

A COMTRADE file is the closest thing to a hardware witness the estate holds: the relay's own capture of the current and
voltage waveforms at the instant it acted. The format (Common Format for Transient Data Exchange) is a standardised
binary one, holding the sampled values at high frequency, specified in samples per cycle, commonly 16 to 256 per cycle
at 50 Hz, so from under a kilohertz to over ten kilohertz, alongside the start timestamp and the configuration that says
what was recorded and how it scales.

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

A COMTRADE file is read by plotting the waveforms and looking for the shape of a fault: a sudden jump in current or
voltage for an overcurrent or overvoltage, or, for underfrequency, the frequency counted off the voltage zero-crossings
sliding below the nominal 50 Hz.

For a legitimate fault, the waveforms show clear physical signatures. An overcurrent fault shows current amplitude
increasing suddenly, and in three-phase systems, the three current phases may show an imbalance (depending on the fault
type: line-to-line, line-to-ground, etc.). The transient is visible: a sudden jump from the pre-fault steady-state to
the fault condition. After protection operates (after the relay's trip signal opens a breaker), the current drops back
toward normal (or to zero if the faulted section is fully isolated).

A waveform that could not have come off real plant is the tell. A trace too clean to be true, perfect sine voltage and
current with none of the noise a live network always carries, or one that breaks physics, a fault current that rises
with no matching sag in voltage, or phase currents that cannot be reconciled with the measured residual, is either a
sensor fault or a forgery.

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

## Relay event log and COMTRADE correlation

A relay's event log (separate from the COMTRADE) records when faults are detected and when protection operates, with
timestamps. The event log carries an entry for a fault detection at the instant the COMTRADE begins recording the
fault, and the event log timestamp matches the COMTRADE's start timestamp (allowing for clock synchronisation
differences).

If the event log times the trip at 10:00:10 but the COMTRADE has the fault starting at 10:00:05, the five seconds have
to be accounted for: a relay clock adrift, a capture misdated, or an event log that noted the trip a beat after the
relay had already begun recording the fault.

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
data is generated at source, and there only physical plausibility and the wider independent record remain.

A COMTRADE is written only when a relay trips, so the record is sparse; a capture present with no fault, or missing where
a trip claims one, stands against a quiet backdrop.

*Last updated: 13 July 2026*
