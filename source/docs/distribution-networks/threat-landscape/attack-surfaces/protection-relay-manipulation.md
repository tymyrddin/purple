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

An attacker modifying relay thresholds degrades protection. Raising the instantaneous overcurrent threshold (1200A to
1600A) stops the relay clearing a heavy fault at once; the slower time-overcurrent element still trips, but only after
its grading delay, so the fault burns longer and the faulted plant takes more thermal stress before it clears. The local
relay still clears the fault, just late. Only when a whole element is defeated, its pickup lifted beyond any real fault,
does clearance fall to a slower upstream backup and the outage spread wider.

    OVERCURRENT RELAY PROTECTION LOGIC: Attack Surface
    ──────────────────────────────────────────────────

    NORMAL OPERATION: Three-parameter protection chain
    ──────────────────────────────────────────────────

    Incoming current  (primary amps)
              │
      ┌───────┴───────────────┐
      ↓                       ↓
    ┌─────────────────────────┐   ┌────────────────────────────┐
    │ 51 time-overcurrent     │   │ 50 instantaneous           │
    │ pickup 300A             │   │ threshold 1200A            │
    │ (set above ~200A load)  │   │ (heavy fault, trips fast)  │
    └────────────┬────────────┘   └─────────────┬──────────────┘
         I > 300A?                        I > 1200A?
                 │ YES                            │ YES
                 ↓                                ↓
         hold time delay 300ms              TRIP (no delay)
         (graded with upstream relays)
                 │ delay expires
                 ↓
               TRIP

    Either element opens the breaker. The attacker's targets are the 51
    pickup, raised to hide smaller faults, and the 50 threshold or the time
    delay, raised to slow the clearance of a heavy one.


    ATTACK SCENARIO: Pickup raised, smaller faults go unseen
    ────────────────────────────────────────────────────────

    Normal:
      load          ~200A
      51 pickup     300A     (trips after the time delay)
      50 threshold  1200A    (trips at once)

    After the attacker raises the 51 pickup to 450A:
      A high-impedance or remote fault drawing 300-450A no longer starts the
      time element, so it is never cleared. The band the old pickup would
      have caught is now unprotected, and the relay looks healthy on load.
      Raising pickup only removes sensitivity: the zone goes deaf to weak
      faults, it does not become hair-trigger.


    ATTACK SCENARIO: Instantaneous slowed, a heavy fault clears late
    ────────────────────────────────────────────────────────────────

    Normal:
      50 threshold  1200A    → a 1500A fault trips at once
      51 delay      300ms

    After the attacker raises the 50 threshold to 1600A (or lengthens the
    delay):
      A 1500A fault no longer gets the instantaneous trip; it waits out the
      slower time-overcurrent delay instead. Clearance is late and the faulted
      plant heats for longer, though the local 51 still clears it ahead of any
      upstream backup, so grading holds and the fault stays local.


    INTERCONNECTED CONSTRAINT: What the attacker cannot hide
    ─────────────────────────────────────────────────────────

    Baseline comparison (DIGSI 5 online-vs-offline):
      Settings file on engineering workstation shows: 51 pickup 300A, 50 threshold 1200A
      Relay reports (queried live): 51 pickup 450A, 50 threshold 1600A
      → MISMATCH flagged immediately

    Attacker's only solution: Corrupt BOTH
      1. Modify relay settings in field
      2. Update baseline in engineering tool database
      3. Both have to match for "online-vs-offline" check to pass

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
appropriate. A relay picking up at 300A responds to faults above 300A; one shifted to 450A ignores the band beneath.

An attacker who increases a relay's pickup setting would cause the relay to ignore smaller faults. In a distribution
network where many protection zones overlap (where multiple relays could potentially protect a fault), increasing a
relay's pickup in one zone might cause that zone's relay to not respond, leaving protection to a less-sensitive relay
elsewhere. This can change the effective protection strategy of the network.

What makes a pickup change hard to catch is that it interacts with load. A relay's pickup has to sit above the normal
maximum load, or it would trip on load alone, so nudging it upward reads as a routine margin adjustment against rising
demand rather than as tampering, even as it widens the band of real faults the relay will now sit through.

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
