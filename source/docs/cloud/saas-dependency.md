# SaaS dependency risk

SaaS adoption is one of the quieter security shifts of the last decade. Each individual SaaS tool is a bounded decision.
The cumulative effect of adopting many is a sprawling identity surface where every SaaS account is a credential that can
be phished, every integration is a token that can be stolen, and every vendor is a third-party risk that the
organisation may have visited briefly during procurement and not revisited since.

## The compounding identity surface

A typical mid-sized organisation will, on inventory, find more SaaS accounts than employees. Each account has a
credential, a session, often an OAuth token granting access to other systems, and an admin somewhere who configured the
integration once and moved on. The collective attack surface includes every SaaS, every integration between them, every
API token issued to connect them, and every former employee whose access was supposed to be revoked.

The interesting failures here are rarely a single SaaS being breached. They are the chain: the marketing tool with read
access to the CRM, which has integration tokens for the email platform, which can reach the file-sharing service, which
contains the data the attacker actually wanted. Each link looked harmless when configured. The chain is harder to assess
and harder to monitor than any individual link.

## Living off cloud

The attacker side of this is increasingly visible as "living off cloud". Legitimate cloud and SaaS services are
weaponised both as attack infrastructure and as exfiltration channels. Their traffic patterns match expected baselines.
Their domains are pre-trusted. The controls that block dubious external infrastructure leave the legitimate ones
untouched, because blocking them would break legitimate work.

The defensive challenge is that traffic to Dropbox or Google Drive or a major SaaS is legitimate by default for most
organisations. Detection has to work on patterns within that traffic (volume, timing, the specific accounts involved)
rather than on the destination itself.

## Personal and small-organisation cloud

The same patterns appear at the individual and family level, where the attack surface is narrower but the consequences
are personal rather than abstract. A single Google account compromised is, for many people, equivalent to a complete
digital identity compromise.

## What the dependency map needs to be

The minimum useful artefact for managing SaaS dependency risk is an inventory: which SaaS the organisation uses, who the
admin is, what data lives there, what integrations connect it to other systems, and what the access path for the
attacker would be if a single user account were compromised.

The inventory is rarely complete the first time it is built and rarely maintained without a named owner. An organisation
that has not yet built one is not in a position to assess SaaS risk; an organisation that has built one once and not
updated it is in only marginally better shape.

## Related

- [Identity collapse and the control plane](identity-collapse.md)
- [Cloud-native detection](cloud-detection.md)
- [Multi-cloud trust boundaries](multi-cloud-trust.md)
- [Credential harvesting via legitimate cloud services](https://red.tymyrddin.dev/docs/in/real/credentials/cloud-hosting.html)
- [SaaS and cloud platform harvesting](https://red.tymyrddin.dev/docs/out/collection/runbooks/saas-harvesting.html)
- [Living-off-cloud exfiltration (notes)](https://red.tymyrddin.dev/docs/out/exfiltration/notes/living-off-cloud.html)
- [Living-off-cloud exfiltration (runbook)](https://red.tymyrddin.dev/docs/out/exfiltration/runbooks/living-off-cloud-exfil.html)
- [Cloud sync exfiltration](https://red.tymyrddin.dev/docs/out/exfiltration/runbooks/cloud-sync-exfil.html)
- [Email and cloud security: putting locks on the spice rack](https://blue.tymyrddin.dev/docs/home/cloud/index.html)
- [Encrypt cloud files before uploading](https://blue.tymyrddin.dev/docs/home/cloud/encrypt.html)
