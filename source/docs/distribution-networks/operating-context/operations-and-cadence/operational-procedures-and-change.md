# Operational procedures and change

Stedin's operational procedures and change cadence sit in a stack of nested rhythms, from daily dispatch through
multi-decade programme milestones. The procedures themselves are dense and auditable, rooted in the Dutch sector safety
frameworks BEI and VIAG, layered with Stedin's own Bedrijf Specifiek Supplement.

## Change cadence

### Maintenance announcements

Two announcement rhythms are visible. Routine planned interruptions run on a short customer-notice cycle, a minimum of a
few days ahead, per
the [Stedin planned-maintenance page](https://www.stedin.net/storing-en-onderhoud/gepland-onderhoud).

The reinforcement programme, on the [Stedin buurtaanpak page](https://www.stedin.net/energietransitie/buurtaanpak), runs
on a longer, three-step communication cadence: a general announcement letter, then a letter once the new substation
locations are agreed with the municipality, then a letter two weeks before work starts, with a BouwApp for following
progress.

The published planning is explicitly provisional, revised as municipal talks and contractor capacity shift, which
signals
that the cadence is rolling rather than fixed.

### Procurement schedules and framework contracts

The defining cadence shift is from project-by-project procurement to long framework contracts with fixed partners, the
LS Buurtaanpak framework signed in January 2026 and the earlier infracontracten from 2024. The contractor-side detail,
the parties, the terms and the area-based assignment, is in [contractor management](contractor-management.md).

On materials, the metering side runs on multi-year frameworks (the smart-meter awards and the 2025 modular DSMR6
tender). The procurement schedule is thus consolidating into fewer, longer commitments rather than recurring competitive
rounds.

### Tender timelines

The buurtaanpak tender-to-execution gap is unusually legible and short: contracts signed in January 2026, a joint
onboarding period across February and March, and first neighbourhoods taken into commission from April 2026 (contractor
announcements, perishable). The production build-up is then staged gradually over the first years rather than immediate.

### Release planning

On the IT and OT side the cadence is quarterly and Agile. Stedin runs Big Room Planning, a quarterly two-day SAFe
planning event bringing IT and business together to set the coming quarter's development, across a DevOps and BizDevOps
organisation (Stedin careers material, and Stedin GIS and SAP recruitment adverts). Larger platform moves happen in
compressed windows, the SAP S/4HANA migration reported as done in four months. So software change runs on a quarterly
increment rhythm sitting well inside the multi-year physical programmes.

### Major programme milestones

Several dated milestones fix the long cadence. The brittle-gas replacement carries a hard 2028 completion target. The
buurtaanpak is framed to reach roughly 3,000 neighbourhoods by 2050, staged through the multi-year contracts above.
Individual transport projects carry their own dates, such as the 150 kV replacement of the Noordring toward mid-2027.
And the planning instruments themselves are milestone-generating: a two-yearly investment plan cycle (IP2024, IP2026),
area masterplans to 2050, and a strategic investment plan reaching 2037. The programme layer is therefore anchored by a
small number of dated commitments spanning years to decades.

### The change itself, from per-station to per-area

Stedin has moved from tackling the network station by station to neighbourhood by neighbourhood, area-based. The old
per-station route generated repeated engineer-then-reject-then-re-engineer loops with municipalities, and that delay
pattern was incompatible with the pace required. The buurtaanpak with fixed contractor and Stedin teams is the operating
model built to remove that churn, underpinned by an execution agreement with the sector and construction bodies.

### The cadence, in layers

The evidence resolves into a stack of nested rhythms:

Real-time and daily, the Bedrijfsvoeringscentrum and meldpunt with the storingsdienst rota. Weekly, contractor work
planning submitted to the meldpunt under framework orders. Quarterly, Big Room Planning and the IT release increment.
Annually, the safety supplement renewing on a fixed 15 April cycle, the tariff proposals and decisions, and the
refreshed build planning. Two-yearly, the investment plan and the quality plans. Five-yearly, the ACM method decision
and WACC reset that set the capital envelope, plus the multi-year materials frameworks. Multi-year, the
six-to-twelve-year buurtaanpak contracts, the three-to-seven-year station projects, and dated targets like brittle gas
to 2028. Multi-decade, the 2050 masterplans and the roughly 3,000-neighbourhood programme.

This cadence is not freestanding: the five-yearly regulatory envelope and the two-yearly investment plan set the outer
clock. The framework contracts with fixed teams are the response to labour and capital constraints, converting scarce
crews into a steady production rhythm rather than stop-start projects. The area-based model is the change made to fit
the pace the transition demands. A technical roadmap would show milestones; the procurement and announcement trail shows
the operating tempo those milestones actually move at.

## Operational workflows

### Permit to work and the appointment system

BEI (Bedrijfsvoering Elektrische Installaties) sets the safety procedures for working on or near electrical
installations, VIAG does the same for gas, and Stedin adds its
own [Bedrijf Specifiek Supplement](https://www.stedin.net/zakelijk/techniek/veilig-werken) with an annual cycle starting
15 April.

Permission to work is not a document so much as a personal appointment (aanwijzing) held in Stedin's
Bedrijfsvoering application.

The role hierarchy is explicit in
the [Stedin BSS BEI](https://www.stedin.net/-/media/project/online/files/zakelijk/branches/aannemers-en-projectontwikkelaars/veilig-werken/stedin-bss-bei.pdf):
the Installatieverantwoordelijke (IV) is the installation-responsible authority who assesses and accredits, the
Operationeel IV (OIV) carries it per area operationally, the Werkverantwoordelijke (WV) is the work-responsible person
per voltage or gas domain, and the Bedieningsdeskundige (BD) is the switching operator.

Before any work, a werkplan and
often a bedieningsplan (switching plan) are created digitally in the Bedrijfsvoering application. So permit-to-work here
is a digital, role-gated workflow rather than a paper chit.

### Switching authorities

Switching authority is a specific flag, not a general competence. A person may perform switching only if their
appointment in the Bedrijfsvoering tool carries the tag "Stedin Schakelbevoegd", which is added only after the WV or AVP
training plus a Stedin-specific switching course from the Stedin Academie, per
Stedin's [contractor information sheet](https://www.stedin.net/-/media/project/online/files/zakelijk/branches/aannemers-en-projectontwikkelaars/veilig-werken/informatieblad-voor-aannemers.pdf).

A two-pair-of-eyes principle applies to the higher-risk cases: in low-voltage distribution fault situations involving
extended operations, the draft bedieningsplan is approved by a second BD and filed within five working days (BSS BEI).

High-voltage work is described from the inside in a recruitment advert: preparing the day from the planned-work
overview, drawing up work plans, switching net sections out and in, guarding on-site safety and supervising
commissioning, on behalf of Stedin, TenneT and commercial clients (Stedin WV Hoogspanning advert, a recruitment page).

### Planned outage processes

Planned work runs off the same werkplan and bedieningsplan artefacts, prepared in advance so that the switching sequence
is designed and second-checked before anyone is on site.

Customer-facing notice of a planned interruption runs on a minimum lead time (three days, from Stedin's
planned-maintenance guidance), which ties back to the compensation regime that excludes announced planned work.

### Contractor access

Contractor access is the most documented part of the appointment system: assessment and accreditation, recognised
credentials, a key policy, an appointment register, metering-company access limits and heavy screening. Because that
regime is contractor-specific, it is set out in full in [contractor management](contractor-management.md).

### Emergency restoration

The out-of-hours architecture is a standby-and-fault-duty rota. Outside regular hours the OIV holding storingsdienst
assumes responsibility for all operations in the area, and the meldpunt always holds a current per-area overview of who
is authorised (BSS BEI).

The rota is visible in pay terms in the adverts: a weekly standby-and-fault allowance in the region of 420 to 440 euro,
with evening, night and weekend hours at 150 and 200 per cent (Stedin Monteur Gas and WV Hoogspanning adverts,
recruitment pages). A WV is required to be reachable and on site within one hour on request. So restoration is carried
by the same appointed WV and BD population operating under the same switching discipline, just under a duty rota rather
than the day plan.

### Incident response

For cyber, the response is the SOC watching IT and OT as one domain, notification to the CSIRT and supervisor on the
NIS2 cadence, island mode for critical systems, and rehearsed restart-after-outage scenarios (from the public
conference account). For physical-safety incidents on gas, the working practice has been pushed toward
gasless and pressureless working after the regulator's findings on the Zoetermeer explosion, which is an incident-driven
procedural change rather than a standing document.

### Storm procedures

No named storm playbook surfaced, but the components that would carry one are all present: the storingsdienst and
wachtdienst rota, the meldpunt as the always-current dispatch overview, the OIV assuming area authority out of hours,
and the one-hour WV availability. The weather dimension shows up obliquely, as extreme weather sitting outside the
compensation regime and as extreme rainfall hampering the maintenance programme in 2023. So the reasonable inference is
that storm response is an escalation of the standby architecture rather than a separate regime, though the
surge-staffing and mutual-aid detail is the part not visible in these sources.

The procedures predict their artefacts cleanly: a Bedrijfsvoering application holding per-person appointments with a
Schakelbevoegd flag, a BAR appointment register, digital werkplannen and bedieningsplannen per job, a key-management
ledger with issue-and-recall records, a meldpunt with a live per-area authority overview, weekly contractor planning
submissions, and a duty rota. This is a dense, auditable operational trail.

*Last updated: 11 July 2026*
