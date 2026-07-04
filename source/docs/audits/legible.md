# Making it legible

There is an organisation, more common than audit folklore admits, that is genuinely good at all this. Backups are
tested because an engineer distrusts untested backups. Incidents are reviewed because the team wants to know
what happened. Access gets removed when people leave because the offboarding actually runs. Then a customer
asks for a certificate, or a regulator asks for evidence, and the organisation discovers that being good and
being able to prove it are different skills. Its security exists as practice. Practice, unrecorded, is
invisible to an auditor, and an auditor is paid not to take anyone's word for things.

## The wrong translation

The instinctive response is to hire the proof: bring in a compliance function, generate the policy set, build
the binder. Done naively, this produces the two-realities problem, the mirror image of the
[borrowed blueprint](borrowed-blueprints.md): a documentation layer that re-describes the organisation to
auditors while the organisation carries on separately underneath. The papers say what the auditor needs to
hear; the practice stays where it was.

This passes audits, for a while. Its deeper cost is that the audit now inspects the description instead of the
organisation, and so can no longer detect anything. The one instrument that might have caught real drift has
been carefully pointed at a painting of the ship.

## Reverse translation

The workable direction is the reverse: not building evidence, harvesting it. A practice that genuinely runs
already leaves residue: change records, tickets, test outputs, exercise notes, monitoring dashboards, calendar
invites, post-incident write-ups. Much of what an auditor needs is a by-product of work already happening; it
is merely scattered, unlabelled, and stored in the heads and inboxes of the people who did it. The translation
work is to route that residue somewhere findable and give it names an auditor recognises, which is a far
smaller job than manufacturing a parallel paper reality, and unlike that job it does not have to be done twice.

The playbooks' evidence stages describe the target shape per standard: the
[resilience dossier](iso22301/dossier.md), the [inspection](iec62443/inspection.md), the
[far bank](nis2/bank.md), the [base camp check](iso27001/base-camp-check.md). All four rest on the same
distinction: implementation evidence says a control exists, effectiveness evidence says it worked under
realistic conditions. An organisation that is actually good usually has plenty of the second kind lying
around, which is the expensive kind, and no idea that it counts. The working craft of routing, naming, and
keeping that residue has its own page: [Evidence](supportive/evidence.md).

## The mapping comes last

Clause mapping, the "Statement of Applicability" genre of document, is where borrowed-blueprint thinking
sneaks back in: it is tempting to start there, because it looks like the deliverable. Started there, it becomes
the design and the two realities follow. Written last, it is a thin index over things that are true: clause on
the left, pointer to the real artefact on the right, no content of its own. A useful test for any compliance
document is whether deleting it would destroy information or just a table of contents. The mapping ought to be
a table of contents.

## What legibility buys

Framed this way, the exercise is not a tax paid to auditors. An organisation whose practice leaves findable
residue can answer its own questions: what did we change, what did we test, what happened last time. The same
legibility that satisfies an external examiner is what lets internal memory outlive the people who hold it,
and it is one of the quieter services the organisational layer performs. The certificate documents, for
outsiders, a property the organisation already had. That is the honest version of compliance, and it is
noticeably cheaper than the other one.
