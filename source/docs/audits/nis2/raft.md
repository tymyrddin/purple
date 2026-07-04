# Building a raft

![Raft](/_static/images/raft.png)

NIS2, Articles 20 and 21: governance, technical measures, operational capability, and the people aboard.

With risks mapped and legal obligations understood, the raft gets built: the combination of technical,
organisational, and procedural safeguards that will carry the organisation across. Governance comes first, as
NIS2 requires, then technical controls, operational capabilities, and the human element.

## Governance is not optional

Under Article 20, the management body shall approve security measures, oversee their implementation,
participate in training, and may bear personal liability for failures. Responsibility cannot be fully
delegated. A security officer or CISO with clear reporting lines to the board gives the obligation a face;
roles and responsibilities defined across the organisation make clear who is accountable for what; a
decision-making framework only counts if it works under pressure, not just on the org chart.

Policies carry board approval. At minimum: the information security policy, acceptable use policy, incident
response procedures, business continuity plans, supply chain security procedures, and data classification and
handling instructions. These documents are operational guides, not shelf furniture.

## Technical implementation

Every control encodes an assumption about the environment it is designed to protect. Network segmentation assumes traffic follows expected paths. MFA assumes the second factor is not recoverable through the same attack path as the first. Patch management assumes the patching window closes exposure before exploitation. Selecting a control means selecting its assumptions. Before committing to an implementation, it is worth asking: what conditions are needed for this control to produce its intended effect, and do those conditions hold in this environment?

Identity and access management usually starts with multifactor authentication on critical systems, role-based
access control aligned with job responsibilities, privileged access management for administrative functions,
and regular access reviews to remove permissions no longer required.

Network and system security can include segmentation to contain breaches, intrusion detection, continuous
monitoring and logging, patch management to close known vulnerabilities, endpoint protection, and vulnerability
scanning to find weaknesses before attackers do.

Data protection may involve encrypting information at rest and in transit, maintaining secure and tested
backups, data loss prevention, and secure disposal at end of life.

Secure development practices belong in procurement and development alike: security requirements in vendor
contracts, [secure coding](https://blue.tymyrddin.dev/docs/dev/appsec/coding/) standards, testing that includes
static and dynamic analysis as well as penetration testing, and change management controls that keep new risks
from arriving with new releases.

## Operational capabilities

Incident response covers detection and monitoring, severity classification, response playbooks, escalation,
communication templates for regulatory reporting, and forensic investigation to understand what occurred.

Business continuity begins with a business impact analysis identifying critical functions and dependencies,
then recovery time and recovery point objectives, documented and regularly tested backup and restoration
procedures, disaster recovery plans, and crisis management procedures that let leadership decide quickly. A
plan that has never been exercised is a hope with a filename.

Asset management may include a comprehensive inventory, classification and ownership for each asset,
configuration management to maintain known-good states, and lifecycle tracking from acquisition to disposal.

## People and culture

Security awareness training works when it is continuous and practical: regular sessions for all staff,
role-specific training for IT, security, and management, and phishing simulations to test effectiveness;
AI-generated scenarios that reflect current attack patterns produce more realistic tests than template-based
approaches. Visibility through ongoing communication, and management that understands its NIS2 obligations,
complete the picture.

[CTF and roleplay exercises](../../foundations/organisational-development/roleplay.md) extend this to
technical competence: participants work through structured challenges with immediate feedback on success or
failure. The format is self-correcting by design: the flag is either captured or it isn't, and the environment
is realistic enough to produce observable behaviour rather than recalled procedure. A staff member who
completes an incident-analysis or network-attack CTF has produced better competence evidence than one who
attended the equivalent training session.

Facilitation counts for more than delivery here. Awareness that changes behaviour comes from environments
where people encounter realistic situations and have to make real decisions. A briefing that presents a recent
incident from the sector and asks "what would you have done?" produces more durable learning than one that
explains the correct procedure. The debrief, where people articulate what they noticed and what they would do
differently, is where the awareness is actually formed.

Human resources security begins at hiring: background checks where appropriate, security clauses in contracts,
onboarding briefings, offboarding procedures that revoke access and recover equipment, and acknowledged
acceptable use policies.

## Output

By the end of this stage, the organisation has implemented controls that function effectively, documented
procedures that staff can follow, trained personnel who understand their roles, and a governance structure with
clear authority.

## Related

* [ISO 27001 The gear depot](../iso27001/gear-depot.md)
* [ISO 22301 The factory's emergency systems](../iso22301/emergency-systems.md)
* [IEC 62443 Locks and patrols](../iec62443/locks-and-patrols.md)
