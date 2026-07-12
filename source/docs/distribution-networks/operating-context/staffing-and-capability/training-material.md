# Training material

Training material has a property the other sources lack: it
does not just name the artefact, it teaches the correct form of it, so it reveals the schema, the fields and the
sign-off structure an investigator could later find. It also exposes the human layer, who acknowledges, who approves,
who signs, that maps onto the operator-action records.

## Switching procedure

The strongest Stedin-specific case. Stedin's own contractor training, described in its [contractor information sheet](https://www.stedin.net/-/media/project/online/files/zakelijk/branches/aannemers-en-projectontwikkelaars/veilig-werken/informatieblad-voor-aannemers.pdf), includes a course on writing work plans and switching plans correctly according to the Stedin method, after which the participant knows the process, the application and the way of writing around werkplannen and bedieningsplannen.
That single training description identifies the artefacts a switching operation produces: a werkplan and, for switching,
a bedieningsplan, both created digitally in the Bedrijfsvoering application, plus the Stedin Academie switching course
that gates the Schakelbevoegd flag on a person's appointment, and the BVE/BVG user training for the application itself.

The extended-operation case adds the two-BD approval and the five-day filing of the draft plan. So the
switching-training curriculum is effectively a list of the records each switch leaves behind.

## Relay testing

The vendor training here is unusually explicit about artefacts. Omicron's [Test Universe protection-testing courses](https://www.omicronenergy.com/en/training/courses/detail/protection-testing-101-basics-and-overcurrent-with-test-universe/6366/) teach commissioning, troubleshooting and periodic testing, and centre on creating test plans and customised test reports, testing pick-up values, trip times, zone reaches and impedance characteristics.

The tooling, [Omicron RelaySimTest](https://www.omicronenergy.com/en/products/relaysimtest/), generates an adjustable test report assessing the protection system's behaviour automatically.

Third-party courses go
further into the specific artefacts, teaching XRIO settings templates per relay model, importing relay settings, and
building test plans for named devices like the ABB REL670, SEL-421 and Siemens 7SA8x (independent relay-testing courses
on Scribd, Udemy and consultant sites, perishable). SEL runs its own commissioning training in the same vein.

The training identifies the relay-test evidence: the settings file loaded, the test plan, the injection records, the pick-up and trip-time results, and the as-found and as-left report.

## Commissioning

Commissioning training and roles reveal the sign-off artefacts. Stedin describes commissioning engineers whose job is to
deliver installations that actually work, alongside protection and control (Meet- en Regeltechniek) work on high-voltage
stations (Stedin careers material, recruitment pages).

The operational documents name the
mechanism: a vrijgave (release) session convened by the IV between all parties before a contractor is authorised.

So commissioning produces test records, protection settings verification, the release-session record and the appointment
authorisation, on top of the relay-test reports.

## Maintenance workflow

The maintenance training sits on the asset system already mapped. Stedin's own [bedrijfsschool](https://werkenbij.stedin.net/werken-en-leren) teaches the maintenance and inspection workflow, and the tooling is IBM Maximo, whose training and documentation describe work-order lifecycle, inspection records and the e-audit change trail.

The workflow training therefore
points at work orders, inspection findings, condition scores and the attribute-level audit of who changed what.

## Alarm acknowledgement

This is the one that depends on Stedin's SCADA product, e-terra. Operator training in any control-room
environment covers acknowledging alarms, and the artefact is an alarm and event journal entry carrying operator
identity, timestamp and acknowledgement state. The genre is standard across the SCADA and DCS operator-training
curricula; the specific journal fields belong to Stedin's e-terra configuration, which is not public, so the
category is certain and the exact schema is the gap.

## Training as a specification of the record

Training material teaches the workforce to produce those artefacts in a particular form, which is why it is the clearest single statement of what ordinary work is supposed to leave behind.

A switching course that teaches writing a bedieningsplan in a named application is, in effect, a specification of the switching record. A relay-testing course that teaches producing an as-found and as-left report is a specification of the commissioning evidence.

The training exists precisely to standardise the artefact, so it reveals both the artefact and its expected structure.

Training is where the human-action layer becomes legible: it names who is authorised to acknowledge, to switch, to approve, and that authority maps directly onto the operator field in the eventual record. The training tells not just that an action is logged but whose identity attaches to it.

The same two blanks recur across material: the alarm-journal schema and the SCADA operator-log format, both tied to Stedin's private e-terra configuration.

*Last updated: 11 July 2026*
