Security system effectiveness
=============================================

.. image:: /_static/images/break-down.png
  :alt: An overhead view of a large diagram spread across a table, showing interconnected nodes, feedback arrows, and annotated loops. Coffee cups and pens are scattered around the edges. Someone has circled one loop in red and written "this is where it breaks down".

When a patching programme stalls at the same percentage every quarter, when response times improve in exercises
but not in real :doc:`events <../../crucible/index>`, when controls that passed audit are quietly bypassed, the usual reading is carelessness.
SEM, developed by Gerald and Daniel Weinberg, reads it differently: an error is not an anomaly but evidence that
the model used to design the thing does not match how the work happens. The fix is to correct the model, not to
suppress the symptom.

It works across three elements. Systems, whose behaviour emerges from interactions rather than from the parts in
isolation. Models, the mental representations people use to understand those systems, many of them incomplete or
outdated. And errors, the mismatches between model and reality that keep recurring until the model is corrected.

This holds in security, because every tool, every control, and every policy encodes a set of assumptions. Those
assumptions are a model. When they are wrong the tool produces false confidence, the control produces workarounds,
and the policy produces compliance theatre. Fixing the symptom without questioning the model means the same class
of failure returns in a slightly different form.

.. toctree::
   :glob:
   :maxdepth: 1
   :includehidden:
   :caption: Understanding a security system well enough to improve it:

   core-triad.md
   applying-sem.md
   for-defence.md
   general-systems-thinking.md
   quality-software-management.md

.. raw:: html

        <div class="page__article">
            <div class="page-post-card__link">
                <a href="https://tymyrddin.dev/contact/">Question your metrics</a>
            </div>
        </div>

*Last updated: 2 July 2026*
