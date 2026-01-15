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

## Narrative

- The Spark (foreign element): The Scarlet Semaphore began its "experimentation," visible only by [a fleeting internal notice](https://red.tymyrddin.dev/docs/scarlet/op-red-lantern/wall/internal-notice-tss) and red lanterns rearranging routes.
- The Reaction: The Department of Silent Stability detected the anomalies and [issued a cautious briefing](https://blue.tymyrddin.dev/docs/shadows/red-lantern/kickoff/internal-briefing-doss), which is promptly [intercepted by the attackers](https://red.tymyrddin.dev/docs/scarlet/op-red-lantern/wall/internal-briefing-doss).
- The Escalation: The Scarlet Semaphore used this intelligence to [refine its "control-plane attack" theories](https://red.tymyrddin.dev/docs/scarlet/op-red-lantern/bench/), creating a formal catalog.
- The Patrician's Move: Seeing the activity as a useful but disruptive threat, the Patrician intervened. He [recruited the talent](https://red.tymyrddin.dev/docs/scarlet/op-red-lantern/wall/ponders-visit), converting the threat into a strategic asset.
- The New Equilibrium: The project was rebranded under [Purple Lantern Practice Ltd.](../spark/patrician-engagement), with the goal of "simulated controlled burns" to strengthen the city's overall defenses, as the [Dept. of Silent Stability](https://blue.tymyrddin.dev/docs/shadows/) continues its intelligence gathering and detection capabilities.

