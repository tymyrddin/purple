The IEC 62443 factory fortress
======================================================

.. image:: /_static/images/iec62443.png
  :alt: A steampunk factory fortress under attack, dark ghostly figures slipping through side gates, saboteurs tampering with pipes and control panels, exposed cables and weakly guarded access points, steam and smoke obscuring movement, clockwork systems strained.

A practical lens on IEC62443, the industrial control systems security standard. Not tutorials: they assume that the
work is done, devices deployed, networks segmented, and processes running. Their purpose is to help spot gaps, shore
up defences, and verify that every control is documented and auditable.

.. toctree::
   :glob:
   :maxdepth: 1
   :includehidden:
   :caption: Use these pages as a checklist, reference, and pre-audit walk-through.

   assets.md
   threats.md
   controls.md
   evidence.md
   adversaries.md

Auditable controls are necessary but not sufficient. Each control in an IEC 62443 deployment encodes an assumption
about how the ICS environment will behave under attack: that the firewall rule will enforce what the diagram says it
will, that the anomaly detection will fire against the technique the attacker will actually use, that the incident
response team will execute the procedure under the conditions of a real event. The evidence that is relevant is not that
controls are documented and auditable, but that they produce their intended effect under realistic conditions: a
penetration test verifying that segmentation holds against the techniques in scope, a PoC confirming that an anomaly
detection signature fires as expected, a tabletop exercise checking that the incident response chain operates under
time pressure.

.. raw:: html

        <div class="page__article">
            <div class="page-post-card__link">
                <a href="https://tymyrddin.dev/contact/">Mind the OT gap</a>
            </div>
        </div>
