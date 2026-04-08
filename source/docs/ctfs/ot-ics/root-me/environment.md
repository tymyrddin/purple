# Environment

Root-Me challenges in this section use `ics-simlab`. 

- Network and Forensic challenges use individual ics-simlab components to generate artefacts locally. 
- Realist challenges deploy the full environment to Root-Me's infrastructure via Docker Compose (if possible).

## Host requirements

| Component         | Specification                              |
|:------------------|:-------------------------------------------|
| OS                | Linux (Ubuntu 22.04 or Debian 12)          |
| Docker            | Engine 24+, Compose v2.20+                 |
| Python            | 3.12+ (orchestrator and component scripts) |
| RAM (minimum)     | 4 GB                                       |
| RAM (recommended) | 8 GB                                       |
| CPU               | 2 cores minimum, 4 recommended             |
| Disk              | 10 GB minimum, 20 GB recommended           |

## Running ics-simlab

The orchestrator generates all Docker Compose files and firewall rules from a single YAML
configuration in `orchestrator/ctf-config.yaml`. All three zones start from a single
`make` workflow.

```
make generate    # generate compose files and firewall rules from config
make build       # build all zone images
make up          # start containers and jump-host
make firewall    # apply inter-zone iptables rules (requires sudo)
```

For a narrowed scope (fewer zones), edit `ctf-config.yaml` before running `make generate`.
Changing zone scope after building requires rebuilding the affected images.

## Generating artefacts for Network and Forensic challenges

Start only the component(s) required. Capture traffic with `tcpdump` or Wireshark during
exploitation. Stop the component after capture. The full environment does not need to be
running.

## Realist challenge deployment

The full environment (all three zones plus jump-host) can run on a single Linux host. Root-Me
provisions this from the submitted Docker Compose configuration. The jump-host provides the
participant entry point via SSH key authentication.
