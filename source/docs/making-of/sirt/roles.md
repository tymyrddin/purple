# SIRT roles

Clearly defined roles reduce confusion during incidents and ensure that critical actions have owners. The temptation to leave roles ambiguous in order to preserve flexibility is a temptation worth resisting: flexibility during an incident is not the same as ambiguity, and the cost of ambiguity, at the moment when it matters, is very high.

## The [PSL](../../foundations/problem-solving/index.rst) view of role definition

Assigning roles involves three layers. The rational layer is the straightforward one: who does what, in what sequence, with what authority. The emotional layer is less often addressed: does the person in this role understand why it matters, and do they feel equipped to do it under pressure? A role that looks correct on paper but belongs to someone who has never exercised it is a gap waiting to be discovered at the worst moment. The political layer is the one most often avoided: who has the standing to declare an incident, to escalate it to leadership, and to require that other parts of the organisation cooperate?

Skipping the emotional and political layers produces a role chart that describes what should happen without creating the conditions for it to happen.

## Essential roles

Incident lead: oversees the response process, makes strategic decisions, escalates to leadership when needed, keeps the team focused and the timeline moving. This role requires both the authority to make decisions and the personal composure to make them under pressure. It is also the role most exposed to the political layer: the incident lead often has to tell people above them in the organisation that something has gone wrong.

Technical lead: investigates the technical aspects, coordinates forensic evidence collection, maintains the picture of what the incident involves technically. Works closely with monitoring and SOC functions where they exist. The quality of this role depends on access: access to systems, logs, and the people who operate them.

Communications lead: manages internal messaging to staff and leadership, prepares external communications when necessary, keeps messaging consistent and timely. Communication failures during incidents are as consequential as technical failures. A communications lead who cannot get accurate information from the technical lead, or who does not know what can be disclosed to whom, is in an impossible position.

Documentation lead: records incident actions, timelines, and decisions throughout the response. Produces post-incident reports for learning and compliance. The discipline to document during an incident, while also responding to it, is harder than it sounds. This role is often underfunded in terms of time and attention.

Business representatives: legal, HR, and management ensure that operational decisions are made with awareness of business priorities, obligations, and consequences. They provide context on business-critical systems and potential impact that the technical team may not have.

## Practical notes

These are examples, not a template. A very small organisation may combine several of these roles in one or two people. What matters is that the responsibilities are assigned and understood before an incident occurs, not improvised during one.

The statement that someone is "available" for SIRT work during an incident is not the same as role clarity. Availability and clarity are both necessary.

Test the roles before you need them. A [tabletop](../../purple/incident-response/choreography.md) exercise that runs the team through a plausible incident scenario will reveal gaps in role clarity, authority, and process that no amount of documentation review will surface.
