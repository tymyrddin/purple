# Operational fragility

Cloud platforms make destructive actions easy in a way that on-prem infrastructure rarely did. A single click in a web
console can terminate a production database. A single API call from a misconfigured automation script can delete a
storage bucket. A single typo in a Terraform plan can roll back a year of state. The kinetic feedback that physical
infrastructure provided, the rack lights, the blinking switches, the colleague within shouting distance, is absent. The
action is silent, immediate, and as authorised as any other action the principal was permitted to take.

## Not a security failure in the usual sense

This is operational fragility, and it is structurally different from the security failure modes the rest of this section
describes. It is not an attacker exploiting a misconfiguration. It is a legitimate user, with legitimate credentials,
taking an action that the cloud platform was happy to authorise. The defence is not security-engineering in the
conventional sense; it is operational design.

The framing does the work because the responses look different. A security failure produces detection rules, hardening,
and incident response. An operational fragility produces role separation, change controls, and recovery design. Both are
work. Treating the second category as the first produces controls that an attacker would route around and that
legitimate users find obstructive.

## What reduces blast radius

Several patterns reduce the consequence of legitimate-but-mistaken actions.

Role separation, where the right to delete production is held by fewer principals than the right to read it. The
asymmetry is justified by the asymmetric cost of mistakes: a read action has bounded consequences, a delete action does
not.

Staged changes, where actions of consequence pass through review or dry-run before they execute. A Terraform plan
reviewed before apply. A "are you sure?" dialogue that requires typing the resource name. A two-key step for the most
destructive operations.

Tooling that confirms before destroying, with consequences spelled out in plain language. "This will delete 47 instances
and permanently remove the data on their attached volumes" is more useful than "Confirm deletion of selected
resources?".

Recovery design that assumes the action will be taken eventually and arranges for it to be reversible. Soft delete with
a retention period. Versioned storage. Backups that have been tested for restore rather than only for completion.
Configuration as code, with the code stored somewhere other than the system being configured.

## Why Friday at 16:43

The 16:43 Friday element is not incidental. The conditions under which production gets deleted by accident are
well-known: tired operator, end of week, intermittent attention, unfamiliar tooling, time pressure, after-hours change.
Designing operations to fail safely under those conditions is a different exercise from designing them to be efficient
under ideal ones.

A cloud platform that prevents accidental deletion at 14:00 on a Tuesday but not at 16:43 on a Friday is not actually
preventing accidental deletion. The hostile environment is the one where the prevention has to hold.

## Where this fits with the rest

This page links to none of the external pieces directly because the operational-fragility theme runs through the others
rather than concentrated in one place.

The [CI/CD exposure](cicd-exposure.md) page covers the deployment-pipeline version of this question: a pipeline with the
right to deploy is a pipeline with the right to break things, and the controls that prevent malicious breakage also need
to address mistaken breakage.

The [identity collapse](identity-collapse.md) page covers the credential-and-permissions version: who has the right to
do what, and whether the answer reflects the cost of getting it wrong.

The [shared responsibility](shared-responsibility.md) page covers the contractual version: the line between what the
provider is responsible for and what the customer is determines who is in a position to prevent which kinds of mistake.

The Friday 16:43 view is what those look like when you stack them on top of each other and ask: when this goes wrong,
who notices, who cleans up, and how much of what was lost is genuinely recoverable.

## Related

- [CI/CD exposure](cicd-exposure.md)
- [Identity collapse and the control plane](identity-collapse.md)
- [Shared responsibility](shared-responsibility.md)
