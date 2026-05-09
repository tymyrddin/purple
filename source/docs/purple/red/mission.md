# The red team mission

A red team exists to challenge assumptions about security. Not to break things for fun, but to show where defences fail under realistic attack conditions.

## Red teaming

Adversary emulation is the core of the work. Replicating the tactics, techniques, and procedures of real threat actors relevant to an organisation, rather than running random exploitation, produces findings that map onto the threat the organisation is actually facing.

Objective-driven testing keeps the work focused. Each engagement has clear goals: stealing specific data, gaining domain admin, persisting undetected for thirty days, moving laterally to operational technology systems. Success means achieving objectives despite defences, not merely finding vulnerabilities.

Realistic tradecraft uses the same tools, techniques, and operational security practices that real attackers use. Command-and-control infrastructure, living-off-the-land binaries, social engineering, and physical access attempts are all in scope where they reflect a relevant adversary's behaviour.

Evidence collection is what turns the exercise into something the blue team can act on. Every action, every timestamp, every technique is documented so that defenders can understand exactly what happened and build better detections from it.

## Common confusions

Vulnerability scanning is useful, but it is not red teaming. Red team operations assume vulnerabilities exist and focus on exploitation paths and defensive gaps.

Penetration testing finds individual weaknesses. Red teaming chains multiple techniques together to achieve strategic objectives, testing entire defensive programmes rather than individual controls.

The work is not about breaking things. Causing outages or destroying data is not the goal. Red team operations maintain operational security and avoid disruption while still testing defences realistically.

It is also not about surprise attacks. Effective red teaming requires coordination with defenders or, at minimum, clear rules of engagement. Completely surprising an organisation rarely produces useful learning.

## Related

- [Offensive mindset and methodology](mindset.md)
- [Adversary emulation vs. vulnerability testing](adversary.md)
- [Coordinating with purple team](coordination.md)
- [Ethical boundaries and rules of engagement](ethics.md)
