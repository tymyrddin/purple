# Scoping engagements

Scope defines what is in bounds and what is not. The practical purpose is clear: focused testing produces better findings than unfocused testing, and clear boundaries prevent accidents.

The less obvious purpose is that the scope negotiation itself is informative. What gets excluded, and why, reveals something about the organisation. Systems kept out of scope because they are too critical to risk testing are often the systems where the most consequential model failures live. The payment processing environment that cannot be touched is also the environment that has not been tested since the architecture changed. [SEM's observation about model drift](../foundations/system-effectiveness/core-triad.md) applies: the assumption that a system is secure ages silently, and scope exclusions are one of the mechanisms by which that ageing stays invisible.

This does not mean testing everything regardless of risk. It means treating the scope document as a finding in itself: where is the organisation unwilling to look, and what does that reveal about its model of its own security posture?

## Technical scope

Be specific about what can be tested. "Production environment" is not a scope; "the web application running on these servers, accessed via these endpoints, during these time windows" is. The specificity is not bureaucratic; it is what makes the engagement reproducible, attributable, and safe.

Define clearly what cannot be touched: payment systems, medical devices, safety-critical controls, regulated data stores. Define what attack vectors are permitted: active scanning, social engineering, physical access, supply chain simulation. Define the depth of permitted exploitation.

Time windows matter more than most scope documents acknowledge. Testing during a change freeze, a product launch, or peak trading hours is testing a different system from testing during normal operations. The conditions under which the engagement runs shape what it can find.

## Organisational scope

Which teams participate, and which are informed without participating? The answer shapes what the engagement can test. An engagement where only the SOC knows it is happening tests something different from one where the whole security function is aware, which tests something different again from a fully blind exercise where nobody on the blue side knows.

Third parties: can testing involve vendors, partners, or cloud providers? Usually not without explicit agreement, and obtaining that agreement is itself a useful exercise. The absence of a mechanism for doing so is a finding.

## Depth and intensity

How far can the engagement go after initial access? The answer to this question often reveals political constraints more than technical ones. An engagement that stops at identification and does not simulate exploitation is producing a different class of finding from one that runs the full attack chain. Both are valid. The choice is worth making explicit and deliberate rather than defaulting to the less uncomfortable option.

## Related

- [Objectives](objectives.md)
- [Rules of engagement](rules.md)
- [Safety and risk management](safety.md)
- [Systems, models, and errors](../foundations/system-effectiveness/core-triad.md)
