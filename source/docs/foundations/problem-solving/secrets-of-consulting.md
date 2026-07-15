# Book review: The secrets of consulting

![Secrets of consulting](/_static/images/foundations-secrets.png)

Gerald Weinberg's "The Secrets of Consulting: A Guide to Giving and Getting Advice Successfully" (1985) collects three
decades of advising into a run of numbered laws, rules and effects, each pinned to a folksy name and a small story. It
reads like a self-help book and is easy to dismiss as one. The trap is that most security work is consulting whether or
not anyone calls it that: an assessment gives advice, a finding gives advice, an architecture review gives advice, and
the advice keeps not being taken. Weinberg's subject is exactly that gap, between having the right answer and getting
anyone to act on it.

## It's always a people problem

The Second Law of Consulting holds that no matter how it looks at first, it is always a people problem. Security spends
much of its budget arguing the opposite. A misconfiguration is a fact about a machine; the reason it was there, went
unnoticed for a year, and reappears a quarter after it is fixed is a fact about people and incentives, which is where the
[emotional and political dimensions](three-domains.md) of the problem usually live. A report that stops at the machine
has described the easy half. The point is not that technical detail is beneath the consultant, but that a consultant who
treats the technical layer as the whole problem will be reliably surprised when the fix does not hold.

## The wider you spread it, the thinner it gets

The Law of Raspberry Jam is the book's most quoted line and among its most useful to a security function: the wider you
spread it, the thinner it gets. Influence and reach trade against each other. A security team that inserts itself into
every decision, every ticket, every review can end up touching everything and changing nothing, because attention spread
that thin stops carrying weight. The uncomfortable reading is that a mandate covering the whole organisation may be a
symptom of weakness rather than strength. Depth in a few places the business actually feels tends to shift more than
breadth across places it does not.

## Advice people can take

Much of the book is about making advice safe to accept, which is the same wall change work meets from the other side.
Weinberg's version is the Buffalo Bridle: the herd can be led anywhere, so long as it already wants to go there. Advice
that asks a client to admit they were wrong, or to hand a win to the security team, meets resistance that has little to
do with whether the advice is correct. The craft is to arrange things so the client can adopt the change and keep their
footing. In security this is the difference between a finding that names a culprit and one that leaves everyone a
face-saving route to the fix.

## Testing a promise

Two of the book's smaller tools travel well. The Orange Juice Test judges a supplier by a demanding request: the answer
worth trusting is "we can do it, and here is what it will cost", not the cheerful "no problem" that means nobody has
thought about it. Applied to a control, a vendor, or a team's own commitments, it sorts honest capacity from wishful
compliance. The Titanic Effect is the darker one: the belief that disaster is impossible is what arranges the disaster.
A programme whose risk register has quietly agreed that the crown-jewel system cannot fail has already met it.

## Where it shows its age

The register grates. The relentless naming of laws after animals and kitchen items, the imagined workshops, the gentle
winking, all of it can read as evasion once the stakes climb. The frame is the solo external consultant selling advice by
the day, which maps awkwardly onto an in-house team that cannot walk away and has to live with the client forever. And
1985 shows: nothing here anticipates the scale, speed, or adversarial edge of modern security work. The laws never add up
to a method, and Weinberg does not pretend they do. What survives is a short list of questions to run before the fix,
whose problem this is, who has to save face, what is being spread too thin, what has been quietly declared impossible. A
flawless assessment nobody acts on has failed at the only part the book takes seriously: the getting-anyone-to-act half,
which no amount of technical rigour reaches on its own.

*Last updated: 15 July 2026*
