# Protection relay manipulation

Attacks on protection relays cluster around a few moves: changing trip thresholds, modifying pickup settings, disabling
protection functions, or causing false trips. A relay compromise can disable the protection system or cause it to
operate incorrectly, leading to cascade failures or leaving faults uncontrolled.

Protection relay settings are managed through engineering tools (DIGSI, AcSELerator) and tested before deployment.
Settings are versioned and compared against baselines. Unauthorised changes leave traces in the engineering workstation
logs, settings files, and the online-versus-offline comparison.

## Threshold modification

The portrait's protection relays (inferred as SIPROTEC 5 and SEL-451, not independently confirmed yet) trip when
measured electrical quantities exceed configured thresholds. An overcurrent relay trips when current exceeds the
threshold, an over-voltage relay trips when voltage exceeds the threshold, a frequency relay trips when frequency
deviates beyond the threshold. These thresholds are the front line of protection against faults in the network.

An attacker modifying relay thresholds disables protection. Increasing an overcurrent threshold (1200A to 1500A) allows
larger fault currents without a trip. The fault would then propagate deeper into the network, affecting more equipment
and more customers. In cascading-fault scenarios, downstream equipment fails after prolonged stress and significant
degradation.

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
      Pickup: 40A (MODIFIED: shifted well above normal 3A load)
      Threshold: 1200A (unchanged)

    Zone behaviour:
      • Normal load 1A-3A: below pickup, relay idle (correct, as before)
      • High-impedance or remote fault drawing 20A-35A: now below the
        40A pickup, so the relay stays idle and the real fault is missed
      • Only currents above 40A start the element at all
      • The whole 5A-40A band the old pickup would have caught is now
        unprotected, while the zone looks healthy day to day
      • Deaf to weak faults, not hair-trigger: raising pickup only
        removes sensitivity


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

An attacker faces a choice: modify the thresholds gradually over multiple maintenance cycles (so that each individual
change appears normal), or modify them suddenly (in which case a settings comparison would immediately flag the change).
An attacker with inside knowledge of the maintenance schedule might insert a threshold change during a legitimate
maintenance window, making it appear as an authorised change.

## Pickup setting compromise

A relay's pickup setting defines the current level at which the relay begins to respond to a fault. Below the pickup
current, the relay ignores the fault. At and above the pickup, the relay measures the time delay and trips if
appropriate. A relay with a 5A pickup setting will respond to faults greater than 5A; a relay with a 50A pickup will
ignore smaller faults.

An attacker who increases a relay's pickup setting would cause the relay to ignore smaller faults. In a distribution
network where many protection zones overlap (where multiple relays could potentially protect a fault), increasing a
relay's pickup in one zone might cause that zone's relay to not respond, leaving protection to a less-sensitive relay
elsewhere. This can change the effective protection strategy of the network.

Pickup setting changes are often less obvious than threshold changes because they interact with the network's load
current. A relay's pickup must be set above the normal maximum load current, or it would trip constantly. An attacker
who increases the pickup to just above the known maximum load would appear to be setting it reasonably, but would
actually be creating a narrow margin that could be exceeded during high-load conditions.

## Protection function disabling

Some protection relays have multiple protection functions: overcurrent, over-voltage, under-voltage, frequency, and
others. These can be individually enabled or disabled. An attacker who can disable a protection function would remove
protection from that class of faults.

Disabling a protection function is a more obvious attack than modifying a threshold, because the online-versus-offline
comparison would show a function that is disabled when it should be enabled. An attacker might disable a function to
hide a settings change, expecting that the function is not regularly tested and that the disabling would go unnoticed.
But modern protection-maintenance practices include periodic functional testing of relays, and a disabled function would
likely be caught.

Alternatively, an attacker might temporarily disable a protection function around the time of an intended attack (
causing a fault when the protection is disabled), then re-enable the function after the attack, hoping that the window
of disability is not discovered.

## False trip injection

A compromised relay could trip when it should not, causing an unnecessary outage. This can be caused by modifying a
relay's logic so that it trips at the wrong condition, or by commanding the relay to trip directly through its output
coil.

False trips are damaging because they cause unplanned outages and degrade customer confidence. They also consume the
operator's emergency-response resources. A pattern of false trips from a particular relay might cause the operator to
question the relay's reliability and might lead to it being bypassed or removed, which would then remove protection from
that zone. An attacker could strategically cause false trips to degrade confidence in a particular protection zone, then
replace the relay with a compromised device that has disabled protection.

## Settings baseline divergence

Protection relay settings live in the relay's non-volatile memory and in the engineering-tool database, and a routine
online-versus-offline comparison is what a single-sided change runs into. Two things have to hold for that to work. *The
comparison catches a single-sided change only if someone runs it on a cadence short enough to matter, and only if the
stored baseline is itself trustworthy. More often than not the check is manual and tied to a maintenance visit rather
than continuous, and the engineering-tool baseline is rarely reconciled against an independent record, so an attacker
who corrupts both sides has a long window before anyone looks.* Which is why a divergence is not self-explaining: it has
[three readings](../../observable-semantics/field-devices-and-protection/protection-relay-state.md), authorised, stale
baseline, or unauthorised, and separating them is the whole task.

To hide a change, then, an attacker has to modify both the relay's settings and the baseline in the engineering-tool
database. Change only the relay and the comparison flags the mismatch; change only the baseline and a later maintenance
update silently corrupts the relay, which shows once it is tested under fault conditions. Compromising both, the relay
to run a malicious configuration and the database to store a matching false baseline, defeats the comparison, but takes
two separate systems and is correspondingly harder, if more durable.

## Observable traces

Relay setting changes surface in the
[relay's own event log](../../observable-semantics/field-devices-and-protection/protection-relay-state.md), the DIGSI 5
or AcSELerator QuickSet connection logs, the maintenance records, and the as-found-and-as-left comparison, all of which
legitimate maintenance produces too.

*Last updated: 13 July 2026*
