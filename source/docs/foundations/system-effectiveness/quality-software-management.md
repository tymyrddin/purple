# Book review: Quality software management

![Quality software management](/_static/images/foundations-quality-software.png)

Gerald Weinberg's "Quality Software Management" runs to four volumes published between 1992 and 1997, and the argument is
one sentence stretched across roughly fifteen hundred pages: quality is not a property of software but of the management
pattern that produces it. 

Volume one takes on systems thinking, volume two measurement, volume three the manager's own
conduct under pressure, volume four change. Each leans on the [systems vocabulary](general-systems-thinking.md) of the
earlier work and on Virginia Satir, and together they are the closest Weinberg came to a single field manual. Security
manages the production of an assurance rather than a product, but it manages it the same way, so the series reads across
almost intact.

## Volume one: quality lives in the pattern

The organising idea, taken from Crosby and rebuilt on systems thinking, is that an organisation has a characteristic way
of producing software, and the quality of what comes out is largely set by that pattern before any individual starts
work. Weinberg lays out six cultural patterns, numbered zero to five: Oblivious, which does not know it is developing at
all; Variable, which depends entirely on who is in the room; Routine, which follows process and mistakes the process for
the goal; Steering, which manages by results and adjusts as it goes; Anticipating, which builds for situations it has not
met; and Congruent, in which people act on the state of the whole rather than their corner of it. The ladder does not let
anyone skip. A shop cannot buy its way from Variable to Anticipating, and neither can a security function betting that a
maturity model will lift it two rungs on procurement. He draws the machinery underneath with diagrams of effects, simple
causal loops that show how a well-meant fix feeds the problem it was aimed at, a familiar shape to anyone who has watched
a control tightened in one place breed the workaround that quietly reopens it in another.

## Volume two: measuring to see, not to steer

The measurement volume is the one security most needs and least practises. First-order measurement is observation before
metrics: watch the work, count what is actually happening, and resist the reflex to wire a number straight to a control.
The warning underneath is that a measure adopted as a target stops measuring anything, because people optimise the number
rather than the thing it once stood for. Security lives inside this failure. Patch percentages, mean time to close,
coverage counts: each begins as a way to see and hardens into a thing to game, and the dashboard grows more reassuring as
the estate grows less safe. The discipline on offer is to keep asking what a number was meant to reveal and whether it
still does, which is uncomfortable precisely because the answer is often no.

## Volume three: the manager as instrument

Congruent action is the Satir volume, and its subject is what managers actually do the moment stress arrives. Under
threat the same stances recur: placating the powerful, blaming the absent, retreating into procedure, or going numb to
the whole thing. Congruence is the alternative, action that takes account of self, other and context at once, and it is
far harder than it reads. For security this is the [organisational core](../organisational-development/satir-core.md) of
incident work. The bridge call where the awkward fact goes unsaid, the review that quietly assigns blame so the meeting
can end, the manager who ships procedure instead of judgement: these are the incongruent stances doing real operational
damage, and the volume treats them as trainable rather than fixed.

## Volume four: change is a pattern, not an event

The last volume applies the [Satir change model](../change-management/satir-change-model.md) to organisations: a settled
state is disturbed by a foreign element, tips into chaos, and reorganises around a transforming idea only after a stretch
that feels like regression. Weinberg's contribution is to insist that the chaos is not a scheduling failure to be planned
away but the mechanism of change itself, and that managers who cannot sit in it will kill the transformation to end their
own discomfort. Any security team that has watched a new control, a reorganisation, or a tooling migration make things
worse before better has lived the curve. The quiet point is that the dip is where the change is actually happening, and
pulling out to restore calm restores the old state along with it.

## Four volumes, one claim

The series rewards being read as one book. The two highest cultural patterns from volume one, Anticipating and Congruent,
are the subjects of volumes four and three, which is no accident: Weinberg is arguing that a mature organisation is one
that can both see change coming and act congruently while it lands, and that measurement is what joins the seeing to the
acting. Pulled together, the claim to security is blunt. A programme's ceiling is its management pattern, its metrics
mostly measure how it wants to be seen, its incidents are decided by whether people can stay congruent under load, and
its improvements will pass through a stretch of looking worse. Every item on that list sits upstream of any tool.

## The weight of it

Four volumes is a great deal of Weinberg, and the density is real. The software-engineering scenery has dated, all
measurement programmes and process maturity from an era before continuous delivery, let alone before security had an
adversary in the room. The cultural-pattern ladder can read as tidier than organisations behave, as though every shop
sits cleanly on one rung. And the length means the good ideas arrive diluted: a determined reader could lift the six
patterns, the diagram of effects, the target-corrupts-the-measure warning, the congruence stances and the change curve,
and hold most of the value in a fraction of the pages. What the length buys, for anyone willing to spend it, is the
accumulation. By volume four it is genuinely hard to keep believing that quality, or security, is something a tool
delivers rather than something a management pattern permits.

*Last updated: 15 July 2026*
