# The translation challenge

The control-plane attack playbooks describe three phases over 3-4 weeks:

Phase 1: [Registry reconnaissance and initial ROA creation](../playbooks/1.md)

- Attacker knows: "I'm mapping RPKI deployment and establishing legitimate presence"
- Defender sees: Nothing. Maybe routine RPKI queries in public API logs (if anyone's looking)

Phase 2: [ROA scope expansion and validation environment mapping](../playbooks/2.md)

- Attacker knows: "I'm poisoning the validation infrastructure with fraudulent ROA"
- Defender sees: ROA creation log entry. Might look like operator error. Might not be noticed at all.

Phase 3: [Prefix hijacking with RPKI validation cover](../playbooks/3.md)

- Attacker knows: "I'm exploiting the poisoned control plane to hijack traffic"
- Defender sees: BGP announcement that validates as VALID. Traffic routing changing. Services degrading. Possibly thousands of unrelated alerts because attacker triggered noise generation.

The scenario must model what defenders see, when they see it, and with what ambiguity.