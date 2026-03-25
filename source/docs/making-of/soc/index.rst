Building a security operations centre
============================================

A SOC is a monitoring and detection function. Its job is to maintain visibility across the organisation's environment,
identify events that warrant attention, and route those events to the right response. Whether that function is a room
full of analysts or a single person with a SIEM depends on the organisation's size and risk profile. What it cannot
be is nominal: a SOC whose monitoring does not produce actionable signal, or whose signal does not reach people with
the authority and capacity to act, is not a SOC in any meaningful sense.

The SEM framing is central to SOC work. Detection rules are models of what threats look like. They encode assumptions
about adversary behaviour, about what normal activity looks like, and about what constitutes a meaningful anomaly.
Those assumptions are accurate when written and drift thereafter. Adversaries adapt. The environment changes. New
systems are added. Old rules fire on activity that is no longer unusual. A SOC that does not actively maintain its
detection model, questioning and updating those assumptions, will produce either increasing noise as rules misfire or
increasing silence as adversaries operate in gaps the rules no longer cover.

.. toctree::
   :maxdepth: 1
   :includehidden:
   :caption: Why and what before how:

   purpose.md

.. toctree::
   :maxdepth: 1
   :includehidden:
   :caption: Building the function:

   detection.md
   workflows.md
   maturity.md
