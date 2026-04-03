# Workflows that get followed

## Turning playbooks into actions

Workflows are where knowledge becomes muscle memory. [Playbooks](playbooks.md) describe the intended response; a workflow makes it happen. When the pressure hits, people do not want explanations. They want the next 
step, right now.

A workflow that slows people down will be bypassed. A workflow that guides them will be used instinctively.

## What good workflows look like

### The “breadcrumb trail”

A guided sequence that:

* Shows the next step clearly
* Offers the exact query / button / command needed
* Captures evidence automatically
* Prevents out-of-order or skipped steps

If analysts leave the system to find instructions, your workflow is not a workflow.

### The “guard rail”

A workflow that stops self-inflicted chaos:

* Safe defaults
* Policy surfaced at the moment of action
* Hard stops on destructive steps
* Automatic routing to the right approver

The point is not control; it is preventing preventable pain.

### The “handover chain”

A workflow designed for the reality of changing shifts:

* Persistent context
* Automatic notifications and ownership
* Clear task history
* No information loss during handover

This is how you prevent incidents freezing because someone went home.

## Workflow design principles

1. Embedded, not external: Workflows live in the tools people already use.
2. Minimal steps, maximal clarity: Every extra click is a chance to bail out.
3. Automation first: Humans make decisions; systems do the grunt work.
4. No bureaucracy creep: Approvals where necessary, not everywhere.

Bureaucracy creep is worth pausing on, because it does not appear by accident. Approval steps accumulate because each 
one was added by someone protecting themselves or their team from accountability for a decision. 

The [PSL framing](../foundations/problem-solving/in-security.md) is useful here: the political layer shapes the 
workflow as much as the rational one. A workflow audit that only asks "is this step necessary?" will not remove steps 
that exist for political reasons. The question to ask is: what consequence was this approval step added to prevent, 
and for whom?

## Where workflows probably live

* Ticketing systems (Jira, ServiceNow, RTIR)
* SIEM/SOAR platforms
* ChatOps bots in Teams / Slack
* Endpoint security consoles

If a workflow requires opening yet another tool, it will die quietly and alone.

## Related

- [Playbooks](playbooks.md)
- [Manuals that actually work](manuals.md)
- [SOC workflows](../making-of/soc/workflows.md)
- [SIRT structure](../making-of/sirt/structure.md)
