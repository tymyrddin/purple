# Runbook: DNS open recursion and cache poisoning

`city-directory` is a BIND9 recursive resolver that accepts queries from any
source, performs recursion for any caller, and has DNSSEC validation disabled.
An attacker on the internet can use it as a forwarder, an amplification
reflector, and, with an on-path or timing position, a cache poisoning
platform. A poisoned A record for the historian hostname redirects any
DNS-dependent client to an attacker-controlled address, making credential harvest
a passive operation.

- Techniques: 
  - [Trust exploitation and misconfiguration](https://purple.tymyrddin.dev/docs/ctfs/ot-ics/attack-surface#trust-exploitation-and-misconfiguration-abuse)
  - [Credential attacks and authentication abuse](https://purple.tymyrddin.dev/docs/ctfs/ot-ics/attack-surface#credential-attacks-and-authentication-abuse)
  - [Data exfiltration](https://purple.tymyrddin.dev/docs/ctfs/ot-ics/attack-surface#data-exfiltration)
- Challenge type: Network (PCAP) or Realist
- Difficulty: Advanced

## Components to start

```bash
./ctl up
```

Minimal containers: `city-directory`, `unseen-gate`

For the credential harvest stage, also bring up `uupl-historian` as the poisoning
target. To verify that a DMZ client uses this resolver and would receive the poisoned
record, add whichever DMZ component makes DNS queries (e.g. `contractors-gate` or
`sorting-office`).

Entry point: any host with a route to `city-directory` (10.10.5.31:53).
The internet zone has direct access.

## Background

`city-directory` runs BIND9 9.20 with:
- `allow-query { any; }`: resolves for any source
- `allow-recursion { any; }`: recursive resolution for any caller
- `dnssec-validation no`: accepts unsigned and incorrectly-signed DNS responses
- `forwarders { 8.8.8.8; 8.8.4.4; }`: forwards unresolved queries upstream

The combination of open recursion and disabled DNSSEC validation makes this a
workable amplification reflector and a cache poisoning target. The DNSSEC
setting does not make poisoning trivial: modern BIND9 randomises source port
and query ID, but it removes one defence layer and means forged responses with
invalid signatures are accepted.

## Attack path

### Stage 1: enumerate the resolver

```bash
# Version disclosure via CHAOS class query
dig @10.10.5.31 version.bind chaos txt
# "9.20-..." (exact version string)

# Confirm open recursion: resolve an external name from unseen-gate
dig @10.10.5.31 google.com
# Returns A records; the resolver is performing recursion on behalf of any caller

# Confirm DNSSEC is off: query a signed domain and check the AD (authenticated data) flag
dig @10.10.5.31 cloudflare.com +dnssec
# No AD flag: DNSSEC validation not performed
```

### Stage 2: use the resolver for reconnaissance

```bash
# Resolve internal hostnames to map the network
# Internal zones are only answered if the resolver has authority or a cached entry
dig @10.10.5.31 uupl-historian.uupl.am
dig @10.10.5.31 historian.uupl.am

# The resolver forwards to 8.8.8.8 for external names; internal names with no
# zone authority return NXDOMAIN unless a local zone is configured
```

### Stage 3: DNS amplification (DoS vector, educational)

```bash
# Forged UDP query with victim source address: the resolver's larger response
# lands at the victim rather than the attacker
# ANY queries produce the largest responses; most resolvers now limit them

# Illustrative only; confirm amplification factor:
dig @10.10.5.31 google.com ANY +bufsize=4096
# Response size vs query size gives the amplification ratio

# A real amplification attack sends high-volume forged queries
# Do not direct at any host outside the lab
```

### Stage 4: cache poisoning path (requires on-path position)

Cache poisoning against a modern BIND9 instance is harder than against older
implementations. Source-port randomisation and query-ID randomisation (both
present in BIND9 9.20) mean a blind off-path attack requires guessing a 16-bit
query ID and a 16-bit source port simultaneously, effectively 32 bits of
entropy. The `dnssec-validation no` setting removes one layer of protection but
does not make poisoning trivial.

The operationally significant path is on-path: if the attacker can intercept or
substitute the resolver's upstream queries (for example, by being on the same
network segment as the upstream forwarder connection, or by controlling a
nameserver in the resolution path), forged answers are accepted without
signature verification.

```bash
# Step 1: identify a hostname that DMZ clients resolve via this resolver
# The historian is queried by SCADA components: uupl-historian.uupl.am

# Step 2: position to intercept the resolver's upstream UDP query
# (lab-internal: ARP poisoning or network tap on the DMZ uplink)

# Step 3: forge a DNS response matching the query ID and source port
# Tools: dnsspoof, scapy, or a custom forger

# Step 4: poisoned cache now serves attacker-controlled IP for historian hostname

# Verify:
dig @10.10.5.31 uupl-historian.uupl.am
# Returns attacker-controlled IP instead of 10.10.2.10
```

### Stage 5: credential harvest from poisoned historian

```bash
# Once the cache is poisoned, any DMZ client that resolves the historian hostname
# and sends HTTP requests (including authentication headers) reaches the attacker

# Simple listener on attacker-controlled IP:
python3 -m http.server 8080
# Wait for a client to connect and POST with historian credentials

# More realistic: run a minimal Flask app that returns valid historian responses
# while logging every authentication header received
```

## Flag placement

For a Network challenge: the PCAP contains a DNS response with an unusual TTL
or an unexpected answer section. The participant inspects the capture, identifies
the poisoned record, and extracts the flag embedded in the TXT record of a
follow-up query.

For a Realist challenge: after poisoning the cache, the attacker-controlled
historian endpoint logs credentials from the SCADA component. The flag is
embedded in those credentials or returned in the fake historian response.

## DNSSEC and why it is disabled here

DNSSEC validation is the correct mitigation: a signed response with a valid
chain from a trusted root cannot be forged. It is disabled on `city-directory`
because signed domains can have misconfigured signatures that cause resolution
failures, and the operational pressure to "just make it work" during an outage
tends to win. Disabling DNSSEC validation is a one-line config change that is
very easy to make and never quite gets reversed.

Open recursion is equally easy to restrict: `allow-recursion { 10.10.5.0/24; }`
limits recursive resolution to the DMZ subnet. That change has also not
happened.
