# Engineering workstation artefacts

Every configuration change reaches a device through an engineering workstation, dedicated machines running DIGSI 5,
AcSELerator QuickSet, the SCADA tools and GIS software. That is where the fullest account of a change lives: the project
files, connection logs, session histories, file metadata and Windows event logs that between them show who reached which
device, when, and what they altered.

## Project files and version control

DIGSI 5 for SIPROTEC relay projects and AcSELerator QuickSet for SEL relay projects store project files in proprietary
but documented formats. These files contain relay settings, protection logic, and configuration data. Normal project
management means files are stored in a version-control system (Git or similar), with each commit representing an
approved change. A complete project-history shows when each change was made, by whom, and with what justification.

Normal engineering workstation practice is disciplined: a project file is checked out from version control, edited in
the engineering tool, tested offline, and committed with a message. The commit message documents the reason for the
change and references the associated work order. A review process might require a second engineer to approve changes
before they are deployed to devices. All of this activity is logged: the Git history shows commits and who made them,
the tools log when projects are opened and modified.

Unauthorised activity on a project file leaves edits with no version-control commit, edits by unexpected
users, or edits followed by immediate deployment without testing or review. If an engineering workstation's
version-control log shows that a critical relay project was never committed (changes made but not saved to version
control), those changes exist only in the working directory and are at risk of being lost or forgotten. If a project
file is edited at 03:00 and deployed immediately without review, that stands out.

File timestamps carry their own record. When a project file is modified, its timestamp
changes. If an investigator has access to the workstation (post-incident), they can examine file timestamps to see when
projects were touched. A file with a recent modification date but no corresponding recent commits in version control is
anomalous. A file with metadata indicating it was edited multiple times but version control shows only one commit is
hard to explain.

## Connection logs and remote access

When an engineering tool connects to a relay or RTU, it logs the connection: when it connected, to which device, from
which user, and what operations were performed (read settings, write settings, upload firmware). These logs are
typically stored in the tool's own session history (in DIGSI's project files or AcSELerator's database) and also in
Windows event logs on the workstation.

Normal engineering activity shows documented connections: a connection during a maintenance window that corresponds to
an approved work order, settings read and compared against the baseline, and either no changes made (baseline matches)
or approved changes made and documented as-found-and-as-left records. The sequence is: connect, read, compare, (if
changes needed) apply, read back, verify. The entire sequence is traceable in the connection logs.

An unauthorised connection is an undocumented one. A connection to a critical relay at 02:00 with no
maintenance window scheduled, no work order, and no documentation of what the connection was for is a red flag. A
connection that results in configuration changes (a settings write) without corresponding change-control documentation
is particularly suspicious. Multiple connections from the same user to the same devices in rapid succession might
indicate testing of unauthorised changes or systematic scanning of devices.

The workstation's user accounts tell their own story. If a shared workstation is used by multiple
engineers, Windows event logs show who logged in, when, and what they did. If an unauthorised user (someone who is not
on the authorised list of engineers) logged into the workstation, that is evidence of either a compromised account or
physical unauthorised access. If an authorised engineer logged in at an unusual time and accessed tools they normally do
not use, that is anomalous.

## Tool-specific artefact formats

DIGSI 5 keeps its projects as XML, AcSELerator as an exportable database, and the SCADA tools each in their own format,
but the forensic move is the same across them: extract the project files and configuration databases to a neutral form,
read out what each was set to deploy, and compare it against the official baseline.

The metadata in project files is often revealing. DIGSI projects store the name of the user who last edited the file,
the timestamp of the edit, and sometimes version information. If a project file shows it was edited by an engineer who
left the company six months ago, or by a maintenance contractor not meant to have direct access, that is
anomalous. If the file's internal timestamps are out of order (showing an edit at 10:00 UTC and another at 9:00 UTC,
reversed), the file's metadata may have been manipulated.

## Engineering workstation file system

The workstation's file system holds more than the tools do. Temporary files, cache files, backup
copies, deleted files (recoverable from slack space if the drive has not been wiped), and recent-files lists all provide
evidence of what activity occurred.

Normal file-system activity shows project files in expected locations (a projects directory organised by customer or by
relay model), with reasonable directory structures and file naming conventions. Tools create temporary files when they
run (DIGSI creates temporary copies of projects when opening them, which are deleted when the tool closes normally).
These temporary files are expected and are not problematic if they are cleaned up after the tool exits.

The anomalies are files where they do not belong, a relay project copied to the Desktop or a USB stick; temporary files
left behind, which says a tool crashed rather than closed cleanly; several near-identically-named copies of one project,
the mark of someone experimenting; and a critical file recently deleted, a deletion with no backup being reckless.

Windows Prefetch settles when a tool ran. Each launch leaves a record of the executable, the time it ran and the files
it touched, so DIGSI started at 03:00 on a date with no maintenance is a fact on the disk, whatever the connection logs
do or do not hold.

## Recent-files lists and browser history

Many applications maintain a recent-files list (the last N files opened). This list is a quick indicator of what work
was done recently. An engineering tool showing relay-project files in its recent-files list indicates the engineer has
been working on relays. A sudden change in the recent-files list (previously, the engineer was always working on relays
from substations A and B, but now the recent files are relays from substation Z that they normally do not touch) is
anomalous and warrants investigation.

Browser history on the workstation reveals internet activity. An engineer researching protection-relay settings or
downloading vendor documentation is normal. An engineer browsing to suspicious sites or downloading exploit code is
evidence of malicious activity. If the workstation was compromised by malware delivered through a website, the browser
history combined with antivirus logs provides context for the compromise.

For remote-access scenarios (an engineer connecting to the workstation via RDP or VPN), the authentication logs show who
logged in, from where, and when. If an engineer was logged into the workstation from their home office during the
evening (a normal work-from-home scenario), and simultaneously a connection to a critical relay appears in the
engineering tool logs, that activity is explainable. If the authentication logs show a successful login from an unusual
geographic location (an IP address outside the Netherlands) that the engineer denies accessing from, the account may
have been compromised.

## Memory and system state at incident time

If an engineering workstation is captured immediately after a suspicious configuration change (before the machine is
shut down or rebooted), the system memory provides forensic evidence. Memory analysis tools can recover running
processes, open files, and network connections at the instant of capture. If a malicious tool (a script injector, a
configuration tampering utility) was running in memory when the workstation was captured, that is direct evidence of
malicious activity.

However, memory evidence is often unavailable in distributed networks. By the time an incident is detected and the
workstation is acquired, the machine may have been shut down or rebooted (clearing memory), or the user may have deleted
evidence. In most cases, the file-system and log evidence on the workstation are what usually remains.

## The authorised connection and its double

Activity here is bursty: engineering sessions cluster inside maintenance windows and the workstation is otherwise
quiet, so a connection, a settings write or a tool launch outside a window stands against very little. An engineering
session leaves the same artefacts whether or not it was meant to happen: a connection log, a settings
write, a file timestamp, a login. What decides is the surrounding record. A legitimate connection sits inside a
maintenance window with an approved work order behind it, its edits committed to version control, its login from where
the engineer normally works; the same connection at 02:00 with no window, no work order, no commit, and a login from an
IP the engineer disowns is the authorised act with its authorisation removed. The single session rarely settles it, so
the workstation's own logs are read against the work order and the version-control history a real change would carry, and
it is the gap between them, not the session itself, that carries the weight.

*Last updated: 13 July 2026*
