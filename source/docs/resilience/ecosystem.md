# Organisations as an ecosystem

Risks travel. They move through people, technology, suppliers and regulators with the grace of a domino
chain collapsing, so the dependencies between the parts often shape resilience more than the parts do. The
systems view maps the organisation as an ecosystem and reads it accordingly.

## The lens

A handful of habits describe a systems reading.

- The organisation behaves as a living network of people, processes, platforms and partners.
- Dependencies between HR, IT, suppliers and partners shape how it holds up.
- The first failure is rarely the consequential one; the second, third or tenth knock-on brings the
  house down.
- Security, risk, operations, product and vendor management are different lenses on one system.
- The aim is to find the critical weak links and the points where they converge.

## Mapping and walking it

The map begins with what already exists, org charts, process diagrams, vendor lists, incident reports,
and with a question the paperwork rarely captures: who someone calls when a given thing breaks. Built
out with stakeholders from across the teams, it records people, processes, platforms and outside
partners, and marks the single points of failure and the hidden connectors.

Walking a realistic scenario through that map, a cloud outage, a key supplier failing, an insider
absent, a regulatory shock, traces the ripple as it crosses the system.

The walk produces two kinds of output. The first is the map itself, a record of where the organisation
believes its dependencies and failure points are. The second is behavioural: where the team hesitated,
which dependencies they had overlooked, which recovery pathways turned out to rest on assumptions that
had drifted. The map is implementation evidence; the behaviour during the walk is
[effectiveness evidence](../foundations/system-effectiveness/applying-sem.md). The second is what
reveals whether the model is accurate.

A university walked a cloud-outage scenario across its map and watched the ripple run further than the
boxes suggested. The outage took single sign-on with it; single sign-on gated the rota system; and with
no rota, the security desk could not confirm who was on shift to authorise a manual override. Each of the
three sat on the map as its own node. The walk showed the order they fell in, and that the override
depended on the very system the outage had removed.

## Keeping it live

A dependency map ages the moment services move to a new vendor or a team reorganises, so much of its
worth lies in being revisited. Re-walked on a cadence, it shows dependencies forming and dissolving, the same
picture the [loop](../purple/running-the-loop.md) builds from the other direction, one exercised move at
a time. The recommendations it yields span people, technology and
[supply chain](../audits/supportive/supply-chain.md), and stay with the teams who act on them.

*Last updated: 4 July 2026*
