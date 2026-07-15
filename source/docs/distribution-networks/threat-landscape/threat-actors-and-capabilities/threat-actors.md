# Threat actors and capabilities

Threat actors range from state services to criminals to insiders. What each can realistically accomplish is bounded by
the operating constraints, regulatory environment, and technical boundaries of the network.

However elegant in theory, a threat is not credible if it needs simultaneous actions that regulatory safety interlocks
prevent, a maintenance window that does not exist in the operating calendar, or concurrent access the organisational
structure rules out.

## State actors

State actors possess capability and patience to develop supply-chain access, reverse-engineer closed systems, or
maintain persistence over months. Their operational objective is typically either to degrade service on demand (leaving
a network capable of running but able to be stopped abruptly), or to establish long-term surveillance of how a network
actually behaves at scale so they can predict the effect of an attack without executing one.

Supply-chain compromise is a natural entry point for a state actor against a distribution network. The operator, for instance,
procured SCADA software (e-terracontrol for SCADA/EMS, e-terra distribution for DMS), relay engineering tools (DIGSI 5
for SIPROTEC relays, AcSELerator QuickSet for SEL relays), a network model and asset register (Smallworld GIS with
Lovion integration), an asset-management platform (IBM Maximo), a historian, protection relays (inferred as SIPROTEC 5 
and SEL-451, not independently confirmed yet), and a metering infrastructure (Landis+Gyr, Iskraemeco, Kaifa, and Sagemcom
meters over Utility Connect's private CDMA network). 

Each of these is a procurement chain with
software updates, maintenance windows, and configuration tools that move through both internet and air-gapped
engineering workstations. A state actor inserting a conditional payload into a relay firmware update or SCADA
configuration tool would sit passively until activated. The operational asymmetry is that discovering such compromise
after the fact requires comparing the deployed configuration against the vendor baseline, which is labour-intensive and
unlikely to happen during ordinary operations. A persistent, stealthy compromise could remain
undetected for years.

Field devices in medium-voltage stations (Smart Grid Terminals with RTUs capable of both measurement and switching,
communicating over IEC 60870-5-104 protocols now transitioning to IEC 61850) offer another vector. State actors have
reprogrammed or bricked field devices in live grid intrusions, as in the 
[2015 and 2016 attacks on the Ukrainian grid](https://blue.tymyrddin.dev/docs/ot/incidents/ukraine-grid). A modified 
RTU could accept legitimate commands and report correct state for months, then execute conditional logic during a 
specified event (such as a frequency deviation past a threshold, a commanded switching sequence that matches a pattern, 
or at a prespecified date). The device would then cause field equipment to behave outside its normal operating 
envelope, whether by forcing a switchpoint open against protective relay commands, disabling protection thresholds, or 
causing a transformer to remain energised when it should be isolated.

Detection of such compromise depends on continuous integrity checking of the baseline configuration. The operator, running
several hundred RTUs across the network, can compare each against a known-good firmware snapshot, but only if the
comparison routine is resilient to supply-chain compromise itself (if the integrity checker is compromised, it will
return pass). More realistically, detection happens when the compromise manifests an observable anomaly: a relay
refusing a legitimate command, an RTU reporting state that contradicts what field equipment is actually doing, or a
protection setting that diverges from its online-versus-offline baseline.

## Criminal actors

Criminal motivation differs from state actors: criminals work toward financial extraction and operate under pressure to
realise value quickly. Direct attacks on a distribution network (denial of service, ransomware against SCADA) generate
immediate visibility and response from emergency services and regulators, so they are high-risk and low-reward, except 
when negotiating payment during an active outage. 

More realistic criminal scenarios either target high-value customers (industrial facilities, data centres, hospitals) 
who will pay ransom, or target the metering infrastructure for revenue fraud (altering meter readings, disabling 
consumption reporting to steal electricity).

Ransomware against the IT layer is a viable criminal attack. The operator probably maintains SAP for finance and supply-chain
management, Azure for cloud applications, and an engineering environment for SCADA and GIS. If a criminal establishes
persistence in the IT network through credential compromise or supply-chain compromise, they can encrypt the IT layer 
(ERP, CRM, procurement, work-management tools) and demand payment. 

An outage of the IT layer is severe for the operator, but is not a direct cyber-physical attack on the distribution 
network itself. The storingsdienst and field teams can continue emergency restoration and everyday switching 
through the offline Bedrijfsvoering appointment system and manual procedures, though efficiency drops and the window 
for planned work is reduced. A criminal extorting IT-layer outages is exploiting the difficulty operators face in 
rapidly rebuilding SAP and Azure, not the physical grid's resilience.

Metering fraud is another high-value vector. Millions of meters (Landis+Gyr, Iskraemeco, Kaifa,
Sagemcom) run over CDMA networks operated by Utility Connect. A criminal can reprogram a meter to under-report consumption.
An attacker could intercept and modify consumption data in flight to the billing system, stealing electricity or
selling the capability to industrial customers. Metering systems carry authentication and integrity checks, but an
attacker who compromises the provisioning infrastructure or the encoding key for a device family could push modified
firmware to a large population at once. Metering fraud looks like meter malfunction. An operator may attribute
high error rates to sensor ageing rather than attack.

## Insider threats

In the portrait, insider threats cluster around access and authority. The workforce runs to roughly 4,500 
internal staff and 1,000 contractors, with responsibility for physical network maintenance, system operation, and 
engineering. A malicious insider could be an operator with SCADA access to e-terracontrol, an engineer with Smallworld 
network-model edit authority, a technician with physical access to substations, or a contractor with temporary 
appointment authority in the Bedrijfsvoering application.

The insider threat surface exists because of how the organisation staffs its operations. Underneath sits a structural 
shortage of qualified personnel: a projected 600-fitter gap by 2027, with roughly one in five team members new and 
cycling through a familiarisation window. This compression of the talent pool concentrates access and authority in a 
smaller population. 
The operator leans on contractors for a part of its combined headcount, which extends insider-threat
risk into the contractor supply chain, given [the workforce structure](../../operating-context/staffing-and-capability/staffing-realities.md)
and [how contractors are vetted and managed](../../operating-context/operations-and-cadence/contractor-management.md).

Insider actions that damage the network leave forensic traces. Configuration changes show in IBM Maximo's audit
trail. SCADA commands show in e-terracontrol's control room log. Switching operations create werkplan and bedieningsplan
records signed in Bedrijfsvoering. Relay settings divergence surfaces in baseline comparisons.

A skilled insider could hide an act by constructing it as legitimate maintenance or operator error: run a planned outage
that authorises substation access, then make an unauthorised modification during that window that matches planned scope.
But only if they understand the audit trail design and the specific maintenance workflow.

Disabling relay thresholds on a SIPROTEC 5 or SEL-451 takes several conditions at once: access through a legitimate
maintenance window, knowledge of the engineering tool (DIGSI 5 or AcSELerator QuickSet) and the relay configuration, a
change made without observation, avoidance of the online-versus-offline comparison that flags divergence, and no trace
left in settings version history or the relay event log. Most of those conditions are hard to meet simultaneously.

Exfiltration of network data is lower-risk for an insider. An operator or engineer could photograph or copy
network diagrams, substation inventories, relay settings, or customer connection records and remove them from the site.
Such exfiltration would be unobserved unless the operator has egress monitoring or the insider is caught in the 
physical act.

An insider who copies the entire Smallworld network model or the complete asset register from IBM Maximo could hand that
data to a state actor, who would then have a precise map of the network topology, voltage levels, protection
settings on SIPROTEC and SEL relays, and asset replacement ages. That information enables more precise attacks elsewhere
in the supply chain and helps an attacker model what damage a particular compromise could cause.

## Capability constraints

Operational reality imposes hard constraints on what threats can actually execute at scale. The portrait's 
network security does not rest on keeping SCADA equipment air-gapped (modern networks integrate e-terracontrol SCADA 
with Smallworld GIS and IT through APIs and cloud platforms), but on access control, network segmentation, and integrity 
checking. In e-terracontrol, IT releases probably run quarterly and SCADA cycles longer, but both 
move through the same change-control and testing gate. Safety interlocks are specific and testable: a SIPROTEC or SEL 
relay will not trip below a configured threshold, a switchpoint will not energise a disconnected load, a transformer 
will not remain energised after a fault. An attacker trying to violate those interlocks needs to either compromise the 
logic that enforces them or physically command the field device to disobey.

The staffing constraint cuts both ways. The same shortage that thins the workforce concentrates specialised
knowledge (switching authority with the Schakelbevoegd flag, relay commissioning with DIGSI 5 and AcSELerator
QuickSet, e-terracontrol configuration) in a small population. That concentration makes those roles high-value targets 
for insider recruitment or credential theft. At the same time, the shortage means the organisation cannot easily audit 
all work: the contractor reliance is structural, the out-of-hours rota is thin, and the certification pipeline for 
qualified personnel is a hard bottleneck.

A malicious insider who understands the specific gap between what the system is supposed to do and what it actually
does (perhaps because they helped build or maintain it) has time and knowledge advantages.

The maintenance-window cadence is visible and published. Maintenance is announced at least three days in advance for
routine work, and longer for major projects, following [the full maintenance announcement and change
cadence](../../operating-context/operations-and-cadence/operational-procedures-and-change.md). An attacker cannot manufacture a maintenance window, but can plan an attack around them. Similarly,
the appointment system (Bedrijfsvoering application with per-person Schakelbevoegd flags) is auditable and leaves a
trace in the BAR register. An attacker impersonating a qualified person would need to compromise that identity in the
system or forge an appointment, and both approaches leave evidence.

## Gap between theory and practice

The theoretical attack: disable protection relays (remove safeguards), corrupt the network model (send wrong commands),
command field devices to violate safe states. All coordinated to cascade across multiple feeders. A sophisticated
attacker with months of preparation might execute it in theory.

    THEORY: The cascade attack
    ─────────────────────────────────────────

    1. Disable a feeder relay        2. A fault occurs on Feeder A

       Raise its pickup beyond          The Feeder A relay stays idle, so the
       any real fault, or corrupt       fault is not cleared locally.
       the network model.

    3. Backup protection still clears it, late

       The upstream incomer relay picks the fault up and clears it after its
       grading delay, so clearance is late rather than absent. While the
       fault burns, load transfers onto Feeder B, and if Feeder B was already
       near its limit the shift can push it into overload and trip its own
       relay. A single disabled relay slows clearance and stresses its
       neighbours; it does not leave a fault burning unattended.

In practice, an attacker faces three hard constraints.

First, most of the system is not internet-facing: field devices rely on specialised protocols (IEC 60870-5-104, 
transitioning to IEC 61850) that are not directly accessible from the internet. Access requires either supply-chain 
compromise (modifying a device during manufacture or during a maintenance window), network compromise (reaching the 
network segment where the devices sit), or physical access to the device itself.

Second, the system is probably instrumented for forensics, with SIPROTEC and SEL relay settings versioned,
e-terracontrol SCADA commands logged with operator identity, switching operations generating signed werkplan records
in Bedrijfsvoering, and asset changes flowing through IBM Maximo's audit trail. An attack that uses legitimate 
interfaces (connecting with valid credentials, using DIGSI 5 or AcSELerator QuickSet, following the normal workflow) 
will be logged. An attack that bypasses interfaces (directly programming a relay, forging a command) requires either 
physical access or a supply-chain compromise that has already happened.

Third, the operator most likely also has institutional knowledge of what the network should look like: the current relay 
settings on SIPROTEC 5 and SEL-451 units, the baseline network model in Smallworld, the ordinary switching patterns. 
An attacker's changes surface as divergence from those baselines, and there is time to detect and respond because 
most failures of the utility network are not instantaneous; they cascade over seconds to minutes. A relay that trips 
unexpectedly will cause an outage, and the outage will be noticed immediately and will trigger incident investigation.

The most realistic attack surface is not network equipment itself but the processes that manage it:
compromising the engineering workstations where SIPROTEC and SEL relay configurations are built using DIGSI 5 and
AcSELerator QuickSet, compromising a Smallworld network model so that e-terracontrol control-room operators send the
wrong commands, or compromising a certification system so that unqualified personnel can gain access during
maintenance. These attacks work because they exploit legitimate processes that are hard to continuously
audit. An engineer connects DIGSI 5 to a relay to update settings: is this a legitimate update or a supply-chain
compromise? A contractor requests access to a substation: have their credentials been checked against the current
BAR and are their Schakelbevoegd flags current in Bedrijfsvoering? These are not theoretical questions; they are
questions operators answer tens of times a day. The gap between theory and practice is the gap between an
elegantly coordinated attack and the difficulty of executing that attack against an organisation with
procedures, history, and institutional memory.

*Last updated: 13 July 2026*
