# Introduction to threat modelling exercises

Threat modelling is the practice of thinking systematically about who might attack you, how they might do it, and what the consequences would be. The goal is not a document. It is a shared mental model, built by the people who know the system and tested against the people who understand how it could be broken.

The word "model" is doing real work here. A threat model is a representation of the system, the adversary, and the conditions under which an attack becomes possible. Like all models, it encodes assumptions. Like all models, it drifts as the environment changes. A threat model built eighteen months ago and not revisited is a record of how things were, not how they are. The gap between the two is where the most interesting risks live.

## Who needs to be in the room

The exercises in this section are designed as workshop activities, not solo analyst tasks. This is deliberate.

A threat model produced by a single security analyst reflects that analyst's model of the system, the adversary, and the organisation. It will be technically competent and organisationally partial. It will encode the analyst's assumptions about what the developers did, what the operations team knows, and what leadership is willing to act on.

A threat model produced collaboratively, with the people who built the system, the people who operate it, and the people who are responsible for what happens when it fails, surfaces a much richer picture. It also surfaces the disagreements, the gaps in shared understanding, and the places where different parts of the organisation are operating on incompatible assumptions. Those are findings too.

PSL is directly relevant here: all three layers need to be present. The rational layer (what the system does, what the vulnerabilities are) is the easy part. The emotional layer (what people are afraid to name, what concerns feel too uncomfortable to raise with colleagues in the room) and the political layer (whose risk appetite shapes what gets prioritised, who has authority to act on a finding) determine whether the exercise produces change or produces a document.

## How to use this set

Work through the exercises in order: adversary personas, attack path mapping, operational impact, scenario crafting, bringing it together, building the model. Each exercise produces something the next one builds on.

Focus on practical outputs rather than theoretical completeness. A simple threat model that is understood and used is worth far more than a comprehensive one that sits in a folder.

Collaborate openly. The moment when someone says "I had no idea that system was connected to that one" is the exercise working. The moment when someone says "we all know about that risk but we cannot get anyone to act on it" is also the exercise working, and is a different kind of finding.

Keep each exercise to one sheet, one card, or one diagram per output. Complexity is the enemy of use.

## What you are building

By the end of this sequence you will have clear adversary personas, mapped attack paths, operational impact assessments, realistic scenarios, and a lightweight threat model that reflects what the group actually believes and knows.

You will also have surfaced the assumptions that nobody had examined, the risks that were known but unnamed, and the places where the model of the system and the actual system diverge. These are often the most valuable outputs.

## Examples

- [Digital threat modelling for partner abuse: Power On](https://poweron.tymyrddin.dev/en/docs/threat-model/) applies this sequence in a context where the adversary is a known individual and the assets are personal safety and privacy.
- [The garden layout: Threat model, Green team](https://green.tymyrddin.dev/docs/deanonymisation/) applies it to deanonymisation risks, with adversaries, assets, attack vectors, and impacts.
