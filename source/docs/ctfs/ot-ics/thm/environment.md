# Environment selection

TryHackMe VMs run on 0.5-1 GiB RAM and 1 CPU core. This is not a soft constraint. It is the hard ceiling that
determines which simulation approach is viable.

## Option 1: single-process simulation

* `power-and-light-sim`
* No Docker
* Lowest friction, lowest failure rate

This is the default choice. If the challenge can be built with it, use it.

## Option 2: micro-Docker setup

* 2 to 3 containers maximum
* Only if protocol separation is the point of the challenge

Anything larger becomes a debugging exercise in why nothing starts under 1 GB RAM.

Lock this decision before touching VMware. Changing it later means rebuilding the VM.
