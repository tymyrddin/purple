# Threat modelling: a practical, human-first process

*“Name the people and paths that cause harm, then cut the paths and blunt the harm.”*

## 0) Scope & context (set the frame)

Define the system, people, data, and decisions in scope. Name the constraints (time, skills, tooling, legal). If you can’t draw it on one page, you don’t understand it yet.

Outputs: 1-page context diagram, in/out of scope list.

## 1) Adversaries (who’s doing what to whom, and why)

Enumerate likely actors and enablers. In interpersonal contexts that includes intimate partners, family, employers/IT, platform intermediaries; in org contexts, competitors, criminal groups, insiders, suppliers. Capture access, knowledge, and motivation explicitly—not “shadowy hacker,” but “ex with shared iCloud, knows routines, wants control.” ([poweron.tymyrddin.dev][1])

Outputs: Adversary cards with access/knowledge/motivation and capability.

## 2) Assets (what’s worth protecting)

Catalogue the things that matter: people, devices, identities, accounts, locations, money, IP, reputation. Prioritise by business/individual impact, not tech shininess. ([poweron.tymyrddin.dev][1], [green.tymyrddin.dev][2])

Outputs: Asset register with criticality tags.

## 3) Access paths & attack vectors (how they get in)

List the ways adversaries reach assets: physical access, shared credentials, cloud sync, social engineering, supply chain and API paths; for web/data cases, include de-anonymisation routes (linkage attacks, metadata leaks, cross-dataset joins). ([poweron.tymyrddin.dev][1], [green.tymyrddin.dev][2])

Outputs: Attack surface map (people, process, tech), vector catalogue.

## 4) Concrete attacks (what this looks like in real life)

Write scenario snippets that are uncomfortably specific: stalkerware install via “helpful” phone check; location leakage via shared photos; impersonation using reused recovery channels; for data, identity re-construction via public datasets + quasi-identifiers. ([poweron.tymyrddin.dev][1], [green.tymyrddin.dev][2])

Outputs: Attack stories with preconditions, signals, and first moves.

## 5) Threats → harms → impacts (chain it)

Name the harm (monitoring, isolation, financial sabotage, reputational damage), then link to organisational impacts (legal/regulatory exposure, safety risk, loss of service integrity). Keep it human: it’s not “loss of confidentiality,” it’s “their location is exposed to an abusive partner.” ([poweron.tymyrddin.dev][1])

Outputs: Threat–harm–impact matrix with severity/likelihood.

## 6) Assistive & enabling technologies (the stuff that tips the balance)

Note tech that helps the defender (logging, SIEM, EDR, privacy features) and tech that helps the adversary (tracking features, cloud histories, data brokers). Garden metaphor optional; the point is to see the whole ecosystem, not just the fence. ([green.tymyrddin.dev][2])

Outputs: Enabler map (defensive and adversarial).

## 7) Mitigations & responses (map impacts to actions)

For each high-risk chain, pair prevention, detection, response, and recovery actions. In personal-safety contexts: device hygiene, account isolation, evidence preservation, legal support, safe comms plans. In org contexts: hardening, monitoring, playbooks, escalation paths, comms protocols. The Power On flow explicitly links impacts to responses—steal that ruthlessly. ([poweron.tymyrddin.dev][1])

Outputs: Control set per threat chain; quick-win list; playbooks.

## 8) Verification (prove it, don’t vibe it)

Test your model: tabletop the attack stories; run controlled exercises; validate logs catch what the model claims; for de-anonymisation risks, attempt safe red-team linkage tests on synthetic data. Adjust the model when reality argues back.
*
*Outputs: Test results, detection coverage notes, fixes queued.

## 9) Documentation & iteration (make it portable)

Record the model in plain language with just enough structure to be useful across teams (security, legal, support). Revisit after incidents or significant changes. This isn’t a museum piece. ([poweron.tymyrddin.dev][1])

Outputs: Living TM doc, change log, review cadence.

## Reuseful emplates & artefacts

* Adversary card (access/knowledge/motivation/capability/notes).
* Asset register (owner, where it lives, who can touch it, consequences).
* Attack surface map (people/process/tech swimlanes).
* Threat–harm–impact matrix (with severity & likelihood).
* Impact→Response mapper (prevention/detection/response/recovery). ([poweron.tymyrddin.dev][1])
* Tabletop script (roles, injects, log evidence to collect).

## Examples

* [Digital threat modelling for partner abuse | Power On](https://poweron.tymyrddin.dev/en/docs/threat-model/) → sections used here: *Who’s causing the harm?*, *What’s worth protecting?*, *How do they get in?*, *What do these look like in real life?*, *What kind of harm can this cause?*, plus *Mapping impacts to responses* (your “Take back power” flow). ([poweron.tymyrddin.dev][1])
* [The garden layout: Threat model - Green team](https://green.tymyrddin.dev/docs/deanonymisation/) → sections used here: *Adversaries, Assets, Attack vectors, Attacks, Assistive technologies, Threats, Impacts*—provides the garden-ecosystem lens and data-reconstruction examples to fold into vectors and harms. ([green.tymyrddin.dev][2])

## How this scales across client sizes

* Small (SIRT-level): lightweight adversary cards, 1-page attack surface, two top threat chains with mapped responses; a single tabletop to verify.
* Mid (proto-SOC): full matrix, monitoring requirements, red/blue exercises tied to attack stories.
* Large (purple-capable): add adversary emulation and continuous detection tuning; treat the threat model as the spine for scenarios and exercises.

