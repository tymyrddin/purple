# CTFs as learning environments

A well-designed [Capture the Flag exercise](../../crucible/ctfs/index.rst) is one of the closest natural approximations to a Montessori prepared
environment that security learning produces. The challenge is the material. Participants choose what to engage with
and at what depth. Progress is visible without external scoring pressure. Facilitators prepare the environment and
run the debrief. Nobody tells them what to do next.

This is not how CTFs are usually described, and not how they always work. But it is what they can be, and understanding
the conditions that make them work is more useful than cataloguing their formats.

## The structure fits

The [prepared environment principle](prepared-environment.md) holds that the materials for learning work best when arranged so that learners
encounter what they need to encounter, at a level of challenge that suits them, without unnecessary obstacles or
unnecessary scaffolding. A CTF challenge that is designed this way gives the participant a problem that is solvable, that requires
them to develop or apply a technique, and that reveals something about how the technique works when they solve it.

Self-directed learning in a CTF means that the participant decides which challenges to attempt, in which order, and how
long to spend. This is not the same as unconstrained freedom. The environment is structured. But within that structure,
the participant governs their own path. This is the point: the motivation to keep going comes from the work itself
rather than from external obligation.

Hands-on concrete experience is what distinguishes a CTF from a course. The participant does not study a technique. They
apply it, discover what it does and does not do, and update their understanding in response. The gap between what they
expected to happen and what actually happened is the learning.

Intrinsic motivation follows from the design. A challenge pitched at a level of difficulty that fits creates productive
struggle. Participants are not bored and not overwhelmed. They are working. That state is its own reward, and it is
the state in which learning is most durable.

## The realistic PoC requirement

What separates a useful CTF from a box-ticking exercise is whether the challenges reflect how techniques
actually work in real environments.

A sanitised or contrived challenge teaches the move. Participants learn the sequence of steps. They do not
necessarily learn why those steps work, what the technique is actually doing to the target system, or what would cause
it to fail. A realistic proof-of-concept scenario teaches the technique in context. A participant's mental model of
how the attack works has to be updated by the experience.

This is the SEM principle applied to CTF design. The challenge is a model of the attack technique. The quality of the
model shapes the quality of the learning. A model that omits the realistic constraints, the detection opportunities, the
ways the technique breaks under unexpected conditions: that model produces learning that does not transfer. The
participant has learned to solve the challenge, not to understand the technique.

Realistic does not mean perfect fidelity. It means close enough that the participant's intuitions about the technique
are tested by the experience rather than confirmed by it.

## The debrief

A CTF run without a debrief leaves most of its value unused. Participants have had an experience. The [debrief](../../practice/debriefs.md) is where
they consolidate what that experience means.

Useful questions: what was surprising about how the technique worked, what would have caused it to fail, what
detection opportunity did it create, and what does this change about how you would approach this technique in a real
environment.

These are not questions with correct answers. They are questions that make the experience explicit, so that the learning
is portable rather than locked in the specific context of the challenge.

The [Montessori reflection principle](reflection.md) applies here. A facilitator's role in the debrief is to ask the questions that
help participants articulate what they learned, not to explain what the right answer was. Participants who solve the
challenge differently from the intended path have often learned more than those who follow the expected route.

## Where CTFs fail

[Over-gamification](gamified-scenarios.md) is a common failure mode. When the objective becomes solving challenges for points rather than
understanding what the challenges reveal, participants optimise for the flag rather than the learning. Leaderboards and
time pressure can drive this. An antidote is a debrief that treats the question "what did you learn" as more important
than the final score.

Under-difficulty produces no productive struggle. If every challenge is immediately solvable, participants are not
developing capability. They are confirming existing knowledge. The environment needs to be challenging enough that
participants have to extend themselves.

No debrief is the third failure mode. The experience without the consolidation is only half the learning. A CTF that
ends when the scoring closes has used the most expensive part of the preparation and discarded the part that makes it
stick.

