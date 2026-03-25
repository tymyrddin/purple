# Defensive mindset and methodology

Blue teamers think about defence-in-depth, detection opportunities, and resilient systems. Understanding this mindset helps both blue and purple teams work more effectively.

## Think like a defender

Assume breach: Defences will be bypassed. Focus on detection and response, not just prevention. Visibility and speed matter more than perfect perimeter security.

Defence-in-depth: Multiple overlapping controls. If one layer fails, others catch the attack. Prevention, detection, and response work together.

Visibility first: Can't defend what you can't see. Logging, monitoring, and instrumentation enable everything else. Blind spots are where attackers hide.

Prioritise by impact: Not all systems matter equally. Focus defensive resources on crown jewels: critical systems, sensitive data, key services.

Continuous improvement: Every incident teaches lessons. Every purple team exercise reveals gaps. Mature defences evolve based on real-world feedback.

## The defensive lifecycle

Blue team operations follow a continuous cycle:

1. Prepare

Build defensive capabilities before incidents occur: deploy monitoring and detection systems, establish incident response procedures, configure logging and alerting, harden systems and reduce attack surface, train personnel on security practices.

Preparation determines how well you respond when attacks happen.

2. Detect

Identify security incidents as early as possible: monitor security alerts and events, analyse logs for suspicious activity, correlate events across systems, validate alerts to reduce false positives, hunt proactively for undetected threats.

Mean time to detect (MTTD) is a critical metric. Faster detection limits damage.

3. Respond

Contain and remediate confirmed incidents: isolate affected systems, preserve evidence for investigation, eradicate attacker presence, restore systems from clean backups, coordinate across teams (IT, legal, communications).

Mean time to respond (MTTR) determines how much damage occurs.

4. Recover

Return to normal operations safely: validate systems are clean before restoration, implement additional monitoring for reinfection, test recovered services, communicate status to stakeholders, document incident thoroughly.

Recovery proves resilience. Fast, complete recovery limits business impact.

5. Learn

Improve defences based on incident lessons: conduct post-incident review, identify detection gaps that allowed incident, update detection rules and playbooks, implement preventive controls, share intelligence with broader community.

Learning from failures prevents recurrence and strengthens defences.
