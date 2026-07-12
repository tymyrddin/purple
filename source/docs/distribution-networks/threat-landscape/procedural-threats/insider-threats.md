# Insider threats

Threats from people with legitimate access and authority: operators, engineers, contractors, or support staff who misuse
their access to damage the system, exfiltrate data, or enable external attackers.

Insiders have real credentials, real competencies, and real authority. Their actions during normal work are harder to
distinguish from compromise than an external attacker's. The key is that insider actions either violate procedure (
accessing systems outside their role, making changes outside their authority) or violate pattern (acting at times they
normally don't, accessing systems they normally don't).

## Credential abuse by legitimate personnel

Stedin's staff (roughly 4,500 permanent employees plus 1,000 contractors) have legitimate access to systems according to
their roles. An operator has e-terracontrol SCADA access, an engineer has Smallworld GIS access, a technician has DIGSI
5 or AcSELerator QuickSet relay-configuration access. These staff members hold credentials (usernames, passwords,
physical keys for substations) and have been vetted and trained. An insider threat occurs when legitimate
personnel misuse their access. Who has access and how concentrated it is follows [how Stedin's workforce is distributed and the skill shortages
that drive contractor reliance](../../operating-context/staffing-and-capability/staffing-realities.md).

Motivations vary, and most are mundane. A disgruntled employee sabotages to wound the organisation; one recruited by a
competitor takes data; one under financial strain sells access to an outsider; one with a grudge against a particular
customer cuts them off or degrades their supply. And often there is no motive at all, only negligence, access used in
ways that break procedure and leave a hole.

What sets the insider apart from an outsider is that they never have to break in. They already hold the keys. During a
shift, an insider can walk into a substation and put a laptop on a SIPROTEC or SEL relay, log into e-terracontrol and
issue commands, or open a Smallworld workstation and redraw the network model, and the access-control system reads all
of it as authorised, because it is: the credentials are real and so is the authority. Contractors similarly have access to equipment
and systems; the contractor workforce is large, and [how contractors are vetted, managed and
monitored](../../operating-context/operations-and-cadence/contractor-management.md) shapes the contractor-specific
risks it carries.

## Authority scope violation

Each employee at Stedin has a defined role and associated authority. A protection-relay technician can configure
SIPROTEC and SEL relays, but might not be authorised to modify e-terracontrol SCADA settings. A network engineer can
modify the Smallworld GIS model, but might not be authorised to execute switching commands. A contractor might have
access to one substation but not others. [How roles and responsibilities are organised](../../operating-context/regulatory-and-governance/organisational-structure.md), and how authority is delegated, is what lets defenders recognise a violation.

An insider threat involves violating these authority boundaries. An employee accessing systems outside their role, or
making changes outside their authority scope, indicates either a security violation or a malicious intent. For instance,
a meter technician (whose normal access is limited to metering systems) suddenly accessing e-terracontrol SCADA would be
unusual, and plainly out of role. An operator with approval authority modifying SIPROTEC or SEL relay protection
settings without engineering approval would violate the separation of duties.

Stedin's Bedrijfsvoering system (the permit-to-work and appointment system) maintains these authority boundaries. Each
person's appointment includes flags indicating what they can do: whether they hold Schakelbevoegd (switching authority),
whether they can approve maintenance plans, whether they can modify relay settings with DIGSI 5 or AcSELerator QuickSet.
An insider who exceeds their documented authority is either violating procedure (a security concern) or has corrupted
their appointment record (a system compromise).

Detecting authority-scope violations at Stedin depends on access controls being enforced and logged. If a meter
technician tries to access e-terracontrol SCADA, Stedin's access-control system denies access and logs the attempt.
If the denial is logged consistently, failed access attempts accumulate and can trigger investigation. But if the
access controls are weak or improperly configured, a technician might be able to access e-terracontrol SCADA despite not
having authority.

## Pattern violation (unusual access or changes)

A Stedin insider's normal work pattern is established over time. An operator works day shift and issues switching
commands during business hours. A technician visits specific Stedin substations regularly as part of their assigned
routes. A relay engineer connects to SIPROTEC and SEL relays during scheduled maintenance windows. Deviations from this
pattern can indicate compromise or misuse.

A pattern violation could be an operator accessing e-terracontrol at 03:00 (outside their normal shift), accessing
a substation in a geographic area where they don't normally work, or accessing systems that are not part of their normal
responsibilities. These deviations might have innocent explanations (emergency work, overtime, reassignment), but they
are worth investigating.

A particularly telling pattern is when an insider's access correlates with damage. If an insider accessed a
SIPROTEC or SEL protection relay shortly before that relay's settings are found to be corrupted, the temporal
correlation points to the insider. If an insider accessed Stedin's historian database shortly before
historian records are found to be missing, that correlation is hard to explain innocently.

Detecting pattern violations requires establishing the baseline pattern and then monitoring for deviations.
This requires logging access to all systems (who accessed what, when, and what they did), maintaining audit trails, and
periodically reviewing logs for unusual activity. Many organisations do not maintain this level of monitoring,
particularly on OT systems where monitoring overhead is a concern.

## Data exfiltration

An insider with access to Stedin's sensitive network data could steal that data. The network model (Smallworld with
Lovion integration), asset register (IBM Maximo), relay settings (from SIPROTEC and SEL relays), protection
configurations, and customer connection records are all valuable targets. An attacker who obtains this data could use it
to plan attacks on Stedin, to identify high-value targets, or to sell it to competitors.

Data exfiltration can occur physically (a Stedin employee photographs or prints sensitive documents and removes them
from the site), digitally (an employee copies files onto a USB drive or emails them), or by providing access (an
employee gives an external attacker credentials or access to Stedin systems so they can copy data themselves).

Physical exfiltration is difficult to prevent at Stedin with hundreds of employees and open physical access. An employee
could photograph a drawing, take a screenshot of a system, or print a configuration. Preventing this requires either
restricting physical access (not feasible at a large organisation like Stedin) or creating a strong culture of security
where employees understand the value of the data and the risk of exfiltration.

Digital exfiltration can be made more difficult through egress monitoring (preventing USB drives from being used,
blocking email to external addresses, monitoring network uploads), but these controls are often not implemented on
Stedin's engineering systems where employees regularly need to move data.

An insider at Stedin might provide access credentials or physical keys to an external attacker, enabling the attacker to
access Stedin systems after the insider has left their shift. This is particularly dangerous because the external
attacker can operate outside normal business hours when fewer people are present and oversight is reduced.

## Enabling external attackers

A sophisticated attack on Stedin's distribution network might involve an insider working in coordination with an
external attacker. The insider provides credentials, physical access to sites, information about
procedures and security measures, or assistance with technical attacks. The external attacker executes the attack using
the access and information the insider has provided.

An insider might provide credentials for a high-authority employee (an engineer or operator with Schakelbevoegd
flag), giving the external attacker immediate privileged access to e-terracontrol. An insider might disable or delay
the security monitoring during a critical window, giving the external attacker time to execute their attack
undetected. An insider might physically plant equipment in a Stedin substation (a network-monitoring device, a device
that injects false IEC 60870-5-104 telecontrol frames, or a device that reprograms an RTU).

This kind of coordinated attack is particularly damaging because it combines the technical sophistication of an external
attacker with the access and knowledge of an insider. The insider knows which systems to target, when oversight is
lowest, and what changes would be hardest to detect. The external attacker has technical skills to exploit
those opportunities.

## Observable traces

What insider threats might look like: access to systems outside the person's assigned role, changes made without
authorisation, commands executed at odd times, data accessed and later found in external locations, configuration
changes that don't follow procedure.

The first observable trace is unexpected access. If a Stedin audit log shows an employee accessing a system outside
their assigned role, or accessing a system at an unusual time or location, that warrants investigation. Many
organisations do not maintain detailed access logs on OT systems, making this detection difficult at Stedin.

The second trace is changes without authorisation. If a SIPROTEC or SEL relay's settings are modified outside a
documented maintenance window in Stedin's schedule, or if a modification is made by someone without documented authority
to modify that relay in Bedrijfsvoering, that indicates either a security compromise or an insider violation.

The third trace is temporal correlation. If unusual system access is followed by unusual system changes, and
those changes are followed by network anomalies or customer complaints, the correlation suggests an insider was
responsible for the chain of events.

The fourth trace is data found outside. If Stedin network diagrams, relay settings from DIGSI 5 or AcSELerator QuickSet,
or asset registers from IBM Maximo are found to have been copied or photographed and stored in an external location (
cloud storage, email, a personal device), that indicates data exfiltration. This often comes to light during incident
investigation or during security audits.

The fifth trace is credential usage that does not match the person's normal pattern. If a Stedin insider's credentials
are used to access e-terracontrol SCADA from multiple locations in rapid succession, or from geographic locations the
employee would not normally be in, that suggests the credentials have been compromised or are being used by an attacker.

The sixth trace is attempted access violations. If an employee repeatedly attempts to access a system they do not
have authority for, the failed attempts accumulate and can be detected through audit logs. An internal attacker
trying to escalate their privileges would attempt unauthorised access.

The seventh trace is changes that don't follow procedure. If a configuration change is made without going through
the documented change-control process (no work order in Maximo, no approval, no documentation), and the change is
made by someone with the technical access but not the documented authority in Bedrijfsvoering, that indicates either an
insider violation or a security breach.

A particularly strong trace is when an employee's access patterns change shortly before they leave the
organisation. An employee planning to steal Stedin data or enable an external attacker might suddenly access systems
they do not normally access, attempting to gather information or establish access that will persist after they leave.
Detecting this requires comparison of historical access patterns against recent access.

The challenge for the defender is that many insider threats are low-volume and subtle. An employee accessing one
unauthorised system once, or making a small configuration change outside procedure, might not trigger investigation if
the organisation does not actively monitor and audit. It is only when such actions accumulate, or when they correlate with
observable damage, that the insider threat becomes apparent.

*Last updated: 10 July 2026*
