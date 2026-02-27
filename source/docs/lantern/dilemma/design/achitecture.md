# Architecture

## Data-driven engine, YAML all the way down

[Metrics](../metrics/index.rst) defines an enormous amount of tabular data (district stats, building types, metric 
behaviours, threat chains, remedies, detection times). All of that lives in YAML. The Python engine just reads the 
rules and runs them.

## Directory structure

```
ankh-crisis-sim/
├── config/                          # ALL game data lives here
│   ├── game.yml                     # Global settings: time scale, starting budget, term length
│   ├── metrics/
│   │   ├── global.yml               # Public Trust, Budget, Regulatory Pressure, Political Stability, Legitimacy
│   │   └── district.yml             # District metric templates (decay rates, recovery rates per remedy)
│   ├── districts/
│   │   ├── nap_hill.yml             # Wealth, density, infrastructure quality, influence, media multiplier, stressors
│   │   ├── the_shades.yml
│   │   ├── cockbill_street.yml
│   │   ├── isle_of_gods.yml
│   │   ├── university_precinct.yml
│   │   ├── merchant_quarter.yml
│   │   ├── small_gods.yml
│   │   └── river_ankh.yml
│   ├── buildings/
│   │   ├── _types.yml               # Building type templates (24 types: guild_hq, tavern, apothecary, intelligence_service, etc.)
│   │   └── instances.yml            # Actual buildings: name, type, district, position, dependencies, narrative hooks
│   ├── threats/
│   │   ├── categories.yml           # 6 threat categories with disruption types
│   │   ├── stressors.yml            # 5 systemic stressors, starting values, amplification rules
│   │   └── events.yml               # Concrete event templates: trigger conditions, impact chains, narratives
│   ├── remedies.yml                 # The 7 remedy types with costs, effects, narrative text
│   ├── detection.yml                # Detection mechanisms, discovery times per district/building type
│   ├── narratives/
│   │   ├── headlines.yml            # Layer 1: simple headline templates
│   │   └── stories.yml              # Layer 2: richer story templates with variables
│   └── end_conditions.yml           # Loss/neutral/escape conditions with thresholds
│
├── src/
│   ├── __init__.py
│   ├── main.py                      # Entry point
│   ├── config/
│   │   ├── __init__.py
│   │   └── loader.py                # YAML loader, validates + merges configs into typed dataclasses; holds GameSettings
│   ├── engine/
│   │   ├── __init__.py
│   │   ├── simulation.py            # Main loop: tick, advance time, check events, resolve effects
│   │   ├── clock.py                 # Game clock: real-time, pause, speed multiplier
│   │   ├── metrics.py               # Metric state + update rules (trust decay, passive dynamics, inequality modifier)
│   │   ├── events.py                # Event generation: weighted random based on stressors + neglect + event_rate_multiplier
│   │   ├── dependencies.py          # Dependency graph: cascading failures, propagation (cascade_multiplier param)
│   │   ├── detection.py             # Discovery time calculation, hidden vs. visible failures (discovery_speed_multiplier)
│   │   ├── remedies.py              # Remedy application, delayed effects, recurrence risk
│   │   ├── narrative.py             # Headline/story generation from templates + current state
│   │   └── end_check.py             # End condition evaluation; respects game_duration_days override
│   ├── models/
│   │   ├── __init__.py
│   │   ├── city.py                  # City: holds all districts, buildings, global metrics
│   │   ├── district.py              # District: local metrics, building list, stressor state
│   │   ├── building.py              # Building: status, dependencies, detection state
│   │   ├── event.py                 # Active event: source threat, affected buildings, timeline
│   │   └── metric.py                # Metric value with history (for post-game timeline)
│   └── gui/
│       ├── __init__.py
│       ├── app.py                   # Main window (CustomTkinter), grid layout, wires settings popup
│       ├── map_canvas.py            # Map image + district tint overlays + building lamps
│       ├── dashboard.py             # Right panel: global metrics, district summary, active events; gear button
│       ├── news_ticker.py           # Scrolling headline feed; clickable headlines open story popup
│       ├── popups.py                # Hover info, click menus (remedy selection), story popup, intro screen
│       ├── settings_popup.py        # CTkToplevel settings panel: game duration, event frequency, discovery speed, cascade risk
│       ├── theme.py                 # Centralized colour palette, font loading (IM Fell English)
│       ├── time_controls.py         # Pause/play/speed buttons + game clock; active state shown by colour
│       └── postgame.py              # End-of-term reflection screen
│
├── static/
│   ├── fonts/                       # Bundled IM Fell English font files
│   └── images/
│       └── ankh-morpork.png         # Base map image
│
├── tests/
│   ├── test_engine/
│   │   ├── test_simulation.py
│   │   ├── test_metrics.py
│   │   ├── test_dependencies.py
│   │   ├── test_events.py
│   │   ├── test_detection.py
│   │   └── test_remedies.py
│   └── test_config/
│       └── test_loader.py
│
├── pyproject.toml
└── docs/
```

## How the YAML configs work

One file per district so The Shades can be tweaked without touching Nap Hill:

```yaml
# config/districts/the_shades.yml
id: the_shades
name: "The Shades"
wealth: 10          # 0-100
density: 300        # people/acre
infrastructure_quality: 3.0   # failure probability modifier (1.0 = baseline, 3.0 = 3x as likely)
political_influence: 0.2
media_attention_multiplier: 0.2
local_trust: 15

discovery_time_hours: [72, 120]   # base range for non-catastrophic events

stressors:
  underinvestment: extreme
  social_inequality: victim       # string label; used as trust-damage multiplier key
  organisational_fragmentation: high
  just_in_time: amplifier

narrative_hooks:
  - "Fire in the Shades spreads for hours before Watch notices"
  - "Shades residents block entrance demanding clean water"
```

Building instances reference types and districts:

```yaml
# config/buildings/instances.yml
- id: mended_drum
  name: "The Mended Drum"
  type: tavern              # references _types.yml
  district: small_gods
  position: [620, 300]      # map canvas coordinates
  dependencies:
    critical: [brewery_supply, water]
    operational: [energy, thieves_guild]
    strategic: [transport]
  narrative_hooks:
    - "Mended Drum loses its licence after a riot"
    - "Mended Drum brawl spills into street, breaks new fountain"
```

Event templates define what can happen and when:

```yaml
# config/threats/events.yml
- id: pump_failure_shades
  name: "Communal pump failure"
  category: degradation_and_neglect
  target_districts: [the_shades, cockbill_street]
  target_building_types: [slum_dwelling]
  probability_base: 0.02          # per tick, before multipliers
  stressor_amplifiers:
    underinvestment: 2.0
  impact:
    immediate:
      - {metric: local_trust, delta: -5, scope: district}
    secondary:
      delay_hours: 48
      effects:
        - {metric: public_trust, delta: -3, scope: global}
  headlines:
    - "Communal pump runs dry in {district}"
  stories:
    - "Residents of {district} have been without clean water for {duration}. No official response has been recorded."
```

## Engine design

The simulation runs on a tick-based loop (1 tick = 1 game-hour, 24 ticks/day, configurable via `config/game.yml`). Each tick:

1. Clock advances game time
2. Event generator rolls against probabilities (weighted by stressors, neglect, infrastructure quality, and `event_rate_multiplier`)
3. Detection checks if hidden failures become visible (`discovery_time_hours` cached on first check, scaled by `discovery_speed_multiplier`)
4. Dependency resolver propagates cascading effects (throttled to once per day per event; scaled by `cascade_multiplier`)
5. Remedy completion checker resolves events whose remedy duration has elapsed (tracked via `remedy_applied_tick`)
6. Metrics engine applies all pending effects (immediate, delayed, duration-based, passive dynamics)
7. Narrative engine generates headlines from templates for any new visible events
8. End condition checker evaluates loss/completion thresholds (respects `game_duration_days` override)

The engine is completely decoupled from the GUI. It exposes a simple interface:

```
class Simulation:
    def tick(self) -> TickResult         # advance one step, return structured result
    def pause(self) / resume(self)
    def set_speed(self, multiplier)
    def apply_remedy(self, event_id, remedy_id) -> RemedyResult
    def ...
```

`TickResult` bundles all tick outputs: new events, detected events, cascade events, completed remedy events, headlines, 
metric changes, and end condition results.

This means the engine is testable without a GUI, and we could later swap CustomTkinter for a web frontend without 
touching game logic.

## Key engine mechanics

### GameSettings

`GameSettings` is a dataclass held on `GameConfig` in `loader.py`. Its four fields are applied as multipliers in engine subsystems:

| Field                        | Applied in        | Effect                                                   |
|------------------------------|-------------------|----------------------------------------------------------|
| `event_rate_multiplier`      | `events.py`       | Scales every event's base probability                    |
| `discovery_speed_multiplier` | `detection.py`    | Scales `discovery_time_hours` (lower = faster discovery) |
| `cascade_multiplier`         | `dependencies.py` | Scales cascade propagation probability                   |
| `game_duration_days`         | `end_check.py`    | Overrides YAML `days_elapsed` when > 0                   |

Settings are exposed via the GUI settings popup (gear button in dashboard title bar).

### Social inequality trust damage multiplier

District trust damage is amplified or softened based on the district's `social_inequality` stressor label and the 
city's global `social_inequality` level:

| Label         | Formula                       | Effect at global level 0.7           |
|---------------|-------------------------------|--------------------------------------|
| `victim`      | `1.0 + level × 0.8`           | +56% trust damage (Shades, Cockbill) |
| `moderate`    | `1.0 + level × 0.3`           | +21% trust damage (Small Gods)       |
| `beneficiary` | `max(0.3, 1.0 − level × 0.4)` | −28% trust damage (Nap Hill)         |

Only negative trust deltas are modified. Positive effects (recovery) are not scaled.

### Passive metric dynamics

Each day the engine applies background drift independent of individual events:

- Regulatory pressure rises with unresolved detected or responding events; falls after a quiet week
- Political stability falls when trust drops below 25; recovers slowly after an incident-free week
- Legitimacy recovers 0.5 points per month when stability stays above 50
- Crime level rises when Watch coverage falls below 50%; suppressed slowly when above 80%

### Income calculation

Monthly income is applied to budget and scales dynamically:

- Guild fees: floored at 50%, scaled by fraction of operational guild buildings
- Trade tariffs: reduced 30% per failed transport or food-supply building
- Taxes: penalised when public trust drops below threshold (default 30)

## Why this structure

| Concern                                       | Solution                                         |
|-----------------------------------------------|--------------------------------------------------|
| "I want to tweak Nap Hill's media multiplier" | Edit `config/districts/nap_hill.yml`             |
| "I want to add a new building"                | Add an entry to `config/buildings/instances.yml` |
| "I want a new threat event"                   | Add to `config/threats/events.yml`               |
| "I want to change how trust decays"           | Edit `config/metrics/global.yml`                 |
| "I want to rebalance remedy costs"            | Edit `config/remedies.yml`                       |
| "I want to playtest with one district"        | Point `game.yml` at a single district file       |
| "I want to test the engine without a GUI"     | Run tests against `Simulation` directly          |

## Dependencies

Minimal:

- `customtkinter` + `Pillow`: GUI
- `pyyaml`: config loading
- Python dataclasses: typed models
- `pytest`: testing
