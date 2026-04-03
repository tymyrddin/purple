# Supply chain compromise

*For SIRT, SOC, IT operations, and procurement. Live injection into actual monitoring systems: 2-4 hours.*

The scenario exposes a specific and common [model failure](../../foundations/system-effectiveness/core-triad.md): the organisation's security model treats the perimeter as the boundary of control, but trusted vendor access crosses that boundary by design. The monitoring vendor has legitimate credentials and legitimate access. What the organisation has not modelled is what "trusted" means operationally, not the contract, not the relationship, but the technical controls and the actual behaviour of that access day to day. The second thing the scenario exposes is the political constraint on a technical decision: the containment action that is technically obvious (revoke access) is organisationally complex (the vendor has SLAs, the business depends on the service).

## The scenario

Your organisation uses a third-party SaaS monitoring tool with legitimate infrastructure access. Unknown to the team, the vendor has been compromised. The exercise begins with anomalous behaviour from the vendor's account: unusual API calls, queries for user lists, privileged accounts, and network maps. Beacon traffic to an unknown external IP appears in logs.

Investigation reveals that the vendor account is accessing systems outside its normal monitoring scope. A call to the vendor contact produces vague answers, "routine maintenance", that do not explain the specific API calls. Further analysis shows data staging: large queries packaged for exfiltration. A public disclosure then arrives: a security researcher has tweeted that this monitoring vendor has been compromised across multiple customers, and media coverage follows.

## Preparing the exercise

The preparation is part of the exercise. Before running it, identify what a realistic baseline of behaviour looks like for the test account, so the anomalous behaviour stands out against it. This often reveals gaps: the team may discover they do not have a clear baseline for what the monitoring vendor should be doing. That discovery is itself a finding.

Run the exercise against live monitoring tools where possible. The point is not to simulate the experience of using a SIEM but to observe whether the actual monitoring configuration would detect this behaviour in the actual environment.

If the actual vendor cannot participate, the simulation team plays the vendor role. Brief whoever plays that role carefully: the vendor's vague, slow responses are not bad acting, they are realistic. Vendors under real compromise are often genuinely confused about what their tool has done.

## Running the exercise

The inject to watch for is the vendor relationship manager: "We need this tool. We have SLAs. You can't just shut it off." This is not a complication, it is the actual constraint. The technical decision to revoke vendor access is one part of the picture. The organisational decision to act against a vendor contract under ambiguous threat conditions is what the exercise is really testing. The team that treats this as noise to be overridden has learned less than the team that works through it.

Watch for the moment the team contacts the vendor. How they handle that call, the questions they ask, how they interpret vague answers, at what point they stop believing "routine maintenance", reveals a great deal about their investigation instincts and their trust model for vendor relationships.

The media disclosure in the final phase changes the calculus: the threat is now confirmed and the organisation is named in coverage. But how the team reaches that point, and what they do with the time between "suspicious" and "confirmed", is where the value is.

## Debrief

What did the monitoring actually catch, and how quickly? What would have changed that?

Then the structural questions:

What was the organisation's model of this vendor's access before the exercise? Was that model based on the contract, or on an actual review of what the credentials could do and what behaviour constituted a deviation?

At what point did the team become confident enough to act on containment? What would have moved that point earlier?

The vendor relationship manager's concern was legitimate. How is that kind of decision made in the actual organisation? Who has the authority to override an SLA relationship on security grounds, and is that known in advance?

The compromise affected multiple customers. What are the organisation's obligations to those customers, and were those obligations understood before the exercise raised them?

The vendor relationship is a trust assumption. Trust assumptions are not verified by auditing the contract. This exercise is designed to surface what the actual technical controls on that trust look like, and whether they match what the organisation believes they are.

## Outputs

A clear picture of the current detection capability for vendor access anomalies. An assessment of whether the containment decision authority exists and is known in advance. A list of vendor access assumptions worth verifying technically rather than contractually assuming. Any regulatory reporting obligations that were unclear during the exercise.
