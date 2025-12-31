# Control-plane attack chain: summary

## Why these three playbooks form a chain

These playbooks implement a true [control-plane attack](https://purple.tymyrddin.dev/docs/lantern/red-lanterns/control-vs-data-plane), not data-plane abuse.

From the [BGP hijacking tree](https://red.tymyrddin.dev/docs/in/network/roots/ip/bgp-hijacking), most attacks are 
data-plane: they announce false routes (forged letters). Defenses like RPKI are designed to catch these by checking 
announcements against authoritative ROAs (the Guild Registry).

This attack chain corrupts the Registry itself. By phase 3, when we hijack traffic, RPKI validation **endorses our 
hijack as legitimate**. We're not bypassing security. We're corrupting the foundations security depends on.

## The three phases

### Phase 1: Registry reconnaissance and initial ROA creation

**Objective:** Establish ourselves as normal RPKI participant

**Key actions:**
- Map victim's RPKI deployment status
- Create legitimate ROA for our own resources
- Document baseline state before manipulation

**Success metric:** We appear as routine RPKI-aware network operator

**Control-plane relevance:** Reconnaissance of validation infrastructure, establishing trust

### Phase 2: ROA scope expansion and validation environment mapping  

**Objective:** Poison the validation infrastructure

**Key actions:**
- Create fraudulent ROA authorising our AS for victim's prefix
- Map which regions enforce RPKI validation
- Deploy monitoring for ROA status changes

**Success metric:** Fraudulent ROA published and stable for 48+ hours

**Control-plane relevance:** **This is the control-plane attack**. We've edited the authoritative registry. From this point forward, validators will endorse our announcements as legitimate.

### Phase 3: Prefix hijacking with RPKI validation cover

**Objective:** Exploit poisoned validation infrastructure to hijack traffic

**Key actions:**
- Announce more-specific prefix from our AS
- Verify traffic interception
- Forward traffic to maintain service (reduce detection)
- Monitor for detection indicators
- Execute controlled withdrawal

**Success metric:** Traffic intercepted whilst RPKI validation returns VALID

**Control-plane relevance:** Payoff. Our hijack appears legitimate to validation systems because we corrupted them in phase 2.

## Why this is different from normal BGP hijacks

**Data-plane hijack (typical BGP attack):**
```
Attacker: "I originate 203.0.113.0/24"
RPKI Validator: "Checking ROAs... INVALID. Drop this announcement."
Defense: Works as designed.
```

**Control-plane attack (this playbook chain):**
```
Phase 1-2: Attacker creates fraudulent ROA
Phase 3: "I originate 203.0.113.128/25"
RPKI Validator: "Checking ROAs... VALID. Accept this announcement."
Defense: Fails because validation system itself is compromised.
```

The distinction from the [control-plane vs data-plane page](https://purple.tymyrddin.dev/docs/lantern/red-lanterns/control-vs-data-plane):

> Most BGP incidents are forged letters carried by an overly trusting postal service. Control-plane attacks rewrite the Guild Registry itself. From that moment on, everyone is "following the rules". The rules are simply wrong.

That's exactly what we've done. Validators are following the rules (check announcements against ROAs). The ROAs are simply wrong (because we poisoned them).

## Timeline and dependencies

```
Week 1-2: Phase 1
├─ Day 1: Reconnaissance (Action 1.1)
├─ Day 2: Create our legitimate ROA (Action 1.2)
├─ Day 2-3: Wait for publication (30-90 minutes)
├─ Day 3-7: Baseline documentation (Action 1.3)
└─ Day 7: Waiting period (establish presence)

Week 3: Phase 2 (HIGH RISK)
├─ Day 1: Create fraudulent ROA (Action 2.1) ← CRITICAL, may fail
├─ Day 1: Wait for publication (2-4 hours)
├─ Day 2: Map validation deployment (Action 2.2)
├─ Day 3-4: Deploy monitoring (Action 2.3)
└─ Day 5-7: Waiting period (ensure ROA stable)

Week 4: Phase 3 (VISIBLE)
├─ Hour 0: Announce hijack prefix (Action 3.1)
├─ Hour 0-1: Verify interception (Action 3.2)
├─ Hour 1: Establish forwarding (Action 3.3)
├─ Hours 1-X: Monitor hijack (Action 3.4)
└─ Hour X: Controlled withdrawal (Action 3.5)
```

Total timeline: 3-4 weeks from start to completion.

Critical path: Phase 2 Action 2.1 (fraudulent ROA creation). If this fails, entire chain aborts.

## Prerequisites

This attack chain requires:

**Technical:**
- BGP peering session (for announcement in phase 3)
- AS number allocation (legitimately obtained)
- IP address allocation (for creating legitimate ROA in phase 1)
- Forwarding infrastructure (for polite hijacking in phase 3)

**Access:**
- Compromised RIR account credentials (for creating fraudulent ROA in phase 2)
- OR insider access to victim's RPKI infrastructure
- OR exploit in RIR validation logic

**Operational:**
- Multi-week operational security (attack spans 3-4 weeks)
- 24/7 monitoring capability during phase 3
- Abort procedures prepared (for rapid withdrawal if detected)

The credential compromise prerequisite is often the hardest part. This playbook assumes it's already accomplished. In reality, obtaining RIR account access may require separate attack operation (phishing, credential stuffing, social engineering).

## Detection and countermeasures

**Where defenders can catch this:**

Phase 1:
- Detection likelihood: ~0%
- Appears like routine RPKI deployment

Phase 2:
- Detection likelihood: ~30-50%
- Fraudulent ROA creation may trigger RIR validation alerts
- RPKI audit logs show ROA for prefix we don't control
- Requires defender actually reviewing audit logs (rare)

Phase 3:
- Detection likelihood: ~40-70% (varies by victim's monitoring)
- BGP announcement visible in public monitors
- Traffic path changes visible in NetFlow
- **But RPKI validation returns VALID**, reducing alert priority

**Why RPKI validation fails to detect:**

RPKI is designed to prevent unauthorised announcements by checking against authoritative ROAs. This attack works because:

1. We created authoritative ROA (phase 2)
2. Validators trust that ROA (it's signed by RIR)
3. Our announcement matches ROA (AS64513 for 203.0.113.0/24 maxLength /25)
4. Validation returns VALID

The defense mechanism is working correctly. It's checking the right source. The source is simply poisoned.

**Effective countermeasures:**

1. **RPKI audit logging and review**
   - Monitor for ROA creation/modification
   - Alert on ROAs for prefixes not allocated to account
   - Requires active log review (not just collection)

2. **Multi-path validation**
   - Don't rely solely on RPKI
   - Correlate RPKI with IRR, WHOIS, manual verification
   - Flag announcements that validate via RPKI but fail other checks

3. **Traffic baseline monitoring**
   - Monitor traffic source AS distribution
   - Alert on sudden shifts (traffic now coming from unexpected AS)
   - Requires NetFlow analysis and baselining

4. **BGP community-based validation**
   - Use signed BGP communities for additional validation layer
   - Requires widespread deployment (not currently available)

The most effective countermeasure is **RPKI audit trail monitoring**, which would catch phase 2 before phase 3 executes. Most organisations don't have this because RPKI itself is new and auditing the validation infrastructure is not yet standard practice.

## Operational security considerations

**Attribution risk:**

Low during phase 1 (appears legitimate)
High during phase 2 (fraudulent ROA creation leaves audit trail)
Medium during phase 3 (announcement visible but plausibly deniable as "testing")

Post-operation, the strongest evidence is:
- RIR audit logs showing fraudulent ROA creation from specific account
- Timeline correlation (ROA created, announcement made, withdrawal executed)
- If investigation reaches this depth, cover story of "operator error" becomes less plausible

**Cover stories:**

Phase 2 detection: "Spreadsheet error during bulk ROA update, accidentally included wrong prefix"
Phase 3 detection: "Testing RPKI deployment, mistakenly announced prefix from test configuration"

Both are plausible because RPKI is complex and these errors genuinely happen. Cover stories become less believable if:
- Multiple phases detected and correlated
- Timeline shows coordination (too precise to be accidental)
- Forwarding infrastructure discovered (demonstrates intent, not accident)

**Cleanup:**

Post-operation, revoke fraudulent ROA promptly. Long-term persistence is strongest evidence of deliberate attack versus mistake.

## Why this chain was selected for Red Lantern

These three playbooks demonstrate:

1. **Structural vulnerability in trust infrastructure**
   - RPKI is meant to secure BGP
   - RPKI itself can be compromised
   - Defense becomes attack vector

2. **Multi-phase attack requiring operational security**
   - Not single-action attack
   - Requires weeks of preparation
   - Tests detection across multiple phases

3. **Realistic attack path with budget reality gaps**
   - Credential compromise (happens)
   - Incomplete RPKI auditing (common)
   - Limited validation deployment (40% globally)

4. **Clear distinction between control-plane and data-plane**
   - Explicitly demonstrates Registry manipulation
   - Shows why validation alone insufficient
   - Illustrates need for validation system auditing

This is valuable for Wazuh detection engineering because:
- Most BGP detection rules focus on announcements (data-plane)
- Few rules exist for RPKI infrastructure monitoring (control-plane)
- This attack shows why both layers need monitoring

## Limitations and caveats

This attack chain will **fail** if:
- RIR has robust ROA validation (catches fraudulent ROA in phase 2)
- Victim has RPKI audit monitoring (detects fraudulent ROA before phase 3)
- Global RPKI validation enforcement >80% (our announcement dropped everywhere)
- Victim has real-time BGP monitoring with alerting (detected in phase 3 within minutes)

Success requires victim to have:
- Partial or absent RPKI auditing (common)
- Incomplete validation deployment globally (currently true, ~40% deployment)
- Limited BGP monitoring (common outside major transit providers)

As RPKI deployment increases and auditing practices mature, this attack path becomes less viable. Currently (2024-2025), it remains realistic threat.

## References

- [BGP hijacking attack tree](https://red.tymyrddin.dev/docs/in/network/roots/ip/bgp-hijacking) - structural attack taxonomy
- [Control-plane vs data-plane distinction](../spark/control-vs-data-plane.md) - conceptual framework
- [RPKI documentation](https://www.ripe.net/manage-ips-and-asns/resource-management/certification) - validation infrastructure
- [Routinator RPKI validator](https://www.nlnetlabs.nl/projects/rpki/routinator/) - validation tool
- [BGPmon public monitoring](https://www.bgpmon.net/) - announcement visibility

## Success criteria for complete chain

The three-phase chain succeeds when:

1. Fraudulent ROA is created and remains published (phase 2)
2. Traffic is intercepted with RPKI validation returning VALID (phase 3)
3. Operational objective achieved (traffic visibility/interception for required duration)
4. Clean withdrawal executed without detection (phase 3)
5. Post-operation cleanup completed (fraudulent ROA revoked)

The chain demonstrates control-plane attack if validation systems endorsed our hijack as legitimate at time of execution, even if later investigation reveals the attack.

From the purple page:

*A control-plane attack, properly defined, does not lie within the rules. It rewrites the rules themselves.*

That's what we've accomplished. We rewrote the RPKI rules (phase 2), then operated within those corrupted rules (phase 3). Everyone followed the rules. The rules were simply wrong.

## Related

- [A first look at common RPKI publication practices, 2025](https://arxiv.org/html/2512.16369v1)
- [RPKI Read the docs Securing BGP, 2025](https://rpki.readthedocs.io/en/latest/rpki/securing-bgp.html)
- [ARIN: RPKI Best Practices and Lessons Learned, 2025](https://www.arin.net/blog/2025/09/25/nro-rpki-best-practices/)
- [ARIN: RPKI Best Practices and Troubleshooting](https://www.arin.net/resources/manage/rpki/help/bestpractices/)
