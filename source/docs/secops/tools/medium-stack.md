# Medium organisation SecOps stack

Scope: 50–500 employees, dedicated IT/Security staff, need more visibility and automation.

## Objectives

* Faster detection and triage
* Coordinated SOC/SIRT functions
* Structured case management and playbooks
* Integration of multiple data sources

## Components

* Wazuh: Central SIEM, endpoint monitoring.
* Zeek / Suricata: Network monitoring, anomaly detection.
* MISP: Full threat intelligence sharing (with peer orgs / EU CERT).
* TheHive + Cortex: SOAR layer for automated enrichment and workflow.
* OpenVAS / Greenbone: Vulnerability scanning.
* Automation: Ansible / StackStorm for repetitive containment and enrichment tasks.
* Dashboards / reporting: Grafana / Kibana for SOC/SIRT visibility.

## Back of the envelope

```
                       ┌───────────────────────┐
                       │ Endpoints & Servers   │
                       │       (Wazuh)         │
                       └─────────┬─────────────┘
                                 │ Logs & Alerts
                                 ▼
                       ┌──────────────────────┐
                       │     Wazuh SIEM       │
                       │ (central aggregation)│
                       └──────────┬───────────┘
                                  │ Alerts / Cases
               ┌──────────────────┴─────────────────┐
               │                                    │
          ┌────▼──────┐                        ┌─────▼────────┐
          │ TheHive   │                        │ MISP         │
          │ Case Mgmt │                        │ Threat Intel │
          └────┬──────┘                        └────┬─────────┘
               │                                    │
               │                                    │
       Enrichment / Automation <────────────────────┘
               │
          ┌────▼──────┐
          │ Cortex    │
          │ Automation│
          └────┬──────┘
               │ Playbook execution
   ┌───────────▼─────────────┐
   │ Ansible / StackStorm    │
   │ Response & Orchestration│
   └───────────┬─────────────┘
               │
   ┌───────────▼────────────┐
   │ Zeek / Suricata        │
   │ Network Monitoring     │
   └───────────┬────────────┘
               │ Logs & Alerts
   ┌───────────▼────────────┐
   │ OpenVAS / Greenbone    │
   │ Vulnerability Scans    │
   └────────────────────────┘
```

## Notes

* This is a full SOC/SIRT–style stack but still entirely EU open-source friendly.
* Automation reduces repetitive work while keeping humans in the loop.
* Modular: can add more log sources or sensors as the org grows.

```{raw} html
<div class="page-post-card__link">
    <a href="https://tymyrddin.dev/contact/">
      Streamline your SOC/SIRT with our help
    </a>
</div>
```