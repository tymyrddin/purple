# Platform assessment

Cloud CTF challenges need API surface. Before building anything, it is worth assessing what each hosting option
actually provides and where it breaks down.

## What cloud challenges require

The attack techniques in scope (IAM privilege escalation, bucket misconfiguration, Lambda credential exfiltration,
service account key abuse) all interact with cloud provider APIs. A challenge that cannot provide those APIs
teaches tool syntax at best. The participant learns to run a command, not to understand why it works.

At minimum, viable cloud challenge infrastructure needs:

* An API layer that behaves like the target cloud provider (AWS, GCP, Azure)
* Per-participant isolation, or at least per-session state that does not bleed across runs
* Enough compute to run the simulated services without collapse
* A teardown mechanism that actually fires

## Root-Me

Root-Me hosts Docker-based challenges in its Realistic category. A challenge packaged as a Docker Compose file
with LocalStack (AWS simulation) is technically submittable.

Viable for:

* Beginner-tier challenges using S3 and basic IAM (LocalStack basic services run under 1 GB)
* Network challenges that capture cloud API traffic as PCAP

Not viable for:

* Multi-service scenarios (LocalStack Pro services, cross-service pivots)
* GCP or Azure simulation (no equivalent to LocalStack with comparable coverage)
* Per-participant isolation: Root-Me does not provision separate environments per player

The practical ceiling is one service, one misconfiguration, one flag. That is a reasonable beginner challenge and
an unsatisfying intermediate one.

## TryHackMe

TryHackMe allocates 0.5-1 GiB RAM and 1 CPU core to uploaded VMs. LocalStack does not fit at any useful level of
functionality within those constraints. Cloud simulation on TryHackMe means writing a thin Python mock of an API,
which teaches participants to interact with your mock, not with cloud behaviour.

Not viable for cloud CTF challenges beyond cosmetic approximations.

## Self-hosted on Hetzner

Hetzner provides root VPS access at low cost with a straightforward API for provisioning and teardown.

A CX22 instance (4 vCPU, 8 GB RAM, around €5-6/month) comfortably runs LocalStack with Pro services enabled,
handles CTFd for challenge management, and has headroom for a few simultaneous participants. A CX32
(8 vCPU, 16 GB RAM) handles more concurrent load if challenges are shared rather than isolated.

Per-participant isolation is achievable two ways:

* Provision a fresh Hetzner instance per participant via the Hetzner Cloud API, run the challenge environment,
  tear it down after the session or on a timer
* Run isolated Docker networks per participant on a single host, which is simpler but shares the underlying system

Auto-destroy is straightforward: a systemd timer or a Lambda-equivalent (Hetzner's own scheduled actions, or a
small cron job) tears down the environment after a fixed window.

What this enables that platforms cannot:

* Realistic multi-service attack chains (Lambda to EC2, GCP SA key to project owner)
* GCP and Azure simulation alongside AWS
* State persistence across a session without reboot surprises
* Full control over what is exposed, what is logged, and what the participant can observe

The cost of self-hosting is setup and maintenance overhead. The benefit is a challenge environment that does not
require the participant to mentally translate from "this Docker mock" to "how this actually works".

## Recommendation

| Scenario                                                 | Option                                             |
|:---------------------------------------------------------|:---------------------------------------------------|
| Beginner single-service challenge for Root-Me            | Root-Me Docker with LocalStack                     |
| Intermediate or advanced multi-service challenge         | Self-hosted Hetzner                                |
| TryHackMe cloud challenge                                | Not recommended                                    |
| Workshop or team exercise with per-participant isolation | Self-hosted Hetzner with API-provisioned instances |

Start with Root-Me for the simpler challenges in the inventory. Build toward Hetzner as the complexity increases.
Running both in parallel is reasonable: Root-Me for breadth and discoverability, Hetzner for depth.
