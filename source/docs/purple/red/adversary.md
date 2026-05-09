# Adversary emulation vs. vulnerability testing

Red teaming has different flavours depending on objectives. The choice of flavour shapes what the exercise can find and what it cannot.

## Adversary emulation

Adversary emulation simulates a specific threat actor relevant to the organisation. Real adversary techniques, drawn from threat intelligence, are replicated: their tooling preferences, their typical targeting, their operational patterns, their command-and-control protocols. The exercise tests whether existing defences detect and stop those particular adversaries rather than a generic threat.

If APT29 targets the sector, the emulation reflects APT29's preference for living-off-the-land techniques, their credential-theft methods, their command-and-control protocols. The output validates defences against realistic, named threats and prioritises improvements based on adversary behaviour the organisation is actually likely to encounter.

## Assumed breach

An assumed-breach exercise starts after initial access has already happened. The simulated phishing succeeded, credentials were provided, physical access was granted. The focus is on post-exploitation, lateral movement, privilege escalation, and the detection capabilities that operate inside the perimeter rather than at it.

The value is in testing what most exercises skip: the visibility gap between perimeter detection (which is usually mature) and post-compromise detection (which is often less so). Monitoring, alerting, and response procedures get exercised under conditions that resemble the second day of a real incident rather than the first.

## Full-scope red teaming

Full-scope red teaming tests the entire defensive programme from reconnaissance through to impact. No specific technique is excluded within the rules of engagement. Social engineering, physical access, supply chain attacks, and any other ethical and legal technique is in scope.

This is the most realistic test of organisational resilience and the most expensive to run. It reveals unexpected attack paths, cascading failures across functions, and the gaps between defensive controls that no narrower test would have surfaced. It also produces the most uncomfortable findings, which is information about both the defences and the organisation's appetite for honest assessment.

## Focused technical testing

Focused technical testing constrains the scope to a particular system, control, or detection capability. EDR effectiveness, network segmentation, privileged access controls, or a specific detection rule become the explicit subject of the exercise.

The narrower scope produces detailed feedback on a specific security investment. Vendor claims and configuration choices are validated against actual adversary behaviour rather than against the marketing materials. The trade-off is that findings are local to the tested control and do not address how it interacts with the rest of the defensive programme.

## Related

- [Offensive mindset and methodology](mindset.md)
- [Adversary persona workshop](../../threat-modelling/adversary-persona-workshop.md)
- [Attack path mapping](../../threat-modelling/attack-path-mapping.md)
- [Crafting scenarios](../../threat-modelling/crafting-scenarios.md)
