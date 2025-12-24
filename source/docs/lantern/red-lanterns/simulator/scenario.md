# Creating scenario.yaml

The scenario file defines orchestration, not meaning.

It should be boring. If a scenario YAML reads like a thriller, something has gone wrong. It should read like a 
maintenance schedule that nobody wants to receive twice.

## What belongs in scenario.yaml

### Scenario metadata

```yaml
id: control-plane-poisoning
...
```

### Timeline

One entry per playbook action. Use playbook action numbers as timeline markers.

```yaml
timeline:
  # Phase 1: Registry reconnaissance (playbook actions 1.1-1.3)
  # Compressed to 2 hours simulated time
  
  - t: 0
    
```

Each timeline entry should reference playbook action number. If you can't map a timeline entry to a playbook action, 
delete it.

## Translating playbook timing to scenario timing

Playbooks span weeks. Scenarios span minutes. Preserve decision structure, not calendar time. For example:

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
- Are assumptions realistic for the target audience? If scenario assumes enterprise-grade RPKI monitoring, but you're training teams that don't have it, assumptions are wrong.
- Is timing plausible? BGP shouldn't propagate instantly. RPKI shouldn't update in real-time. Humans shouldn't respond in seconds.
- Is noise present? If every event is attack-related, scenario is unrealistic, but meant for a demo of possible entries to correlate.
- Does it avoid explaining itself? Scenario file should be operational, not educational. README provides education.

## Example from control-plane playbooks

Full scenario.yaml structure for the three-phase control-plane attack:

```yaml
id: control-plane-poisoning

```

This is operational definition, not attack narrative. Narrative lives in README.

