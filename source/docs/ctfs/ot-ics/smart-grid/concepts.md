# Challenge concepts

## What is distinct about smart grid challenges

The power grid has two properties that generic OT/ICS challenges often lack: consequences that are
immediately observable (a breaker trips, a meter disconnects, a protection function misoperates), and a
protocol stack where the authentication model ranges from absent to misconfigured. Both of these are
valuable in CTF design.

The interesting design space is consequence-first. The technique (replay a GOOSE message, inject false SV)
is learnable from documentation. What is not obvious from documentation is what happens to the system when
the technique lands, and that is what the simulation needs to show.

## Concepts worth building

### IEC 61850 layer

* GOOSE replay to open a breaker: capture legitimate trip message, replay within timing window, observe
  breaker state change in simulation. Beginner-Intermediate. Requires layer 2 environment.
* MMS relay config exfiltration: access an IED via MMS, download the relay configuration file, extract
  the flag from the settings. Beginner. libiec61850 client provided.
* MMS settings write: connect to an IED, alter a protection threshold to desensitise overcurrent
  protection, demonstrate consequence. Intermediate.
* GOOSE suppression: prevent a legitimate protection trip from propagating by flooding or filtering
  GOOSE multicast. Advanced.

### Metering layer

* DLMS default key access: authenticate to a simulated meter using default DLMS keys, read consumption
  data. Beginner.
* Remote disconnect command: issue an authenticated disconnect command to a meter, observe supply cut
  in the simulation. Beginner-Intermediate.
* Tariff register manipulation: alter billing registers via authenticated DLMS access. Intermediate.

### Wide-area layer

* PMU false data injection: connect to a simulated PMU receiver, inject false phasor data, observe the
  effect on state estimation. Intermediate. Requires a receiver model.

## Challenge inventory

Pending. No smart grid simulator exists yet. See [resources](resources.md) for what needs to be
developed before any challenge can be built here.
