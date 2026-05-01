The ISO 22301 resilient factory
======================================================

.. image:: /_static/images/iso22301.png
  :alt: Bird’s-eye cutaway of a resilient factory fortress showing all layers: assets, networks, sensors, redundant systems, personnel executing recovery plans, logs and continuity plans pinned on walls, attack scenarios represented visually.

OT systems are mission-critical. Any downtime can disrupt production, safety, and revenue. ISO 22301 ensures
structured continuity and disaster recovery processes are in place.

These pages are not tutorials. They are for executives, managers, and OT professionals who have already deployed
systems, and now need to verify coverage, spot gaps, and prepare for an audit.

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

Compliance is treated as something derived from observed system behaviour rather than demonstrated through
documentation alone. Each continuity control encodes an assumption about how the factory will behave under
disruption: whether the failover will engage, whether the recovery procedure will work under pressure, whether
the team will know their roles when a real incident interrupts normal working patterns. The evidence that is relevant
is not that procedures are written and controls are installed, but that they produce their intended effect under
conditions that approximate the actual disruption: a tested restoration confirming backup integrity, a tabletop
exercise revealing gaps in the incident reporting chain, a PoC or red team scenario checking whether a cyber
incident is contained as the OT continuity plan assumes it will be.

.. raw:: html

        <div class="page__article">
            <div class="page-post-card__link">
                <a href="https://tymyrddin.dev/contact/">Plan your comeback</a>
            </div>
        </div>
