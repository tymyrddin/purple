# Caveats and scope

What the direction is not, stated plainly, so the claim is not read wider than it is.

## Not physics

The design inherits the substrate framing whole: it reproduces the evidence an estate emits, not the
electrical behaviour behind it. It never computes a fault current or a load flow, and the band where the
physical dynamics themselves are the evidence sits outside it, as [feasibility](feasibility.md) and
[simulation-substrate](simulation-substrate.md) already set out. Questions that need hardware-in-the-loop
stay out of scope.

## Not detection, not the wire

This is not a monitoring product and does not watch live traffic. It reasons about a record after the fact,
or about the capacity of a record before any fact. The moment-to-moment question detection tools answer is
not the one being asked. The direction sits at the level of observability of a difference in the retained
record, not signature-matching on the network.

## Not accreditation

A capability report is not a compliance certificate and does not attest that an operator meets NIS2. It
states which determinations an estate's record can and cannot support. Whether a regulator or an operator
treats that as evidence toward the Article 21(2)(f) effectiveness duty is their call, not a claim the tool
makes for itself.

## Local, no telemetry

The direction is meant to run locally against an estate configuration and a generated record. It does not
phone home, does not need the operator's live data to leave the operator, and produces no telemetry of its
own. The estate configuration it reads can be as sensitive as the operator chooses to make it, which is a
reason to keep the computation on the operator's own ground.

## Relative to an enumerated set

The verdict, structural layer included, is relative to the explanations enumerated for a class of incident.
It answers "can these explanations be told apart at this estate", not "is there any conceivable account this
record could not distinguish". An explanation left off the list cannot be weighed, and the design does not
discover the explanations for you. The [open questions](evidentiary-capability-open-questions.md) and
[risks](evidentiary-capability-risks.md) pages both return to this, because it is the boundary most easily
forgotten.

*Last updated: 12 July 2026*
