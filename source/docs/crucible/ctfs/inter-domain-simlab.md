# Inter-domain SimLab

[Inter-domain SimLab](https://github.com/tymyrddin/inter-domain-simlab) is a containerlab-based routing range:
a live BGP fabric of transit providers, customer ASes and a passive collector, where an attacker with a
foothold AS practises prefix hijacks, route leaks and RPKI abuse as a free-roam CTF. It is the routing
counterpart to the OT estate in [ics-access-simlab](ics-access-simlab.md). Where that lab models a utility's
IT/OT boundary, this one models the public routing commons: the global table, the relationships between
autonomous systems, and the trust those relationships quietly assume. Consequences emerge from what the player
actually announces.

## Where a player starts

`./ctl player` enters through the bastion, the one door. The player picks an operation from a menu and is
dropped straight onto the box it starts from: the foothold router (`attacker-as`, AS65020) in `vtysh` for a
straight hijack, or the registry-attacker workstation (`launder`, `poison`) for a registry-tamper move, from
where a pivot to the foothold is one `foothold` command away. The looking glass, `lg`, is the player's single
public vantage for confirming what an announcement did to the table. The passive collector belongs to the
operator, not the player, and announces nothing.

## The fabric

Private ASNs (64512 to 65534) and documentation prefixes (TEST-NET), with no internet egress, so the range
stays contained.

| Node           | ASN   | Role                                                  |
|----------------|-------|-------------------------------------------------------|
| transit-a      | 65001 | transit provider, peers with transit-b                |
| transit-b      | 65002 | transit provider, peers with transit-a                |
| victim-as      | 65010 | customer of transit-a, owns 203.0.112.0/22 and a /24  |
| attacker-as    | 65020 | customer of transit-b, the player's foothold          |
| customer-leaky | 65030 | multi-homed leaky ISP, the route-leak position        |
| observer       | 65000 | passive collector, peers both transits, operator only |
| lookingglass   | 65005 | single-vantage public collector, the player's `lg`    |
| web            | n/a   | victim service behind 203.0.113.0/24                  |
| eyeball        | n/a   | client generating traffic toward the victim           |

The registry plane runs RPKI origin validation, with live ROV and ROA state served over native RRDP, and an
IRR database with bgpq4 prefix filters. A move has to get past the same validation a real announcement would
meet, not a simplified stand-in.

## The moves

Seven scenarios play end to end from the foothold, each a prefix hijack, a route leak, or an abuse of the
registry trust, and each with a briefing and a reference solution in the repo:

- false-origin prefix hijack
- incomplete-RPKI hijack
- legitimate-peering hijack
- policy-trust-abuse hijack
- ROA-poisoning hijack
- route-leak hijack
- route-legitimacy subversion

A player drives real BGP announcements from a real `vtysh`, and reads the effect through the looking glass.
Nothing here is an operator knob standing in for the attack: the announcement is the move, and the table's
response is the consequence.
