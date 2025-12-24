# Selecting an attack chain worth operationalising

Not every branch of an attack tree deserves to become a playbook. Some branches are theoretical exercises. Some are 
"yes this is technically possible but nobody has that much patience and free time". Some require the kind of access 
that if you already had it, you wouldn't need to run the attack anyway.

## Selecting

Look at the [complete BGP hijacking tree](https://red.tymyrddin.dev/docs/in/network/roots/ip/bgp-hijacking). 


```
1. BGP hijacking & route leaks [OR]

    1.1 Prefix hijacking [OR]
    
        1.1.1 Sub-prefix hijacking
            1.1.1.1 Announcing a more specific prefix than the legitimate one
            1.1.1.2 Exploiting longest prefix match to attract traffic
            1.1.1.3 Using forged origin AS to inject false routes
            
        1.1.2 Exact-prefix hijacking
            1.1.2.1 Announcing someone else's exact prefix without authorisation
            1.1.2.2 Using a forged origin AS to hijack traffic
            1.1.2.3 Exploiting lack of route validation
            
        1.1.3 Squatting attacks
            1.1.3.1 Announcing unallocated or unused ip space
            1.1.3.2 Using ip addresses that are not officially assigned
            1.1.3.3 Creating fake resources in unallocated space
            
    1.2 Path manipulation [OR]
    
        1.2.1 AS path forgery
            1.2.1.1 Shortening AS path to make route more attractive
            1.2.1.2 Using fake AS numbers in path announcements
            1.2.1.3 Manipulating path attributes to influence route selection
            
        1.2.2 Route leaking
            1.2.2.1 Violating export policies to announce routes to unauthorised peers
            1.2.2.2 Accidental or malicious redistribution of routes
            1.2.2.3 Transit leakage to non-transit peers
            
        1.2.3 Blackholing
            1.2.3.1 Announcing routes to discard traffic (for DoS)
            1.2.3.2 Using blackhole communities maliciously
            1.2.3.3 Redirecting traffic to null interfaces
            
    1.3 Sophisticated techniques [OR]
    
        1.3.1 Time-based attacks
            1.3.1.1 Short-duration hijacks to avoid detection
            1.3.1.2 Pulse hijacking for selective interception
            1.3.1.3 Chronologically coordinated attacks
            
        1.3.2 Targeted hijacking
            1.3.2.1 Focusing on specific countries or organisations
            1.3.2.2 Hijacking critical infrastructure prefixes
            1.3.2.3 Attacks against financial or government networks
            
        1.3.3 Advanced persistence
            1.3.3.1 Long-term hijacking for espionage
            1.3.3.2 Low-volume route manipulation
            1.3.3.3 Stealthy path manipulation
            
    1.4 Exploitation methods [OR]
    
        1.4.1 Rogue AS attacks
            1.4.1.1 Creating fake autonomous systems
            1.4.1.2 Compromising existing AS infrastructure
            1.4.1.3 Social engineering to obtain AS resources
            
        1.4.2 Compromised routers
            1.4.2.1 Taking control of BGP routers
            1.4.2.2 Manipulating routing tables directly
            1.4.2.3 Exploiting router vulnerabilities
            
        1.4.3 Social engineering
            1.4.3.1 Manipulating network operators
            1.4.3.2 Social engineering to change routing policies
            1.4.3.3 Impersonating legitimate network administrators
            
    1.5 Attack objectives [OR]
    
        1.5.1 Traffic interception
            1.5.1.1 Man-in-the-middle attacks
            1.5.1.2 Eavesdropping on communications
            1.5.1.3 SSL/TLS interception
            
        1.5.2 Denial of service
            1.5.2.1 Blackholing traffic
            1.5.2.2 Routing loops
            1.5.2.3 Path inflation
            
        1.5.3 Financial gain
            1.5.3.1 Cryptocurrency exchange targeting
            1.5.3.2 Ad revenue manipulation
            1.5.3.3 Competitive advantage
            
    1.6 Evasion techniques [OR]
    
        1.6.1 Detection avoidance
            1.6.1.1 Short-lived hijacks
            1.6.1.2 Low-volume route leaks
            1.6.1.3 Mimicking legitimate announcements
            
        1.6.2 Attribution obfuscation
            1.6.2.1 Using compromised infrastructure
            1.6.2.2 Through multiple AS paths
            1.6.2.3 Cross-border routing
            
        1.6.3 Legal avoidance
            1.6.3.1 Operating in jurisdictions with weak enforcement
            1.6.3.2 Using bulletproof hosting providers
            1.6.3.3 Exploiting legal grey areas
            
    1.7 Coordination mechanisms [OR]
    
        1.7.1 State-sponsored attacks
            1.7.1.1 Nation-state level hijacking
            1.7.1.2 Intelligence gathering operations
            1.7.1.3 Geopolitical targeting
            
        1.7.2 Criminal syndicates
            1.7.2.1 Organised crime involvement
            1.7.2.2 Ransom-based attacks
            1.7.2.3 Large-scale financial attacks
            
        1.7.3 Insider threats
            1.7.3.1 Malicious network administrators
            1.7.3.2 Compromised employees
            1.7.3.3 Third-party vendor risks
            
    1.8 Infrastructure abuse [OR]
    
        1.8.1 Cloud provider exploitation
            1.8.1.1 Abusing cloud peering relationships
            1.8.1.2 Manipulating cloud routing policies
            1.8.1.3 Exploiting multi-cloud connectivity
            
        1.8.2 IXP manipulation
            1.8.2.1 Internet exchange point attacks
            1.8.2.2 Route server manipulation
            1.8.2.3 Peering fabric exploitation
            
        1.8.3 Cable system targeting
            1.8.3.1 Submarine cable route manipulation
            1.8.3.2 Terrestrial fibre path influencing
            1.8.3.3 Cross-continental path manipulation
```

It has eight major branches and dozens of sub-branches. Most of them will never become playbooks because they're either 
too difficult, too detectable, or require preconditions that don't exist in real networks.

The process of selecting which branch to operationalise is an exercise in applied pessimism. You're not looking for 
the cleverest attack. You're looking for the attack that *might actually work* given how things are actually 
configured, maintained, and defended.

Document, explicitly, for anyone who has to review or execute this playbook later:

### Which branch is selected

Write it down. Draw it. Screenshot the relevant bit of the attack tree and include it in the playbook. Future you, 
reading this at 2 at night when things have gone wrong, needs to know exactly which path through the tree you thought 
was worth pursuing.

Not "we're doing a BGP hijack". Be specific. *We're implementing node 1.1.1 from the BGP hijacking tree: sub-prefix 
hijacking via node 1.1.1.1 'announcing a more specific prefix', specifically targeting the lack of prefix filtering 
on peer AS64512's session combined with the absence of RPKI validation in the APAC region, by announcing 
203.0.113.128/25 that falls within the /24 legitimately originated by AS65001*.

Include the full path from root to leaf: 1 → 1.1 → 1.1.1 → 1.1.1.1. Make it unambiguous which attack variant you are 
testing.

### Why this branch is realistic in real networks

This is where you defend your selection against the critique of "yes but would anyone actually be that stupid?" The 
answer is usually "yes, because it was set up in 2008 and everyone who knew how it worked has left".

For sub-prefix hijacking (node 1.1.1), the realistic conditions include:

- RPKI deployment remains under 40% globally (as of 2024)
- Many networks that have deployed RPKI are only logging invalid routes, not dropping them
- Prefix filtering on peering sessions is inconsistent; many peers only filter obvious bogons
- Longest-prefix-match is fundamental to IP routing and cannot be disabled

These are not failures of individual organisations. These are structural realities of internet routing in 2025. 
Document them. When your test succeeds or fails, you need to know whether it succeeded because your technique was 
good or because the conditions were unusually favourable.

### Which branches are excluded and why

This is possibly more important than documenting what you *did* select. It answers the question "why didn't you do 
the obviously better attack over here?"

Looking at the hijacking tree, here are branches we're explicitly *not* operationalising and why:

*Node 1.1.3 "Squatting attacks"* (excluded)

Reason: Requires announcing unallocated IP space. Most modern networks have basic bogon filters that catch obviously unallocated space. Regional Internet Registries maintain updated bogon lists. Whilst gaps exist, this attack is more easily detected than sub-prefix hijacking of legitimately allocated space.

*Node 1.3.1.1 "Short-duration hijacks to avoid detection"* (excluded)

Reason: Requires extremely precise timing control over BGP convergence, which we don't have when depending on third-party peering relationships. BGP propagation is too variable (30-180 seconds typical) to reliably execute "short-duration" hijacks that last minutes rather than hours. Too likely to either fail to establish routes before we withdraw them, or succeed but cause visible route flapping that attracts attention.

*Node 1.4.1.1 "Creating fake autonomous systems"* (excluded)

Reason: Requires obtaining AS number allocation from RIR, which involves paperwork, justification, and a money trail. Even if we could get an AS number, using it in an attack creates obvious attribution. We're testing detection capabilities, not setting up persistent infrastructure for future operations.

*Node 1.5.3 "Financial gain" objectives* (excluded)

Reason: This is a security test, not actual criminal activity. Any branches that end in "cryptocurrency exchange targeting", "ad revenue manipulation", or "competitive advantage" are excluded by scope. We're testing whether hijacking *could* be done, not executing financially motivated attacks.

*Section 1.7 "Coordination mechanisms"* (entire branch excluded)

Reason: Nodes 1.7.1 *State-sponsored attacks*, 1.7.2 *Criminal syndicates*, and 1.7.3 *Insider threats* describe 
attacker *categories*, not attack *techniques*. These aren't branches you operationalise; they're context about 
who might execute the techniques described in other branches. Irrelevant for our playbook.

Resulting tree:

```
1. BGP hijacking & route leaks [OR]

    1.1 Prefix hijacking [OR]
    
        1.1.1 Sub-prefix hijacking
            1.1.1.1 Announcing a more specific prefix than the legitimate one
            1.1.1.2 Exploiting longest prefix match to attract traffic
            1.1.1.3 Using forged origin AS to inject false routes
            
        1.1.2 Exact-prefix hijacking
            1.1.2.1 Announcing someone else's exact prefix without authorisation
            1.1.2.2 Using a forged origin AS to hijack traffic
            1.1.2.3 Exploiting lack of route validation
            
    1.2 Path manipulation [OR]
    
        1.2.1 AS path forgery
            1.2.1.1 Shortening AS path to make route more attractive
            1.2.1.2 Using fake AS numbers in path announcements
            1.2.1.3 Manipulating path attributes to influence route selection
            
        1.2.2 Route leaking
            1.2.2.1 Violating export policies to announce routes to unauthorised peers
            1.2.2.2 Accidental or malicious redistribution of routes
            1.2.2.3 Transit leakage to non-transit peers
            
        1.2.3 Blackholing
            1.2.3.1 Announcing routes to discard traffic (for DoS)
            1.2.3.2 Using blackhole communities maliciously
            1.2.3.3 Redirecting traffic to null interfaces
            
    1.3 Sophisticated techniques [OR]
    
        1.3.1 Time-based attacks
            1.3.1.2 Pulse hijacking for selective interception
            1.3.1.3 Chronologically coordinated attacks
            
        1.3.2 Targeted hijacking
            1.3.2.1 Focusing on specific countries or organisations
            1.3.2.2 Hijacking critical infrastructure prefixes
            1.3.2.3 Attacks against financial or government networks
            
        1.3.3 Advanced persistence
            1.3.3.1 Long-term hijacking for espionage
            1.3.3.2 Low-volume route manipulation
            1.3.3.3 Stealthy path manipulation
            
    1.4 Exploitation methods [OR]
    
        1.4.1 Rogue AS attacks
            1.4.1.2 Compromising existing AS infrastructure
            1.4.1.3 Social engineering to obtain AS resources
            
        1.4.2 Compromised routers
            1.4.2.1 Taking control of BGP routers
            1.4.2.2 Manipulating routing tables directly
            1.4.2.3 Exploiting router vulnerabilities
            
        1.4.3 Social engineering
            1.4.3.1 Manipulating network operators
            1.4.3.2 Social engineering to change routing policies
            1.4.3.3 Impersonating legitimate network administrators
            
    1.5 Attack objectives [OR]
    
        1.5.1 Traffic interception
            1.5.1.1 Man-in-the-middle attacks
            1.5.1.2 Eavesdropping on communications
            1.5.1.3 SSL/TLS interception
            
        1.5.2 Denial of service
            1.5.2.1 Blackholing traffic
            1.5.2.2 Routing loops
            1.5.2.3 Path inflation
            
    1.6 Evasion techniques [OR]
    
        1.6.1 Detection avoidance
            1.6.1.1 Short-lived hijacks
            1.6.1.2 Low-volume route leaks
            1.6.1.3 Mimicking legitimate announcements
            
        1.6.2 Attribution obfuscation
            1.6.2.1 Using compromised infrastructure
            1.6.2.2 Through multiple AS paths
            1.6.2.3 Cross-border routing
            
        1.6.3 Legal avoidance
            1.6.3.1 Operating in jurisdictions with weak enforcement
            1.6.3.2 Using bulletproof hosting providers
            1.6.3.3 Exploiting legal grey areas
            
    1.8 Infrastructure abuse [OR]
    
        1.8.1 Cloud provider exploitation
            1.8.1.1 Abusing cloud peering relationships
            1.8.1.2 Manipulating cloud routing policies
            1.8.1.3 Exploiting multi-cloud connectivity
            
        1.8.2 IXP manipulation
            1.8.2.1 Internet exchange point attacks
            1.8.2.2 Route server manipulation
            1.8.2.3 Peering fabric exploitation
            
        1.8.3 Cable system targeting
            1.8.3.1 Submarine cable route manipulation
            1.8.3.2 Terrestrial fibre path influencing
            1.8.3.3 Cross-continental path manipulation
```

Acceptable reasons for excluding branches include:

- Requires universal RPKI deployment. If your attack relies on everyone having done their homework, you're depending on a miracle. RPKI deployment is growing, but it's not universal, it's not uniform, and it's definitely not universally configured correctly. Any attack path that requires attackers to navigate working RPKI infrastructure everywhere is currently easier to avoid than to execute. This might change. When it does, update your playbooks.
- Assumes competent change management. Some attack branches can be defeated by proper change management processes. The existence of those processes in a policy document does not mean they exist in practice. However, if your test environment *does* have working change management (because you're testing in a mature organisation that takes this seriously), then attack paths that rely on change management being absent are not realistic *for your context*. Exclude them. Test what's actually bypassable in the environment you're actually testing.
- Depends on people reading alerts on a Friday. Or reading them at all. Or having alert fatigue low enough that they distinguish between "this is the usual noise" and "this is the actual incident we've been planning for". Attack paths that are technically defeated by alerting, but where the alerts are realistically going to be ignored, dismissed, or drowned out by normal operational noise, are fair game. Attack paths that depend on alerts *definitely* being noticed and acted on within a tight timeframe are optimistic.
- Requires access you wouldn't have in a realistic scenario. Node 1.4.2.1 *Taking control of BGP routers* starts with *attacker has compromised router*. If that's your starting point, you need to justify why an attacker would have that. If the answer is "social engineering", document the social engineering path. If the answer is "we're assuming they compromised something else first", document what that something else was and what level of access it provides. If the answer is "we gave them access because this is a test", mark the playbook clearly as requiring elevated initial access and note that the value is in testing detection and response, not in validating the attack path itself.

Lantern does not simulate miracles. It simulates the sort of things that might actually happen in networks configured by humans, defended by tired humans, and operated by humans who have thirty other things to deal with today.