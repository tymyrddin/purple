# Sandboxed production clones

## What?  

A sandboxed production clone is an isolated, near-identical copy of a live production environment, used for:  
- Safe testing of patches, updates, and security configurations  
- Malware analysis without risking real systems  
- Threat hunting using realistic traffic and logs  
- Developer testing without breaking production  

Unlike traditional staging environments, these clones:  
- Mirror real data (anonymised if needed)  
- Run in strict isolation (network segmentation, no outbound internet)  
- Can be reset on-demand (snapshot-based)  

---

## How to build a sandboxed clone  

### Data extraction & sanitisation  

Methods:  
- Database dumps (MySQL, PostgreSQL) with PII scrubbing  
- Virtual machine snapshots (VMware, Hyper-V, AWS AMIs)  
- Containerised clones (Docker/Kubernetes with volume mounts)  

Sanitisation Tools:  
- Anonymisation: `faker` (Python), `pg_anonymizer` (PostgreSQL)  
- Subset sampling: `jq` (JSON), `csvkit` (CSV)  

```bash
# Example: Create a sanitised MySQL dump  
mysqldump --single-transaction production_db | \  
  sed 's/real_email@domain.com/test_user@example.org/g' > sanitised_db.sql  
```

### Environment isolation  

Network Controls:  
- No internet access (iptables/nftables block outbound traffic)  
- Private VLANs (separate from production)  
- Host-based firewalls (allow only required ports)  

Access Restrictions:  
- Separate credentials (no production keys/secrets)  
- Time-limited sessions (auto-expire after 4 hours)  

### Automated deployment  

Infrastructure-as-Code (IaC) Options:  

| Tool      | Use Case                      | Example Command                      |  
|-----------|-------------------------------|--------------------------------------|  
| Terraform | Cloud VM/network provisioning | `terraform apply -var "env=sandbox"` |  
| Ansible   | Configuration management      | `ansible-playbook clone_prod.yml`    |  
| Vagrant   | Local VM cloning              | `vagrant up --provider=virtualbox`   |  

Example AWS Clone Setup:  
```bash
# Create a sandboxed VPC  
aws ec2 create-vpc --cidr-block 10.0.0.0/16 --tag-specifications 'ResourceType=vpc,Tags=[{Key=Name,Value=sandbox-clone}]'  

# Restrict outbound traffic  
aws ec2 create-security-group --group-name "sandbox-no-internet" --description "Block all egress" --vpc-id vpc-123  
aws ec2 revoke-security-group-egress --group-id sg-123 --ip-permissions '[{IpProtocol="-1", FromPort=-1, ToPort=-1, IpRanges=[{CidrIp="0.0.0.0/0"}]}]'  
```

## Tooling recommendations  

| Category           | Open-Source        | Enterprise                         |  
|--------------------|--------------------|------------------------------------|  
| Virtualisation | KVM, VirtualBox    | VMware vSphere, Nutanix            |  
| Containers     | Docker, Podman     | Red Hat OpenShift                  |  
| Orchestration  | Terraform, Ansible | HashiCorp Stack, AWS Control Tower |  
| Monitoring     | ELK Stack, Grafana | Splunk, Datadog                    |  

---

### Implementation checklist  

- [ ] Define data scope (full clone vs. subset)  
- [ ] Implement network isolation (VLANs/firewalls)  
- [ ] Automate deployment (IaC templates)  
- [ ] Schedule regular resets (e.g., weekly snapshots)  
- [ ] Audit access (who can spin up/down clones)  

Example Reset Policy:  
```text
All sandbox clones must:  
1. Be destroyed after 7 days unless exempted  
2. Log all user activity (ssh, database queries)  
3. Block outbound internet by default  
```

---

## Why this works 

- Reduces production risks from untested changes  
- Improves threat detection with realistic data  
- Cost-effective (cloud instances can be paused when unused)  
