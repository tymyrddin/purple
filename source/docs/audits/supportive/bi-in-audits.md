# Use of BI in audits

Audit and compliance work generates volume: event logs, asset inventories, access records, control evidence,
training results, incident reports. Business intelligence tooling turns that volume into audit-ready outputs,
dashboards showing control status over time, trend analysis across review cycles, and gap views organised for
board-level reading. Not every scale problem needs a model: where the analysis is deterministic, a query beats
an inference, because it is explainable by construction, which counts for a great deal on the day a
supervisory authority asks how a number was produced.

## The dependency question

Audit data is among the more sensitive material an organisation holds. It contains personal data (access logs
with usernames, incident reports naming individuals, training records) and, more quietly, a map of where the
organisation is weakest: open findings, unpatched populations, failed tests. Where that material lives, and
under whose jurisdiction, is a decision, not a default.

For European organisations the decision has two layers: 

The legal one: transfers of personal data to US-hosted services have run through three successive frameworks, with 
Safe Harbour and Privacy Shield each struck down by the Court of Justice and the current Data Privacy Framework facing 
challenges of its own; building an evidence pipeline on a transfer basis with that history is a risk decision worth 
making consciously. 

The structural one: under the US CLOUD Act, a provider's jurisdiction follows the provider, not the data centre,
so an EU region of a US platform changes latency and residency optics without changing who can be compelled
to produce the data. Lessening the dependency means choosing by operator, not by map pin.

## Dashboards worth building

A dashboard is a rendered query, and it shows exactly what the underlying
data collection has earned; what the tooling offers is views. Four kinds recur:

* Control status over time: patch compliance, access review completion, backup success, as trends rather than snapshots, the form boards and supervisors tend to read.
* Findings ageing: open corrective actions by age and class, where the perpetual eighty-per-cent action becomes visible.
* Evidence completeness: which controls have current artefacts and which are running on last year's, read from the [evidence base](evidence.md) rather than kept beside it.
* Exercise and awareness metrics across cycles: click-rate trends, drill timings against objectives.

The honest-metrics caveat from [continuous monitoring](continuous-monitoring.md) applies with extra force once
dashboards exist: a well-designed dashboard of dishonest metrics is a measurement of the metric, beautifully
presented.

## The options, by dependency

* Self-hosted open source: [Metabase](https://www.metabase.com/) and [Apache Superset](https://superset.apache.org/) cover dashboarding, [KNIME](https://www.knime.com/) covers data preparation and repeatable pipelines with the audit trail that repeatability brings. Full control, EU infrastructure or on-premises, and the operational burden that comes with running anything.
* EU-based commercial platforms: [Jedox](https://www.jedox.com/en/), [Pyramid Analytics](https://www.pyramidanalytics.com/), and [Toucan Toco](https://www.toucantoco.com/en/plans) among them, where enterprise support, governance features, and someone to call are worth the licence.
* EU regions of US platforms: the least change from an existing estate, and the option that resolves residency without touching jurisdiction, for the reason above.

Deployment model decides more than product choice. The same classification discipline that governs the
evidence base governs what goes into the dashboards: aggregates and trends travel more safely than raw logs,
and a dashboard fed by pseudonymised or aggregated data answers the board's questions without exporting the
sensitive layer at all.

## Dashboards as evidence

A dashboard used in compliance work is itself an artefact, and the
[attributes of a usable artefact](evidence.md) apply: the underlying queries are versioned and reproducible,
the data sources and exclusions are named, and a snapshot carries its date. A trend line nobody can regenerate
is a screenshot with confidence. Where the queries are kept with the evidence chain, the dashboard becomes
part of the demonstration that monitoring is real; where they are not, it is decoration.

## Related

* [Use of AI in audits](ai-in-audits.md)
* [Evidence](evidence.md)
* [Continuous compliance monitoring](continuous-monitoring.md)
* [EU regulations reference](eu-regulations.md)
