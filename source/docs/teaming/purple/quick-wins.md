# Quick wins for starting small

Don't wait for perfect conditions. Start with simple exercises that build capability and demonstrate value.

## Week 1: Phishing simulation

Red team: Send realistic phishing emails to small group. Track who clicks links or submits credentials.

Blue team: Monitor email security alerts, authentication logs, unusual web traffic. Practice response to compromised credentials.

Learning: Do security awareness training and email filtering work? Can blue team detect credential submission? How quickly can compromised accounts be disabled?

## Week 2: Atomic Red Team test

Red team: Run pre-built Atomic Red Team tests for common TTPs (credential dumping, persistence mechanisms).

Blue team: Monitor EDR, SIEM for alerts. Investigate and respond to detected activity.

Learning: What does your EDR actually detect? Which MITRE ATT&CK techniques are visible? Where are blind spots?

## Week 3: Lateral movement simulation

Red team: Simulate attacker with compromised account attempting lateral movement to additional systems.

Blue team: Monitor authentication attempts, unusual access patterns, account usage across multiple systems.

Learning: Can blue team detect lateral movement? How quickly? What network segmentation or access controls limit attacker options?

## Month 2: Assumed breach scenario

Red team: Start with provided credentials (simulating successful phishing). Attempt privilege escalation and access to sensitive data.

Blue team: Monitor for privilege escalation attempts, sensitive data access, suspicious account behaviour.

Learning: If attacker gets initial access, how far can they go? What detections catch post-compromise activity?

## Quarter 2: Full engagement

Red team: Multi-stage attack from initial access through objectives (data exfiltration, system persistence, impact demonstration).

Blue team: Full incident response including detection, containment, eradication, recovery.

Learning: Does complete defensive program work end-to-end? What breaks under pressure?
