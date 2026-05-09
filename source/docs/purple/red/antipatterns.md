# Common red team antipatterns

A few patterns appear in red team programmes often enough to be worth naming. Most have the property of being more visible to outsiders than to the team practising them.

## Antagonistic mindset

A red team treating the blue team as an adversary, hiding findings to "win", or mocking defensive failures, is a red team that has misunderstood the purpose of the exercise. The defenders being tested are colleagues, not opponents. Findings become useful when they are shared in a form that lets defenders act on them, and humiliating disclosure produces the opposite of that.

The shift away from this pattern is not a question of personality. It is a question of how the programme is framed by leadership: whether the red team's measure of success is defensive improvement or evasion-rate. Programmes that reward evasion produce evasive teams. The framing question is upstream of the behaviour.

## Over-reliance on automation

Running automated exploit frameworks without understanding what they generate produces an exercise that is hard to debrief. The blue team detects activity but cannot tell what was tested. The red team cannot explain why something was or was not detected. The findings are noisy and hard to act on.

The remedy is depth on the tools being used: knowing what network traffic they generate, what logs they produce, what defenders would see if the detection were working. This is slower than running a framework and reading the output, and is what turns the output into something useful.

## Ignoring defensive wins

Reporting only successful attacks, with no record of the controls that worked, is a common pattern in reports designed to demonstrate the value of red teaming. It produces a misleading picture: every defensive investment looks ineffective because the report mentions only the failures.

Documenting what worked, MFA blocking credential stuffing, EDR catching a payload, segmentation limiting lateral movement, gives leadership the information needed to make further investment decisions. It also strengthens the relationship between the red and blue functions, which is a precondition for the next exercise to produce more honest findings.

## Scope creep

Expanding testing beyond agreed boundaries because something interesting was found is a structural failure mode of red teaming. The interesting finding may be real and worth pursuing, but pursuing it through unauthorised investigation is the wrong path. The agreed scope was agreed for reasons; expanding it unilaterally undermines the trust that makes the next engagement possible.

The disciplined response is to follow the established escalation process. Critical findings outside scope are disclosed responsibly to the appropriate authority, who then decides whether to authorise expanded testing or to address the finding through a different channel.

## Poor documentation

Incomplete notes, missing timestamps, inability to reconstruct what was done: these are the antipatterns that turn an exercise into a learning event nobody can learn from. The blue team cannot build detections for actions it cannot reconstruct. The red team cannot validate that a new detection caught the same technique on retest if the original technique is not documented precisely enough.

Documentation that feels excessive during the engagement is usually about right when the post-exercise reflection begins. The opposite calibration usually applies when the exercise is being remembered six months later.

## Unrealistic operations

Using techniques that real adversaries would not, massive network scans that any monitoring tool would catch, obvious malware variants, loud exploitation, produces exercises that test the team against a fictional opponent rather than the actual threat landscape.

Tradecraft is worth matching to the threat model. APT-class groups operate differently from ransomware affiliates. Emulating the threats an organisation actually faces produces exercises whose findings translate into defensive improvements; emulating an idealised attacker produces findings that are interesting in isolation and operationally irrelevant.

## Related

- [Common anti-patterns and pitfalls](../practice/antipatterns.md)
- [Ethical boundaries and rules of engagement](ethics.md)
- [Coordinating with purple team](coordination.md)
- [Why simulations fail](../../social-engineering/why-simulations-fail.md)
