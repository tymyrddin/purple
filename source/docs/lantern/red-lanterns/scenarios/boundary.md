# The simulation boundary

Lantern scenarios simulate telemetry, not infrastructure.

We are not running actual BGP daemons announcing actual prefixes. We are generating JSON events that look like what 
BGP monitoring would produce if those announcements were happening.

This means:

- No actual traffic gets intercepted (good, this is testing)
- No actual services fail (good, this is safe)
- No actual RPKI gets modified (good, no legal concerns)
- Telemetry must be realistic enough to trigger authentic analysis (required, otherwise worthless)

The boundary is "what would logs/metrics/alerts show if this attack really happened?"

From the [control-plane playbook Phase 3](../playbooks/3.md), Action 3.1 describes announcing 203.0.113.128/25 via 
BGP, intercepting traffic, and forwarding it to maintain service.

The scenario doesn't do any of this.

The scenario could emit something like:

```json
{
  "event_type": "bgp.update",
  "timestamp": 600,
  "source": {"feed": "bgp-monitor", "observer": "rrc00"},
  "attributes": {
    "prefix": "203.0.113.128/25",
    "origin_as": 64513,
    "as_path": [3333, 64513],
    "next_hop": "192.0.2.1"
  }
}
```

And perhaps separately:

```json
{
  "event_type": "rpki.validation",
  "timestamp": 600,
  "attributes": {
    "prefix": "203.0.113.128/25",
    "origin_as": 64513,
    "validation_state": "VALID"
  }
}
```

### Context

- The Spark (foreign element): The Scarlet Semaphore begins its "experimentation," visible only by [a fleeting internal notice](https://red.tymyrddin.dev/docs/scarlet/op-red-lantern/wall/internal-notice-tss) and red lanterns rearranging routes.
- The Reaction: The Department of Silent Stability detects the anomalies and [issues a cautious briefing](https://blue.tymyrddin.dev/docs/shadows/red-lantern/kickoff/internal-briefing-doss), which is promptly [intercepted by the attackers](https://red.tymyrddin.dev/docs/scarlet/op-red-lantern/wall/internal-briefing-doss).
- The Escalation: The red team uses this intelligence to [refine its "control-plane attack" theories](https://red.tymyrddin.dev/docs/scarlet/op-red-lantern/wall/control-plane), creating a formal catalog.
- The Patrician's Move: Seeing the activity as a useful but disruptive threat, the Patrician intervenes. He [recruits the talent](https://red.tymyrddin.dev/docs/scarlet/op-red-lantern/wall/ponders-visit), converting the threat into a strategic asset.
- The New Equilibrium: The project is rebranded under [Purple Lantern Practice Ltd.](https://purple.tymyrddin.dev/docs/lantern/red-lanterns/spark/patrician-engagement), with the goal of "controlled burns" to strengthen the city's overall defenses, as the blue team continues its intelligence gathering and detection capabilities.

### Scarlet semaphore's

- [Making of the fat finger hijack simulator scenario](https://red.tymyrddin.dev/docs/scarlet/op-red-lantern/simulator/fat_finger_hijack)
- [Making of the subprefix intercept simulator scenario](https://red.tymyrddin.dev/docs/scarlet/op-red-lantern/simulator/subprefix_intercept)
- [Making of the ROA poisoning simulator scenario](https://red.tymyrddin.dev/docs/scarlet/op-red-lantern/simulator/roa_poisoning)
