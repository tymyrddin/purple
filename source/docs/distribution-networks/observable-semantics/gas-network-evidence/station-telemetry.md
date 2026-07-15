# Gas station telemetry

The gas network's live record is thin next to the electricity net's, and it comes from the stations, not the street.
Pressure is handed down through a chain of them: from the national high-pressure transport into a gas receiving station
(where the gas is metered and already carries its odorant), through district stations that drop roughly 8 bar to the 100
or 30 mbar of the low-pressure net, to delivery stations for large users. Each station is instrumented; the low-pressure
mains between them are not. So the telemetered layer covers the nodes and leaves the reticulation to [periodic
inspection](integrity-and-safe-working.md).

## What a station measures

A pressure-reduction station carries inlet and outlet pressure, flow and volume (with temperature and pressure for the
conversion), the state of its regulators, and the state of its safety devices. A volume converter and datalogger at the
station holds the time-series and the digital-input events, a door contact, the position of the slam-shut valve, and
where the station is telemetered these forward over a mobile link to the [SCADA and control
centre](../control-and-command-execution/scada-observables.md) that also switches the electricity network.

The record is lighter than the electricity net's in two ways. Sampling is coarser: many stations run on battery and push
a periodic archive on a schedule rather than a dense live feed. And control is mostly watching: few gas valves are
remotely actuated, so a station reports far more than it is ever told to do. Normal, then, is an outlet pressure held
near its setpoint through the daily demand swing, a flow that tracks consumption, a closed door, and safety devices
sitting quiet.

## The safety chain, which needs no telemetry

The station's protection, a monitor regulator behind the active one, a slam-shut valve, and a relief, is autonomous:
mechanical and pneumatic, it acts on the gas itself and needs neither the control room nor a log to work. That
independence is what makes it evidence. The slam-shut is a latched device that stays shut until an engineer attends and
resets it, so a trip leaves a physical record, the closed valve and the reset report, whether or not the station was
telemetered; where the station reports, the same trip lands as a timestamped over- or under-pressure alarm and a loss of
supply downstream.

The quieter case is the one to hold onto. A monitor regulator taking over when the active regulator drifts holds the
pressure with little or no trace, a first line of defence that can save a station without announcing it. An absence of
alarms is not proof that nothing happened.

## Reading a pressure that moved

An outlet pressure off its setpoint has several readings before a hostile one. A slow drift is regulator wear; a step is
a setpoint change, authorised under a work order and a [bedieningsplan](../engineering-and-change/maintenance-window-signatures.md)
or not; a jump with no physical cause is a sensor fault or a reading interfered with. The safety chain answers
underneath all of them: a genuine excursion pushes the monitor to take over and, past the threshold, trips the
slam-shut, so a pressure the telemetry calls dangerous with no safety-device response, or a safety-device response with
no pressure excursion in the record, is the contradiction to chase.

A [configuration change](../configuration-and-versions/configuration-management.md) at the station, a regulator
setpoint, an alarm limit, a datalogger setting, reads like any other: legitimate with a work order and a window behind
it, unauthorised without.

## Cross-checks

The station's own account is set against records it does not produce. Its outlet pressure meets the inlet pressure of
the station below it on the same tier, so a pressure profile that no longer joins up localises a fault or a false
reading. The commercial metering at the receiving station and the delivery stations closes an energy balance across the
district, the gas equivalent of the meter-against-RTU check in [metre data
semantics](../measurements-and-data-records/metre-data-semantics.md): the gas entering a district accounts for the gas
metered out of it. And the physical state settles the rest, a slam-shut latched shut against a telemetry that logged no
alarm points to a missed or suppressed event; an alarm logged against a valve that never tripped points to a false
report.

## Telling a silent station apart

A telemetered station can go quiet for an innocent reason or a hostile one, and the gas net goes quiet often: battery
and mobile links drop, and a coarse periodic archive looks like a gap even when nothing is wrong. What separates a dead
modem from a silenced device is the company the silence keeps. A comms failure usually takes the neighbouring stations
on the same link with it and follows a normal last reading; a device switched off, of the kind the [Zoetermeer
investigation](../../operating-context/operations-and-cadence/operational-procedures-and-change.md) found when workers
disabled gas detection and pressed on, tends to fall silent alone, sometimes just after a reading worth not recording,
and comes back only when someone re-enables it. The safety chain is the backstop the record cannot silence: whatever the
telemetry does, the slam-shut's latched state is a physical fact an engineer reads off the valve.

The baseline here is quiet but gappy. Gas telemetry is sparse and coarse, comms drops are routine, and the safety
chain is silent by design, so absence is ordinary and proves little on its own, which is exactly why a silenced device
hides well and why the physical and periodic records carry more of the weight than they do on the electricity side.

*Last updated: 14 July 2026*
