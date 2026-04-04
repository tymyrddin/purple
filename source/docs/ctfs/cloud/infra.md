# Infrastructure requirements

To host cloud challenges:

* Cloud provider accounts (AWS/GCP/Azure): free tiers work for basic labs
* Terraform/Ansible: automate deployment of vulnerable setups
* Containerisation (Docker/Kubernetes): for isolated, ephemeral challenge environments
* Monitoring and rate limiting: prevent abuse (AWS GuardDuty, custom scripts)
* Flag validation system: auto-check exploit success (stolen secrets, RCE confirmation)

This combines with the cloud security reference material for
- [AWS](https://blue.tymyrddin.dev/docs/dev/devsecops/aws/),
- [Azure](https://blue.tymyrddin.dev/docs/dev/devsecops/azure/),
- [GCP](https://blue.tymyrddin.dev/docs/dev/devsecops/gcp/), and
- [on-prem](https://blue.tymyrddin.dev/docs/dev/devsecops/on-prem/).

Approach: first set up secure pipelines for a small Dockerised app, then introduce the vulnerabilities the
challenge is built around. This avoids building on a misremembered version of what "secure" looks like.
