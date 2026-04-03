# Insider data exfiltration

*For SIRT, SOC, HR, and legal teams. Tabletop with ethical and legal complications: 90 minutes.*

The scenario exposes the gap between access control as a technical concept and access control as an operational reality. The employee had legitimate access. The exfiltration was systematic over three weeks. The question is not how the data was taken but what would have had to be different for this to be detected at week one rather than week three, and why it was not. The second thing the scenario exposes is the collision between legal and security response logic: security wants to act, legal wants to preserve options, HR has a separate obligation to the employee. Those three functions are rarely practised together before an actual incident.

## The scenario

Thursday, 14:30 GMT. SOC detects unusual activity: an employee account has downloaded 15GB of customer data to personal cloud storage. Investigation shows the activity was systematic over the past three weeks. The employee works in Customer Success, has legitimate access to customer records, submitted their resignation a month ago, and their final day is tomorrow. They are currently in the office.

The scenario turns on a series of compressing pressures: the employee's manager reports they have been acting strangely and may have shared login credentials with a colleague; legal flags that premature action could create wrongful termination liability; a GDPR impact assessment confirms the incident triggers breach notification obligations; and the employee requests to leave early for a medical appointment. Each development changes what is possible and what is advisable.

## Running the exercise

This scenario is unusual because the most productive tensions are between the participating teams, not between the team and the scenario. If only security staff are present, the exercise loses most of its value. The HR and legal participants are not there to obstruct, they represent real constraints that security practitioners encounter in actual insider threat cases and rarely practise alongside.

Watch for the moment when security and legal find themselves with genuinely incompatible priorities. Security wants to disable the account immediately to stop further exfiltration. Legal wants to preserve the option for prosecution, which may require controlled evidence collection that immediate lockout could compromise. Neither position is wrong. The exercise makes that tension concrete rather than theoretical.

The inject about a possibly shared login credential is designed to expand the uncertainty. Once the team considers that another employee may have used the account, the investigation scope changes, and so do the legal implications. Watch whether the team widens their investigation or tries to contain the complexity.

Do not resolve the tensions for the team. The discomfort of holding incompatible requirements while the clock runs is the exercise. A facilitator who steps in to break the deadlock teaches the team that someone will resolve it for them. The point is to practise holding it.

## Debrief

What decisions did the team make? Which ones feel most uncertain in retrospect?

Then the structural questions:

How long was systematic exfiltration happening before detection? What does the monitoring posture need to look like for that window to be one week rather than three?

At what point did legal and security find themselves with conflicting priorities? Had any guidance been established for that collision before this exercise, or was it being worked out in real time under pressure?

The employee had legitimate access. The organisation granted that access. What assumption about monitoring covers the space between "has access" and "used access appropriately"? Is that assumption accurate?

If this had been a real incident, what would have needed to exist, in terms of procedures, pre-established authority, or working relationships, that was not there?

The insider threat is uncomfortable because the organisation created the conditions. The access was granted, monitored inadequately, and the departure process did not trigger a review. That is not a failure of individuals. It is a [system operating as designed](../../foundations/system-effectiveness/core-triad.md).

## Outputs

A clear record of where decision-making stalled and why. An honest assessment of whether cross-team coordination between security, HR, and legal is practised or only theoretically in place. The specific monitoring gaps that would need to close for earlier detection. Any legal and HR guidance worth establishing in advance rather than improvising under time pressure.
