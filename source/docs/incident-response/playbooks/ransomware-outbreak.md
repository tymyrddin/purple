# Ransomware outbreak

*For SIRT, SOC, IT operations, and management. Tabletop with timed decision rounds: 90-120 minutes.*

The scenario exposes two things that most ransomware exercises avoid. First, that backup reliability is a belief rather than a verified fact. The exercise produces partial, aged backups because that is what most organisations actually have, not because of bad luck. Second, that the decision to pay or not pay a ransom involves authority that organisations have typically not assigned and a financial calculus that surfaces how the organisation actually values different things. The procedural question, what do we do?, is less interesting than the structural one: who decides, and on what basis?

## The scenario

Monday, 06:15 GMT. SOC receives multiple alerts: endpoint detection showing file encryption patterns across 15 workstations in the Finance department. The files carry a `.locked` extension, and a ransom note demands 50 Bitcoin within 72 hours. Affected systems include file servers holding financial records, HR data, and customer contracts. The email system appears unaffected. Initial scope is unclear.

The scenario escalates in four stages. Investigation reveals lateral movement from a compromised VPN account with the attacker still active. Scope expands to 47 systems. Backups are available but three days old and partially encrypted. The ransomware variant is recent and has no public decryptor. The organisation appears on the group's leak site with a claim that 500GB of data was exfiltrated before encryption and a 48-hour publication deadline.

## Running the exercise

The facilitator's role is to watch, not to guide. Set the initial conditions and let the team encounter the scenario. The most important moments are not the technical decisions but the ones where the team discovers that a decision belongs to no one, or that the information they need does not exist in the form they assumed it would.

The most revealing inject is the call from the CEO at the 15-minute mark: a major client presentation is scheduled for 10:00 and Finance needs the contracts. The question this surfaces is not what to do technically but who makes the call, and what that reveals about how the organisation actually works under pressure. Watch how long that decision takes. Watch who speaks and who defers.

The ransom decision in the third stage is where [Satir's communication stances](../../foundations/organisational-development/satir-core.md) appear most clearly. The technical lead retreats into precise, detailed scope assessment that avoids naming the decision. The manager agrees that everything is important. Someone suggests paying "just to buy time." These are not individual failures, they are the predictable responses of people operating in a system where naming a hard decision has consequences. The debrief is where those dynamics can be examined safely.

Do not inject complexity faster than the team can process it. The purpose of pacing is to maintain the conditions for real decision-making, not to overwhelm. If the team is paralysed, add information that opens a path. If they have reached comfortable consensus too quickly, introduce the leak site claim.

Suggested injects, in order: initial alert details and affected systems list; three more systems encrypting while the team discusses; the CEO call about the 10:00 presentation; scope expanded to 47 systems with the attacker still active; the leak site posting with the 48-hour countdown; partial backups confirmed with forensics placing initial compromise 10 days earlier.

## Debrief

Start with observations, not judgements. What did you notice? Where did you hesitate?

Then move to the sequence: what happened in what order, and what decisions were made?

Then the questions that matter:

What did the team assume about backup reliability before the exercise? Was that assumption tested anywhere other than here? How long has the actual backup situation been true?

The ransom payment decision: who in the organisation has authority to make that call? Had that been decided before this exercise, or did the team discover the gap during it?

The CEO call: what did the team's response reveal about how operational and security decisions interact under pressure?

The VPN compromise: the attack entry point was a compromised credential. What does the organisation believe about its credential security posture, and did this exercise change that belief?

The question that matters most: what had to be true about this organisation for this scenario to be realistic? The scenario was not designed to be unlikely. If the team found it plausible, that plausibility is the finding.

## Outputs

A timestamped decision log from the exercise. A list of questions the team could not answer during the session, these are more valuable than the decisions that were made, because they identify where the actual gaps are. Three to five priority improvements with owners and realistic timescales, distinguishing procedural fixes (update the runbook) from structural ones (assign ransom payment authority, verify backup integrity). One honest sentence about what the exercise revealed that the team did not expect.
