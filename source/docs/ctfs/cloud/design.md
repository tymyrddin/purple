# Challenge design principles

Effective cloud CTF challenges progress from basic reconnaissance to full-scale cloud compromise, teaching
practical skills at each level.

## Beginner: "The Cloud Tourist"

Goal: introduce fundamental cloud concepts and tools.

Example challenge: "Find the open S3 bucket named flag-bucket-{randomID} and retrieve flag.txt."

Skills taught:

* Basic enumeration using awscli, gobuster, or manual inspection
* Public bucket identification and recognising misconfigured storage
* Cloud provider navigation (AWS Console, GCP Storage Explorer)

Real-world parallel: bug bounty scenarios finding exposed S3 buckets with sensitive data.

Defensive takeaway: always set BlockPublicAccess and audit bucket policies.

```bash
aws s3 ls s3://flag-bucket-123 --no-sign-request
curl https://flag-bucket-123.s3.amazonaws.com/flag.txt
```

## Intermediate: "The Privilege Escalator"

Goal: teach IAM exploitation, lateral movement, and OSINT.

Example challenge: "A Lambda function has overprivileged IAM rights. Steal its keys and escalate to an EC2 instance."

Skills taught:

* AWS CLI and SDK usage: extracting Lambda env vars, assuming roles
* IAM privilege escalation: exploiting `iam:PassRole`, `sts:AssumeRole`
* OSINT for cloud credentials: searching GitHub, logs, metadata

Real-world parallel: Lambda with AdministratorAccess leaking keys.

Defensive takeaway: Principle of Least Privilege for Lambda roles.

Exploit chain:

* Dump Lambda env vars (via RCE or `/proc/environ`)
* Find AWS keys, run `aws sts get-caller-identity`
* Escalate via `iam:PassRole` to `aws ec2 describe-instances`

## Advanced: "The Cloud Kingdom Takedown"

Goal: simulate full cloud compromise across AWS/GCP/Azure.

Example challenge: "A GCP service account key was leaked. Use it to compromise the entire organisation."

Skills taught:

* Cloud pivoting: moving from one service to another
* OAuth and API abuse: escalating via `iam.serviceAccounts.getAccessToken`
* Lateral movement from Cloud Functions to Compute to BigQuery

Real-world parallel: APT attack using stolen service account keys for cloud takeover.

Defensive takeaway: disable key creation, enforce VPC Service Controls, monitor IAM anomalies.

Exploit chain:

* Leaked key: `gcloud auth activate-service-account`
* Enumerate resources: `gcloud projects list`
* Privilege escalation: abuse `roles/owner` on a project
* Data exfiltration: dump BigQuery datasets

## Challenge progression flow

A cloud CTF does not just teach attack techniques. Every challenge creates a natural opportunity to ask: what
would have detected this, and what would have prevented it.

| Level        | Attack path                       | Defensive lesson          |
|:-------------|:----------------------------------|:--------------------------|
| Beginner     | Find open S3 bucket               | Secure public storage     |
| Intermediate | Lambda to EC2 takeover            | Least privilege for IAM   |
| Advanced     | Service account key to org breach | Service account hardening |
