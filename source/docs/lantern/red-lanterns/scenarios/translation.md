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

## Related

### Context

- The Spark (foreign element): The Scarlet Semaphore begins its "experimentation," visible only by [a fleeting internal notice](https://red.tymyrddin.dev/docs/scarlet/op-red-lantern/wall/internal-notice-tss) and red lanterns rearranging routes.
- The Reaction: The Department of Silent Stability detects the anomalies and [issues a cautious briefing](https://blue.tymyrddin.dev/docs/shadows/red-lantern/kickoff/internal-briefing-doss), which is promptly [intercepted by the attackers](https://red.tymyrddin.dev/docs/scarlet/op-red-lantern/wall/internal-briefing-doss).
- The Escalation: The red team uses this intelligence to [refine its "control-plane attack" theories](https://red.tymyrddin.dev/docs/scarlet/op-red-lantern/wall/control-plane), creating a formal catalog.
- The Patrician's Move: Seeing the activity as a useful but disruptive threat, the Patrician intervenes. He [recruits the talent](https://red.tymyrddin.dev/docs/scarlet/op-red-lantern/wall/ponders-visit), converting the threat into a strategic asset.
- The New Equilibrium: The project is rebranded under [Purple Lantern Practice Ltd.](https://purple.tymyrddin.dev/docs/lantern/red-lanterns/spark/patrician-engagement), with the goal of "controlled burns" to strengthen the city's overall defenses, as the blue team continues its intelligence gathering and detection capabilities.

### Scarlet Semaphore's

- [Making of the fat finger hijack simulator scenario](https://red.tymyrddin.dev/docs/scarlet/op-red-lantern/simulator/fat_finger_hijack)
- [Making of the subprefix intercept simulator scenario](https://red.tymyrddin.dev/docs/scarlet/op-red-lantern/simulator/subprefix_intercept)
- [Making of the ROA poisoning simulator scenario](https://red.tymyrddin.dev/docs/scarlet/op-red-lantern/simulator/roa_poisoning)
