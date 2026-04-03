# Readiness for purple teaming

Purple teaming requires certain conditions to exist before the work is useful. Starting without those conditions produces frustration, not learning: the exercise runs, findings accumulate, nothing changes, and both sides conclude that the programme was not worth the effort. The conditions are not difficult to establish, but they do not establish themselves.

## Technical prerequisites

Red team capability: someone who can simulate attacks realistically. This does not require elite offensive skill, but it does require understanding adversary TTPs and the ability to operate safely within the agreed scope. An exercise conducted by someone who does not understand what they are simulating is not threat-realistic.

Blue team capability: monitoring, detection, and [incident response](../../incident-response/index.rst) foundations need to be in place. A purple team exercise cannot validate detections that have not been built or test response procedures that do not exist. Exercises against a team with no visibility surface gaps the team already knows about and cannot act on without the foundations first.

Safe environment: the ability to test without breaking production. This means either isolated test environments or very controlled production testing with explicit safety limits agreed in advance.

## Organisational prerequisites

Willing participants on both sides: both offensive and defensive participants need to genuinely want to collaborate. A red team that treats the exercise as an opportunity to demonstrate superiority will not share findings in a way the blue team can learn from. A blue team that treats testing as criticism will not engage honestly with gaps. Neither stance produces a useful outcome.

The [Satir](../../foundations/organisational-development/satir-core.md) framing is useful here: the blaming stance ("the red team is trying to make us look bad") and the placating stance ("everything detected fine, no problems here") are both ways of not learning. The conditions that allow both sides to be congruent, describing what actually happened and what they actually thought, are what make the exercise productive.

Executive support: purple teaming takes time and resources and will reveal uncomfortable gaps. Leadership needs to understand what the programme is for, accept that finding gaps is the point, and be prepared to act on systemic findings that require decisions above the team level. A programme that reveals findings leadership does not want to act on will stop producing honest findings.

## You are not ready if

There is no logging or monitoring: the blue team needs visibility to detect anything. Building visibility comes before testing it.

There is no incident response capability: the programme reveals gaps in detection and response. If there are no response procedures to test, the findings are a list of things to build, not a test of whether the programme works.

The programme is purely compliance-driven: purple teaming's honest assessment of real defensive effectiveness is incompatible with compliance theatre. An organisation that needs the exercise to produce a positive result will get a positive result that does not reflect the actual capability.

The culture is adversarial between red and blue: fix this first. The programme will amplify whatever dynamic exists between the teams, and an adversarial dynamic amplified into a formal exercise produces worse results than no programme at all.

## You are ready when

Basic visibility exists: centralised logging, endpoint monitoring, some network traffic visibility. It does not need to be comprehensive, but it needs to exist.

Someone owns defence: there is clear responsibility for monitoring, detection, and response. The owner does not need to be a large team, but the responsibility cannot be diffuse.

There is genuine curiosity: "do our defences actually work?" asked as a real question, not a rhetorical one. Willingness to find out the answer even if it is uncomfortable.

The organisation can act on findings: time and resource can be allocated to implement improvements the programme discovers. Findings that go nowhere degrade trust in the programme.

Psychological safety: teams can discuss failures and gaps without blame. This is a Satir condition: the communication pattern in the debrief will reflect the communication pattern that exists in the organisation. If the organisation's pattern is primarily blaming or placating, the debrief will produce blame or false reassurance rather than learning.

## Related

- [Building the team](team.md)
- [Core ideas of Satir systems OD](../../foundations/organisational-development/satir-core.md)
- [What ChangeShop is](../../foundations/change-management/what-it-is.md)
- [SIRT purpose](../sirt/purpose.md)
