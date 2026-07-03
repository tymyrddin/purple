# Metadata service abuse

The instance metadata service is the most consistently exploited piece of cloud infrastructure that is not technically a
security boundary. It exists to provide running workloads with the information they need to operate (instance identity,
attached IAM credentials, network configuration), and it is reachable from inside the workload by a fixed, well-known IP
address. That makes it [discoverable](attack-surface.md) to anyone who has compromised the workload.

## The credential exposure pattern

The pattern is straightforward. An attacker who reaches a workload, through a server-side request forgery, a remote code
execution, or a misconfigured proxy that forwards arbitrary requests, can request the metadata service and receive
temporary credentials valid for the [workload's IAM role](identity-collapse.md). Those credentials open whatever the role permits, which is
frequently more than the workload actually uses. The API calls that follow are what [cloud detection](cloud-detection.md) is left to catch.

The pattern is well-documented offensively because it is straightforward to exploit and consistently rewarding.
ICMP-based variants exist alongside the more common HTTP-based form.

## Mitigations and their gaps

The mitigations are well-understood and inconsistently implemented.

The newer metadata service versions require session tokens that mitigate the basic SSRF pattern. Where the application
stack supports the upgrade, this closes the most common variant. Where it does not, the legacy interface remains
exposed.

Network-level controls can block access to the metadata IP from contexts that have no operational reason to reach it,
including container sidecars, web request handlers that never need to call the metadata service, and proxies whose role
does not include forwarding internal IP traffic.

Least-privilege IAM roles limit what the credentials can do once exposed. A workload with a role scoped to its own
bucket and its own queue produces a smaller blowup than a workload with a role scoped to the whole account.

## Adjacent network-layer attacks

The metadata service is not the only piece of cloud network particulars that has produced abuse patterns.
Middlebox-specific attacks exploit the cloud provider's deviations from standard internet routing. BGP- and CDN-level
attacks reach further still, into the network underpinning of cloud providers themselves, where the routing
infrastructure that connects cloud data centres to the rest of the internet becomes the attack surface.

## Network-layer variants

- [Cloud metadata service abuse via ICMP](https://red.tymyrddin.dev/docs/in/network/roots/icmp/cloud-metadata-service-abuse.html)
- [Cloud and middlebox-specific attacks](https://red.tymyrddin.dev/docs/in/network/roots/tcp/cloud-middlebox-attacks.html)
- [BGP and CDN/cloud infrastructure attacks](https://red.tymyrddin.dev/docs/in/network/roots/bgp/bgp-cdn-cloud-infrastructure-attacks)
