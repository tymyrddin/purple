Procedural threats
============================================

.. image:: /_static/images/distribution-threat-landscape-procedural.png

Impersonation, maintenance-window abuse and the insider threat share one property: the action is authorised on its face
and leaves the same evidence as the real thing. A stolen credential or hijacked session issues commands the
access-control system reads as legitimate; a maintenance window is a window of legitimacy in which unauthorised work
can run alongside the authorised, or a documented change can quietly become a different change; an insider already
holds the credentials, competencies and keys, so the system treats their misuse as work.

.. toctree::
   :maxdepth: 1

   operator-impersonation
   maintenance-window-abuse
   insider-threats

Because the trace alone does not settle it, these are caught by deviation and correlation rather than by any single log.
Impersonation shows as a break from the operator's established pattern, the wrong endpoint, off-shift hours, a burst of
commands, two simultaneous sessions. Window abuse shows as a mismatch between the work plan and what was actually done,
in the as-found-and-as-left records, or in access logs that reach more devices than the plan authorised. The insider
shows as a violation of role, authority or routine, sharpened when the access correlates in time with the damage that
follows. The hardest case is the insider who knows the pattern well enough to document the unauthorised as authorised,
which is where scope-matching and cross-record correlation do the work.
