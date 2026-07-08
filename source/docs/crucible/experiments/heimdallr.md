# Heimdallr

![Heimdallr](/_static/images/heimdallr.png)

[Heimdallr](https://github.com/tymyrddin/heimdallr) is a place to try detection engineering rather than read
about it. It runs OpenSearch and Sigma locally: load a JSONL dataset, write or import a Sigma rule, run it,
and see exactly what fired and what did not, scoped per dataset so a rule reveals whether it is specific or
noisy.

The experiment is in the last of its four views. Data holds what is loaded, Detections holds which rules to
run, Findings holds what fired per dataset, and Experiments compares runs as a rule is iterated. That last one
is the point here: it turns the question from "does this rule look right" into "what changed in what fired
when the rule changed". A rule that fires on the attack technique and stays quiet on the benign dataset is a
finding. One that lights up on both is a lesson about the gap between what a rule was meant to match and what
it actually matches.

Public attack datasets make the ground, each tagged by the ATT&CK technique it exercises: OTRF Security
Datasets (the easiest start, much of it already JSONL), EVTX-ATTACK-SAMPLES, Atomic Red Team, and the Boss of
the SOC scenario set.

## Running it

`./ctl up` starts OpenSearch, its Dashboards, and the UI; `./ctl ui` prints the UI URL (`http://localhost:5000`).
Drop a dataset directory under `ingest/` and load it from the Data view, pick or author a rule from
`rules/sigma/` in Detections, and read what fired in Findings. `./ctl detect` is the command-line shortcut for
compiling the Sigma rules and running detections, and the OpenSearch Dashboards surface at
`http://localhost:5601` is the deeper hunt-and-tune view.

*Last updated: 2 July 2026*
