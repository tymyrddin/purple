# Building a raft

![Raft](/_static/images/raft.png)

With risks mapped and legal obligations understood, it is time to build your raft. This is the combination of technical, organisational, and procedural safeguards that will carry you safely across. Begin with governance, as NIS2 requires, then add technical controls, operational capabilities, and the human element.

## Governance is not optional

The management body shall approve all security measures, oversee their implementation, participate in training, 
and may bear personal liability for failures. Responsibility cannot be fully delegated. Organisations may appoint a 
security officer or chief information security officer with clear reporting lines to the board. Define roles and 
responsibilities across the organisation so everyone knows who is accountable for what. Establish decision-making 
frameworks that work in practice.

Policies shall have board approval. At minimum, these include the information security policy, acceptable use policy, 
incident response procedures, business continuity plans, supply chain security procedures, and data classification 
and handling instructions. These documents are operational guides.

## Technical implementation builds the foundation

Every control encodes an assumption about the environment it is designed to protect. Network segmentation assumes traffic follows expected paths. MFA assumes the second factor is not recoverable through the same attack path as the first. Patch management assumes the patching window closes exposure before exploitation. Selecting a control means selecting its assumptions. Before committing to an implementation, it is worth asking: what conditions are needed for this control to produce its intended effect, and do those conditions hold in this environment?

Identity and access management should start with multifactor authentication on critical systems. Implement role-based access control aligned with job responsibilities, and privileged access management for administrative functions. Conduct regular access reviews to remove permissions that are no longer required.

Network and system security can include segmentation to contain breaches, intrusion detection to spot attacks, continuous monitoring and logging, patch management to close known vulnerabilities, endpoint protection, and vulnerability scanning to identify weaknesses before attackers do.

Data protection may involve encrypting information both at rest and in transit, maintaining secure and tested backups, implementing data loss prevention measures, and ensuring secure disposal of information at the end of its life.

Secure development practices should be integrated into procurement and development processes. Include security requirements in vendor contracts, follow secure coding standards, perform testing including static and dynamic analysis as well as penetration testing, and apply change management controls to prevent new risks from being introduced.

## Operational capabilities make it real

Incident response should include the ability to detect and monitor events, classify their severity, follow response playbooks, escalate issues when necessary, use communication templates for regulatory reporting, and perform forensic investigations to understand what occurred.

Business continuity begins with a business impact analysis to identify critical functions and dependencies. Define recovery time and recovery point objectives, document backup and restoration procedures, test them regularly, and maintain disaster recovery plans. Crisis management procedures enable leadership to make rapid decisions when needed. All plans should be exercised to ensure they work in practice.

Asset management may include maintaining a comprehensive inventory, classifying and assigning ownership for each asset, managing configurations to maintain known-good states, and tracking the lifecycle from acquisition to disposal.

## People and culture complete the vessel

Security awareness training should be continuous and practical. Provide regular sessions for all staff, role-specific training for IT, security, and management, and phishing simulations to test effectiveness. Maintain visibility of security through ongoing communications, and ensure management understands their obligations under NIS2.

[CTF and roleplay exercises](../../foundations/organisational-development/roleplay.md) extend this to technical competence: participants work through structured challenges with immediate feedback on success or failure. The format is self-correcting by design: the flag is either captured or it isn't, and the environment is realistic enough to produce observable behaviour rather than recalled procedure. A staff member who completes an incident-analysis or network-attack CTF has produced better competence evidence than one who attended the equivalent training session. Facilitation counts for more than delivery here. Awareness that changes behaviour comes from environments where people encounter realistic situations and have to make real decisions. A briefing that presents a recent incident from the sector and asks "what would you have done?" produces more durable learning than one that explains the correct procedure. The debrief, where people articulate what they noticed and what they would do differently, is where the awareness is actually formed.

Human resources security begins at hiring. Conduct background checks where appropriate, include security clauses in contracts, deliver onboarding briefings, and ensure offboarding procedures revoke access and recover equipment. Employees should acknowledge acceptable use policies.

## Output

By the end of this stage, the organisation will have implemented controls that function effectively, documented procedures that staff can follow, trained personnel who understand their roles, and a governance structure with clear authority.

