# Gas integrity and safe working

Most of what proves the gas network safe is not a live log but a periodic measurement and a piece of paper: a
cathodic-protection potential read at a test point, an odorant check, a leak survey walked down a street, a permit to
open a live main. The record is thinner and slower than the electricity net's, and it is meant to be, so its signatures
are as much about missing, stale or overdue records as about anomalous ones.

## Cathodic protection

Part of the network is steel, held clear of corrosion by a small protective voltage that keeps the pipe's potential more
negative than the standard criterion (around minus 850 millivolts against a copper/copper-sulphate reference). The
evidence is that potential, read at test points and drainage points, together with the output of the rectifiers that
supply it. The measurement was made by hand at something like ten thousand points once a year; remote sensors now report
several times a day and have cut the physical visits to roughly one in three years.

Normal is potentials sitting within criterion and rectifiers holding steady. The anomaly that counts is a loss of
protection potential, the reading drifting above the criterion, which leaves the steel exposed and, in time, invites a
leak. Its innocent cause is usually a failed rectifier or a broken bond; its cross-check is the potential against the
rectifier's output and against a field reading. A remote potential that stays flat and healthy while a field
measurement disagrees is a stuck or misreported sensor rather than a protected pipe, the same lesson the electricity
side draws from a measurement no independent record confirms.

## Odorisation and gas quality

Distribution gas is odorised with THT, an added odorant, so that a leak can be smelled; the nose is the public's primary
detector. The odorant is added upstream, by the national transport operator at the handover, so the network generally
receives gas that already carries it, and assurance is periodic rather than continuous: random-sample measurements of
odorability and THT content by gas chromatograph at the transfer points.

Green gas is the exception that puts odorisation inside the operator's own record. Injected locally into the
distribution net, it is odorised before it enters, under a regime of checks, at start-up, at twenty-four hours, at four
weeks, and monthly, with the [safety regulator pressing](../../operating-context/regulatory-and-governance/regulatory.md)
for continuous monitoring of gas quality and THT at the injection points. Normal is THT within band and the checks made
on schedule. Under-odorised gas is a safety signature, leaks that will not be smelled, and it reads as a THT measurement
below band, a check missed, or an injection point's quality drifting, set against the point's own dosing record and
against customer reports of gas smelled or not smelled.

## Leak surveys

The low-pressure net is surveyed for leaks on a cycle, roughly two-yearly across the estate and at least yearly on the
brittle-gas mains still awaiting replacement, walked with a hand detector or a sleepmat or driven with a vehicle
sniffer. A leak that is found is located and put into a severity class set by its reading and its distance to buildings,
and the class fixes how quickly it has to be repaired. The artefact is a classified survey record, not a live sensor
stream.

Normal is surveys run on schedule, leaks found, classed and closed within the window their class allows. The signatures
are an overdue survey, a leak found but left unclassed or unrepaired past its window, or a repair booked with no survey
behind it. Each is read against the next record along, the survey against the leak class, the class against the repair
work order, the whole against the brittle-gas replacement map that says where the worst pipe still lies.

## Working a live main

Work on a live gas main is done gas-free and pressure-free wherever it can be. The line is verified drukloos and unable
to re-pressurise, a plug is set, and the steps follow the national gas safety instruction (VIAG) and a bedieningsplan.
The record is procedural: the permit, the safety-instruction sign-offs, the drukloos verification, the as-left. Normal
is the permit, the plan and the verification all present and agreeing.

The unsafe reading of the same work is the one the [Zoetermeer
investigation](../../operating-context/operations-and-cadence/operational-procedures-and-change.md) set out: a
gas-detector alarm overridden rather than obeyed, a supplementary procedure for non-standard work absent, and a line
worked while it could still carry gas. It is a safety failure first, but it is an evidence one too, the same act, safe or
unsafe, told apart by whether the gas-free verification and the instruction sign-offs are there and consistent or
missing.

## The register and the map

All of this rests on the asset register and the network drawings being right. When the register is stale the crew works
to a picture that no longer matches the ground, which is what the Zoetermeer investigation found in the outdated
drawings, so a divergence between the register and the field is a signature in its own right. A change to the register,
meanwhile, carries the same authorised-or-not question as any other record, worked out in [database transaction
logs](../database-and-transactions/database-transaction-logs.md): a network drawing altered with no work behind it is as
much a question as a relay setting changed the same way.

## What the gas record cannot always show

The gas net's evidence is periodic and paper-heavy by design, so its hardest cases are not falsified logs but absent
ones. A cathodic-protection point unread, a leak survey overdue, an odorant check skipped, a gas-free verification not
filed: each is a hole where a record belongs, and a hole is easy to make and hard to tell from ordinary lag. What
separates a benign gap from a covering one is corroboration the operator does not control, a field potential, a
customer's report of smell, a survey the neighbouring section shares, the physical state of a valve or a plug, and,
underneath, the register agreeing with the ground. The gas record is thin enough that the physical world often has to be
the witness the paperwork cannot.

The noise floor is set by slowness, not volume. Measurements are sparse and scheduled, records lag the field as a matter
of course, and an overdue check or a stale drawing is common and mostly innocent, so a single gap proves little; the
signal is a gap that lines up with something else, an unsmelled leak, a corroded main, a work a permit does not cover.

Work on a live main, two origins:

    A GAS MAIN WORKED WHILE IN SERVICE
    ──────────────────────────────────
                    GAS-FREE, PER PLAN      │  UNSAFE, DETECTION OVERRIDDEN
    drukloos check  verified and filed      │  none
    gas detector    obeyed, work stops      │  alarm overridden, work continued
    procedure       VIAG plan followed      │  supplementary step missing
    register/map    matches the site        │  stale, did not match

*Last updated: 14 July 2026*
