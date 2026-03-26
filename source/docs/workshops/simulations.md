# Simulations in practice

Simulations give participants a way to make decisions with consequences, observe the effects of those decisions, and ask why they happened. This is different from a tabletop exercise, where consequences are described, and different from a real incident, where the consequences cannot be rewound. The simulation sits between the two: it is safe enough to fail in and realistic enough that the failure is informative.

Three things simulations do that other formats cannot.

## Safe consequence space

In most security discussions, participants are cautious about naming the decision they would actually make. The political and emotional layers are present. Saying "I would prioritise availability over containment" in a meeting carries implications that the same choice in a simulation does not. The simulation creates a space where the choice can be made, its effects observed, and the reasoning examined without those implications.

This is the Montessori prepared environment applied to decision-making. The simulation arranges the materials so that participants can encounter what they need to encounter. The facilitator's job is not to tell them what the right decision was. It is to design the environment so that the wrong decision reveals itself.

## Surfacing assumptions

Every simulation is a model, and every model encodes assumptions. The assumptions a simulation forces into view are the ones participants hold about how the system works, who is responsible for what, and what constitutes a bad outcome. These assumptions are usually implicit until the simulation makes them consequential.

When a participant is surprised by a simulation outcome, that surprise is a finding. The attack path they did not anticipate, the cascade they did not expect, the political consequence they had not modelled: these are the things the simulation is for. A session that produces no surprises has either been designed without challenge or has confirmed that the group's model of the system is accurate. The first is a design failure. The second is genuinely useful to know.

## Mixed-audience engagement

Infrastructure crises and security incidents involve people who do not share a technical vocabulary. Executives, legal teams, operational staff, and technical responders need to engage with the same event from different positions. Most formats privilege one vocabulary. Simulations that are designed without jargon allow people at each level to engage from their own domain without needing to translate.

The debrief is where the different perspectives become productive. The technical participant who was focused on the attack path and the executive who was focused on the public statement were in the same scenario. The gap between what each of them noticed is the finding.

## The simulators

The following environments support different kinds of sessions. Each is most useful with a specific audience and a specific set of questions.

[The Patrician's Crisis simulator](https://github.com/tymyrddin/ankh-crisis-sim) simulates governing Ankh-Morpork's infrastructure under compounding failures, contested resources, and political pressure. It uses no technical vocabulary and is designed for mixed audiences including non-technical leadership. The debrief can attend to which trade-off decisions were made and which were deferred, and what that reveals about how the organisation prioritises under pressure.

[Power and Light simulator](https://github.com/tymyrddin/power-and-light-sim) is a static ICS/SCADA environment built in the same Ankh-Morpork setting. It supports technical audiences testing attack paths against realistic operational technology controls. The debrief can attend to which paths were not anticipated and what that reveals about the current threat model.

[Smart Grid simulator](https://github.com/tymyrddin/smart-grid-sim) demonstrates nation-state attack scenarios against smart grid infrastructure, with a focus on making the consequences visible to senior management audiences. The debrief can attend to the gap between what participants understood the consequences to be before the simulation and after.

[ICS simlab](https://github.com/tymyrddin/ics-simlab) and [Smart grid simlab](https://github.com/tymyrddin/smart-grid-simlab) are flexible OT/ICS CTF environments. Both are under development and intended for structured attack path exercises and skill-building sessions with technical teams.

## Structuring the debrief

The value of a simulation accumulates in the debrief. A simulation run without a debrief leaves the learning in the room. The questions that matter are not "did we win" but what was the group surprised by, what assumptions turned out to be wrong, what decision would the group make differently, and what does the simulation suggest about the actual system.

The retrospective format from [retrospectives](retrospectives.md) applies directly. The simulation gives the energy timeline its material. The debrief makes that material useful.
