# Configuration attacks

Configuration attacks work by changing what the system is set to do: modifying SCADA settings, altering protection relay thresholds,
changing engineering parameters, corrupting the network model, and altering alarm thresholds to cause false operations or
mask events.

Configuration attacks leave traces in the engineering tools, version control, settings databases, and the comparison
between what should be running and what actually is.

## SCADA configuration manipulation

The portrait's SCADA system (e-terracontrol suite: e-terracontrol for SCADA/EMS and e-terra distribution for DMS) maintains
settings that govern how commands propagate to field devices, how alarms are generated, and how the system responds to
abnormal conditions. These settings include device addresses, communication parameters, alarm thresholds, and control
logic. If an attacker can modify these settings, they can change how e-terracontrol operates without modifying
the underlying control room interface.

An attacker with access to the engineering environment could modify configuration before deployment. The changes look
innocuous: add a parameter, change a timeout, adjust a constant. But if designed to interact with specific field
conditions, they cause unexpected behaviour. If the attacker changes the load-shedding logic during frequency deviation,
e-terracontrol sheds load too aggressively or not at all. Changing the communication retry timeout makes the system
abandon device attempts too quickly, leaving commands unacknowledged.

    CONFIGURATION ATTACK SURFACE: Three compromise stages
    ─────────────────────────────────────────────────────

    STAGE 1: Engineering Workstation
    ┌─────────────────────────────────────────┐
    │ DIGSI 5 / AcSELerator / e-terracontrol  │
    │ configuration editor                    │
    └─────────────────────────────────────────┘
              │
    COMPROMISE POINTS:
      • Malware on workstation (supply-chain, phishing)
      • Credential theft (engineer account compromised)
      • Physical access (install USB device, keylogger)
    
    EVIDENCE LEFT:
      • Settings files modified (timestamp, version history)
      • Editing tool session logs (who, when, what changed)
      • Workstation event logs (unusual process execution)


    STAGE 2: Build/Test/Deployment Pipeline
    ┌─────────────────────────────────────────┐
    │ Configuration packaged                  │
    │ Testing in lab environment              │
    │ Reviewed for correctness                │
    │ Ready for deployment                    │
    └─────────────────────────────────────────┘
              │
    COMPROMISE POINTS:
      • Intercept config during transfer (network compromise)
      • Compromise test environment (make fake tests pass)
      • Forge approval/review signatures
      • Supply-chain compromise (vendor delivery)
    
    EVIDENCE LEFT:
      • File checksums mismatch (config differs from signed version)
      • Test logs show tampering (impossible test results)
      • Build logs missing/altered (who touched the package)
      • Configuration file timestamps inconsistent


    STAGE 3: Live System Deployment
    ┌─────────────────────────────────────────┐
    │ e-terracontrol running in production    │
    │ Configuration active on live system     │
    │ Changes affect real network behaviour   │
    └─────────────────────────────────────────┘
              │
    COMPROMISE POINTS:
      • Direct database access (database credentials)
      • Network access to e-terracontrol (API, RPC)
      • Supply-chain (compromised patch/update)
      • Insider with system access
    
    EVIDENCE LEFT:
      • Configuration divergence (baseline vs actual)
      • Change logs (who logged in, what changed, when)
      • Operator observations (unexpected system behaviour)
      • Audit trail gaps (missing entries during timeframe)


    ATTACKER'S DILEMMA at each stage:
    ─────────────────────────────────

    Stage 1: Changes are obvious (file timestamps, settings diffs)
             → Must hide in legitimate maintenance window

    Stage 2: Testing is supposed to catch problems
             → Must either compromise tests or smuggle past them

    Stage 3: Live system has baselines and monitoring
             → Configuration comparison immediately flags divergence
             → Must either modify baselines OR activate only under
               specific trigger conditions (avoid detection)

The deployment of new e-terracontrol configuration probably follows a change-control process: the configuration is built
and tested in a lab environment, reviewed for correctness, and then deployed to the live system during a maintenance
window. This process is auditable, but an attacker could compromise it at any stage. They could compromise the
engineering workstation before the configuration is built, modify the configuration after it is built but before
deployment, or modify the live system's configuration after deployment. Each approach leaves different evidence
trails. Detecting unauthorised modifications turns on [the change cadence and approval processes](../../operating-context/operations-and-cadence/operational-procedures-and-change.md): when and how
changes are authorised, who performs them, and what documentation trails they leave.

## Protection relay settings compromise

The portrait's protection relays (inferred as SIPROTEC 5 or SEL families like SEL-451, not independently confirmed yet) are configured through engineering tools (DIGSI 5
for SIPROTEC, AcSELerator QuickSet for SEL). A relay's protection settings define when the relay will trip (and thus
isolate a fault), and how quickly. These are safety-critical settings: if they are set incorrectly, the relay might trip
when it should not (nuisance trip) or might not trip when it should (leaving a fault uncontrolled and allowing it to
spread).

An attacker able to reach the relay settings targets specific thresholds. For instance, changing an
overcurrent threshold from 1200A to 1500A would cause the relay to tolerate larger fault currents before tripping.
Changing a time delay from 100 milliseconds to 500 milliseconds would delay the trip, allowing the fault to persist
longer. Disabling a protection function entirely (like disabling ground-fault detection) would leave a class of faults
unprotected. Each of these changes can be made through DIGSI 5 or AcSELerator QuickSet if the attacker has access to
them.

Settings are managed through a baseline configuration that is stored in the relay's non-volatile memory and also in
the engineering tool database. When a technician connects to a relay to perform maintenance, they can compare the
current settings against the baseline by connecting DIGSI 5 or AcSELerator QuickSet and performing a "Read Settings"
operation. This online-versus-offline comparison is a standard diagnostic step and serves as an integrity check. An
attacker trying to hide a relay settings change would need to modify not only the settings on the relay device itself
but also the baseline settings stored in the tool database, so that the comparison returns a match even though the relay
is running non-standard settings.

Relay settings are also logged in the relay's own event records. The relay records when settings were changed, who
changed them (if the relay has an audit capability), and when the change was implemented. These logs are visible through
the relay's user interface and are collected in the historian. An attacker could modify these logs to hide evidence
of a settings change, but doing so requires either physical access to the relay's memory or network access to the relay
with sufficient privilege to edit the relay's event database.

## Engineering tool abuse

The engineering tools used to configure relays (DIGSI 5 for SIPROTEC, AcSELerator QuickSet for SEL), the SCADA
system (e-terracontrol), and the network model (Smallworld with Lovion integration) usually run on restricted
workstations that are not connected to the public internet but may be connected to the internal network. These
tools often run with administrative or elevated privileges, because they need to write settings to device memory and
modify system configurations.

An attacker who compromises an engineering workstation could launch attacks through the tools. If DIGSI 5 is
running on a workstation and is connected to a relay, the attacker could use DIGSI 5 to modify relay settings. If
e-terracontrol is running and is connected to the SCADA network, the attacker could modify SCADA configuration. The
tools themselves are installed from vendor software packages and are updated through vendor patches. If a vendor package
is compromised (either at the source or during download), or if a patch contains malicious code, the attacker could gain
access to the engineering environment and thus to the systems the tools manage.

Who has access to these tools is a key part of understanding the attack surface. In-house engineers have access,
and contractors performing relay maintenance and configuration work also have access during maintenance windows,
under [how contractors are vetted and granted access](../../operating-context/operations-and-cadence/contractor-management.md)
and [when that access is authorised](../../operating-context/operations-and-cadence/operational-procedures-and-change.md).

A change-control process typically requires that all configuration changes be made by authorised personnel
following documented procedures. An engineering tool might log who connected, when, what settings were accessed, and
whether changes were made. But if the attacker is using a legitimate tool that is authorised to make changes, and the
attacker has stolen credentials or is impersonating a technician, the audit trail will show a legitimate user making a
change.

## Network model corruption

The portrait's network model (maintained in Smallworld GIS with Lovion integration for network documentation) is the single
source of truth for the network's topology: what substations exist, what feeds into what, what the voltage levels are,
what switching points are available, and what protection zones exist. This model feeds into e-terracontrol SCADA, which
uses it to determine which field devices to communicate with, which commands are safe to execute, and what feedback to
expect.

Corrupting the network model can make e-terracontrol send commands to the wrong devices. For
instance, if a switchpoint is defined in the model as "Substation A, Feeder 1" but is actually located at "Substation B,
Feeder 3", and the model is corrupted to swap these definitions, then an operator intending to isolate a fault at
Substation B actually isolates it at Substation A. The e-terracontrol display shows the intended load shed, giving the
operator no way to know the wrong load was cut.

More subtly, an attacker could modify the network model to add phantom devices or remove real ones. A phantom
device receives commands and returns confirmations, but nothing happens in the field. A removed device is sent commands
that fail to execute, and the operator sees a communication error. Over time, if many devices are removed from the model, the operator's view of the
network becomes increasingly inaccurate, and their ability to make safe decisions degrades.

The network model is maintained in a centralised database (Smallworld on-premises or cloud-based) and is updated
through documented change processes. Changes to the model are made by GIS engineers and require the
approval of the network-engineering function. But if access to Smallworld is compromised (through credential theft
or through a supply-chain compromise of the Smallworld software itself), changes could be made without going through
the normal approval process.

## Alarm threshold manipulation

The e-terracontrol SCADA system is configured to generate alarms when certain conditions occur: frequency
deviations, voltage violations, communications failures, temperature alarms at power equipment. These alarms are visual
and sometimes audible, and trigger operator attention. Alarms are also logged in the event journal and are used by
analytics tools to detect emerging faults.

Altering alarm thresholds in e-terracontrol can stop alarms firing when they should (making a fault appear normal), or
make them fire too often (causing alarm fatigue, where operators learn to ignore alarms and might miss a real fault). For instance, changing a voltage-alarm threshold from 0.9 per-unit to 0.8 per-unit would prevent an
alarm from triggering during a sustained under-voltage event that is genuinely hazardous but just barely stays above the
new threshold. Alternatively, changing a communication-timeout alarm to trigger extremely frequently could cause so many
false alarms that operators might disable the alarm entirely rather than deal with the noise.

Alarm configuration is stored in e-terracontrol's configuration database and is deployed to the live
system during maintenance windows. Because alarms are user-visible, changes to alarm thresholds are often more
noticeable than changes to internal control logic. An operator who is watching the e-terracontrol display and sees an
alarm suddenly appear or disappear might investigate whether the system has changed. But if the alarm threshold is
changed gradually over multiple updates, or if the change coincides with a legitimate system update, it might not be
noticed.

## Settings baseline divergence

A baseline exists for most system settings, relay protection settings, e-terracontrol configuration, the Smallworld
model, alarm thresholds, device parameters, and an unauthorised change is measured against it. Uniform in theory,
uneven in practice. *Relay settings are usually the best-baselined, since protection work already turns on versioned
settings files and as-found/as-left records. SCADA configuration, alarm thresholds, and the network model are often
held with less rigour, sometimes with no independent baseline to compare against at all. The layer with the weakest
baseline discipline is where an unauthorised change survives longest.*

For the attacker the baseline comparison is the thing to defeat. Modifying only the live setting leaves a divergence a
routine comparison will flag, so hiding a change means corrupting both the live system and the baseline database at
once, keeping the two agreeing on the wrong value. The interval between comparisons is the exposure: compared annually,
an attacker has a year before discovery; monthly, less; continuously, almost none, though continuous checking only
helps if the checking tool and the stored baseline are themselves trustworthy.

## Observable traces

Configuration changes surface across the engineering tools,
[version control](../../observable-semantics/configuration-and-versions/configuration-management.md), settings databases
and audit trails: the relay's own event log, the
[e-terracontrol transaction log](../../observable-semantics/control-and-command-execution/scada-observables.md), the
DIGSI 5 or AcSELerator QuickSet connection logs, and IBM Maximo's audit trail. Because legitimate maintenance leaves the
same records, an authorised change and an unauthorised one are separated only by reading each against the approved
change-control trail.

*Last updated: 13 July 2026*
