# Resources

## Protocol libraries

| Library                                                     | Protocol                   | Notes                                                                           |
|:------------------------------------------------------------|:---------------------------|:--------------------------------------------------------------------------------|
| [libiec61850](https://github.com/mz-automation/libiec61850) | IEC 61850 (GOOSE, SV, MMS) | C library with Python bindings. The practical tool for any IEC 61850 challenge. |
| [gurux-dlms](https://github.com/Gurux/gurux.dlms.java)      | DLMS/COSEM                 | Java; Python port available. Client and server implementations.                 |
| [OpenDNP3](https://github.com/automatak/dnp3)               | DNP3                       | See also the OT/ICS section.                                                    |
| [pyc37118](https://github.com/achance6/pyc37118)            | IEEE C37.118.2             | Python PMU simulator and parser.                                                |

## Simulation

| Tool                                             | Role                                                                     |
|:-------------------------------------------------|:-------------------------------------------------------------------------|
| [OpenDSS](https://www.epri.com/pages/sa/opendss) | Distribution system simulation. Python interface via `py_dss_interface`. |
| [pandapower](https://www.pandapower.org/)        | Power systems analysis in Python. Grid topology modelling.               |
| [GridLab-D](https://www.gridlabd.org/)           | Distribution grid simulation. Steeper learning curve, higher fidelity.   |

## Gap

None of the existing simulation environments (power-and-light-sim, ics-simlab) implement IEC 61850 or
DLMS/COSEM. A smart grid simulator is a prerequisite for building any of the challenges in this section.
The candidates for that work are libiec61850 for the substation layer and gurux-dlms for the metering layer,
built on top of a grid model from OpenDSS or pandapower.

That work does not exist yet. Platform packaging pages for this section follow once it does.
