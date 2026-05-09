# Coordinating with purple team

A red team that operates in opposition to the blue team produces a different kind of exercise than one that operates in coordination with it. Purple teaming is the latter, and the coordination work happens before, during, and after each engagement.

## Before engagements

Joint planning sets the objectives, scope, and success criteria. What is being tested? What is the team hoping to learn? Without explicit answers, the exercise drifts toward whichever activity is easiest to run and produces findings that may or may not address the actual question.

Expectation-setting clarifies what the red team will and will not do. The general scenarios and techniques can be shared without revealing the specific timing or methods, which preserves enough realism for the exercise to test something while reducing the risk of misinterpretation during execution.

Communication protocols establish how the two teams stay in contact. A shared real-time channel works for high-collaboration exercises; post-exercise reflection alone works for less-disclosed modes. The protocol carries the most weight for the case where something unexpected happens, which is the case the team is least likely to plan for.

## During engagements

Observable operations leave traces the blue team can detect, assuming their monitoring works. Completely silent operations produce a successful evasion and no learning. The trade-off between realism and visibility is set by the chosen [coordination mode](../coordination.md).

Evidence preservation maintains clear logs and artefacts so the blue team can reconstruct what happened, whether they detected it in real time or not. The reconstruction is what produces the post-exercise learning; without it, the reflection becomes a discussion of impressions rather than evidence.

Escalation paths handle the case where the red team finds something critical outside the agreed scope. A path that allows responsible disclosure without disrupting the exercise, and without putting the red team in the position of investigating systems they were not authorised to touch, is part of the engagement design rather than something to figure out on the day.

## After engagements

A joint reflection brings both teams together. The red team explains what it did and why; the blue team explains what it saw and what it missed. The conversation works best when both sides are present, because the gap between attack-reality and defence-perception is often where the most useful findings are.

TTP sharing turns the exercise into capability. Detailed technical information, every command, every path, every artefact, lets the blue team build detections, update playbooks, and improve defences specifically for the patterns the red team used. Without that detail, the exercise produces general impressions rather than specific improvements.

Detection-opportunity identification names the specific points where the blue team could have detected activity but did not. These are the priority improvements; they are also the most actionable output of the entire engagement.

Honest assessment from the red team about defensive effectiveness, where the controls held, where the blind spots were obvious, gives the blue team a counterweight to the inevitable post-exercise emphasis on what was missed. Both directions of feedback are needed.

## Related

- [Documentation and evidence collection](docs.md)
- [Working with purple team for improvement](../blue/purple.md)
- [Purple team coordination models](../purple-team/coordination.md)
- [Knowledge transfer: playbooks](../../knowledge-transfer/playbooks.md)
