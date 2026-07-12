# Metre data semantics

Stedin's smart-meter base (Landis+Gyr, Iskraemeco, Kaifa, Sagemcom) reports consumption data via CDMA to the metering
platform. The meters record cumulative kilowatt-hours consumed, and the platform aggregates readings across customers,
feeders, and the entire network. Consumption patterns, anomalies, and the relationship between meter readings and
network measurements form the observable layer for metering integrity.

## Normal consumption patterns and baselines

The meters record consumption continuously. A residential meter in a typical Dutch home consumes 8-15 kWh per day
in winter (heating load) and 3-8 kWh per day in summer. An office building shows a sharp daytime peak (08:00-18:00) and
minimal nighttime consumption. A supermarket shows steady baseline load (refrigeration, lighting) plus daily peaks
around shopping hours. Industrial customers show load that correlates with production schedules. These patterns are
consistent and repeatable year-over-year, with seasonal variation and day-of-week variation (weekday loads differ from
weekend loads).

Stedin's metering platform aggregates readings at multiple levels: individual meter, district, feeder, substation, and
network-wide. The aggregated consumption shows the sum of all customer consumption downstream of a measurement point. A
feeder's total consumption at 15:00 matches the sum of all meter readings downstream of that feeder. When
consumption is compared across aggregation levels, the pyramid balances: the sum of all customers equals the sum
of all meters, which equals the sum of all feeders, which equals the network-wide total.

The baseline for each meter, district, feeder, and substation is constructed from historical data. The expected
consumption pattern for a Tuesday afternoon in March is known with reasonable precision. When real-time data arrives, it
is compared against the baseline. A meter that normally shows 2 kW steady load suddenly dropping to zero is anomalous. A
feeder that normally shows 50 MW at midday suddenly showing 30 MW stands out. A network-wide consumption that diverges
from the expected pattern by more than a few per cent points the same way. These anomalies can indicate equipment failure,
customer usage change, meter malfunction, or tampering.

## Meter-to-network measurement alignment

Stedin's distribution network has multiple independent measurement sources. Smart meters measure consumption at
individual customer points, aggregating to feeders and substations. RTUs at substations measure total feeder consumption
via CT (current transformer) inputs and report to the SCADA and historian. These two independent measurement sources (
meters and RTUs) show alignment. The sum of all meter readings on a feeder approximately equals the RTU's
measurement of total feeder consumption at the feeder's source point.

When meter readings and RTU measurements diverge, the divergence is a forensic signature. If individual meters report
500 kWh consumed on a feeder but the RTU reports 600 kWh flowed into that feeder from the source, there is a gap (100
kWh of energy unaccounted for). The gap could indicate: a meter is under-reporting (a tampered or malfunctioning meter
is not recording all consumption), energy theft (a customer bypassing their meter), a non-metered customer consuming
energy, or the RTU's measurement is wrong. Conversely, if meters report 600 kWh but the RTU reports 500 kWh, the meters
are over-reporting or the RTU's measurement is wrong.

Normal alignment is within a few per cent (the difference between what meters report and what RTUs measure for the same
feeder is typically less than 3-5 per cent, accounting for technical losses in the network and metering uncertainty).
Larger divergences require investigation. A feeder where meters consistently report 10 per cent more consumption than the
RTU measures is suspicious and could indicate systematic meter over-reporting or RTU under-reporting. A specific
customer whose meter reports 20 per cent more consumption than their RTU-measured usage would suggest is anomalous.

## Consumption profile anomalies

Individual customer consumption profiles develop over time and become predictable. A residential customer's profile
shows morning and evening peaks, a daytime trough, and very low nighttime consumption. If that customer's profile
suddenly flattens (no daily variation, steady constant consumption throughout the day and night), that is anomalous. The
anomaly could indicate the meter is falsifying data, or the customer's actual usage changed dramatically.

Geographic patterns also appear. All meters on a specific feeder show seasonal variation that tracks the external
temperature (higher consumption in winter, lower in summer). If one feeder suddenly shows inverted seasonality (highest
consumption in summer), that feeder's meters are anomalous. If all feeders in a specific district show suspicious round
numbers (all customers reporting exactly 1000 Wh consumed, with no variation), that is evidence of synthetic data.

Consumption anomalies that correlate with events are informative. If a feeder's total consumption suddenly drops by 50
per cent at a specific instant, that could indicate: a large customer disconnected, a protection relay tripped the feeder
off (which would be visible in SCADA logs), energy theft was suddenly removed, or the meters are falsifying data.
Comparing the consumption drop against the SCADA event log shows whether a relay trip explains the drop. If there is no
relay trip and no disconnection in SCADA logs, the drop is unexplained.

## Meter tampering signatures

Meter tampering can take several forms, each with distinct signatures. A meter can be physically bypassed (a circuit
shunt or reverse-polarity connection is installed so the meter does not record the consumed energy). The visible
signature is that the meter's consumption does not match the customer's actual load (which can be estimated from other
sources like billing complaints or electricity-company inspection) or the meter reading stays constant when the customer
reports consuming power.

A meter can be remotely modified if it accepts remote commands via CDMA. The signature of remote tampering is that the
meter's consumption value suddenly resets or jumps without a corresponding disconnection-reconnection event. A meter reading that goes backward (consumption decreases instead of
increasing) is an obvious signature, as meters are designed to record cumulative consumption only.

A meter can be swapped. A tampered or non-reporting meter is physically replaced with a different meter that reports
artificially low consumption. The signature is a discontinuity in the meter's serial number or an abrupt change in the
consumption profile at the instant of meter replacement. If a meter ID suddenly changes and the consumption history
resets, that indicates a meter replacement. The question is whether the replacement was documented (a work order
authorises the replacement) or unauthorised.

A meter's reported consumption can be altered during transmission or at the platform. If the meter correctly records and
reports 1000 Wh, but the metering platform receives 500 Wh, the data was modified in transit or at the platform. The
signature is a divergence between what the meter transmitted (visible in Utility Connect's CDMA logs if available) and
what the platform recorded. If the platform's audit log shows the value was edited (who edited it, when, what the
old value was), that is the signature of manual tampering.

## Non-technical losses and energy theft

Stedin recognises several classes of electricity loss. Technical losses are expected: electricity dissipates as heat in
the distribution network's conductors, transformers have inherent losses, and metering has inherent uncertainty.
Non-technical losses are energy that is consumed but not properly metered or billed, including energy theft, metering
errors, and unauthorised connections.

Non-technical losses are estimated as the gap between the total energy input to a region (measured by the wholesale
market) and the total metered consumption (sum of all meter readings). When non-technical losses spike above the
expected baseline, investigation is warranted. A district that normally shows 2 per cent loss suddenly showing 8 per cent
loss indicates either a new systematic metering problem, energy theft, or new unauthorised load.

Individual meters or customers can also be outliers. If a specific customer shows a consumption that is substantially
lower than their historical average and lower than structurally similar customers in the same area, they may be
bypassing their meter. If a customer shows zero consumption (a meter reading that does not change) despite active load
visible at the property (electrical service lines present, customer still occupied), the meter is likely tampered.
Identifying such outliers requires statistical analysis, but the signatures are clear when found.

## Regulatory and billing applications

Stedin's metering data flows to Netbeheer Nederland for the national energy balance and to billing systems for customer
accounts. The data also flows to regulators who verify that metering is accurate. When metering data is disputed (a
customer claims they were over-billed, or a regulator questions Stedin's reported network losses), the meter readings
are the source of evidence.

Stedin has been involved in metering disputes with the ACM (Dutch energy regulator). In one [dispute over meter
readings](https://www.acm.nl/nl/publicaties/geschilbesluiten-consumenten-stedin-over-meterstanden), it was Stedin's own
logbook, the physical record of repeated in-person attempts to read a meter, that proved decisive: the ACM accepted it
as evidence that Stedin had met its reading obligation and ruled the complaint unfounded. The handwritten record carried
the point the digital platform alone could not.

The metering platform's audit logs (who accessed the data, when, and what changes were made) are forensic sources for
understanding whether data was modified. If the audit log shows that a technician accessed meter XYZ's record and
manually edited the consumption value from 1000 Wh to 800 Wh without a corresponding technical reason, that is evidence
of tampering. Conversely, if the audit log is complete and shows no such edits, the data is more trustworthy.

## Consumption forecasting and anomaly detection

Stedin's metering platform can apply statistical models to detect anomalies. A model predicts the expected consumption
for each customer based on historical data, weather, calendar (weekday/weekend), and seasonal factors. When real-time
meter readings arrive, they are compared against the prediction. Readings that deviate significantly from the prediction
are flagged for investigation.

This approach is effective for detecting sudden changes (a meter that stops reporting due to malfunction, or a customer
who suddenly increases consumption due to new equipment). It is less effective for detecting gradual systematic
tampering (a meter that slowly under-reports by 1 per cent per day). The strength of anomaly detection is that it is
automated and scalable (thousands of customers can be monitored continuously). The limitation is that it generates false
positives (legitimate consumption changes trigger alerts) and requires human review to distinguish legitimate anomalies
from tampering.

For forensic analysis, anomaly detection can provide initial leads. If a district shows unusually high consumption that
does not match expectations, that is a pointer to investigate. If anomalies cluster geographically (all meters in one
substation district are anomalous), that suggests a systematic problem at that location. If anomalies correlate
temporally (all anomalies occur at night or all occur on weekends), that suggests a pattern related to behavioural or
operational factors.

*Last updated: 12 July 2026*
