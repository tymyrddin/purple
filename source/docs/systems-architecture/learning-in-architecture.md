# Learning in architecture

Architecture practice is a learning practice. The architect learns from the systems they design, from the organisations they work in, and from the gap between what they expected and what they observe. The teams they work with learn from the architecture: from the designs themselves, from the decisions and trade-offs embedded in them, and from the process of engaging with architectural thinking.

This is where the [Montessori](../foundations/montessori/index.rst) framing is most directly applicable, but the SEM and [PSL](../foundations/problem-solving/index.rst) frames also have something to say about how architectural learning works and what prevents it.

## Architecture documentation as prepared environment

The Montessori prepared environment is one in which the materials for learning are arranged so that the learner can encounter what they need to encounter, at the right level of challenge, without unnecessary obstacles and without unnecessary scaffolding. The point of preparation is not to make things easy; it is to make them possible.

An architecture document, well made, is a prepared environment for understanding the system. It provides the conceptual materials, arranged in a way that allows the reader to build accurate understanding without requiring the architect to be present. The diagrams, the decision records, the rationale sections, the explicit statement of constraints and assumptions: these are the materials. When they are absent or inaccessible, the system can only be understood by the people who built it, and only while they are still present.

Poor architecture documentation fails as a prepared environment in predictable ways. It describes what was decided without describing why, which means the reader cannot evaluate whether the decision still applies in changed circumstances. It describes the ideal design without describing what was not done and why, which means teams encounter the boundaries of the architecture without understanding what they are for. It describes the system as it was designed rather than as it is, which means the documentation actively misleads rather than prepares.

## How architects learn

Architects learn from feedback between their models and the systems those models represent. The feedback comes through implementation, through operation, through incidents, and through the observations of the people working closest to the system.

The [SEM](../foundations/system-effectiveness/index.rst) principle here is that the architect's model is continuously being tested against the actual system. Every time the system behaves in a way the model did not predict, there is learning available. Whether that learning is captured depends on whether the architect is attending to the feedback and whether the conditions exist for the feedback to reach them honestly.

The conditions that prevent architectural learning are social as much as technical. If implementation teams know that reporting divergence from the architecture will be treated as a compliance failure rather than a model-updating signal, they will report divergence less. If the architect is not present during operations and incident response, the feedback from those activities does not reach them. If the architecture review process is primarily about approval rather than honest examination, the review produces endorsement but not learning.

## Learning together

The most durable architectural learning happens between the architect and the people who implement and operate the systems. The architect brings the system-level model. The implementation team brings the detailed knowledge of what was actually built, what constraints were encountered, and where the model and the reality diverged. The operations team brings the knowledge of how the system behaves under real conditions. The incident record brings the history of where the model was most wrong, most recently.

Creating the conditions for this learning to happen is partly a facilitation task. PSL's observation that the effective leader of a complex group creates the conditions for others to contribute their best work applies directly. The architect who treats design reviews as presentations rather than conversations, or who treats implementation feedback as a quality control problem rather than a model-correction opportunity, forecloses this learning.

The Montessori principle of facilitation over instruction is relevant: the architect's job in a learning context is to ask the questions that help others articulate what they know, not to explain what the architect already knows. The people closest to the system often understand it more accurately than the architecture describes it. That understanding is a resource, not a threat to the architect's authority.
