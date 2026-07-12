# Incident analysis and forensics

Incident investigation and forensic analysis form two halves of a single picture. The forensic literature tests which engineering traces actually survive and can be recovered, whilst incident reports document the material traces that emerge when systems fail. Together they show how to distinguish malicious change from legitimate engineering through the residue both leave behind.

## Forensic methods

### The framing source

[NIST's OT DFIR framework](https://nvlpubs.nist.gov/nistpubs/ir/2022/NIST.IR.8428.pdf) (NISTIR 8428) is the neutral backbone. It categorises forensic data and, notably, splits the tooling into IT-based tools and OT-based tools that access the PLC's and equipment's software, firmware and configuration directly, and it lists as priority data exactly the engineering residue rather than only malware: security logs, project files, network traffic and HMI interactions. That priority list is the reframe made explicit: the project file and the configuration are first-class evidence, not context around the malware.

### Project files

The sharpest example is Microsoft's open-source ICS Forensics framework, [ICSpector](https://github.com/microsoft/ics-forensics-tools), which extracts PLC project configuration and code from controllers so the project running on the PLC can be compared against the copy held on the engineering workstation. That method exists only because engineering leaves two comparable traces, the running project and the workstation copy, and a divergence between them is the signature of a change. As a Python framework analysing controller metadata and project files, it stands as a reference for extraction-layer design.

### Upload logs

The survey literature is candid about where the upload trace lives and where it fails. A [survey of SCADA forensics](https://www.osti.gov/servlets/purl/1493135) notes that the Siemens PLC logging system records detailed event activity usable for investigation, but only under two conditions: the change is made through the proprietary engineering software (TIA Portal), and the workstation itself is not compromised. The upload of a program is logged, but the log is tool-mediated, so an out-of-band change bypasses it. The trace of legitimate engineering exists precisely because legitimate engineering goes through the tool, which is also its limit as evidence.

### Firmware history

PLC memory forensics is where firmware version and control-logic history are recovered. The [memory-analysis work](https://www.sciencedirect.com/science/article/pii/S2666281722000087) sets out to detect malicious firmware, injected or modified control logic and I/O manipulation, but the same extraction recovers the legitimate firmware version and logic baseline, and the papers are frank that heterogeneous hardware and proprietary firmware make this per-model and laborious. Firmware history is recoverable but not uniform. The engineering trace at this layer is device-specific and often requires reverse engineering rather than a clean log.

### Relay configuration versions

The settings artefacts from relay testing, the XRIO settings files, the as-found and as-left reports, are the engineering-side record; the DFIR side is recovering the settings actually resident on the device and comparing them to that baseline. The DIGSI project for a SIPROTEC relay and the settings database for an SEL relay are dated, versioned project files in the same sense as a PLC project, so the same online-versus-offline comparison logic applies: the configuration version on the relay against the engineering copy is the evidence that a settings change occurred.

### Serial communication logs

The protocol and I/O layer is the thinnest and the most actively researched, because industrial devices frequently lack forensic-compliant logging at all. One study repurposes a PLC as a non-intrusive [forensic I/O recorder](https://dl.acm.org/doi/fullHtml/10.1145/3600160.3605059) to log I/O changes in a forensically compliant manner, motivated by that very gap. Serial and protocol captures (S7comm, Modbus, DNP3, IEC 60870-5-104) and the logs of serial-to-ethernet converters are the trace here, the same converters that were bricked in the Ukraine 2015 case to destroy exactly this evidence.

### The finding that runs through the literature

The consistent message is a gap between what should be recoverable and what is. The papers repeatedly note that ICS devices lack forensic-grade logging, that engineering traces are tool-mediated and device-heterogeneous, and that much of the residue lives on the engineering workstation rather than the device. The survey leans on van der Knijff of the Netherlands Forensic Institute, whose control-systems-forensics work is a Dutch primary source on precisely this difference, and the field also cites the German BSI IT-Forensik guidance, so the European DFIR literature is well represented.

### DFIR and standards as complementary halves

DFIR and standards are complementary halves of the same picture. The standard is the a priori taxonomy of every observable a conformant system could emit. The DFIR literature is the empirical test of which of those observables actually persists and can be recovered after the fact. The gap between the two, the events the standard defines but the device does not durably log, is not a footnote; it is the substrate-versus-narrative distinction in operational form. The standard describes the intended record; the forensic paper measures the material trace that genuinely remains, and finds it thinner, more tool-dependent and more workstation-resident than the standard implies.

For Stedin concretely, this points the engineering-trace question at three places: the DIGSI and settings projects for its protection relays, the project and configuration on its MV-station RTUs and gateways, and the configuration and logs of its e-terra control layer. The expectation from the literature is that the richest residue sits on the engineering workstations and in the tool logs rather than in forensic-grade on-device logging, consistently less than the paperwork promises.

## Incident traces

### Outage investigations

The strongest Dutch exemplar is the [2 September 2022 Flevoland event](https://www.tennet.eu/nl/nieuws/combinatie-van-factoren-veroorzaakte-stroomstoring-flevoland), investigated independently by DNV for TenneT and Liander with the ACM involved from the outset. The forensic layer shows staff in Dronten and Lelystad operating a switch simultaneously, a short circuit following, a back-up provision failing so it took over four minutes to clear, an overhead line overloading, smouldering and sagging onto a railway catenary, and relay cabinets and cable needing replacement.

The internationally canonical one is the [GB 9 August 2019 ESO technical report](https://www.ofgem.gov.uk/sites/default/files/docs/2019/09/eso_technical_report_-_final.pdf), hosted by the regulator, which reconstructs a lightning strike to a second-by-second sequence: a wind farm de-loading 737 MW, a steam turbine tripping 244 MW, then one gas turbine tripping automatically on steam pressure and a second tripped manually by operational staff, vector-shift and rate-of-change-of-frequency protection disconnecting embedded generation, under-frequency trips at 49 Hz, low-frequency demand disconnection shedding around a gigawatt, and restoration in four minutes forty-two seconds. It even names the trigger as a discrepancy on three independent safety-critical speed-measurement signals.

### Regulator reports

For Stedin specifically, the ACM dispute decisions are this genre in miniature: the meter-reading disputes turn on Stedin's own logbook showing repeated physical meter-read attempts, and the transport-capacity decision turns on whether Stedin examined congestion management before refusing, cited against a specific Netcode article. The GB event also generated a separate [government review through the E3C committee](https://assets.publishing.service.gov.uk/government/uploads/system/uploads/attachment_data/file/855767/e3c-gb-power-disruption-9-august-2019-final-report.pdf), sitting above the operator's own technical report.

### Post-incident reviews

The richest current example is the [ENTSO-E panel investigation of the 28 April 2025 Iberian blackout](https://www.entsoe.eu/publications/blackout/28-april-2025-iberian-blackout/), a 49-member panel producing a factual report and a final report. The observable evidence is dense: a first generation-transformer trip near Granada milliseconds after 12:32:57 on an overvoltage protection, frequency falling below 48 Hz by 12:33:18, the France-Spain AC lines tripping at 12:33:21 and the HVDC link at 12:33:24, all reconstructed from data supplied by the Spanish, Portuguese and French operators and from SCADA measurements, with PV-inverter manufacturers' data showing inverters tripping on overvoltage. It also records that the Spanish operator ran a security assessment that morning and concluded no action was needed, which is the operator-noticed layer.

### Weather event reports

TenneT publishes a [running operational log of transmission faults](https://www.tennet.eu/nl/ons-hoogspanningsnet/stroomstoringen) that is remarkable for its granularity. Entries carry timestamps, the specific connection, whether a protection relay operated correctly, the megawatts lost, and voltage-dip records with residual-voltage percentages and durations in hundredths of a second, together with probable causes ranging from a short circuit in a GIS coupling field to birds nesting in a mast with a piece of barbed wire. There is also an older Dutch parliamentary study of the Haaksbergen weather-caused outage that works through network design, the N-1 criterion and mobile emergency-generator capacity.

### Annual reliability reports

The sector baseline is Netbeheer Nederland's [annual reliability report](https://www.netbeheernederland.nl/sites/default/files/2025-04/03.02._betrouwbaarheid_van_elektriciteitsnetten_in_nederland_-_resultaten_2024.pdf), which breaks results down by operator and by voltage level, so Stedin's own figures sit inside it. Stedin's own annual-report reliability chapter adds the causal breakdown, attributing a large share of faults to excavation damage and untraceable internal cable-and-joint defects, which is engineering-record evidence. TenneT publishes an annual security-of-supply monitor on top of that.

### Cyber incident write-ups

The Ukraine 2015 grid attack is the reference text. The [E-ISAC and SANS analysis](https://nsarchive.gwu.edu/sites/default/files/documents/3891751/SANS-and-Electricity-Information-Sharing-and.pdf) describes operators watching the HMI as breakers opened and closed without their input, an operator being logged out and locked out because the password had been changed, operators forced to manual mode, technicians dispatched to more than fifty substations, KillDisk wiping workstations, serial-to-ethernet converters bricked with malicious firmware, and a telephone denial-of-service flooding the call centre. The [INL CyOTE case study](https://cyote.inl.gov/content/uploads/24/2025/12/CyOTE-Case-Study_Ukraine-2015.pdf) formalises the observables by enumerating radmin logs reflecting unauthorised HMI inputs, packet captures of instructions sent to field controllers, and alarms from changes to the operational database or device configuration, showing which staff in engineering, OT, and IT could have observed each event.

### Reading the genre

The layers stack. At the bottom is a continuous operational log (TenneT's fault page, refreshed as events occur). Above it, single-incident forensics (Flevoland, GB 2019). Above that, the sector annual reliability report where individual operator figures live. Above that, cross-border panel reviews (ENTSO-E Iberia). And running alongside, cyber post-mortems that function as observable-evidence catalogues.

For Stedin, four examples fit the genre without being read this way: its figures inside the Netbeheer Nederland report, its own annual-report fault causes, the ACM dispute decisions describing its logbooks and Netcode compliance at incident level, and the SodM Zoetermeer investigation documenting gas-side engineering-record forensics after the explosion.

A manual states what a system is supposed to do; these documents record what it actually did, at the level of the relay that operated, the frequency that fell, the operator who switched to manual, the logbook that showed three attempts. Material trace of ordinary work becomes visible only when something forces it into the record. Observable evidence is not hidden in security documents; it sits in reliability reports and outage investigations that utilities publish as a matter of routine.

*Last updated: 11 July 2026*
