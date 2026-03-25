# Adversary emulation vs. vulnerability testing

Red teaming has different flavours depending on objectives.

## Adversary emulation

Purpose: Simulate specific threat actors relevant to your organisation.

Approach: Research real adversary TTPs from threat intelligence. Replicate their tools, techniques, targeting, and operational patterns. Test whether defences detect and stop those specific adversaries.

Example: If APT29 targets your sector, emulate their preference for Living-off-the-Land techniques, their credential theft methods, their command and control protocols.

Value: Validates defences against realistic, known threats. Prioritises defensive improvements based on actual adversary behaviour.

## Assumed breach

Purpose: Test detection and response after initial compromise.

Approach: Start exercise with access already granted (simulated phishing success, provided credentials, physical access). Focus on post-exploitation, lateral movement, and detection capabilities.

Value: Tests blue team's ability to detect attackers already inside. Validates monitoring, alerting, and response procedures.

## Full-scope red teaming

Purpose: Test entire defensive programme from reconnaissance through impact.

Approach: No holds barred (within rules of engagement). Use any ethical and legal technique to achieve objectives. Includes social engineering, physical access, supply chain attacks.

Value: Most realistic test of organisational resilience. Reveals unexpected attack paths and cascading failures.

## Focused technical testing

Purpose: Test specific defensive controls or technologies.

Approach: Constrained scope focusing on particular systems, controls, or detection capabilities. Might test EDR effectiveness, network segmentation, privileged access controls.

Value: Provides detailed feedback on specific security investments. Validates vendor claims and configuration effectiveness.

