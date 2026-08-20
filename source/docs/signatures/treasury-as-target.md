# The treasury as target

*North Korea, and cyber operations run as a revenue line*

The standard account of North Korean hacking arrives as a
roster. [Lazarus Group](https://attack.mitre.org/groups/G0032/), [APT38](https://attack.mitre.org/groups/G0082/), 
[Bureau 121](https://plausibledenial.org/north-korea/rgb-bureau-121), a drift of aliases behind
them (BlueNoroff, [Andariel](https://attack.mitre.org/groups/G0138/), 
[Kimsuky](https://attack.mitre.org/groups/G0094/)), and a highlight reel to match: Sony in 2014, the [Bangladesh 
central bank in 2016](https://attack.mitre.org/groups/G0082/), [WannaCry in 2017](https://attack.mitre.org/software/S0366/), a long run of exchange thefts, and
the [Bybit heist of February 2025](https://www.fbi.gov/investigate/cyber/alerts/2025/north-korea-responsible-for-1-5-billion-bybit-hack),
attributed by the FBI to North Korean actors and the largest cryptocurrency theft on record. The roster names
capabilities and pins incidents to a flag. It treats the money as motive, and having named the motive, it stops.

The question here is not what the groups do but what conditions produce a state whose cyber operations function, overtly
and at scale, as a revenue line.

What sets the case apart is degree rather than kind. Other states host, tolerate, or direct financially motivated
operations. [Iranian actors have been documented](https://home.treasury.gov/news/press-releases/sm556) running
ransomware for profit, and the Russian ecosystem blurs criminal and state operations to the point where the categories
overlap. What is unusual about Pyongyang is how sustained the revenue function has become, and how consistently the
international record describes its cyber actors in exactly those terms: tasked with raising money for the country. The
difference is one of emphasis and legibility, not a monopoly.

## A loop that closes, at one level

The condition can be described, the behaviour can be described, but the return path, the line showing that the behaviour
feeds back into the condition that produced it, tends to resist sourcing. The North Korean case is unusual in that the
loop closes, provided the level at which it does so is stated plainly.

Sanctions imposed over the nuclear and ballistic-missile programmes constrict the state's access to foreign currency and
to ordinary international finance. Cyber operations offer another route to it. The proceeds help sustain the regime and,
on the available evidence, help fund the weapons programme, whose continuation is what the sanctions answer. Revenue in,
survival out, and back again, at least in outline.

The return edge is the part that can be cited rather than asserted, and it can be cited at the level of aggregate state
finance, not at the level of individual stolen dollars.
The [UN Panel of Experts](https://digitallibrary.un.org/record/4041323/files/S_2024_215-EN.pdf), the body that monitored
sanctions compliance until its mandate lapsed in 2024, described cyber-threat actors subordinate to the Reconnaissance
General Bureau, naming Kimsuky, Lazarus, Andariel and BlueNoroff, and set out their key tasks as obtaining information
of value and illicitly generating revenue for the country. Member-state reporting to the Panel put figures in the open:
one government's assessment held that malicious cyber activity
generated [roughly half of the country's foreign-currency income](https://digitallibrary.un.org/record/4041323/files/S_2024_215-EN.pdf),
another that around 40% of the weapons-of-mass-destruction programmes were funded by illicit cyber means. These are
assessments reported by the Panel, not numbers it independently derived, and the loop they let one close is a loop of
aggregate funding rather than a traceable transaction-level circuit. Held at that level, it holds.

![A reinforcing loop in the finance of the North Korean state. Sanctions cut the state's access to foreign currency, cyber operations restore it, the revenue funds the weapons programme, and the programme's continuation is what draws the sanctions, closing the circuit. Marked R, one reinforcing loop, held at the level of aggregate state finance rather than traceable transactions. Drawn in grey, meaning a sourced effect on a branch with no evidenced return into the loop: self-reliance policy (juche), and the supply of trained operators. An increase in sanctions on the DPRK lowers access to foreign currency. An increase in access to foreign currency lowers illicit cyber revenue operations, by human intervention. An increase in illicit cyber revenue operations raises state hard-currency income. An increase in state hard-currency income raises the nuclear and missile programme. An increase in the nuclear and missile programme raises sanctions on the DPRK, by human intervention. An increase in self-reliance policy (juche) lowers access to foreign currency, by human intervention. An increase in the supply of trained operators raises illicit cyber revenue operations, by human intervention.](/_static/images/treasury-loops-diagram.svg)

## The signature is the print of the problem

Read the operational history as a signature, and it maps, item by item, onto a state that needs hard currency and cannot
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
2017, reaching some 300,000 machines across 150 countries and encrypting hospitals and firms with no relation to any
target list.
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
individual workers can earn up to 300,000 dollars a year, the collective take running to hundreds of millions, routed
back to entities including the Ministry of Defence. A December 2024 indictment
described [fourteen nationals generating at least 88 million](https://www.justice.gov/archives/opa/pr/fourteen-north-korean-nationals-indicted-carrying-out-multi-year-fraudulent-information)
over roughly six years, remitted through Chinese financial channels for the regime's benefit. The scheme has since drawn
a run of prosecutions against the US-based facilitators who host
the [laptop farms](https://www.justice.gov/opa/pr/two-us-nationals-sentenced-facilitating-fraudulent-remote-information-technology-worker)
that make the deception work. Fraud at the terminal, ransom at scale, theft on the chain, wages by proxy: four
techniques feeding, on the evidence, one state revenue apparatus.

## Where the tidy version breaks

The clean version runs: outside threat, therefore poverty, therefore ransomware. It is too clean.

The scarcity is not purely imposed from outside. [Juche](https://www.britannica.com/topic/Juche), the doctrine of
self-reliance that has organised the state since the 1950s, and the military-first priority alongside it, have long
channelled resources towards defence and heavy industry, and the self-sufficiency projects have come, by most accounts,
at considerable economic and social cost. Kim Jong-un has met each round of sanctions with fresh calls
for [self-reliance](https://www.aljazeera.com/news/2019/4/11/north-korea-must-deliver-blow-to-those-imposing-sanctions)
rather than retreat. Some of the scarcity, then, appears to be produced inside the border by policy, not only outside it
by pressure. Sanctions sharpen a condition the regime also manufactures. Treating the revenue operations as a simple
reflex of external pressure understates the case, because the pressure and the policy compound each other.

## The pipeline is part of the substrate

The talent does not appear from nowhere. By [defector and secondary accounts](https://www.fdd.org/analysis/2018/10/03/kim-jong-uns-all-purpose-sword/),
children who show aptitude in mathematics and science are selected early, some reportedly from around fourteen, and some
gifted students are channelled through specialist schools into institutions including Kim Il Sung University and Kim
Chaek University of Technology, with periods of overseas training before assignment to units under the Reconnaissance
General Bureau. The pathway is not a single standard conveyor for every operator, but its shape recurs across the
reporting. Bureau 121, the principal cyber agency, draws hand-picked graduates and, by defector accounts, rewards them
with [privileges rare in the wider economy](https://www.nbcnews.com/tech/security/north-korea-hackers-are-handpicked-pampered-elite-reuters-n262396).

The system's own edge case is the most telling image of it. In 2016 an
eighteen-year-old, [Ri Jong Yol](https://www.imo-official.org/team_r.aspx?code=PRK&year=2016), took silver at the
International Mathematical Olympiad for the third year running and, the night before his team flew home, walked off a
Hong Kong campus and sought refuge in the South Korean consulate. Contemporary reporting described him as
a [strong candidate for the country's elite technical apparatus](https://www.nbcnews.com/news/north-korea/how-north-korea-recruits-trains-its-army-hackers-n825521),
an assessment rather than a documented posting. The point survives the qualification: the pipeline is engineered closely
enough that its raw material becomes visible at the moment a piece of it declines to travel.

## What stays open

Two edges are best left unclosed, and one of them has grown wider.

The first is internal. How the currency is actually apportioned, between the missile programme, elite maintenance, and
general survival, is inferred from outside rather than documented from within. The loop closes at aggregate funding, not
at line items. The consolidated balance sheet is a construct, not a ledger anyone has recovered.

The second is the observer's own position, and here the case demonstrates the substrate problem in real time. The
reading leans on the UN Panel because the Panel spent years assembling the record that lets the loop close. That Panel's
mandate [ended on 30 April 2024 after Russia vetoed its renewal](https://press.un.org/en/2024/sc15648.doc.htm). The
sanctions architecture itself remains: the 1718 committee still stands. What lapsed was the body doing the observing. So
the evidential terrain thins from here, shifting towards threat-intelligence vendors and onchain investigators whose
incentives are their own. The edges of the system have moved because the institution watching them has gone, which is
the substrate problem turned on the analyst rather than the subject.

What survives all of it is a single displacement. The behaviour is not a matter of national temperament, hacker culture,
or the sophistication the roster likes to advertise. It is what a treasury does when it has been cut off from the
ordinary means of filling itself. State-directed theft is fiscal policy conducted by other means.