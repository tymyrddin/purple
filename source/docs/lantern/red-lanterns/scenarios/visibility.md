# The visibility problem

Playbooks assume attacker visibility into their own actions. Scenarios must not.

From the playbook, Phase 2 Action 2.1 (fraudulent ROA creation) is the control-plane attack. It's the moment 
where the Registry gets poisoned. It's the critical action that enables everything else.

But will defenders see it?

Most organisations don't have:

- Real-time RPKI audit log monitoring
- Alerting on ROA creation for prefixes they don't control
- Correlation between ROA changes and BGP announcements
 
RPKI CA audit logs exist but weren't monitored. ROA changes were logged but not alerted on. Validation state changed 
propagate slowly (30-90 minutes).

A scenario that makes this obviously detectable is lying about defender capabilities.

A better scenario emits:

- ROA creation log (JSON event, timestamped, but not obviously malicious)
- Validator state change 30 minutes later (prefix transitions to "not found" for victim, "valid" for attacker)
- BGP announcement that correlates with ROA change (but only if defenders think to correlate)

Defenders must connect these dots themselves. The scenario doesn't do it for them.

## Narrative

- The Spark (foreign element): The Scarlet Semaphore began its "experimentation," visible only by [a fleeting internal notice](https://red.tymyrddin.dev/docs/scarlet/op-red-lantern/wall/internal-notice-tss) and red lanterns rearranging routes.
- The Reaction: The Department of Silent Stability detected the anomalies and [issued a cautious briefing](https://blue.tymyrddin.dev/docs/shadows/red-lantern/kickoff/internal-briefing-doss), which is promptly [intercepted by the attackers](https://red.tymyrddin.dev/docs/scarlet/op-red-lantern/wall/internal-briefing-doss).
- The Escalation: The Scarlet Semaphore used this intelligence to [refine its "control-plane attack" theories](https://red.tymyrddin.dev/docs/scarlet/op-red-lantern/bench/), creating a formal catalog.
- The Patrician's Move: Seeing the activity as a useful but disruptive threat, the Patrician intervened. He [recruited the talent](https://red.tymyrddin.dev/docs/scarlet/op-red-lantern/wall/ponders-visit), converting the threat into a strategic asset.
- The New Equilibrium: The project was rebranded under [Purple Lantern Practice Ltd.](../spark/patrician-engagement), with the goal of "simulated controlled burns" to strengthen the city's overall defenses, as the [Dept. of Silent Stability](https://blue.tymyrddin.dev/docs/shadows/) continues its intelligence gathering and detection capabilities.

