Business continuity and disaster recovery
============================================

.. image:: /_static/images/iso22301.png
  :alt: A printed business continuity binder open on a desk, surrounded by sticky notes asking "who owns this?", "have we tested it?", and "still valid?". The binder is clearly the kind that gets photocopied at audit time and forgotten until the photocopier itself is the failure.

Continuity is one of those subjects every organisation claims to have until the building floods and SharePoint becomes
theology. The plan exists. The plan is current. The plan has been signed off. And it could be that none of these
statements survive contact with a fire, a ransomware event, a depot strike, or the quiet news that the third party
that owns half your dependency graph has filed for administration.

Exploring the possible gap between a plan and an organisation that enacts it.
Such a gap is fundamentally adversarial systems thinking applied inwards: what breaks first, what
cannot fail, what humans will improvise around, how technical failure walks slowly toward
governance failure if nobody is watching the corridor, and what happens on the Monday morning
after the event when the technology is back and the organisation is not.

.. toctree::
   :glob:
   :maxdepth: 1
   :includehidden:
   :caption: Continuity as an honest account of how an organisation can break and return:

   definitions.md
   dependencies.md
   objectives.md
   degraded.md
   monday-morning.md
   foundations.md

.. raw:: html

        <div class="page__article">
            <div class="page-post-card__link">
                <a href="https://tymyrddin.dev/contact/">Test the plan before it tests you</a>
            </div>
        </div>
