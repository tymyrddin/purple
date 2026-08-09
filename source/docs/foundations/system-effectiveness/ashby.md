# The ceiling on regulation

A security team that keeps adding people, tooling and playbooks and keeps being surprised by the same class of thing is
usually read as an execution problem. Ashby's answer is arithmetic, and less forgiving.

The quantity he counts is variety: the number of distinguishable elements in a set. A team with four distinct responses to
things going wrong has a response variety of four, whatever its headcount, and the set of things that can go wrong has a
variety of its own, usually a larger one. The law of requisite variety says what follows from the gap between those two
numbers, and what follows is a ceiling. Past a point more effort changes nothing, because the limit is not made of
effort.

Ross Ashby was an English psychiatrist, Director of Research at Barnwood House in Gloucester through the 1950s and later
at the Biological Computer Laboratory in Illinois. He came to control theory from the clinical side, asking how a brain
holds a body steady, and built a machine to answer it.

*Ashby's book has no web page in front of it. The link to it downloads a PDF rather than opening a page.*

## Variety is a count

Ashby gives variety in two forms, the count itself and its logarithm to base 2, so the variety of a pack of playing
cards is fifty-two, or 5.7 bits. The variety of an estate's builds is how many distinct builds it runs. The variety of
what arrives at a security team is how many distinct kinds of thing can go wrong.

Standardising a fleet from three hundred images down to three reduces the variety of that set by a factor of one
hundred, and the count is the whole of what changed.

The count is not a property of the set alone. A two-armed semaphore offers sixty-four positions to an observer close
enough to tell the arms apart and thirty-six to one who cannot, and Ashby draws the moral: *a set's variety is not an
intrinsic property of the set: the observer and his powers of discrimination may have to be specified if the variety is
to be well defined.* The number moves when the distinctions move, which is also why two teams counting the same estate's
disturbances arrive at different totals.

## The law

Ashby's [first worked case](https://pespmc1.vub.ac.be/books/IntroCyb.pdf) is a water-bath with a thermostat, and it gives every term something to point at.

*The thermostatically-controlled water-bath. E is its temperature, and what is desired (η) is the temperature range
between, say 36° and 37°C. D is the set of all the disturbances that may drive the temperature outside that range:
addition of cold water, cold draughts blowing, immersion of cold objects, etc.*

```text
    cold water, draughts,
    cold objects
         │
         D ─────────────┐
         │              │
         ▼              ▼
         R ──────────►  T  ──────────►  E
    the heater       the bath      the temperature,
                                   which has to stay
                                   between 36 and 37
```

D is what arrives, and it goes two ways: into the bath, and into the thermostat that has to notice it. R is the
regulator, the heater and whatever decides when it fires, and the variety of R is the number of distinct things it can
do. T is what D and R both act on. E is the essential variable, and only a narrow band of its values will do.

Swap the labels and the frame holds. D is what arrives at a security team. R is what that team can actually do, which is
not the same as what it owns: tools raise R only where they add a response the team did not already have. T is the
estate they both act on. E is whatever has to stay true, and the acceptable band is the version of it someone would sign
off.

A well-regulated bath holds its temperature whatever the day threw at it, which is why regulation done well is hard to
see from outside. Ashby's own image: *the skilled provider for a family may go through difficult times without his
family realising that anything unusual has happened. The family of an unskilled provider would have discovered it.*

Count the distinct disturbances, count the distinct responses, and the outcomes cannot be squeezed below the first
divided by the second. Twelve distinct kinds of thing that can go wrong against four available responses leaves a
minimum outcome variety of three, before any question of which outcomes are acceptable. If only one of them is
acceptable, four responses will not deliver it, and effort is not the missing ingredient.

Ashby states the same relationship logarithmically, where the division becomes a subtraction:

$$V_O \ge V_D - V_R$$

writing $V_D$, $V_R$ and $V_O$ for the varieties of the disturbances, the responses and the outcomes, each as a
logarithm rather than a count. The same lower bound is there either way; only the arithmetic changes. Raising $V_R$
lowers it from the response side, and reducing $V_D$ lowers it from the disturbance side.

On what sort of statement this is: *The theorem is primarily a statement about possible arrangements in a rectangular
table. It says that certain types of arrangement cannot be made. It is thus no more dependent on special properties of
machines than is, say, the "theorem" that four objects can be arranged to form a square while three can not. The law
therefore owes nothing to experiment.*

## Two consequences

The degenerate case is one response. A regulator with only one is not regulating at all: whatever arrives, the same
thing happens, and the outcome is whatever the disturbance makes it. *... D now is, as it were, exerting full control
over the outcomes.* Every incident handled the same way is that case, and the attacker is choosing the result.

The second consequence is that the law is a ceiling rather than a target. The same structural limit turns up in [Shannon's tenth theorem (page 68)](https://pure.mpg.de/rest/items/item_2383164/component/file_2383163/content),
which caps the noise a correction channel can remove at the information that channel can carry, with Shannon's noise
standing where Ashby's disturbance does. Both are impossibility results. They say where the limit sits, not how to work,
and the moral is drawn in the book itself: a would-be regulator can only try to get near the maximum, because beyond it
there is nowhere to go.

## The version that circulates

The popular form is that a control system has to be at least as complex and capable as the system it governs. That
swaps the size of the governed system for the variety of the disturbances, and the book rejects the swap:

*Largeness in itself is not the source; it tends to be so regarded partly because its obviousness makes it catch the eye
and partly because variations in size tend to be correlated with variations in the source of the real difficulty. What
is usually the main cause of difficulty is the variety in the disturbances that must be regulated against.*

Size is not the quantity that binds. The variety of the disturbances is, and only relative to which outcomes count as
acceptable.

The two versions licence different budgets. "Match the complexity of the estate" is an unbounded demand and reads as a
case for more of everything. "Match the variety of the disturbances, relative to what has to stay inside limits" is
bounded, and it admits a second move that the folk version hides.

Cassie Kozyrkov's essay on leadership in the agentic era runs on the folk version. It scales the law with what a system
can do rather than with what disturbs it, and concludes that playing at tomorrow's level requires self-amplification.
What survives once the law is stated properly is
[an argument about attention](../../thirteen/designing-what-machines-notice.md), which is that second move under
another name.

## Two moves, not one

Amplify the regulator, or attenuate the environment. Stafford Beer, who took cybernetics into management, called that
pair variety engineering. Both reduce the same gap, one by increasing response variety and the other by reducing
disturbance variety, and only one of them usually gets bought.

Amplification is the visible half: more analysts, more detection content, more automation, now agents. It raises what R
can do, and it costs what it costs.

Attenuation reduces the variety arriving in the first place. Standardising builds so an estate runs three images rather
than three hundred. Segmenting so a disturbance in one place cannot arrive in another. Allow-listing so the set of
things that can happen is smaller than the set of things that could. None of that makes the security team cleverer, and
all of it moves the same inequality.

A programme that reaches for amplification and stops has taken the expensive half of the law and left the cheap half on
the table.

## The channel

Ashby's examples of regulators falling short are sensory. Deafness. The driver who cannot see clearly through a
rain-obscured windscreen. The organism that cannot see ultraviolet. What fails in each is the channel from D to R, not the repertoire
of responses.

That is the shape of most monitoring gaps. A security team with a full playbook and no telemetry from a segment is not
short of responses. It is short of channel, and the missing logs set the number. A regulator cannot make use of
distinctions its channel cannot carry. A control nobody can observe is not a control.

Ashby's other case is the cat and the mouse. The mouse that reaches its hole has reacted to the threat, at D, rather
than to the disaster itself, at E, and has forestalled it. Detection engineering is the work of moving the reaction from
E back to D, which is what lets a team's existing responses count for anything.

## Debts downstream

[Weinberg's systems vocabulary](general-systems-thinking.md) starts here, and the borrowings are clearest where Weinberg does not say so.

The [architectural reading of organisational resistance](../../systems-architecture/change-and-homeostasis.md) runs on homeostasis. That word is Ashby's too. He built the Homeostat in 1948 from four linked units. It was given limits within which its essential variables had to stay, and it hunted through its own settings
until it found a configuration that held them, then hunted again whenever it was knocked out of one.

The law does not say how to regulate. It says how much regulation is available for the variety on hand, and it is
indifferent to how hard anyone is trying.

*Last updated: 9 August 2026*
