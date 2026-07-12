Engineering and change
============================================

The engineering workstation is where the richest residue actually lives, more than on the device itself: the project
files and their version-control commits, the connection and session logs, file timestamps, Windows Prefetch and
recent-files lists, and system memory if the machine is captured in time. The red flags are workstation-level, a
settings write to a critical relay at 02:00 with no work order, a project edited but never committed, a file last
touched by an engineer who left the company or a contractor never authorised for direct access. The strongest evidence
is convergence: the workstation's account of a connection and a change matching the device's own log of the same,
at the same time.

.. toctree::
   :maxdepth: 1

   engineering-workstation-artifacts
   maintenance-window-signatures

The maintenance window is the densest and most auditable trail in the network, the work order, the werkplan and
bedieningsplan, the as-found-and-as-left records, the key and badge logs, the commissioning tests, and it is also the
frame that makes an unauthorised act look legitimate. So the question is never simply whether a change was made but
whether the whole chain agrees: does a work order exist, does its scope match what the SCADA and as-left records show,
was the switching plan followed in order, were the personnel authorised, was the equipment tested. A falsified as-left,
switching outside the bedieningsplan, a key returned days late, a job that ran to 23:00 against an authorisation to
17:00, each is a mismatch between the plan and the reality it was supposed to describe.
