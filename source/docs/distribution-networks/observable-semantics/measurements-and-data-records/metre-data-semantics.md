# Metre data semantics

The smart-meter base (Landis+Gyr, Iskraemeco, Kaifa, Sagemcom) reports consumption data via CDMA to the metering
platform. The meters record consumption as a cumulative register and as the interval readings they send to the platform, which
aggregates across customers, feeders, and the entire network. Consumption patterns, anomalies, and the relationship between meter readings and
network measurements form the observable layer for metering integrity.

## Normal consumption patterns and baselines

The meters record consumption continuously. A residential meter in a typical Dutch home consumes 8-15 kWh per day
in winter (shorter days and more lighting, plus a heat pump where fitted; Dutch homes mostly heat with gas) and 3-8 kWh per day in summer. An office building shows a sharp daytime peak (08:00-18:00) and
minimal nighttime consumption. A supermarket shows steady baseline load (refrigeration, lighting) plus daily peaks
around shopping hours. Industrial customers show load that correlates with production schedules. These patterns are
consistent and repeatable year-over-year, with seasonal variation and day-of-week variation (weekday loads differ from
weekend loads).

The metering platform aggregates readings at multiple levels: individual meter, district, feeder, substation, and
network-wide. The aggregated consumption shows the sum of all customer consumption downstream of a measurement point. A
feeder's total consumption at 15:00 matches the sum of all meter readings downstream of that feeder. When
consumption is compared across aggregation levels, the pyramid balances: the sum of all customers equals the sum
of all meters, which equals the sum of all feeders, which equals the network-wide total.

The baseline for each meter, district, feeder, and substation is constructed from historical data. The expected
consumption pattern for a Tuesday afternoon in March is known with reasonable precision. When real-time data arrives, it
is compared against the baseline. A meter that normally shows 2 kW steady load suddenly dropping to zero is anomalous. A
feeder that normally shows 5 MW at midday suddenly showing 3 MW stands out. A network-wide consumption that diverges
from the expected pattern by more than a few per cent points the same way. These anomalies can indicate equipment failure,
customer usage change, meter malfunction, or tampering.

## Meter-to-network measurement alignment

The distribution network has multiple independent measurement sources. Smart meters measure consumption at
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

Meter tampering can take several forms, each with distinct signatures. A physically bypassed meter (a shunt or reverse-polarity connection across it) reads a consumption that does not match
the customer's actual load, estimable from billing complaints or an inspection, or a reading that stays flat while the
customer draws power.

A meter modified over its CDMA command channel shows a consumption value that suddenly resets or jumps with no
disconnection-reconnection behind it, or, most obviously, a reading that runs backward, which a cumulative meter should
never do.

A swapped meter, one physically replaced with another reporting artificially low consumption, shows as a discontinuity
in the serial number or an abrupt profile change at the instant of replacement; a meter ID that changes and a history
that resets is a replacement, and the only question is whether a work order authorised it.

Consumption altered in transit or at the platform, the meter reports 1000 Wh but the platform records 500, shows as a
divergence between what the meter transmitted (in Utility Connect's CDMA logs, where available) and what the platform
stored, or as an edit in the platform's own audit log.

## Non-technical losses and energy theft

Not all the missing energy is a crime. Some loss is only physics, heat in the conductors, the transformers' own losses,
the slack in any meter, and it is expected. The rest, the non-technical loss, is energy used but not metered or billed:
theft, metering error, an unauthorised connection.

It is estimated as the gap between what the wholesale market says entered a region and what the meters say was drawn.
When that gap opens past its usual width, a district running its normal 2 per cent suddenly sitting at 8, it is a new
metering fault, theft, or fresh unauthorised load.

Individual meters or customers can also be outliers. If a specific customer shows a consumption that is substantially
lower than their historical average and lower than structurally similar customers in the same area, they may be
bypassing their meter. If a customer shows zero consumption (a meter reading that does not change) despite active load
visible at the property (electrical service lines present, customer still occupied), the meter is likely tampered.
Identifying such outliers requires statistical analysis, but the signatures are clear when found.

## Regulatory and billing applications

The metering data flows through the grid operators' central market data exchange into the national settlement that TenneT balances, and to billing systems for customer
accounts. The data also flows to regulators who verify that metering is accurate. When metering data is disputed (a
customer claims they were over-billed, or a regulator questions the reported network losses), the meter readings
are the source of evidence.

The operator has been involved in metering disputes with the ACM (Dutch energy regulator). In one [dispute over meter
readings](https://www.acm.nl/nl/publicaties/geschilbesluiten-consumenten-stedin-over-meterstanden), it was the operator's own
logbook, the physical record of repeated in-person attempts to read a meter, that proved decisive: the ACM accepted it
as evidence that the operator had met its reading obligation and ruled the complaint unfounded. The handwritten record carried
the point the digital platform alone could not.

The metering platform's audit logs (who accessed the data, when, and what changes were made) are forensic sources for
understanding whether data was modified. If the audit log shows that a technician accessed meter XYZ's record and
manually edited the consumption value from 1000 Wh to 800 Wh without a corresponding technical reason, that is evidence
of tampering. Conversely, if the audit log is complete and shows no such edits, the data is more trustworthy.

## Consumption forecasting and anomaly detection

The metering platform can apply statistical models to detect anomalies. A model predicts the expected consumption
for each customer based on historical data, weather, calendar (weekday/weekend), and seasonal factors. When real-time
meter readings arrive, they are compared against the prediction. Readings that deviate significantly from the prediction
are flagged for investigation.

It is good at the sudden things, a meter that stops reporting, a household whose use jumps when they buy an electric
car, and blind to the patient ones, the meter that shaves one per cent off a day. Running across thousands of customers
at once is its strength; the price is a steady stream of false positives, the ordinary changes of life tripping the
alert, which a person still has to sift from real tampering.

For forensic analysis, anomaly detection can provide initial leads. If a district shows unusually high consumption that
does not match expectations, that is a pointer to investigate. If anomalies cluster geographically (all meters in one
substation district are anomalous), that suggests a systematic problem at that location. If anomalies correlate
temporally (all anomalies occur at night or all occur on weekends), that suggests a pattern related to behavioural or
operational factors.

## Which of the innocent readings holds

A metering anomaly rarely arrives with its cause attached. A feeder's consumption halving at an instant could be a large
customer disconnecting, a relay tripping the feeder, theft suddenly lifted, or meters falsifying; a district's losses
climbing from two to eight per cent could be a new metering fault, theft, or unauthorised load. The record narrows it by
refusing to let the meter be the only witness: a drop that a SCADA relay trip explains is not a metering event at all,
and a suspected tamper is placed by where its signature sits, at an individual meter against physical verification, in
the gap between what Utility Connect's CDMA logs show leaving the meter and what the platform stored, or in an edit to
the platform's own audit log. Where the digital record runs out, the physical one can still decide it, as the operator's
handwritten read log did in the ACM dispute.

Benign variation is heavy at the single meter, where consumption varies household to household and detection throws false
positives, and low at the aggregate, where the sum of meters against the feeder's own measurement leaves little room for
benign disagreement.

*Last updated: 13 July 2026*
