# Feedback and learning

Purple teaming's value comes from converting findings into improvements. The feedback loop between red and blue, between exercise and operations, is what turns the practice from a series of events into something the organisation learns from.

## The reflection after the exercise

The conversation that follows an exercise typically has four components, none of which are difficult on their own and all of which can be skipped under time pressure.

A timeline reconstruction. Walking through what happened when, what was detected, what was missed, what was acted on. Without this, the conversation defaults to the parts of the exercise that were memorable, which are not necessarily the parts that were informative.

A gap identification. Where did detection fail? Where was response slow or incorrect? The aim is to name the gap specifically enough that the next conversation can be about what to do, rather than about whether the gap is real.

A root-cause reading. The gap was visible; the question is what produced it. Tooling limits, process failures, training gaps, and decision authority each have different remediation paths, and treating one as another produces work that does not close the gap.

An improvement priority. Not every gap warrants the same response, and a list with everything on it is a list with nothing on it. The honest version asks which fixes provide the most risk reduction for the available capacity, including the quick wins that have been deferred for other reasons.

## Red to blue, blue to red

The two sides feed each other in different directions.

A red team turns attacks into defences by sharing the technical detail of what was done: every command, every file path, every connection. The blue team takes that detail and identifies where detection could have triggered, builds rules from the indicators, and updates response procedures with the patterns that were not previously covered. This is the obvious half of the exchange.

The less obvious half runs the other way. A blue team that knows where its visibility gaps are, where new tooling has just been deployed, or where threat intelligence is pointing can ask the red team to test specific paths. This makes the next exercise more informative than a generic scenario, and it surfaces the defensive wins that the red team can attempt to evade rather than the gaps the team already knows about.

## A learning culture is a precondition, not a side effect

The mechanisms above (reflection, gap identification, two-way feedback) are easier to describe than to make work. The conditions under which they produce learning are separate from the mechanisms.

Blameless review focuses on the system that produced the gap rather than the individual who was at the keyboard when it appeared. Psychological safety means people can describe what they actually saw and did without expecting that description to be used against them. Finding gaps through purple teaming has to be treated as success rather than failure, or the practice trains everyone to surface fewer of them.

These are stated easily and built slowly. Without them, the mechanisms run on schedule and produce documents nobody trusts.

## Communication conditions that make feedback honest

Structured reflections are the mechanism. The conditions that make them work are separate from the mechanism, and considerably harder to establish.

[Satir](../../foundations/organisational-development/satir-core.md) identified several patterns in how people communicate under pressure, all of which appear reliably in purple team reflections. Placating: the blue team agrees that the finding is important and that they will address it, because disagreeing feels risky and agreement ends the uncomfortable conversation. Computing: the response to a finding is the creation of a new policy or process document, which produces the feeling of action without the reality of changed capability. Blaming: the conversation focuses on who was at the keyboard when the alert was missed, rather than on the system conditions that made missing it likely.

None of these patterns produce learning. They produce the appearance of feedback while preserving the conditions that created the gap.

What makes feedback genuinely honest is congruence: alignment between what is said in the reflection, what people actually experienced during the exercise, and what the organisation is willing to do about it. When those three things diverge, the reflection is theatre. The divergence is usually visible to everyone in the room, which is why it produces cynicism rather than motivation in teams that have been through too many of them.

The practical implication is that how leadership responds to the first uncomfortable finding sets the tone for everything that follows. An exercise that reveals a significant gap, followed by leadership treating that gap as information rather than as someone's failure, teaches the team what honest reporting is safe. An exercise followed by a search for accountability teaches the team what it is not.

## Related

- [Coordination models](../coordination.md)
- [Common anti-patterns and pitfalls](antipatterns.md)
- [Core ideas of Satir systems OD](../../foundations/organisational-development/satir-core.md)
- [Organisational conditions for change](../conditions.md)
