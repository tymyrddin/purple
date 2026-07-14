# Telephony and verbal authority

Not all authority runs through the written system. Out of hours and under a fault, work is authorised by voice: a call
to the on-call officer, a verbal go-ahead, a switching order read down the line. This is the thinnest evidence layer in
the estate and a known blind spot, because a phone call, left to itself, records that it happened and not a word of what
was said. What keeps the verbal layer accountable is not the call but the paperwork and the registers around it, and the
gap opens exactly where those are skipped.

## What a verbal approval normally leaves

The estate runs most of its authority on paper: the [bedieningsplan](../engineering-and-change/maintenance-window-signatures.md),
the work order, the appointment register. Verbal authority is the exception kept for a fault. A verbal switching or work
plan (a mondeling bedieningsplan) is given by the on-call officer, the OIV holding the storingsdienst for the area, over
the phone or a conference call, under a rule that it is registered afterwards. The safety instruction the portrait works
to makes passing an instruction by voice safe by mandating read-back: the receiver repeats the instruction and the
sender confirms it was understood, in standardised phrasing, and neither a signal nor elapsed time counts as authority
to act. Both parties write the plan down on the spot, and the meldpunt (central dispatch) and the
[Bedrijfsvoeringscentrum](../control-and-command-execution/scada-observables.md) register the hand-over and hold the
current picture of who is responsible for which area.

So a genuine verbal approval is not meant to be bare. It leaves the registered verbal plan, the two written drafts held
one by each party, the meldpunt's hand-over log, the crew's check-in and check-out, and the action that followed in the
SCADA journal. The call is the least of these.

## The call itself

Underneath the paperwork sits the call, and it is the weakest record of the set. A call-detail record shows that a call
happened, between which numbers, when, and for how long, and nothing of what was said. Content survives only if the line
was recorded. Safety-critical control-room and dispatch lines are often voice-logged, so an operations centre may hold
the audio of an operational call for a short retention; whether the portrait's control room records its own lines is not
established, and that uncertainty is the point. Field voice runs on ordinary mobile rather than a recorded radio network,
so a crew's calls leave carrier metadata and none of their content.

## Genuine authority versus a claim of it

A legitimate emergency verbal approval carries a call to the on-call officer at about the time of the work, a read-back
the officer confirmed, a registered plan, and a matching write-up in the work order and incident report, with the
approver holding the authority to give it, Schakelbevoegd, and on the storingsdienst rota for that area. The change
dressed as verbally approved that is not has its tell somewhere in that chain: no call behind the write-up, a call to
someone with no authority to approve, a write-up filed with no registration and no plan, or a recorded line, where one
exists, that carries no such approval.

The difficulty is that the honest and the dishonest version look identical on the telephony alone. Both may show a call;
neither may show its content. The distinction lives in the registers and the plan, not in the call, which is why the
[credential trail](access-control-and-key-management.md) and the operational record have to carry what the phone cannot.

## Cross-checks

The verbal approval is set against records the caller does not control. The write-up's named approver is checked against
who actually held the OIV role for that area at that hour, in the meldpunt's roster; against a call to that person, in
the call-detail records; and against the read-back on the recorded line where one exists. The verbal plan is checked
against the two written drafts and against the action that followed in the SCADA journal and the switching log. The
crew's presence is checked against the check-in and check-out registered at the meldpunt. Where these agree the verbal
authority is corroborated; where the write-up stands alone, it is a claim.

## Telling a real approval from a claimed one

The verbal layer is accountable to exactly the degree its registration happened. Done properly, a verbal approval is one
of the better-corroborated acts in the estate: read back, written down twice, logged at the meldpunt, and followed by an
action the SCADA records. Done in haste and never written up, it collapses to a call-detail record, a call to a number
at a time, its content gone unless a line happened to be recording. So the signature of a fabricated approval is not a
strange call but a missing register: an approval with no roster match, no registered plan, no check-in, standing on a
write-up alone. The blind spot is real but narrow. It is the fast out-of-hours go-ahead that the paperwork never caught
up with, and it is there, and only there, that whether the line was recorded decides whether anything can be said at all.

The noise floor is sparse and mostly content-free by design. Almost all authority runs on paper; verbal authority is the
out-of-hours exception, and of the calls that carry it, usually only the metadata survives. The baseline is thin, a
scatter of call-detail records and a few registrations, so a single uncorroborated verbal approval is not on its own an
anomaly; it is ordinary under a fault. The signal is a verbal approval the registers, the roster and the action cannot
confirm, not the mere fact that authority was given by voice.

An emergency change approved by phone, two origins:

    A CHANGE APPROVED BY VOICE, OUT OF HOURS
    ────────────────────────────────────────
                    GENUINE APPROVAL           │  FABRICATED
    call record     to the on-call officer     │  none, or to no one authorised
    roster          the officer held the duty  │  the approver was not on it
    read-back       on the recorded line       │  absent, or contradicts the write-up
    registered plan filed after, two drafts    │  none
    write-up        matches call and action    │  stands alone

*Last updated: 14 July 2026*
