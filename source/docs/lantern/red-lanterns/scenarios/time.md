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
