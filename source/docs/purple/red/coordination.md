# Coordinating with purple team

Effective purple teaming requires red team to work collaboratively, not antagonistically, with blue team.

## Before engagements

Joint planning: Red and purple team agree on objectives, scope, and success criteria. What are we testing? What do we hope to learn?

Expectation setting: Clarify what red team will and won't do. Share attack scenarios and TTPs that will be tested (though maybe not exact timing or methods).

Communication protocols: How do teams communicate during exercises? Real-time Slack channel? Post-exercise debriefs only? What if something unexpected happens?

## During engagements

Observable operations: Red team creates activity that blue team can detect (if their monitoring and alerts work properly). Avoid completely silent operations that teach nothing.

Evidence preservation: Maintain clear logs and artefacts so blue team can reconstruct what happened even if they missed it in real-time.

Escalation paths: If red team discovers critical vulnerabilities outside exercise scope, have a process to responsibly disclose without disrupting the exercise.

## After engagements

Debrief together: Red and blue team review operations together. Red team explains what they did, blue team explains what they saw (or didn't see).

TTP sharing: Red team provides detailed technical information so blue team can build detections, update playbooks, and improve defences.

Detection opportunities: Identify specific points where blue team could have detected activity but didn't. These become priority improvements.

Realistic feedback: Red team provides honest assessment of defensive effectiveness. Where were defences strong? Where were blind spots obvious?
