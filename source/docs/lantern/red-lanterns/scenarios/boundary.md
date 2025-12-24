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
