# Writing telemetry.py

Telemetry is written from the defender's chair, not the attacker's ego.

Reference the existing [ROA poisoning telemetry](https://raw.githubusercontent.com/ninabarzh/red-lantern-sim/refs/heads/main/simulator/scenarios/advanced/roa_poisoning/telemetry.py) for structure. 

Control-plane playbook scenarios needs similar treatment.

## The defender's perspective problem

Attackers know what they're doing. Defenders don't.

When [Scarlet Semaphore](https://red.tymyrddin.dev/docs/scarlet/op-red-lantern/roa_poisoning#roa-manipulation-techniques) creates a fraudulent ROA (Phase 2, Action 2.1), they know:
- This is deliberate
- This enables the hijack in phase 3
- Timing is coordinated
- Cover story is prepared

Defenders see:
- ROA creation log entry
- Timestamp
- Account username
- IP address (possibly anonymised via TOR/VPN)
- Prefix and AS number

That's it. No context. No explanation. No "THIS IS AN ATTACK" label.

Telemetry must generate what defenders would actually observe, not what would be convenient for detection.

## Event structure for control-plane attacks

From the playbook Phase 2 Action 2.1 (fraudulent ROA creation):

```python
def generate_roa_creation_event(clock, scenario_name):
    """
    Generate RPKI ROA creation event.
    
    This is what RIR audit logs would show.
    It looks routine unless you know to check whether
    this account should be creating ROAs for this prefix.
    """
    return {
        "event_type": "rpki.roa_change",
        "timestamp": clock.now(),
        "source": {
            "feed": "rpki-ca",
            "observer": "ripe_ncc",  # or ARIN, APNIC, depending on prefix allocation
        },
        "attributes": {
            "change_type": "created",
            "prefix": "203.0.113.0/24",
            "origin_as": 64513,  # Attacker's AS, NOT victim's
            "max_length": 25,
            "actor": "admin_backup",  # Compromised account
            "actor_ip": "185.220.101.45",  # TOR exit node, suspicious but not proof
            "actor_location": "RU",  # Misleading geolocation
            "previous_roa": None,  # No ROA existed before (or victim's was deleted)
        },
        "scenario": {
            "name": scenario_name,
            "attack_step": "roa_creation",  # Only for training mode
        }
    }
```

## Signals defenders plausibly receive

For Phase 1 (reconnaissance), defenders receive almost nothing:

- Maybe HTTPS queries to public RPKI validators (stat.ripe.net, cloudflare RPKI API)
- These queries are completely normal, thousands happen daily
- No alerts, no logs worth noticing

For Phase 2 (ROA poisoning), defenders might receive:

- ROA creation audit log (IF they're collecting RIR logs, most aren't)
- Validator state change notification (30-90 minutes later, IF monitoring validators)
- No BGP events yet (announcement hasn't happened)

For Phase 3 (hijack), defenders should receive:

- BGP UPDATE announcement
- RPKI validation result (returns VALID, confusingly)
- Traffic flow changes (IF NetFlow monitored)
- Service degradation alerts
- Route flapping noise (attacker-generated)

## Ambiguity and overlap

From [The Poisoned Registry](https://red.tymyrddin.dev/docs/scarlet/op-red-lantern/roa_poisoning#incident-response-misdirection), attackers deliberately create ambiguity:

### Misdirection 1: Blame automation

Telemetry should allow this interpretation:

```python
{
    "event_type": "rpki.roa_change",
    "attributes": {
        "actor": "automation-bot",  # Not obviously human
        "change_reason": "scheduled_maintenance",  # Plausible
        ...
    }
}
```

Defenders seeing this might conclude "automation error" rather than "deliberate attack".

### Misdirection 2: Timing during maintenance

If ROA creation happens during declared maintenance window:

```python
{
    {
        "event_type": "maintenance.scheduled",
        "timestamp": clock.now() - 3600,  # One hour before ROA change
        "attributes": {
            "maintenance_type": "rpki_roa_updates",
            "scheduled_by": "noc_team",
        }
    }
    
    # Then later...
    {
        "event_type": "rpki.roa_change",
        "timestamp": clock.now(),
        "attributes": {
            "change_type": "created",
            ...
        }
    }
}
```

Correlation makes attack look like legitimate maintenance gone wrong.

### Misdirection 3: Multiple concurrent issues

Generate overlapping events:

```python
# At t=600, both happen:
- BGP hijack announcement
- Unrelated router high CPU alert
- Disk space warning on logging server
- BGP session flap on different peer
```

Which one is the attack? All of them look important.

## Realistic misinterpretation allowance

Telemetry should permit defenders to reach wrong conclusions that are reasonable given the data.

### Reasonable wrong conclusion 1: Configuration error

ROA created for wrong prefix by mistake:

```python
{
    "event_type": "rpki.roa_change",
    "attributes": {
        "change_type": "created",
        "prefix": "203.0.113.0/24",  # Victim's prefix
        "origin_as": 64513,  # Attacker's AS
        "comment": "Bulk update from spreadsheet row 47",  # Suggests copy-paste error
    }
}
```

Defender interpretation: "Someone [fat-fingered](https://red.tymyrddin.dev/docs/scarlet/op-red-lantern/fat_finger_hijack) the spreadsheet during bulk ROA update."

This is plausible. These errors happen. It's wrong, but reasonably wrong.

### Reasonable wrong conclusion 2: Vendor/automation issue

```python
{
    "event_type": "rpki.roa_change",
    "attributes": {
        "actor": "rpki-automation-v2.1",
        "change_type": "created",
        "triggered_by": "api_call",
        "api_client": "netops-tooling",
    }
}
```

Defender interpretation: "Automation created ROA, probably from configuration management system. Bug in our tooling?"

Also plausible. Automation does unexpected things.

### Reasonable wrong conclusion 3: Insider error

```python
{
    "event_type": "rpki.roa_change",
    "attributes": {
        "actor": "admin_backup",  # Legitimate account name
        "actor_ip": "192.0.2.100",  # Internal IP (if attacker pivoted through internal system)
        "timestamp_utc": "2024-12-20T15:30:00Z",  # Business hours
    }
}
```

Defender interpretation: "Bob from NOC team made ROA change during normal work hours from office network. Probably 
legitimate, maybe check with Bob?"

Plausible until they actually check with Bob and he says "wasn't me."

## Early telemetry should be boring

Phase 1 generates almost nothing interesting:

```python
def generate_phase1_reconnaissance(clock, bus):
    """
    Phase 1 is nearly invisible.
    Generate events that look like routine RPKI queries.
    """
    # Query to public validator
    bus.publish({
        "event_type": "https.request",
        "timestamp": clock.now(),
        "source": {"feed": "webserver-logs", "observer": "stat.ripe.net"},
        "attributes": {
            "method": "GET",
            "uri": "/data/rpki-validation/data.json?resource=203.0.113.0/24",
            "client_ip": "185.220.101.1",  # TOR exit
            "user_agent": "curl/7.68.0",
        }
    })
```

This is so boring it wouldn't trigger alerts at RIPE. Thousands of similar queries happen daily.

If Phase 1 looks suspicious, you've made it unrealistic.

## Late telemetry should be confusing

Phase 3 generates many simultaneous events:

```python
def generate_phase3_hijack(clock, bus):
    """
    Phase 3 generates multiple overlapping signals.
    Some are attack, some are noise, some are cascading effects.
    """
    # The actual hijack
    bus.publish({
        "event_type": "bgp.update",
        "timestamp": clock.now(),
        "attributes": {
            "prefix": "203.0.113.128/25",
            "origin_as": 64513,
            "as_path": [3333, 64513],
        }
    })
    
    # RPKI validation (confusingly returns VALID)
    bus.publish({
        "event_type": "rpki.validation",
        "timestamp": clock.now() + 2,
        "attributes": {
            "prefix": "203.0.113.128/25",
            "origin_as": 64513,
            "validation_state": "VALID",  # Because fraudulent ROA exists
            "roa_found": True,
        }
    })
    
    # Service degradation (5 minutes later, cascading effect)
    bus.publish({
        "event_type": "service.degraded",
        "timestamp": clock.now() + 300,
        "attributes": {
            "service": "web_frontend",
            "latency_p99": 5000,  # 5 second latency, was 100ms
            "error_rate": 0.15,  # 15% errors
        }
    })
    
    # Route flapping noise (attacker-generated)
    for i in range(20):
        bus.publish({
            "event_type": "bgp.flap",
            "timestamp": clock.now() + 60 + (i * 30),
            "attributes": {
                "prefix": f"10.{i}.0.0/16",  # Unrelated prefixes
                "flap_count": 10 + i,
            }
        })
    
    # Monitoring alerts (from multiple systems)
    alerts = [
        "BGP peer session reset",
        "High CPU on router-r1",
        "Disk space low on log-server",
        "NetFlow export delayed",
    ]
    for alert in alerts:
        bus.publish({
            "event_type": "alert.triggered",
            "timestamp": clock.now() + 120,
            "attributes": {"message": alert, "severity": "warning"},
        })
```

Defenders seeing this stream must:

- Identify which event is the attack
- Distinguish attack from noise
- Correlate across events (hijack + validation + service degradation)
- Ignore red herrings (unrelated alerts)

If correlation is obvious, telemetry is too clean.

## Allowing reasonable misinterpretation

Perfect clarity is a bug. Defenders should have multiple plausible interpretations.

For the fraudulent ROA at t=300:

- Interpretation A: Legitimate maintenance. "ROA created during maintenance window by automation. Probably routine."
- Interpretation B: Configuration error. "Wrong prefix in spreadsheet during bulk update. Human error."
- Interpretation C: Automation bug. "RPKI tooling created unexpected ROA. Software bug."
- Interpretation D: Compromised credentials. "Account used, but actor IP is TOR exit node. Possible compromise?"
- Interpretation E: Insider threat. "Legitimate account from internal IP. Possible malicious insider?"

All five are reasonable given limited data. Only D and E are correct, but A/B/C are plausible enough that defenders 
might investigate them first.

Telemetry should support all interpretations. Defenders must gather additional evidence to rule out wrong ones.

## What NOT to include in telemetry

No attack labels. Real logs don't label themselves; no intent attribution. Defenders infer intent from behaviour, 
not from metadata; no perfect correlation keys. Real events don't link themselves conveniently; No defender 
instructions. Allow defenders to figure out what best to investigate next.

## Early boring late confusing as design pattern

Structure telemetry generation:

```python
def register(event_bus, clock, scenario_name):
    # Phase 1: Mostly silent (t=0 to t=300)
    @event_bus.on(lambda e: e['entry']['action'] == 'reconnaissance')
    def phase1_quiet(event):
        # Generate minimal, boring telemetry
        pass
    
    # Phase 2: Subtle but detectable (t=300 to t=600)
    @event_bus.on(lambda e: e['entry']['action'] == 'fraudulent_roa')
    def phase2_subtle(event):
        # Generate ROA change log
        # Defenders COULD catch this IF they're monitoring audit logs
        pass
    
    # Phase 3: Loud but confusing (t=600 to t=900)
    @event_bus.on(lambda e: e['entry']['action'] == 'hijack')
    def phase3_chaos(event):
        # Generate hijack + noise + cascading failures
        # Many simultaneous events, correlation required
        pass
```

This models how [The Poisoned Registry](https://red.tymyrddin.dev/docs/scarlet/op-red-lantern/roa_poisoning) operation 
actually progresses: invisible preparation, subtle compromise, chaotic exploitation.

## Testing your telemetry

Before running scenario, ask:

- Does telemetry come from realistic sources? "rpki-ca", "bgp-monitor", "netflow-collector" are plausible. "attack-detector-9000" is not.
- Could events be legitimately misinterpreted? If ROA creation can only mean "attack", telemetry is too clean.
- Is timing realistic? RPKI shouldn't propagate instantly. Cascading failures shouldn't happen simultaneously.
- Are there red herrings? If every event is attack-related, defenders aren't being tested.
- Would real defenders see this? If scenario assumes perfect logging/monitoring, it's aspirational not realistic.

The goal is telemetry that defenders must interpret, not telemetry that interprets itself. And for now, the simulator is still under construction.

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

### Repository

- [Scenarios](https://github.com/ninabarzh/red-lantern-sim/blob/main/simulator/scenarios/README.md)
- [Fat finger hijack telemetry.py](https://github.com/ninabarzh/red-lantern-sim/blob/main/simulator/scenarios/easy/fat_finger_hijack/telemetry.py)
- [Subprefix interception telemetry.py](https://github.com/ninabarzh/red-lantern-sim/blob/main/simulator/scenarios/medium/subprefix_intercept/telemetry.py)
- [ROA poisoning/Control plane manipulation telemetry.py](https://github.com/ninabarzh/red-lantern-sim/blob/main/simulator/scenarios/advanced/roa_poisoning/telemetry.py)

