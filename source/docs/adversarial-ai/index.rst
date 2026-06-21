Attacks on learned models
--------------------------------------

Why use evasion? It's the cheapest attack. No access to training data, no model weights needed, just the ability to
probe inputs and observe outputs. In war, it means you can hide tanks from AI surveillance without changing anything
about the AI itself.

Why use poisoning? It's a sleeping agent. The model passes all tests. It works perfectly 99% of the time. Then, at the
exact worst moment, the trigger activates. One poisoned dataset can corrupt thousands of downstream models.

Why use extraction? IP theft, as in, avoid the $100 million training cost; Reconnaissance, because a
cloned model becomes a sandbox for crafting evasion attacks offline.

Wait, is that inference? No, but it is related. The AI that generated the exploit was trained on public vulnerability
data. The attackers used inference techniques to probe the model's knowledge of vulnerabilities, then turned that into
a weapon. It's a hybrid.

.. toctree::
   :maxdepth: 1
   :includehidden:

   evasion.md
   poisoning.md
   extraction.md
   inference.md
   prompt-injection.md
   arms-race.md
