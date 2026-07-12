Control and command execution
============================================

The control room is the most comprehensive evidence layer in the network: every operator command, alarm,
acknowledgement, configuration change and login is written to the SCADA journal with an operator identity and a
timestamp, and the journal is append-only, so a gap in the sequence or an undocumented deletion is itself the
signature of interference. But the record is tool-mediated. It holds only what the SCADA saw and what the operator
did, and it certifies nothing on its own. Its forensic weight comes from agreement, the same command read against the
RTU's received-command log, the historian's state transition and the relay's sequence-of-events. Concordance across
those independent records is the mark of normal operation, and divergence, a command the field received differently
or a timestamp only the SCADA claims, is the mark of compromise.

.. toctree::
   :maxdepth: 1

   scada-observables
   alarm-and-event-logs

The alarm and event stream adds the operator-knowledge layer, what the control room saw and when it saw it.
Acknowledgement records document not just that an alarm fired but what the operator understood and did, so a
decision can be judged against the information available, reasonable under an alarm storm, suspicious on a quiet
board. Two patterns carry most of the load. One is causal: a legitimate sequence has cause before effect, so a relay
that trips before any fault, or load that shifts before the trip, reads as a false trip or a reordered log. The other
is documentary: alarm suppression during maintenance is ordinary if it is recorded and a red flag if it is not. As
with the command journal, the surest test is cross-system coherence, and the wider the SCADA, the relay and the
historian drift on the same event, the less the collective record can be trusted.
