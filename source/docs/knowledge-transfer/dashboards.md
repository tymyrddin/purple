# Dashboards that actually get used

A dashboard that looks impressive in a demo but is ignored during an incident is not a dashboard; it is decor. The 
reason dashboards become decor is usually not bad design. It is that the dashboard was built to demonstrate capability 
or satisfy an audit rather than to serve the person doing the work. 

[SEM's model-drift observation](../foundations/system-effectiveness/core-triad.md) applies directly: the dashboard 
encodes a model of what matters; when that model is shaped by what leadership wants to see rather than what analysts 
need to see, the two diverge, and the analyst stops consulting it. The design principles below address the symptoms; 
the conditions question is who the dashboard is actually built for.

Dashboards that work answer three questions instantly:

1. Is something wrong?
2. Where is it happening?
3. How bad is it?

If analysts cannot answer these at a glance, the dashboard has failed its only job.

## What good dashboards look like

### The “smoke alarm”

A brutally simple view showing:

* Three to five critical indicators
* Clear thresholds and severity
* A single screen without scrolling
* Immediate visual cues for “stop everything” moments

If you need a manual to read the dashboard, bin it.

### The “where is the fire?”

A situational board that shows:

* Affected systems
* Likely propagation paths
* Status of containment
* Alert volume trends
* Hotspots and bottlenecks

This is the board everyone naturally gravitates to during a live incident.

### The “posture snapshot”

A calm-day dashboard for spotting slow-moving disasters:

* Patch coverage
* Endpoint gaps
* Backup health
* Unusual authentication patterns
* Data ingestion issues

This is where tomorrow’s breach quietly announces itself.

## Design principles for dashboards

1. Zero friction: No nested menus, no tooltips, no scavenger hunts.
2. Human-first: Colour only where it matters, minimal clutter, no vanity charts.
3. Operational, not political: Executives get their own dashboard; this one is for people doing real work.
4. Instant refresh: If the threat moves faster than your updates, the dashboard is ornamental.

## Where dashboards live

* On a wall in the SOC
* On every analyst’s second monitor
* In a pinned tab, always open
* On a TV in the incident room

Dashboards that are hard to reach become dashboards nobody reaches for.

## Related

- [Playbooks](playbooks.md)
- [Workflows](workflows.md)
- [SOC detection](../making-of/soc/detection.md)
- [Incident response metrics](../incident-response/metrics.md)
