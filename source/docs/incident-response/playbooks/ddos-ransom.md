# DDoS with ransom demand

*For SOC, network operations, SIRT, and communications teams. Fast-paced tabletop with public pressure: 90 minutes.*

The scenario exposes the gap between availability decision-making as a technical process and as an organisational one. The technical question, can we mitigate this?, has an answer. The organisational question, do we pay, who decides, on what timeline, with what public statement, typically does not, because it has never been tested at the speed the scenario demands. The scenario also surfaces the assumption that crisis communication is a separate track from technical response. Under time and public pressure, those tracks collapse into each other, and the team discovers whether they can hold both simultaneously.

## The scenario

Friday, 16:45 GMT. The public-facing website and APIs begin degrading severely. SOC identifies a large-scale DDoS attack: 50+ Gbps traffic from a botnet. Services are completely unavailable within 10 minutes. An email arrives demanding 5 Bitcoin within two hours or the attack continues for 72 hours. Customer support is overwhelmed. Social media is filling with angry customers. The weekend starts in 15 minutes.

The scenario runs in five decision rounds, each introducing a new pressure. Technical mitigation is possible but has cost. The ransom deadline approaches. A competitor uses the outage in their marketing. A customer threatens legal action. The cloud provider offers enhanced DDoS protection at €50,000 per month. A spokesperson needs a statement. The attack may or may not stop, the facilitator decides based on how the exercise is going.

## Running the exercise

The scenario works because of its timing, not its technical content. Friday afternoon, 15 minutes until the weekend, a two-hour deadline: these are not arbitrary details. They represent the conditions under which many actual availability incidents occur. If the exercise is run at 10:00 on a Tuesday with two hours allocated, it tests something different and less realistic.

The CFO inject is the moment the exercise is built around: "Isn't it cheaper to just pay the €30k ransom than lose €500k in revenue?" This is not a bad-faith question. It is a reasonable question the organisation ideally has a pre-established answer to. If the team has not thought about extortion payment policy before this exercise, they will discover they have no authority framework for the decision in real time. Watch whether anyone in the room knows whether the organisation has a policy on paying DDoS ransom, and whether it covers this scenario specifically.

The communications dimension is as important as the technical one. The inject where the competitor tweets about the outage tests whether the communications function is inside or outside the incident response loop. In many organisations, the answer, discovered during the exercise, is "outside, and we have no process for pulling them in quickly."

For advanced teams, add one or two complexity factors: a key technical person unreachable on holiday, a simultaneous internal alert requiring SOC attention, a regulatory body requesting an incident update. These are not to punish the team but to surface where the response plan assumes ideal staffing and conditions.

## Debrief

What happened to the communication between technical and communications teams under pressure? At what point did they diverge?

Then the structural questions:

Does the organisation have a policy on paying extortion demands? If so, who knows it exists? If not, who has authority to make that decision under a two-hour deadline on a Friday evening?

The attack arrived at 16:45. What does the actual weekend escalation path look like? Was the exercise staffed in a way a real incident would be?

The CFO's question was not wrong. What analysis would the organisation need to run to give an honest answer, and has that analysis been done before this exercise required it?

What did the competitor's tweet reveal about how the organisation monitors its public reputation during an incident?

The timing is as much the finding as the decisions. An organisation that can handle this scenario well at 10:00 on a Tuesday may not be able to handle it at 16:45 on a Friday. The exercise is designed to surface whether that is true.

## Outputs

A clear record of communication coordination failures, if any. An explicit decision on extortion payment policy, or a named decision to make one. An honest assessment of weekend escalation paths and whether they are actually functional. Any changes to public communication procedures that would survive the conditions the exercise created.
