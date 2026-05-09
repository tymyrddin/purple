# Building red team capability

A red team capability matures over time. There is no need to start with elite operators. The early work uses pre-built frameworks and known techniques against known defences; sophistication is something that gets added as the programme has somewhere productive to put it.

## Starting point

The first months of a red team capability are about establishing a rhythm with the blue team rather than demonstrating advanced tradecraft. [Atomic Red Team](https://www.atomicredteam.io/) and similar frameworks run pre-built attack simulations that test detection capabilities without requiring custom exploit development. The point of using them is calibration, not display.

Common attack paths cover most of what early exercises need to surface: phishing, credential abuse, lateral movement with stolen credentials, privilege escalation through misconfigurations. These are the techniques real adversaries use most often, and they are also the techniques whose defensive coverage organisations most commonly overestimate.

Collaborative exercises with the blue team, where attacks are announced and techniques are shared in real time, produce the conditions for the practice to become routine. Once those conditions exist, the move toward less-disclosed exercises happens naturally.

## Developing capabilities

Threat-intelligence-driven exercises replace the generic frameworks. Real adversary techniques relevant to the organisation's sector are studied and replicated, which makes the exercises more realistic and the findings more directly actionable.

Custom tooling fills gaps the off-the-shelf frameworks do not address. An organisation with unusual technology, unusual exposure, or unusual constraints will eventually need exercises that test those specifics, which off-the-shelf playbooks cannot provide.

Scope expansion adds dimensions the early exercises avoided. Social engineering, physical access, and supply chain attack simulations test parts of the organisation that pure technical testing leaves untouched, and they produce findings that no technical exercise would surface.

Operational security shifts from noisy and obvious to stealthy and adversary-realistic. The exercises start to test how detection holds up against techniques designed to avoid detection rather than against techniques that announce themselves.

## Advanced operations

Full adversary emulation replicates a specific threat actor end-to-end, from reconnaissance through impact. The exercise behaves as the named adversary would, using their tooling preferences and operational patterns. Findings translate directly to defences against that adversary.

Assumed-breach scenarios start with access already obtained and test detection, response, and recovery under realistic compromise conditions. The earlier phases (reconnaissance, initial access) are taken as given so that the exercise can reach the post-compromise activity that is otherwise often skipped.

Continuous adversary simulation uses automated red team tooling to feed scenarios into the blue team's environment continuously, with detection tuning happening alongside. This is the configuration most likely to be called "purple team automation", and it is the maturity stage most organisations underestimate the cost of.

A purple team service inside the organisation, when fully developed, continuously challenges and improves the security posture as a built-in function rather than as a periodic event. Few organisations reach this stage; the ones that do usually arrive through a long sequence of smaller capabilities rather than through a single deliberate investment.

## Related

- [Building blue team capability](../blue/capability.md)
- [Defensive skills for attackers](../../foundations/montessori/defensive-skills.md)
- [Rotation programmes](../../foundations/montessori/rotation.md)
- [Building a purple team programme](../purple-team/team.md)
