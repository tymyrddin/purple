# Cloud-native detection

Detection in cloud environments is mostly an exercise in collecting and correlating control-plane logs. Unlike on-prem
environments where the network and endpoints are the primary detection surface, in a cloud environment the API audit log
is the most informative single source. Every action of any consequence, from spinning up an instance to changing an IAM
policy, leaves a structured event with timestamp, principal, source, and outcome.

## The visibility problem

The volume of those events is high, the events are not all equally interesting, and the principals are not all human.
Service accounts perform automated actions that look superficially like attacker activity. Legitimate developer
workflows produce alerts that resemble compromise. Distinguishing signal from noise is the central detection-engineering
challenge in cloud, and the answer rarely scales without sustained investment in baselining.

The visibility problem is also a coverage problem. The audit log captures control-plane actions, but data-plane
activity (read access to a storage bucket, query traffic against a database, the contents of a function invocation) is
logged by different mechanisms with different defaults. An organisation that has tuned its detection to the audit log
alone is detecting half the activity worth seeing.

## Behavioural baselines

Behavioural baselines work better in cloud than in on-prem because the activity is more structured. A service account
that normally calls three APIs against four resources is detectably anomalous when it suddenly calls fifteen APIs
against fifty resources. The same pattern in an on-prem network is harder to characterise because the traffic shapes are
noisier.

The baselining work that produces useful detection is iterative. Initial baselines are wrong in specific ways, and the
alerts they generate are the input to refinement. A programme that treats the first set of alerts as the answer rather
than the starting point produces a tuning paralysis that never closes.

## Detection patterns at the early stage

For organisations beginning a cloud defence programme, the detection patterns that produce results are not the most
sophisticated; they are the ones that catch the most common attacks first. Cloud-account compromise via [leaked
credentials](attack-surface.md). Anomalous IAM activity. Unusual region usage. Unauthorised changes to logging configuration. Each of these
has a high-fidelity detection pattern and substantial defensive value.

## Hunting in cloud environments

Threat hunting in cloud is mostly hunting through [identity and control-plane behaviour](identity-collapse.md). Unusual role assumptions.
Cross-account access. Long-dormant credentials suddenly active. Changes to audit configuration.

## What automation trust does to detection

Cloud detection is shaped by automation in a way that on-prem detection is not. Most of the activity in a mature cloud
account is automated: deployment pipelines, scheduled jobs, autoscaling events, scripted maintenance. The detection
model has to distinguish between automated activity that is expected and automated activity that is not, which is a
different problem from distinguishing human activity from automated activity. The hardest case is the [legitimate-but-destructive
action](operational-fragility.md), authorised and expected in shape, wrong only in intent or timing. Automation trust, the implicit confidence
that the automation is doing what it was designed to do, becomes a security property that has to be earned and audited
rather than assumed.
