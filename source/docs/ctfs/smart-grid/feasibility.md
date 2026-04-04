# Feasibility

## What is blocking progress

No smart grid simulator exists yet. The challenges described in this section cannot be packaged until one
does. That is the single largest dependency, and it determines the order of everything else.

The specific gaps:

* No IEC 61850 implementation in power-and-light-sim or ics-simlab. GOOSE, SV, and MMS require
  a dedicated simulation layer built on libiec61850 or equivalent.
* No DLMS/COSEM implementation for the metering layer.
* No grid topology model connected to either. Protocol behaviour without a connected physical model
  produces challenges where the flag is "command accepted", not "breaker opened" or "meter disconnected".

## The layer 2 problem

GOOSE operates at Ethernet layer 2, not IP. Standard Docker bridge networks do not forward layer 2
multicast. Any challenge involving GOOSE replay or injection requires either:

* macvlan or ipvlan Docker networking, which adds host configuration complexity
* A dedicated network namespace per challenge instance
* A software bridge that forwards Ethernet multicast explicitly

This is solvable, but it rules out a simple Docker Compose submission to Root-Me without additional
infrastructure. TryHackMe is not viable for the same reason, compounded by the RAM ceiling. Self-hosted
on Hetzner is the realistic platform for any IEC 61850 challenge.

DLMS and IEEE C37.118.2 both run over TCP/UDP and do not share this constraint.

## What needs to be built first

In order:

1. A grid topology model (OpenDSS or pandapower) with enough components to make consequences visible:
   at minimum a substation with one or two feeders, a set of meters, and observable physical state.
2. An IEC 61850 layer on top: GOOSE publisher/subscriber, SV stream, MMS server on the simulated IEDs.
3. A DLMS/COSEM server representing the AMI head-end and at least one meter.
4. A challenge harness that resets state between runs and places flags in protocol-reachable locations.

Steps 1 and 2 together are roughly the scope of a new simulator repository.

## Platform verdict

| Challenge type                 | Viable platform                        |
|:-------------------------------|:---------------------------------------|
| DLMS/COSEM metering challenges | Root-Me (Docker, TCP-based)            |
| IEEE C37.118.2 PMU challenges  | Root-Me (Docker, TCP-based)            |
| IEC 61850 GOOSE/SV challenges  | Self-hosted Hetzner only               |
| IEC 61850 MMS challenges       | Root-Me viable if layer 2 not required |

The DLMS and MMS challenges can move forward once the simulator exists. The GOOSE and SV challenges
require the Hetzner hosting work to be in place as well.
