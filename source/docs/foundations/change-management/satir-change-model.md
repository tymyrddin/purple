# The Satir Change Model in practice

The Satir Change Model matters in ChangeShop because it names the phase where change most often dies.
Not because the destination was wrong, and not because the people involved were incompetent or obstructive.
Because organisations reach the chaos phase, interpret the drop in performance as evidence of failure, and
retreat to the old status quo before the new one has had time to form.

This pattern is consistent across contexts. It appears in infrastructure migrations, security programme overhauls,
team restructures, and phishing simulation redesigns. The surface details differ. The shape does not.

## The chaos phase is not optional

Chaos in the Satir model is not a sign that something has gone wrong in the implementation. It is a structural
feature of real change. Old habits no longer work. New habits are not yet established. People are operating in
the gap between them, and performance reflects that.

In a pipeline rollout, chaos looks like this: deployments break for reasons that are not immediately clear,
access permissions block work that was previously unblocked, someone re-introduces the manual workaround that the
pipeline was supposed to replace. Pipelines are re-run without knowing why they failed. YAML is debugged at
unreasonable hours. The staging environment is wiped by accident, or production, if the project is ambitious.

In a phishing programme redesign, it looks like this: click rates rise when realistic techniques replace
obvious simulations. Credential submissions appear in systems where none existed before. The SOC receives more
noise. Reporting pipelines are tested by actual activity and frequently break. Staff who previously felt
competent discover that they cannot reliably distinguish safe from unsafe.

In both cases the temptation is identical: "we made things worse." This conclusion is available at the chaos
phase of almost every meaningful change, and it is almost always wrong. What has changed is not the actual risk,
but the visibility of it.

## What survival looks like

Getting through the chaos phase requires a specific kind of organisational behaviour that does not come naturally.

Accepting a performance drop and communicating that it is expected is harder than it sounds when leadership is
watching metrics and asking questions. The alternative, pretending the drop is not happening or promising it
will resolve faster than it can, is worse, because it removes the possibility of realistic planning and
undermines the credibility of whoever made the promise.

Over-communicating during chaos is necessary because people will still misunderstand, miss the message, or
apply it to circumstances that were not covered. The instinct to communicate less when things are difficult is
precisely backwards.

Providing structure without pretending everything is under control is a delicate balance. People need enough
stability to function, but false reassurance about the timeline or the difficulty of integration produces
cynicism when reality diverges from the claim.

Removing backdoors is harder still. In a pipeline project, this means not quietly re-enabling SSH access when
deployments stall. In a phishing programme, it means not reverting to easier simulations when click rates rise.
The backdoor is comfortable because it removes the immediate pressure. It also removes the reason to develop the
capability that makes the change worthwhile.

Supporting early adopters matters disproportionately. The people who move into integration ahead of others are
practical demonstrations that the new system is survivable. They answer questions their peers will not ask a
facilitator, and they reduce the perceived risk of committing to the change.

## What the metrics look like

During the chaos phase, the metrics will look worse. This is the correct reading of the situation, not a failure
of measurement.

A phishing programme that moves from obvious simulations to realistic techniques will produce higher click rates
at first. This is not evidence that staff have got worse at recognising phishing. It is evidence that the previous
programme was measuring recognition of yesterday's scams rather than resilience against current ones. The worse
metrics are more accurate metrics.

A pipeline project that makes deployment failures visible will produce a higher reported failure rate at first.
This is not evidence that deployments have become less reliable. It is evidence that failures which were previously
absorbed through manual intervention are now being surfaced. The worse metrics are more accurate metrics.

Framing this correctly, as visibility rather than regression, is the communication work that determines whether
an organisation interprets the chaos phase as progress or failure.

## The uncomfortable parallel

Both transformations follow the same shape: a comfortable fiction is replaced by a painful reality, which is
replaced, if the organisation does not retreat, by a usable system.

The organisations that stop at the painful reality retain the comfortable fiction. The ones that do not end up
with actual capability: repeatable deployments, staff who report rather than guess, defences that evolve with
attacker techniques, and metrics that reflect the real state of the environment rather than the state an
organisation would prefer to believe it is in.

The Satir model does not tell you how to design the change. It tells you where support is needed and what
the pressure to abandon the change actually means. That is the part most change efforts fail to account for.

## Related

- [The Satir Change Model](../organisational-development/satir-change-model.md)
- [Why security change stalls](why-change-fails.md)
- [Why simulations fail](../../social-engineering/why-simulations-fail.md)
- [The pipeline as a change](../../systems-engineering/pipeline.md)
- [Building a phishing programme that actually works](../../social-engineering/phishing-programme.md)