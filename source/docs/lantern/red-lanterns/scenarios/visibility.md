# The visibility problem

Playbooks assume attacker visibility into their own actions. Scenarios must not.

From the playbook, Phase 2 Action 2.1 (fraudulent ROA creation) is the control-plane attack. It's the moment 
where the Registry gets poisoned. It's the critical action that enables everything else.

But will defenders see it?

Most organisations don't have:

- Real-time RPKI audit log monitoring
- Alerting on ROA creation for prefixes they don't control
- Correlation between ROA changes and BGP announcements

The [Scarlet Semaphore operation notes on ROA poisoning](https://red.tymyrddin.dev/docs/scarlet/op-red-lantern/roa_poisoning):  
RPKI CA audit logs exist but aren't monitored. ROA changes are logged but not alerted on. Validation state changes 
propagate slowly (30-90 minutes).

A scenario that makes this obviously detectable is lying about defender capabilities.

A better scenario emits:

- ROA creation log (JSON event, timestamped, but not obviously malicious)
- Validator state change 30 minutes later (prefix transitions to "not found" for victim, "valid" for attacker)
- BGP announcement that correlates with ROA change (but only if defenders think to correlate)

Defenders must connect these dots themselves. The scenario doesn't do it for them.

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
