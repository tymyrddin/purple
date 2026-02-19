# Systemic stressors

The city is not a blank slate. These pre-existing conditions shape how disruptions unfold and who they hurt most.

Stressor levels are city-wide floats (0.0–1.0). They are set at game start from `config/threats/stressors.yml` and drift over time based on player decisions. District YAML files use string labels (`extreme`, `chronic`, `high`, `moderate`, `victim`, `amplifier`, `beneficiary`) to modify local event probability for events with a matching `stressor_amplifier`.

## Austerity and underinvestment

The Patrician runs a famously tight budget. Maintenance is deferred, upgrades are delayed, and reserve capacity is minimal. Systems work until they suddenly don't.

Amplifies: Degradation and neglect, operational error (due to untrained staff or outdated procedures).

*Engine effects:*
- `underinvestment` amplifies event probability when used as a `stressor_amplifier` in event templates.
- `extends_recovery_time`: multiplies the stressor-adjusted effective downtime at remedy application. At level 1.0 with `extends_recovery_time: 2.0`, repair times double.
- Stressor drift: rises by `neglect_increase` each day at least one event has been ignored for >24h; rises by `budget_cut_increase` each month when public trust is below the tax-penalty floor.

## Just-in-time logistics

Ankh-Morpork eats, and it eats *now*. Food arrives daily from the Sto Plains. Manufacturing relies on parts that arrive exactly when needed. There is almost no slack in the system.

Amplifies: Transport disruption, commercial disruption, supply chain failure.

*Engine effects:*
- `just_in_time` amplifies event probability when used as a `stressor_amplifier` in event templates.
- `domain_multipliers` in cascade propagation: the `just_in_time` level scales the cascade trust-damage delta for matching domains (e.g., food, transport). Higher just_in_time means each cascade causes more trust damage per event, modelling a supply chain with no buffer stock.

## Vendor monoculture

Many critical systems rely on a single provider. A single firm manages most traffic control. A single clacks company carries most financial data. A single engineering guild maintains most pumping stations.

Amplifies: Supply chain and vendor failure, strategic interference (a single point of pressure).

*Engine effects:*
- `vendor_monoculture` amplifies event probability when used as a `stressor_amplifier` in event templates.
- Cascade scope escalation: when a cascade event has `cascade_scope: neighbours`, there is a `vendor_monoculture`-level probability it escalates to city-wide scope (e.g., at level 0.7, 70% chance a local cascade becomes city-wide). This models a single vendor failure propagating everywhere simultaneously.
- A multiplier can also be applied to cascade trust damage for affected domains.

## Social and spatial inequality

The city is starkly divided. The wealthy hills of Nap Hill have redundant connections and rapid response. The Shades, and other poorer districts, have ageing infrastructure and are last to be restored. This inequality is built into the very pipes and wires.

Amplifies: Unequal impact, residential disruption, loss of trust.

*Engine effects:*

The city-wide `social_inequality` level (a float 0.0–1.0) is applied as a trust-damage multiplier on every negative district trust delta, scaled by the district's inequality label:

| District label              | Formula                       | Effect at global level 0.7 |
|-----------------------------|-------------------------------|----------------------------|
| `victim` (Shades, Cockbill) | `1.0 + level × 0.8`           | +56% trust damage          |
| `moderate` (Small Gods)     | `1.0 + level × 0.3`           | +21% trust damage          |
| `beneficiary` (Nap Hill)    | `max(0.3, 1.0 − level × 0.4)` | −28% trust damage          |

*Only negative effects are amplified. Positive trust recovery is not scaled.*

Stressor drift: inequality rises when remedies are applied to high-wealth districts and falls when `resilience_investment` is applied to low-wealth districts.

## Organisational fragmentation

Responsibility is split between the Patrician's office, the Guilds, the City Watch, and private companies. In a crisis, no one is sure who is in charge, and information moves slowly between silos.

Amplifies: Operational error, delayed recovery, confused communication.

*Engine effects:*
- `organisational_fragmentation` amplifies event probability when used as a `stressor_amplifier` in event templates.
- `delays_response`: multiplies effective downtime at remedy application alongside `underinvestment.extends_recovery_time`. At level 1.0 with `delays_response: 1.5`, repair times increase by 50%.
- `accelerates_trust_decay`: scales scandal damage for ignored events. At level 0.5 with factor 1.2, each scandal tick is 10% worse. Applied via `scandal_org_frag_mult` in `apply_passive_dynamics`.
- Stressor drift: rises by `neglect_increase` each day events are ignored; rises by `budget_cut_increase` each month under fiscal pressure.
