# Threat modelling as a workshop process

Threat modelling is a structured process for understanding who would attack you, how they would do it, and what would hurt most. Done as a workshop rather than as a solo analyst exercise, it builds shared understanding across technical and non-technical participants and surfaces assumptions that no single person would have noticed alone.

The full threat modelling process lives in its own section of this documentation. What follows is its place in the family of analytical processes.

## What kind of process it is

Threat modelling works with a system and asks what could go wrong with it. This makes it complementary to scenario planning, which works with the future, and to backward planning, which works with a desired state. Threat modelling is the process for understanding the current system's vulnerability to the adversaries who are actually likely to target it.

The SEM framing is important here. A threat model is a model. It encodes assumptions about who the adversaries are, what they want, and what paths they have available. Those assumptions are accurate at the point of creation and drift thereafter. A threat model that is not periodically revisited becomes a record of historical thinking rather than a current analysis, and the gap between the model and reality is the gap that adversaries will use.

## Where it fits with the other processes

Scenario planning asks what futures are possible. Threat modelling asks who is trying to make one of those futures happen and how. The two processes are naturally sequential: a scenario planning session that surfaces a plausible future involving a certain class of attacker feeds directly into a threat modelling session focused on that attacker's likely approach.

Backward planning uses threat modelling as one of its inputs. Understanding the attack paths available to realistic adversaries shapes what "the desired state of security" actually means and what obstacles stand between the current state and that desired state.

The retrospective processes close the loop: after a purple team exercise or a real incident, the retrospective should examine whether the threat model was accurate and what needs to be updated.

## Running it as a workshop

The threat modelling section of this documentation covers the full process: adversary persona development, attack path mapping, operational impact assessment, scenario construction, and building a coherent model from the components. These are designed as face-to-face exercises, run with the people who know the system and the people who understand the threat landscape together in the same room.

The workshop format matters because threat models built by a single analyst in isolation reflect that analyst's mental model of the system. Threat models built with the people who operate the system, the people who built it, and the people who are responsible for its security surface a much richer and more accurate picture, along with the disagreements and gaps that reveal where the real work is.
