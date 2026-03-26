# Coordination models

Purple teaming can operate in different modes depending on objectives, maturity, and what the exercise is designed to test. The choice of coordination model encodes assumptions about what the organisation needs to learn at its current stage. Making that choice deliberately, rather than defaulting to the model that feels most familiar, is itself a maturity indicator.

## Disclosed testing

The blue team knows the exercise is happening, when it starts, and what general TTPs will be tested. Red and blue teams communicate throughout.

When to use: early purple team exercises, testing new defensive tools or procedures, training new analysts, validating specific detection rules. The blue team can focus on detection and response without confusion about whether activity is real.

What this tests: whether the detection and response process works when primed. It does not test whether the organisation detects attacks under realistic conditions. That is a legitimate thing to test at an early stage; the limitation only becomes a problem when the organisation believes disclosed testing is validating the same thing as more realistic testing.

The [ChangeShop](../../foundations/change-management/index.rst) observation: disclosed testing is the mode with the lowest resistance. Both sides know what is happening, the exercise is clearly bounded, and the findings are easier to accept because everyone was prepared. This is also why it is the mode that produces the least discomfort, and the mode where the organisation learns the least about what would actually happen.

## Blind testing

The blue team knows exercises occur regularly but does not know the specific timing or scenario. Red team activities are revealed during or shortly after execution.

When to use: more mature detection capabilities, testing response procedures, assessing whether monitoring catches realistic activity. Provides more realistic signal about detection effectiveness than disclosed testing.

What this tests: whether detection works when the blue team is operating normally rather than primed. This is meaningful because normal operating conditions are what the organisation will be in when a real adversary is present.

The risk of misidentification, treating an exercise as a real incident, needs explicit management. Clear communication channels and defined protocols for "is this real?" questions are worth establishing before this mode is used.

## Double-blind testing

The blue team does not know exercises are happening. Red team operates with realistic constraints. Findings are revealed after the exercise.

When to use: testing mature defences, assessing true operational effectiveness, validating detection of low-and-slow adversary behaviour. The most realistic test of whether the organisation would detect and respond to an actual attack.

What this tests: everything disclosed and blind testing tests, plus whether the organisation can recognise and respond appropriately to an event it did not expect and was not primed for.

The costs are real: risk of confusion, inappropriate response, and operational disruption. This mode requires careful scoping and safety controls. It also provides delayed learning, because the debrief happens after the exercise is complete rather than during it.

The [PSL](../../foundations/problem-solving/index.rst) note: this mode puts the most stress on the political layer. The blue team discovering that it did not detect a significant simulated attack, in a mode where it had no warning, can trigger the defensive reactions that prevent learning. The debrief facilitation here is the most demanding.

## Continuous purple teaming

Ongoing collaboration where red team continuously feeds scenarios, blue team continuously tunes detections, and automated testing validates coverage.

When to use: mature organisations with dedicated resources, automated testing frameworks, and a culture that accepts continuous challenge as normal.

What this produces: the fastest improvement cycle. Detection gaps identified and closed rapidly. High confidence in the accuracy of the detection model.

The risk at this level is alert fatigue and normalisation: when exercises are continuous, the signal that "this is important" can become background noise. Managing this requires deliberate attention to what the programme is surfacing and whether it is producing genuine improvement or the appearance of a working programme.
