# Safety notes for cloud CTF labs

Running vulnerable cloud environments requires strict isolation and active monitoring to prevent accidental
breaches or abuse.

## Dedicated cloud accounts (non-prod)

Limits blast radius if credentials leak and prevents accidental damage to real business resources.

* AWS: create a new account under AWS Organisations with no payment methods attached
* GCP: use a separate project with billing alerts (€0.01 threshold)
* Azure: set up a test subscription with spending caps

```bash
aws organizations create-account --email "ctf-labs@yourdomain.com" --account-name "RootMe-Cloud-CTF"
```

## Auto-destroy timers

Stops forgotten labs from accumulating costs and prevents long-term exposure of vulnerable resources.

AWS Lambda with CloudWatch can schedule a termination function. Terraform can also handle it:

```hcl
resource "null_resource" "destroy_after" {
  triggers = {
    always_run = timestamp()
  }

  provisioner "local-exec" {
    command = "sleep 7200 && terraform destroy -auto-approve"
  }
}
```

Alternative: AWS EventBridge to auto-terminate resources tagged `CTF=true` after 2 hours.

## Abuse monitoring

CTF labs attract participants looking to mine crypto or host malware.

* AWS GuardDuty: enable alerts for `Cryptocurrency:EC2/BitcoinTool.B!DNS` and
  `UnauthorizedAccess:IAMUser/InstanceCredentialExfiltration`
* GCP log alerts: monitor `compute.instances.create` from non-trusted IPs and `storage.buckets.list` spikes
* Custom scripts: detect abnormal CPU usage (above 90% for 10 minutes triggers auto-shutdown)

```bash
aws guardduty create-detector --enable --finding-publishing-frequency FIFTEEN_MINUTES
```

## Network isolation

Prevents a lab compromise from spreading to other environments.

* AWS: dedicated VPC with no peering or NAT
* GCP: enable VPC Service Controls to block exfiltration
* Azure: NSGs blocking outbound traffic except to whitelisted IPs

```hcl
resource "aws_vpc" "ctf_isolated" {
  cidr_block           = "10.0.0.0/16"
  enable_dns_hostnames = false
}
```

## Credential hygiene

Leaked keys compromise the whole cloud organisation.

* Short-lived credentials: AWS STS AssumeRole with maximum 1-hour sessions
* GCP: disable service account key creation, use Workload Identity instead
* Azure: require MFA for all users

```bash
gcloud iam deny-policy --organization=YOUR_ORG_ID \
  --deny-all --identity='*' \
  --permissions='iam.serviceAccountKeys.create'
```

## Legal

CTF labs can be mistaken for real attacks.

* AWS: submit a penetration testing request
* GCP/Azure: document lab IP ranges for abuse teams
* Add a "This is a CTF" banner to all web interfaces

## Pre-launch checklist

1. Dedicated cloud account with billing alerts
2. Terraform destroy-after timer (2-4 hours maximum)
3. GuardDuty or equivalent log monitoring enabled
4. Network isolation in place (no peering, egress filtering)
5. Legal and abuse team notified
