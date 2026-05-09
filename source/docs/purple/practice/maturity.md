# Maturity progression

A purple team capability matures over time. Where it sits on that progression at any moment is less informative than which direction it is moving and what is currently limiting that movement.

The levels below describe technical capability. Organisational maturity, covered after, runs on a different timeline.

## Ad-hoc testing (initial)

At this level, security tests happen occasionally and one-off. There is no structured approach, limited documentation, and minimal coordination between offensive and defensive functions. Vulnerability scans and penetration test reports drive reactive improvements when something looks bad enough to act on.

Moving forward at this level is establishing a regular testing cadence, documenting what is being tested and why, and beginning to bring red and blue work into the same room.

## Structured exercises (developing)

At this level, purple team exercises happen on a quarterly or semi-annual rhythm with defined objectives, recorded scope, post-exercise reflection, and tracked improvement items. Testing is aligned to MITRE ATT&CK, detection coverage is mapped, and basic metrics are tracked.

Moving forward involves increasing the cadence of exercises, automating the more routine tests so that scarce time is spent on the things that need judgement, and building deliberate detection-engineering capability rather than treating detections as a side effect of incidents.

## Continuous validation (managed)

At this level, exercises are monthly or continuous, automated TTP validation is part of the regular flow, and detection tuning is routine rather than reactive. Purple team work is integrated with change management: a new system or a significant configuration change triggers a relevant test rather than waiting for the next scheduled exercise.

The transition from this level to the next is mostly about automation, threat-intelligence integration, and predictive defence work that uses the historical data the programme has now accumulated.

## Automated adversary emulation (optimised)

At this level, automated testing runs continuously, defensive tuning happens in something close to real-time, and purple team thinking is embedded in security activity rather than running as a separate function. Custom adversary emulation, security as code, and proactive threat hunting are routine.

A rough roadmap from initial to optimised, for organisations starting near zero: build visibility and logging in the first quarter, establish purple team exercises in months three to six, increase frequency and automation through year one, reach continuous validation in year two, and take on advanced automation thereafter. The timeline is illustrative rather than prescriptive.

## Organisational maturity alongside technical maturity

The levels above describe technical capability. An organisation can reach level 3 technically while remaining at level 1 organisationally, which means findings surface consistently and are consistently not acted on. The gap between technical and organisational maturity is where purple team programmes quietly die.

Organisational maturity has its own progression, and it does not follow the same timeline as the technical one.

At the early stage, findings are treated as report content rather than as requirements. Leadership is aware that purple teaming is happening and considers it valuable in principle. In practice, the resource allocation decisions that determine whether findings get fixed sit above the security function's authority, and the findings wait.

At the developing stage, there is a mechanism for findings to reach decision-makers and a rough expectation that significant gaps will be addressed before the next exercise cycle. This mechanism is imperfect and occasionally requires escalation, but it exists.

At the managed stage, findings from exercises feed directly into the organisation's risk and prioritisation processes. Purple team output is considered alongside other operational demands rather than competing separately for attention. The programme has demonstrated enough times that it surfaces real risk that its findings carry weight.

At the optimised stage, the organisation understands that the [chaos phase](../../foundations/organisational-development/satir-change-model.md) of capability improvement, the period during which things appear to get worse before they get better, detection counts rise, metrics look alarming, is expected and planned for rather than treated as evidence that the programme is not working.

Technical and organisational maturity need to develop together. A technically sophisticated programme in an organisationally immature environment produces excellent documentation of gaps that do not get fixed. That is useful to exactly no one, except possibly the adversary.

## Related

- [Measurements and early success](measurements.md)
- [Organisational conditions for change](../conditions.md)
- [Readiness](../readiness.md)
- [The Satir Change Model](../../foundations/organisational-development/satir-change-model.md)
