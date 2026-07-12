# Firmware and software versions

Stedin's field devices (RTUs, protection relays, smart grid terminals) run firmware: executable code stored in
non-volatile memory that implements the device's protocols, logic, and functionality. Each firmware version is uniquely
identified by a version number, and Stedin maintains records of which devices are running which versions. Version
tracking, upgrade histories, and cryptographic verification of firmware integrity form the observable layer for hardware
compromise detection.

## Firmware version baselines

Each field device at Stedin is expected to run a specific known firmware version. RTUs at medium-voltage stations
might be running a Smart Grid Terminal firmware version such as 3.5.2. Protection relays, with the maker inferred as
SIPROTEC or SEL, might be running a version such as 5.12.4. Stedin keeps a baseline of the expected version for each
device.

A query to the device (via the SCADA, via the engineering tool, or via a direct connection) asks the device to report
its firmware version. The response is compared against the baseline. A match means the device is running the expected
firmware. A mismatch indicates either: a legitimate firmware update that the baseline has not been updated to reflect,
or an unauthorised firmware modification.

Normal firmware updates follow a documented process. Stedin evaluates a new firmware release from the vendor, approves
it, schedules an update window, and performs the update. The process is typically: download the new firmware, verify it
against the vendor's digital signature (if available), load it into the engineering tool, connect to the device, and
upload the new firmware to the device's flash memory. The device reboots with the new firmware, reports the new version,
and the baseline is updated.

Firmware version history is the record of all firmware updates to a device: when
each update was performed, by whom, what version was deployed, and whether the update was successful. The history is
observable through device logs (if the device records firmware updates) and through Stedin's asset-management system (
Maximo or equivalent).

## Unauthorised firmware modification signatures

Unauthorised firmware modification would appear as a device reporting a firmware version that diverges from the
baseline, with no corresponding update record in the update history. If the baseline shows RTU X at version
3.5.2, but querying RTU X reports version 3.5.3, either the baseline is outdated (there was an update that was not
reflected in the baseline) or the firmware was modified.

The challenge is that a sophisticated attacker might compromise not only the firmware on the device but also the
version-reporting mechanism. The compromised firmware could report the old version while running new malicious code,
defeating the simple version check. To detect this attack, more sophisticated methods are needed: cryptographic
verification of the firmware (if the vendor provides signatures), extraction and analysis of the firmware from the
device's flash memory, or observation of the device's behaviour to detect functional anomalies that indicate modified
firmware.

An RTU with modified firmware might behave anomalously: failing to execute commands correctly, reporting false
measurements, losing communication intermittently, or executing commands that were not issued. These behavioural
anomalies are the signatures of firmware compromise when the firmware version check is bypassed.

## Firmware integrity verification

Some vendors provide cryptographic signatures for firmware releases. If Stedin obtains firmware from the vendor signed
with the vendor's private key, the signature can be verified before deploying the firmware to a device. A firmware
package that fails signature verification (either the signature is invalid, or the firmware contents have been modified
since signing) is rejected.

A firmware distribution process that enforces signature verification has the engineering tool verify the
signature before loading the firmware, and refuse to load unsigned or incorrectly signed firmware. If a device is
queried for its firmware and the firmware fails signature verification (extracted from the device and verified against
the vendor's public key), the firmware is either modified or corrupted.

For devices where the vendor does not provide signatures, hash-based verification can be used: Stedin computes a
cryptographic hash (SHA-256 or similar) of the expected firmware and stores the hash in a secure location. When a device
is audited, the firmware is extracted, hashed, and compared against the stored hash. A matching hash provides confidence
that the firmware is authentic and unmodified.

## Firmware update audit logs

Stedin's engineering workstations (DIGSI, AcSELerator, other tools) log when firmware updates are performed. The logs
record: the timestamp of the update, the user who performed it, the source of the firmware (file path, version
number), and the target device (device address, type). After the update, the device is queried to verify it reported the
new version.

A legitimate firmware update produces a clean log trail: the update is recorded, the device confirms the new version,
and the baseline is updated. An unauthorised firmware update might produce fragmented evidence: no update log (the
engineering tool was bypassed), or the device reports a version that does not match any recognised version.

Failed firmware updates are also logged. If an update is attempted but fails (the device rejects the firmware, or
the network connection is lost), the failure is recorded. A device that has never successfully reported a firmware
version (no successful update has ever been completed) stands out.

## Firmware version and feature correlation

Firmware versions have associated features and capabilities. Firmware version 3.5.2 has specific protections against
certain types of input manipulation, or has certain communication protocols enabled. If a device reports a firmware
version but behaves as though it is running a different version (supports protocols it should not support, or lacks
protections it should have), the reported version is false.

Behavioural testing of firmware can verify consistency. If an RTU reports it is running firmware version 3.5.2, it
responds correctly to commands defined in the 3.5.2 specification and fails to respond to commands added in
later versions. If the RTU supports features only available in version 3.6.0 or later, but reports version 3.5.2, the
version report is false.

## Software version tracking for host systems

SCADA servers, historian servers, and engineering workstations also run software with version numbers. The SCADA
system (GE SCADA, Siemens, Schneider, etc.) has version and patch levels. The historian system also has version and patch levels. These versions are tracked and baseline versions maintained, similar to field-device
firmware.

Normal software updates follow a documented process: the vendor releases an update (often a security patch), the update
is evaluated for compatibility and risk, it is tested in a controlled environment, and then deployed to production
systems. The deployment of a software update is documented: when it was applied, by whom, and whether it was
successful.

Unauthorised software modifications would appear as system processes or executables that diverge from the expected
version. File-integrity monitoring tools can detect if critical system files have been modified. If an SCADA server's
core executables are different from what the vendor provided (detected through hash verification), the system may be
compromised.

## Version control integration and artefact chains

Where firmware and software are held under version control, the deployed version corresponds to a specific commit; a
running version that matches no commit, or a committed change that never reached the device, is the divergence to look
for.

## Reverse engineering and firmware analysis

For devices where the firmware is suspected of being compromised, forensic analysis involves extracting the firmware (
from the device's flash memory via JTAG, or via vendor tools if available) and analysing it. The analysis involves:
disassembling the code, identifying modified sections, comparing against the expected firmware version, and
understanding what the unauthorised code is doing.

This analysis is technically challenging and typically requires specialised expertise and tools. It is also
destructive (extracting firmware from a device may require physical access and may damage the device). For operational
networks, firmware extraction is typically done post-incident or on lab equipment, not on active production devices.

The evidence from firmware analysis is powerful but requires expert interpretation. If a modified firmware section is
identified, it can potentially be reverse-engineered to understand the attacker's intent (what malicious logic was
injected). However, this requires access to the original unmodified firmware for comparison, and may require
reverse-engineering skills to understand proprietary code formats and logic.

*Last updated: 12 July 2026*
