# North Korea's fiscal policy

*North Korea, and the treasury turned inside out*

The standard account of North Korean hacking arrives as a roster. [Lazarus
Group](https://attack.mitre.org/groups/G0032/), [APT38](https://attack.mitre.org/groups/G0082/), [Bureau
121](https://plausibledenial.org/north-korea/rgb-bureau-121), a drift of aliases behind them (BlueNoroff,
[Andariel](https://attack.mitre.org/groups/G0138/), [Kimsuky](https://attack.mitre.org/groups/G0094/)), and a highlight
reel to match: Sony in 2014, the Bangladesh central bank in 2016, [WannaCry in
2017](https://attack.mitre.org/software/S0366/), a long run of exchange thefts, and the [Bybit heist of February
2025](https://www.fbi.gov/investigate/cyber/alerts/2025/north-korea-responsible-for-1-5-billion-bybit-hack), attributed
by the FBI to North Korean actors and the largest cryptocurrency theft on record. The roster names capabilities and pins
incidents to a flag. It treats the money as motive, and having named the motive, it stops.

What needs explaining is not the roster but the revenue system it serves. The groups are one instrument inside a
larger apparatus: a set of externally facing extraction mechanisms that turn the world outside the border into a source
of hard currency. Cyber operations are the digital component of that apparatus, and the unusually scalable one, since a
stolen wallet crosses no frontier and needs no ship. That scalability is why they draw the eye. They are not the whole
machine.

What sets the case apart is degree rather than kind. Other states host, tolerate, or direct financially motivated
operations. What is unusual about Pyongyang is not that it steals for the state but that the whole chain is unusually
legible: state institutions, operational units, revenue-generating activity, laundering and weapons programmes are
joined in the public record, by indictment, sanctions notice and monitoring report, to a degree few other states allow.
Legibility, not monopoly, is the distinctive feature, and it is what lets a loop be drawn at all.

## A loop that closes

The condition can be described, the behaviour can be described, but the return path, the line showing that the behaviour
feeds back into the condition that produced it, tends to resist sourcing. The North Korean case is unusual in that the
loop closes.

Sanctions imposed over the nuclear and ballistic-missile programmes constrict the state's access to foreign currency and
to ordinary international finance. Cyber operations offer one route back to it; arms sales, exported labour and commodity
trades offer others, and the macro logic does not depend on which instrument fills it. The proceeds help sustain the
regime and, on the available evidence, help fund the weapons programme, whose continuation is what the sanctions answer.
Revenue in, survival out, and back again, at least in outline.

The return edge is the part that can be cited rather than asserted, and cyber is the instrument for which it can be
cited at all, at the level of aggregate state finance rather than individual stolen dollars. The [UN Panel of
Experts](https://digitallibrary.un.org/record/4041323/files/S_2024_215-EN.pdf), the body that monitored sanctions
compliance until its mandate lapsed in 2024, described cyber-threat actors subordinate to the Reconnaissance General
Bureau, naming Kimsuky, Lazarus, Andariel and BlueNoroff, and set out their key tasks as obtaining information of value
and illicitly generating revenue for the country. Member-state reporting to the Panel put figures in the open: one
government's assessment held that malicious cyber activity generated roughly half of the country's foreign-currency
income, another that around 40% of the weapons-of-mass-destruction programmes were funded by illicit cyber means. These
are assessments reported by the Panel, not numbers it independently derived, and the loop they let one close is a loop
of aggregate funding rather than a traceable transaction-level circuit. Held at that level, it holds.

![A reinforcing loop in the finance of the North Korean state. Sanctions cut the state's access to foreign currency, cyber operations restore it, the revenue funds the weapons programme, and the programme's continuation is what draws the sanctions, closing the circuit. Marked R, one reinforcing loop, held at the level of aggregate state finance rather than traceable transactions. Drawn in grey, meaning a sourced effect on a branch with no evidenced return into the loop: self-reliance policy (juche), and the supply of trained operators. An increase in sanctions on the DPRK lowers access to foreign currency. An increase in access to foreign currency lowers illicit cyber revenue operations, by human intervention. An increase in illicit cyber revenue operations raises state hard-currency income. An increase in state hard-currency income raises the nuclear and missile programme. An increase in the nuclear and missile programme raises sanctions on the DPRK, by human intervention. An increase in self-reliance policy (juche) lowers access to foreign currency, by human intervention. An increase in the supply of trained operators raises illicit cyber revenue operations, by human intervention.](/_static/images/treasury-loops-diagram.svg)

## Four thefts, one treasury

As a signature, the operational history maps, item by item, onto a state that needs hard currency and cannot
readily come by it through ordinary trade.

One of the first major financial operations to become publicly visible was the Bangladesh Bank heist. In February 2016
operators later attributed to Lazarus manipulated the SWIFT terminals
at [Bangladesh Bank](https://www.justice.gov/usao-cdca/pr/north-korean-regime-backed-programmer-charged-conspiracy-conduct-multiple-cyberattacks)
and issued fraudulent payment instructions against its account at the Federal Reserve Bank of New York. The US complaint
describes an attempt reaching towards a billion dollars, of which about 81 million left the system; in
the [familiar account of the incident](https://nsarchive.gwu.edu/news/cyber-vault/2019-02-20/tainted-trove) a
misspelling in one instruction helped draw attention before more went out. The same complaint charged a North Korean
programmer, Park Jin Hyok, naming him as part of a government-sponsored team and tying the group to Sony and to what
came alongside.

Ransomware ran in parallel, and one instance of it read as a blunter instrument. WannaCry spread indiscriminately in May
2017, reaching [more than 200,000 victims across at least 150 countries](https://www.aljazeera.com/news/2017/5/14/ransomware-attack-hit-200000-victims-in-150-countries)
and encrypting hospitals and firms with no relation to any target list.
The [US indictment](https://www.justice.gov/archives/opa/pr/three-north-korean-military-hackers-indicted-wide-ranging-scheme-commit-cyberattacks-and)
that later set out the wider campaign describes bank heists, cryptocurrency theft, ransomware and extortion across
overlapping periods rather than a clean succession from one method to the next. As a revenue tool WannaCry was, on its
own terms, unimpressive: indiscriminate propagation and small ransom demands make it a poor cousin to the targeted theft
that generated the real money.

Cryptocurrency theft is the form that generated it. It suits the mission precisely: settlement is fast, final, and
beyond the reach of any correspondent bank that might claw a transfer back. The UN Panel estimated
around [three billion dollars taken across 58 suspected attacks](https://www.abc.net.au/news/2024-03-22/north-korea-stealing-cryptocurrency-to-fund-nuclear-weapons/103618152)
on crypto platforms between 2017 and 2023. Blockchain analysis put
a [single year, 2022, at 1.7 billion](https://gjia.georgetown.edu/2024/05/27/how-north-koreas-cryptocurrency-theft-supports-foreign-policy-goals/),
and 2025 higher again, with DPRK-linked actors estimated by Chainalysis to have
taken [around two billion dollars in that year](https://www.chainalysis.com/blog/crypto-hacking-stolen-funds-2026/)
and a cumulative total approaching seven billion. Bybit alone accounted for roughly 1.5 billion. These are
attribution-based estimates drawn from onchain analysis, not audited accounts, and estimated is the operative word.

The quietest form is payroll. Thousands of skilled workers, dispatched mostly to China and Russia and equipped
with [stolen and fabricated identities](https://www.justice.gov/archives/opa/pr/justice-department-disrupts-north-korean-remote-it-worker-fraud-schemes-through-charges-and),
take remote IT jobs at companies that believe they are hiring domestic freelancers. The US government has warned that
[individual workers can earn up to 300,000 dollars a year](https://www.justice.gov/opa/pr/justice-department-announces-nationwide-actions-combat-illicit-north-korean-government),
the collective take running to hundreds of millions, routed back to entities including the Ministry of Defence. A December 2024 indictment
described [fourteen nationals generating at least 88 million](https://www.justice.gov/archives/opa/pr/fourteen-north-korean-nationals-indicted-carrying-out-multi-year-fraudulent-information)
over roughly six years, remitted through Chinese financial channels for the regime's benefit. The scheme has since drawn
a run of prosecutions against the US-based facilitators who host
the [laptop farms](https://www.justice.gov/opa/pr/two-us-nationals-sentenced-facilitating-fraudulent-remote-information-technology-worker)
that make the deception work.

The position has since grown teeth. In July 2026 eleven states, the Netherlands among them, issued a [joint
alert](https://www.canada.ca/en/global-affairs/news/2026/07/alert-to-countries-companies-and-other-entities-regarding-north-korean-it-workers.html)
warning that North Korean IT workers were concealing their identities with increasing sophistication, artificial
intelligence among the tools, and were now tied not only to wages but to data theft, cryptocurrency theft and the
exfiltration of sensitive information. The state's cut of these earnings runs to [90 or 95 per
cent](https://www.koreaherald.com/article/10440989), one defector recalling that he kept about five. The worker, then,
is no longer only a cheaper substitute for a hacker. The salaried seat is itself an access point: a fraudulent hire who
can draw a wage, reach privileged systems, remove data, take cryptocurrency, plant malware and remit the proceeds is not
one technique but several folded into a single chair.

Fraud at the terminal, ransom at scale, theft on the chain, wages by proxy: four techniques feeding, on the evidence,
one state revenue apparatus, and the fourth is quietly becoming the others' host.

## Two payrolls

The digital payroll has an older, heavier twin. Long before a programmer sat unseen inside a Western company's chat
channels, the state was exporting bodies. A UN estimate put [roughly 100,000 North Koreans working
abroad](https://www.nknews.org/2024/03/100k-north-koreans-still-earning-money-for-regime-overseas-un-report/) in 2023,
generating on the order of 500 million dollars a year, spread across some forty countries in information technology,
construction, hospitality and medicine. The state takes the bulk of what they earn.

This is not only historical residue. Investigations have traced [North Korean forced labour into Russian construction
and Chinese seafood supply chains](https://liberties.aljazeera.com/en/north-koreas-forced-labour-reaches-europe/), some
of the product surfacing in goods bound for the EU, one importer reportedly supplying cafeterias in the European
Parliament, with much of the wage taken by the state.

So there are two payrolls. One is a programmer with a fabricated identity, invisible on a video call. The other is a
labourer physically present on a building site or a trawler, entirely visible and no freer for it. Both convert
controlled North Korean labour into foreign currency the state can spend. The IT worker is the interesting case
precisely because it is the digital successor to the older model, the same extraction moved onto the wire, where it
scales and hides better.

## A repertoire, not a trick

Beside the cyber theft, the labour export shows a shape larger than either. A 2025 RAND assessment, working through the
record the old UN Panel left behind, mapped DPRK sanctions-evasion activity worldwide between 2010 and 2022: [China and
Russia together accounted for over half of
it](https://www.rand.org/content/dam/rand/pubs/research_reports/RRA3400/RRA3413-1/RAND_RRA3413-1.pdf), and the greatest
numbers turned up across Asia, Africa and Europe, in construction, manufacturing, textiles and much else. The apparatus
is not a cyber economy with a few sidelines. It is a repertoire of extraction mechanisms, of which cyber is the newest
and most scalable arm.

The clearest sign that it is a repertoire rather than a trick is that it changes with circumstance. Since September 2023
the state has found a buyer able to pay in an unusually useful currency: demand for weapons. The [Multilateral Sanctions
Monitoring Team
reported](https://msmt.info/view/save/2025/05/29/1085cade-a4b1-4405-94c0-7c980c24fd21-Unlawful_Military_Cooperation_including_Arms_Transfers_between_North_Korea_and_Russia_%28MSMT_2025_1%29.pdf)
a sharp expansion of military cooperation with Russia, arms transfers, and later the deployment of North Korean troops,
with one participating state's assessment putting 2024 ammunition deliveries as high as nine million rounds.

That complicates the tidy image of cyber as the revenue line. It may no longer be the dominant one. A Bloomberg
Economics analysis in August 2026 estimated the state generated [as much as 22 billion dollars in foreign revenue from
2022 to
2025](https://en.protothema.gr/2026/08/17/how-kim-jong-un-circumvented-sanctions-and-funneled-up-to-22-billion-into-pyongyangs-coffers/),
with arms and military cooperation a major component. The figure is necessarily soft, but the direction is not subtle,
and it sits well above what the cyber estimates alone would carry. The earlier assessments that put cyber at around half
of foreign-currency income belong to the window before the Russia relationship scaled; the mix has almost certainly
shifted since.

A state with a cyber economy would be in difficulty the moment a given technique was countered. A state with a
repertoire reaches for another instrument when conditions change.

## Ships, coal, and wigs

The repertoire reaches back into the physical economy as readily as the digital one. Illicit coal exports [appear to be
rising again on 2025 port
data](https://www.nknews.org/2026/06/north-korean-illicit-coal-exports-rising-due-to-lax-sanctions-monitoring-report/),
moved through third-country logistics and origin-laundered so the cargo loses its provenance, with China functioning
less as a straightforward buyer than as a financial and logistical interface. Alongside the illicit trade runs a legal
one, and it has its oddities. In 2023 North Korea sent China [around 167 million dollars of wigs, false eyelashes and
hairpieces](https://www.koreatimes.co.kr/foreignaffairs/northkorea/20240122/n-koreas-exports-of-beauty-products-jump-over-13-times-in-2023-data),
some 57 per cent of its recorded exports for the year, much of it [relabelled and re-exported onward as made in
China](https://www.asiaone.com/asia/how-north-korean-eyelashes-make-their-way-west-made-china).

The footprint is not always a wallet or a warship. Sometimes it is a wig. The accounting is comic; the sum is not.

Under all of it sits the oldest infrastructure of evasion, the ship. The UN Panel documented continuing evasion through
deceptive vessel practices and illicit petroleum imports, and FATF now names [maritime and shipping
exploitation](https://www.fatf-gafi.org/en/publications/Financingofproliferation/complex-proliferation-financing-sanction-evasion-schemes.html)
as one of the major sanctions-evasion typologies tied to proliferation financing. The two infrastructures run in
parallel. A cyber campaign needs domains, wallets, proxies, exchanges, front companies and stolen identities. A maritime
evasion operation needs ships, flags, ownership structures, manifests, transshipment points and brokers. Both are
apparatus for crossing a boundary that is supposed to be shut.

## Laundering is the machinery

Whatever the instrument, the proceeds have to come home, and the route home is not an afterthought. North Korean
financial institutions and representatives operate abroad through [front companies, banking relationships and
intermediaries](https://assets.korearisk.com/uploads/sites/4/2024/04/n2403268.pdf), the layer the Panel documented
before it was wound up. In November 2025 the US [sanctioned North Korean bankers and
institutions](https://www.koreatimes.co.kr/foreignaffairs/northkorea/20251105/us-sanctions-8-n-korean-individuals-2-entities-over-cybercrime-money-laundering) described as laundering the proceeds of
cybercrime and IT-worker operations.

So the chain is longer than the roster suggests. Not hacker to cryptocurrency to Pyongyang, but operation to foreign
identity or entity, to intermediary, to conversion, to laundering, to a controlled North Korean institution, to a state
programme. The laundering apparatus is not the plumbing that comes after the interesting part. It is part of the
revenue-generating machinery, and it is also where the chain becomes legible, since each conversion leaves a
counterparty, and counterparties are what indictments and sanctions notices are built from. The state's need to move the
money is the same need that lets outsiders read the system.

## Self-reliance, self-inflicted

The clean version runs: outside threat, therefore poverty, therefore ransomware. It is too clean.

The scarcity is not purely imposed from outside. [Juche](https://www.britannica.com/topic/Juche), the doctrine of
self-reliance that has organised the state since the 1950s, and the military-first priority alongside it, have long
channelled resources towards defence and heavy industry, and the self-sufficiency projects have come, by most accounts,
at considerable economic and social cost. Kim Jong-un has met each round of sanctions with fresh calls
for [self-reliance](https://www.aljazeera.com/news/2019/4/11/north-korea-must-deliver-blow-to-those-imposing-sanctions)
rather than retreat. Some of the scarcity, then, appears to be produced inside the border by policy, not only outside it
by pressure. Sanctions sharpen a condition the regime also manufactures. Treating the revenue operations as a simple
reflex of external pressure understates the case, because the pressure and the policy compound each other.

## From Olympiad to operator

The talent does not appear from nowhere. By [defector and secondary
accounts](https://www.fdd.org/analysis/2018/10/03/kim-jong-uns-all-purpose-sword/), children who show aptitude in
mathematics and science are selected early, and some gifted students are channelled through specialist schools into
institutions including Kim Il Sung University and Kim Chaek University of Technology, with periods of overseas training
before assignment to units under the Reconnaissance General Bureau. The pathway is not a single standard conveyor for
every operator, but its shape recurs across the reporting. Bureau 121, the principal cyber agency, draws hand-picked
graduates and, by defector accounts, rewards them with [privileges rare in the wider
economy](https://www.nbcnews.com/tech/security/north-korea-hackers-are-handpicked-pampered-elite-reuters-n262396).

The system's own edge case is the most telling image of it. In 2016 an eighteen-year-old, [Ri Jong
Yol](https://www.imo-official.org/team_r.aspx?code=PRK&year=2016), took silver at the International Mathematical
Olympiad for the fourth year running and, the night before his team flew home, walked off a Hong Kong campus and sought
refuge in the South Korean consulate. Contemporary reporting described him as a [strong candidate for the country's
elite technical
apparatus](https://www.nbcnews.com/news/north-korea/how-north-korea-recruits-trains-its-army-hackers-n825521), an
assessment rather than a documented posting. The pipeline is engineered closely enough that its raw material becomes
visible at the moment a piece of it declines to travel.

## The observer changed

Two edges stay unclosed, and they are different in kind.

The first is internal. How the currency is actually apportioned, between the missile programme, elite maintenance, and
general survival, is inferred from outside rather than documented from within. The loop closes at aggregate funding, not
at line items. The consolidated balance sheet is a construct, not a ledger anyone has recovered.

The second is the observer's own position. The UN Panel
of Experts, which spent years assembling the record the loop depends on, [lost its mandate on 30 April 2024 after Russia
vetoed renewal](https://press.un.org/en/2024/sc15648.doc.htm). At the time that looked like the observer simply going
dark. It went otherwise. A [Multilateral Sanctions Monitoring Team stood up in October
2024](https://www.government.nl/documents/2025/10/22/joint-statement-multilateral-sanctions-monitoring-team-on-report-covering-dprk-cyber-and-it-worker-activities)
and has since published on the Russia relationship and, pointedly, on cyber and IT-worker activity, describing itself as
filling the gap the Panel's dissolution left.

The replacement is not the same institutional object. Where the Panel was a Security Council-mandated body, the MSMT is
a coalition of participating states, drawing on national submissions and private-sector intelligence rather than a
single mandate. The sanctions architecture itself remains: the [1718 committee still
stands](https://main.un.org/securitycouncil/en/sanctions/1718). What changed was the shape of the body doing the
observing, and its evidential base changed with it. As the state altered what it was doing, moving weight from cyber
towards arms and the Russia relationship, the apparatus watching it altered too. The thing observed and the means of
observing it moved together.

The behaviour is not a matter of national temperament, hacker culture, or the sophistication the roster likes to
advertise. It is what a treasury does when it has been cut off from the ordinary means of filling itself. State-directed
theft is fiscal policy conducted by other means.

The roster stops too early. The more exact picture is a treasury turned inside out. A cryptocurrency exchange becomes an
externally located reserve; a Western company, a payroll provider; a laptop farm, a foreign office; a Russian building
site, an export terminal for labour; a Chinese trading intermediary, something close to a branch bank; a vessel under a
flag of convenience, a moving interface for evasion; and an identity lifted from an ordinary person, a piece of state
infrastructure. The state is small and territorially hemmed in. Its revenue apparatus is geographically enormous,
projected in fragments into other countries' companies, labour markets, banks, shipping lanes, blockchains and citizens.

That inversion is the real footprint, and a highly centralised state produced it, not a decentralised one. The world tries to contain North Korea by shutting its access to the international economy.
North Korea answers by placing pieces of its economy outside North Korea. The boundary built to hold the state in
becomes the surface across which it reaches out. The treasury as target was only half the story. The treasury has
learned to make the world its target surface.
