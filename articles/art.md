
This is not incompetence. It is the system behaving exactly as it did before, including in the room where the review takes place.

## Describing the incident instead of explaining it

Most incident post-mortems or retrospectives reconstruct the sequence of events. What happened, in what order, and 
what should have been done differently. Useful, but shallow.

The more important question is usually skipped: what had to be true about the organisation for this to happen at all?

An incident is not a deviation from normal operations. It is normal operations with one assumption exposed as false.

The phishing email was not an anomaly. It was the expected outcome of a filtering posture tuned to yesterday’s threat 
landscape. The missed lateral movement was not bad luck. It was the expected outcome of a detection model that no 
longer matched the network it was supposed to observe.

If you only fix the sequence, you leave the structure intact. The system will produce the same class of failure 
again, just with slightly different timestamps.

## Why honest reviews rarely happen

Incidents do not occur in a vacuum. Systems have owners. Decisions have history. Contracts have signatures on them.

In the review, those realities are present.

Under pressure, people default to safe behaviour. The technical specialist gives a precise, detailed timeline that 
somehow avoids naming the decision that set the conditions. The manager agrees everything is important, and nothing 
material changes. The team blames the phishing email rather than the posture that let it through.

This is not a failure of individuals. It is a predictable response to an environment where naming the real issue has 
consequences.

So the review produces documentation. Not understanding.

## What a useful review actually does

A useful review updates the organisation’s model of itself.

That means asking different questions:

* What had to be true for this to happen?
* How long has that been true?
* What would need to change for the same attack to fail differently next time?
* What did the situation look like from where the decision was made?

This shifts the focus from error to context. Not who missed it, but what they were working with, and why that made 
sense at the time.

For that to work, the conditions matter more than the format:

* The review is explicitly separate from performance evaluation
* The facilitator has no stake in the outcome
* The focus is on system behaviour, not individual blame

Get that wrong, and no framework will save you. Get it right, and people will say things that do not appear in any 
dashboard or report, but explain everything.

## How to tell if it is working

You do not need maturity models for this. The signals are obvious.

Leading indicator: the nature of the actions.

* Procedural: update a runbook, add a step, send a reminder
* Structural: change visibility, decision rights, system design

If most actions are procedural, you are producing paperwork.

Lagging indicator: recurrence.

If the same class of incident keeps returning in slightly different forms, your reviews are not reaching the 
conditions that generate them. You would be trimming symptoms.

## Where to start

The difficult part is not templates or facilitation techniques. It is making it possible to say true things without 
those truths being used against the people who say them.

That is not a security problem. It is an organisational one.

It requires explicit backing from leadership and consistent proof that honest reporting leads to better outcomes 
than safe reporting.

Once that condition exists, the rest is almost trivial. People already understand far more about how the system 
actually works than any document suggests. The review is simply where that knowledge is allowed to surface.

Get the conditions right, and the insights follow. Get them wrong, and you will keep writing excellent reports about 
the same failures.