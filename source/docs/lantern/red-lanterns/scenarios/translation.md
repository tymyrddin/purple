# The translation challenge

The control-plane attack playbooks describe three phases over 3-4 weeks:

Phase 1: [Registry reconnaissance and initial ROA creation](../playbooks/1.md)

- Attacker knows: "I'm mapping RPKI deployment and establishing legitimate presence"
- Defender sees: Nothing. Maybe routine RPKI queries in public API logs (if anyone's looking)

Phase 2: [ROA scope expansion and validation environment mapping](../playbooks/2.md)

- Attacker knows: "I'm poisoning the validation infrastructure with fraudulent ROA"
- Defender sees: ROA creation log entry. Might look like operator error. Might not be noticed at all.

Phase 3: [Prefix hijacking with RPKI validation cover](../playbooks/3.md)

- Attacker knows: "I'm exploiting the poisoned control plane to hijack traffic"
- Defender sees: BGP announcement that validates as VALID. Traffic routing changing. Services degrading. Possibly thousands of unrelated alerts because attacker triggered noise generation.

The scenario must model what defenders see, when they see it, and with what ambiguity.

## Narrative

- The Spark (foreign element): The Scarlet Semaphore began its "experimentation," visible only by [a fleeting internal notice](https://red.tymyrddin.dev/docs/scarlet/op-red-lantern/wall/internal-notice-tss) and red lanterns rearranging routes.
- The Reaction: The Department of Silent Stability detected the anomalies and [issued a cautious briefing](https://blue.tymyrddin.dev/docs/shadows/red-lantern/kickoff/internal-briefing-doss), which is promptly [intercepted by the attackers](https://red.tymyrddin.dev/docs/scarlet/op-red-lantern/wall/internal-briefing-doss).
- The Escalation: The Scarlet Semaphore used this intelligence to [refine its "control-plane attack" theories](https://red.tymyrddin.dev/docs/scarlet/op-red-lantern/bench/), creating a formal catalog.
- The Patrician's Move: Seeing the activity as a useful but disruptive threat, the Patrician intervened. He [recruited the talent](https://red.tymyrddin.dev/docs/scarlet/op-red-lantern/wall/ponders-visit), converting the threat into a strategic asset.
- The New Equilibrium: The project was rebranded under [Purple Lantern Practice Ltd.](../spark/patrician-engagement), with the goal of "simulated controlled burns" to strengthen the city's overall defenses, as the [Dept. of Silent Stability](https://blue.tymyrddin.dev/docs/shadows/) continues its intelligence gathering and detection capabilities.

