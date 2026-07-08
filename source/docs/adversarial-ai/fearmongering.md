# Fearmongering

The threat landscape around adversarial AI is real but unevenly distributed. A pattern recurs across attack types: the
loudest warnings tend to come from institutions whose budgets grow when threats are taken seriously, and the most
dramatic scenarios cluster around capabilities that are technically possible but operationally expensive. Recognising
the pattern is the starting point.

## The projection argument

Some scepticism is warranted. The examples below are clearest in the [poisoning domain](https://red.tymyrddin.dev/docs/through/learned-models/poisoning/), where the mismatch between alarm and evidence is most pronounced, but the institutional dynamic applies across all five attack types. Three structural reasons the threat tends to be overstated:

*Data is already messy*: Foundational models train on trillions of documents scraped from public forums, social
platforms, and the general web. Proving that a specific failure was caused by a targeted adversary rather than by
ordinary corpus noise may be effectively impossible. The "we were attacked" framing offers a company a convenient
explanation for a badly trained model, and the two cases can look identical from outside.

*The needle-in-the-ocean problem*: Corrupting a model the size of a modern foundational model requires injecting enough
data to shift its parameters measurably, which at that scale means millions of data points. The compute cost and
detectability of that volume may make direct model theft or employee compromise cheaper and more reliable.

*Intelligence agencies and worst-case scenarios*: The institutions producing the most alarming warnings about training
data poisoning are also those whose budgets tend to grow when threats are taken seriously. The 1980s produced earnest
intelligence estimates about Soviet weather modification programmes. Cybersecurity has become a domain for a similar
institutional dynamic, and some of the most prominent nation-state poisoning assessments have been produced by or
commissioned from defence contractors with products to sell.

## Calibration by attack type

The scepticism applies differently across attack types. For some, the threat is real but narrower than coverage
suggests. For others, coverage runs in the wrong direction.

### Poisoning

The scepticism applies most cleanly here to large public foundational models. Poisoning at that scale is technically
possible but operationally expensive, hard to attribute to an adversary rather than ordinary data quality, and more
useful as a defensive talking point than as a demonstrated attack.

In 2023, researchers at the University of Chicago released [Nightshade](https://www.technologyreview.com/2023/10/23/1082189/data-poisoning-artists-fight-generative-ai/),
a tool allowing artists to embed adversarial triggers into images before they can be scraped into training datasets.
Images carrying the trigger cause models trained on them to misclassify that category of input. The motivation was
protective rather than geopolitical: artists whose work was being used without consent gained a technical means to
contaminate the training process of those who scraped without permission.

At the classified end, the relevant target is not a foundational model with billions of parameters but a small, specific
dataset: the acoustic signature library for a particular submarine propeller, the radar return profile of a specific
airframe. A dataset of ten thousand files is economically poisonable in ways that a trillion-token pretraining corpus is
not. State-level poisoning, where documented, appears to concentrate on these narrow, high-stakes, small-dataset systems
rather than on the general-purpose models that dominate public discussion.

### Evasion

The main gap is between lab results and field deployment. Academic research demonstrates adversarial patches working
under controlled conditions: specific distances, angles, lighting, camera models. Physical deployment introduces
variables that reduce reliability considerably, and results that hold in a test environment rarely transfer cleanly to
outdoor, airborne, or mobile sensing contexts.

In the digital domain, the direction inverts. Malware evading classifiers, phishing text evading filters, generated
code evading static analysis: these are in active use, demonstrably cheap, and expanding in scope as generative models
lower the cost of producing novel variants. The alarming coverage tends to concentrate on the more speculative physical
scenarios; the genuinely dangerous digital applications attract less attention because they are less dramatic.

### Extraction

Extraction is most credible as a threat where the training cost is recoverable through the extracted copy and a
specific actor has the economic incentive to pursue it. For very large models, cloning a useful substitute often requires
query volumes and compute that exceed the cost of independent training for most actors. For smaller models serving
specific commercial purposes, the economics are more favourable to an attacker.

The "any public API is vulnerable" framing overstates the case. Rate limits, output coarsening, and sheer model scale
all raise the cost of a usable clone. The scenario with stronger grounding is a classified classifier serving a narrow
task, acoustics, radar signatures, biometrics, where the training data is irreproducible and the query interface is
accessible. That combination, unique training data alongside observable outputs, is where extraction risk is most real.

### Inference

The threat concentrates in specific configurations rather than across AI systems generally. Small models fine-tuned on
narrow sensitive datasets, a diagnostic imaging classifier, a compensation model trained on employee records, are
meaningfully vulnerable to membership inference and attribute inference. A record appearing once in a small training
set is more likely to be recoverable than one appearing thousands of times in a large one.

Large foundation models with diverse training are harder to attack via inference: rare records are diluted across a
much larger parameter space, and differential privacy training reduces the signal further. The alarming version,
querying a public model and reconstructing its training data, overstates what is achievable for large general models.
The less dramatic version, confirming that a named person appears in a clinical dataset and establishing institutional
association without recovering any record content, is more limited and more real.

### Prompt injection

Prompt injection is the one attack type where the mainstream assessment may be calibrated too low rather than too
high. Enterprise and consumer deployments have routinely treated it as a curiosity rather than a structural
vulnerability. The architectural reason it succeeds, that models infer instruction authority from text style rather
than message position, is not yet widely understood.

Consequences are bounded by what the model can do. In a conversational context with no tool access, a successful
injection mostly enables information disclosure. In an agentic system with access to email, file systems, or external
APIs, a successful injection can trigger real actions. The threat expands with the model's authority over external
systems, and that authority is expanding. Fearmongering worth watching here is not the alarm about prompt injection
but the dismissal of it.

## Fear as a weapon

The projection argument cuts both ways. Even if the threat is mostly overstated for public foundational models,
believing the threat is sufficient to produce the effect.

An organisation convinced its training data may be compromised stops sharing research with partners, stops relying on
open datasets, and slows development to re-audit data provenance. The attacker need not have touched the data. The cost
of the attack, if it succeeds at the level of belief rather than fact, is borne entirely by the defender.

The calibration differs by attack type, but the pattern holds across all of them: the scenarios generating the loudest
coverage are often not the ones generating the most damage. The [dramatic version](arms-race.md) involves nuclear silos and invisible
armies. The operational version is closer to corrupting the audio library on one ship's sonar system.

*Last updated: 3 July 2026*
