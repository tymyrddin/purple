# Contractor management

Contractors do a large share of the operational work: field maintenance, cable laying, substation construction, relay commissioning, metering installation, and emergency restoration. They are effectively an extension of the workforce, and much of the operational evidence is created through their hands.

At the end of 2023, Stedin Netbeheer staffed 5,471 people, 4,465 internal and 1,006 external (contracted), so roughly 18 per cent of the workforce was hired-in (2023 group annual report, via a council-hosted copy). Beyond this, contractors perform the physical build and maintenance work under framework contracts, which shapes what operational evidence exists and how work gets authorised and tracked.

## Framework contracts and area-based assignment

Stedin has moved from project-by-project procurement to long-term framework contracts with fixed partners. The [LS Buurtaanpak framework](https://www.stedin.net/energietransitie/buurtaanpak), signed in January 2026, is Stedin's largest network tender at around 3.5 billion euro, involving twelve contractors, each assigned a geographic area and coupled to fixed operator teams. Contracts run roughly six to twelve years, creating stable working relationships rather than transient project teams.

The buurtaanpak programme targets reaching roughly 3,000 neighbourhoods by 2050, staged through the multi-year contracts. First neighbourhoods were taken into commission from April 2026, with the ramp staged as three projects in 2026, seven in 2027 and thirteen in 2028, targeting a steady state of ten or more neighbourhoods per contractor per year.

Earlier infracontracten, introduced across the network area from 2024, similarly moved to pre-agreed longer-term working arrangements with contractors (2023 report). This consolidation into long-term relationships means a stable pool of contractors rather than rotating teams, which improves continuity but also creates persistent relationships where contractors gain deep knowledge of the systems and procedures.

## Access and credential management

Contractor access to the systems is governed through a documented access-control regime. Contractors are assessed by the Installatieverantwoordelijke (IV, installation-responsible authority) and hold their own appointment policy meeting national law, with a minimum of two Werkverantwoordelijken per discipline, and recognised credentials such as Stipel PCE, VCA and NBNL-GPI, all set out in Stedin's [contractor information sheet](https://www.stedin.net/-/media/project/online/files/zakelijk/branches/aannemers-en-projectontwikkelaars/veilig-werken/informatieblad-voor-aannemers.pdf).

Physical access is governed by the Sleutelbeleid (key policy), set out in the [metering-company information sheet](https://www.stedin.net/-/media/project/online/files/zakelijk/branches/aannemers-en-projectontwikkelaars/veilig-werken/informatieblad-voor-meetbedrijven.pdf): keys are issued through the key-management function, the IV, OIV or WV can order keys handed back without giving a reason, and a monthly list of authorised staff is exchanged with the contractor. Appointments live in the Bedrijfsvoering Aanwijzingen Register (BAR), and contractors are responsible for keeping their own appointment data current.

Personnel screening is heavy: a VOG (background check) and full screening are required before starting, and self-employed contractors are not accepted for Werkverantwoordelijke roles. This creates a formal boundary: contractors have credentials and appointments recorded in the operator's systems, so their access is auditable and revocable.

For metering companies specifically, the access model is more restricted: they get access to meter equipment and metering data, with no authority to operate assets. Their role is specific and bounded.

## Work authorisation and scheduling

Contractors operating under framework orders (raamopdrachten) submit a weekly plan of works to the central meldpunt (trouble desk). The IV sets annually which framework orders a given contractor may issue at all (contractor information sheet). This creates a scheduling hierarchy: the IV approves what categories of work a contractor can do, the contractor submits weekly plans of what they will do, and the meldpunt coordinates and approves the specific work.

For planned work, a werkplan (work plan) defines what will be done and a bedieningsplan (switching plan) defines what switching operations are required to isolate the work area safely. Both are created digitally in the Bedrijfsvoering application before work begins. Customer-facing notice of a planned interruption runs on a minimum lead time of three days, per Stedin's [planned-maintenance guidance](https://www.stedin.net/storing-en-onderhoud/gepland-onderhoud).

For emergency work, a contractor is called via the storingsdienst (fault-duty) rota and responds within specified time windows, typically one hour, under Stedin's [BSS BEI safety supplement](https://www.stedin.net/-/media/project/online/files/zakelijk/branches/aannemers-en-projectontwikkelaars/veilig-werken/stedin-bss-bei.pdf). Emergency work is documented after the fact in work orders and incident reports.

Planned and emergency work leave different evidence trails: planned work carries advance notice, documented scope and pre-approval; emergency work is reactive and documented in logs after completion.

## Work orders and completion records

Contractor work is tracked through work orders in the asset-management system (IBM Maximo). A work order specifies the asset, the work to be done, the contractor assigned, the planned start and end dates, and the completion criteria. When work is completed, the contractor documents the actual work performed: what was done, any deviations from plan, test results if applicable, and sign-off by the Werkverantwoordelijke.

For relay commissioning or settings changes, the as-found-and-as-left records are critical: before maintenance, the technician documents the current state; after maintenance, the final state. These records are stored in Maximo and in the engineering tool databases (DIGSI for SIPROTEC relays, AcSELerator for SEL relays).

Maintenance records create an operational audit trail: what work was authorised, who performed it, when, what the results were, and whether the work matched the plan. Discrepancies between the work plan and the completion record (undocumented changes, scope creep, missing sign-offs) are evidence of control failure or deviation.

## Evidence trails contractors create

A contractor's work touches most of the estate's evidence at once. Connecting an engineering laptop to a relay leaves a
connection log on the device and in the network record; a settings upload through DIGSI or AcSELerator logs the user,
the values written and the time, doubled by the relay's own log; commissioning generates Omicron test reports; every job
carries a Maximo work order with its authorisation and sign-off; site visits leave badge-reader and switching-log
entries in Bedrijfsvoering. The breadth is the point. One contractor's shift can write to the workstation logs, the
relay, Maximo, the badge system and the switching log together, so their actions are both heavily evidenced and, to an
impersonator, a rich thing to hide behind.

## A distributed, mobile workforce

Because contractors do so much of the field work, a large portion of the operational evidence is created by people who are not employees. Their access is managed through credentials and appointments recorded in the operator's systems, but they work under contract and rotation. A contractor working on relays here might work for three different utilities in a given week, a workforce that is distributed, mobile, and often more specialised in specific technical areas than the operator's own staff.

## The contractor evidence question

Much of what would otherwise read as anomalous is just contractor work. An engineering workstation reaching a relay at
02:00 is usually emergency maintenance under the fault-duty rota; a settings file on a laptop that differs from the relay
is more often one prepared for testing before upload; test records with no work order behind them are the mark of
informal commissioning checks; a work order whose completion date trails the relay's settings timestamp most likely means
the job was done one day and logged in Maximo the next. Each is a legitimate trail that can pass for compromise at a glance. What
separates the two is the ordinary triple: whether the work was authorised, whether it matches the scope in the work
plan, and whether the completion record matches what actually changed.

That resemblance is also what makes contractor access a high-value target. A contractor holds legitimate access to
several systems, can account for connections and changes, and works under looser supervision than internal staff, so an
attacker wearing a contractor's credentials moves in a way the logs read as routine.

*Last updated: 14 July 2026*
