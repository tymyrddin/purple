# Book review: An introduction to general systems thinking

![An introduction to general systems thinking](/_static/images/foundations-general-systemsthinking.png)

Gerald Weinberg's "An Introduction to General Systems Thinking" (1975) is where his systems vocabulary starts. It teaches
through worked examples and puzzles rather than mathematics, on the argument that the mathematics of genuinely complex
systems mostly does not exist, and that pretending otherwise is its own kind of failure. Everything in [the SEM
triad](core-triad.md) is downstream of it. Read now, its use to security is that it dismantles the confidence with which
people describe systems they have not actually observed.

## A system is a point of view

The founding move is to deny that systems are things in the world. A system is a way of looking, a boundary someone drew
and a set of relationships someone chose to attend to. The same network is a routing system, a trust system, a billing
system or an attack surface depending on who is looking and what they came to find. Weinberg organises the book around
three questions an observer keeps asking: why do I see what I see, why do things stay the same, why do things change.
Security skips the first and argues about the third. A good many disagreements about risk are really disagreements about
where the boundary was drawn and which relationships were left outside it.

## The law of medium numbers

The most quietly devastating idea in the book is the Law of Medium Numbers. Some systems are small enough to analyse part by
part. Some are large and uniform enough for statistics to hold. A great many sit in the awkward middle: too complicated
for exact analysis, too organised for the averages to settle. Weinberg's claim is that these medium-number systems throw
up large, irregular surprises more or less on schedule. A security estate is a textbook case, which is why the formal
risk model and the appeal to base rates disappoint in the same way. The surprises are not a sign the model was sloppy.
They are a property of the class of system.

## Deciding what to ignore

Two laws sit together. The Square Law of Computation says the effort of modelling everything grows faster than the
system does, so exhaustive treatment is not merely hard but self-defeating. The Lump Law answers it: to learn anything,
one cannot try to learn everything. Simplification is not a regrettable shortcut but the whole discipline, and the choice
of what to leave out is where competence and blind spots both live. A monitoring strategy is a theory of what can be
safely ignored. When it fails, the omission was usually deliberate and then forgotten, rather than never seen at all.

## The observer in the diagram

Weinberg keeps returning to the observer's fingerprints on the observation. What the eye-brain notices is shaped more by
the brain than the scene; what a law describes often depends on the notation it was written in. For security this lands
on the dashboard. A view renders what its designer decided was worth rendering, and its tidiness is a fact about the
designer, not the estate. Two teams watching the same environment through different instruments can see genuinely
different systems, and each takes its own for the territory. The remedy on offer is not a better instrument but a
standing suspicion of the one in hand.

## The price of generality

The generality is also the cost. Weinberg pitches so far above any particular domain that the reader has to supply every
security example, and the puzzles the book does supply carry the flavour of a 1975 lecture hall. The prose circles, the
way an absorbing lecture does, and a reader who came for procedure will close it unsatisfied. What it hands over is no
checklist, only a cast of mind: notice the boundary, distrust the tidy picture, expect the medium-number surprise, treat
every model as a choice someone made. A defender who takes that on tends to stop trusting their own diagram, which is
uncomfortable, and closer to the truth than the diagram was.

*Last updated: 15 July 2026*
