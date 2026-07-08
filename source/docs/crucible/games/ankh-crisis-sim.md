# Lord Vetinari's Dilemma

![Ankh Morpork feedback loops](/_static/images/ankh-morpork-sim.png)

[Lord Vetinari's Dilemma](https://github.com/tymyrddin/ankh-crisis-sim) puts a player in charge of
Ankh-Morpork and its interconnected infrastructure, energy, water, communications, transport, and asks them
to keep the city standing through a run of disruptions with no clean answers. It is a governance game, not a
technical one: it models what happens when systems fail, degrade, or are disrupted, without a single protocol
or exploit on screen.

The rules are the city's own. Each building or district is a concentration of services and dependencies, so an
incident in one place surfaces as a consequence somewhere else and several moves later: service availability
drops, economic output falls, public sentiment turns, institutional trust erodes, regulatory scrutiny climbs.
A player responds by allocating scarce resources and choosing which trade-off to accept between short-term
stability and long-term resilience, under time pressure and a budget that runs out.

## Playing it

Requires Python 3.12, a virtual environment, and `pip install -e ".[dev]"`. `python -m src.main` opens a brief
introduction, and pressing Start enters the city: a map of building lamps (green, yellow, amber, red), a
metrics dashboard (trust, budget, regulatory pressure, political stability, legitimacy, public health, crime),
a news ticker, and time controls, starting paused. Clicking a building with an active event offers a remedy,
and the remedies offered are filtered to those the threat model permits for that domain, so the choice is
constrained the way a real one would be. There is no leaderboard and no victory screen.

## What it is for

It is built for the people who make the trade-offs and rarely see the cascade: executives, boards, policy
makers, regulators, and mixed technical and non-technical groups in the same room. The fictional city lets
them speak openly about failure and pressure without pointing at a real location, and recognise the pattern
without the defensive reaction the real one would trigger. The game ends the way the job does, with no victory
screen: "You served your term. Here is what happened."

That is incident response one level up from the console: the same fail-safely rehearsal the
[incident-response](../../incident-response/index.rst) exercises run for responders, played instead by the
people who set the budget and carry the consequences.

*Last updated: 2 July 2026*
