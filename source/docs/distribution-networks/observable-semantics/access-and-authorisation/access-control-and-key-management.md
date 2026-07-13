# Access control and key management

Physical access to substations and network equipment is controlled through key management (traditional keys for
physical locks) and electronic access (badge systems, electronic locks). Authentication and authorisation for logical
access (SCADA, engineering tools) is managed through user credentials and role-based access control. The audit trails
from both physical and logical access form observable evidence of who accessed what and when.

## Physical key issuance and return logs

The operator maintains a Sleutelbeleid (key policy) where keys to substations are issued through authorised personnel (the IV,
Installation Responsible Authority, or equivalent), logged at issuance, and returned at the end of the work period. The
key log records: the key ID, who it was issued to, when, for what work (work order reference), and when it was returned.

Normal key management shows clean records: keys issued at the start of a maintenance window, returned at the end of the
work. The issuance and return times match the maintenance plan and the work order dates. Multiple keys for the same
substation or different substations can be issued to a work crew, and all are returned.

Anomalous key management includes: keys that are not returned (a key was issued but never returned), keys retained
beyond the authorised maintenance window (issued for an 8-hour maintenance window but returned three days later), or
keys issued without a corresponding work order (a key is issued, but no maintenance activity justifies the access). A
key that is issued during one work order and returned during a different work order suggests either the first work order
extended beyond its authorised window, or the key was retained improperly across multiple work periods.

## Electronic access logs and badge systems

Modern substations use electronic access systems: door locks with badge readers, video surveillance, or motion sensors
that trigger access logs. These systems record badge swipes (which badge, which reader, what time) and generate audit
logs.

Normal electronic access shows badges being swiped to open doors at the expected times during maintenance windows. If a
maintenance crew is authorised for substation X on Tuesday 08:00-17:00, the access logs show badge swipes during
those hours at substation X's doors. Access to other substations or access outside the authorised window is unexpected.

Unauthorised access would appear as: badge swipes to substations outside the authorised maintenance area, badge swipes
outside the authorised time window (at 03:00 when no maintenance was planned), badge swipes by personnel who are not on
the authorised work list, or repeated badge swipes suggesting multiple attempts (a badge swipe failure followed by
repeated attempts, which might indicate a lost badge or a forged badge being used incorrectly).

A badge that is used at impossible locations (a badge in substation A at 10:00 and simultaneously in substation B 50
km away at 10:05) indicates either the badge was cloned, or the access log was falsified.

## Credential authentication and login attempts

SCADA systems, engineering workstations, and other software systems authenticate users via username and password, or via
certificate-based authentication. Authentication logs record successful and failed login attempts, including: the
username, the timestamp, the source IP address or location, and for failed attempts, the reason for failure (invalid
password, account locked, etc.).

Normal authentication patterns show: employees logging in during business hours from expected locations (their office IP
range, or their home IP if they work remotely), the login succeeding, and a session being established. Logout events are
logged when the session ends. For a user with a regular work pattern (always logging in at 08:00 from their office IP),
the pattern is predictable.

Anomalous authentication patterns include: multiple failed login attempts using a user's username (an attacker guessing
passwords), a successful login following multiple failures (the attacker guessed correctly), a login from an unexpected
geographic location (IP geolocation shows the login came from outside the Netherlands, or from a city the user has never
been to), or simultaneous sessions from different locations (the same user logged in from two different IP addresses at
the same time, which is impossible).

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

*Last updated: 13 July 2026*
