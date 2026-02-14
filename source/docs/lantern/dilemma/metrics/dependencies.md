# Building dependencies

## Dependency types

What they represent: The web of relationships that keep a building functioning. A building isn't an island, it requires inputs from other buildings and services, and its outputs feed others.

Core dependency categories:

| Dependency Type | Examples                                                       | Failure Impact                    |
|-----------------|----------------------------------------------------------------|-----------------------------------|
| Utility         | Energy (clacks, lighting), Water (pumps, pipes), Waste removal | Immediate operational failure     |
| Supply chain    | Food deliveries, brewing ingredients, scroll paper             | Gradual depletion (days to weeks) |
| Service         | Watch protection, Guild regulation, Clerks' Guild records      | Slow degradation, then crisis     |
| Labour          | Workers commuting from other districts                         | Daily rhythm disrupted            |
| Security        | Thieves' Guild "quota" system, private guards                  | Theft increases, trust erodes     |
| Governance      | Guild charter, City license, Patrician's approval              | Legal existence threatened        |

Building-level dependency map:

```
[Utility Provider] → [Building] → [Output Recipients]
        ↑                  ↓              ↓
[Maintenance]        [Workers]      [Customers/Citizens]
        ↑                  ↑              ↓
   [Guild]           [Transport]    [Tax Revenue/City Budget]
```

## Building typology dependencies

## Guild HQs

*(Assassins' Guild, Thieves' Guild, Fools' Guild, Seamstresses' Guild)*

Consumes:
- Energy: High (lighting, heating vast halls, training facilities)
- Water: High (sanitation, kitchens, some guilds have peculiar cleaning needs)
- Communications: Critical (clacks, messengers, dead-letter drops)
- Security: Internal (own enforcers), but relies on Watch for external perimeter
- Labour: Apprentices, journeymen, masters (many commute from other districts)
- Supplies: Guild-specific (weapons, costumes, tools of the trade)

Produces:
- Tax revenue: To city (significant)
- Skilled labour: To economy
- Social order: By regulating their trade
- Business confidence: Stability signal
- Guild fees: Internal revenue
- Enforcement: "Justice" within their domain

Critical dependencies:

| Dependency        | Failure Consequence                                                                                 |
|-------------------|-----------------------------------------------------------------------------------------------------|
| Communications    | Can't coordinate with members; can't receive Patrician's inquiries; unlicensed practitioners emerge |
| Energy            | Can't heat training halls; apprentices idle; prestige damaged                                       |
| Water             | Sanitation fails; disease risk; minor inconvenience (guilds have resources to adapt)                |
| Watch cooperation | If Watch stops respecting guild boundaries, turf wars erupt                                         |

Cascading failure paths:
```
Guild HQ Comms Failure
    ↓
Can't coordinate with members
    ↓
Unlicensed practitioners operate unchecked
    ↓
Trade quality drops; public safety risk
    ↓
Public trust declines; regulatory pressure increases
    ↓
Patrician demands action; guild influence erodes
```

## Taverns and inns

*(The Mended Drum, Biers)*

Consumes:
- Energy: Moderate (lighting the sign, cellar, kitchen)
- Water: High (cleaning, brewing, diluting beer, allegedly)
- Communications: Gossip (lifeblood), clacks for suppliers
- Food & Beverage Supplies: Brewery (beer), farms (food), ice house (preservation)
- Labour: Barmen, bouncers, serving staff (local residents)
- Protection: Thieves' Guild quota (paid), Watch tolerance (cultivated)

Produces:
- Tax revenue: Alcohol tax, business tax
- Public morale: Social lubrication
- Social cohesion: Information exchange, deal-making
- Employment: Local jobs
- Noise: (externalised cost)

Critical dependencies:

| Dependency     | Failure Consequence                                                        |
|----------------|----------------------------------------------------------------------------|
| Brewery supply | No beer = no customers = closure within days                               |
| Water          | Can't clean glasses; can't brew; health hazard                             |
| Energy         | Dark, cold cellar; no atmosphere; customers go elsewhere                   |
| Thieves' Guild | If quota unpaid, "accidents" happen; if paid but Guild fails, protection无效 |

Cascading failure paths:
```
Brewery Failure (see example)
    ↓
Mended Drum beer supply stops
    ↓
Customers go to rival pubs
    ↓
Revenue drops; can't pay Thieves' Guild quota
    ↓
Guild enforcers visit; property damage
    ↓
Pub closes; unemployment; local morale drop
    ↓
Small Gods district trust declines
```

Special case: Biers: Biers has unusual dependencies. Its clientele (undead) are less sensitive to beer temperature, more sensitive to... existential ambiance. If the "right sort" can't find it, they simply don't come. Its dependency is reputation and discoverability rather than supply chains.

## Civic amenities

*(Dwarf Bread Museum, The Dysk theatre)*

Consumes:
- Energy: Moderate (lighting exhibits, heating)
- Water: Low (cleaning, cafe if present)
- Communications: Marketing, ticket sales, reviews
- Tourist traffic: Visitors from other districts/cities
- Curatorial expertise: Guild-trained curators
- Security: Theft prevention (valuable artefacts)

Produces:
- Cultural asset: Pride, identity
- Tourist revenue: Indirect (visitors spend elsewhere)
- Soft power: Ankh-Morpork as "civilized"
- Education: Historical/cultural knowledge

Critical dependencies:

| Dependency      | Failure Consequence                                                      |
|-----------------|--------------------------------------------------------------------------|
| Security        | Theft of Scone of Stone = cultural crisis, dwarf diaspora outrage        |
| Communications  | No ticket sales = no revenue; forgotten attraction                       |
| Tourist traffic | If transport fails, no visitors; cultural value unrealised               |
| Curators        | If Guild of Museum Curators (if it exists) strikes, exhibits deteriorate |

Cascading failure paths:
```
Dwarf Bread Museum Security Failure
    ↓
Scone of Stone stolen
    ↓
Dwarf community outrage; protests at Patrician's Palace
    ↓
Diplomatic incident with dwarf kingdoms
    ↓
Trade sanctions; economic impact
    ↓
Public trust declines; regulatory pressure spikes
    ↓
Watch resources diverted to investigation
    ↓
Other districts get less attention...
```

## Slum dwellings

*(The Shades, Cockbill Street)*

Consumes:
- Energy: Minimal (if they can afford candles, stolen clacks)
- Water: Communal pumps (critical)
- Waste removal: None (streets are the system)
- Shelter: Existing buildings (minimal maintenance)
- Community: Mutual aid (critical survival network)

Produces:
- Labour pool: Workers for city economy
- Local trust: Strong community bonds
- Crime: As economic alternative
- Pride: (Cockbill Street special)
- Rent: (to unseen landlords, often UU or guilds)

Critical dependencies:

| Dependency          | Failure Consequence                                       |
|---------------------|-----------------------------------------------------------|
| Communal water pump | No water = death within days; disease follows             |
| Community networks  | If community fragments, survival impossible               |
| Access to work      | If bridge closed, can't reach jobs; no income; starvation |
| Landlord tolerance  | If UU demands rent and residents can't pay, eviction      |

Cascading failure paths:
```
Communal Pump Failure (Shades)
    ↓
No local water source
    ↓
Residents must travel to Small Gods for water
    ↓
Small Gods resentment; inter-district tension
    ↓
Shades residents weakened; disease risk
    ↓
Watch ignores; no media coverage
    ↓
Weeks later: outbreak, death, Vimes discovers
    ↓
Vimes intervention; political crisis; nobles complain about "favoritism"
    ↓
Global trust impact (delayed, severe)
```

Special case: Cockbill Street pride: Cockbill Street residents will not report failures. They'd rather suffer silently than admit need. This means detection time is maximum, decay is advanced before discovery, and recovery requires Vimes-level intervention.

## Middle-class and artisan housing

*(Isle of Gods, Small Gods residences)*

Consumes:
- Energy: Moderate (lighting, cooking, workshops)
- Water: Piped (if available) or local pumps
- Communications: News, guild newsletters
- Transport: Access to work, markets
- Schools: Dame schools, guild training for children
- Local shops: Daily supplies

Produces:
- Tax revenue: Property tax, income tax
- Social stability: The city's backbone
- Local businesses: Corner shops, bakeries
- Guild members: Future journeymen

Critical dependencies:

| Dependency  | Failure Consequence                                       |
|-------------|-----------------------------------------------------------|
| Transport   | Can't get to work = no income = can't pay rent = eviction |
| Local shops | If shops close, must travel further; time/cost increases  |
| Water       | Moderate impact (can afford to buy water temporarily)     |
| Energy      | Workshop closures; income loss                            |

Cascading failure paths:
```
Bridge Closure (Isle of Gods)
    ↓
Artisans can't reach Merchant Quarter workshops
    ↓
No income for days/weeks
    ↓
Can't pay local shopkeepers
    ↓
Shopkeepers can't pay suppliers
    ↓
Local economy collapse; multiple businesses fail
    ↓
Isle of Gods trust declines; regulatory pressure increases
    ↓
Temples complain to Patrician
    ↓
Political influence activates; repair prioritized
```

## Major civic institutions

*(Pseudopolis Yard, Post Office, Royal Mint)*

Consumes:
- Energy: High (24-hour operations)
- Water: High (cells need sanitation, kitchens)
- Communications: Critical (clacks, messengers)
- Transport: Paddy wagons, postal coaches, bullion wagons
- Staff: Trained personnel (many commute)
- Records: Paper, ink, filing systems

Produces:
- Public order: Watch presence
- Trust in government: Symbol of functioning state
- Economic enablers: Mail moves, currency exists
- Legitimacy: Visible governance

Critical dependencies:

| Dependency        | Failure Consequence                                               |
|-------------------|-------------------------------------------------------------------|
| Communications    | Watch can't coordinate; Post Office can't sort; Mint can't verify |
| Energy            | Cells dark; records unlit; night operations impossible            |
| Staff             | If transport fails, no night watch; no mail delivery              |
| Records integrity | If files destroyed, criminals released, debts forgotten           |

Cascading failure paths:
```
Pseudopolis Yard Communications Failure
    ↓
Watch patrols can't coordinate
    ↓
Crime wave (targeted, criminals know)
    ↓
Merchant Quarter hit hard; guilds furious
    ↓
Regulatory pressure spikes; Patrician demands action
    ↓
Budget diverted to temporary clacks tower
    ↓
Other infrastructure projects delayed
    ↓
Small Gods water pump upgrade postponed...
```

Special case: interconnected civic institutions:
The Post Office, Mint, and Watch are increasingly interdependent under Vetinari's reforms. A failure in one cascades to others:
- Post Office fails → Watch can't receive mail-in crime tips
- Mint fails → Watch can't pay salaries
- Watch fails → Post Office robbed, Mint vulnerable

## The Palace / Patrician's seat

Consumes:
- Energy: High (constant lighting, security systems)
- Water: High (kitchens, sanitation, gardens)
- Communications: Maximum (clacks, messengers, spies)
- Security: Elite guards (the only building with its own dedicated force)
- Information: From every district, guild, and foreign power
- Food: Exquisite, from across the Disc

Produces:
- Governance: Laws, decrees, judgments
- Stability: The centre holds
- Strategic direction: Long-term city planning
- Legitimacy: The Patrician's presence

Critical dependencies:

| Dependency     | Failure Consequence                                              |
|----------------|------------------------------------------------------------------|
| Communications | Vetinari blind; city drifts; factions maneuver                   |
| Security       | Assassination attempt (constant threat, but if actual breach...) |
| Information    | Bad decisions based on bad intel                                 |
| Loyalty        | If guards turn, game over                                        |

Cascading failure paths:
```
Palace Communications Intercepted (strategic interference)
    ↓
Vetinari receives false information about guild loyalty
    ↓
Makes decision based on bad intel (e.g., favors Thieves over Assassins)
    ↓
Assassins' Guild offended; withdraw support
    ↓
Regulatory pressure from offended guild; stability decreases
    ↓
Nobles sense weakness; conspiracy forms
    ↓
Political stability critical; city holds breath
    ↓
Vetinari discovers deception; massive accountability actions
    ↓
Trust recovers; but fragility exposed
```

## Unseen University (UU)

Consumes:
- Energy: Massive (magical research, heating, lighting)
- Water: High (wizards eat constantly, need sanitation)
- Communications: Gossip (vital), clacks for arcane supplies
- Rare & Arcane Supplies: Dragon's blood, octiron, etc.
- Food: Enormous quantities (wizard appetites)
- Silence: (for research, rarely achieved)

Produces:
- Magical knowledge: Theoretical and practical
- High-status graduates: For guilds, government
- Occasional crises: Reality fluctuations, monster summons
- Employment: Servants, groundskeepers, suppliers
- Consumption economy: Local merchants thrive on UU gold

Critical dependencies:

| Dependency           | Failure Consequence                                     |
|----------------------|---------------------------------------------------------|
| Arcane supplies      | No dragon's blood = research stops; experiments fail    |
| Food                 | Wizards get *hangry*. This is a documented catastrophe. |
| Internal cooperation | If faculty feuds, magic leaks; city at risk             |
| Patrician tolerance  | If relationship sours, UU privileges threatened         |

Cascading failure paths:
```
Arcane Supply Chain Failure
    ↓
UU can't replenish critical components
    ↓
Wizard experiment destabilizes; containment fails
    ↓
Magical leak affects surrounding district
    ↓
Three-day rain of frogs on Merchant Quarter
    ↓
Business disrupted; guilds furious
    ↓
Patrician demands UU "handle it"
    ↓
Archchancellor apologizes; pays compensation
    ↓
Budget hit; regulatory pressure on UU increases
    ↓
UU becomes slightly more cooperative (for a while)
```

Special case: UU as landlord: UU owns much of the Shades. If UU experiences financial pressure (rare), it might 
demand rent increases from the poorest residents. This creates a dependency chain:

```
UU budget pressure → Rent increases → Shades evictions → Homelessness → Crime increase → Watch pressure → City budget pressure
```

## Cascading failure paths

Cross-district examples.

## Example: Water cascade

```
Small Gods Pump Failure (Infrastructure Quality: Low)
    ↓
Small Gods residents without water (Day 1-2)
    ↓
Residents travel to Shades pumps (straining their capacity)
    ↓
Shades pumps fail from overuse (Infrastructure Quality: Very Low)
    ↓
Shades residents without water; disease risk (Day 3-4)
    ↓
Shades residents desperate; travel to Isle of Gods
    ↓
Isle of Gods residents resent intrusion; tensions rise
    ↓
Isle of Gods local trust declines; temples complain
    ↓
Regulatory pressure increases; Watch deployed to manage crowds
    ↓
Watch resources diverted from Merchant Quarter
    ↓
Merchant Quarter crime increases (Thieves' Guild "testing" boundaries)
    ↓
Merchants furious; guild pressure on Patrician
    ↓
Patrician orders emergency water carts to Shades AND Small Gods
    ↓
Budget spent; Nap Hill complains about "waste on those people"
    ↓
Global trust: Small Gods (+), Shades (+), Nap Hill (-), Isle of Gods (-)
    ↓
Net effect: Complicated
```

## Example: Transport cascade

```
Isle of Gods Bridge Structural Failure (Degradation & Neglect)
    ↓
Isle of Gods residents trapped; can't reach jobs (Day 1)
    ↓
Merchant Quarter businesses short-staffed
    ↓
Merchant Quarter productivity drops; tax revenue dips
    ↓
City budget pressure (minor) (Week 1-2)
    ↓
Isle of Gods residents desperate; use boats (unsafe)
    ↓
Boating accident; deaths; media coverage (Week 2-3)
    ↓
Public trust declines; regulatory pressure spikes
    ↓
Patrician orders emergency bridge repair (expensive)
    ↓
Budget diverted from Shades infrastructure upgrade
    ↓
Shades residents bitter (promised upgrade delayed)
    ↓
Shades local trust declines; crime increases
    ↓
Watch stretched thin; Nap Hill burglary goes uninvestigated
    ↓
Nap Hill furious; noble complaints
    ↓
Regulatory pressure remains high; political stability trembles
    ↓
Patrician reflects: "One bridge..."
```

## Example: Communications cascade

*Strategic interference*

```
Clacks Tower in Small Gods "mysteriously" fails (repeated small outages)
    ↓
Small Gods businesses can't coordinate with Merchant Quarter suppliers
    ↓
Supply chain delays; just-in-time failures (Day 1-3)
    ↓
Merchant Quarter shops run out of popular items
    ↓
Customer frustration; merchants blame "system"
    ↓
Guild of Merchants demands investigation (Day 4-5)
    ↓
Watch investigates; finds "no clear cause" (sabotage well-disguised)
    ↓
Merchants unsatisfied; regulatory pressure increases
    ↓
Second tower fails; pattern emerges (Day 7)
    ↓
Vetinari suspects strategic interference; deploys personal agents
    ↓
Meanwhile, Small Gods trust declines (city can't protect infrastructure)
    ↓
Small Gods residents grumble; some stop paying "voluntary" taxes
    ↓
City budget pressure (minor); Watch morale drops (overworked)
    ↓
Three weeks later: culprit identified (foreign agent, rival city)
    ↓
Accountability actions (executions, diplomatic protest)
    ↓
Trust slowly recovers; resilience investment (new towers) announced
    ↓
But damage done: fragility exposed
```

## Dependency strength ratings

Not all dependencies are equal. Some are critical (failure = immediate shutdown), others are operational (failure = degraded function), others are strategic (failure = long-term decline).

| Building Type     | Critical Dependencies    | Operational Dependencies | Strategic Dependencies |
|-------------------|--------------------------|--------------------------|------------------------|
| Guild HQ          | Communications           | Energy, Water            | Watch cooperation      |
| Tavern            | Brewery supply, Water    | Energy, Thieves' Guild   | Transport (staff)      |
| Civic Amenity     | Security                 | Communications, Energy   | Tourist traffic        |
| Slum Dwelling     | Water pump               | Community networks       | Landlord tolerance     |
| Artisan Housing   | Transport                | Local shops, Energy      | Schools                |
| Civic Institution | Communications, Energy   | Staff, Records           | Public trust           |
| Palace            | Communications, Security | Information, Loyalty     | (none: it's the top)  |
| Unseen University | Arcane supplies, Food    | Internal cooperation     | Patrician tolerance    |

## Detection time modifiers by building type

How quickly a failure is noticed depends on building type and district:

| Building Type     | Base Detection Time | District Modifier              | Notes                                    |
|-------------------|---------------------|--------------------------------|------------------------------------------|
| Guild HQ          | Immediate (hours)   | None (guilds self-report)      | They tell the Patrician before he asks   |
| Tavern            | Fast (same day)     | x1.0                           | Customers notice immediately             |
| Civic Amenity     | Moderate (1-3 days) | District influence             | Museum theft might take days to discover |
| Slum Dwelling     | Slow (3-7 days)     | x2.0 (Shades), x3.0 (Cockbill) | No one reports; must be discovered       |
| Artisan Housing   | Moderate (1-2 days) | x1.2 (Isle of Gods isolation)  | Neighbors notice, but may not report     |
| Civic Institution | Fast (same day)     | None (staff present)           | Shift change reveals problems            |
| Palace            | Immediate           | None                           | Vetinari knows everything                |
| Unseen University | Variable            | None                           | They may not *tell* anyone               |

This building dependency framework creates the final layer of decision pressure:

- A broken pump in the Shades isn't just a pump, it's a cascade that will eventually reach Nap Hill through crime, disease, or Vimes's conscience.
- A brewery failure isn't just about beer, it's about tavern closures, unemployment, local trust decay, and eventually merchant pressure.
- A clacks tower failure might be accident, neglect, or strategic interference, and guessing wrong has consequences.

The Patrician must see the whole web, not just the broken thread.
