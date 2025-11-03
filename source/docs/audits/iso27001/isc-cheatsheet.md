#  Cheat sheet information security controls

## Control types by function

These categories describe when and how controls operate in relation to security incidents.

| Control type | Goal                                   | Examples                                                                                                    |
|--------------|----------------------------------------|-------------------------------------------------------------------------------------------------------------|
| Preventive   | Stop incidents before they happen      | Security policy, confidentiality agreements, cryptography, environment segregation, access control software |
| Detective    | Identify incidents quickly             | Audit logs, intrusion detection systems, monitoring, alarms, video surveillance, reconciliation checks      |
| Corrective   | Minimise impact and prevent recurrence | Patching, backup recovery, incident investigation, business continuity plan activation, system restoration  |

## Control types by scope

These categories describe where and at what level controls are applied within the organisation.

| Control type | Goal                                                    | Examples                                                                                       |
|--------------|---------------------------------------------------------|------------------------------------------------------------------------------------------------|
| Management   | Align ISMS with organisational strategy                 | Risk management, management reviews, continual improvement, policy definition                  |
| General      | Baseline security mechanisms for all systems            | Annual review of user access, baseline security controls from ISO/IEC 27001 Annex A            |
| Specific     | Controls embedded in individual applications or systems | Application authentication, transaction validation, access mechanisms for specific ERP systems |

## Relationships at a glance

* Assets → have vulnerabilities
* Threats → exploit vulnerabilities → create risk scenarios
* Controls → address vulnerabilities and mitigate risk
* Limitation: Controls reduce risk but cannot eliminate all threats (the mountain will always have rocks)

Visual representation:

```
         Exploit
[Threats] -------> [Vulnerabilities] -------> [Assets at Risk]
                          ↑
                          |
                     [Controls]
                      (address)
                          ↓
                    [Reduced Risk]
```

This shows how controls act like climbing gear on the ISO 27001 mountain: they help protect assets and reduce risks, 
but cannot stop the mountain itself from having rocks or avalanches (threats).

## TL;DR

* Controls are interrelated: Antivirus software is preventive (blocks malware), detective (identifies infections), and corrective (removes threats) at the same time.
* Two classification dimensions: A single control can be both "Preventive" (function) and "General" (scope). For example, a password policy prevents unauthorised access and applies generally across all systems.
* Management vs General vs Specific: Management controls align strategy and governance, general controls ensure baseline security across the organisation, and specific controls apply to particular systems and processes.
* Goal-oriented: Each functional control type focuses on a clear purpose — prevent incidents, detect them quickly, or correct them effectively.
