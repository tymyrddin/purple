# CI/CD exposure

The pipeline that builds and deploys to a cloud environment is a security boundary that most threat models treat as
infrastructure. Treating it as a target produces different findings.

## The pipeline as privileged access path

A CI/CD system has, by definition, the credentials needed to deploy to production. It has source code access, often
build secrets, sometimes signing keys, and a privileged path into the cloud account that the security team may not be
able to easily revoke. A compromise of the pipeline is functionally equivalent to a compromise of the production
environment, and is often less visible because the activity looks like normal deployment traffic. The same access makes
the pipeline a source of [operational fragility](operational-fragility.md): the right to deploy is the right to break,
whether the trigger is malice or a bad merge on a Friday afternoon.

The pipeline also has the build-time access that determines what runs. Code that passes review and tests can be modified
during the build by a compromised pipeline before the artefact is signed. The downstream verification, where it exists,
is signing-key based and depends on the pipeline's own keys, which the pipeline holds.

## What hardening looks like

The hardening work is recognisable. Strict access controls on pipeline configuration, with changes reviewed by people
who understand what they enable. Short-lived credentials for deployment, scoped narrowly to the resources the pipeline
actually needs. Audit logs from the CI/CD system fed into the same SIEM as cloud audit logs, so that the join between
pipeline activity and cloud-account activity is visible to defenders. Pipeline changes reviewed with the same rigour as
production changes, because they are production changes by another route. Segregation between the build environment and
the deployment environment, so that a compromise of the build does not directly imply a compromise of the deployment.

## Multi-cloud and on-prem variants

The pipeline assumptions differ when the deployment target [spans clouds](multi-cloud-trust.md), or moves between cloud and on-prem, or replaces
a managed CI/CD with a self-hosted one. The credentials, the secret-management story, and the network access patterns
each change.

[Identity-federation patterns](identity-collapse.md) reduce the long-lived credential surface significantly, particularly on cloud providers
where workload identity federation is mature.

## The exit dimension

The strategic question, for an organisation that has settled into a single CI/CD provider, is the lock-in implication.
The pipeline is portable in principle and often less portable in practice; the assumptions baked into provider-specific
syntax accumulate. A migration from one CI/CD platform to another is rarely a free week of engineering, and the cost is
rarely visible until the migration becomes urgent for other reasons.

## Hardening the pipeline

- [From code to cloud without the exploits: a CI/CD security fairy tale](https://blue.tymyrddin.dev/docs/dev/devsecops/cicd/index.html)
- [Multi-cloud and on-prem CI/CD deployment](https://blue.tymyrddin.dev/docs/dev/devsecops/cicd/next.html)
- [Foundation for a secure GCP deployment pipeline](https://blue.tymyrddin.dev/docs/dev/devsecops/gcp/pipeline.html)
- [Big tech cloud exit checklist](https://blue.tymyrddin.dev/docs/dev/devsecops/cicd/exit-checklist.html)
