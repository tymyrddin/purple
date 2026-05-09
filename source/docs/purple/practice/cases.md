# Case studies and examples

What follows are three composite scenarios drawn from purple team programmes at different points in their development. The names and specifics have been changed; the patterns are real.

## Ransomware simulation

The scenario tested an organisation's ability to detect and respond to a ransomware attack from initial phishing through to attempted lateral movement and simulated encryption of test files.

The red team obtained initial access through a phishing email that the user clicked, dumped credentials with Mimikatz, attempted lateral movement to file servers, and ran simulated encryption against a designated test directory. The exercise included no real-data encryption.

The blue team missed the phishing event itself: the user clicked the link before any control caught it. The EDR detected the Mimikatz execution and generated an alert. The SOC began investigation within fifteen minutes, identified the activity as malicious, and contained the affected accounts before the lateral movement could spread to file servers.

The findings divided into things that worked and things that needed attention. Email filtering had not caught the initial phishing, suggesting either the lure was sophisticated enough to evade existing detection or the filters were less effective than the previous report had suggested. EDR detection of credential dumping worked well. Response coordination between SOC and IR was fast enough to prevent the simulated encryption from spreading beyond the initial system. Backup procedures were untested during the exercise, which became the most important finding: nobody knew whether the recovery side of the response would work.

The improvements that followed were proportionate. Email security awareness training was updated to include the lure type that succeeded. Backup restore procedures were tested for the first time at the scale a real ransomware incident would require. New lateral movement detection rules were added based on what the red team had attempted. The ransomware response playbook was rewritten with the gaps the exercise had revealed.

The next exercise showed faster detection of the equivalent phishing pattern and prevented lateral movement entirely.

## Insider threat detection

The scenario tested the ability to detect a malicious insider with legitimate access who was systematically collecting and staging sensitive data for exfiltration.

The red team operated with provided credentials, simulating an existing insider rather than a compromised external account. Activity was kept within the bounds of the simulated insider's normal job function, with gradual escalation toward sensitive data access and a final staging step in preparation for exfiltration.

The blue team did not detect the early activity, because nothing about it deviated from a baseline of normal access. UEBA flagged unusual data access patterns several hours into the simulation, when the cumulative profile of the activity began to diverge from the baseline. Investigation revealed the systematic collection pattern and the response team contained the account within two hours of the initial UEBA flag.

The findings showed both strengths and gaps. Behavioural analytics worked as designed, but with a delay that would be costly in an actual incident. Manual investigation skills were strong; the analyst who pulled the threads together produced a clear picture of the activity. Response time was acceptable for an exercise but worth improving for a real incident. Data access monitoring had gaps that allowed the early collection phase to pass undetected.

The improvements covered enhanced data access logging, new insider threat hunt playbooks, automated alerts for bulk data access, and the addition of DLP controls at the points the staging activity had used.

Subsequent testing detected anomalies considerably earlier in the cycle.

## Supply chain compromise

The scenario simulated a compromised vendor account with legitimate access to monitoring infrastructure, testing the organisation's ability to detect when trusted access is being used outside its agreed scope.

The red team used vendor credentials to access monitoring systems, conducted reconnaissance of the network from the trusted position, and attempted to leverage that access for broader compromise of internal systems.

The blue team's network anomaly detection flagged unusual API calls from the vendor account. The SOC investigation revealed that the access pattern fell outside the vendor's normal scope of work. A confirmation call to the vendor identified the activity as suspicious. Access was revoked and credentials were reset.

The findings indicated that third-party access monitoring was effective for this kind of scenario. Vendor communication procedures worked as documented. The baseline of normal vendor behaviour, which was the precondition for the anomaly detection to fire, turned out to be the most important asset in the response, and it had been built largely informally rather than as a planned control.

The improvements that followed formalised what had previously been informal: documented vendor access baselines, enhanced monitoring of third-party API usage, vendor security requirements written into contract language, and a vendor incident reporting clause that gave both sides a defined path when something looked wrong.

## What recurs across organisations

The findings in the case studies above are specific to those organisations. Some patterns recur often enough across many programmes to be worth naming.

Living-off-the-land technique detection is generally weaker than detection of recognisable malware, because the techniques use legitimate tools that produce legitimate-looking activity.

Cloud environment visibility is generally less mature than on-premises visibility. The attack surface is different and the logging baseline often lags the operational migration.

Supply chain security is inconsistent. Some organisations monitor third-party access closely; others have not begun. The variance is wide and the failure mode is structurally similar to the insider scenario.

Incident response coordination needs practice rather than documentation. Procedures written and approved without being run frequently are procedures that fail under pressure.

On the other side, EDR controls catch most common malware, MFA prevents the majority of credential stuffing, network segmentation limits lateral movement when it has been implemented thoughtfully, and security awareness training does measurably reduce phishing success rates.

The cultural observations that recur are also worth naming. Blameless culture enables faster improvement, because the people who saw what happened are willing to describe it accurately. Regular exercises build team confidence and reduce the panic response that comes from a first encounter with a novel technique. Metrics demonstrate progress to leadership, which is what protects the programme during the next budget cycle. Purple teaming catches gaps before audits do, which sometimes saves the organisation from regulatory consequences and sometimes is just less embarrassing.

## Related

- [Coordination models](../coordination.md)
- [Common anti-patterns and pitfalls](antipatterns.md)
- [Maturity progression](maturity.md)
- [Building a phishing programme that actually works](../../social-engineering/phishing-programme.md)
