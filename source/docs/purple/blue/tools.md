# Blue team tools and capabilities

Blue teams use diverse tools for monitoring, detection, response, and investigation. The list below covers the categories most blue teams need; the specific products in each category have alternatives, and the choice depends on existing infrastructure, budget, and the skill profile of the team that will operate them.

## Monitoring and logging

SIEM platforms: Splunk, Elastic Stack, Microsoft Sentinel, LogRhythm.

Log aggregation: Fluentd, Logstash, Graylog.

Cloud logging: AWS CloudWatch, Azure Monitor, Google Cloud Logging.

Centralised authentication logs: Windows Event Forwarding, Syslog.

## Endpoint protection

EDR solutions: CrowdStrike Falcon, Microsoft Defender for Endpoint, SentinelOne, Carbon Black.

Anti-malware: traditional AV plus next-generation protections.

Host-based firewalls: Windows Firewall, iptables, pf.

Application control: AppLocker, Carbon Black App Control.

## Network monitoring

IDS/IPS: Snort, Suricata, Zeek (Bro).

Network traffic analysis: Wireshark, tcpdump, NetworkMiner.

DNS monitoring: passive DNS, DNS query logging and analysis.

Proxy logs: web proxy logs for HTTP and HTTPS visibility.

## Threat intelligence

Threat intelligence platforms: MISP, ThreatConnect, Anomali.

OSINT feeds: Abuse.ch, AlienVault OTX, VirusTotal.

Commercial feeds: vendor-specific threat intelligence.

ISACs: sector-specific information sharing.

## Investigation and forensics

Memory forensics: Volatility, Rekall.

Disk forensics: FTK, EnCase, Autopsy.

Network forensics: NetworkMiner, Moloch.

Timeline analysis: Plaso, log2timeline.

Malware analysis: REMnux, FlareVM, sandbox environments.

## Orchestration and automation

SOAR platforms: Splunk SOAR (Phantom), Palo Alto XSOAR (Demisto), Microsoft Sentinel automation.

Playbook frameworks: TheHive, WALKOFF.

Scripting and APIs: Python and PowerShell for custom automation.

## Related

- [The blue team mission](mission.md)
- [Detection, response, and recovery](detect-recover.md)
- [Red team tools and techniques](../red/tools.md)
- [SOC detection](../../incident-response/soc/detection.md)
