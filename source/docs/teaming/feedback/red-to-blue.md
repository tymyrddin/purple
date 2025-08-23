#  Red → Blue: translating attacks into defences

## Actionable workflow

Document TTPs (Tactics, Techniques, Procedures)

Example format:

```
## [T1059.003](https://attack.mitre.org/techniques/T1059/003/) (PowerShell)  
- **Exploit Used:** `Invoke-Mimikatz` via trusted LOLBAS (Living-Off-The-Land Binaries)  
- **Detection Gap:** No alerts for `amsi.dll` bypass in Sysmon logs  
```

### Prioritize by impact

Use the DETT&CT framework:

    D = Detectability (Can we see it?)  
    E = Exploitability (How easy is it?)  
    T = Threat (Is it being used in the wild?)  
    T = Training (Do analysts understand it?)  
    & = AND  
    CT = Criticality (How bad is it if successful?)  

### Generate defensive artefacts

For SIEM: Sigma rule example:

```yaml
    title: AMSI Bypass Attempt  
    logsource:  
      product: windows  
      service: sysmon  
    detection:  
      selection:  
        EventID: 7  
        Image|endswith: \powershell.exe  
        LoadedDll|contains: \amsi.dll  
      filter:  
        Signature: Microsoft  
      condition: selection and not filter  
```

For EDR: Custom YARA rule to detect in-memory Mimikatz patterns.

## Tools

* [Atomic Red Team](https://atomicredteam.io/) → [Sigma Converter](https://github.com/Neo23x0/sigma)
* [MITRE D3FEND](https://d3fend.mitre.org/) for countermeasure mapping
