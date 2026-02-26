# One supplier, no margin

*On vendor monoculture, systemic dependencies, and the failure that cannot be contained*

The Grand Trunk Company operates the clacks network that carries most of
Ankh-Morpork's financial data. This is not a coincidence of history. It
is the outcome of a rational market. The Grand Trunk invested in
infrastructure that no competitor could match. Its network effects meant
that every new connection made the network more valuable, which attracted
more connections, which created more value. The smaller operators who once
ran local semaphore routes found it easier to connect to Grand Trunk than
to compete with it. Connecting to Grand Trunk rather than building your
own network is individually rational. One by one, the individual rational
choices produced a single company handling most of the city's critical
communications.

The Guild of Engineers, similarly, is not a monopoly through malice. It
is a monopoly through competence, reputation, and the network of
relationships that make it the default choice for any serious infrastructure
contract. Hiring a non-guild engineer for a pumping station is technically
possible. It is rarely done, because the Guild certifies its work, insures
its practitioners, and can be held to account in a way that a freelance
engineer cannot. The logic that makes the Guild dominant is the same logic
that makes its dominance a risk: if the Guild's certification standards
are compromised, if its senior practitioners are unavailable, if its
supplier relationships fail, every pumping station it maintains is affected
simultaneously.

The monoculture did not require a conspiracy to produce. It required only
that standardisation, network effects, and incumbent advantage operate as
they normally do. The result is a city where a failure in a single
provider is not a failure of one service in one district. It is a failure
of one service everywhere the provider operates, simultaneously, without
geographic or organisational containment.

## What diversity does

The mechanism of the monoculture problem is easier to understand by
considering what it removes.

When systems are diverse, a failure in one provider is bounded by the
extent of that provider's footprint. The clacks tower in the Shades fails;
the towers operated by the smaller company in the Merchant Quarter continue
running. The pump maintained by an independent engineer fails; the pumps
maintained by a different contractor in Dolly Sisters continue functioning.
The failure is local. It affects the users of the failed provider. It does
not propagate to users of other providers, because those users are not
connected to the failure point.

Diversity is containment. A field planted with ten varieties of wheat,
of which a pathogen can infect one, loses at most a tenth of its crop
to that pathogen. A field planted with a single variety loses everything.
The pathogen is not stronger in the monoculture field. The containment
is weaker. The failure propagates further not because of anything about
the failure itself, but because the diversity that would have bounded it
does not exist.

When all critical systems share a single provider, the failure of that
provider is bounded only by its footprint, which is everything. A fault
introduced into the Grand Trunk's core routing produces simultaneous
outages at every node connected to the Grand Trunk, across every district,
in every building that depends on clacks for coordination. The fault
does not need to be large. It needs only to be in the shared dependency.

## How monocultures form

Vendor monocultures in critical infrastructure form through the same
mechanisms that produce market dominance in any sector. Network effects:
the more users a platform has, the more useful it becomes to each user,
which attracts more users. Standardisation: operating on the same system
as your counterparts reduces transaction costs, which makes the dominant
system stickier as adoption grows. Regulatory entrenchment: a single
system that meets regulatory requirements becomes the default option
for compliance, as it did with MEDoc in Ukraine's tax reporting framework.
Switching costs: once systems and processes are built around a provider,
the cost of switching is high enough to make staying rational even when
the alternative would be marginally better.

None of these dynamics requires bad intentions. Each individual choice
to adopt the dominant provider is rational given the information and
incentives available to the organisation making it. The aggregate outcome,
a critical dependency shared by every organisation in a sector or
geography, is a systemic risk that no individual organisation bears
fully and that therefore does not appear in any individual organisation's
risk register at its true magnitude.

The systemic risk is an externality. Each organisation that joins the
monoculture contributes to the aggregate fragility without fully bearing
its cost. The cost, when a failure occurs, is distributed across every
user of the shared dependency. The benefit of the monoculture, lower
costs, better integration, regulatory compliance, accrues to each
individual organisation. The risk of the monoculture accrues to everyone
simultaneously.

## Nineteen July 2024

On 19 July 2024, a software update to CrowdStrike's Falcon sensor product
caused approximately 8.5 million Windows systems to enter a non-recoverable
boot failure state simultaneously. CrowdStrike's endpoint detection and
response software is installed on a very large fraction of enterprise
Windows systems globally, because endpoint security is a domain where
the market has consolidated around a small number of providers, and
because CrowdStrike had achieved a reputation for technical quality that
made it the default choice for organisations seeking best-in-class
protection.

The failure was not geographically bounded. It was bounded by the
CrowdStrike footprint, which covered organisations across every sector
and every country where large enterprises operate. Dutch banks reported
system failures within minutes of the update deploying. German hospitals
began diverting non-emergency patients as clinical systems went down.
Austrian postal services halted operations. Airports across Europe
reported check-in system failures. Airlines grounded flights, not
because their own infrastructure had failed but because the shared
dependency they had all installed had simultaneously failed.

The fault was in a single content configuration file. The technical
cause was a memory access error in the sensor kernel driver. The
vulnerability that made this into a global event was not the memory
access error. It was the architecture in which a single software update,
deployed automatically to millions of systems without staged rollout
or canary testing at scale, could reach every user of the product
simultaneously, with no geographic or organisational firebreak between
the update and its consequences.

The diversity that would have contained the failure did not exist. Some
organisations recovered within hours because their systems ran on
non-Windows platforms that were unaffected; this is the diversity
mechanism operating at the operating system level, which happened to
provide partial containment. Within the Windows enterprise ecosystem,
containment was absent. The failure propagated to the full extent of
the shared dependency's footprint.

- [Airlines and Financial Services Hit Hard by CrowdStrike Outage, David Love, July 19, 2024](https://www.nasdaq.com/articles/airlines-and-financial-services-hit-hard-crowdstrike-outage)
- [CrowdStrike Shares How a Rapid Response Content Update Caused Global Outage, 24 July 2024](https://www.infosecurity-magazine.com/news/crowdstrike-response-update-outage/)
- [Monitoring and Support During the CrowdStrike Falcon Outage, CIS case study](https://www.cisecurity.org/insights/case-study/monitoring-and-support-during-the-crowdstrike-falcon-outage)

## Ukraine, June 2017

On 27 June 2017, a software update to MEDoc, a Ukrainian accounting
application, delivered a destructive payload to every system that had
installed it. MEDoc was not a niche product. Ukraine's state tax service
had mandated its use for electronic tax reporting, making it a de facto
regulatory requirement for any business conducting formal financial
activity in the country. The monoculture was not the outcome of market
preference alone; it was the outcome of regulatory structure that
required adoption of a single tool.

The attack, which became known as NotPetya, spread from MEDoc-connected
systems through shared network credentials and unpatched SMB
vulnerabilities to any reachable Windows machine. It was designed to
destroy rather than to extort: systems encrypted without recoverable
keys, master boot records overwritten. Ukrainian infrastructure was the
primary target. The mechanism of propagation was the shared dependency.

The malware reached Maersk, the Danish shipping conglomerate, through
a single computer at its Ukrainian office that had MEDoc installed. From
that entry point, it reached 45,000 PCs and 4,000 servers across the
company's global network within hours, because the network was flat
enough to allow it. Port terminals worldwide stopped accepting containers.
The global container shipping network, which Maersk operates at a scale
representing roughly a fifth of global trade, was operationally dark for
ten days. TNT Express, the Dutch logistics company, lost an estimated
400 million euros in a single quarter. Pharmaceutical and food manufacturers
across Europe reported production and distribution disruptions.

The original entry vector was one computer at one Ukrainian office using
one piece of tax compliance software. The monoculture that converted
this local entry into a global catastrophe operated at two levels: the
regulatory monoculture that mandated MEDoc, and the flat network
architecture within affected organisations that provided no containment
once the initial compromise was achieved.

- [TNT Express pegs Petya losses at $374m, Juha Saarinen, Sep 21 2017](https://www.itnews.com.au/news/tnt-express-pegs-petya-losses-at-374m-473837)
- [Ransomware attacks impact corporate earnings, Stuart Collins, September 22, 2017](https://www.commercialriskonline.com/ransomware-attacks-impact-corporate-earnings/)
- [NotPetya attack cost up to £15m, says UK ad agency WPP, Warwick Ashford, 25 Sep 2017](https://www.computerweekly.com/news/450426854/NotPetya-attack-cost-up-to-15m-says-UK-ad-agency-WPP)
- [Year in Review: Malware Attacks Impact Operations and the Bottom Line, December 22, 2017](https://www.cfr.org/articles/year-review-malware-attacks-impact-operations-and-bottom-line)

## The booking system behind the airline

Amadeus is the largest global distribution system for airline bookings,
handling the reservation and inventory management for hundreds of airlines
worldwide. Airlines use Amadeus because it provides the industry-standard
interface through which travel agents and online booking systems access
inventory. The network effects are strong: being on Amadeus gives an
airline access to the full distribution ecosystem; being off it means
accepting limited distribution. The rational choice for most airlines is
adoption.

When Amadeus experiences availability problems, which it has on several
occasions, the affected airlines include competitors who otherwise share
no infrastructure. A failure in Amadeus is not an airline failure; it
is a booking layer failure that produces simultaneous booking unavailability
across airlines that have invested heavily in keeping their own core
systems separate and independent. The independence they have maintained
applies to everything except the layer they all share.

This is the characteristic signature of the monoculture failure mode: the
failure appears in a layer that is not typically included in individual
organisations' infrastructure risk assessments, because it is provided
by a vendor, listed as a dependency, and treated as an external service
rather than as a component of the organisation's own infrastructure.
The risk that Amadeus might fail, and that its failure would produce
simultaneous outage across hundreds of airlines, is a risk that no
individual airline fully accounts for, because no individual airline
controls it. It is a systemic risk generated by the collective adoption
of a shared dependency, distributed across all users of that dependency,
and visible to none of them individually at its full magnitude.

- [Amadeus: The Software Behind The 45-Minute Airport Check-In Glitch, Dec 03, 2025](https://www.ndtv.com/india-news/what-triggered-the-airport-check-in-chaos-amadeus-software-explained-9743330)
- [Navitaire outage: Airline ops hit in India, Asia-Pacific and Europe; Know what’s the current status, February 19, 2026](https://www.thestatesman.com/india/navitaire-outage-airline-ops-hit-in-india-asia-pacific-and-europe-know-whats-the-current-status-1503559399.html)

## The risk register blind spot

Single-vendor dependencies produced by market consolidation, regulatory
standardisation, or network effects rarely appear in organisational risk
registers at their systemic magnitude. They appear, if they appear at all,
as third-party risks assessed at the level of one organisation's exposure
to one provider's failure. This assessment understates the actual risk
in two ways.

The first is correlation. When an organisation assesses the risk that its
clacks provider will fail, it assesses the probability of an outage
affecting its own service. What it does not assess is the probability
that the same outage will simultaneously affect every other organisation
in its sector that uses the same provider, producing a correlated failure
that removes the ability to divert to alternatives or draw on sector-wide
mutual aid. A shared dependency that fails does not just fail for one
organisation. It fails for every organisation in the same position at
the same time.

The second is second-order exposure. When an organisation assesses its
own exposure to a provider failure, it does not typically assess its
exposure to failures in providers that its own providers depend on. An
airline assessing its IT infrastructure risk might assess the risk of
its booking system provider failing. It is less likely to assess the
risk of the certification authority that validates the booking system's
security certificates, or the cloud infrastructure provider that the
booking system runs on, failing. The dependency chain extends beyond the
first-order vendors, and the monocultures that matter most in a crisis
are often several layers down, invisible to the organisation until
something at that layer fails.

## What containment requires

Containment of monoculture failures requires diversity at the level of
the shared dependency, which is frequently at odds with the economics
that produced the monoculture in the first place.

An organisation that runs two competing clacks providers for different
parts of its communication network is paying more per message than an
organisation that has consolidated onto one provider and negotiated
volume pricing. A sector that maintains two booking systems for different
route groups is paying for duplication that appears inefficient in normal
operation. A city that uses two engineering guilds for different
infrastructure domains has a more complex contracting environment than
a city that has consolidated all maintenance with one guild.

The cost of diversity is real, visible, and accrues in every normal
period. The benefit of diversity is real, invisible, and only accrues
in the periods when the dominant provider fails. The normal periods are
almost all of them. The economics consistently favour consolidation.
The risk consistently favours diversity. These two facts coexist and
the economics generally win, until a 19 July when they don't.

## The Guild's leverage

In Ankh-Morpork, the Guild of Engineers understands its position very
well. It does not need to provide poor service to be a risk to the city.
It only needs to be indispensable, which it has ensured it is, to have
leverage that would not be available to it if the city's pumping stations
were maintained by a diverse collection of competing contractors. This
leverage is exercised politely, in the form of contract negotiations that
the Patrician would prefer to resolve differently but cannot. The city's
dependency is not a secret. It is a structural feature of how the
maintenance market developed, and reversing it would require maintaining
two engineering guilds for years at higher total cost to establish
the competitive alternative that does not currently exist.

The Patrician considers this situation with the particular patience he
reserves for structural problems that cannot be resolved in a single
budget cycle. The Grand Trunk Company is a similar consideration. The
Purple Lantern data house is a third. In each case, the city depends on
a single provider for something critical, and the path back to diversity
is longer and more expensive than the path that led to the monoculture.

The failure, when it comes, will not be bounded by geography or by which
service the fault originates in. It will be bounded by the footprint of
the provider. The footprint is everything.

The Patrician makes a note on his list. The list is already long.
