# Small organisation SecOps stack

Scope: 1–50 employees, limited IT staff, low budget, but still wants structured security.

## Objectives

* Detect obvious threats
* Rapidly respond to incidents
* Keep tools simple and maintainable
* Focus on practicality over coverage

## Components

* Wazuh: Core log collection, integrity monitoring, alerts.
* MISP Lite or community feeds: Basic threat intelligence.
* TheHive (lightweight): Simple case tracking.
* EDR: Wazuh agents on endpoints.
* Optional network monitoring: Suricata/Zeek for key servers or critical network points.
* Automation: Minimal — only repetitive tasks like alert notification via email or chat.

## Back of the envelope

```
               ┌─────────────────────┐
               │ Endpoints & Servers │
               │     (Wazuh)         │
               └─────────┬───────────┘
                         │ Logs & Alerts
                         ▼
                 ┌────────────────┐
                 │ Wazuh SIEM     │
                 │ (central hub)  │
                 └───────┬────────┘
                         │ Alerts
                         ▼
                 ┌───────────────┐
                 │  TheHive      │
                 │ Case Tracking │
                 └───────┬───────┘
                         │
                         ▼
                 ┌───────────────┐
                 │  MISP Lite    │
                 │ Threat Intel  │
                 └───────────────┘
```

## Notes

* Focus is on “doable security”: log monitoring, IOC enrichment, light case tracking.
* Minimal automation to reduce complexity.
* Everything can run on a few EU-based servers or small cloud VM instances.

```{raw} html
<div class="page-post-card__link">
    <a href="https://tymyrddin.dev/contact/">
      Let’s secure your small organisation the smart way
    </a>
</div>
```
