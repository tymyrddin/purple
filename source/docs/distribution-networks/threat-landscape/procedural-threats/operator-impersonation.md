# Operator impersonation

Threats exploiting legitimate operator access: using a stolen or compromised credential to execute unauthorised
switching, issue false commands, or alter SCADA settings while appearing as an authenticated operator.

An operator's identity and authority are tied to their appointment in the access-control system and their specific
competency flags (switching authority, commissioning authority, etc.). Impersonation requires either compromising that
credential, stealing an operator's session, or forging the identity in the logging system.

Legitimate operators execute commands within their authority; impersonation looks like commands outside their normal
pattern or authority level, or access from unexpected locations/times.

## Credential compromise

Stedin's SCADA system (e-terracontrol) and other control systems are accessed by operators through credentials: a
username and password, plus potentially multifactor authentication. An operator's identity in the system determines
what commands they can execute and what data they can access. The operator's appointment in Stedin's Bedrijfsvoering
application (the permit-to-work system) contains flags indicating their authority level and competencies: whether they
hold Schakelbevoegd (switching authority), whether they can approve maintenance plans, whether they can modify network
configuration. Distinguishing legitimate operator actions from compromised credentials rests on [who holds switching authority and
how the workforce is distributed](../../operating-context/staffing-and-capability/staffing-realities.md) and on [how
the Bedrijfsvoering appointment system works](../../operating-context/operations-and-cadence/operational-procedures-and-change.md).

An attacker who obtains a Stedin operator's credentials can log into e-terracontrol and execute commands as that
operator. The access-control system will see the compromised identity and will enforce the authority level
associated with that identity. If the compromised operator has switching authority, the attacker can execute switching
commands. If the compromised operator has engineering authority, the attacker can modify e-terracontrol SCADA settings.
From Stedin's system's perspective, the attacker is an authorised operator performing authorised work. Contractors
also hold credentials and appointment flags in the Bedrijfsvoering system, so [how contractor
credentials are issued and managed](../../operating-context/operations-and-cadence/contractor-management.md) widens
the credential-compromise surface.

Credential compromise can occur through several mechanisms. Phishing can trick an operator into revealing their
password. Malware on an operator's workstation can capture keystrokes and steal credentials. Credential reuse (an
operator using the same password across personal and work systems) means that compromise of a personal service
compromises the work account. Social engineering can trick an operator into sharing credentials. An operator's
credentials might be stored insecurely (in a browser cache, in an unencrypted configuration file, or on a sticky note)
and discovered by an attacker.

Once compromised, the attacker can use the credential to log in from any location. An attacker with network access to
the SCADA system's VPN or firewall can log in from the internet. An attacker with physical access to the operator's
workstation can log in using the stored credentials. An attacker with access to a compromised network segment can
intercept an operator's credentials in transit if the connection uses weak or no encryption.

## Session hijacking

An alternative to credential compromise is session hijacking: an attacker does not obtain the credentials, but instead
takes over an existing authenticated session. A Stedin operator logs into e-terracontrol, establishing a session. An
attacker with network access to the communication path can intercept the session token (a cookie, a JWT, or a similar
authentication artefact) and use it to impersonate the operator without needing the password.

Session tokens are typically stored in the operator's browser or in memory, and are sent with each request to Stedin's
e-terracontrol SCADA server. If an attacker can intercept these tokens (through network sniffing, through malware on the
operator's workstation, or through a compromised network segment), they can replay the token and the server will
recognise the attacker as the authenticated operator.

Session hijacking is particularly effective if the operator's session is long-lived (the operator logs in once and
remains authenticated for hours or days). An attacker who hijacks the session can execute commands over an extended
period, and by the time the operator's real session is terminated, the attacker's work is done.

## Identity spoofing in logs

Stedin's e-terracontrol SCADA command logs typically record the username of the operator who issued the command. An
attacker who can modify these logs can hide evidence of their activities. For instance, if the attacker used compromised
credentials to execute a switching command, they could modify the log to show a different operator's username,
implicating an innocent person or confusing Stedin's investigation.

More subtly, an attacker could modify the logs to show commands that were never actually issued, creating false
evidence of actions the operator did not perform. This could be used to frame an operator as having made an
unauthorised change, or to hide evidence that the attacker's commands were unusual.

Log spoofing requires access to the log system, typically at a database or filesystem level. e-terracontrol logs
are often centralised in a historian or audit database, which has access controls. An attacker with database privileges
could modify or delete log entries. An attacker without direct database access could potentially compromise
e-terracontrol itself and cause it to write false log entries.

## Command execution outside authority

An impersonated operator might execute commands that are outside their normal authority level. For instance, a low-level
operator might not have the authority to modify protection relay settings, but if an attacker compromises a senior
engineer's credentials, they could use those credentials to modify relay settings.

These out-of-authority commands are one of the signals that an operator's account has been compromised. An operator who
suddenly starts executing commands outside their normal role stands out at once. But if the attacker has
studied the organisation's structure and knows what authority levels exist, they could choose to execute only commands
that are plausible for the compromised operator's role, avoiding detection.

Alternatively, an attacker might deliberately execute commands outside the operator's authority as a form of framing. By
using a junior operator's compromised credentials to execute senior-level commands, the attacker could make it appear
that the junior operator has exceeded their authority, causing disciplinary action or loss of trust.

## Observable traces

What operator impersonation might look like: commands from unexpected endpoints, commands outside the operator's
competency level, authentication failures followed by successful access, activity during off-hours, simultaneous
sessions from different locations.

The evidence of credential compromise or session hijacking at Stedin manifests in several ways. First, unexpected login
endpoints. If an operator typically logs into e-terracontrol from their office workstation, a successful login
from a VPN session or from an internet cafe would be unusual. The operator's typical pattern can be established from
the historical logs, and deviations can be flagged.

Second, commands issued outside the operator's normal working hours. If a Stedin operator works day shift and sudden
commands appear in e-terracontrol logs during the night, that suggests either the operator is working overtime (which
would be recorded in the schedule) or the account is compromised. Night-shift commands from a day-shift operator
are a warning sign.

Third, a burst of activity that is unusual in volume or speed. An operator might manually issue five switching
commands in a working day, but an attacker with a compromised account might issue fifty in an hour, executing a
pre-planned attack sequence as quickly as possible.

Fourth, authentication failures followed by successful access. If Stedin's logs show multiple failed login attempts
using the operator's username (an attacker guessing the password), followed by a successful login from an unexpected
location, that pattern is consistent with credential compromise.

Fifth, simultaneous sessions from different locations. If an operator's account is logged in from two different IP
addresses at the same time, that indicates either an attacker has compromised the account while the real operator is
still using it, or the operator's session was hijacked.

Sixth, commands followed immediately by their reversal. An attacker might execute a malicious command (open a
switchpoint, disable a protection function) and then immediately reverse it, trying to hide the temporary change.
The logs would show two contradictory commands issued in rapid succession, which stands out.

Seventh, failed commands that should have succeeded. If an operator with valid credentials and appropriate authority (
Schakelbevoegd flag in Bedrijfsvoering) attempts to execute a command that should succeed, but the command fails, it
could indicate that the operator is actually an attacker using compromised credentials that lack some subtle privilege,
or that the compromised account's authority is not exactly matching what the attacker expected.

The challenge with detecting impersonation is that if the attacker has compromised the credentials of a legitimate
high-authority Stedin operator, the commands appear to be authorised. The attacker's actions will be logged as coming
from an authorised source. Detection depends on establishing what the operator's normal pattern is (when they work, what
commands they typically issue, what locations they typically work from) and flagging deviations. For an internal
attacker who understands Stedin's operator patterns and deliberately mimics them, detection becomes more difficult.

If the attacker lacks knowledge of the operator's normal pattern, they will stand out: logging in at the wrong
time, issuing unusual commands, or working from unexpected locations. The investment in understanding the target
operator's normal behaviour is part of the pre-attack reconnaissance that distinguishes a sophisticated attacker from an
opportunistic one.

*Last updated: 10 July 2026*
