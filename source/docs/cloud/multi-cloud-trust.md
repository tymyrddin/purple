# Multi-cloud trust boundaries

The trust boundary between cloud providers is structurally different from the trust boundary inside a cloud account.
Cross-cloud federation, identity providers that span clouds, and data flows that cross provider lines all create trust
assumptions that are harder to reason about than single-cloud security.

## Lock-in as a security property

Lock-in is the strategic dimension that determines whether trust boundaries are even reviewable. A workload tightly
coupled to a specific provider's services has the security properties of that provider, with no easy comparison and no
realistic exit. A workload designed for portability has worse single-provider economics and a better strategic position
when the question of moving comes up.

The exit work is rarely free. By the time the question of moving becomes urgent, the answer is "yes, but it will take a
year" if the architecture supports it, and "no, but we will pretend otherwise" if it does not. The realistic path is to
do the lock-in assessment before the exit becomes urgent, which is when the assessment is least likely to feel
necessary.

## On-prem as alternative

Self-hosted infrastructure on providers like Hetzner or OVH is not strictly cloud in the AWS/GCP/Azure sense, but it
sits in the same architectural space and addresses some of the lock-in concerns directly. The trade-offs include lower
abstraction (more operational work) and different jurisdictional positioning.

## Jurisdiction and compliance

Jurisdiction sits alongside lock-in and is harder to engineer around. Cloud workloads are subject to the legal regime of
wherever the data physically lives, which sometimes differs from the regime the customer operates under. Regulatory
compliance frameworks attempt to bridge these regimes; the bridges are imperfect.

GDPR is the most-litigated example. The technical and procedural work of compliance differs by provider, and the pattern
recurs in other regulatory frames with the same structural challenge: the provider's data handling has to be auditable
enough for the customer to demonstrate compliance, and the customer's controls have to extend across whatever providers
are in scope.

## Related

- [Shared responsibility](shared-responsibility.md)
- [CI/CD exposure](cicd-exposure.md)
- [SaaS dependency risk](saas-dependency.md)
- [Big tech cloud exit checklist](https://blue.tymyrddin.dev/docs/dev/devsecops/cicd/exit-checklist.html)
- [Google Cloud (GCP) lock-in assessment](https://blue.tymyrddin.dev/docs/dev/devsecops/gcp/lock-in.html)
- [On-prem and alternative clouds lock-in assessment](https://blue.tymyrddin.dev/docs/dev/devsecops/on-prem/lock-in.html)
- [Best practices for securing on-premises cloud services](https://blue.tymyrddin.dev/docs/dev/devsecops/on-prem/README.html)
- [On-prem at Hetzner: cost notes](https://blue.tymyrddin.dev/docs/dev/devsecops/on-prem/estimated-costs.html)
- [GDPR on Google Cloud](https://blue.tymyrddin.dev/docs/dev/devsecops/gcp/gdpr-compliance.html)
- [GDPR compliance on Hetzner](https://blue.tymyrddin.dev/docs/dev/devsecops/on-prem/gdpr-compliance.html)
- [Protecting an Amazon cloud kingdom from barbarians (and Dave)](https://blue.tymyrddin.dev/docs/dev/devsecops/aws/index.html)
