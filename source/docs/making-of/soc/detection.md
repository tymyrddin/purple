# Detection and response

Detection without coordinated response is situational awareness with no consequences for the adversary and no benefit for the organisation. Response without detection is hoping that incidents announce themselves. The two functions need to be designed together even when they are operated by different people.

## The detection model problem

Every detection rule encodes an assumption: that a particular pattern of behaviour indicates a threat, that a particular threshold of activity is anomalous, that a particular log source is reliable enough to act on. Those assumptions are accurate when the rule is written. They drift because the environment changes, because adversaries adapt, and because the rule was written against a threat model that has since evolved.

The [SEM](../../foundations/system-effectiveness/index.rst) principle here is that errors are model failures. A rule that fires on benign activity and generates noise is a model that has drifted from reality. A rule that fails to fire on malicious activity that it was designed to catch is a model failure of a different kind, and one that is harder to notice because silence does not announce itself. Both types of failure deserve the same investigative attention.

Treating detection as a managed model rather than a set of installed rules means: explicitly documenting what each rule is intended to catch and on what assumption, reviewing rules regularly against what is being observed, and treating false positive and false negative findings as evidence about model accuracy rather than as housekeeping items.

## Triage and escalation

The objective of triage is to distinguish events that warrant investigation from events that do not, as quickly and accurately as possible. The constraints on triage are attention (analysts can process a limited number of alerts before quality degrades), information (the triage decision depends on context that the alert may not provide), and time (events that require containment deteriorate if triage is slow).

Assigning risk levels to alerts based on impact and urgency only works if the criteria for those levels are explicit and shared. An implicit threshold that analysts learn informally will be applied inconsistently across analysts and over time. Document the criteria, test them against real cases, and update them when the cases reveal that the criteria are wrong.

Escalation criteria need the same explicitness. "Critical alerts go to SIRT immediately" requires a definition of critical. The definition needs to be specific enough to apply without requiring a senior analyst to make the call in every case, while remaining accurate enough that genuine critical events reach the SIRT without delay.

## Coordination with the SIRT

The boundary between SOC and SIRT is where incidents pass from detection to response. That boundary needs to be explicitly designed, not left to emerge from practice. What information does the SIRT need from the SOC when an incident is handed over? What does the SOC continue to do once the SIRT is engaged? When does the handover happen, and how?

Regular joint exercises keep the handover process functional. The first time a handover happens under real incident conditions is too late to discover that the communication channels are unclear or that the information the SIRT expects is not in the format the SOC provides.
