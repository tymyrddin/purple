# Monday morning after the fire

Continuity plans most likely focus on the event. The event is the easier part. The harder
work begins the morning after, when the technology is back, the adrenaline has drained,
and an organisation is left with the consequences. Assume that is Monday.

## The day the plan stops covering

Monday morning, the building is partly accessible. Some staff did not sleep. Some staff did
not come in. The CEO is on television. The customer success team is fielding calls about an
outage that has technically been resolved but is still being felt as ongoing. Insurance has
questions. The press has sharper questions. A regulator wants a written timeline by Wednesday.

This is where continuity most often falters, not because the technology has not been restored
but because the organisation has not. Technical recovery has finished and operational
recovery has not started, and the gap may have no clear owner. The DR document closes at the
moment the RTO is hit. The continuity work is just getting started, and the people who might
have run it are most likely exhausted from the event.

## Where it can go wrong

The communications strategy was usually written for the event and not for the aftermath. The
pre-drafted holding statement covered the first six hours. The next six weeks get improvised.

Decisions made during the event under pressure are now being audited under daylight. Some of
them may look defensible. Some may look hard to defend. The organisation has not yet decided
which it will say about which.

The temporary workarounds are quietly becoming permanent, because nobody has bandwidth to undo
them and the manual process is "fine for now." Six months later, "for now" can become the
architecture.

Staff who held things together during the event are now exhausted, and the organisation may
ask them to also lead the recovery, the post-incident review, the regulator engagement, and
their normal job. Some of them are likely to leave in the next quarter. Their leaving may be
recorded as unrelated.

The accountability question is starting to be asked, and it is not always asked carefully.
The people who held the line during the event may find themselves answering for decisions
made under pressures the auditors are no longer in a position to feel.

The board is asking for assurance that this will not happen again, which is not a question
for which an honest answer will do, and the organisation is now working out which version of an evasive
answer it is comfortable producing.

## The Monday-morning question

For any continuity plan, the question worth asking is: who runs the organisation for the two
weeks after technical recovery, and what does their job look like on those days?

If the answer is not in the plan, the plan stops at the easy part.

The answer involves named roles for the post-event period that are distinct from the event
roles, an explicit recovery-of-the-organisation workstream, a comms posture that anticipates
the regulator, the press, and the workforce in that order, and a calendar that protects the
people who held the line during the event from being immediately drafted into the people who
have to hold the line during the aftermath.

## The triage layer

Smaller organisations often lack the resources to run all of this in parallel. The [DR
scenario triage playbook](https://blue.tymyrddin.dev/docs/org/startup/playbooks/dr-scenario-triage.html) is one
entry point for that conversation, with a startup-scale framing. The framing assumes
constraint rather than abundance, which can produce more honest priorities than the
alternative.

## When recovery becomes governance

Technical failure tends to walk slowly toward governance failure if nobody is watching the
corridor between them. The board started asking about IT and ends up asking about ownership,
about why this dependency was not visible, about who signed off the architecture, about what
the audit committee was told and when. By the time those questions land, the incident has
often stopped being a technology event and become a leadership event. The continuity plan
that did not anticipate this transition is usually the one currently being rewritten.

A continuity programme that takes the Monday-morning view seriously will spend at least as
much design effort on the operational recovery period as on the technical recovery period.
That is rarely where most of the budget goes, which may be part of why so many organisations
meet the RTO and miss the recovery.

## Related

- [Degraded operations](degraded.md)
- [Continuity through a foundations lens](foundations.md)
- [Incident response choreography](../incident-response/choreography.md)
- [Risk to operations](../risk-management/to-operations.md)

*Last updated: 4 July 2026*
