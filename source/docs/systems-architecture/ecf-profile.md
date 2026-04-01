# The e-CF profile: fit and limits

The European e-Competence Framework (e-CF) provides a reference framework for IT competences, designed to support 
consistent assessment, development, and communication of professional capability across European organisations and 
roles. It is structured around five competence areas (Plan, Build, Run, Enable, Manage) and defines competences at 
five levels, from entry-level contribution to strategic leadership.

The systems architect role maps most directly to e-CF competence A.5 Architecture Design, which describes the 
ability to "estimate, analyse, review and evaluate requirements for enterprise or solution architecture, and 
propose architecture or solution architecture designs that align with business needs." Supporting competences 
include A.1 Information Systems and Business Strategy Alignment, A.3 Business Plan Development, and 
B.2 Component Integration.

## Where the e-CF fits

The e-CF A.5 competence levels provide a reasonable map of technical progression in architecture work:

- At lower levels, the architect contributes to the design of components under the guidance of more senior colleagues, learning to apply architectural principles and standards.
- At middle levels, the architect designs architectures for specific systems, makes independent technical decisions within defined constraints, and communicates designs to relevant stakeholders.
- At higher levels, the architect provides authoritative guidance on architecture across the organisation, sets standards, manages the relationship between technical direction and business strategy, and may influence architectural thinking beyond their own organisation.

This progression is real and the framework's description of the technical activities at each level is largely accurate. For organisations assessing architectural capability and for individuals planning their development, the e-CF provides a useful common language and a reasonable basis for comparison.

## Where the e-CF does not fit

The e-CF is a competence framework: it describes what a person can do at a given level of proficiency. It does not 
describe the conditions under which those competences produce the outcomes they are intended to produce. This is 
where the [foundations work](../foundations/index.rst) reveals the framework's limitations.

- The SEM dimension is absent. The e-CF A.5 description of architecture work treats model accuracy as a property of the initial design rather than as an ongoing maintenance responsibility. An architect assessed as highly competent under the e-CF may produce thorough and well-constructed architectural documentation that becomes progressively less accurate over time, because the framework has no mechanism for assessing whether the architect understands [model drift](../foundations/system-effectiveness/core-triad.md) or takes responsibility for it. The e-CF describes the work of creating the model; it does not describe the work of keeping it honest.
- The [ChangeShop](../foundations/change-management/index.rst) dimension is absent. The e-CF describes the architect's engagement with stakeholders and with business needs, but it does not address whether the architect understands that architectural change is an intervention in a [homeostatic](../foundations/change-management/what-it-is.md) system. An architect who excels at the technical activities described in A.5 but does not understand organisational resistance will produce designs that satisfy the competence description while failing to produce architectural change in the organisation. The e-CF would rate them competent; the outcomes would suggest otherwise.
- The [PSL](../foundations/problem-solving/index.rst) dimension is partly present and partly absent. The e-CF acknowledges stakeholder communication and business alignment, which addresses the rational layer in a limited way. It does not address the emotional layer or the political layer. A senior e-CF A.5 architect is expected to "provide authoritative guidance" and to work with stakeholders at a strategic level, but the framework does not specify what capability this requires beyond technical seniority. The political work of creating and maintaining architectural authority, and the emotional work of engaging with the human consequences of architectural decisions, are not captured.
- The [Satir](../foundations/organisational-development/satir-core.md) dimension is absent. The e-CF does not address communication patterns, does not address the conditions for honest architectural review, and does not address how architects behave under stress. The [survival stances](../foundations/organisational-development/satir-core.md) that produce architectural dysfunction are not visible in a competence profile.

## What this means for using the e-CF

The e-CF is most useful as a floor: it describes the minimum technical competence required for architectural work at 
a given level. Below that floor, the technical work is not reliable. Above it, whether the technical competence 
produces the intended outcomes depends on conditions the framework does not capture.

This does not mean the e-CF is wrong or that organisations should not use it. It means that organisations that assess 
and develop architects exclusively through an e-CF lens will produce architects who are technically proficient but 
underprepared for the social and organisational dimensions of the role. The framework describes a necessary condition 
for effective architecture practice, not a sufficient one.

For an architect's own development, the e-CF is a useful map of the technical dimension. The foundations work in this 
collection is a map of the rest. The two are complementary, and both are incomplete without the other.

## Related

- [The conditions not in the job description](conditions.md)
- [The role of a systems architect](the-role.md)
- [Integrating PSL, ChangeShop, SEM, and Satir OD](../foundations/organisational-development/composite-model.md)
