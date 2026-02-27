# Recovery pathways

How the city chooses to recover shapes its future resilience and the public's trust.

## Technical restoration

Fixing the immediate problem. Restoring service to pre-incident levels. Fastest option, but may not address underlying causes. Carries a recurrence risk, the same building may fail again sooner.

*In-game remedy: `technical_restoration`. Short downtime (4h base). Moderate cost.*

## Resilience investment

Rebuilding to a higher standard. Adding redundancy, upgrading systems, training staff. Slower and more expensive, but reduces future risk and improves the district's `infrastructure_quality` modifier. Trust gain is delayed, citizens only notice the improvement once it has been running for a while. Politically difficult to justify unless the crisis was severe enough.

*In-game remedy: `resilience_investment`. Long downtime (72h base). High cost. Reduces `infrastructure_quality` modifier and decreases `underinvestment` stressor on completion.*

## Compensatory measures

Paying for the harm caused. Compensating businesses, waiving fees, providing alternative services (e.g., bottled water). Addresses short-term anger but does not fix the system. The trust boost fades after a few days.

*In-game remedy: `public_compensation`. Zero downtime (resolves immediately). Medium cost. Trust boost reverses after `duration_days`.*

## Operational workaround

Shifting the burden elsewhere rather than fixing it. The problem remains latent; another district or building absorbs the risk. May anger the district that ends up carrying the load.

*In-game remedy: `operational_workaround`. Short downtime. Medium cost. Applies a trust penalty to a randomly chosen other district (`risk_transfer` side effect).*

## Accountability actions

Identifying who or what was responsible. Public inquiries, firings, contract cancellations, regulatory changes. Essential for restoring trust, but can be divisive, may backfire, and does not fix the underlying system.

*In-game remedy: `accountability_action`. Zero downtime. Low cost. Backfire risk: if it misfires, the trust penalty compounds instead of recovering.*

## Press statement

Framing the narrative before the facts settle. Buys a window of reduced scandal pressure, citizens see the statement and hold off on full outrage. But if no concrete action follows within the window, trust falls harder than if nothing had been said.

*In-game remedy: `press_statement`. Zero cost. Zero downtime (does not fix anything). Opens a 48h window: scandal damage during that period is halved (`slows_decay_multiplier`). If no real remedy is applied before the window closes, a `contradicts_penalty` is applied and the event reverts to DETECTED.*

## Do nothing

Choosing not to act. Zero immediate cost, but trust decays faster, duration penalties accumulate daily, and cascade probability on the event is raised (`cascade_risk_boost`). The longer it is ignored, the worse the eventual outcome.

*In-game remedy: `do_nothing`. Zero cost. Raises `cascade_risk_boost` on the event as a side effect.*

## The recovery choice

Every crisis forces a choice between these pathways. The choices made determine not just whether services return, but whether the city emerges stronger, weaker, or more divided.

## Note on effective downtime

When a remedy is applied, the actual repair time (`effective_downtime_hours`) is computed from the base `downtime_hours` adjusted by stressor levels at that moment:

- `underinvestment.extends_recovery_time` multiplies the base time
- `organisational_fragmentation.delays_response` multiplies it further

This value is locked in at the moment of application. Stressor changes after the remedy starts do not retroactively alter the repair schedule. Players see the adjusted time displayed as "Xh remaining of Yh" in the remedy panel.