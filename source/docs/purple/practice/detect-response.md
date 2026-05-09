# Detection and response

Purple teaming turns red team attacks into blue team improvements. The mechanism is simple to describe and slow to do well: every observed technique is a hypothesis about what the defence can detect, and the exercise is the test of that hypothesis.

## Building detections from attacks

The starting material is what the red team did and what was visible while they did it. Specific commands executed, file paths created, registry keys touched, network connections made, and the process trees that hold the relationships between them.

Translating those observations into SIEM rules is a craft rather than a transcription. A correlation rule that fires on LSASS access combined with suspicious module loads is more useful than a rule that fires on either alone, because the combination matches a technique while either signal alone produces noise. Including time, user, and asset context in the rule reduces false positives at the cost of some adaptability when the technique varies.

EDR behavioural rules work better when oriented to the technique rather than the tool. A rule that detects credential dumping behaviour catches the technique whether the tool is Mimikatz, a custom binary, or a procedure that nobody has named yet. A rule that detects Mimikatz only catches Mimikatz.

A new detection is a hypothesis until it has been retested. The next exercise validates whether the new rule fires when the technique is run again, in a slightly different way, against a slightly different target. Without that validation, the rule is documentation rather than capability.

## Testing what coverage actually means

Coverage testing maps tested techniques to MITRE ATT&CK and identifies which produce alerts. The framework is useful, but the coverage percentage is a metric that decouples easily from defensive value: a programme can claim 80% coverage while remaining blind to the 20% an actual adversary would use.

True positive validation asks whether alerts fire for the activity they were designed to fire for, not just for activity that happens to share a feature with the attack. Reducing false positives is necessary; ensuring the alert contains enough context that an analyst can act on it under the time pressure of an actual incident is what turns the alert from noise into capability.

Detection speed is worth measuring once the alert is reliable. Time from action to alert depends on log processing latency, correlation interval, and the queueing behaviour of the SIEM. Each of these is something purple team exercises can surface that ordinary operational testing cannot.

## Validating response procedures

Detection without response is documentation. Exercises test the response side too: whether documented procedures are clear enough to follow under pressure, whether handoffs between SOC, IR, and IT operations work as the diagrams suggest, whether the escalation path arrives at someone who can act and not just someone who can pass the call along.

Recovery is the part most often skipped because it is the slowest. An exercise that tests containment without testing whether systems can be restored cleanly produces false confidence. Testing a backup-and-restore procedure for the first time during the actual incident the procedure was written for is the wrong moment to find out whether it works.

## Common detection gaps

Living-off-the-land techniques, native Windows tools used maliciously such as PowerShell, WMI, and PsExec, evade detections oriented to recognisable malware.

Cloud environments often have insufficient logging of API activity and missed visibility on IAM changes. The attack surface is different and the defensive baseline often lags the operational migration.

Encrypted traffic creates blind spots in HTTPS inspection, in cloud service access, and in encrypted command-and-control channels.

Insider threats are the legitimate use of legitimate accounts for malicious purposes. Detection here depends more on behavioural baselines than on rules.

Supply chain compromise, the trusted third party with legitimate access doing something the agreement did not anticipate, is structurally hard to detect because the access is correctly authorised.

## Related

- [Coordination models](../coordination.md)
- [SOC detection](../../incident-response/soc/detection.md)
- [Building a phishing programme that actually works](../../social-engineering/phishing-programme.md)
- [Applying SEM to security](../../foundations/system-effectiveness/applying-sem.md)
