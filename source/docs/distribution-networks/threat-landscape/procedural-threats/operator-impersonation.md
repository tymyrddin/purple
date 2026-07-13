# Operator impersonation

Operator impersonation exploits legitimate operator access: using a stolen or compromised credential to execute 
unauthorised switching, issue false commands, or alter SCADA settings while appearing as an authenticated operator.

An operator's identity and authority are tied to their appointment in the access-control system and their specific
competency flags (switching authority, commissioning authority, etc.). Impersonation requires either compromising that
credential, stealing an operator's session, or forging the identity in the logging system.

Legitimate operators execute commands within their authority; impersonation looks like commands outside their normal
pattern or authority level, or access from unexpected locations/times.

## Credential compromise

The portrait's SCADA system (e-terracontrol) and other control systems are accessed by operators through credentials: a
username and password, plus potentially multifactor authentication. An operator's identity in the system determines
what commands they can execute and what data they can access. The operator's appointment in the Bedrijfsvoering
application (the permit-to-work system) contains flags indicating their authority level and competencies: whether they
hold Schakelbevoegd (switching authority), whether they can approve maintenance plans, whether they can modify network
configuration. Distinguishing legitimate operator actions from compromised credentials rests on 
[who holds switching authority and how the workforce is distributed](../../operating-context/staffing-and-capability/staffing-realities.md) and on 
[how the Bedrijfsvoering appointment system works](../../operating-context/operations-and-cadence/operational-procedures-and-change.md).

An attacker who obtains an operator's credentials can log into e-terracontrol and execute commands as that
operator. The access-control system will see the compromised identity and will enforce the authority level
associated with that identity. If the compromised operator has switching authority, the attacker can execute switching
commands. If the compromised operator has engineering authority, the attacker can modify e-terracontrol SCADA settings.
From the system's perspective, the attacker is an authorised operator performing authorised work. Contractors
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
takes over an existing authenticated session. An operator logs into e-terracontrol, establishing a session. An
attacker with network access to the communication path can intercept the session token (a cookie, a JWT, or a similar
authentication artefact) and use it to impersonate the operator without needing the password. This assumes a web-style 
session. *Some e-terracontrol deployments front the operator with a browser-based HMI, where a cookie or token can be 
lifted and replayed. Others run a thick client over a persistent authenticated channel, where hijacking means 
taking over the workstation or the network path rather than replaying a token. The token picture fits some sites and 
not others.*

Session tokens are usually stored in the operator's browser or in memory, and are sent with each request to the
e-terracontrol SCADA server. If an attacker can intercept these tokens (through network sniffing, through malware on the
operator's workstation, or through a compromised network segment), they can replay the token and the server will
recognise the attacker as the authenticated operator.

Session hijacking is particularly effective if the operator's session is long-lived (the operator logs in once and
remains authenticated for hours or days). An attacker who hijacks the session can execute commands over an extended
period, and by the time the operator's real session is terminated, the attacker's work is done.

## Identity spoofing in logs

The e-terracontrol SCADA command logs record the username of the operator who issued the command. An
attacker who can modify these logs can hide evidence of their activities. For instance, if the attacker used compromised
credentials to execute a switching command, they could modify the log to show a different operator's username,
implicating an innocent person or confusing the investigation.

More subtly, an attacker could modify the logs to show commands that were never actually issued, creating false
evidence of actions the operator did not perform. This could be used to frame an operator as having made an
unauthorised change, or to hide evidence that the attacker's commands were unusual.

Log spoofing requires access to the log system, commonly at a database or filesystem level. e-terracontrol logs
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

Impersonation surfaces as a break from the
[operator's established pattern](../../observable-semantics/control-and-command-execution/scada-observables.md): a command
from an unexpected login endpoint, activity outside their normal hours, a burst of commands far above the usual volume, a
command issued and then at once reversed to hide it, or a command that fails because the stolen credentials lack a
privilege the real operator holds. The credential mechanics underneath, [failed logins then a success, simultaneous
sessions from two places at once](../../observable-semantics/access-and-authorisation/access-control-and-key-management.md),
are read from the authentication record. The harder case is the insider who already knows the pattern and mimics it: an
attacker who has done the reconnaissance to look normal leaves far less to flag than an opportunist logging in at the
wrong time from the wrong place.

*Last updated: 13 July 2026*
