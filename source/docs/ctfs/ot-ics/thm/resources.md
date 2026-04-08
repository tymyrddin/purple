# Simulator power-and-light-sim

[https://github.com/tymyrddin/power-and-light-sim](https://github.com/tymyrddin/power-and-light-sim)

Python-based simulator with a physics engine and a Purdue-model network topology (enterprise,
operations, control, DMZ zones). Configuration-driven via YAML. Runs with Python 3.12.

Techniques reference the categories in [attack surface](../attack-surface.md).

## Protocol implementation status

| Protocol    | Port         | Status                    |
|:------------|:-------------|:--------------------------|
| Modbus TCP  | 10502-10510+ | Complete                  |
| Modbus RTU  | Serial       | Complete                  |
| DNP3        | 20000        | Partial                   |
| IEC 104     | 2404         | Complete                  |
| OPC UA      | 4840         | Complete                  |
| S7          | 102          | Complete                  |
| EtherNet/IP | 44818        | Complete (simplified CIP) |

Known implementation issues (documented in SIMULATOR_GAPS.md):
* Modbus FC43/MEI14 device identity: all devices return identical vendor information due to a
  pymodbus bug; information disclosure via Modbus still works, but device fingerprinting is
  unrealistic
* S7 ports 102/103 require elevated privileges; use `setcap` or iptables port forwarding rather
  than running the simulator as root
* Modbus unit ID validation: servers respond to all unit IDs regardless of configuration; unit ID
  scanning demonstrations are unrealistic until fixed

## Physics engines

TurbinePhysics, ReactorPhysics, HVACPhysics, GridPhysics, PowerFlow. Attacks that change device
state produce observable physical consequences via these engines.

## Attack scripts

Organised by phase: recon, discovery, analysis, exploitation, assessment.

Recon: `turbine_recon.py` is confirmed working. All other recon scripts require validation against
the current simulator.

Exploitation: `turbine_overspeed_attack.py`, `turbine_emergency_stop.py`,
`modbus_shutdown_attack_demo.py`, `plc_logic_extraction.py`, and others are present. The
exploitation README states all scripts need validation against the current simulator. The turbine
PLC Modbus vulnerability is documented with real-world impact assessment in `theoretical-impact.md`.

## Done

* Modbus TCP and RTU servers (state manipulation)
* IEC 104 server (state manipulation)
* OPC UA server with certificate tooling (state manipulation, process intelligence, trust exploitation)
* S7 server (state manipulation, control logic manipulation), privileged port workaround required
* DNP3 partial implementation (state manipulation, process intelligence)
* EtherNet/IP with simplified CIP support
* Physics engines responding to control writes (state manipulation)
* Blue team tooling: `tools/blue_team.py`, 8+ workshop challenges

## Feasible

* DNP3 CROB challenge: protocol present at port 20000, partial implementation; a dedicated
  challenge exercising the control relay output block path with visible physical consequence is
  not yet built (state manipulation)
* Subtle setpoint drift: physics layer responds to setpoint writes; a within-bounds incremental
  manipulation challenge does not yet exist (control logic manipulation)
* Data integrity injection: the physics layer is in place but there is no confirmed attacker path
  that feeds false readings into the physics model as real sensor input (data integrity manipulation)
* Replay challenge: the deterministic physics makes power-and-light-sim well suited to replay
  (stable expected behaviour makes deviations detectable), but no replay infrastructure exists
  yet (replay attacks)
* MQTT broker: not present; adding one as a telemetry bus would enable wildcard subscription and
  false telemetry injection challenges at low cost (process intelligence, data integrity manipulation)
