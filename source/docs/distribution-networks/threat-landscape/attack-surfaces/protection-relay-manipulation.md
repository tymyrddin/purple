# Protection relay manipulation

Threats to protection relays: changing trip thresholds, modifying pickup settings, disabling protection functions, or causing false trips. A relay compromise can disable the protection system or cause it to operate incorrectly, leading to cascade failures or leaving faults uncontrolled.

Protection relay settings are managed through engineering tools (DIGSI, AcSELerator) and tested before deployment. Settings are versioned and compared against baselines. Unauthorised changes leave traces in the engineering workstation logs, settings files, and the online-versus-offline comparison.

## Threshold modification

Stedin's protection relays (inferred as SIPROTEC 5 and SEL-451, not independently confirmed) trip when measured electrical quantities exceed configured thresholds. An overcurrent relay trips when current exceeds the threshold, an over-voltage relay trips when voltage exceeds the threshold, a frequency relay trips when frequency deviates beyond the threshold. These thresholds are the front line of protection against faults in Stedin's network.

An attacker modifying relay thresholds disables protection. Increasing an overcurrent threshold (1200A to 1500A) allows larger fault currents without a trip. The fault would then propagate deeper into the network, affecting more equipment and more customers. In cascading-fault scenarios, downstream equipment fails after prolonged stress and significant degradation.

    OVERCURRENT RELAY PROTECTION LOGIC: Attack Surface
    ──────────────────────────────────────────────────

    NORMAL OPERATION: Three-parameter protection chain
    ──────────────────────────────────────────────────

    Incoming current measurement
              │
              ↓
         ┌───────────────────────────────┐
         │ PICKUP: Is I > 5A?            │  ← Minimum sensitivity threshold
         │ (if NO: ignore, stay armed)   │    Usually set above max load
         └──────────────┬────────────────┘
                        │ YES
                        ↓
         ┌───────────────────────────────┐
         │ THRESHOLD: Is I > 1200A?      │  ← Trip level (overcurrent limit)
         │ (fault vs load discrimination)     Attacker target: INCREASE (hide faults)
         └──────────────┬────────────────┘
                        │ YES
                        ↓
         ┌───────────────────────────────┐
         │ TIME DELAY: Hold 100ms        │  ← Coordinated with upstream relays
         │ (let faster relays act first) │    Attacker target: INCREASE (delay trip)
         └──────────────┬────────────────┘
                        │ DELAY EXPIRES
                        ↓
                   🔴 TRIP RELAY


    ATTACK SCENARIO: Threshold manipulation
    ────────────────────────────────────────

    Normal setting:
      Pickup: 5A (above 3A max load)
      Threshold: 1200A
      Delay: 100ms
      → Trip on sustained 1200A current within 100ms

    After attacker modifies (DIGSI 5 or AcSELerator QuickSet):
      Pickup: 5A (unchanged, appears normal)
      Threshold: 1500A (MODIFIED: +300A margin)
      Delay: 100ms (unchanged)

    Result:
      • Fault current 1200-1500A: Relay sees current > pickup but < threshold → NO TRIP
      • Fault propagates further into network
      • Downstream equipment overheats and fails
      • Cascade spreads to adjacent zones


    ATTACK SCENARIO: Pickup increase (more dangerous)
    ──────────────────────────────────────────────────

    Normal setting:
      Pickup: 5A
      Threshold: 1200A
      → Responds to any fault above 5A

    After attacker modifies:
      Pickup: 40A (MODIFIED: shifted above normal 3A load)
      Threshold: 1200A (unchanged)

    Zone behaviour:
      • Load current swings 25A-35A: Relay responds (I > pickup)
      • Load current spikes 38A: Relay still responds (I > pickup)
      • Load current temporarily 42A during startup: Relay NOW IGNORES (threshold not exceeded yet)
      • This creates false sense of protection during transient events
      • Protection zone becomes "hair-trigger" on benign swings, deaf to real faults


    INTERCONNECTED CONSTRAINT: What the attacker cannot hide
    ─────────────────────────────────────────────────────────

    Baseline comparison (DIGSI 5 online-vs-offline):
      Settings file on engineering workstation shows: Threshold 1200A, Pickup 5A
      Relay reports (queried live): Threshold 1500A, Pickup 40A
      → MISMATCH flagged immediately

    Attacker's only solution: Corrupt BOTH
      1. Modify relay settings in field
      2. Update baseline in engineering tool database
      3. Both must match for "online-vs-offline" check to pass

    Evidence emerges if:
      • Baseline not recently checked (audit gap)
      • Relay event logs record settings-change timestamp (who, when)
      • Maintenance records show no authorised change
      • Next firmware update from engineering tool: forces relay to baseline (corrupts it back)


The attacker faces a choice: modify the thresholds gradually over multiple maintenance cycles (so that each individual change appears normal), or modify them suddenly (in which case a settings comparison would immediately flag the change). An attacker with inside knowledge of the maintenance schedule might insert a threshold change during a legitimate maintenance window, making it appear as an authorised change.

## Pickup setting compromise

A Stedin relay's pickup setting defines the current level at which the relay begins to respond to a fault. Below the pickup current, the relay ignores the fault. At and above the pickup, the relay measures the time delay and trips if appropriate. A relay with a 5A pickup setting will respond to faults greater than 5A; a relay with a 50A pickup will ignore smaller faults.

An attacker who increases a relay's pickup setting would cause the relay to ignore smaller faults. In Stedin's distribution network where many protection zones overlap (where multiple relays could potentially protect a fault), increasing a relay's pickup in one zone might cause that zone's relay to not respond, leaving protection to a less-sensitive relay elsewhere. This can change the effective protection strategy of the network.

Pickup setting changes are often less obvious than threshold changes because they interact with the network's load current. A relay's pickup must be set above the normal maximum load current, or it would trip constantly. An attacker who increases the pickup to just above Stedin's known maximum load would appear to be setting it reasonably, but would actually be creating a narrow margin that could be exceeded during high-load conditions.

## Protection function disabling

Some protection relays have multiple protection functions: overcurrent, over-voltage, under-voltage, frequency, and others. These can be individually enabled or disabled. An attacker who can disable a protection function would remove protection from that class of faults.

Disabling a protection function is a more obvious attack than modifying a threshold, because the online-versus-offline comparison would show a function that is disabled when it should be enabled. An attacker might disable a function to hide a settings change, expecting that the function is not regularly tested and that the disabling would go unnoticed. But modern protection-maintenance practices include periodic functional testing of relays, and a disabled function would likely be caught.

Alternatively, an attacker might temporarily disable a protection function around the time of an intended attack (causing a fault when the protection is disabled), then re-enable the function after the attack, hoping that the window of disability is not discovered.

## False trip injection

A compromised relay at Stedin could trip when it should not, causing an unnecessary outage. This can be caused by modifying a relay's logic so that it trips at the wrong condition, or by commanding the relay to trip directly through its output coil.

False trips are damaging because they cause unplanned outages and degrade customer confidence in Stedin. They also consume the operator's emergency-response resources. A pattern of false trips from a particular relay might cause the operator to question the relay's reliability and might lead to it being bypassed or removed, which would then remove protection from that zone. An attacker could strategically cause false trips to degrade confidence in a particular protection zone, then replace the relay with a compromised device that has disabled protection.

## Settings baseline divergence

Stedin's protection relay settings are stored in the relay's non-volatile memory and are also stored in the engineering tool database (on the engineering workstation or in a centralised configuration repository). Standard maintenance procedure is to connect to a relay periodically and compare the current settings against the baseline to detect divergence. How these baselines are maintained and tested is foundational to catching unauthorised changes, and rests on [how Stedin verifies and documents relay settings](../../operating-context/operations-and-cadence/maintenance-philosophy.md).

A relay with diverged settings indicates either that a maintenance activity modified the settings (which should be documented and approved at Stedin), or that an unauthorised modification has occurred. The distinction depends on whether the settings change matches the documented maintenance and whether the change was approved.

An attacker would need to modify both the relay's settings and the baseline in Stedin's engineering tool database to hide the change. If only the relay is modified and the baseline remains unchanged, an online-versus-offline comparison will immediately reveal the mismatch. If only the baseline is modified and the relay remains unchanged, a later maintenance activity that updates the relay from the baseline will silently corrupt the relay's settings, which will be obvious once the relay is tested under fault conditions.

A sophisticated attacker might compromise Stedin's engineering tool database to store a false baseline, then compromise a relay to run a different (malicious) configuration. The online-versus-offline comparison would show a match (because both the relay and the baseline are compromised), but the relay is actually running the wrong settings. This would require compromising two separate systems, which is more difficult but more durable.

Evidence of relay setting changes emerges from multiple sources: the relay's own event log (which records when settings were changed and often records who changed them, if the relay has an audit capability), the engineering tool's connection logs (showing when DIGSI 5 or AcSELerator QuickSet connected to the relay and what was read or written), the maintenance records (which document what settings changes were approved and when), and as-found-and-as-left records that document the state of the relay before and after maintenance. The challenge is that legitimate maintenance generates the same evidence trail. An engineer connecting to a relay and modifying settings leaves the same logs as an attacker would. The distinction emerges from whether the activity was authorised, whether it matches the documented scope of work, and whether the settings change is consistent with the intended maintenance outcome.

*Last updated: 10 July 2026*
