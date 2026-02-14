# Detection mechanisms & discovery times

The city's sensory apparatus: how failures are noticed, who reports them, and how long it takes for information to 
reach decision-makers. A failure noticed immediately can be fixed before trust decays significantly. A failure 
discovered after a week may have already triggered cascades.

## Detection mechanisms by type

| Mechanism              | Description                                                | Reliability                            | Speed                | Districts Present                     |
|------------------------|------------------------------------------------------------|----------------------------------------|----------------------|---------------------------------------|
| Guild self-reporting   | Guilds inform the Patrician of issues in their domain      | High (they want protection)            | Fast (hours)         | Merchant Quarter, Guild HQ areas      |
| Watch patrol           | Officers notice failures on beat                           | Moderate (depends on patrol frequency) | Variable             | All, but frequency varies by district |
| Citizen complaint      | Residents report via messengers, clacks, or personal visit | Low in poor districts, High in rich    | Slow to Moderate     | Nap Hill (fast), Shades (none)        |
| Media investigation    | *Ankh-Morpork Times* reporters discover stories            | Moderate (they look for news)          | Moderate to Fast     | High-influence districts prioritized  |
| Tax shortfall          | Budget office notices reduced revenue                      | High (numbers don't lie)               | Slow (weeks)         | All (economic indicator)              |
| Vimes intuition        | Commander Vimes "has a feeling"                            | Paradoxically high                     | Variable             | Anywhere he's paying attention        |
| Spontaneous event      | Explosion, fire, collapse - hard to miss                   | 100%                                   | Immediate            | Any                                   |
| Strategic intelligence | Vetinari's personal network                                | Very High                              | Fast                 | All (but limited capacity)            |
| No detection           | Failure continues until cascade forces discovery           | N/A                                    | Potentially infinite | Shades, Cockbill Street               |

## Discovery time base values by district

How long before *someone* in authority notices a non-catastrophic failure (e.g., a broken pump, not an explosion):

| District            | Base Discovery Time                                   | Modifiers                                             | Rationale                                         |
|---------------------|-------------------------------------------------------|-------------------------------------------------------|---------------------------------------------------|
| Nap Hill            | 4-8 hours                                             | Noble complaint accelerates to 1-2 hours              | Residents expect service and complain immediately |
| Merchant Quarter    | 2-6 hours                                             | Business hours matter; night failures slower          | Lost revenue focuses attention                    |
| University Precinct | 6-12 hours                                            | Wizards may not notice or care                        | Insulated, self-contained                         |
| Isle of Gods        | 12-24 hours                                           | Temple networks help, but isolation hurts             | Community notices, but may handle internally      |
| Small Gods          | 24-48 hours                                           | No single voice; gradual complaints                   | Residents grumble but assume no one cares         |
| The Shades          | 72-120 hours (3-5 days)                               | No reporting; must be discovered by patrol or cascade | Residents expect nothing                          |
| Cockbill Street     | 120+ hours (5+ days, possibly never)                  | Pride prevents reporting; active concealment          | "We don't need help"                              |
| River Ankh          | Immediate if visible (fire, flood), otherwise ignored | Visual events only                                    | Out of sight, out of mind                         |

## Discovery time by building type

Buildings themselves within a district affect discovery speed:

| Building Type     | Discovery Time Modifier                | Mechanism                        |
|-------------------|----------------------------------------|----------------------------------|
| Guild HQ          | 0.5x (half the district time)          | Self-reporting                   |
| Tavern            | 0.8x                                   | Customers notice and talk        |
| Civic Amenity     | 1.5x                                   | May be visited infrequently      |
| Slum Dwelling     | 2.0x (Shades), 3.0x (Cockbill)         | No reporting; active concealment |
| Artisan Housing   | 1.0x (baseline)                        | Neighbors notice                 |
| Civic Institution | 0.3x (fastest)                         | Staff present 24/7               |
| Palace            | 0.1x (effectively immediate)           | Vetinari                         |
| Unseen University | 2.0x (if internal), 1.0x (if external) | They may not tell anyone         |

Example calculation:
- Small Gods base: 24-48 hours
- Small Gods tavern failure: 24-48 × 0.8 = 19-38 hours
- Small Gods slum failure: 24-48 × 1.5 (Slum) = 36-72 hours (no, wait, Slums aren't in Small Gods - let's do Shades instead)
- Shades base: 72-120 hours
- Shades slum failure: 72-120 × 2.0 = 144-240 hours (6-10 days)

## Detection mechanism effectiveness by district

Which mechanisms actually work in each district:

| District            | Guild Report        | Watch Patrol       | Citizen Complaint | Media             | Vimes               | Strategic |
|---------------------|---------------------|--------------------|-------------------|-------------------|---------------------|-----------|
| Nap Hill            | High (nobles)       | High               | Very High         | Very High         | Low (rarely visits) | High      |
| Merchant Quarter    | Very High           | High               | High              | High              | Low                 | High      |
| University Precinct | Low (UU internal)   | Moderate           | Low               | Moderate          | Very Low            | Moderate  |
| Isle of Gods        | Moderate (temples)  | Moderate           | Moderate          | Low               | Low                 | Low       |
| Small Gods          | Low (minor guilds)  | Moderate           | Low               | Low               | Low                 | Low       |
| The Shades          | None                | Low (infrequent)   | None              | None              | High (when focused) | Low       |
| Cockbill Street     | None                | Very Low           | None (pride)      | None              | Very High           | Low       |
| River Ankh          | None (barge guild?) | Low (river patrol) | Low (boatmen)     | High (if visible) | Low                 | Low       |

## Discovery time by incident type

Some failures announce themselves; others hide:

| Incident Type           | Base Discovery Time                              | Mechanism                                    |
|-------------------------|--------------------------------------------------|----------------------------------------------|
| Explosion/collapse      | Immediate                                        | Everyone notices                             |
| Fire                    | Immediate (if visible), 1-2 hours (if interior)  | Smoke, alarm                                 |
| Water pump failure      | District-dependent (above)                       | Gradual; noticed when people can't get water |
| Clacks tower failure    | 4-8 hours                                        | Users notice, report                         |
| Bridge structural issue | 12-24 hours (cracks), Immediate (collapse)       | Gradual vs. catastrophic                     |
| Crime wave              | 24-72 hours                                      | Pattern emerges slowly                       |
| Guild dispute           | Immediate (they tell you) or hidden (they don't) | Political                                    |
| Supply chain disruption | 3-7 days                                         | Shortages appear gradually                   |
| Disease outbreak        | 7-14 days                                        | Symptoms appear, then spread                 |
| Strategic interference  | Possibly never                                   | Designed to be undetectable                  |

## The "Vimes Effect" on discovery

When Samuel Vimes is personally focused on an area, discovery time collapses:

| District            | Normal Discovery | With Vimes Attention                 |
|---------------------|------------------|--------------------------------------|
| Nap Hill            | 4-8 hours        | 2-4 hours (he's efficient)           |
| Merchant Quarter    | 2-6 hours        | 1-3 hours                            |
| University Precinct | 6-12 hours       | 4-8 hours (he intimidates wizards)   |
| Isle of Gods        | 12-24 hours      | 6-12 hours                           |
| Small Gods          | 24-48 hours      | 8-16 hours                           |
| The Shades          | 72-120 hours     | 4-8 hours (he walks the beat)        |
| Cockbill Street     | 120+ hours       | 2-4 hours (they tell him everything) |

Mechanism: Vimes walks, talks to people, and has a network of informants (and former street urchins) who trust him. In the Shades, he's the only authority figure who isn't a threat.

Cost: Every hour Vimes spends in one district is an hour not spent in another. His attention is a scarce resource.

## The "Moist Effect" on discovery

When Moist von Lipwig is assigned to fix something, discovery *accelerates* because he's looking, but initial reports may be unreliable:

| Phase          | Discovery Speed | Reliability                |
|----------------|-----------------|----------------------------|
| First 24 hours | Very Fast       | Low (he's guessing)        |
| Days 2-3       | Fast            | Improving                  |
| Day 4+         | Very Fast       | High (he's figured it out) |

Mechanism: Moist talks to everyone, charms information out of people, and isn't afraid to ask stupid questions. He also cuts corners, so initial assessments may miss underlying issues.

## Discovery time cascades

A failure discovered late has already caused damage:

```
Day 1: Pump fails in Cockbill Street (no report)
Day 2: Residents carry water from Small Gods (resentment builds)
Day 3: Small Gods pump strained (but not failing yet)
Day 4: Shades residents notice Cockbill Street neighbors using "their" pumps
Day 5: Inter-district tension; minor fights
Day 6: Cockbill Street elder finally walks to Pseudopolis Yard (6 hours)
Day 7: Vimes learns of problem; visits immediately
Day 8: Pump repaired

Trust impact by day of discovery:
- If discovered Day 2: -5 trust (Cockbill), 0 elsewhere
- If discovered Day 7: -20 trust (Cockbill), -5 (Small Gods, Shades), inter-district tension penalties
- Repair cost: Same (pump fixed), but relationship repair needed
```

## Strategic detection

Lord Vetinari doesn't rely on official channels. His personal detection mechanisms include:

| Mechanism                     | Coverage                | Reliability    | Discovery Time          |
|-------------------------------|-------------------------|----------------|-------------------------|
| Palace clerks                 | All written reports     | High           | Daily summary           |
| Personal spies                | Key individuals, guilds | Very High      | Hours to days           |
| Assassins' Guild intelligence | They share selectively  | Variable       | Depends on relationship |
| Dinner invitations            | Nobles talk             | Moderate       | Weekly                  |
| Reading between lines         | All communications      | Extremely High | Immediate (to him)      |
| The "Vetinari pause"          | He already knew         | 100%           | Before you did          |

Mechanism: Vetinari has arranged information flows so that he receives multiple independent reports on any significant matter. Discrepancies between reports tell him as much as the reports themselves.

## Detection difficulty by district

| District            | Easy to Detect                      | Hard to Detect                               | Effectively Invisible    |
|---------------------|-------------------------------------|----------------------------------------------|--------------------------|
| Nap Hill            | Water failure, crime, transport     | Internal noble conspiracies                  | -                        |
| Merchant Quarter    | Business disruption, guild disputes | Quiet criminal coordination                  | -                        |
| University Precinct | Explosions, visible magic           | Internal faculty politics                    | Most things (they hide)  |
| Isle of Gods        | Bridge issues, temple disputes      | Gradual infrastructure decay                 | -                        |
| Small Gods          | Catastrophic failures               | Slow degradation, minor crimes               | Most routine failures    |
| The Shades          | Fires, collapses, visible deaths    | Pump failures, disease onset, crime patterns | Everything until cascade |
| Cockbill Street     | (Nothing without Vimes)             | Everything                                   | All failures concealed   |
| River Ankh          | Fires, floods, visible pollution    | Gradual siltation, contamination             | Baseline condition       |

## Discovery time as a strategic variable

The Patrician can invest in improving detection:

| Investment                   | Cost                      | Effect                                     | Districts Affected                     |
|------------------------------|---------------------------|--------------------------------------------|----------------------------------------|
| More Watch patrols           | Budget (ongoing)          | Discovery time -25%                        | All, but especially Shades, Small Gods |
| Citizen reporting incentives | Budget (small)            | Complaint frequency +50%                   | Medium-influence districts             |
| Clacks redundancy            | High (capital)            | Communications failure detection immediate | All with clacks                        |
| Guild liaison officers       | Political                 | Guild reporting improves                   | Guild districts                        |
| Vimes overtime               | Vimes exhaustion          | His attention spreads thinner              | One district at a time                 |
| River monitors               | Moderate                  | River issues detected faster               | River Ankh                             |
| Shades outreach              | Political (nobles object) | Discovery time in Shades -50%              | Shades, Cockbill Street                |

## Detection metrics framework

| Metric                            | Behaviour                                                  |
|-----------------------------------|------------------------------------------------------------|
| Base discovery time               | Function of district (wealth, influence) and building type |
| Detection mechanism effectiveness | Different mechanisms work in different districts           |
| Vimes effect                      | His attention collapses discovery time in poor districts   |
| Moist effect                      | Fast discovery, initially unreliable                       |
| Vetinari effect                   | He already knows (narrative convenience)                   |
| Investment options                | Budget can improve detection, but trade-offs exist         |
| Cascade penalty                   | Late discovery = more trust damage, harder recovery        |
