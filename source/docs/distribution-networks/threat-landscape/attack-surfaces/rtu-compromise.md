# RTU compromise

Threats to remote terminal units and field devices: firmware modification, malicious configuration injection, I/O manipulation, or remote device takeover. An RTU compromise can cause field devices to execute unauthorised commands, ignore legitimate ones, or report false state.

RTU firmware is updated through the engineering tools and leaves traces in version records and firmware history. I/O changes can be detected through discrepancies between commanded and actual device state.

## RTU firmware modification

Remote terminal units (Smart Grid Terminals in Stedin's medium-voltage stations, older RTUs in substations) run firmware that implements the communication protocol (IEC 60870-5-104), collects sensor measurements, executes I/O commands (energise relay coils, close switchpoints). An attacker modifying RTU firmware changes how the device behaves. A modified RTU can accept commands on IEC 60870-5-104 while ignoring them internally, report false measurements, or execute conditional logic under specific circumstances.

Firmware updates for RTUs are typically delivered through the engineering tools (the workstation that manages field devices) or through a firmware update mechanism built into the RTU itself. The operator downloads firmware from the vendor, loads it into an engineering tool, and connects to the RTU over a serial link or network to push the firmware. This process is normally documented and leaves a trace: the RTU records its firmware version, and Stedin documents when the firmware was updated and what version was deployed. Knowing [how RTU maintenance is scheduled and controlled](../../operating-context/operations-and-cadence/operational-procedures-and-change.md) and [who has authority to work on field devices](../../operating-context/operations-and-cadence/contractor-management.md) helps defenders distinguish legitimate firmware updates from unauthorised modifications.

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
    │ → Trigger: ACTIVATED ✗           │
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
    │ → Firmware now behaves maliciously ✗     │
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

Configuration is typically stored in the RTU's non-volatile memory (flash or EEPROM) and is loaded when the device boots. An attacker with physical access could connect a JTAG debugger or similar tool and directly read or write the RTU's memory. An attacker with network access could compromise the configuration upload mechanism and inject malicious configuration.

## I/O command hijacking

An RTU deployed at a Stedin site has digital inputs and outputs. Inputs are connected to sensors (current transformers, voltage transformers, protection relay contacts indicating a fault condition). Outputs are connected to field devices (relay coils that can be energised to open or close a switchpoint, alarm lamps, status indicators).

An attacker who can compromise the RTU's I/O handling could cause a mismatch between commanded outputs and actual outputs. For instance, an operator could command an output to Close a switchpoint, but the compromised RTU could ignore the command and keep the switchpoint open. Alternatively, the RTU could execute the command physically, but report back to e-terracontrol SCADA that the command failed, making the operator believe the switchpoint is still open.

More dangerously, a compromised RTU could execute outputs autonomously without receiving a command from e-terracontrol SCADA. If the RTU's logic is modified to sense a specific input condition (like a frequency deviation below 48 Hz), the RTU could be programmed to open a switchpoint whenever that condition is met, without waiting for a command from Stedin's control room. This would appear to e-terracontrol as if the RTU is malfunctioning (spontaneously opening a switchpoint), but would actually be the programmed behaviour of the compromised firmware.

## Device state manipulation

An RTU at a Stedin site continuously reports its state to e-terracontrol SCADA: whether inputs are high or low, whether outputs are energised, whether communication is normal, and what measurements are being collected. An attacker who can compromise the RTU's state reporting could cause the RTU to report false state to the operators.

For instance, a compromised RTU could report that a switchpoint is Open when it is actually Closed. An operator would believe the switchpoint is open and might take actions based on that false belief. If the operator is trying to de-energise a load for safety, and relies on the false report that the switchpoint is open, they might believe the work is safe to proceed when it is actually not.

Alternatively, a compromised RTU could report false measurements: reporting a voltage as 240V when it is actually 280V, or reporting a current as 0A when it is actually 1000A. This would cause e-terracontrol's alarms and protections to be based on false information about the network.

The challenge for the attacker is that field devices have independent state. A relay at the output can be visually observed or measured independently. A technician doing work at a site might physically measure the voltage and recognise that it is not what the RTU is reporting. But if the attacker's goal is only to influence e-terracontrol's decision-making (not to actually misrepresent the physical state indefinitely), then the false reporting only needs to persist long enough for the operator to make a decision based on it.

## Observable traces

What RTU compromise looks like in firmware version history, I/O event logs, and the gap between commanded and actual state.

RTU compromise leaves traces in several places. First, the RTU records its firmware version in its non-volatile memory and typically reports this version when queried. If Stedin's operator has a record of what firmware version should be running and periodically checks the deployed firmware, a mismatch indicates a problem. But if the attacker compromises the firmware version reporting as well (so that the RTU reports the old version while running new code), this check fails.

Second, RTUs typically have event logs that record when commands were received, whether they executed successfully, and when state changed. An RTU with compromised firmware that ignores commands, or that executes commands different from what was received, would show inconsistencies in its event logs. For instance, if Stedin's control room operator's log shows "issued Close to Switchpoint A" but the RTU's event log shows "received Close to Switchpoint B", the mismatch is evidence.

Third, there is a gap between commanded and actual state. If a control room operator commands a switchpoint to close, e-terracontrol sends a command to the RTU, the RTU's event log shows it received the command, the RTU reports back that the command succeeded, but the actual switchpoint (measured independently by a technician, or measured by a separate sensor) remains open, there is clear evidence of RTU compromise.

Fourth, firmware update records at Stedin leave a trace. The operator typically maintains a record of which firmware version is deployed to each RTU and when it was updated. An unexpected firmware update, or a firmware version that does not match the records, stands out.

Fifth, pattern analysis can reveal compromise. An RTU that begins behaving oddly (reporting unusual values, executing commands unexpectedly, or losing communication) might be malfunctioning rather than compromised, but pattern analysis can help distinguish. If many RTUs across Stedin begin behaving anomalously at the same time, or if the anomalous behaviour occurs only when specific field conditions are met, that pattern is more consistent with compromise than with random hardware failure.

The most difficult compromises to detect are those where the RTU operates normally most of the time and only exhibits anomalous behaviour under specific activation conditions. An RTU that runs normal firmware 99 per cent of the time and only activates malicious code when it receives a specific input pattern would appear to be functioning normally to most audits. Detection would require continuous monitoring of RTU behaviour and historical analysis of logs to look for patterns that suggest conditional activation.

*Last updated: 10 July 2026*
