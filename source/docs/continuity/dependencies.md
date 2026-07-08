# Operational dependency mapping

Most continuity plans describe what runs. Few describe what each running thing depends on,
which is often the part that decides whether the plan holds.

## The mapping exercise

For each business-critical activity, the exercise is to ask:

- which systems it requires, including the ones presumed to be background infrastructure
- which people can perform it, and which cannot
- which third parties are in the path, including the ones that contractually deny they are
- which credentials, licences, or contracts permit it
- which data is required, and from which source, and at what freshness
- which physical access is assumed, including the bits that became invisible after 2020

Each of these is a candidate failure point. The map can be considered finished not when the
questions have been answered, but when the answers have been validated against something other
than the org chart.

## Patterns the exercise surfaces

Activities that depend on a single person's expertise, who is not on call, who is not
documented, and who is not always reachable. The bus factor of one is rarely visible until the
bus arrives.

Activities that depend on a SaaS vendor whose own continuity posture is opaque. The vendor's
status page is not a continuity plan. It is a marketing surface.

Dependency graphs that terminate at a credential nobody can rotate without the original
architect, who left in 2023, whose access has been preserved as a courtesy because nobody
wanted to be the one to break the system.

Activities whose dependency on physical access has been forgotten because everything has felt
remote for several years. The keys, the badges, the on-site key fob storage, the printer that
prints the recovery codes: all of these tend to drop off the map quietly.

Activities whose authorisation chain assumes someone with delegated authority is reachable.
At 22:00 on a Friday, the assumption is doing more work than the documentation acknowledges.

## Three categories worth keeping separate

Critical: the activity itself. The thing the organisation needs to do to remain an
organisation.

Dependent: things the activity needs to function. Systems, data, people, vendors, access.

Blocking: things whose failure stops the activity even though they are not part of it. The
building, the identity provider, the firewall ruleset that nobody has authority to change at
22:00 on a Friday, the third party whose breach has caused regulators to pause your operations
even though your own systems are fine.

The third category is frequently the one missed. Blocking dependencies sit outside the
activity diagram, which is why they slip through the planning, and why they often turn out to
be the cause of the longest outages.

## Markers of a useful map

Not a complete one. A complete dependency map is a research project with no natural end, and
in practice it is out of date by the time it is published. A useful map identifies the
critical activities, the dependencies known to be load-bearing, and the dependencies suspected
of being load-bearing but not yet validated.

Validation is the step most likely to be skipped. A map that has not been pressure-tested is
a hypothesis. A map pressure-tested by an exercise is a finding. The two can look similar on
paper and behave very differently in practice.

## Related

- [Resilience, continuity, and disaster recovery](definitions.md)
- [Recovery objectives and what they mean](objectives.md)
- [Asset identification](../risk-management/asset-identification.md)
- [Architecture as model](../systems-architecture/architecture-as-model.md)

*Last updated: 9 May 2026*
