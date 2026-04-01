# Feedback and learning

Purple teaming's value comes from converting findings into improvements. Structured feedback loops ensure learning happens.

## Structured debrief process

Timeline reconstruction: Walk through exercise chronologically. What happened when? What was detected?

Gap identification: Where did detection fail? Where was response slow or incorrect?

Root cause analysis: Why did gaps exist? Tool limitations? Process failures? Training needs?

Improvement prioritisation: What fixes provide most risk reduction? Quick wins vs. long-term projects?

## Red → Blue: Turning attacks into defences

TTP documentation: Red team provides complete technical details of all techniques used.

Detection opportunities: Identify specific points where blue team could have detected activity.

Rule creation: Convert red team IOCs into detection rules, correlation logic, hunt hypotheses.

Playbook updates: Add newly discovered attack patterns to response procedures.

## Blue → Red: Defence-led emulation priorities

Visibility gaps: Blue team identifies blind spots where red team should focus testing.

New tool validation: After deploying new security controls, blue team requests targeted testing.

Threat intelligence integration: Blue team shares threat intel that red team emulates.

Defensive wins: Blue team highlights effective controls red team should attempt to evade.

## Building a learning culture

Blameless post-mortems focus on systemic improvements rather than individual fault.

Psychological safety means it is safe to report failures and gaps without fear of punishment.

Finding gaps through purple teaming is success, not failure.

Document lessons learned, share them with the broader team, build organisational memory.

## The communication conditions that make feedback honest

Structured debriefs are the mechanism. The conditions that make them work are separate from the mechanism, and
considerably harder to establish.

Satir identified several patterns in how people communicate under pressure, all of which appear reliably in
purple team debriefs. Placating: the blue team agrees that the finding is important and that they will address
it, because disagreeing feels risky and agreement ends the uncomfortable conversation. Computing: the response
to a finding is the creation of a new policy or process document, which produces the feeling of action without
the reality of changed capability. Blaming: the debrief focuses on who was at the keyboard when the alert was
missed, rather than on the system conditions that made missing it likely.

None of these patterns produce learning. They produce the appearance of feedback while preserving the conditions
that created the gap.

What makes feedback genuinely honest is congruence: alignment between what is said in the debrief, what people
actually experienced during the exercise, and what the organisation is willing to do about it. When those three
things diverge, the debrief is theatre. The divergence is usually visible to everyone in the room, which is why
it produces cynicism rather than motivation in teams that have been through too many of them.

The practical implication is that how leadership responds to the first uncomfortable finding sets the tone for
everything that follows. An exercise that reveals a significant gap, followed by leadership treating that gap as
information rather than as someone's failure, teaches the team what honest reporting is safe. An exercise
followed by a search for accountability teaches the team what it is not.
