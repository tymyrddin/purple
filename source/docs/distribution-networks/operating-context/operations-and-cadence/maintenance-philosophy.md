# Maintenance philosophy

Stedin is mid-transition
from time-based to risk-and-condition-based maintenance, with predictive elements being seeded rather than mature, and a
small number of hard replacement programmes running in parallel on safety grounds.

## Risk-based maintenance

This is the explicit direction of travel and the best-attested part. Stedin describes moving away from the static
intervals a supplier specifies at handover toward dynamic maintenance driven by the condition of an asset and its risk
of failure, on the reasoning that an installation exposed to sea air needs attention sooner than one in a sheltered
setting, and that condition-and-risk targeting is more effective and efficient (from the implementation partner Gemba's
case study).

Risk-based here carries its usual meaning: prioritise the assets whose failure would carry the most
consequence, and shape the plan around minimising failure risk rather than around the calendar.

## Condition-based maintenance

Condition is being made an input rather than the whole method. The same programme builds dashboards in IBM Maximo that
surface the state of an asset alongside plan progress, schedule completeness and the percentage of deviations found,
with condition rendered in simple colour coding (Gemba case study).

The tell that condition is already feeding the plan is in the [2023 report](https://www.stedingroep.nl/-/media/project/groep/files/stedin-groep-jaarverslag-2023.pdf) reliability chapter: in 2023 Stedin executed around 8,950 low- and medium-voltage maintenance orders, 91 per cent of what was planned, and it notes that inspections showed less maintenance was needed than scheduled.
Adjusting the plan down on inspection findings is condition-based behaviour, even where the label is not used.

## Predictive maintenance

This is the least mature of the three. The enabling telemetry is being deployed rather than a full predictive regime
being run: a new generation of smart sensors and Smart Grid Terminals in medium-voltage stations for remote measurement and switching, described in the [2020 report](https://www.stedin.net/-/media/project/groep/files/investor-relations/financiele-jaarverslagen/jaarverslag-stedin-groep-2020.pdf), and algorithm development in the innovation lab aimed at recognising faults early.

The trajectory points at prediction,
but the public evidence supports condition-and-risk-based maintenance with predictive inputs being introduced, not a
settled predictive programme.

## Inspection intervals

Inspection sits at the centre as the trigger and the plan-corrector. The annual maintenance plan sets the intended
volume of low- and medium-voltage orders, inspection then reveals where less or more is genuinely needed, and completion
is tracked as a percentage against plan, with external factors named when they interfere (extreme rainfall hampering
fieldwork in late 2023, per
the 2023 report).

The direction is away from fixed intervals toward inspection findings feeding a dynamic schedule, which is consistent
with the risk-based transition above.

## Asset lifecycle policies

Lifecycle is owned by the Asset Management function, which sets policy on a long horizon (framed as decisions meant to
hold in twenty or fifty years) and specifies components to be future-proof, described in [Stedin Asset Management material](https://werkenbij.stedin.net/asset-management).

The foundation is the asset register (bedrijfsmiddelenregister) underpinning the quality-assurance system, notable
because Stedin was once formally directed to complete it: a regulator found it lacked current, complete data on the age
and material of cables and pipes, precisely the attributes needed to schedule maintenance and time replacement, in an older [ACM/NMa enforcement decision](https://www.acm.nl/en/publications/publication/6377/NMa-gives-Dutch-regional-network-operator-Stedin-a-binding-instruction-for-having-an-incomplete-fixed-assets-register). Whether that register is now rich enough in age, material and condition attributes to drive genuine
risk-based decisions is the live question the whole philosophy rests on.

## Replacement programmes

Two kinds run side by side. The safety-driven and non-deferrable one is brittle gas main replacement (grey cast iron and
asbestos cement): 212 km removed in 2023, on schedule to have all brittle pipe out of the network before
2028 (2023 report).

The reliability-driven one is electricity replacement to keep the network safe and dependable. In the investment plans
these sit as distinct categories, replacement (vervanging) separated from expansion (uitbreiding), network-driven and
customer-driven, which is how the replacement obligation stays visible against the expansion pressure competing for the
same crews.

## Implications of the philosophy

The philosophy predicts its own evidence. A risk-and-condition-based regime built on Maximo implies a populated asset
register carrying age, material, environment and condition attributes per asset class, failure-mode and criticality
logic sitting behind the risk scoring, condition scores feeding work-order generation, and a maintenance jaarplan
tracked as percentage-complete with a deviations metric.

The predictive ambition implies sensor and Smart Grid Terminal
telemetry streams and the models consuming them, still maturing.

The replacement programmes imply per-asset-class
replacement schedules tracked against dated targets, the 2028 brittle-gas deadline being the sharpest.

The lifecycle
ownership implies component specifications and long-horizon policy documents held by Asset Management, distinct from the
execution records held by the maintenance chain.

*Last updated: 11 July 2026*
