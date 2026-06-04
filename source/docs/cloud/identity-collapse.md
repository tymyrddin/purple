# Identity collapse and the control plane

In a sufficiently mature cloud environment, security collapses into identity security. The control plane API is the
entry point to almost everything: instances, storage, network, secrets, billing, and the audit log itself. Whoever has
the right token, role, or session has the cloud environment. The traditional notion of "perimeter" stops being a useful
frame.

## IAM as central battleground

This makes IAM the central battleground. Persistence in a compromised cloud account is rarely about leaving a process
running on a machine; it is about establishing identity-based footholds that survive even if the original credential is
rotated. A new IAM user with administrative permissions. An overly broad service account key. A federated identity
provider trust that nobody audits. An OAuth token that does not expire. Each is durable in a way that traditional
persistence mechanisms are not, and each is less visible to detection systems oriented to host-level activity.

## Reaching the control plane

Initial access into the control plane often does not look like a traditional intrusion. A leaked credential in a public
repository, a phishing victim with privileged access, a misconfigured CI/CD pipeline with deployment credentials, or a
compromised endpoint with cached cloud session tokens, each produces control-plane access without the network-level
signatures that endpoint-focused detection is tuned for.

## Hunting for control-plane persistence

Detection in this domain depends on watching the control plane closely. Unusual API calls. IAM changes outside normal
change windows. New credential creation events. Role assumptions from unusual sources. Changes to the audit
configuration itself. Each is a signal worth alerting on, with the understanding that a sufficiently sophisticated
attacker will attempt to disable the audit configuration before doing anything visibly suspicious.

The general principle is that anomalous identity behaviour is more informative in cloud than in on-prem, because the
activity is more structured and the legitimate baseline is more describable.

## Why the collapse is structural

The identity-centric posture of cloud security is not a design oversight. Cloud platforms are explicitly
identity-centric: the API gates everything, every action is attributed to a principal, and the access decisions are
bound to identity rather than to network location. This is what makes cloud platforms scalable; it is also what makes
them collapse into identity security in a way that on-prem environments do not.

Treating identity as the primary security boundary, and the network as a secondary one, is the conceptual shift that the
rest of cloud defence depends on. Programmes that have not yet made this shift will produce defensive postures that look
reasonable on a diagram and miss the actual attack patterns.

## Related

- [Cloud attack surfaces](attack-surface.md)
- [Metadata service abuse](metadata-abuse.md)
- [Cloud-native detection](cloud-detection.md)
- [Cloud control plane persistence](https://red.tymyrddin.dev/docs/through/persistence/notes/cloud.html)
- [Cloud IAM persistence](https://red.tymyrddin.dev/docs/through/persistence/runbooks/cloud-iam.html)
- [Cloud initial access playbooks](https://red.tymyrddin.dev/docs/in/cloud/playbooks/index.html)
- [Playbook: cloud initial access](https://red.tymyrddin.dev/docs/in/cloud/playbooks/cloud-entry.html)
- [Pivot from endpoint to cloud](https://red.tymyrddin.dev/docs/in/endpoint/runbooks/pivot-to-cloud.html)
