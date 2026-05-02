# Interview and workshop facilitation

Internal workshops and evidence-gathering sessions are how an organisation discovers what it actually knows
about its own systems, as distinct from what it has documented. The answers people give, the questions they
do not ask, the topics where the room goes quiet: all of these reveal the mental models people hold of the
systems they work in, and those models often diverge from the documented procedures in ways that matter for
an audit.

Running these sessions internally, before an external auditor does, is how an organisation surfaces gaps
while there is still time to address them. The goal is an honest picture of the current state: where controls
operate as intended, where they do not, and where documentation and practice have quietly parted ways.

## Framing questions around practice, not policy

The most consistent failure mode in internal evidence-gathering sessions is asking about policy rather than
practice. "Do you have a process for reviewing access rights?" will receive a confident affirmative from
almost any team that is aware of the compliance obligations touching their area. "Walk me through the last
time an access review was completed. Who initiated it, how was it conducted, where are the records, and what
changed as a result?" will produce a considerably more revealing answer.

The distinction is between what the organisation says it does and what it actually does. Policy questions test
the first. Practice questions test the second. Evidence gaps and process gaps are only visible if the questions
reach past the policy layer.

Useful framing patterns:

* "Tell me what happened the last time..." forces specificity and reveals whether the process is real
* "Who would I talk to if I wanted to see the output of..." surfaces ownership and process currency
* "Walk me through how this works in practice" invites narrative, which reveals assumptions
* "What would need to go wrong for this control to fail?" moves from claimed function to actual limits

Questions that begin with "do you" or "does your organisation" are policy questions. They have their place in
scoping, but they are rarely sufficient as evidence.

## What silence reveals

A gap in someone's answer is not always ignorance. Sometimes it is evidence that the process does not exist
in the form described in the documentation. Sometimes it is political: the person knows the answer and is not
willing to give it in this setting. Sometimes it is emotional: the honest answer implicates them or someone
they work with.

Recognising which kind of silence is present shapes the follow-up. If someone is struggling to describe a
process in specific terms, a factual prompt may help. If someone seems to know the answer but is visibly
reluctant to give it, shifting the frame often unlocks more: asking about common challenges in that area rather
than about their specific situation, or returning to the topic later in a less direct way.

Silence about the same topic from multiple interviewees is a finding in its own right. It does not confirm a
specific gap, but it confirms that the area is worth examining with direct evidence: logs, configuration
records, system outputs.

## The three layers of a witness

The [three domains of problem solving](../../foundations/problem-solving/three-domains.md) apply to everyone
in an internal evidence-gathering session.

The rational layer is what they know about the systems, processes, and controls in their area. This is what
most sessions try to reach.

The emotional layer is how they feel about having their area examined, their organisation's security posture,
and the implications of honest answers. A person who fears that admitting a gap will create trouble for them or their
team will give rational answers that route around the problem. This is not deception; it is a normal response
to a setting with evaluative stakes.

The political layer is what they are permitted to say, what they have been briefed to say, and what the
consequences would be in their organisation for saying something else. In large or hierarchical organisations,
interviewees may arrive with prepared answers to anticipated questions. Those answers are part of the evidence,
but the gaps between the official line and the specifics are also part of it.

Recognising which layer is blocking a conversation is what allows the approach to change. A witness who does
not know is a different situation from a witness who knows and is uncomfortable, and both are different from
a witness whose honest answer was filtered out before the meeting.

## Group workshops for evidence gathering

Facilitated workshops gather evidence and build collective understanding simultaneously, which makes them
useful for anything that requires cross-functional input: threat modelling, gap analysis sessions, scope
definition, and post-incident review.

The [adversary persona workshop](../../threat-modelling/adversary-persona-workshop.md) technique applies
directly in audit scope-definition sessions: the same process that identifies who might attack a system can
identify which systems and services are in scope and why. The [threat modelling choreography](../../threat-modelling/choreography.md)
covers the broader sequence and is worth reading alongside this page for anyone running workshops as part of
evidence gathering.

For facilitated workshops to produce reliable evidence rather than socially-constructed consensus, a few
conditions matter:

Preparation: people need to know what they are being asked to contribute and have time to gather the relevant
information before the session. A workshop that asks people to recall specifics from memory produces guesses
dressed as answers.

Size: large groups produce less honest output than small ones. A session with more than eight participants
tends toward the official position and away from the specific and uncomfortable. Smaller groups, or breaking
a larger group into working sub-groups, produce better evidence.

Facilitation over instruction: the facilitator's role is to ask questions and surface disagreement, not to
provide answers or steer toward expected conclusions. [Facilitation over instruction](../../foundations/montessori/facilitation.md)
covers this distinction in depth. The instinct to demonstrate expertise is the facilitator's greatest liability
in an evidence-gathering setting.

## When a room suppresses findings

The threat register observation applies here: the threats hardest to identify in a workshop are those whose
naming creates social or political difficulty. The same pattern applies to audit evidence. The hardest controls
to assess in a facilitated session are those where the gap is known and embarrassing, or where the gap
implicates someone in the room.

Insider threat is the canonical example, but the pattern is broader. Any finding that would expose a gap in
an area with a powerful owner, require budget from a team that does not benefit, or contradict an official
position held by someone senior is at risk of being quietly suppressed in a group setting.

Approaches that reduce suppression:

* Separate identification from attribution: gather evidence about gaps before discussing who is responsible
  for addressing them. The ownership conversation changes the atmosphere in ways that close down the
  evidence-gathering conversation.
* Collect written input before discussion: structured pre-work, questionnaires, or anonymous submissions
  surface information that would not emerge in a group conversation.
* Conduct individual interviews alongside group sessions: individuals will say things one-to-one that they
  would not say with colleagues present.
* Treat stated limitations as evidence: "we don't have visibility into that" is not a non-answer. It is an
  answer about the organisation's monitoring coverage.

## Related

* [The three domains of problem solving](../../foundations/problem-solving/three-domains.md)
* [Facilitation over instruction](../../foundations/montessori/facilitation.md)
* [Adversary persona workshop](../../threat-modelling/adversary-persona-workshop.md)
* [Threat modelling choreography](../../threat-modelling/choreography.md)
* [Threat register](threat-register.md)
* [Findings and reporting](findings-reporting.md)