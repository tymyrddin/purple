# RTU compromise

An RTU can be attacked in several ways: firmware modification, malicious configuration injection, I/O manipulation, or remote device takeover. An RTU compromise can cause field devices to execute unauthorised commands, ignore legitimate ones, or report false state.

RTU firmware is updated through the engineering tools and leaves traces in version records and firmware history. I/O changes can be detected through discrepancies between commanded and actual device state.

## RTU firmware modification

Remote terminal units (Smart Grid Terminals in medium-voltage stations, older RTUs in substations) run firmware that implements the communication protocol (IEC 60870-5-104), collects sensor measurements, executes I/O commands (energise relay coils, close switchpoints). An attacker modifying RTU firmware changes how the device behaves. A modified RTU can accept commands on IEC 60870-5-104 while ignoring them internally, report false measurements, or execute conditional logic under specific circumstances.

Firmware updates for RTUs are most often delivered through the engineering tools (the workstation that manages field devices) or through a firmware update mechanism built into the RTU itself. An operator downloads firmware from the vendor, loads it into an engineering tool, and connects to the RTU over a serial link or network to push the firmware. This process is normally documented and leaves a trace: the RTU records its firmware version, and the operator documents when the firmware was updated and what version was deployed. Knowing [how RTU maintenance is scheduled and controlled](../../operating-context/operations-and-cadence/operational-procedures-and-change.md) and [who has authority to work on field devices](../../operating-context/operations-and-cadence/contractor-management.md) helps defenders distinguish legitimate firmware updates from unauthorised modifications.

An attacker could compromise firmware at several points: the vendor's firmware distribution (inserting malicious code into the firmware before it is released), the firmware download in transit (modifying it on the way), the operator's engineering workstation (so that malicious code is injected when the firmware is loaded), or the RTU itself (directly accessing it and reprogramming its flash memory).

A modified RTU firmware could include a "dead man's switch": logic that lies dormant until activated by a specific condition. For instance, the firmware could include code that is triggered when the RTU receives a specific sequence of commands (a sequence that would never occur in normal operation, but that an attacker could intentionally send). Once triggered, the modified firmware could cause the RTU to ignore subsequent commands, to report false measurements, or to execute specific switching operations. This approach keeps the compromise dormant and undetected until the attacker chooses to activate it.

    DORMANT FIRMWARE: Activation by Command Sequence
    ────────────────────────────────────────────────

    NORMAL OPERATION (firmware running, trigger inactive)
    ─────────────────────────────────────────────────────

    RTU firmware
    ┌──────────────────────────────────┐
    │ Standard IEC 60870-5-104 logic   │
    │ • Execute commands normally      │
    │ • Report state correctly         │
    │ • Respond to polling             │
    │                                  │
    │ [Dormant trigger code: waiting]  │
    └──────────────────────────────────┘
                  ↑
    Incoming commands processed normally:
    Close A → Close A executed
    Open B  → Open B executed
    SetPoint X → SetPoint X set


    TRIGGER SEQUENCE DETECTED (attacker sends specific pattern)
    ───────────────────────────────────────────────────────────

    RTU firmware
    ┌──────────────────────────────────┐
    │ Receives command sequence:       │
    │ 1. SetPoint 9999 (invalid)       │
    │ 2. Close A, then Open A (loop)   │
    │ 3. Frequency 48.5 Hz (edge case) │
    │ 4. [Never normally occur]        │
    │                                  │
    │ RECOGNITION: This is the         │
    │ attacker's activation pattern    │
    │                                  │
    │ → Trigger: ACTIVATED           │
    └──────────────────────────────────┘


    POST-ACTIVATION (malicious behaviour now active)
    ────────────────────────────────────────────────

    RTU firmware
    ┌──────────────────────────────────────────┐
    │ Dormant code now executes:               │
    │                                          │
    │ Option A: Ignore commands                │
    │ • e-terracontrol: "Close A"              │
    │ • RTU: ACK sent, but ignore internally   │
    │ • Switchpoint A remains OPEN             │
    │                                          │
    │ Option B: Report false state             │
    │ • Actual: Switchpoint A = OPEN           │
    │ • Reported: Switchpoint A = CLOSED       │
    │ • Operator believes protection working   │
    │                                          │
    │ Option C: Execute autonomous action      │
    │ • Trigger: When frequency drops below    │
    │           48.5 Hz (blackout risk)        │
    │ • Action: Open specified load shedding   │
    │           switchpoint without command    │
    │                                          │
    │ → Firmware now behaves maliciously     │
    └──────────────────────────────────────────┘


    DETECTION CHALLENGES
    ────────────────────

    Before activation:
    • Dormant trigger code hidden in firmware binary
    • Firmware version comparison shows expected version (attacker controls version string)
    • Event logs show normal operations
    • RTU appears healthy

    After activation:
    • If attacker continues to hide (maintains consistency between commands and reports),
      may go undetected until compared against field device independent state
    • RTU event log shows inconsistencies only if attacker fails to spoof ACK/responses
    • Field device physical state (relay coil energised or not) can reveal the lie


## Malicious configuration injection

In addition to firmware, RTUs have configuration data that governs how the device operates. This includes device addresses, communication parameters, the mapping between measured values and input channels, and the mapping between output commands and field devices. An attacker who can modify this configuration can change how the RTU operates.

A common configuration attack modifies the I/O mapping. For instance, if the configuration normally specifies that "Output 1 energises switchpoint A", an attacker could modify the configuration so that "Output 1 energises switchpoint B instead". When an operator commands switchpoint A to close, the RTU would actually close switchpoint B. The operator would receive acknowledgement (the RTU would report that the command executed), and would believe switchpoint A is closed when it is actually switchpoint B that is closed.

Configuration is stored in the RTU's non-volatile memory (flash or EEPROM) and is loaded when the device boots. An attacker with physical access could connect a JTAG debugger or similar tool and directly read or write the RTU's memory. An attacker with network access could compromise the configuration upload mechanism and inject malicious configuration.

## I/O command hijacking

An RTU deployed at a site has digital inputs and outputs. Inputs are connected to sensors (current transformers, voltage transformers, protection relay contacts indicating a fault condition). Outputs are connected to field devices (relay coils that can be energised to open or close a switchpoint, alarm lamps, status indicators).

An attacker who can compromise the RTU's I/O handling could cause a mismatch between commanded outputs and actual outputs. For instance, an operator could command an output to Close a switchpoint, but the compromised RTU could ignore the command and keep the switchpoint open. Alternatively, the RTU could execute the command physically, but report back to e-terracontrol SCADA that the command failed, making the operator believe the switchpoint is still open.

More dangerously, a compromised RTU could execute outputs autonomously without receiving a command from e-terracontrol SCADA. If the RTU's logic is modified to sense a specific input condition (like a frequency deviation below 48.5 Hz), the RTU could be programmed to open a switchpoint whenever that condition is met, without waiting for a command from the control room. This would appear to e-terracontrol as if the RTU is malfunctioning (spontaneously opening a switchpoint), but would actually be the programmed behaviour of the compromised firmware.

## Device state manipulation

An RTU continuously reports its state to e-terracontrol, and an attacker who compromises that reporting makes the SCADA's
picture diverge from what is physically there: a switchpoint shown Open while it is still live, a measurement flattened
so an alarm that should fire stays silent. The hazard is a decision taken on the false picture, an operator
de-energising a load for safety on a switchpoint that never opened. Because
[the reported state can be set against an independent measurement](../../observable-semantics/field-devices-and-protection/rtu-behaviour.md),
the lie does not have to survive scrutiny, only persist long enough for that one decision.

## Observable traces

RTU compromise leaves traces across the
[RTU's own logs](../../observable-semantics/field-devices-and-protection/rtu-behaviour.md): a firmware version that no
longer matches the record, a received command that differs from the one issued, a reported success the field device's
state contradicts, an unexpected firmware-update entry. None is decisive alone, a thin RTU may barely log and a version
string can itself be forged, and the hardest compromise runs normal firmware almost all the time, turning malicious only
on a trigger. What exposes that is pattern rather than any single record: several devices anomalous at once, or anomalies
that track a specific field condition.

*Last updated: 13 July 2026*
