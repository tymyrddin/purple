# District metrics

## Wealth Level

What it represents: The average economic status of residents and businesses in the district. Not just income, but assets, savings, and capacity to absorb shocks.

Starting values (as defined):

| District            | Wealth Level | Numerical Proxy |
|---------------------|--------------|-----------------|
| Nap Hill            | High         | 80-100          |
| University Precinct | High         | 75-95           |
| Merchant Quarter    | High         | 70-90           |
| Isle of Gods        | Medium       | 45-65           |
| Small Gods          | Low-Medium   | 30-50           |
| The Shades          | Very Low     | 5-20            |
| Cockbill Street     | Very Low     | 5-15            |

Behavioural mechanics:

| Aspect             | Behaviour                                                                                                                                   |
|--------------------|---------------------------------------------------------------------------------------------------------------------------------------------|
| Shock absorption   | High wealth districts can absorb 2-3 weeks of disruption before significant hardship. Low wealth districts feel impact within 2-3 days.     |
| Recovery capacity  | Wealthy residents can pay for private repairs, bypassing city systems. Poor residents have no alternatives.                                 |
| Tax contribution   | Direct correlation: wealthier districts contribute more to city budget, but also demand more services.                                      |
| Protest threshold  | Low wealth districts protest faster (hunger), but high wealth districts protest *louder* (newspapers, guild connections).                   |
| Migration pressure | If wealth gap widens significantly, poor districts see out-migration (those who can leave) or in-migration (those with nowhere else to go). |

Dynamic changes:

| Event                            | Wealth Impact                                 |
|----------------------------------|-----------------------------------------------|
| Prolonged service failure        | Decreases (businesses close, residents leave) |
| Successful resilience investment | Increases (area becomes more desirable)       |
| Crime wave                       | Decreases (businesses relocate)               |
| New transport link               | Increases (access improves commerce)          |
| Guild intervention               | Variable (depends on guild)                   |

## Population density

What it represents: Number of people per square acre. Affects how many are affected by any given failure, and how quickly problems spread.

Starting values:

| District            | Density                 | Numerical Proxy (people/acre) |
|---------------------|-------------------------|-------------------------------|
| Nap Hill            | Low                     | 20-40                         |
| University Precinct | Medium                  | 60-100                        |
| Merchant Quarter    | High (day), Low (night) | 200+ day, 30 night            |
| Isle of Gods        | Medium                  | 70-110                        |
| Small Gods          | High                    | 150-200                       |
| The Shades          | Very High               | 250-350                       |
| Cockbill Street     | Very High               | 300-400                       |

Behavioural mechanics:

| Aspect                      | Behaviour                                                                                                            |
|-----------------------------|----------------------------------------------------------------------------------------------------------------------|
| Impact multiplier           | Direct correlation: a water pump failure in the Shades affects 10x more people than the same failure in Nap Hill.    |
| Disease transmission        | High density = faster spread of illness (and rumors).                                                                |
| Protest formation           | High density = crowds assemble faster. Low density = protests require organization.                                  |
| Service delivery efficiency | High density = cheaper per capita to deliver services (one pump serves many), but catastrophic failure affects more. |
| Housing pressure            | High density = any housing loss (fire, collapse) displaces many.                                                     |

Dynamic changes:

| Event            | Density Impact                                                             |
|------------------|----------------------------------------------------------------------------|
| Housing collapse | Temporary decrease (displacement), then increase (remaining crowd tighter) |
| New construction | Increase (if housing) or decrease (if commercial displaces residents)      |
| Refugee influx   | Rapid increase (crisis event)                                              |
| Epidemic         | Temporary decrease (death, flight)                                         |
=
## Infrastructure quality

What it represents: The physical condition of roads, pipes, clacks towers, pumps, and buildings. Baseline probability of failure.

Starting values:

| District            | Infrastructure Quality | Failure Probability Modifier               |
|---------------------|------------------------|--------------------------------------------|
| Nap Hill            | High                   | 0.3x (failures 70% less likely)            |
| University Precinct | High                   | 0.4x (UU maintains its own)                |
| Merchant Quarter    | High                   | 0.4x (guilds maintain)                     |
| Isle of Gods        | Medium                 | 1.0x (baseline)                            |
| Small Gods          | Low-Medium             | 1.5x (50% more likely)                     |
| The Shades          | Very Low               | 3.0x (3x more likely)                      |
| Cockbill Street     | Very Low               | 3.5x (even worse)                          |
| River Ankh          | Very Low               | 4.0x (it's a river; it does what it wants) |

Behavioural mechanics:

| Aspect                           | Behaviour                                                                                                                                       |
|----------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------|
| Failure probability              | Base chance × quality modifier. A pump in Nap Hill rarely fails; a pump in the Shades fails constantly.                                         |
| Repair cost                      | Inverse relationship: poor quality districts cost *more* to fix because underlying systems are degraded. Fixing one pipe means replacing three. |
| Repair time                      | Same: poor quality = longer repairs (unexpected complications).                                                                                 |
| Detection time                   | Poor quality = failures noticed slower (fewer people report, harder to access).                                                                 |
| Cascading failure susceptibility | Poor quality = one failure triggers others (weak pipe bursts, weak road collapses).                                                             |

Dynamic changes:

| Event                   | Quality Impact                                                   |
|-------------------------|------------------------------------------------------------------|
| Resilience investment   | Significant increase (new infrastructure)                        |
| Technical restoration   | Temporary return to baseline, but underlying degradation remains |
| Neglect (no investment) | Slow decay over time (years)                                     |
| Catastrophic failure    | Sudden drop (bridge collapse, main burst)                        |
| Age                     | Very slow decay (decades)                                        |

## Political influence

What it represents: The district's ability to get the Patrician's attention. Not population, but *voice*. A function of wealth, guild presence, noble residents, and symbolic importance.

Starting values:

| District            | Political Influence | Attention Multiplier (from earlier)   |
|---------------------|---------------------|---------------------------------------|
| Nap Hill            | Very High           | 2.0x                                  |
| Merchant Quarter    | Very High           | 1.8x                                  |
| University Precinct | Very High           | 1.5x                                  |
| Palace (district)   | Absolute            | 3.0x (but not a residential district) |
| Isle of Gods        | Medium              | 0.8x                                  |
| Small Gods          | Low                 | 0.5x                                  |
| Cockbill Street     | Low (Vimes proxy)   | 0.1x (spikes with Vimes)              |
| The Shades          | Negligible          | 0.2x                                  |

Behavioural mechanics:

| Aspect                       | Behaviour                                                                                                                      |
|------------------------------|--------------------------------------------------------------------------------------------------------------------------------|
| Complaint effectiveness      | High influence = one complaint triggers action. Low influence = hundreds of complaints ignored.                                |
| Media coverage               | Direct correlation: Nap Hill broken pipe = front page. Shades broken pipe = paragraph on page 12 (if that).                    |
| Resource allocation          | High influence districts get priority repairs, even if low influence districts need it more.                                   |
| Guild backing                | High influence districts have guild representatives who attend Council meetings.                                               |
| Vetinar's personal attention | Very high influence districts occasionally receive direct Patrician inquiries. "I hear Nap Hill is unhappy about the new tax." |

Dynamic changes:

| Event              | Influence Impact                                                         |
|--------------------|--------------------------------------------------------------------------|
| Noble moves in/out | Significant change (one family can shift Nap Hill's influence)           |
| Guild relocation   | Major shift (if Merchants' Guild moves, influence moves with them)       |
| Vimes visits       | Temporary spike for Cockbill Street (while he's there)                   |
| Major disaster     | Temporary increase (media attention, sympathy) - the "victim multiplier" |
| Decades of neglect | Slow decay (if ignored long enough, a district's influence atrophies)    |

Special case - Cockbill Street:

Cockbill Street has baseline negligible influence, but a standing "Vimes proxy" of 1.5x whenever Samuel Vimes is personally aware of an issue. If Vimes visits, the street briefly has Nap Hill-level attention. This creates interesting dynamics: nobles resent it ("why do *they* get priority?"), and Vimes must choose which battles to fight.

## Local Trust/Satisfaction

What it represents: District-level confidence in the city government. Can diverge significantly from global Public Trust. A district can be furious while the rest of the city is calm, or vice versa.

Starting values (baseline):

| District            | Starting Local Trust | Rationale                                         |
|---------------------|----------------------|---------------------------------------------------|
| Nap Hill            | Moderate-High        | Services work; they have alternatives anyway      |
| University Precinct | Moderate             | Wizards don't trust anyone, but UU insulates them |
| Merchant Quarter    | Moderate-High        | Guilds handle most problems; city is backup       |
| Isle of Gods        | Moderate             | Temples provide community support                 |
| Small Gods          | Low-Moderate         | Services patchy; residents expect little          |
| The Shades          | Very Low             | Services almost nonexistent; trust is for fools   |
| Cockbill Street     | Paradoxical          | Low trust in city, high trust in Vimes personally |

Behavioural mechanics:

| Aspect                  | Behaviour                                                                                                                                                                                    |
|-------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Decay rate per incident | Inverse to wealth: poor districts lose trust faster (less margin), but start lower so less to lose. Rich districts lose trust slower, but drop further when they do (expectations violated). |
| Recovery rate           | Direct correlation with remedy effectiveness in that specific district. A fix in the Shades matters more *there* than a fix in Nap Hill matters *there*.                                     |
| Inequality sensitivity  | If residents perceive they're treated worse than another district, local trust drops even if service is adequate. "Nap Hill got new pipes *again*?"                                          |
| Protest threshold       | When local trust drops below 20 (on 0-100 scale), protests become likely. Threshold lower in Shades (fatalistic), higher in Nap Hill (entitled).                                             |
| Crime correlation       | Low local trust = residents don't report crimes = more crime = lower trust. Vicious cycle.                                                                                                   |

Decay rates per incident type (district-specific):

| Incident Type          | Nap Hill | Small Gods | Shades | Mechanism                                 |
|------------------------|----------|------------|--------|-------------------------------------------|
| Water failure (1 day)  | -5       | -8         | -2     | Shades expected it; Nap Hill outraged     |
| Water failure (1 week) | -30      | -25        | -15    | Everyone angry, but Shades started lower  |
| Watch delay (burglary) | -15      | -5         | -1     | Shades never expected Watch anyway        |
| Bridge closed          | -8       | -15        | -20    | Shades workers can't get to jobs          |
| Guild strike           | -10      | -20        | -25    | Shades more dependent on informal economy |
| Symbolic failure       | -5       | -2         | -1     | Who cares about museum?                   |

Recovery rates per remedy (district-specific):

| Remedy                 | Nap Hill              | Small Gods        | Shades                   | Mechanism                                             |
|------------------------|-----------------------|-------------------|--------------------------|-------------------------------------------------------|
| Technical restoration  | +5/day (fast)         | +3/day (moderate) | +1/day (slow)            | "About time" vs. "Well, that's something"             |
| Resilience investment  | +2/week (sustained)   | +4/week (hopeful) | +6/week (transformative) | New pipes in Shades = miracle; in Nap Hill = expected |
| Compensatory measures  | +8 (one-time)         | +10 (one-time)    | +15 (one-time)           | Free beer in Shades = genuine celebration             |
| Accountability actions | +10 (if noble blamed) | +5 (general)      | +20 (if Vimes involved)  | Vimes appearance = max recovery in Shades             |
| Vimes visit            | -5 (resentment)       | +10 (hope)        | +30 (faith restored)     | Paradox: Nap Hill resents attention elsewhere         |

Special interactions:

- Vimes effect: When Vimes personally intervenes in a Shades or Cockbill Street failure, local trust recovers 2-3x faster than any other remedy. However, this *decreases* local trust in Nap Hill slightly (jealousy) and increases regulatory pressure globally (nobles complain about favoritism).
- Moist effect: When Moist von Lipwig is assigned to fix something, local trust initially drops 5-10 points ("a con man?"), then if he succeeds, recovers 15-20 points ("remarkable!").
- Guild intervention: If a guild fixes a problem in their district, trust in the *guild* increases, but trust in the *city* may not (residents credit the guild, not the Patrician).
- Contagion: Low trust in one district can spread to adjacent districts. Shades dissatisfaction seeps into Small Gods. Nap Hill smugness annoys everyone else.

## Summary Table - District Metrics Behaviour

| District            | Wealth   | Density    | Infrastructure | Influence         | Local Trust (Start)         | Special Characteristics                                                                   |
|---------------------|----------|------------|----------------|-------------------|-----------------------------|-------------------------------------------------------------------------------------------|
| Nap Hill            | High     | Low        | High           | Very High         | 75                          | Outraged by minor failures; recovers fast when fixed; resents attention to poor districts |
| University Precinct | High     | Medium     | High           | Very High         | 70                          | Insulated by UU; wizards don't care about city; but dependent on UU functioning           |
| Merchant Quarter    | High     | High (day) | High           | Very High         | 72                          | Business-focused; any disruption = lost income = rapid trust decay                        |
| Isle of Gods        | Medium   | Medium     | Medium         | Medium            | 60                          | Religious factions complicate response; river isolation magnifies transport failures      |
| Small Gods          | Low-Med  | High       | Low-Med        | Low               | 45                          | Forgotten middle; not rich enough to matter, not poor enough for Vimes                    |
| The Shades          | Very Low | Very High  | Very Low       | Negligible        | 15                          | Expected nothing; small improvements generate huge trust gains                            |
| Cockbill Street     | Very Low | Very High  | Very Low       | Low (Vimes proxy) | 20 (in city), 80 (in Vimes) | Proud; won't complain; Vimes is their real government                                     |
| River Ankh          | N/A      | N/A        | Very Low       | Medium            | N/A                         | No residents, but affects all districts; symbolic heart                                   |

## How District Metrics Interact with Global Metrics

| Global Metric       | District Interaction                                                                                                                                   |
|---------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------|
| Public Trust        | Weighted average of district trust, weighted by population and influence. A Nap Hill trust crash affects global trust more than a Shades crash.        |
| Budget              | District wealth affects tax contribution. District infrastructure quality affects repair costs.                                                        |
| Regulatory Pressure | District political influence determines how much a local failure increases global pressure. A Nap Hill complaint = high pressure. Shades = negligible. |
| Political Stability | Weighted by inequality. High inequality (Shades vs. Nap Hill) creates structural instability regardless of average trust.                              |
| Legitimacy          | Not directly district-affected, but if *all* districts lose trust simultaneously, legitimacy erodes.                                                   |

This district-level framework creates meaningful choices:

- Do you fix Nap Hill's water first (high political influence, low population) or Small Gods' (medium influence, high population)?
- Do you invest in Shades infrastructure (huge trust gains, cheap in absolute terms, but high regulatory pressure from nobles asking "why *there*?")?
- Do you send Vimes to Cockbill Street (massive local trust recovery, but Nap Hill resentment)?
- Do you let the Merchants fix their own problem (saves budget, increases guild power) or intervene directly (costs budget, maintains city control)?

The Patrician's art is balancing these pressures moment by moment, district by district, while never letting anyone see him sweat.

