# PSL applied to security work

A red team engagement is, on paper, about finding vulnerabilities. Viewed through PSL, it is a live demonstration of systemic failure across all three dimensions.

## Where most engagements go

Rational findings are documented carefully. Technical debt, misconfigurations, privilege escalation paths, gaps in detection coverage. This is the visible layer, and it is the layer that gets funded.

Emotional blockers are observed but rarely reported. Developers afraid to flag issues that would delay release. Ops teams that have normalised shortcuts because escalating them once produced blame and the problem still was not fixed. Leadership that has shaped a reporting culture around green dashboards, so reality gets filtered before it reaches the people who need to act on it.

Political realities are avoided almost entirely. Too sensitive. So the report notes that a critical identity flaw exists, and twelve months later it is still there, because fixing it would require cross-team coordination, and no single team owns the outcome, and the incentive structures do not reward the effort.

The result is a technically sophisticated piece of work that produces no change. An expensive PDF.

## What PSL-aligned security work looks like

A PSL-aware approach involves a different scope from the start.

### Mapping the real attack surface

Not just systems, but decision paths, ownership gaps, and trust assumptions. Where does responsibility transfer between teams? Where are handoffs informal? Where does someone assume someone else has visibility they do not have?

Ownership ambiguity is a vulnerability class. It should be reported as one.

### Reporting organisational findings alongside technical ones

Not only "privilege escalation via IAM misconfiguration" but also "no team owns IAM lifecycle," "engineers lack safe escalation paths," and "security reviews are performative." These are findings. They have exploitability. They have impact ratings.

### Designing findings that force decisions

A finding that says "fix X" can be deprioritised indefinitely. A finding that says "fixing X requires changing Y organisational incentive, and until that changes this attack path remains open regardless of tool investment" is harder to file away. It puts a decision in front of leadership that cannot be resolved by moving a ticket to the next sprint.

### Treating resistance as signal

When pushback comes on a finding, it is not noise to be managed. It is data about the system.

"This is too hard to fix" describes a capacity problem worth documenting. "This is not a priority right now" describes an incentive problem. "We already knew about this" describes an accountability problem: the organisation could see the issue and chose not to resolve it, which is a different finding from the vulnerability itself.

## The uncomfortable conclusion

Most organisations do not have a security problem in the narrow technical sense. They have a problem-solving problem. The vulnerabilities that remain open the longest are not open because nobody could write the fix. They are open because the conditions required to act on them do not exist.

PSL is useful in security precisely because it refuses to treat that observation as someone else's problem.

## Related

- [The three domains of problem solving](three-domains.md)
- [Practical problem solving behaviours for security leaders](psl-approach.md)
- [Applying SEM to security](../system-effectiveness/applying-sem.md)
- [Building a purple team](../../making-of/purple-team/team.md)
- [Building a SIRT](../../making-of/sirt/purpose.md)
