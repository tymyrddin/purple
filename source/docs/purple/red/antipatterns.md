# Common red team antipatterns

## Antagonistic mindset

Problem: Treating blue team as the enemy, hiding findings to "win", or mocking defensive failures.

Better: Red team exists to improve defences, not humiliate defenders. Collaboration produces better security than competition.

## Over-reliance on automation

Problem: Running automated exploit frameworks without understanding what they do or considering operational security.

Better: Understand tools deeply. Know what network traffic they generate, what logs they create, how defenders might detect them.

## Ignoring defensive wins

Problem: Only reporting successful attacks and ignoring effective defensive controls.

Better: Document what worked. If MFA blocked credential stuffing or EDR caught a payload, that's valuable information proving security investments work.

## Scope creep

Problem: Expanding testing beyond agreed boundaries because "we found something interesting."

Better: Stay within scope rigidly. If you discover critical issues outside scope, follow the escalation process rather than investigating unauthorised systems.

## Poor documentation

Problem: Incomplete notes, missing timestamps, inability to explain exactly what was done.

Better: Document obsessively. Blue team can't learn from actions they can't reconstruct.

## Unrealistic operations

Problem: Using techniques real adversaries wouldn't (massive network scans, obvious malware, loud exploitation).

Better: Match tradecraft to threat model. APT groups operate differently than ransomware gangs. Emulate the threats your organisation actually faces.

