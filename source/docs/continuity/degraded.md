# Degraded operations

Some continuity plans assume binary states: running, or not running. The interesting territory is the long middle in 
which something is half-broken and the organisation is half-working.

A degraded operation is the work that proceeds while something is broken. This can mean:

- manual processes restored where automation has failed
- a subset of customers served while others are deferred
- read-only access while write paths are being recovered
- a tier-two team performing a tier-one function with longer cycle times
- a process running with stale data because the upstream feed is down
- a region serving requests that another region would normally handle

None of these are the full service. None of them are an outage. They are the operating mode
where most of the continuity work happens, and where most plans are quietest.

## The messy middle is the test

A ten-minute outage where the runbook works as written, rarely tests the continuity posture
seriously. The plan covers it because the plan was written for it.

A harder test is a three-day partial degradation where three different runbooks
half-work, where communications drift between teams, where the question "are we actually in
an incident right now" goes unanswered for forty minutes because nobody wants to be the one to
declare it. That is the regime in which the plan either holds or quietly fails.

Organisations often rehearse the first kind because it is easier to design and easier to
grade. The second kind is harder to script and harder to score, which is why it is rarely
rehearsed, and may be why it is so often where the real failures happen.

## Three questions per activity

For each business-critical activity, the design questions for degraded operations are:

What does the diminished version look like? Concretely: what subset of inputs, what subset of
outputs, what acceptable cycle time, what acceptable data freshness, what acceptable error
rate.

Who is authorised to declare that the activity is in degraded mode? Not who runs it, but who
owns the decision to drop from full service to reduced service. This person is often
unspecified, which is why the decision tends to be made implicitly by whoever notices first.

How does the organisation know when to come out of degraded mode? This is frequently the
skipped question. Organisations are usually better at entering degraded mode than at leaving
it. The diminished service can quietly become the new normal, the workaround becomes the
process, and a year later the original full-service mode may no longer be operationally
feasible because nobody remembers how it worked.

## Workarounds that calcify

Temporary measures during disruption tend to outlive the disruption. A manual process
introduced for a week tends to persist for months. A bypass put in place during recovery tends
to remain in place because removing it requires effort that nobody is funding now that the
incident has been declared closed.

This is not a moral failure. It is what tightly loaded systems do under pressure. A plan that
pretends otherwise can quietly produce permanent degradation by accident.

A useful continuity programme tracks workarounds explicitly: what was put in, when, by whom,
under what authority, with what intended end date, and what the test of removal looks like.
Without that record, the workarounds may disappear into the architecture and become
tomorrow's unexplained dependency.

## Related

- [Operational dependency mapping](dependencies.md)
- [Recovery objectives](objectives.md)
- [Monday morning](monday-morning.md)
- [Incident choreography](../incident-response/choreography.md)