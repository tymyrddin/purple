# Attack path mapping

An attack path is the sequence of steps an adversary takes from their starting position to their objective. Mapping attack paths makes the sequence visible so the group can reason about where to intervene.

The [SEM](../foundations/system-effectiveness/index.rst) framing is important here. An attack path map is a model of the system as the group believes it to be. The paths it shows are the paths through that model. The paths it does not show are the paths through the model's blind spots: the connections nobody knew about, the trust relationships nobody thought to question, the system that was assumed to be isolated and turned out not to be.

This means that a well-run attack path mapping session produces two kinds of output: the paths that are visible, and the questions that reveal where the model needs testing. Both matter.

## The exercise

Choose one adversary persona from the [previous exercise](adversary-persona-workshop.md). Use the one the group found most uncomfortable; it is usually the most informative.

Draw the possible entry points on a whiteboard or with sticky notes. Entry points are anywhere the adversary could plausibly begin: a phishing email, a contractor's account, a partner integration, a public-facing API, a physical location.

Extend paths step by step. From each entry point, ask: what would this adversary try next? What do they gain from this step? Where does that lead? Continue until the path reaches something whose loss, compromise, or disruption would actually hurt: a critical asset, a sensitive data store, an operational system.

Repeat for each entry point. You are looking for overlap: steps that appear in multiple attack paths are chokepoints, and chokepoints are usually the most efficient places to strengthen defences.

## What the map reveals

Beyond the paths themselves, pay attention to:

What the group does not know. When someone says "I am not sure what that system can reach from here," that uncertainty is a finding. The attack path map is only as accurate as the group's knowledge of the actual system, and gaps in that knowledge are gaps in the model.

What surprises people. A connection nobody knew about, a trust relationship that extends further than expected, a system that turns out to have access to something sensitive. These surprises are the exercise working.

What the group is unwilling to map. If a path through a particular system or team gets deflected or minimised repeatedly, that deflection is worth noting. It may reflect legitimate scope constraints or it may reflect political discomfort with naming certain attack surfaces.

## Keeping it useful

Aim for a sketch, not a compliance report. A whiteboard photograph of interconnected sticky notes is the right level of fidelity. A thirty-page diagram is not.

The map is correct at the time it is drawn and begins drifting immediately. Mark it with the date. Build in a trigger for revisiting it: when a new system is added, when a significant integration changes, when an incident reveals a path that was not on the map.

## Related

[Simulations in practice](../workshops/simulations.md) describes how to use simulator environments to test the paths mapped in this exercise, including the Power and Light and ICS simlab environments.
