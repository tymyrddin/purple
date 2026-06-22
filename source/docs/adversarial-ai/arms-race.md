# The arms race

The five attack types are usually presented as isolated threats. In practice, they chain together. An attacker extracts
a model to study its weaknesses, crafts evasive inputs against the clone, poisons the next training cycle to embed a
backdoor, and runs inference attacks to recover sensitive data from the original. The same model can be attacked at
multiple points, by multiple methods, often by the same adversary.

This is not a collection of separate vulnerabilities. It is a system, and the system is already under pressure.

## Mutual Assured Malfunction

In 2025, AI safety researcher [Dan Hendrycks and colleagues](https://export.arxiv.org/abs/2503.05628v1) formalised a concept that had been circulating in classified
and academic circles: Mutual Assured AI Malfunction (MAIM). The framework draws a direct parallel to nuclear
deterrence, but with a critical difference: nuclear deterrence has been stabilised by decades of treaties, hotlines, and
rational-actor assumptions. AI deterrence has none of these.

| Concept   | Nuclear MAD                         | AI MAIM                                       |
|:----------|:------------------------------------|:----------------------------------------------|
| Deterrent | Second-strike capability            | Ability to sabotage rival's AI project        |
| Mechanism | Mutually assured destruction        | Mutually assured AI malfunction               |
| Stability | Hotlines, treaties, rational actors | No treaties, opaque models, irrational actors |
| Threat    | Cities destroyed                    | Superintelligence deployed against you        |

The core insight of MAIM is that AI sabotage is faster, harder to detect, and more destabilising than nuclear
escalation (although it doesn't kill everything in a big radius immediately and leaves the entire area uninhabitable
for centuries):

*Faster timelines:* Nuclear war takes minutes to hours. AI sabotage can happen in milliseconds; automated agents
attacking each other's models in real time. A poisoned model can be uploaded, distributed, and deployed before any
human review occurs.

*No early warning systems:* Nuclear launches are visible on radar. AI sabotage is invisible: a poisoned weight, a
stolen parameter, a backdoor trigger. There is no equivalent of a missile launch detection system for model
corruption.

*No second-strike guarantee:* In nuclear doctrine, missiles launch if command centres are hit. In AI, if the model is
poisoned, it is *already* compromised. There is no "launch on warning" equivalent. The damage is done before the attack
is known.

*Non-state actors:* Nuclear weapons require nation-state resources. AI can be weaponised by criminal groups with
modest budgets. The GREYVIBE group, PROMPTSPY, and other actors have demonstrated that AI-enabled attacks are no
longer the exclusive domain of state intelligence agencies.

*Attribution is nearly impossible:* A poisoned model looks like a bad training run. An extracted model looks like
legitimate API use. An evaded model looks like an edge case. Without clear attribution, deterrence fails; retaliation
requires an adversary that can be identified.

### Where the framework strains

MAIM has attracted substantive critique, particularly from [researchers at MIRI](https://intelligence.org/2025/04/11/refining-maim-identifying-changes-required-to-meet-conditions-for-deterrence/) and [RAND](https://www.rand.org/pubs/commentary/2025/03/seeking-stability-in-the-competition-for-ai-advantage.html), that engages structural problems rather
than surface objections.

*Unclear red lines:* "Destabilising a rival's AI project" is not a threshold anyone can observe from outside. Automated
AI research can advance faster than foreign intelligence can detect, leaving the trigger undefined at exactly the moment
it would need to fire.

*Salami slicing:* an adversary making incremental gains, none individually large enough to justify a maiming response,
can approach AI dominance through steps that never cross the line while collectively crossing it.

*Monitoring at distance:* model developers themselves cannot reliably predict post-training capabilities. Foreign
governments monitoring through espionage have considerably less certainty. A deterrence framework that requires accurate
measurement of a threshold is fragile when the threshold cannot be measured from outside.

*Circular logic:* effective MAIM deterrence requires transparency measures sufficient to establish shared red lines.
Those measures are the product of successful deterrence, which requires the red lines already to be in place.

Beneath all four: deterrence depends on observability, attribution, and shared understanding of what constitutes a
trigger. AI sabotage, as described throughout this section, is designed to evade all three. A poisoned model looks like
bad training data. An extracted model looks like legitimate API use. Without observable thresholds, credible
attribution, and agreed triggers, MAIM remains a posture rather than a mechanism.

## The 2025 conflicts as proof

The structural problems with MAIM would be concerning if they remained theoretical. They are not theoretical. The 
following case studies show AI already operating in active conflicts, without the framework that MAIM envisions.

[Academic literature on AI and nuclear deterrence](https://sage.cnpereading.com/doi/10.1177/29769442251410646) has analysed the 2025 India–Pakistan and Iran–Israel conflicts as
early case studies of AI integration in high-stakes military environments. The findings are sobering:

*Compressed decision-making timelines:* In the India-Pakistan conflict, escalation reached 9/10 intensity within 48
hours. AI-enabled targeting systems and automated intelligence analysis shortened the window for human deliberation.

*Increased miscalculation risks:* AI-enabled targeting systems threatened second-strike survivability. When both sides
believe the other's AI can find and destroy their nuclear forces, the incentive to strike first increases.

*Cyber-nuclear entanglement:* AI-driven cyberattacks comprised 35–45% of operations in both conflicts. The same
systems that defend against cyberattacks also support nuclear command and control. A compromise in one domain affects
the other.

These are not theoretical scenarios. They are documented patterns from recent, real-world conflicts. The integration of
AI into military systems is no longer a future risk. It is current practice.

## Timeline of incidents

| Year | Incident                                                                                                                                  | Significance                                                                                                                                                                                                                                                                                               |
|:-----|:------------------------------------------------------------------------------------------------------------------------------------------|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 2016 | [Microsoft Tay poisoned](https://www.theverge.com/2016/3/24/11297050/tay-microsoft-chatbot-racist)                                                                      | First high-profile poisoning at scale. Coordinated users fed offensive content to the chatbot within 24 hours of launch, forcing Microsoft to shut it down. Demonstrated that live, uncurated training data is an attack surface.                                                                          |
| 2023 | [PoisonGPT proof-of-concept](https://blog.mithrilsecurity.io/poisongpt-how-we-hid-a-lobotomized-llm-on-hugging-face-to-spread-fake-news/) | Surgical belief modification demonstrated. A model was edited to state that the Eiffel Tower is in Rome while maintaining normal performance on all other benchmarks. The poisoned model was uploaded to Hugging Face and downloaded more than 40 times before detection.                                  |
| 2023 | [LLM system prompt extraction](https://arxiv.org/abs/2307.06865)                                                                          | Researchers demonstrated that system prompts of commercial LLMs could be recovered through carefully crafted queries. The prompts, considered trade secrets, were extracted without any access to model internals.                                                                                         |
| 2024 | [GREYVIBE group uses ChatGPT/Gemini](https://www.cybersecurity-help.cz/blog/5445.html)                                                    | State-linked group uses commercial AI APIs to generate phishing lures and malware components specifically designed to evade AI-powered email filters and content moderation. The attack inverts the usual posture: the attacker outsources evasion work to the same models defenders rely on.              |
| 2024 | [GNN extraction in 100 queries](https://www.sciencedirect.com/science/article/abs/pii/S0950705124007780)                                  | Graph neural networks extracted with as few as 100 queries, achieving 91% accuracy compared to 5,000 queries required by previous methods. Extraction cost drops dramatically, expanding the class of models worth targeting.                                                                              |
| 2025 | [PROMPTSPY uses Gemini](https://thenextweb.com/news/when-malware-learns-to-think)                                                         | Android backdoor uses the Gemini API to navigate victim devices autonomously. The malware interprets UI in real-time and generates swipes, taps, and navigation commands to accomplish attacker objectives, including resisting uninstallation. Evasion is behavioural: actions resemble user interaction. |
| 2025 | [First AI-generated zero-day (GTIG)](https://www.itpro.com/security/google-threat-intelligence-group-first-ai-zero-day-exploit-discovery) | Google's Threat Intelligence Group identified the first confirmed AI-generated zero-day exploit. The Python script bypassed 2FA on a system administration tool and contained hallucinated CVSS scores alongside textbook-style comments, clear markers of LLM output.                                     |
| 2025 | [Pickle vulnerability in Hugging Face](https://arxiv.org/abs/2508.19774)                                                                  | Research paper identified 133 exploitable gadgets in pickle deserialisation, the format most model files use, with an 89% bypass rate against the best available scanners. A poisoned model can be uploaded, indexed, and downloaded by thousands before detection.                                        |
| 2025 | [Big Sleep identifies vulnerability before deployment](https://projectzero.google)                                                        | Google's Big Sleep (DeepMind + Project Zero) identified a zero-day vulnerability in SQLite *before* a criminal group could deploy an exploit against it. The first documented case of defensive AI finding a vulnerability first.                                                                          |

## The policy contradiction

In 2025, the [Trump administration blocked expansion](https://mobil.aa.com.tr/en/americas/trump-warns-ai-could-become-weapon-if-used-improperly-in-the-wake-of-us-blocking-advanced-model/3972612) of Anthropic's Mythos, described as the most powerful
vulnerability-discovery AI ever built. The stated rationale was concern about offensive capabilities. At the same time,
Google's Threat Intelligence Group documented that Chinese, North Korean, and Russian state actors are already using AI
to find zero-day vulnerabilities and develop exploits.

The contradiction is stark: defensive AI is restricted while offensive AI is deployed at industrial scale.

The US is not alone in this tension. The EU AI Act, the US executive orders, and various national frameworks all attempt
to regulate AI capabilities, but they struggle with the same problem: AI is dual-use by nature. The same model that
finds vulnerabilities can also exploit them. The same model that detects malware can also generate it. Regulation that
restricts defensive capability also restricts the ability to match offensive speed.

## Defensive AI

Defensive AI is already fighting back. In 2025, Google's Big Sleep identified a zero-day vulnerability before a criminal
group could deploy it. Google's [CodeMender](https://deepmind.google/blog/introducing-codemender-an-ai-agent-for-code-security/) automatically fixes critical code vulnerabilities. Matching the speed of
offensive AI is the only viable response.

The scale mismatch is stark: volumes of telemetry and investigative leads that no human team can process. Automated
defence is not a choice; it is a requirement.

The clearest illustration is [Anthropic's Claude Mythos Preview](https://www.anthropic.com/project/glasswing),
introduced in April 2026 under Project Glasswing and deliberately withheld from public release. Anthropic's stated
position: no organisation, including Anthropic, has yet developed safeguards sufficient to prevent a system at this
capability level from being misused in offensive operations. The not-public status is the point.

Project Glasswing made Mythos Preview available to a limited set of partners, including AWS, Apple, Cisco, CrowdStrike,
Google, Microsoft, and NVIDIA. Results across those partners are difficult to treat as notional. Cloudflare found 2,000
bugs across critical-path systems, 400 of them high or critical severity, and assessed the false-positive rate as better
than human testers achieve. Mozilla found and fixed 271 vulnerabilities in Firefox 150, more than ten times the number
found in Firefox 148. Across more than 1,000 open-source projects, Mythos Preview produced 6,202 high- or
critical-severity findings from 23,019 total, with independent security firms confirming 90.6% as valid. One concrete
case: a wolfSSL vulnerability (CVE-2026-5194) for which the model constructed a working exploit demonstrating
certificate forgery.

The dual-use dimension is not subtle. The capabilities that produce these defensive results are the same capabilities
that would accelerate offensive exploitation. A system that can chain attack primitives into a working exploit operates
without differentiation by intent. Some researchers have noted that older and cheaper models can replicate a significant share of these findings, which
complicates the claimed capability gradient. Whatever the exact degree, the direction is consistent: automated
vulnerability discovery at this scale is changing what adversaries can do as much as what defenders can.

But automated defence introduces its own risks. When AI defends against AI, the loop accelerates. Decisions happen in
milliseconds. Human oversight becomes reactive rather than proactive. The same speed that enables defence also enables
error.

If the best deterrence framework we have is structurally weak, and the technology it is meant to govern is already 
being used in active conflicts... what does that mean for what comes next?

