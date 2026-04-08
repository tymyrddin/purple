# Foundational resources

| Resource | Platform | Role |
|:---|:---|:---|
| [ics-simlab](https://github.com/tymyrddin/ics-simlab) | Root-Me | Dynamic ICS environment: multi-step, stateful scenarios with zones and pivoting |
| [power-and-light-sim](https://github.com/tymyrddin/power-and-light-sim) | TryHackMe | Deterministic ICS simulator: repeatable scenarios with physics engines |

Platform assignment follows from resource constraints. TryHackMe allocates 0.5-1 GB RAM and 1 CPU
core. The full ics-simlab stack runs 16 containers and requires 4-8 GB RAM. Root-Me runs Docker on
its own infrastructure with no such constraint.

Simulator details, component documentation, and done/feasible breakdowns are in the platform
sections: [Root-Me](root-me/resources.md) and [TryHackMe](thm/resources.md).
