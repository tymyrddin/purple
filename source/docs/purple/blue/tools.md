# Blue team tools and capabilities

Blue teams use diverse tools for monitoring, detection, response, and investigation.

## Monitoring and logging

- SIEM platforms: Splunk, Elastic Stack, Microsoft Sentinel, LogRhythm
- Log aggregation: Fluentd, Logstash, Graylog
- Cloud logging: AWS CloudWatch, Azure Monitor, Google Cloud Logging
- Centralised authentication logs: Windows Event Forwarding, Syslog

## Endpoint protection

- EDR solutions: CrowdStrike Falcon, Microsoft Defender for Endpoint, SentinelOne, Carbon Black
- Anti-malware: Traditional AV plus next-gen protections
- Host-based firewalls: Windows Firewall, iptables, pf
- Application control: AppLocker, Carbon Black App Control

## Network monitoring

- IDS/IPS: Snort, Suricata, Zeek (Bro)
- Network traffic analysis: Wireshark, tcpdump, NetworkMiner
- DNS monitoring: Passive DNS, DNS query logging and analysis
- Proxy logs: Web proxy logs for HTTP/HTTPS visibility

## Threat intelligence

- TIP (Threat Intelligence Platforms): MISP, ThreatConnect, Anomali
- OSINT feeds: Abuse.ch, AlienVault OTX, VirusTotal
- Commercial feeds: Vendor-specific threat intelligence
- ISACs: Sector-specific information sharing

## Investigation and forensics

- Memory forensics: Volatility, Rekall
- Disk forensics: FTK, EnCase, Autopsy
- Network forensics: NetworkMiner, Moloch
- Timeline analysis: Plaso, log2timeline
- Malware analysis: REMnux, FlareVM, sandbox environments

## Orchestration and automation

- SOAR platforms: Splunk SOAR (Phantom), Palo Alto XSOAR (Demisto), Microsoft Sentinel automation
- Playbook frameworks: TheHive, WALKOFF
- Scripting and APIs: Python, PowerShell for custom automation
