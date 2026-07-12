# Public repositories

A public repository turns taxonomy concrete: it supplies the actual file, so the schema, naming conventions and tag vocabulary stop being described and start being inspectable, and it doubles as the corpus a parser or analysis pipeline needs. The value is structural, not the exposure of any deployment.

## Relay and substation configs, as inspectable structure

The richest single example is an [open-source IED implementation](https://github.com/robidev/iec61850_open_server) driven entirely by an SCL file. It instantiates IEDs, logical devices, logical nodes and services from the SCD, and ships a sample substation model containing a merging unit publishing sampled values, a protection IED whose overcurrent element (PTOC) drives a trip conditioner (PTRC) that issues a trip over GOOSE, a breaker IED (XCBR) subscribing to that GOOSE, and interlocking through the CILO logical node, with control configured as select-before-operate with enhanced security. That one repository exposes the entire structure of a real protection scheme, the logical-node naming, the GOOSE trip path, the interlocking and the control model, without any utility's confidential configuration.

The editor around it, [OpenSCD](https://github.com/openscd/open-scd), reads and writes those SCL files, and a separate academic project, [rapid61850](https://github.com/stevenblair/rapid61850), generates C from any SCD and exposes the full data model with its data types and functional constraints at runtime.

## The event vocabulary, made concrete

[libiec61850](https://github.com/mz-automation/libiec61850) is where the standards taxonomy stops being abstract. It implements MMS, GOOSE and SV, ships example ICD and SCD files and a log service with a SQLite driver, and its [configuration-file-format documentation](https://libiec61850.com/configuration-file-format/) spells out the model structure, including the trigger options as literal integer codes: 1 for data changed, 2 for quality changed, 4 for data update, with the functional-constraint and data-attribute-type enumerations referenced in the library's header files. Those trigger codes are exactly the event-emission taxonomy the standards define, now sitting in a publicly available config file.

The companion lib60870 does the same for IEC 60870-5-104, Stedin's present telecontrol protocol, so the point-and-cause-of-transmission structure of the layer Stedin actually runs is inspectable too.

## SCADA and HMI examples

On the SCADA and HMI side the open projects expose the config and screen structure: portable SCADA and IIoT gateways carrying IEC 61850, DNP3, IEC 60870-5-104 and ICCP point maps, and open HMI packages whose SVG-and-HTML screen definitions show how a mimic is structured. The synchrophasor world has openPDC for PMU stream structure. None of these is a specific utility's system; each is a worked example of the file format.

## The Dutch and European tie

A sister Dutch DSO has open-sourced its own field-device integration layer. Alliander's Grid eXchange Fabric, now under the Linux Foundation Energy umbrella, publishes protocol adapters including IEC 61850 and DLMS, so the structure of a Dutch DSO's device-integration platform is public. [CoMPAS](https://github.com/com-pas), a Linux Foundation Energy collaboration on open SCL tooling with RTE and Alliander among its members, makes the shape of the substation-configuration and device-integration artefacts visible in European public code. Stedin's own transition toward IEC 61850, layered over a CIM-based e-terra model, would produce SCL and CIM artefacts of the same structure.

## The corpus point, and the close

These repositories are the test corpus against which a config or project parser is developed. The sample SCDs from the open IED project, the ICDs bundled with libiec61850, the SCDs in rapid61850, and OpenPLC on the controller side provide ground truth for the substation-configuration layer. Each file allows a parser to be developed and validated against real structure before it meets a live deployment.

The repo exposes the form, schema and vocabulary, the material substrate of configuration, held separately from any one operator's content. What Stedin specifically ticked, enabled and retained stays in its own private configuration; everything around it, from the standard down to the example file, is legible in public.

*Last updated: 11 July 2026*
