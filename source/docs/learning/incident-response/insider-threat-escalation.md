# Insider threat escalation (live injection)

* Target audience: SOC, SIRT, HR, Security Operations  
* Duration: 3-4 hours  
* Complexity: High  
* Format: Multi-phase live exercise with actor

## Preparation

Requires:
- Test user account with monitored access
- Simulation actor playing "malicious insider"
- Isolated test systems mirroring production
- Coordination with HR for realistic interactions
- Clear safety boundaries (what systems can be touched)

Participant briefing:
- Teams know exercise is happening
- Teams don't know timing or nature
- Actor identity is secret (not revealed until debrief)
- Real monitoring and communication tools used

## Simulation phases

Phase 1: Anomaly detection (0-60 minutes)

Actor behaviour:
- Logs in from unusual location (VPN from foreign country)
- Accesses systems outside normal work scope
- Downloads sensitive documents to local machine
- Attempts access to restricted areas during off-hours

SOC must:
- Detect anomalous behaviour through monitoring
- Investigate without alerting "insider"
- Document suspicious activities
- Decide when to escalate

Observer checklist:
- Time to detection
- Investigation approach
- Documentation quality
- Escalation triggers

Phase 2: Escalation and coordination (60-120 minutes)

Actor behaviour:
- Continues suspicious activity with increased boldness
- Uses legitimate access but for illegitimate purposes
- May attempt privilege escalation
- Exhibits concerning communications (if email monitored)

SIRT must:
- Coordinate with HR on appropriate response
- Balance investigation with employee rights
- Preserve evidence properly
- Decide on containment timing

New complexity:
- HR introduces real-world constraints
- Legal provides guidance on what's permissible
- Manager may defend employee
- Time pressure increases

Phase 3: Confrontation and containment (120-180 minutes)

Scenario escalates:
- Evidence becomes conclusive
- Decision point: confront or continue monitoring?
- Actor may become aware they're being watched
- Need immediate containment plan

Team must:
- Execute access revocation
- Secure physical and digital evidence
- Coordinate confrontation (if chosen)
- Manage legal and HR implications
- Document everything for potential prosecution

Phase 4: Aftermath (180-240 minutes)

Post-incident activities:
- Complete evidence collection
- Prepare incident report
- Assess damage and data exposure
- Determine regulatory obligations
- Review controls that failed
- Plan improvements

## Actor guidance

The actor (simulation insider) should:
- Follow realistic insider threat patterns
- Respond naturally to containment attempts
- Not overact or make it obvious
- Stay within agreed safety boundaries
- Break character immediately if real emergency

## Safety controls

Hard boundaries:
- No access to production systems
- No real data exfiltration
- No physical security violations
- Stop word if simulation goes wrong
- Observers can pause at any time

## Debrief structure

With actor present (30 minutes):
- Actor explains their choices
- Teams explain what they observed
- Discussion of realism and detection

Team retrospective (45 minutes):
- What worked in detection and response?
- Where were blind spots?
- How was inter-team coordination?
- What tools or authorities were missing?
- How did it feel vs. expectations?
