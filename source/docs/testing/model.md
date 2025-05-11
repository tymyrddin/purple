# Threat-modelled adversary emulation

## Step 1: Threat profile development

1. Industry: Financial Services  
2. Adversaries:  
   - FIN7 (Tactics: T1078, T1059, T1204)  
   - Lazarus (Tactics: T1053, T1547, T1021)  
3. Critical Assets: SWIFT terminals, trader workstations  

## Step 2: Build emulation plan

```yaml
# fin7-emulation.yaml  
techniques:  
  - T1078.004: # Valid Accounts  
    steps:  
      - "Compromise service account via phishing"  
      - "Establish persistence via scheduled task"  
  - T1059.005: # Visual Basic  
    steps:  
      - "Macro-enabled Excel doc with C2"  
```

## Step 3: Execute with Realism Constraints

```bash
# Caldera plugin for FIN7 TTPs  
python3 server.py --insecure --plugins threat_emulation/fin7
```
