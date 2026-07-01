# Cloud attack surfaces

The reconnaissance surface in a cloud environment is wider, more public, and more amenable to automated enumeration than
the on-prem equivalent. DNS records, certificate transparency logs, public storage buckets, exposed metadata endpoints,
leaked credentials in source repositories, and the structured naming conventions of cloud services all reduce the work
of mapping a target to scripted enumeration.

## Recurring patterns

Misconfigurations recur because the surface is large and the defaults are not always safe. A public storage bucket. An
over-permissive IAM role. A security group that allows 0.0.0.0/0 on a database port. A serverless function with debug
logging enabled in production. A managed database with public networking left on after a one-off migration. Each is a
single configuration mistake with substantial consequences, and each is more discoverable to an external observer than
the on-prem equivalent.

## Why the testing is harder than it looks

Testing the cloud attack surface from the inside is structurally different from testing on-prem networks. The surface is
not a network in the classical sense; it is a collection of API endpoints, identity-bound permissions, and configuration
state spread across multiple regions and services. A scanner that finds open ports cannot tell whether an IAM role is
over-permissive. A scanner that reads IAM policies cannot tell whether the policy attaches to anything that is currently
running.

The result is that cloud attack surface assessment requires understanding both the configuration model and the runtime
model, and producing findings that distinguish between "exposed but unused" and "exposed and load-bearing".

## Surface reduction

The work that produces results is systematic rather than tactical. Auditing public-facing assets on a cadence rather
than reactively. Monitoring for unintended exposure, with the assumption that exposure happens through deployment
changes rather than through deliberate decisions. Treating the cloud account itself as a high-value target, with the
access controls and audit trail that implies.

## Related

- [Shared responsibility](shared-responsibility.md)
- [Identity collapse and the control plane](identity-collapse.md)
- [Cloud-native detection](cloud-detection.md)
- [Cloud surface discovery](https://red.tymyrddin.dev/docs/in/cloud/notes/recon.html)
- [Cloud recon runbooks](https://red.tymyrddin.dev/docs/in/cloud/runbooks/index.html)
- [Cloud misconfigurations](https://red.tymyrddin.dev/docs/in/cloud/notes/misconfigurations.html)
- [Why cloud environments are hard to test](https://red.tymyrddin.dev/docs/in/cloud/notes/challenges.html)
