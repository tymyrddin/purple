# Defensive skills for attackers

A red team member who understands defence operates more realistically and gives more useful feedback. Learning how
detection, response, and monitoring actually work reveals where attacks are visible and how to test in a way that tells
the defender something.

## Defensive skill as an offensive asset

Knowing what monitoring exists is what makes an operation realistic; it is the difference between testing the gaps that
count and burning effort on techniques no defender could ever catch. It also sharpens feedback. "We got domain admin"
is a good deal less useful than "lateral movement over WMI went undetected, because X." Speaking the blue team's
language, and understanding their constraints, tools, and priorities, [turns an engagement into a collaboration](../../purple/running-the-loop.md) rather
than a scorecard. And over a career, red teamers who understand defence often make better leaders and architects,
having seen both halves of the board.

## Core defensive concepts

The ground to cover is roughly four-layered. [Detection spans the network](../../incident-response/soc/detection.md) (IDS/IPS, NDR), the endpoint (EDR, AV), the
application (logs, APM), identity (authentication monitoring), and cloud (cloud-native SIEM). Response runs through
triage, containment, eradication, and recovery, and carries its own logic, which is why defenders cannot simply "delete
the malware" and move on. Operational constraints are the texture of the work: round-the-clock monitoring limits, alert
fatigue, false positives, competing priorities, thin resources. And visibility has edges worth knowing: what gets
logged and what does not, how long it is kept, what a SIEM query can and cannot reach, and where blind spots lie.

## Hands-on exercises

A [day in the SOC](rotation.md), around eight hours, puts a red team member alongside an analyst through a full shift: reviewing
alerts, investigating suspicious events, working the SIEM and EDR tooling, sitting in on incident response, and feeling
the actual workload. What it teaches is which detections genuinely work, how long an investigation really takes, what
information helps and what merely adds noise, and the operational pressure the SOC lives under.

Building detection rules, perhaps four hours, turns the offensive knowledge around. Mapping red team techniques to MITRE
ATT&CK, finding the detection opportunities, writing correlation rules, and testing them against benign activity
surfaces how hard detection engineering is, how stubborn the false-positive problem can be, what data the rules depend
on, and how to test without setting off production alerts.

An incident response drill, around three hours, casts the red team member in the blue role for a tabletop or simulation:
responding to a simulated attack, following the playbook, coordinating across teams, and making containment calls. The
lesson is in the complexity of response, the weight of decisions made under pressure, and how much of it is
communication and recovery rather than technical cleverness.

A threat hunt, another four hours or so, runs a proactive search with blue team tools: forming a hypothesis, working
through logs and telemetry, analysing what turns up, documenting the hunt, and writing detection rules from it. It
builds hypothesis-driven investigation, data-mining instincts, a sense of what makes an indicator useful, and the habit
of documenting a hunt so others can follow it.

## Tools worth knowing

The toolkit overlaps heavily with the blue team's. SIEM platforms such as Splunk, Elastic, and Sentinel, with their
query languages and correlation and dashboarding. EDR tools such as CrowdStrike, Defender, and SentinelOne, with their
investigation interfaces and response actions. Log analysis across Windows Event Logs, Sysmon, Linux, and cloud provider
logs. The basics of forensics: disk, memory, timeline, evidence preservation. And threat intelligence: the platforms,
the IOC formats, STIX/TAXII, and actor profiling.

## Carrying it into offensive work

The payoff lands at each stage of an engagement. Beforehand, reviewing the defensive capabilities and the monitoring on
the ground lets operations be planned around realistic gaps. During, detection opportunities are worth noting as they
pass, along with whatever goes unseen. Afterwards, the most valuable feedback is detection-focused: where exactly the
blue team could have caught the activity, and help writing the rules that would let them.

