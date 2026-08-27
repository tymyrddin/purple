# Russia's useful blur

*Russia, and an ecosystem the state need not own*

The tidy version of Russian cyber power comes as an organisation chart. On one side the state units:
[Sandworm](https://attack.mitre.org/groups/G0034/) and [Fancy Bear](https://attack.mitre.org/groups/G0007/), both
tracked to the GRU, the military intelligence directorate. On the other the criminal syndicates: Conti,
[Evil Corp](https://attack.mitre.org/groups/G0119/), REvil, LockBit, ransomware operations, several renting out
extortion for a cut. Two columns, a line between them, espionage and sabotage filed under the first, profit under the
second.

The line is drawn for convenience and does not hold. The Russian case is not a closed revenue loop but a
gradient: directed state operation at one end, tolerated criminal enterprise at the other, and in between a range of
relationships that resist a clean name. Even calling it a gradient flatters it, because a gradient is a single axis, and
the tie between the Russian state and a given operator runs along several at once: command, protection from prosecution,
intelligence cooperation, patriotic alignment, provision of infrastructure, financial benefit, the freedom to refuse. An
actor is less a point on a line than a different reading on each of those dials.

So the organisation chart is not false because the real chart is a spectrum. It is false because there is no single
organisational relation to chart. What the case turns on is not which column an actor belongs in, nor even where on the
line it sits, but what the blur permits, and how unevenly the evidence lets anyone fix the relationship at all.

![A spectrum of Russian cyber actors from state command on the left to criminal autonomy on the right, with three regions beneath it: directed state operation, tasked criminal capability, tolerated free agent. Each actor is drawn as a range on the spectrum rather than a point, the width of the range showing how unevenly the evidence locates it. Sandworm and Fancy Bear sit hard against the state end in narrow bands. Evil Corp spans a wide band across the middle, sitting in neither column. Conti, REvil and LockBit spread toward the criminal end, with Conti reaching back toward the middle where the leaked logs show intelligence interest. The bands overlap and no line divides the spectrum, which is the boundary not holding.](/_static/images/boundary-gradient-diagram.svg)

## An option, not a payroll

The substrate is a large population of skilled operators and a criminal economy the state neither suppresses nor fully
employs. What the state supplies is not wages but jurisdiction: freedom from prosecution, protection from extradition,
local hosting, local laundering, access to Russian-speaking criminal markets and to malware talent, and a climate in
which robbing foreign adversaries carries little social cost. Crime is permitted to run, and capability follows from the
permission rather than from command.

The economics of that are the point. A state cyber unit carries salary, recruitment, training, command and attribution
costs. A criminal ecosystem carries those costs itself, and the state acquires, in effect, an option over the resulting
capability, exercisable when convenient and disownable otherwise. The state inherits a criminal market already built and
draws on it selectively, an arrangement cheaper than a payroll and deniable in a way a payroll never is.

The discipline that keeps the arrangement liveable is visible in the code. Ransomware built in this environment
routinely [checks the system language or keyboard layout](https://www.threatdown.com/blog/ransomwares-russia-problem/)
and exits without encrypting if it finds itself on a machine in Russia or the wider Commonwealth of Independent States.
The convention is not uniform, and the motive may be as much about avoiding local law enforcement as about any explicit
protection, but read at the level of the ecosystem it is territorial discipline written into the malware. The payload
pauses to ask whether the target is one of ours, and proceeds only on the answer. The domestic boundary is reproduced in
the first few lines of the attack.

What can be said with more confidence sits at the level of tolerance. The US Treasury has described Russia as
a [haven for ransomware actors, enabling them to operate openly](https://home.treasury.gov/news/press-releases/jy1486),
and separately as
having [enabled ransomware by cultivating and co-opting criminal hackers](https://home.treasury.gov/news/press-releases/jy2114)
while continuing to offer safe harbour. One sanctioned operator, Mikhail Matveev, put the bargain in his own words in
public interviews cited by Treasury: his activity would be tolerated by local authorities as long as he stayed loyal to
Russia. The Canadian Centre for Cyber Security goes further, assessing that Russian intelligence and law
enforcement [almost certainly maintain relationships with cybercriminals](https://www.cyber.gc.ca/en/guidance/baseline-cyber-threat-assessment-cybercrime)
and let them operate with near impunity, in a relationship that runs both ways, the state tasking criminals and on
occasion running ransomware itself. A 2025 SWP analysis frames the bargain plainly: criminals
are [left free to operate provided they avoid Russian targets](https://www.swp-berlin.org/10.18449/2025C30/) and
occasionally take on a task the state assigns, which is part of why only about 3.6 per cent of Russia-origin incidents point
inward.

## Sabotage on the calendar

At the directed end of the gradient the relationship is legible, and the signature is sabotage that tracks the
geopolitical calendar. Sandworm, tied to the GRU, took down parts of the Ukrainian power grid in December 2015 and again
in 2016, the first publicly acknowledged blackouts caused by cyberattack, and returned in April 2022 with
[an Industroyer variant](https://www.welivesecurity.com/2022/04/12/industroyer2-industroyer-reloaded/) in an ultimately
thwarted attempt against high-voltage substations as the invasion got under way. In 2017 the same group released
NotPetya through the hijacked update mechanism of a Ukrainian tax-accounting package, a wiper wearing the costume of
ransomware: it displayed a ransom note but was built without any means of decrypting what it destroyed. It spread past
its Ukrainian target across the world and did damage later estimated in the billions. US prosecutors
[charged six GRU officers of Unit 74455](https://www.justice.gov/archives/opa/pr/six-russian-gru-officers-charged-connection-worldwide-deployment-destructive-malware-and)
with the grid attacks, NotPetya, a hack-and-leak operation against a French presidential campaign, and the Olympic
Destroyer attack on the 2018 Winter Games, describing nearly a billion dollars in losses to three identified NotPetya
victims alone. None of these operations was primarily a revenue operation. Each is state capability expressed through
cyber means, and each belongs to the one end of the range where nobody has to ask who gave the order.

## Evil Corp, both at once

If Sandworm marks the end where the relationship is legible, Evil Corp marks the place where it stops being separable at
all. The group behind the Dridex banking trojan and a succession of ransomware strains is as commercial as cybercrime
gets, charged with theft of
[more than a hundred million dollars across dozens of countries](https://home.treasury.gov/news/press-releases/sm845).
It is also tasked. A 2024 tri-lateral action with the United Kingdom and Australia
[sanctioned its leader, Maksim Yakubets, alongside his father-in-law, Eduard Benderskiy](https://www.themoscowtimes.com/2024/10/02/russias-evil-corp-hackers-unmasked-by-sweeping-sanctions-a86542),
a former security-services officer described as orchestrating the group's relationship with the Russian state and
shielding it after the 2019 sanctions. The UK's National Crime Agency went further still, describing the group as
[tasked to strike NATO targets and protected from prosecution](https://www.nationalcrimeagency.gov.uk/who-we-are/publications/732-evil-corp-behind-the-screens)
through that same family tie.

None of these descriptions supersedes another. There is no moment at which the criminal enterprise becomes a state
instrument. Criminal profit, state protection, intelligence tasking and a family network inside the FSB occupy the same
organisation at the same time. Evil Corp is best read as an investigative label for a shifting set of people rather than
a stable firm, but across the changes the pattern holds: it does not sit in either column, because the columns name
relations it holds at once. It is the gradient collapsed into a single address.

## Alignment is not command

Evil Corp shows relations coexisting. Conti shows how easily they are confused. When a pro-Ukraine
insider [leaked Conti's internal chat logs](https://therecord.media/conti-ransomware-gang-chats-leaked-by-pro-ukraine-member)
in early 2022, days after the group publicly pledged support to the invasion, the archive read in two registers at once.
Much of it is an ordinary software firm: development sprints, trouble encrypting large files, attempts to obtain demos
of endpoint-detection products in order to test evasion, the complaints any payroll produces. Alongside that,
researchers
found [references to FSB interest](https://www.rapid7.com/blog/post/2022/03/01/conti-ransomware-group-internal-chats-leaked-over-russia-ukraine-conflict/)
in material the group could reach, including the investigative outlet Bellingcat's files on Alexei Navalny.

The archive documents a criminal organisation behaving like a business, and an apparent intelligence interest in what it
could collect. It does not document a chain of command. Pro-Russian is not state-directed. State contact is not state
command. State protection is not state ownership. Public support for the invasion is an ideological alignment, a
different proposition from taking instructions from a service.

There is a second finding in the mundanity. A firm that has already solved recruitment, development, testing, affiliate
management, victim negotiation, infrastructure, payment and operational security is a large stock of capability
assembled without any state having to build a bureaucracy. The state does not need to stand up a cybercriminal
organisation of its own. One already exists, and it can be reached.

## Enforcement on a switch

The strongest evidence against all of this is the state acting against the crime. When Russia
[arrested alleged REvil members](https://krebsonsecurity.com/2022/03/conti-ransomware-group-diaries-part-i-evasion/) in
January 2022, announcing it as a response to a US request, that is Moscow policing the ecosystem it is said to tolerate,
and taken at face value it cuts the other way. What weakens it as a counter-example is not that the arrests secretly
served toleration, but that they did not hold: they coincided with a narrow diplomatic opening,
[eight of the fourteen were tried](https://therecord.media/four-revil-ransomware-gang-members-sentenced-prison-russia),
on card-fraud and malware charges rather than ransomware, and the activity resumed regardless.

Taken less as a verdict than as a demonstration, the episode says something the toleration story on its own does not.
The question is not whether Russia arrests ransomware operators, since it plainly sometimes does. It is what decides
when the boundary suddenly becomes enforceable, and the answer looks contingent: an opening, a signal, a use. The
arrests show that the state can switch the relationship from tolerance to enforcement when it chooses, and for as long
as enforcement does not hold, that capacity reads as part of the substrate; ransomware prosecutions that held, or
extraditions, would count against the reading. An ecosystem that knows it can be reached behaves differently from one
that believes itself autonomous. The absence of enforcement is not the whole mechanism. The credible possibility of it
is.

## Blur in the plumbing

The blur runs between people. It also runs between services. The machinery an operation needs, hosting,
malware, laundering, initial access, is itself a market, and the state's relationship to each layer varies as much as
its relationship to any crew.

In 2025 the United States, the United Kingdom and Australia jointly sanctioned
[Media Land, a Russia-based bulletproof-hosting provider](https://www.afp.gov.au/news-centre/media-release/afp-supports-government-sanctions-two-dark-web-services-and-their),
describing infrastructure sold precisely to evade detection and law enforcement and to keep ransomware online, with a
sister company and associated personnel named alongside. In July 2026 a joint EU-UK cyber sanctions package
[reached across the same terrain](https://www.consilium.europa.eu/en/press/press-releases/2026/07/13/russian-cyber-attacks-and-destabilising-activities-council-sanctions-nine-individuals-and-four-entities/),
designating nine individuals and four entities that included Media Land and its owner, actors tied to the LummaC2,
Trickbot and Conti malware families, and a pro-Russia hacktivist group, described collectively as enabling ransomware,
phishing and attacks on critical infrastructure.

A hosting company does not have to become an intelligence service to become useful to one. The point of the sanctions
record is that the boundary does not sit only between a government hacker and a criminal hacker. It runs through the
stack: a state unit, a criminal group, a hosting provider, a malware developer, a launderer, an access broker, an
affiliate, each with a different and rarely documented relationship to the state. The useful ambiguity is not only
between people. It is between services.

## No orders necessary

The most consequential relationship in the ecosystem may be the one that needs no instruction at all. A 2025 study by
Karen Nershi in the [Journal of Cybersecurity](https://doi.org/10.1093/cybsec/tyaf037), working from 4,194 ransomware
victims and more than 60,000 messages leaked from the Conti group, found Russia-based ransomware activity tracking
Russian state interests: heavier targeting of companies that pulled out of Russia after the 2022 invasion, and raised
activity around Western elections. Alignment, and not necessarily tasking.

That gap is the space between Conti and Evil Corp, and it holds a mode of its own. An operator does not have to receive
an order naming a target. It can read the weather. Russia is at war with the West; Western firms have taken positions
against Russia; attacking them pays; the authorities are unlikely to mind. Behaviour that serves the state's interest
follows without the state having said a word. A state does not have to command an ecosystem that has learned its
preferences.

The patriotic proxy is the clearest species of this. The EU's 2026 package named Z-Pentest, a pro-Russia hacktivist
group, which targets critical infrastructure in the energy and water sectors and hit a Danish water utility in December
2024. Such groups are not criminal for profit, and not conventional state units either. They are aligned, and alignment
is enough. It is also a reminder that the ecosystem is not only ransomware. Disruption and signalling are their own line
of work.

## The footprint in layers

Laid out as layers rather than actors, the ecosystem takes a rough shape, though the layers are relationships and not
boxes, and the same person sometimes sits in several at once.

| Layer                 | Function                                   | Relationship to the state |
|-----------------------|--------------------------------------------|---------------------------|
| GRU and FSB units     | espionage, sabotage, influence             | direct                    |
| Evil Corp type actors | crime plus intelligence tasking            | demonstrated cooperation  |
| Conti type actors     | crime plus political alignment and contact | ambiguous                 |
| ransomware crews      | extortion                                  | tolerated                 |
| hacktivist groups     | disruption and signalling                  | aligned, proxy            |
| bulletproof hosts     | infrastructure                             | enabling                  |
| malware developers    | technical capability                       | commercial, overlapping   |
| launderers            | conversion and concealment                 | criminal infrastructure   |
| access brokers        | initial access                             | criminal market           |
| domestic enforcement  | selective suppression                      | control over the boundary |

The last row is the one easiest to leave out, and it does the most work. The state's ability to arrest, release, ignore,
threaten or recruit is not outside the ecosystem. It is the part that holds the rest in place.

## The blur is the point

Across the gradient, the operational signature is not any single technique. It is the utility of the boundary
staying blurred. Sabotage that can be disowned, crime that can be leaned on, enforcement that can be performed or
suspended: each depends on the state's relationship to the operator remaining unfixed. The same substrate that lets a
criminal crew run for profit lets it be reached when convenient, and the Evil Corp record shows the same relationships
that protected a criminal group also enabling the tasking of it. Whether all of this amounts to a deliberately designed
architecture, or an accreted set of conveniences that happen to compose one, is a further claim the evidence does not
settle.

Underneath the signature is a plainer fact. Russia does not need to own the capability to have access to it. The Conti
archive is the exhibit, in the way a leaked contractor's paperwork tends to be. The picture it paints is mundane:
extortion at scale is produced by something structured like an ordinary company, embedded in an economy that permits it,
at points apparently useful to a service it is not formally part of. The drama is in the effects. The production is
clerical.

![A diagram of effects for the Russian state's relationship to cybercrime, drawn as one reinforcing loop with a single branch. State toleration sustains the criminal ecosystem, the ecosystem supplies deniable capability, the capability proves useful to the state, and that usefulness is why the state keeps tolerating and cultivating it. The four edges run in the same direction, so the loop is reinforcing, marked R and read clockwise. Drawn in grey, meaning a sourced effect on a branch with no evidenced return: enforcement, the switch the state can throw and rarely does, which lowered the ecosystem briefly with the 2022 REvil arrests and did not hold. An increase in state toleration raises the criminal ecosystem. An increase in the criminal ecosystem raises deniable capability. An increase in deniable capability raises usefulness to the state, by human intervention. An increase in usefulness to the state raises state toleration, by human intervention. An increase in enforcement lowers the criminal ecosystem, by human intervention.](/_static/images/boundary-loops-diagram.svg)

Seen as effects, the blur is not inertia but a loop that pays to keep. Toleration feeds the ecosystem, the ecosystem
yields deniable capability, the capability proves useful, and that usefulness is why the toleration continues: one
reinforcing loop, marked R. Enforcement hangs off it in grey, the switch the state can throw and, on the 2022 evidence,
rarely makes hold on the ransomware itself. It is not a revenue loop but a loop that keeps the boundary open, and it
says nothing about whether any single crew took an order.

## Tasking, never quite proven

The edge that resists closure is tasking. It is one thing to show that an operator caused an effect, which indictments,
malware analysis and leaked logs can often establish. It is another to show the relationship under which the effect was
produced: instructed, encouraged, tolerated, or merely aligned. The evidence separates these unevenly. The Treasury and
NCA accounts of Evil Corp assert direct tasking. The Conti logs suggest contact and interest rather than a chain of
command. Nershi's correlations show alignment without an order. The CIS-exclusion convention demonstrates a shared
understanding, not an instruction. Collapsing all of these into "state-sponsored" flattens exactly the distinction the
gradient is made of: demonstrated instruction and permitted freedom are not the same relationship, even when both point
the same way.

How these actors get named is the same boundary in another guise, and the naming has begun to move. The vocabulary of
attribution used to compress varied relationships into a binary, state-sponsored or criminal, and the personified threat
actor, the advanced persistent threat with a number and a nickname, invited the picture of a single directed hand. The
official language has quietly abandoned the chart. The UK described the 2026 sanctions as targeting both Russian state
actors and criminal proxies operating in support of Russian objectives, and the EU Council filed all thirteen
designations under "Russia's cyber ecosystem".

The porousness of the boundary between Russian state operations and Russian crime is easy to read as weakness, a state
that cannot control its own underworld. It reads closer to the opposite. A boundary held firmly would make the
relationship easy to classify, producing a capability that is clearly the state's or a crime that is clearly not. A
boundary left porous lets capability, criminality and state interest overlap without having to become the same
organisation, each able to borrow the other's cover. The blur may not be a failure to draw the line. It may be what the
line is for.

The Russian system works because the state leaves the loop open. A fully state-owned criminal apparatus would be
expensive, attributable and slow. A genuinely independent one would drift, and in time turn inconvenient or hostile. The
useful zone lies between, where capability, criminality and state interest overlap without ever quite becoming the same
thing. A criminal ecosystem became an extension of Russia's options, a boundary kept open rather than a capability
owned.
