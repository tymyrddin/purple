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