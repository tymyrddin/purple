# Coordination models

Purple teaming can operate in different modes depending on objectives and maturity.

## Disclosed testing (high collaboration)

Approach: Blue team knows exercise is happening, when it starts, and what general TTPs will be tested. Red and blue teams communicate throughout.

When to use: Early purple team exercises, testing new defensive tools or procedures, training new analysts, validating specific detection rules.

Advantages: Maximum learning. Blue team can focus on detection and response without confusion about whether activity is real or test. Enables real-time tuning.

Disadvantages: Doesn't test true detection under realistic conditions. Blue team may be more vigilant than normal operations.

## Blind testing (moderate collaboration)

Approach: Blue team knows exercises occur regularly but doesn't know specific timing or scenarios. Red team activities are revealed during or shortly after execution.

When to use: Mature detection capabilities, testing response procedures, assessing whether monitoring catches realistic attacks.

Advantages: More realistic test of detection without surprise that could cause panic or inappropriate response. Balances realism with safety.

Disadvantages: Can still generate confusion if blue team mistakes exercise for real incident. Requires clear communication channels.

## Double-blind testing (traditional red team)

Approach: Blue team doesn't know exercises are happening. Red team operates covertly. Findings revealed only after exercise completion.

When to use: Testing mature defences, assessing true operational effectiveness, validating detection of stealthy adversaries.

Advantages: Most realistic test of detection and response under actual conditions. Reveals true blind spots.

Disadvantages: Risk of confusion, inappropriate response, or operational disruption. Requires careful scoping and safety controls. Provides delayed learning.

## Continuous purple teaming (advanced)

Approach: Ongoing collaboration where red team continuously feeds scenarios to blue team, blue team continuously tunes detections, automated testing validates coverage.

When to use: Mature organisations with dedicated resources, automated testing frameworks, cultural acceptance of continuous challenge.

Advantages: Fastest improvement cycle. Detection gaps identified and closed rapidly. High confidence in defensive effectiveness.

Disadvantages: Requires significant resources and tooling. Can create alert fatigue if not managed carefully.
