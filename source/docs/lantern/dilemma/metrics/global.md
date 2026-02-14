# City-wide metrics

## Public trust

What it represents: The population's confidence that the Patrician and the guild system will maintain order, provide essential services, and keep the city functioning. Not affection - Vetinari doesn't need to be loved - but a pragmatic acceptance that things work.

Starting value: "Business as usual" - the baseline after centuries of pragmatic tyranny. The city functions; people grumble but go about their business. The Patrician has arranged things so that removing him would cause chaos, which people trust him to prevent.

Decay behaviours:

| Incident Type                                  | Trust Impact       | Mechanism                                                                                                          |
|------------------------------------------------|--------------------|--------------------------------------------------------------------------------------------------------------------|
| Combined utility outage (power + water)        | Severe             | People can tolerate one thing failing. Two at once feels like the city is collapsing.                              |
| Guild strike or internal war                   | Critical           | The entire social contract depends on guilds regulating themselves. If they fight, the system fails.               |
| Watch failure (crime wave, delayed response)   | Moderate to Severe | Depends on district. Nap Hill trust crashes fast; Shades trust had nowhere to fall.                                |
| Single utility failure (water but power works) | Mild               | People complain; trust erodes slowly.                                                                              |
| Transport failure (bridge closed)              | Moderate           | Commuters notice; economic impacts compound.                                                                       |
| Symbolic failure (museum theft, theatre fire)  | Mild               | Cultural institutions failing signals decay, but doesn't threaten survival.                                        |
| Narrative amplification                        | Multiplier         | A failure that becomes a story (drinking water brown, river on fire) damages trust 2-3x more than a quiet failure. |

Recovery behaviours:

| Remedy                 | Trust Recovery Rate        | Mechanism                                                                                                        |
|------------------------|----------------------------|------------------------------------------------------------------------------------------------------------------|
| Technical restoration  | Fast initial, then plateau | "They fixed it" generates immediate relief, but lingering suspicion remains.                                     |
| Resilience investment  | Slow but permanent         | Announcing upgrades rebuilds trust gradually; visible improvements (new pipes) accelerate it.                    |
| Compensatory measures  | Moderate, temporary        | Free beer or tax breaks buy goodwill, but expire. If root cause persists, trust falls back.                      |
| Accountability actions | Variable                   | Scapegoating works short-term; genuine reform works long-term. Wrong target (blaming someone popular) backfires. |
| Time alone             | Very slow                  | If nothing else happens, trust slowly regenerates as people forget. Months to years.                             |

Special cases:
- Vimes effect: If Vimes personally intervenes in a failure, trust recovers faster in the Shades and Cockbill Street, but may cause resentment elsewhere ("he cares more about them than us").
- Moist von Lipwig effect: If Moist is put in charge of fixing something, trust initially drops (con man!), then recovers dramatically if he succeeds.

## Budget (City Treasury)

What it represents: Not just gold in the vault, but the city's capacity to spend on repairs, compensation, and investment. Includes tax revenue, guild contributions, and emergency borrowing capacity.

Starting treasury: "Comfortable but not extravagant." Vetinari runs a tight ship; there's reserve for genuine emergencies, but not enough to fix everything at once. Major projects require guild loans.

Income sources per "turn" (say, monthly):

| Source                  | Contribution    | Reliability      | Notes                                                                       |
|-------------------------|-----------------|------------------|-----------------------------------------------------------------------------|
| Taxes (general)         | High            | Stable           | Based on economic activity; dips during disruptions.                        |
| Guild fees              | Moderate        | Very Stable      | Guilds pay for their charters; hard to increase quickly.                    |
| Trade tariffs           | Variable        | Unstable         | Depends on river traffic, road conditions, foreign relations.               |
| University contribution | Low             | Extremely Stable | UU pays a symbolic amount; trying to increase it is politically impossible. |
| Emergency borrowing     | High (one-time) | Available        | From guilds or wealthy families. Comes with political strings.              |

Expenditure costs (per remedy application):

| Remedy                 | Base Cost       | Cost Multipliers                                         | Notes                                                                                  |
|------------------------|-----------------|----------------------------------------------------------|----------------------------------------------------------------------------------------|
| Technical restoration  | Moderate        | District infrastructure quality (worse = more expensive) | Fixing a pump in Nap Hill is cheap; in the Shades, you're rebuilding the whole street. |
| Resilience investment  | High            | District wealth level (richer = more expensive upgrades) | Nap Hill demands brass pipes; Small Gods accepts clay.                                 |
| Compensatory measures  | Low to Moderate | Population affected                                      | Tax breaks cost future revenue; free beer costs now.                                   |
| Accountability actions | Low             | Political capital, not gold                              | Firing someone is cheap; hiring their replacement later is not.                        |

Special behaviours:
- Crisis spending: During a major incident, the Patrician can authorise emergency funds beyond normal budget, but this depletes reserves and may require guild approval.
- Guild loans: Available immediately, but the guild will expect favours later. Mr Boggis doesn't forget.
- Narrative effect on income: If trust drops below a threshold, tax collection becomes "difficult" (passive resistance, "mistakes" in accounting).

## Regulatory pressure

What it represents: The combined force of the guilds, the nobility, and the Patrician himself demanding action, compliance, or accountability. Not a measure of laws, but of *enforcement attention*.

Starting value: Moderate. The guilds regulate themselves; the Patrician regulates the guilds. A stable equilibrium of mutual suspicion.

What increases it:

| Trigger             | Pressure Increase | Mechanism                                                                         |
|---------------------|-------------------|-----------------------------------------------------------------------------------|
| Guild complaint     | Moderate          | A guild officially demands action. Downey (Assassins) complaining carries weight. |
| Noble outcry        | Moderate to High  | Lord Rust writing letters to the Patrician. Multiple nobles amplify.              |
| Watch request       | Low to Moderate   | Vimes asking for resources or authority. Usually granted.                         |
| Media campaign      | Moderate          | The *Ankh-Morpork Times* runs a series. Public opinion mobilizes guilds.          |
| Repeated failures   | Cumulative        | Same district, same problem, third time? Someone will answer for it.              |
| Election/transition | Spikes            | Any hint of leadership change makes everyone demand guarantees.                   |

What decreases it:

| Action                 | Pressure Decrease | Mechanism                                                            |
|------------------------|-------------------|----------------------------------------------------------------------|
| Accountability actions | Significant       | Someone was punished. The system worked. Move along.                 |
| Successful restoration | Moderate          | Problem solved. Next?                                                |
| Guild negotiation      | Moderate          | Private deals reduce public pressure. "We've handled it internally." |
| Time without incident  | Slow              | Pressure slowly dissipates if nothing new happens.                   |
| New crisis             | Shifts attention  | Old pressure forgotten; new pressure emerges elsewhere.              |

Thresholds for intervention:

| Pressure Level | Behaviour                                                                                                                    |
|----------------|------------------------------------------------------------------------------------------------------------------------------|
| Low            | Business as usual. Guilds self-regulate. Patrician observes.                                                                 |
| Moderate       | Patrician sends a polite inquiry. Guild heads receive dinner invitations.                                                    |
| High           | Patrician summons relevant parties. "Suggestions" become firm requests. Watch may be authorized to investigate.              |
| Critical       | Direct intervention. Guild charters reviewed. Nobles reminded of past assassinations. Moist von Lipwig assigned to "fix it." |
| Extreme        | Martial law? Unthinkable in Ankh-Morpork, but if guilds are at war and the river is on fire... Vimes gets emergency powers.  |

## Political stability

What it represents: The absence of coup, revolution, or civil war. Not the same as trust - a stable city can have grumpy citizens. Instability means factions are actively maneuvering against each other or the Patrician.

Starting value: High. Vetinari has arranged things beautifully. Everyone *could* overthrow him; no one can agree on who would replace him.

Relationship to other metrics:

| Metric              | Relationship to Stability                                                                                                                        |
|---------------------|--------------------------------------------------------------------------------------------------------------------------------------------------|
| Public trust        | Direct but not linear. Low trust creates instability *if* factions organize around it. High trust insulates against faction plotting.            |
| Inequality          | Direct. High inequality (Shades vs. Nap Hill) creates structural instability. Doesn't cause immediate crisis, but magnifies every other trigger. |
| Guild satisfaction  | Critical. If the major guilds are happy, stability is high. If two guilds are feuding, stability drops.                                          |
| Noble satisfaction  | Moderate. Nobles matter less than guilds, but they're louder.                                                                                    |
| Regulatory pressure | Inverse. High pressure means something is wrong; stability correlates negatively.                                                                |
| Succession clarity  | Implicit. Everyone knows Vetinari is mortal. No clear heir = underlying instability.                                                             |

What decreases stability:

| Trigger             | Impact           | Mechanism                                                                                  |
|---------------------|------------------|--------------------------------------------------------------------------------------------|
| Guild war           | Critical         | Thieves vs. Merchants? Assassins vs. Fools? City stops functioning.                        |
| Noble conspiracy    | High             | Letters, secret meetings, mercenary hiring. Usually detected early.                        |
| Food/water shortage | High             | Hungry people are unstable people.                                                         |
| Trust collapse      | Moderate to High | If trust falls far enough, someone will try to capitalize.                                 |
| Succession trigger  | Extreme          | Vetinari sneezes twice and the city holds its breath. If he actually dies? Chaos.          |
| External threat     | Paradoxical      | War usually *increases* stability (rally around the Patrician), unless the city is losing. |

What increases stability:

| Action                       | Impact      | Mechanism                                                |
|------------------------------|-------------|----------------------------------------------------------|
| Successful crisis management | Significant | Patrician looks competent; plotters pause.               |
| Guild concessions            | Moderate    | Keeping the guilds happy is job one.                     |
| Public works                 | Mild        | Visible investment makes people think the system works.  |
| Accountability actions       | Variable    | Scapegoating helps; genuine reform helps more.           |
| Time without crisis          | Slow        | Stability slowly accretes as people forget alternatives. |

"Election" thresholds: Ankh-Morpork doesn't have elections, but it has succession events:

| Condition                       | Succession Risk                                                           |
|---------------------------------|---------------------------------------------------------------------------|
| Vetinari healthy, guilds stable | Near zero                                                                 |
| Vetinari visibly ill            | Moderate. Nobles prepare. Guilds watch.                                   |
| Vetinari incapacitated          | High. Council of Guilds meets. Carrot's name mentioned. Nobles object.    |
| Vetinari dies                   | Critical. Succession crisis unless clear successor designated (he won't). |
| Vetinari resigns                | Never happening. He'd haunt the place.                                    |

Captain Carrot Ironfoundersson is the wildcard. He's the rightful heir to the throne, he's loved by the Watch, respected by dwarfs, and utterly uninterested in power. If stability collapses, his existence is both a threat (someone could use him) and a safety valve (he could unite factions if he chose). He won't choose. That's the tension.

## Legitimacy

What it represents: The moral and historical right to rule. Different from trust (pragmatic confidence). A leader can be trusted to run things competently but lack legitimacy (usurper). Or have legitimacy but squander trust (incompetent heir).

Starting value: High. Vetinari has ruled for decades, was "elected" by the guilds (however that works), and maintains order. No one questions his *right* to rule, only his decisions.

How it differs from trust:

| Dimension   | Trust                 | Legitimacy                             |
|-------------|-----------------------|----------------------------------------|
| Basis       | Performance           | Right/History/Tradition                |
| Changes     | Fast (incident today) | Slow (accumulated record)              |
| Restoration | Fix the problem       | Time, continuity, succession           |
| Loss        | Service failure       | Coup, assassination, charter violation |
| Measurement | "Are things working?" | "Should this person be in charge?"     |

What affects legitimacy:

| Action                         | Legitimacy Impact    | Mechanism                                                                                   |
|--------------------------------|----------------------|---------------------------------------------------------------------------------------------|
| Successful long rule           | Gradual increase     | Vetinari has been here forever; he *is* the city now.                                       |
| Guild endorsement              | Significant          | The guilds elected him; their continued support renews legitimacy.                          |
| Clear succession               | Establishes baseline | If Carrot took over, legitimacy starts high (rightful heir). If Moist took over... less so. |
| Coup attempt (failed)          | Increases            | Surviving a coup proves you're meant to be there.                                           |
| Coup attempt (successful)      | Resets to zero       | New ruler must build legitimacy from scratch.                                               |
| Mass protests                  | Decreases            | If people are in streets, your right to rule is questioned.                                 |
| Guild withdrawal of support    | Critical decrease    | If the guilds stop endorsing you, you're done.                                              |
| Assassination attempt (failed) | Paradoxical          | Depends on who tried. Assassins' Guild attempt? Bad. Random lunatic? Actually helps.        |
| Breaking charter               | Severe               | If Vetinari violated the terms of his own appointment, legitimacy collapses. He won't.      |

Recovery rate:

| Method               | Rate        | Mechanism                                                                     |
|----------------------|-------------|-------------------------------------------------------------------------------|
| Time                 | Very slow   | Generations. A usurper's descendants eventually become "the rightful rulers." |
| Military victory     | Moderate    | Winning a war (especially defensive) builds legitimacy fast.                  |
| Dynastic marriage    | Moderate    | Connecting to previous rulers.                                                |
| Guild re-endorsement | Significant | A formal vote of confidence resets legitimacy high.                           |
| Popular acclaim      | Variable    | Spontaneous "Long live the Patrician!" moments. Rare.                         |
| Carrot's endorsement | Extreme     | If the rightful heir publicly supports you, legitimacy becomes unassailable.  |

Special case - Carrot: If Carrot ever chose to press his claim, legitimacy would transfer instantly to him. Not because he'd be better (he might be), but because he's the *rightful* king. Vetinari knows this. Carrot knows this. Everyone knows this. Carrot's decision *not* to claim the throne is the only thing maintaining Vetinari's ultimate legitimacy. If Carrot ever changed his mind, the Patrician would step aside. Probably with a faint smile.

## Metric behaviours

| Metric              | Starting                        | Decay Drivers                                             | Recovery Drivers                     | Special Notes                                                    |
|---------------------|---------------------------------|-----------------------------------------------------------|--------------------------------------|------------------------------------------------------------------|
| Public Trust        | Moderate (pragmatic acceptance) | Service failures, guild conflict, narrative amplification | Fixes, compensation, accountability  | Vimes effect in poor districts; Moist effect on visible projects |
| Budget              | Comfortable reserves            | Spending, economic downturn                               | Taxes, guild loans, tariffs          | Guild loans come with political strings                          |
| Regulatory Pressure | Moderate equilibrium            | Guild complaints, noble outcry, media, repeated failures  | Accountability, fixes, negotiation   | Pressure shifts attention; new crisis replaces old               |
| Political Stability | High (Vetinari's masterpiece)   | Guild war, conspiracy, shortages, succession trigger      | Crisis management, concessions, time | Carrot is the ultimate safety valve and the ultimate threat      |
| Legitimacy          | High (historical right)         | Charter violation, coup, guild withdrawal                 | Time, victory, endorsement           | Carrot's endorsement = instant max                               |

This framework gives you everything needed to understand *how* the city responds to crises, without requiring numerical balance. The Patrician's decisions become meaningful trade-offs:

- Fix Nap Hill's water quickly (high political influence) or Small Gods' water (more people affected)?
- Use budget for technical fixes now, or resilience investment for later?
- Blame the Thieves' Guild (accountability) and risk their support, or compensate victims and hope the problem doesn't recur?
- How long before regulatory pressure from the merchants forces action?
- Is political stability strong enough to survive a week of river fires?
