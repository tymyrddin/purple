# Utility conference presentations

Conference material is often the single place where an architecture diagram, vendor name and a live screenshot appear together, because the point of the talk is to show the working system, protocol names, asset counts and all. A Dutch DSO is surprisingly forthcoming in these venues.

## Improving outage restoration

The clearest example reads like a conference paper written up in full. Stedin's [distribution-automation roll-out](https://www.pacw.org/full-scale-distribution-automation-roll-out-at-dutch-dso) is documented with real system detail: around 2.4 million customers and roughly 20,000 secondary substations, each a medium-voltage ring main unit with an MV/LV transformer and a low-voltage panel, plus thousands of customer stations with their own RMUs in Stedin's MV rings. It describes the programme started around 2014, remote-controlled RMUs and centrally-reported fault passage indicators installed to cut Customer Minutes Lost, and the crucial architecture detail: distribution-automation RTUs communicating over mobile links on IEC 60870-5-104 to SCADA for real-time control-room use, with non-real-time sensor data separated off into the historian. That single article documents the protocol, the real-time-versus-historian data split, and the supplier-selection method, including three suppliers providing demo equipment that Stedin technicians installed and disassembled against timed scoring.

## Predictive maintenance

Stedin's condition-monitoring work is presented openly. It applies Smart Cable Guard for online partial-discharge monitoring of medium-voltage underground cables, with methodology for detecting both present and developing defects inside the asset-management strategy. Stedin asset managers have presented predictive-analytics use cases across asset management, grid planning and investment, and operation and maintenance, drawing on smart meters, substations and the historian. Both name the data feeds.

## Digital substations

Stedin's Middelharnis II project is a green and digital gas-insulated substation, replacing SF6 with g3 and using low-power instrument transformers as sensors, combining high-, medium- and low-voltage data to optimise the system. The [asset-digitalisation programme with eSmart Systems](https://www.esmartsystems.com/case-studies/stedin/) is an image-based digital inventory of more than 22,000 secondary substations validated by AI models, producing a visual source of truth for over 10 million asset attributes, explicitly motivated by legacy systems, inconsistent data and documentation gaps.

## Reducing false alarms, relay replacement, ADMS deployment

False-alarm reduction and relay replacement are staple CIRED and PAC World subjects, and Stedin publishes at CIRED (its authors appear in the network-components and asset-management sessions). ADMS deployment carries the recurring gap: the distribution-automation paper describes the SCADA and historian split and the FPI-based outage detection, but the advanced-distribution-management product and relay-replacement programme do not appear by name. The control-room platform is the layer Stedin presents least specifically.

## The payoff and the screenshots

The strength of conference presentations lies in their focus on demonstrating operational improvement: they show the real interface, the real architecture and the real numbers rather than a sanitised abstraction. The distribution-automation write-up gives a protocol and a data-flow separation. The eSmart case study gives an asset count and an attribute count. A CIRED condition-monitoring paper gives the sensor and the analysis chain. Where screenshots appear, they show the actual SCADA mimic, the alarm list and the asset dashboard, revealing the fields, the naming conventions and sometimes the product.

The residue that persists across these presentations is the control-room platform: named nowhere specifically, yet described functionally everywhere.

*Last updated: 11 July 2026*
