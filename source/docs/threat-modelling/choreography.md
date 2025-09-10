# Threat modelling: a practical, human-first process

*“Name the people and paths that cause harm, then cut the paths and blunt the harm.”*

This choreography surfaces real-world threats to people, processes, and assets by mapping actors, motivations, 
attack paths, and impacts—always **faces-to-faces**, collaboratively, and with a human-first lens. It goes 
beyond standard technical checklists by highlighting human dynamics, context, and the ecosystem of enabling 
technologies. Each step produces actionable insight on its own, yet together these dances build a resilient, 
adaptive threat-aware culture.

## The flow

1. **Scope & context** — define the system, people, data, decisions, and constraints. Keep it concise enough to fit on one page.
2. **Adversaries** — enumerate likely actors and enablers, capturing access, knowledge, and motivation.
3. **Assets** — catalogue what matters most and prioritise by impact.
4. **Access paths & attack vectors** — map how adversaries can reach assets.
5. **Concrete attacks** — create scenario snippets that are uncomfortably specific.
6. **Threats → harms → impacts** — link potential harm to organisational consequences.
7. **Assistive & enabling technologies** — see the full ecosystem of defensive and adversarial tools.
8. **Mitigations & responses** — map impacts to actionable prevention, detection, response, and recovery measures.
9. **Verification** — tabletop exercises, controlled tests, and safe red-team probes validate the model.
10. **Documentation & iteration** — keep the model live, portable, and revisited as conditions change.

## Reuseful emplates & artefacts

* Adversary card (access/knowledge/motivation/capability/notes).
* Asset register (owner, where it lives, who can touch it, consequences).
* Attack surface map (people/process/tech swimlanes).
* Threat–harm–impact matrix (with severity & likelihood).
* Impact→Response mapper (prevention/detection/response/recovery).
* Tabletop script (roles, injects, log evidence to collect).

## Examples

* [Digital threat modelling for partner abuse | Power On](https://poweron.tymyrddin.dev/en/docs/threat-model/) → sections used: *Who’s causing the harm?*, *What’s worth protecting?*, *How do they get in?*, *What do these look like in real life?*, *What kind of harm can this cause?*, plus *Mapping impacts to responses*.
* [The garden layout: Threat model - Green team](https://green.tymyrddin.dev/docs/deanonymisation/) → sections used: *Adversaries, Assets, Attack vectors, Attacks, Assistive technologies, Threats, Impacts*—provides the garden-ecosystem lens and data-reconstruction examples to fold into vectors and harms.

## Scaling across client sizes

* **Small (SIRT-level):** lightweight adversary cards, 1-page attack surface, two top threat chains with mapped responses; a single tabletop to verify.
* **Mid (proto-SOC):** full matrix, monitoring requirements, red/blue exercises tied to attack stories.
* **Large (purple-capable):** add adversary emulation and continuous detection tuning; treat the threat model as the spine for scenarios and exercises.
