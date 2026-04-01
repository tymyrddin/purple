# Maturity progression

Purple team capability matures over time. Understand where you are and plan progression.

## Level 1: Ad-hoc testing (Initial)

Characteristics:
- Occasional one-off security tests
- No structured approach
- Limited documentation
- Minimal coordination between red and blue

Capabilities:
- Basic vulnerability scanning
- Penetration testing reports
- Reactive security improvements

Next steps:
- Establish regular testing cadence
- Document objectives and scope
- Begin red/blue collaboration

## Level 2: Structured exercises (Developing)

Characteristics:
- Quarterly or semi-annual purple team exercises
- Defined objectives and scope
- Post-exercise debriefs
- Tracked improvement items

Capabilities:
- MITRE ATT&CK aligned testing
- Detection coverage mapping
- Documented playbooks
- Measurement of basic metrics

Next steps:
- Increase exercise frequency
- Automate common tests
- Build detection engineering capability

## Level 3: Continuous validation (Managed)

Characteristics:
- Monthly exercises or continuous testing
- Automated TTP validation
- Regular detection tuning
- Integrated with change management

Capabilities:
- Automated adversary simulation
- Continuous detection coverage monitoring
- SOAR-driven response automation
- Threat intelligence integration

Next steps:
- Predictive defence based on intel
- Advanced adversary emulation
- Full defensive program integration

## Level 4: Automated adversary emulation (Optimised)

Characteristics:
- Continuous automated testing
- Real-time defensive tuning
- Predictive threat modelling
- Purple team embedded in all security activities

Capabilities:
- Autonomous detection and response
- Proactive threat hunting
- Custom adversary emulation
- Security as code practices

Roadmap for progression:
1. Build visibility and logging (Months 1-3)
2. Establish purple team exercises (Months 3-6)
3. Increase frequency and automation (Months 6-12)
4. Continuous validation (Year 2)
5. Advanced automation (Year 2+)

## Organisational maturity alongside technical maturity

The levels above describe technical capability. An organisation can reach Level 3 technically while remaining
at Level 1 organisationally, which means findings surface consistently and are consistently not acted on.
The gap between technical and organisational maturity is where purple team programmes quietly die.

Organisational maturity has its own progression, and it does not follow the same timeline as the technical one.

At the early stage, findings are treated as report content rather than as requirements. Leadership is aware that
purple teaming is happening and considers it valuable in principle. In practice, the resource allocation
decisions that determine whether findings get fixed sit above the security function's authority, and the
findings wait.

At the developing stage, there is a mechanism for findings to reach decision-makers and a rough expectation
that significant gaps will be addressed before the next exercise cycle. This mechanism is imperfect and
occasionally requires escalation, but it exists.

At the managed stage, findings from exercises feed directly into the organisation's risk and prioritisation
processes. Purple team output is considered alongside other operational demands rather than competing separately
for attention. The programme has demonstrated enough times that it surfaces real risk that its findings carry
weight.

At the optimised stage, the organisation understands that the chaos phase of capability improvement (the period
during which things appear to get worse before they get better, detection counts rise, metrics look alarming)
is expected and planned for rather than treated as evidence that the programme is not working.

Technical and organisational maturity need to develop together. A technically sophisticated programme in an
organisationally immature environment produces excellent documentation of gaps that do not get fixed. That is
useful to exactly no one, except possibly the adversary.
