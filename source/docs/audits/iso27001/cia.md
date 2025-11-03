# Confidentiality, integrity, availability

The CIA triad is the foundation of information security. It describes three properties every organisation 
must protect in its information systems. Each one matters on its own, but security only works when all three 
are kept in balance.

| Aspect          | Core question                    | Relevant Annex A domains                                                                                       |
|:----------------|:---------------------------------|:---------------------------------------------------------------------------------------------------------------|
| Confidentiality | Who can see the data?            | A.5 Information security policies, <br/>A.6 Organisation of information security, <br/>A.9 Access control      |
| Integrity       | Can we trust the data?           | A.8 Asset management, <br/>A.12 Operations security, <br/>A.14 System acquisition, development and maintenance |
| Availability    | Can we use the data when needed? | A.12 Operations security, <br/>A.17 Information security aspects of business continuity                        |

## Confidentiality

Confidentiality is about ensuring that information is only accessible to those who are authorised to see it. 
Think of it as controlling who gets the keys:

* Role-based access control (who can access what)
* Encryption of data at rest and in transit
* Multifactor authentication
* Clean desk and locked screen policies
* Secure disposal of media and printouts
* Marking and handling of confidential documents

Examples:

* An HR database containing salary data is protected so only HR staff can view it.
* Customer data exported for reporting is encrypted before being sent to a partner.
* A USB drive with internal project files is securely wiped before reuse.
* A shared drive with open read access for “Everyone” violates confidentiality, even if no one misuses it.

Auditors will check whether permissions match job roles, whether encryption is actually enabled, and whether 
staff follow procedures for data handling. They may review access logs, policy documents, or system configurations.

## Integrity

Integrity means that information remains accurate, complete, and unaltered except by authorised actions. It ensures 
that what is stored or transmitted is what was intended and not corrupted, changed, or lost along the way:

* Validation of input and file formats
* Version control and audit trails
* Checksums, hashes, and digital signatures
* Change approval and segregation of duties
* Database transaction controls and rollback features

Examples:

* Financial figures in an accounting system must not be modified manually without authorisation.
* A signed PDF contract must remain identical after sending; digital signatures prevent unnoticed edits.
* Automated scripts that import supplier data validate the input before updating records.
* A ransomware attack that encrypts and renames files breaks integrity — even if backups exist.

Auditors will look for systems that track changes, enforce review or approval for edits, and detect data corruption or unauthorised modifications. They may check audit logs, version histories, or data validation settings.

## Availability

If a system is down, even perfect confidentiality and integrity are pointless. Availability means that information 
and systems are accessible to authorised users when needed:

* Regular, tested backups and restores
* Redundant power, storage, and network connections
* Service monitoring and alerting
* Preventive maintenance and patching schedules
* Business continuity and disaster recovery plans

Examples:

* A hospital records system must stay online 24/7; downtime can delay treatment.
* An e-commerce site going offline during a sales campaign causes direct financial loss.
* A ransomware incident can deny access to systems even if the data itself remains intact.
* Scheduled maintenance outside working hours supports availability without disrupting users.

Auditors will check whether backup procedures are tested, whether downtime is logged and reviewed, and whether 
continuity plans exist and align with business priorities. They may also ask to see the results of recovery tests.

## Balancing act

The CIA triad is not a checklist. It is a conversation between priorities: confidentiality, integrity, and 
availability often pull in different directions, and the right balance depends on your organisation, systems, 
and risks. Each element supports the others, but none can be absolute. 

### Confidentiality vs. Availability

Protecting sensitive information can limit access for those who need it, slowing operations. For example:

* Your threat intelligence team stores malware samples and internal reports on a secure sandbox. Access is heavily restricted, so when a SOC analyst on a late shift urgently needs a sample to investigate an incident, it takes hours to get approval, delaying response.
* A cloud storage bucket is encrypted with client-side keys, but the recovery keys are held by one overworked engineer who is on vacation. As a result, critical data is technically protected but temporarily unavailable.

### Integrity vs. Availability

Ensuring accurate, validated data can slow down workflows or automated processes. Like with:

* An automated SIEM ingestion pipeline checks logs against multiple integrity rules before accepting them. During peak traffic, the validation process queues log entries, delaying real-time alerting.
* A DevOps team enforces signed container images for production deployments. If the signing service is down, deployment is blocked, preventing urgent hotfixes.

### Confidentiality vs. Integrity

Restricting access for confidentiality can reduce review and error detection, affecting integrity.

* Only one senior engineer can approve configuration changes on a critical cloud environment. While access is tightly controlled, misconfigurations slip through because no one else can review changes in time.
* A financial reporting system restricts access to CFO and controller only. A minor formula error in a spreadsheet goes unnoticed until an external audit flags it. No one else was allowed to check the numbers.

## Practical

The CIA triad is a strategic conversation, not a mechanical checklist. Success comes from balancing priorities and 
making deliberate, documented choices.

1. Identify critical information and systems.
2. Assess which CIA element is most sensitive in each context.
3. Document trade-offs and decisions: why a control was chosen, why another was not, and compensating measures if any.
4. Be ready to explain your rationale calmly during an audit — auditors look for thoughtfulness, not perfection.

