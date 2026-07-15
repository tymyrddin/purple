# Book review: Are your lights on?

![Are your lights on?](/_static/images/foundations-lights-on.png)

Donald Gause and Gerald Weinberg's "Are Your Lights On? How to Figure Out What the Problem Really Is" (1982) is a slim,
aphoristic book about the step most problem-solving skips: working out what the problem actually is. It reads as a run of
small fables with the morals left slightly loose, easy to finish in an afternoon and easy to underrate for years
afterwards. For security work, where the presenting complaint is almost never the real one, it earns the reread.

## A problem is a difference

The working definition is deliberately awkward: a problem is a difference between things as perceived and things as
desired. Three ways to close a difference fall out of it. Change the world until the perception shifts, change what is
desired, or change the perception itself. Most people reach for the first and never notice the other two. A team told "we
have too many critical vulnerabilities" hears an instruction to close vulnerabilities. The difference might close just as
well by mending a severity scale everyone games, or by asking whether "critical" still means what the dashboard implies.

The definition also refuses to settle. Gause and Weinberg are blunt that you can never be sure you have it right, even
after the problem is solved. Their test, that if you cannot name three things wrong with your understanding of a problem
you do not yet understand it, can be uncomfortable.

## Whose problem is it, and where does it come from

Two questions do most of the book's work. The first is whose problem it is. The advice not to solve other people's
problems when they can solve them perfectly well themselves sounds glib until you count the security findings that
quietly transfer someone else's discomfort onto a team with no authority to act on it. A report that lands a fix on the
group that gains nothing from it has not defined the problem, it has relocated it.

The second question is where the problem comes from, and here the book turns the mirror around. The chief source of
problems, the authors argue, is solutions: every fix seeds the next problem. A new control closes one gap and creates a
bypass, a support burden, a workaround that hardens into a habit. The point is not that solving is futile. It is that a
solver who cannot see themselves as a source of problems keeps being surprised by their own second-order effects, which
is a fair description of a good deal of security tooling.

## Do you really want to solve it

The book's least comfortable turn is the moral one. Some problems are better left, because the cure costs more than the
disease, or because the disruption falls on people who never agreed to carry it. Gause and Weinberg do not sermonise,
they just insist the question be asked aloud rather than assumed away. Security tends to assume the other way, that any
risk found is a risk worth closing, which is how a remediation programme can spend its credibility on findings nobody
outside the security team believes in.

## The lights and where the book runs thin

The title comes from a parable about a tunnel and a sign telling drivers to switch their headlights on, and the tangle
that follows when the authors try to write a second sign telling them when to switch the lights off again. Every attempt
either patronises the driver, misfires in daylight, or drops the responsibility on the wrong person. The moral is that a
problem statement smuggles in a hidden owner and a hidden theory of who ought to act, and rushing to the solution carries
both in unexamined.

Where the book runs thin is scale and power. Its fables are individual and tidy, while real organisational problems are
collective, contested, and rarely resolve as cleanly as a one-page story. It says almost nothing about power, which is
where the [political dimension](three-domains.md) of a security problem usually lives, and its lightness can read as
evasion when the stakes are high. Read it, then, not as a method but as a set of reflexes: ask what the problem is, whose
it is, where it came from, and whether it is worth solving, before reaching for the fix. For anyone who has shipped a
technically correct answer to a problem no one had, the reflexes are worth more than most methods.

*Last updated: 15 July 2026*
