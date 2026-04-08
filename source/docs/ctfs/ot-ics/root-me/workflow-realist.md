# Realist challenges

Realist challenges deploy the full ics-simlab environment. The participant connects to a
running service and completes a defined objective. The submission to Root-Me is a Docker
Compose configuration, not an artefact.

The [full-chain runbook](runbooks/full-chain.md) is the concrete reference for the first
Realist challenge: a three-zone attack from jump-host entry to turbine emergency stop,
covering trust exploitation, data exfiltration, lateral movement, process intelligence, and state manipulation in sequence. This workflow follows that chain
as a running example.

See [workflow.md](workflow.md) for Network and Forensic challenge creation.

## Phase 1: Define the scenario and scope

Decide the attack chain, entry point, and flag location before touching the configuration.

Full chain: jump-host → legacy workstation → enterprise workstation → historian → engineering
workstation → turbine PLC estop. Three zones, five stages, one flag written to a turbine PLC
register by the physics engine when the estop fires. The flag is not present until the
turbine trips.

Scope the zones to the minimum needed. The full chain requires all three zones. A narrower
challenge (already inside the operational zone, objective is the historian) needs only the
operational zone and its dependencies.

## Phase 2: Configure ics-simlab

Edit `orchestrator/ctf-config.yaml` to set active zones and any scenario-specific values.
Place the flag in `ctf-config.yaml` as an environment variable passed to the relevant container:

```yaml
control_zone:
  turbine_plc:
    env:
      CTF_FLAG: "RM{your_flag_here}"
```

In `zones/control/components/turbine-plc/turbine_hil.py`, read `CTF_FLAG` from the
environment and write it to `HR[9]` (and `HR[10]` if needed) when the estop condition fires.
The flag is absent from `HR[9]` before the estop, present after.

Run `make generate` to produce all Compose files and firewall rules from the updated
configuration.

## Phase 3: Deploy locally and validate

```
make build && make up && sudo make firewall
ssh -i ~/.ssh/ctf_key moist@localhost -p 2222
```

Execute the full attack path from the jump-host, following the [full-chain runbook](runbooks/full-chain.md),
without consulting the solution. Confirm:

* The flag is absent from `HR[9]` before the turbine trips
* The flag is present after `modbus_write coil 0 1`
* No shortcut bypasses the intended pivot path: the engineering workstation's Modbus tools
  are the only route to the control zone from inside the environment

Test restart and partial startup. If the turbine PLC or historian fails to start cleanly
on the second boot, the challenge fails unpredictably in production. Reboot the host and
run `make up` again; confirm all services reach stable state before the participant can connect.

## Phase 4: Document the entry

README for participants:
* Entry point: SSH key, adversary username, host address
* Objective: retrieve the flag from the UU Power and Light control network
* Scenario framing: enough to understand the environment, nothing that hints at the path

For the full-chain challenge, the README states that the participant has an SSH key for the
UU P&L jump-host and knows the enterprise subnet. Nothing else. The network inventory, the
credentials file, and the engineering notes are all inside the environment.

Solution for Root-Me reviewers:
* Exact commands at each stage with expected outputs
* Flag location (`HR[9]` on 10.10.3.21, present only after turbine trips)
* Technique breakdown: trust exploitation (FTP/SMB legacy trust), data exfiltration (historian
  credential exfiltration), lateral movement (pivot via engineering workstation), process intelligence
  (PLC register read), state manipulation (estop write)
* Real-world reference: ICS-CERT ICSA-10-090-01, BlackEnergy/Ukraine 2015

## Phase 5: Resource and timing checks

ics-simlab on a single host requires at minimum 4 GB RAM. Confirm:

* All containers reach stable state within Root-Me's startup window (check `docker ps`
  health status after `make up`)
* The turbine physics engine is running and producing live values before the participant
  connects (read `HR[0]` from outside; it returns a non-zero RPM)
* Container restart resets all state cleanly: `HR[9]` is 0 after reboot, not the previous
  session's flag write

If services race on startup, add `depends_on` with `condition: service_healthy` in the
Compose file, or add a startup delay to the turbine PLC entrypoint.

## Phase 6: Package and submit

The submission contains the generated Docker Compose files, any modified source files,
the README, and the solution. Test the package on a clean Linux host before submitting.

Realist challenge reviews take longer than Network challenge reviews because Root-Me verifies
the environment deploys and the solution works on their infrastructure. Submit one Realist
challenge at a time until the first one clears review.

## A note on multiple Realist challenges

Root-Me flags are static per submission. The full-chain challenge covers the complete attack
path. The next Realist challenge uses the same infrastructure but a different endpoint, for
example IED relay threshold manipulation (control logic manipulation) instead of the turbine estop. The
participant reaches the engineering workstation by the same path, then pivots to the relay
rather than the PLC. Each challenge teaches a distinct technique; the series as a whole
covers the full depth of the environment.
