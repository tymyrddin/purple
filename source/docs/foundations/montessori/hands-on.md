# Hands-on materials and exercises

The Montessori insight about materials is that they should be concrete, self-correcting, and designed to isolate a single concept or skill so that the learner can engage with it directly without requiring interpretation from an instructor.

For adult security learning, this translates to exercises that are close enough to real conditions to be meaningful, safe enough to fail in without consequence, and designed so that the feedback comes from the exercise itself rather than from someone evaluating the attempt.

## What makes a good security exercise

A good exercise targets a real challenge. Cloud misconfiguration is real. Privilege escalation is real. Credential harvesting via legitimate cloud services is real. An exercise that uses a scenario that is obviously fictional, that uses terminology that does not match what the team will encounter in practice, or that simplifies the environment to the point where the skills learned do not transfer, does not meet this standard.

A good exercise is modular. The starting point is accessible without requiring hours of setup. The core challenge is containable and completable in a session. Optional extensions exist for those who want to go deeper. The exercise does not assume that every person who engages with it is starting from the same place or needs to arrive at the same depth.

A good exercise is self-correcting. The learner should be able to tell whether their approach is working from the results they observe, without requiring an instructor to validate each step. In a sandboxed lab, this might mean that a successful privilege escalation produces visible access to a target file. In a detection exercise, it might mean that the alert fires or does not fire in a way that is directly observable.

## Categories of exercise for security teams

Simulated incidents: the team receives indicators consistent with a real attack scenario and works through detection, triage, and response. The scenario uses current threat intelligence rather than archetypal patterns. After the exercise, the actual attack path is revealed and the team can compare what they detected against what was happening.

Exploitation in a safe environment: working through an attack path in a sandboxed environment, using real techniques against real configurations. The goal is not to produce a red team report but to understand how the technique works, what artefacts it produces, and what would be needed to detect it.

Configuration challenges: a deliberately misconfigured environment that the learner must audit, diagnose, and correct. The challenge is in finding all the problems, not just the obvious ones. Extensions ask the learner to explain how each misconfiguration could be exploited and what the detection approach would be.

Design problems: given a set of requirements and constraints, design a security control or detection approach. There is no single correct answer. The exercise surfaces the assumptions the learner is making and the trade-offs they are prioritising. Peer review makes the different approaches visible and produces genuine discussion.

## Rotating the material

Exercises that do not change become exercises in following a known path rather than exercises in security thinking. The material needs to rotate as the threat landscape changes, as the team's capability develops, and as new techniques become relevant.

This is not a large production effort if the library is designed for modularity. Updating a scenario to reflect a current threat intelligence report is a different exercise from rebuilding the whole curriculum. The rotation also signals to the team that the learning is connected to what is actually happening, which supports the intrinsic motivation that self-directed learning depends on.

## Related

- [The prepared environment](prepared-environment.md)
- [CTFs as learning environments](ctf-value.md)
- [Reflection and feedback loops](reflection.md)
- [Scenario labs](../../purple/scenario-labs.md)
- [Live experiments](../../purple/live-experiments.md)
