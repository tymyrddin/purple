# Requirements and constraints

TryHackMe's official documentation states: *Please submit only community challenge content (CTF) for public release, as walkthrough rooms are currently not being reviewed for public publishing. However, you are more than welcome to continue creating and experimenting with walkthrough rooms for personal use and share them privately with friends or colleagues.*

Users get a VM and an objective. And, we can build our own workshop from that, with questions and reflection.

## Constraints

| Constraint        | Specification                      |
|:------------------|:-----------------------------------|
| Host OS           | Ubuntu                             |
| Virtualisation    | VMware Workstation                 |
| Simulation base   | Docker or Python ICS simulators    |
| Development model | No dev VMs, only final VM is built |
| Scheduling        | Sequence only, no timelines        |

## Reality check

A few constraints deserve to be stated plainly, because they shape everything downstream:

* TryHackMe infrastructure is not built for ICS realism, it is built for disposable CTF boxes
* 0.5 to 1 GB RAM turns most “industrial simulations” into polite fiction
* Persistence is gone on reboot, so anything stateful needs to fake it convincingly
* Internet is off, so any dependency that quietly reaches GitHub will fail in a very unhelpful way

Translation: this is not a simulation of industry, it is theatre with just enough machinery to look convincing under dim lighting

## Technical constraints

| Requirement       | Specification                                                      |
|:------------------|:-------------------------------------------------------------------|
| Linux OS          | Debian versions up to Debian 8 only (newer versions not supported) |
| Windows OS        | Must boot from MBR partition                                       |
| Windows licensing | Do not activate Windows; TryHackMe uses AWS licensing              |
| Network           | NIC: DHCP only, not static IP                                      |
| Boot method       | BIOS, not UEFI (for Windows)                                       |
| RAM after upload  | Free users: 0.5 GiB; Premium users: 1 GiB                          |
| CPU after upload  | 1 core                                                             |
| Persistence       | No changes persist after reboot                                    |
| Internet access   | Disabled by default; request via support if needed                 |

### Critical resource warning

TryHackMe allocates only 0.5-1 GiB RAM and 1 CPU core to uploaded VMs. The full `ics-simlab` stack runs 16
containers and requires 4-8 GB RAM locally. Therefore:

- Do not attempt to run the full `ics-simlab` inside the TryHackMe VM
- Use `power-and-light-sim` (Python-based, lighter weight)
- Request a resource bump from TryHackMe support if the simplified environment still fails

