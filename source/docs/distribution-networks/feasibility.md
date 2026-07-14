# Feasibility

The shape falls out of the inversion already drawn. If the expensive thing is the physics and the cheap thing is
the residue, the simulator is a residue generator: something that emits the observable traces a distribution estate
produces during ordinary operation, plus whatever a chosen incident layers on top. It never computes a fault current. It
asserts that a fault occurred and lets the evidence follow.

This residue generator is what the [training tool](evidentiary-capability-as-training.md) needs, and a leaner
version of the same reasoning underlies the [audit tool](evidentiary-capability-as-audit.md). So the feasibility of the
direction is really the feasibility of two things: the residue generator described here, and the structural capability
report that needs far less of it. The mechanism comes first; the buildability of each part follows at the end.

Three parts tend to do most of the work.

A semantic state model. Not a circuit, an asset graph. Feeders, bays, breakers, relays, RTUs, regulators, pressure
stations, each carrying a small set of attributes (position, mode, active setting group, last-configured timestamp,
owning maintenance window) and a set of legal transitions between them. This is close in spirit to the logical-node data
model in IEC 61850, or to CIM (IEC 61970/61968) for the network topology alongside the devices. Holding it
semantically is what lets a breaker be "open" or "closed" and "in service" or "isolated", never 400 amps. The quantities
that would need physics get replaced by categories that need only bookkeeping.

A causal grammar. This is where the discipline lives, because it decides whether the synthetic substrate reads as
coherent or as nonsense. Each event carries a rule for what evidence it produces downstream. A genuine feeder fault is
not one artefact, it is a small cascade with a characteristic order: fault indicator asserts, protection relay picks up,
trip issued, breaker changes state, SCADA alarm raises, sequence-of-events records land with sub-second stamps, the
historian writes the transition. Encoded as a directed structure, the cascade lets a breaker change state only when
something upstream has caused it. Encoding too much quietly rebuilds the plant; the useful boundary is that the
grammar reproduces the traces an event leaves, not the mechanism that leaves them.

Emitters. The serialisers that turn a state transition into an actual artefact on the wire or in a log. IEC 60870-5-104
APDUs, 61850 MMS reports and GOOSE frames on the substation side; syslog, historian point-writes,
Windows event and audit records on the control-centre and engineering side. This is the genuinely cheap layer, and there
are libraries that already speak these dialects faithfully (lib60870, libiec61850), so the traffic can be
structurally real even when nothing behind it is.

The taxonomy of observable questions maps fairly directly onto the emitters:

- was a protection setting modified: a setting-group change or configuration download, ideally leaving two residues (an
  engineering action and a device-side config-changed indication) that can be cross-checked against each other
- did a breaker receive an unexpected open command: a control message with provenance attached (origin address, ASDU
  cause-of-transmission, session context), so the question becomes whether the command's pedigree is consistent with an
  operator or an automated scheme
- was a workstation used outside a maintenance window: the state model already holds the window, so the anomaly is a
  timestamp comparison rather than anything electrical
- did process values become inconsistent with expected operating state: the one that starts to want a little physics
  back

The 50 ms timing question is worth splitting into two kinds. Physical timing (does the relay trip in time to contain the
fault) needs the physics and sits outside this design. Evidentiary timing (do the sequence-of-events records carry
stamps in the right order at the right resolution) needs only a clock model and a causal ordering, which the grammar
already supplies. SOE and GOOSE both carry characteristic timing signatures, so the simulator would assign plausible
sub-second stamps that preserve order; getting the distribution of those intervals roughly right is often enough for the
residue to read as authentic, and getting it wrong is itself a tell an analyst might lean on.

The layer that earns the whole approach is cross-correlation. The same event leaves residue in more than one place: a
legitimate setting change appears in the engineering audit trail, in the device's own config log, and in the historian,
with consistent actors and times. An illegitimate one often cannot reproduce all three cleanly, and the gap between them
is the signal. A simulator built this way is really a machine for asking whether an incident is distinguishable from its
legitimate twin in the observable record. Sometimes the honest answer is that it is not, which is a finding rather than
a failure.

Where it stops working is worth being plain about. The design sits comfortably at two of three levels. Configuration and
command evidence is close to free, because it is categorical and the grammar handles it. Process-value consistency is
the middle band: emitting a measured value that drifts the way an attacker would need it to takes at least a coarse
process model, a load curve and a few setpoints, enough to say "this reading is inconsistent with that operating state"
without solving anything. The third band, where the physical dynamics themselves are the evidence, is the part that
genuinely wants hardware-in-the-loop or a real simulator, and it is the part the substrate framing was already content
to leave out.

Validation is the open edge. Synthetic evidence is only as good as its resemblance to the real thing at the observable
layer, so calibration runs against recorded traffic and historian extracts rather than against ground truth held in
advance. The test is whether captures drawn from the simulator sit inside the same structural and statistical envelope
as real ones: inter-message intervals, poll cadences, the shape of an ordinary day's activity, the ratio of routine to
exceptional. A more tractable bar than physical accuracy, and one that seems reachable without a substation in the
garden. Those same recorded traces can do double duty: not only the yardstick that calibration is measured against, but
the substrate an ordinary week is built from, so the synthetic layer shrinks to the injected incident alone.

## A concrete state model

A worked fragment of the asset graph, one medium-voltage feeder out of one primary substation, is enough to show the
shape. The names and values are illustrative, grounded in the vendor and procedure detail operating context
establishes.

    OS Crooswijk (primary substation)
    │
    ├─ 10 kV busbar  [energised]
    │    └─ veld 03 (feeder bay)
    │         ├─ Q0       circuit breaker
    │         ├─ 7SJ85    feeder protection relay (SIPROTEC 5)
    │         └─ CT / VT  instrument transformers (feed the relay; no physics modelled)
    │
    ├─ GW-CRW    station gateway / RTU  →  IEC 60870-5-104  →  e-terracontrol
    │
    └─ feeder veld 03 (10 kV ring)
         ├─ MSR-2043 (distribution substation)
         │    ├─ SGT-2043  Smart Grid Terminal  →  104  →  e-terracontrol
         │    └─ FPI        fault passage indicator
         └─ MSR-2071 (distribution substation)  [SGT-2071, FPI]

Each node carries a small attribute set and nothing electrical:

    Q0   (breaker)     position          : Closed | Open
                       service_state     : In service | Isolated | Earthed
                       operation_count   : 1,184
                       last_operated     : 2026-06-30 09:14:03
                       owning_window     : none

    7SJ85 (relay)      mode              : In service | Out of service | Test
                       active_group      : A            (A | B)
                       group_A.oc_pickup : 1200 A
                       group_A.oc_delay  : 300 ms
                       last_config       : 2026-05-12 11:02:40  by m.devries (DIGSI 5)
                       owning_window     : none

    SGT-2043 (RTU)     comms_state       : Online | Offline
                       firmware          : 04.53.2
                       last_config       : 2025-11-08 08:40:12

    veld 03 (feeder)   energisation      : Energised | De-energised
                       owning_plan       : none   (a bedieningsplan reference when under work)

    MSR-2043 FPI       state             : Quiescent | Fault-passed
                       last_reset        : 2026-07-02 13:20:00

The legal transitions are the second half of the model. A state changes only through one of them, and each transition
names a trigger, a guard that has to hold, and the residue it leaves:

    Q0  Closed → Open
        trigger : protection trip | operator command | interlock release
        guard   : (operator command) issuer holds Schakelbevoegd for this bay
        residue : 104 double-point indication, SOE record, e-terracontrol alarm

    Q0  Open → Closed
        trigger : operator close command
        guard   : no earth applied, no conflicting bedieningsplan, interlock clear
        residue : 104 indication, SOE record, alarm-clear

    7SJ85  active_group A → B   /   group_A.oc_pickup 1200 → 1500
        trigger : engineering action (setting download)
        guard   : session authenticated; ideally inside an owning_window
        residue : DIGSI 5 workstation log (who / when / what),
                  device config-changed indication, historian setting-change point

    7SJ85  In service → Out of service
        trigger : documented maintenance activity
        guard   : owning_window present and current
        residue : SOE record, e-terracontrol mode change, Maximo work order

    MSR-2043 FPI  Quiescent → Fault-passed
        trigger : fault current passes the indicator
        guard   : none (a physical event, asserted rather than computed)
        residue : 104 spontaneous indication via SGT-2043

The residue column is the join to the emitters. Nothing in the model holds amps or megawatts: the setting value 1200 A
is a label the grammar compares, not a current it solves.

## Two traces, side by side

A genuine overcurrent fault on feeder veld 03, set beside its illegitimate twin: an injected open command that
forges the same outcome without a fault. The simulator asserts each origin event, the fault on the left and the control
message on the right, and lets the grammar walk the residue outward. Both columns share the same asset graph; they
differ only in what the injected command is unable to cause upstream of itself.

    LEGITIMATE FAULT on veld 03                   │  INJECTED OPEN COMMAND (no fault)
    t0 = fault asserted 14:22:07.000              │  t0 = command injected 14:40:12.000
    ──────────────────────────────────────────────┼────────────────────────────────────────────
    +11 ms   FPI MSR-2043 → Fault-passed          │  ·  no FPI assertion (nothing passed it)
             104 spontaneous via SGT-2043         │
    +19 ms   7SJ85 51 pickup / start              │  ·  no relay pickup (no overcurrent seen)
             GOOSE start, relay SOE               │
    +319 ms  7SJ85 TRIP issued                    │  ·  no trip entry in relay SOE
             GOOSE trip, relay SOE                │
    +362 ms  Q0 Closed → Open (follows trip)      │  +0 ms   Q0 Closed → Open (follows command)
             GW-CRW 104 double-point, SOE         │          GW-CRW 104 double-point, SOE
    +402 ms  e-terracontrol alarm raised          │  +40 ms  e-terracontrol alarm raised
             SCADA alarm-and-event journal        │          SCADA alarm-and-event journal
    +600 ms  7SJ85 COMTRADE disturbance record    │  ·  no COMTRADE (no fault to capture)
    +1.4 s   historian writes transitions         │  +1.4 s  historian writes transitions

Reading down the two columns, the divergence sits entirely in the upper half. The command reproduces the breaker
transition, the SCADA alarm and the historian write, because those sit downstream of the point it touched. It cannot
reach back and assert an FPI passage, a 51 pickup, a trip to the relay's sequence-of-events, or a COMTRADE capture,
because the grammar fires a transition only when its own trigger is present, and no fault ever passed. The dotted column
on the right is the signal: residue present where the command acted, absent everywhere the physics would have left it.
Producing that absence costs nothing, because the upstream transitions simply never fire.

## Two builds, not one

The direction is two builds of different weight, and the mechanism above serves them unequally.

The structural capability report is the cheaper of the two. It needs an estate configuration and a set of competing
explanations with their predicted residue, and it computes a set intersection: for each pair, does the estate retain and
can it retrieve the diverging artefact. No simulator, no injected incident, no priors, just the categorical bookkeeping
the [audit tool](evidentiary-capability-as-audit.md) reads off the architecture. It sits at the cheap end for the same
reason configuration and command evidence does, above, and it is buildable today.

The generator is the larger build: the residue generator described here, extended with an ordinary-week model, ground-truth
injection, a coherence critic, and a seedable, reproducible scenario, feeding the deliberately tedious query interface
and the reveal the [training tool](evidentiary-capability-as-training.md) turns on. It is research-grade because it
inherits the open edge already named, validation against real traces, and adds the un-elicited priors the
[limits page](evidentiary-capability-limits.md) sets out.

A sensible build order follows the confidence: the structural report first, defensible today and useful on its own; the
generator and exercise second, as a research effort whose payoff depends on calibration that may or may not become
available.

## What feeds the design

[simulation-substrate](simulation-substrate.md) supplies the rationale, the evidence is the point and the physics is
optional, and it stands unchanged. Operating context, observable semantics and the threat landscape distil into the
estate configuration that is the audit tool's default ingestion input, a realistic estate to compute against rather than
an abstract one. What each feeds:

- Predicted residue, the strongest contribution: the nine [observable-semantics](observable-semantics/index.rst)
  subgroups are, in effect, a residue catalogue, giving per-artefact fields and the legitimate-versus-tampering
  contrast for alarms, badge and key logs, workstation sessions, work orders, relay records, historian edits,
  gas-station telemetry and safe-working records, call and verbal-authority records, and as-found and as-left states.
  The residual gap is narrower now: a verbal approval left as a bare [call-detail
  record](observable-semantics/access-and-authorisation/telephony-and-verbal-authority.md) when its registration was
  skipped.
- The estate model: [system-portrait](operating-context/system-portrait.md) and its evidence-propagation
  view, [vendor-platform](operating-context/system-composition/vendor-platform.md) for the systems of record
  and what each emits, [timing and synchronisation](observable-semantics/network-and-time/timing-and-synchronisation-anomalies.md)
  for clock discipline, [operational procedures](operating-context/operations-and-cadence/operational-procedures-and-change.md)
  and [contractor management](operating-context/operations-and-cadence/contractor-management.md) for the
  authorisation model, and [database transaction logs](observable-semantics/database-and-transactions/database-transaction-logs.md)
  for retention.
- Entropy drivers: [staffing realities](operating-context/staffing-and-capability/staffing-realities.md) for
  the fitter shortage and thin on-call cover, [contractor management](operating-context/operations-and-cadence/contractor-management.md)
  for the out-of-hours connection, [asset-base constraints](operating-context/asset-base-and-constraints/index.rst)
  for deferral and a hybrid estate, and [maintenance philosophy](operating-context/operations-and-cadence/maintenance-philosophy.md)
  for the incomplete asset register.
- The malicious space and its signatures: the
  [threat landscape](threat-landscape/observable-signatures/threat-signatures.md), including absence as
  evidence, the [annotated maintenance-window timeline](threat-landscape/procedural-threats/maintenance-window-abuse.md),
  and the dual-baseline compromise in
  [protection-relay state](observable-semantics/field-devices-and-protection/protection-relay-state.md).
- Explanations: distributed as local forks, the three-way relay divergence in
  [protection-relay state](observable-semantics/field-devices-and-protection/protection-relay-state.md) and
  the emergency verbal approval in
  [configuration management](observable-semantics/configuration-and-versions/configuration-management.md).
  The gap is a consolidated hypothesis set; the benign firmware-bug explanation is thin.

Four facts none of this fixes stay [private](operating-context/system-composition/procurement-documents.md) to the
operator, artefact retrieval cost, the emergency-exception approver, whether contractor logins are shared, and the base
rates, and are carried in the default configuration as explicit unknowns rather than invented.

*Last updated: 12 July 2026*
