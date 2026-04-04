# Cloud vulnerabilities for challenges

From easy to advanced.

## Storage and access misconfigurations

* S3/GCP bucket enumeration (open listings, sensitive data leaks)
* Azure Blob Storage public read exploits
* Presigned URL abuse (time-limited but guessable URLs)

## IAM and privilege escalation

* Overprivileged Lambda roles (exfiltrate env vars)
* AWS AssumeRole hijacking via stolen STS tokens
* GCP service account key leaks

## Serverless and API exploits

* Lambda RCE via malicious event inputs
* API Gateway misconfigs (CORS, auth bypass)
* GraphQL introspection to data dump

## CI/CD pipeline attacks

* GitHub Actions token theft
* Jenkins/GitLab RCE via unauthenticated endpoints
* ArgoCD SSRF to cluster takeover

## Container and Kubernetes attacks

* Docker socket exposure to host escape
* Kubernetes dashboard no-auth to pod exec
* etcd unauthenticated access to cluster secrets

## Advanced cloud-native exploits

* AWS SSM Session Manager abuse
* GCP Cloud Build privilege escalation
* Azure Automation Account RCE
