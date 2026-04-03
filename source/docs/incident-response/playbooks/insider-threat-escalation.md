# Insider threat escalation

*For SOC, SIRT, HR, and security operations. Multi-phase live exercise with a simulation actor: 3-4 hours.*

The scenario exposes the operational gap between security monitoring capability and response authority. SOC may detect anomalous behaviour within minutes. The decision to act on that detection involves HR, legal, and management in ways that the security team has typically not practised. The scenario makes that coordination concrete and time-pressured. The second thing it exposes is the assumption embedded in most insider threat models: that the organisation will be able to observe, investigate, and act as a coherent unit. In practice, those three activities involve different teams with different timelines, different obligations, and occasionally different interests.

## The scenario

A simulation actor, playing a malicious insider, uses a test account to perform realistic insider threat behaviours over the course of the exercise: logging in from an unusual location, accessing systems outside their normal work scope, downloading sensitive documents, attempting access to restricted areas during off-hours. The participating teams know a simulation is happening today. They do not know the timing or nature of what is coming, and the actor's identity is not revealed until the debrief.

The scenario moves through four phases. The first hour is anomaly detection: the SOC needs to notice something is wrong, investigate without alerting the insider, and decide when to escalate. The second hour is coordination: the SIRT brings in HR, whose constraints change what the security team can do. The third hour is confrontation and containment: the evidence is conclusive, the insider may have noticed they are being watched, and the team executes containment. The final phase is aftermath: evidence collection, reporting, regulatory obligations, and review of what failed.

## Preparing the exercise

Preparation is part of the exercise. Before running it, identify what a realistic baseline of activity looks like for the test account, so the actor's deviations stand out against it. Brief the actor on how actual insider threat behaviour progresses, it is rarely dramatic and usually involves legitimate access used for illegitimate purposes, gradually escalating in boldness. Coordinate with HR on what constraints they will introduce: this works best when it reflects real policy, not a simulation of policy. The HR participant is not playing an obstacle role, they are representing constraints the security team will encounter in a real case.

Establish hard safety boundaries before starting: no access to production systems, no real data, a clear stop word. These are not formalities. A live exercise with an actor and real communication channels can produce situations that require immediate de-escalation, and having the stop word established in advance makes that possible without confusion.

## Running the exercise

The facilitator's job during the detection phase is to observe without intervening. How long does it take the team to notice? What triggers escalation to investigation? Do they act immediately or continue to monitor? These reveal the team's actual instincts and the monitoring configuration's actual sensitivity, not what the team believes about either.

The coordination phase is where the exercise becomes most productive. Watch the moment when security wants to act and legal wants to wait. The team will be tempted to treat the legal constraint as an obstacle to route around. The more useful response, which the debrief can support, is to understand why the constraint exists and what process would let the team act within it. [Facilitation over instruction](../../foundations/montessori/facilitation.md) applies here: the facilitator's job is not to resolve the tension but to ensure the team works through it rather than around it.

The actor's behaviour works best when realistic rather than theatrical. Actual insiders do not announce themselves. The detection requires genuine attention to anomaly, not pattern-matching against an obvious villain.

## Debrief

Begin with the actor's account of what they did and what they noticed about the team's response. This is unusual in debrief structures but consistently produces the most useful learning. The team discovers whether their detection and investigation were visible to the actor, whether their hesitation at key decision points was longer than it needed to be, and whether their containment approach was sound from the insider's perspective.

Then the team's account: what did they observe and when? Where did they hesitate and why?

Then the structural questions:

How long between the first anomalous behaviour and detection? What would need to change for that window to be shorter?

At what point did security and HR find their response logic in tension? Was there any pre-established guidance for that situation, or was it being invented under pressure?

Who had authority to revoke the account? Was that known before the exercise?

What did the investigation reveal about the monitoring posture? Were the logs adequate? Were they actually reviewed?

The insider threat scenario is uncomfortable because it requires holding two things simultaneously: genuine respect for employee rights and a security response that may be adverse to the employee. The exercise does not resolve that tension. It makes it concrete so it can be addressed structurally rather than improvised when time matters.

## Outputs

A clear record of detection timing and what triggered it. An assessment of whether cross-team response coordination between security, HR, and legal is functional or theoretical. Any clarification needed on account access revocation authority. Specific monitoring improvements that would enable earlier detection of the behaviours exhibited.
