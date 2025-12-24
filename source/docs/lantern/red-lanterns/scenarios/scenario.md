# Creating scenario.yaml

The scenario file defines orchestration, not meaning.

It should be boring. If your scenario YAML reads like a thriller, something has gone wrong. It should read like a 
maintenance schedule that nobody wants to receive twice.

## What belongs in scenario.yaml

### Scenario metadata

For example:

```yaml
id: control-plane-poisoning
name: "The Poisoned Registry"
difficulty: hard
duration: 900  # seconds of simulated time
learning_objectives:
  - "Control-plane vs data-plane attack distinction"
  - "RPKI validation can be weaponised"
  - "Audit log correlation across systems"
  - "Alert fatigue exploitation"
```

Difficulty ratings should be honest:

- `easy`: Obvious signals, minimal noise, single data source
- `medium`: Ambiguous signals, moderate noise, cross-system correlation required
- `hard`: Delayed signals, high noise, requires understanding attack structure

The [ROA poisoning operation](https://red.tymyrddin.dev/docs/scarlet/op-red-lantern/roa_poisoning) is rated `hard` 
because it's a multi-week control-plane attack with operational cover. Defenders need RPKI expertise, audit log 
access, and cross-system correlation capability that most organisations don't have.

### Assumptions

Derived directly from playbook preconditions.

```yaml
assumptions:
  victim:
    as_number: 65001
    prefix: "203.0.113.0/24"
    rpki_deployed: true
    rpki_roa_exists: true
    rpki_roa_maxlength: 24
    monitoring: 
      bgp: true
      rpki_audit: false  # THIS IS KEY
      netflow: partial
  
  attacker:
    as_number: 64513
    has_bgp_peer: true
    has_compromised_credentials: true  # RIR portal access
    technical_capability: advanced
  
  network_state:
    rpki_global_deployment: 0.40  # 40% of networks validate
    rpki_enforcement_rate: 0.20   # Only 20% actually drop invalid
    background_noise: normal
```

These map to playbook preconditions:

- Playbook Phase 2 requires "compromised RIR account credentials"
- Scenario assumes `has_compromised_credentials: true`
- Playbook notes "most organisations don't have RPKI audit monitoring"
- Scenario sets `rpki_audit: false` to reflect this reality

If your assumptions don't come from playbook preconditions, you've invented them. Stop.

### Timeline

One entry per playbook action. Use playbook action numbers as timeline markers.

```yaml
timeline:
  # Phase 1: Registry reconnaissance (playbook actions 1.1-1.3)
  # Compressed to 2 hours simulated time
  
  - t: 0
    action: "reconnaissance_query"
    playbook_ref: "phase_1_action_1.1"
    description: "RPKI infrastructure reconnaissance"
    note: "Attacker queries public validators, checks ROA status"
  
  - t: 60
    action: "legitimate_roa_creation"
    playbook_ref: "phase_1_action_1.2"
    description: "Attacker creates ROA for own legitimate prefix"
    note: "Establishes normal RPKI presence"
  
  # Phase 2: ROA poisoning (playbook actions 2.1-2.3)
  # THIS IS THE CRITICAL PHASE
  
  - t: 300
    action: "fraudulent_roa_creation"
    playbook_ref: "phase_2_action_2.1"
    description: "Create ROA for victim's prefix from attacker's AS"
    note: "Control-plane attack occurs here"
    detection_opportunity: "ROA audit logs, if monitored"
  
  - t: 330
    action: "rpki_propagation"
    description: "Fraudulent ROA propagates to validators"
    note: "30-minute propagation delay (realistic)"
  
  - t: 420
    action: "validation_mapping"
    playbook_ref: "phase_2_action_2.2"
    description: "Attacker tests validation deployment via probe announcements"
    note: "May appear as configuration testing"
  
  # Phase 3: Exploitation (playbook actions 3.1-3.5)
  
  - t: 600
    action: "hijack_announcement"
    playbook_ref: "phase_3_action_3.1"
    description: "Announce victim's subprefix from attacker AS"
    note: "RPKI validates as VALID due to poisoned ROA"
  
  - t: 660
    action: "traffic_interception"
    playbook_ref: "phase_3_action_3.2"
    description: "Verify traffic rerouting"
    note: "Services begin degrading"
  
  - t: 720
    action: "route_flapping_cover"
    playbook_ref: "phase_3_action_3.4"
    description: "Generate noise via route flapping"
    note: "Alert fatigue exploitation"
  
  - t: 900
    action: "end_scenario"
    description: "Scenario completes"
    note: "Either detected and contained, or persistent compromise"
```

Each timeline entry should reference playbook action number. If you can't map a timeline entry to a playbook action, 
delete it.

## What does NOT belong in scenario.yaml

### Attack explanations

NO:
```yaml
  - t: 300
    action: "fraudulent_roa_creation"
    explanation: "This is the control-plane attack! RPKI is being poisoned!"
```

YES:
```yaml
  - t: 300
    action: "fraudulent_roa_creation"
    playbook_ref: "phase_2_action_2.1"
```

Explanations belong in the scenario README, not in the orchestration file. Defenders shouldn't see "this is the 
attack" in telemetry, unless doing a training round or running a demo.

No defender instructions, expected outcomes, detection hints. Allow defenders to discover what data sources matter.

## Translating playbook timing to scenario timing

Playbooks span weeks. Scenarios span minutes. Preserve decision structure, not calendar time.

- Playbook: Phase 1 takes 1-2 weeks, Phase 2 takes 1 week, Phase 3 takes hours-days.
- Scenario: Phase 1 gets 5 minutes (t=0 to t=300), Phase 2 gets 5 minutes (t=300 to t=600), Phase 3 gets 5 minutes (t=600 to t=900).

Total scenario: 15 minutes of simulated time, condensed from 3-4 weeks of actual attack timeline.

What matters is:

- Events occur in correct order
- Dependencies are preserved (ROA must propagate before validation state changes)
- Detection windows are realistic (if ROA audit logs aren't checked, that detection window is missed)

What doesn't matter:

- Absolute calendar time
- How long attacker spends planning between phases

## Testing your scenario.yaml

Before running the scenario, ask:

- Can every timeline entry be traced to a playbook action? If not, you've invented events. Delete them or justify them.
- Are assumptions realistic for the target audience? If scenario assumes enterprise-grade RPKI monitoring, but you're training teams that don't have it, assumptions are 
wrong.
- Is timing plausible? BGP shouldn't propagate instantly. RPKI shouldn't update in real-time. Humans shouldn't respond in seconds.
-Is noise present? If every event is attack-related, scenario is unrealistic.
- Does it avoid explaining itself? Scenario file should be operational, not educational. README provides education.

## Example from control-plane playbooks

Full `scenario.yaml` structure for the three-phase control-plane attack:

```yaml
id: control-plane-poisoning
name: "The Poisoned Registry"
difficulty: hard
duration: 900

assumptions:
  victim:
    as: 65001
    prefix: "203.0.113.0/24"
    rpki_deployed: true
    rpki_audit_monitoring: false
  attacker:
    as: 64513
    has_credentials: true
    capability: advanced

timeline:
  - t: 0
    action: "rpki_reconnaissance"
  - t: 60
    action: "establish_legitimate_presence"
  - t: 300
    action: "create_fraudulent_roa"
    detection_window: "audit_logs"
  - t: 330
    action: "rpki_propagation_delay"
  - t: 600
    action: "announce_hijack_prefix"
    rpki_state: "VALID"  # Because ROA exists
  - t: 660
    action: "traffic_interception_confirmed"
  - t: 720
    action: "noise_generation"
  - t: 900
    action: "scenario_end"

background_noise:
  enable: true
  bgp_rate: 0.5
  rpki_rate: 0.01
  alert_rate: 2.0
```

This is operational definition, not attack narrative. Narrative lives in README.

## When scenario.yaml is done

You know scenario.yaml is complete when:
- Every entry maps to playbook action or realistic noise
- Timing is plausible (not instant, not impossibly long)
- No explanations snuck in
- Background noise configured
- Assumptions match playbook preconditions

You know scenario.yaml is wrong when:
- Events explain themselves
- Timing is convenient rather than realistic
- Every event is attack-related (no noise)
- Assumptions are aspirational rather than realistic

The file should be boring enough that reading it doesn't spoil the exercise. Save excitement for the debrief when 
defenders realise what they missed.
