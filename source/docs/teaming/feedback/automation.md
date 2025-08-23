# Feedback loop automation

## Technical integration

### Automated reporting pipeline

Red Team: Logs attacks in structured format (e.g., JSON):

```json
    {
      "tactic": "TA0002 (Execution)",
      "technique": "T1059.003",
      "tool": "PowerShell",
      "bypassed_defenses": ["EDR-123"],
      "detection_quality": "low" 
    }
```
    
Blue Team: Ingests into ticketing system (Jira/Servicenow) with priority tags.

### Defence validation testing

Automated replay of attacks after mitigations are deployed:

```bash
# Example: Re-test PowerShell detection after EDR update  
atomic-red-team.exe -t T1059.003 --check  
```

## Tools

* [VECTR](https://github.com/SecurityRiskAdvisors/VECTR) for tracking test cases
* [Zeus Cloud](https://github.com/DenizParlak/Zeus) for auto-generating detection rules
