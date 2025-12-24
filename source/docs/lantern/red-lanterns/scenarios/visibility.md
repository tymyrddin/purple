# The visibility problem

Playbooks assume attacker visibility into their own actions. Scenarios must not.

From the playbook, Phase 2 Action 2.1 (fraudulent ROA creation) is the control-plane attack. It's the moment 
where the Registry gets poisoned. It's the critical action that enables everything else.

But will defenders see it?

Most organisations don't have:

- Real-time RPKI audit log monitoring
- Alerting on ROA creation for prefixes they don't control
- Correlation between ROA changes and BGP announcements

The [Scarlet Semaphore operation doc](https://red.tymyrddin.dev/docs/scarlet/op-red-lantern/roa_poisoning) notes that 
RPKI CA audit logs exist but aren't monitored. ROA changes are logged but not alerted on. Validation state changes 
propagate slowly (30-90 minutes).

A scenario that makes this obviously detectable is lying about defender capabilities.

A better scenario emits:

- ROA creation log (JSON event, timestamped, but not obviously malicious)
- Validator state change 30 minutes later (prefix transitions to "not found" for victim, "valid" for attacker)
- BGP announcement that correlates with ROA change (but only if defenders think to correlate)

Defenders must connect these dots themselves. The scenario doesn't do it for them.