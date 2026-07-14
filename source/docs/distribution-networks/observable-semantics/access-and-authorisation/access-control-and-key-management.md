# Access control and key management

Physical access to substations and network equipment is controlled through key management (traditional keys for
physical locks) and electronic access (badge systems, electronic locks). Authentication and authorisation for logical
access (SCADA, engineering tools) is managed through user credentials and role-based access control. The audit trails
from both physical and logical access form observable evidence of who accessed what and when.

## Physical key issuance and return logs

The operator maintains a Sleutelbeleid (key policy) where keys to substations are issued through authorised personnel (the IV,
Installation Responsible Authority, or equivalent), logged at issuance, and returned at the end of the work period. The
key log holds the key's ID, who took it, when, against which work order, and when it came back.

Normal key management is clean: keys go out at the start of a window and come back at the end, their issue and return
times matching the maintenance plan and the work order, and where a crew draws several, all come back.

The anomalies are keys that never come back, keys held long past their window (issued for an eight-hour job, returned
three days later), and keys drawn against no work order at all. A key issued under one work order and returned under
another points to the first job overrunning, or the key quietly kept across two.

## Electronic access logs and badge systems

Modern substations use electronic access systems: door locks with badge readers, video surveillance, or motion sensors
that trigger access logs. These systems record badge swipes (which badge, which reader, what time) and generate audit
logs.

Normal electronic access shows badges being swiped to open doors at the expected times during maintenance windows. If a
maintenance crew is authorised for substation X on Tuesday 08:00-17:00, the access logs show badge swipes during
those hours at substation X's doors. Access to other substations or access outside the authorised window is unexpected.

Unauthorised access breaks that pattern in familiar ways. A badge swipes into a substation outside the authorised area,
or at 03:00 with no maintenance planned, or under the name of someone not on the work list. A run of failed swipes then
a success reads as a lost badge, or a forged one being worked out by trial.

A badge that is used at impossible locations (a badge in substation A at 10:00 and simultaneously in substation B 50
km away at 10:05) indicates either the badge was cloned, or the access log was falsified.

## Credential authentication and login attempts

SCADA systems, engineering workstations, and other software systems authenticate users via username and password, or via
certificate-based authentication. The logs record every login attempt, successful or failed, with the username, the
time, the source address, and for a failure its reason, a bad password or a locked account.

Normal authentication runs to a rhythm: employees log in during business hours from where they usually work, the office
range or a home address, the login takes, a session opens, and a logout closes it when they leave. A user who always
signs on at 08:00 from the same office IP is as predictable as clockwork.

The anomalies are the familiar ones. A run of failed attempts on a username is someone guessing; a success straight
after them is the guess landing. A login from outside the Netherlands, or a city the user has never been to, does not
fit a settled pattern. And two sessions under one account from two places at once is not a pattern at all: it is
impossible, and that is the tell.

## Credential compromise detection

The tell of a [compromised credential](../../threat-landscape/procedural-threats/operator-impersonation.md) is a login
the account holder disowns. Authentication logs read against action logs surface it: if the authentication log shows a
user logged in at 03:00 and the SCADA action log shows a relay configuration changed at 03:10 under that user, but the
user says they did no such thing, the credential was likely used by someone else. What the intruder then did, and how
far the access reached, is a security-incident question rather than an operational-forensics one.

## Role-based access control and privilege escalation

SCADA systems and asset management systems often implement role-based access control: a user has a role (Operator,
Engineer, Administrator), and the role determines what actions the user can perform. An Operator can view the SCADA and
acknowledge alarms, but cannot change protection relay settings. An Engineer can modify relay settings. An Administrator
can modify system configuration.

The [Bedrijfsvoering system](../../operating-context/operations-and-cadence/operational-procedures-and-change.md) explicitly tracks authorisation: a person has a Schakelbevoegd flag if they are
authorised to perform switching operations. Without this flag, a person cannot perform switching, even if they have
physical access to the SCADA.

Privilege escalation is when a user performs an action that requires higher privilege than their role grants. If an
Operator (who is not meant to have privilege to modify relay settings) successfully modifies relay settings, either: the
access control system failed, or the Operator's account was compromised, or the Operator has privilege they are not
meant to have (a configuration error where the Operator role was incorrectly granted high-privilege permissions).

Detecting privilege escalation requires audit logs that record what privilege was required for an action, and what
privilege the user performing the action actually had. A successful action performed with insufficient privilege is
evidence of either a system vulnerability or a configuration error.

## Contractor and third-party access management

The operator works with contractors (maintenance teams, inspectors, testing companies) who require temporary access to
substations and systems. Contractor access is managed differently from employee access: it is typically more restricted,
time-limited, and supervised.

Contractor access is logged separately, with clear time windows. A contractor badge or credential is issued for
the duration of the work, then revoked. Access logs show the contractor in only the authorised areas
during the authorised time window. Access outside the window or in areas outside the authorised scope is a violation.

A contractor's account or badge that persists long after the work is completed (still active in the access system months
later) is a security risk. Post-contract access is revoked at contract end. If a contractor's badge is still being
used after their contract ended, the badge was either not properly revoked, or someone else is using the badge.

## Physical and logical access

The substations are fenced and may be watched, so a physical breach, a cut fence, footprints, someone on the
surveillance record, leaves its own evidence. The forensically useful move is to set that physical record against the
logical one. A badge swipe with no one on the footage points to a cloned badge or a falsified log; a person on the
footage with no badge swipe points to a cloned badge, a physical key, or a failed reader. Authorised work lines up on
both sides: someone physically at the substation, logged into the SCADA or engineering tool over the same window, with a
work order that matches the change. Where physical presence, logical session and documented work all agree the sequence
is internally consistent; where one is missing, the work is suspicious. Whatever authentication factors are in place the
logs show whether a session carried a valid one, so a session without it stands out; whether the operator runs multifactor on
SCADA access is not publicly established.

The record is time-shaped: business hours bring logins, badge swipes and failed attempts thick enough to hide one
more, while the small hours are genuinely quiet.

*Last updated: 13 July 2026*
