# Why phishing simulations often fail

Most security awareness programmes have a structural flaw: they teach people to recognise phishing emails drawn
from vendor training libraries, which are typically six to eighteen months behind what is actually arriving at
your organisation.

The obvious typo. The generic "your account has been compromised" subject line. The suspicious link to a newly
registered domain with no certificate. These are training artefacts, not current threats.

People who fail these simulations learn to look for the wrong signals. People who pass them gain confidence in
the wrong instincts.

Meanwhile, real campaigns have moved on. QR codes embedded in PDFs evade URL scanning entirely. Credential
harvesting pages sit on legitimate Microsoft infrastructure, blending into trusted domains.
Adversary-in-the-middle proxies capture session tokens after MFA completes, rendering the second factor largely
decorative. If your simulations do not use these techniques, they are not preparing people for what is actually
arriving.

## The mismatch between what you test and what you defend

A simulation designed to bypass email filters in order to guarantee delivery is not testing your security
posture. It is testing whether people click links in a vacuum.

Phishing is a system problem: detection, reporting, and response are interconnected. If a simulation does not
run through live defences or reflect current attacker techniques, it teaches nothing useful about either people
or systems. Most programmes fail on both counts.

The result is a programme that generates a metric, click rate, that measures recognition of vendor training
templates, and reports that metric to management as evidence of security posture. It is not. It is evidence that
people can identify the kind of phishing that no longer gets used.

## The Satir arc through a simulation programme redesign

Replacing a compliance-theatre simulation with a threat-intelligence-driven programme follows the same change
arc as any significant disruption to established practice.

The late status quo is comfortable: annual simulation, predictable templates, click rates that trend downward
year on year as people learn to recognise the templates, a reassuring line on a chart.

Resistance arrives when you introduce realistic techniques. "This is too realistic." "People will fail more."
"This will look bad in reports." These are accurate observations, not objections to be managed. Click rates will
rise. Credential submissions will appear in systems where none were recorded before. The metrics will get worse
before they get better, and worse metrics will require explanation.

Chaos follows: the SOC receives more noise, reporting pipelines are tested by activity they were not expecting
and frequently break, staff who previously felt competent discover they cannot reliably distinguish safe from
unsafe. The dangerous thought arrives: "we made things worse." You did not. You removed the blindfold.

Integration begins when people who played attacker in purple team exercises become better reporters as
defenders. Reporting rates rise. Detection tuning improves because the detection gaps are now visible rather
than hidden behind a simulation that was never going to surface them. Metrics become meaningful because they
reflect the real state of the environment.

The new status quo is a programme that evolves with attacker techniques, measures things worth measuring, and
treats security as a habit rather than a training module.

## What the metrics actually measure

Trends matter more than point-in-time results.

Click rate indicates susceptibility. Credential submission rate indicates actual risk. Defender catch rate shows
whether controls are keeping pace with the techniques being used. Report rate measures whether staff actively
participate in detection rather than passively hoping someone else will notice.

Declining submissions and rising report rates show behaviour change. Variation in detection rates across
techniques indicates whether controls adapt or stagnate. Departmental breakdowns allow targeted follow-up
rather than blanket repeat training for the whole organisation.

An annual simulation gives a snapshot. A monthly programme shows direction.

## Integration with security operations

The programme's value multiplies when simulated reports flow through the same intake and triage process as real
incidents. This exercises the response pipeline continuously rather than waiting for an actual incident to
reveal that the pipeline does not work as expected. Credential submission patterns inform identity and access
decisions. Detection gaps become concrete tuning cases for the email filtering stack.

At that point you are no longer running a training programme. You are running a live, recurring systems test.

The goal is not zero clicks. The goal is an organisation that detects quickly, reports consistently, and adapts
continuously. A programme built on real techniques, exercised in a real environment, is the fastest path to
that outcome without waiting for a real incident to teach the lesson.

## Related

- [The Satir Change Model](../foundations/organisational-development/satir-change-model.md)
- [The Satir Change Model in practice](../foundations/change-management/satir-change-model.md)
- [Phishing-resistant controls](https://blue.tymyrddin.dev/docs/purple/begin/human/phishing-resistant)
- [Attack simulation runbooks](https://blue.tymyrddin.dev/docs/ngo/awareness/attack-simulation)