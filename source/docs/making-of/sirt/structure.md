# SIRT structure

The structure of a SIRT is a model of how the organisation expects incidents to unfold and be handled. Like all models, it is accurate when designed and drifts thereafter. Understanding it as a model rather than as a fixed arrangement has practical consequences for how it is built and maintained.

## What the structure needs to do

Before settling on a structure, document what the structure is for. A SIRT operating in a small organisation with one site and no regulatory reporting obligations has different structural requirements from one operating across multiple jurisdictions with mandatory breach notification timelines. Designing a structure that matches the complexity of the larger case when the smaller case is the actual situation produces overhead that prevents the SIRT from functioning.

The structure needs to answer four questions concretely:

How does an incident get identified and declared? What counts as an incident requiring SIRT involvement, and who can make that call? An implicit threshold that everyone will recognise when they see it is not a threshold; it is an assumption that will produce inconsistent escalation.

How does the SIRT get assembled? When an incident is declared, who is notified, how, and in what sequence? A contact and escalation path that exists only in people's heads will fail when those people are unavailable.

How does the SIRT coordinate during the incident? What communication channels are used, what is the cadence of updates, and how are decisions made when the team is distributed or time-constrained?

How does the incident get closed? Who declares it resolved, what is required before that declaration is made, and what triggers the [post-incident review](learning.md)?

## Preparation as the primary work

Most of the work of incident response happens before any incident occurs. Escalation paths, contact lists, authority definitions, and simple checklists for common incident types are all prepared in advance. This is the sense in which the SIRT structure is a prepared environment: it creates the conditions under which response can be fast and effective, rather than improvised.

Simple checklists for recurring incident types, such as malware detections, account compromises, and data exposure findings, are worth maintaining even if they feel obvious. The cognitive load during an active incident is higher than anticipated, and a short checklist that confirms the basic steps are covered is more reliable than memory.

## Keeping the structure current

The structure as designed will not match the structure as operated after significant time has passed. People change roles. Organisational structure changes. Systems are added or replaced. The threat landscape shifts. Each of these changes can invalidate parts of the SIRT model without the model being updated.

The [SEM](../../foundations/system-effectiveness/index.rst) principle applies: errors are model failures. When the SIRT does not function as expected during an incident, the gap between the model and reality is information about what has drifted. Post-incident review is the primary mechanism for capturing this information and using it to update the model. An organisation that reviews incidents primarily to assign responsibility, rather than to understand the gap, loses this information.

Version the SIRT documentation and review it at least annually, or after any significant organisational change or significant incident. A SIRT structure that has not been reviewed in two years is probably wrong in ways no one has noticed yet.
