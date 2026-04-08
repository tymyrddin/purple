# Workflow

This workflow is being derived from designing [Dead Reckoning](room-reckoning.md) and [Double Strike](room-double-strike.md).
Both rooms use `power-and-light-sim` as a single-process Python service, no Docker. Each room is
a separate VM. The steps below apply to both unless noted.

## Phase 1: Work from a copy of the simulator

Clone `power-and-light-sim` to a per-room working copy. Do not build against the upstream repo
directly. Both rooms require changes to simulator configuration and to simulator code: flag values
embedded in protocol responses, physics engine callbacks, and port and device layout differ between
rooms. Track all changes in the working copy so the build is reproducible, and so nothing
unfinished lands back upstream.

## Phase 2: Map the room design to simulator capabilities

Before touching the VM, determine what each flag requires from the simulator:

* Flags that live in YAML config: port numbers, register definitions, device names, OPC UA
  node descriptions
* Flags that require Python code changes: anything embedded in a protocol response field that
  YAML does not expose (OPC UA server description, IEC-104 quality descriptor, physics engine
  register writes triggered by a condition)

Reckoning flag 4 and Double Strike flag 4 both require the physics engine to write a value into a register
or data object when a condition is met. That is a code change to `TurbinePhysics` or
`GridPhysics`, not a YAML entry.

Cross-check against [SIMULATOR_GAPS.md](https://github.com/tymyrddin/power-and-light-sim/blob/main/SIMULATOR_GAPS.md) for known issues on the relevant protocols before
committing to a flag placement that relies on a partially implemented code path.

## Phase 3: Make the simulator changes

In the working copy:

* Adjust YAML for protocol ports, device layout, and register or object definitions per the room
  design
* Modify Python source where flag placement requires it: OPC UA server initialisation, physics
  engine event callbacks, IEC-104 data object construction
* Confirm changes work locally before building the VM; iterating inside a running VM takes much
  longer

For Double Strike, write the wiper script against the simulator's config and event log paths as they
will exist inside the VM. Confirm those paths now. ;-)

## Phase 4: Build the VM

VMware VM, Debian 8 compatible, BIOS boot, DHCP. Install dependencies per [noted requirements](reqs.md). Copy the
modified simulator into the VM; do not clone at runtime. Vendor all Python dependencies into a
local directory inside the VM with `pip install --find-links` so the VM has no internet
dependency at runtime.

## Phase 5: Room-specific additions

Dead Reckoning needs nothing beyond the simulator.

Double Strike needs:

* Flask portal on port 8080: single-route app, static document containing the substation IP
  range reference; default credentials discoverable via source comment or response header.
* Wiper script on the filesystem, not triggered automatically, placed where normal exploration
  finds it.
* Backup configuration copy at a non-obvious path, written during the VM build; this is the
  flag 5 location, a build-time placement.

## Phase 6: Startup and determinism

Register `power-and-light-sim` (and the Flask portal for Double Strike) as `systemd` services. Boot the
VM cold and confirm all services come up without intervention. If services race under memory
contention, add a startup delay.

## Phase 7: Test under constraint

Throttle to 1 CPU and 512 MB RAM. Run the full attack path from zero knowledge.

Dead Reckoning: scan, OPC UA anonymous browse, Modbus register read, governor setpoint write, overspeed
flag.

Double Strike: portal credentials, internal document, IEC-104 interrogation, state read, breaker
command, wiper find and trigger, backup recover.

Then test restart and partial startup. Fix anything that breaks before moving on; problems that
surface here will surface again inside TryHackMe's infrastructure, with no shell access to debug
them.

## Phase 8: Close unintended paths

Remove SUID binaries not on the attack path. Verify only the intended ports are listening.

## Phase 9: Optimise and stabilise

Remove build tools and pip cache. Compress build-phase logs. Confirm identical state after a
cold reboot: same register values, same flag locations, same service state.

## Phase 10: Export and validate

Shut down cleanly. Export to OVF from VMware, import into VirtualBox, export as OVA. Re-import
the OVA and run the full attack path again before submitting.

## Phase 11: Integrate with TryHackMe

Upload the OVA. Create the room, map tasks to attack stages per the room design, attach the VM.
Use `machine_ip` as the platform variable for the target IP.

## Phase 12: Write the solution

Document the intended path: commands, expected outputs, reasoning. Align with the room design,
not with whatever accidental path worked during testing.