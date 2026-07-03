# Clearing the backlog

![Patch sprint](/_static/images/patch-sprint.png)

A patch sprint is a short, bounded push to clear a backlog of known vulnerabilities, misconfigurations, and
deferred security work. It treats patching as an event with owners and protected time, rather than a
background obligation nobody holds and everybody postpones.

The premise is that a patch backlog is rarely a technical problem. The vulnerabilities are known and the fixes
are often simple. What is missing is protected time, clear ownership, and enough confidence in rollback to
apply a change without dreading what it might break. A sprint manufactures those conditions on purpose instead
of waiting for them to surface in normal work. It shifts them for a week; making the shift permanent is a
separate and larger piece of work the sprint can inform but not do.

Most of the value sits in the preparation and the residue, not the week itself. Triage first: group the
backlog by owner, by risk, and by how hard each item really is, and separate what can be fixed inside the
sprint from what needs architecture or a decision made elsewhere first. Establish, or at least understand, the
rollback path before anyone touches production, since a sprint where people are afraid to apply a fix is one
where the systems that most need it stay untouched. And settle what "done" means in advance, patched
everywhere or patched on the highest-risk tier, remediated or mitigated with a plan, so success is not later
declared on closed tickets rather than on reduced risk.

While it runs, the useful daily question is not what someone is working on but what is stopping them applying
a given fix. Those blockers are the second output, and often the more valuable one. A test environment that
does not reflect production is a finding about the environment, not merely a stuck ticket. The applied patches
close today's gap; the record of what made patching hard is what might change the rate at which the backlog
grows back, once it reaches someone with the authority to act on it. A sprint that produces only patches and
no such record has treated the symptom and left the thing that produces it.

