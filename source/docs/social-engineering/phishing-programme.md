# Building a phishing programme that actually works

The redesign of a phishing simulation programme follows the Satir arc described elsewhere in these foundations.
This page covers what each phase looks like in practice, and what a programme built on genuine attacker
techniques requires to operate.

## Purple team sessions as the foundation

Before monthly simulations make sense, people need context for what they are being tested on. Purple team
sessions, run roughly every six months, or when onboarding new cohorts, provide that context through
direct experience rather than instruction.

Half the room plays attacker, half plays defender. Both sides operate simultaneously: simulated campaigns go
out, real-time dashboards are watched, detection and reporting and response are practised. Then the sides
switch. People have experience of what a convincing phishing campaign looks like from the inside before they
are asked to recognise one from the outside.

The difference in engagement between "come and role-play a hacker" and "come and learn defence" is not a
small one. Experience of the attacker's perspective is what makes the defender's instincts accurate rather
than pattern-matched to last year's templates.

These sessions build the foundation for the recurring monthly simulations. Without them, the simulations
produce data without context. With them, the data lands in an environment where people know what it means.

## Monthly simulations: applying the skills

After staff have been through purple team training, monthly phishing simulations deploy current attack
techniques against the live production environment. Staff know a test is coming (it is announced) but not
the timing or the specific method.

Importantly, email filters remain fully operational. If a simulated email is blocked, that is data, not a
failure. Either the technique needs updating to reflect current evasion tactics, or the filter is doing its
job and that vector is already well defended. Both outcomes are useful.

Tools such as Gophish manage campaign delivery. Templates are built from current threat intelligence rather
than a static library: what is actively being used against organisations like yours, now. Public sources
suffice if curated carefully: vendor threat reports, incident diaries, sandbox submissions, sector-specific
advisories. A brief introduction at each session explains the origin of the technique, why it is effective, and
why it is harder to detect than last year's examples. Context improves retention.

The monthly runs measure clicks, credential submissions, report rates, and defender catch rates. They measure
both the effectiveness of controls and staff response behaviour, and they reinforce the lessons from the purple
team sessions rather than operating in isolation from them.

## What current techniques look like

QR codes embedded in PDFs bypass URL scanning that operates on text. Credential harvesting pages hosted on
legitimate Microsoft or Google infrastructure blend into domains that browser security indicators treat as
trusted. Adversary-in-the-middle proxies sit between the target and the legitimate service, capturing session
tokens after MFA has completed. At which point the second factor has already served its purpose and the
session is live.

Using these techniques in simulations is not cruelty. It is the minimum required to prepare people for what
is actually arriving. A simulation that avoids techniques because they are too effective at achieving delivery
is not testing the organisation. It is demonstrating what the organisation would prefer to believe about
itself.

## The transition period

When a programme moves from vendor-template simulations to current-technique simulations, the metrics will
get worse before they get better. Click rates rise. Credential submissions appear. The SOC receives more
noise. Reporting pipelines get tested by volume they were not handling before and sometimes break.

This is the chaos phase of the transition. The correct response is to frame it accurately: these metrics show
that the programme is now measuring something real. The previous numbers were a record of how well people
could recognise phishing that no longer gets used. These numbers are a record of where the gaps actually are.

Fixing systems is the work. Blaming users is available as an alternative but produces only a more anxious
version of the same vulnerability. The people who submitted credentials to a realistic AiTM proxy were not
careless. They were operating in a system that had not given them the tools to identify that specific technique.
Giving them those tools, through the purple team sessions, through context at each monthly run, is what
changes the outcome.

## The new status quo

In organisations that run programmes like this, security becomes a background habit. People report suspicious
emails without prompting and discuss phishing attempts in normal team meetings. Participants who have played
attacker often become the most reliable reporters, having seen exactly how convincing a real email can be.

The programme's value compounds when integrated with broader security operations: reported simulations flow
through the same triage process as real incidents, credential submission patterns inform access decisions, and
detection gaps become tuning cases rather than abstract concerns.

This is no longer a training programme measured by a click-rate chart. It is a continuous, live test of the
organisation as a system, detection, reporting, response, and adaptation all running together.

## Related

- [The Satir Change Model](../foundations/organisational-development/satir-change-model.md)
- [The Satir Change Model in practice](../foundations/change-management/satir-change-model.md)
- [Why simulations fail](why-simulations-fail.md)
- [Phishing-resistant controls](https://blue.tymyrddin.dev/docs/purple/begin/human/phishing-resistant.html)
- [Attack simulation runbooks](https://blue.tymyrddin.dev/docs/ngo/awareness/attack-simulation)