# The time compression problem

Real attacks take weeks. Tabletop exercises take hours. Lantern scenarios compromise between realism and practicality.

The three-phase playbook spans 3-4 weeks. A Lantern scenario condenses this to perhaps 60 minutes of simulated time, 
with critical decision points spaced 5-15 minutes apart.

This is not lying. This is focusing on the moments that matter.

[Phase 1](../playbooks/1.md) (week 1-2 in playbook) might become:

- `t=0`: Initial RPKI query (barely notable)
- `t=60`: Legitimate ROA creation (routine)

[Phase 2](../playbooks/2.md) (week 3 in playbook) becomes:

- `t=300`: Fraudulent ROA appears (THIS IS THE DETECTION OPPORTUNITY)
- `t=420`: Validation deployment mapping (visible as test announcements)

[Phase 3](../playbooks/3.md) (week 4 in playbook) becomes:

- `t=600`: Hijack announcement (loud, but validates as VALID)
- `t=660`: Traffic interception confirmed (services degrading)
- `t=720`: Route flapping noise (alert fatigue exploitation)
- `t=900`: Either incident contained or persistent compromise

The scenario preserves the decision structure (when could defenders have noticed?) whilst compressing calendar time.

## Narrative

- The Spark (foreign element): The Scarlet Semaphore began its "experimentation," visible only by [a fleeting internal notice](https://red.tymyrddin.dev/docs/scarlet/op-red-lantern/wall/internal-notice-tss) and red lanterns rearranging routes.
- The Reaction: The Department of Silent Stability detected the anomalies and [issued a cautious briefing](https://blue.tymyrddin.dev/docs/shadows/red-lantern/kickoff/internal-briefing-doss), which is promptly [intercepted by the attackers](https://red.tymyrddin.dev/docs/scarlet/op-red-lantern/wall/internal-briefing-doss).
- The Escalation: The Scarlet Semaphore used this intelligence to [refine its "control-plane attack" theories](https://red.tymyrddin.dev/docs/scarlet/op-red-lantern/bench/), creating a formal catalog.
- The Patrician's Move: Seeing the activity as a useful but disruptive threat, the Patrician intervened. He [recruited the talent](https://red.tymyrddin.dev/docs/scarlet/op-red-lantern/wall/ponders-visit), converting the threat into a strategic asset.
- The New Equilibrium: The project was rebranded under [Purple Lantern Practice Ltd.](../spark/patrician-engagement), with the goal of "simulated controlled burns" to strengthen the city's overall defenses, as the [Dept. of Silent Stability](https://blue.tymyrddin.dev/docs/shadows/) continues its intelligence gathering and detection capabilities.

