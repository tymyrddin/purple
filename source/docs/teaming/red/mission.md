# The red team mission

Red teams exist to challenge assumptions about security. Not to break things for fun, but to show where defences fail 
under realistic attack conditions.

## What red teaming is

Adversary emulation: Replicating tactics, techniques, and procedures (TTPs) of real threat actors relevant to your 
organisation. Not random exploitation, but purposeful simulation of how actual adversaries would operate.

Objective-driven testing: Every engagement has clear goals. Steal specific data, gain domain admin, persist 
undetected for 30 days, move laterally to OT systems. Success means achieving objectives despite defences, 
not just finding vulnerabilities.

Realistic tradecraft: Using the same tools, techniques, and operational security practices that real attackers use. 
Command and control infrastructure, living-off-the-land binaries, social engineering, physical access attempts.

Evidence collection: Documenting every action, timestamp, and technique used so blue team can understand exactly 
what happened and build better detections.

## What red teaming is not

Vulnerability scanning is useful, but it is not red teaming. Red team operations assume vulnerabilities 
exist and focus on exploitation paths and defensive gaps.

Penetration testing finds individual weaknesses. Red teaming chains multiple techniques together to 
achieve strategic objectives, testing entire defensive programmes rather than individual controls.

It is not about breaking things. Causing outages or destroying data is not the goal. Red team operations 
maintain operational security and avoid disruption while still testing defences realistically.

It is also not about surprise attacks: Effective red teaming requires coordination with defenders or at least clear 
rules of engagement. Completely surprising your own organisation rarely produces useful learning.

