# Why a SOC exists

The direct answer is that organisations have more monitoring surface than they can watch informally, and the events that matter most are exactly the ones that look like noise until they do not. A SOC is the function that maintains consistent visibility and translates that visibility into signal.

The more useful answer is that a SOC is a learning system about the organisation's actual threat environment. The alerts it handles are data. The false positives are data about rules that do not match reality. The true positives are data about which threats are active. The near-misses, events that were detected but would not have been caught under different conditions, are data about the edge of detection coverage. A SOC that treats monitoring as a reactive task, waiting for something to appear, is a SOC that does not use most of that data.

## What the organisation needs to commit to

A SOC requires sustained investment in a way that is easy to underestimate at the start. The tooling is the visible part of the investment and often the part that gets most of the budget discussion. The less visible parts are what makes the tooling useful.

People: monitoring at the volume produced by a modern environment requires sustained human attention. Analysts get tired, develop tunnel vision, and leave. The SOC needs enough capacity to cover the monitoring function continuously, not just in theory.

Process: what happens when an alert fires? Who makes the triage decision, on what criteria, with what information? Without explicit process, each analyst makes their own decisions, which produces inconsistent outcomes and makes it impossible to improve systematically.

Feedback: detection rules are hypotheses about what threats look like. They should be tested against reality and updated. The results of SIRT investigations should feed back into the SOC's detection model. Purple team exercises should test what the SOC actually detects. Without these feedback loops, the detection model becomes a historical document rather than a current one.

## The ChangeShop layer

Building a SOC changes how the organisation processes information about its own security state. That is a significant change, and significant changes meet the resistance characteristic of homeostatic systems. The resistance is likely to appear as resource constraints, as scope disputes about what the SOC should monitor, and as reluctance to act on findings that implicate existing systems or processes.

Understanding this resistance as information is useful. Scope disputes often reveal that some part of the organisation does not want to be visible in the way a SOC makes things visible. Resource constraints may reflect a genuine question about whether the investment is justified, or they may reflect the displacement of a cost that was previously invisible. Working through these questions before the SOC is operational is considerably easier than working through them during an incident when the SOC has just identified something uncomfortable.
