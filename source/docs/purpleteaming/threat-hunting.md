# Threat hunting

Unlike the [Security Operations Center (SOC) and Incident Response (IR) teams](../soc/README.md), threat hunters not only respond to threats; they actively search for them. This process involves making hypotheses on the existence of potential threats, which are then either confirmed or disproven on the basis of collected data and analysis.

Threat hunting is also quite a different activity from either incident response or digital forensics. The purpose of [DFIR methodologies](blue-dfir:index) is to determine what happened after a breach was discovered. In contrast, when a team engages in threat hunting, the aim is to search for attacks that may have already slipped through the defensive layers.

Threat hunting also differs from penetration testing and vulnerability assessment. These attempt to simulate an attack, ask questions such as what 'could' happen if someone compromised security. Whereas threat hunters work from the premise that an attacker is already in the network and then look for indicators of compromise, lateral movement, and other tell-tale artifacts that may provide evidence of the attacker.