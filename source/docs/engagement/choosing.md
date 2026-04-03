# Choosing an engagement

In [PSL](../foundations/problem-solving/in-security.md), a problem is the difference between a perceived current 
state and a desired state. That definition has a practical implication for engagement choice: you cannot choose the 
right engagement before you have established both states. An organisation that jumps directly to 
"we need a red team exercise" may have already decided on a solution before examining the problem. The solution 
may be correct. Or it may be addressing the visible symptom of a gap that sits somewhere else entirely.

The sequence that consistently produces better choices runs through three steps: surface the desired state, surface 
the current state honestly, then examine the gap. The engagement choice follows from the gap, not from assumptions 
about it.

## Surface the desired state first

A [forward-looking workshop](../workshops/forward-looking.md) is a good starting point. It asks what the organisation 
wants to be able to do that it cannot do today, what the threat landscape looks like in twelve to eighteen months, 
and what conditions would need to be true for the security programme to be considered genuinely adequate.

This is not a risk register exercise and it is not threat modelling. It is a structured choreography for making the 
desired state explicit rather than leaving it implicit and therefore untestable. Weinberg's observation applies here: 
when a group works through what they expect and want, they are revealing the assumptions they are currently operating 
on. Those assumptions are the first things worth examining.

## Surface the current state honestly

A [temperature reading retrospective](../workshops/retrospectives.md) surfaces the currently perceived state: what is 
actually working, what is not, where energy is low, what people know but have not said in a formal setting. It is 
distinct from a report or a maturity assessment because it captures experience, not just compliance status.

Where the current state is less well understood, further investigation may be needed before the gap can be 
characterised. This might be a technical assessment, a series of conversations with the people closest to the work, or 
a small ChangeShop-style process that brings the real problems into the room rather than the sanitised versions.

The important thing is that the currently perceived state is established from what the system actually does, not from 
what it is documented to do. These are often different.

## Examine the gap

The gap between the desired state and the current state is the problem to address. Its nature determines which 
engagement fits.

If the gap is about unknown or unvalidated detection coverage, the relevant engagement could be a purple team exercise or red team assessment. The organisation believes it detects certain things and wants to know whether that belief is accurate.

If the gap is about procedure and coordination under pressure, a tabletop or live simulation could be the right fit. The procedures may exist on paper; the question is whether the team can follow them when conditions are difficult.

If the gap is about understanding the threat landscape against the current architecture, a threat modelling workshop will likely produce the most useful output. It tests the organisation's model of its own attack surface rather than its operational response to attacks.

If the gap is about the relationship between current controls and a regulatory or framework requirement, a risk or audit engagement might be what is needed. It addresses the rational layer of the posture.

If the gap is primarily in the emotional or political layer, which [PSL describes](../foundations/problem-solving/in-security.md) as people not following a process they know exists, or findings not being acted on despite being clearly documented, then a technical engagement is unlikely to close it. The engagement that is a best fit is one that examines the conditions: why the procedure is not being followed, who has the authority to change the incentive structure, and which a follow-up choreography could surface about the real constraints.

## Choose again

[Backward planning](../workshops/backward-planning.md) sits well after the problem is clear. It takes the findings and works backwards from the desired state, surfacing the dependencies and obstacles on the path from where the organisation actually is to where it wants to be.

This engagement may update the picture of the current state and the desired state, but mostly gives paths for making the necessary changes. 

It is how capable organisations work: iteratively, with each intervention producing a better understanding of the system, and each understanding informing a better next move.

## Related

- [Forward-looking processes](../workshops/forward-looking.md)
- [Temperature reading retrospectives](../workshops/retrospectives.md)
- [Backward planning with obstacle avoidance](../workshops/backward-planning.md)
- [What ChangeShop is](../foundations/change-management/what-it-is.md)
- [PSL applied to security work](../foundations/problem-solving/in-security.md)
- [Objectives](objectives.md)
