# Who would come for this

Threat modelling asks who would attack a system, how they would go about it, and what would hurt most if they
did. Run as a workshop rather than a solo analyst's write-up, it does what the solo version cannot: it builds
a shared picture across the people who operate the system, the people who built it, and the people
responsible for defending it, and it surfaces the disagreements and blank spots that mark where the real work
is. The full process lives in [threat modelling choreography](../threat-modelling/choreography.md); the
question here is where it sits among the analytical processes.

A threat model is a model, accurate at the moment it is drawn and drifting from then on. It encodes
assumptions about who the adversaries are, what they want, and which paths are open to them, and a model left
unrevisited slowly becomes a record of last year's thinking. The distance between the model and the current
reality is the distance an adversary is free to use, so the value is less in the artefact than in the habit of
returning to it.

It sits naturally between the others. Scenario planning asks which futures are possible; threat modelling asks
who is trying to bring one about, and how. A scenario that surfaces a particular class of attacker feeds
straight into a threat model of that attacker's likely approach. Backward planning takes the available attack
paths as an input, since they shape what a desired security posture even means. And a retrospective closes the
loop: after an exercise or a real incident, it asks whether the model held and what needs redrawing.


*Last updated: 8 July 2026*
