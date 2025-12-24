# Turning tree nodes into playbook actions

Each node in the selected chain becomes one or more actions. An action is the operational unit of a playbook. It's 
the thing someone actually *does*. It's what gets typed into a terminal, or clicked in a GUI, or configured in a YAML 
file.

Let's operationalise node 1.1.1.1 from the [BGP hijacking tree](https://red.tymyrddin.dev/docs/in/network/roots/ip/bgp-hijacking): *Announcing a more specific prefix than the legitimate one*.

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

## Recording

### Intent

What routing outcome is being pursued? Not "send a BGP UPDATE" (that's execution). Not "compromise the network" 
(that's goal, not intent). Intent is the middle layer.

For node 1.1.1.1, the intent is: *Cause AS65001's legitimate /24 prefix 203.0.113.0/24 to become less preferred than 
our forged /25 prefix 203.0.113.128/25, specifically in the APAC region, exploiting longest-prefix-match routing 
behaviour, so that traffic destined for 203.0.113.128-255 is routed via our AS64512 instead of the legitimate AS65001*.

Intent answers the question "what are we trying to make the control plane do?" It connects execution (the thing we 
type) to goal (the thing we're ultimately testing). If you can't write down the intent clearly, you don't understand 
the action well enough to include it in a playbook.

### Preconditions

What must already be misconfigured, missing, or ignored for this action to be possible?

For node 1.1.1.1 to work, we need:

Action-level preconditions:

- "Peer AS64512 must not be filtering prefixes from our AS64513 based on IRR data or ROAs" (configuration gap)
- "RPKI validation must be either not deployed in APAC region, or set to 'log only' rather than 'drop invalid'" (common misconfiguration, documented in the tree's mitigation section)
- "No monitoring of unexpected /25 announcements within known /24 allocations from this peer" (defensive gap)
- "Target AS65001 does not have ROA covering /25 subdivisions of their /24" (RPKI configuration gap)

These are specific to executing *this node*. They're different from tree-level preconditions like *attacker has 
BGP peering*, which is assumed for the entire section 1.1 *Prefix hijacking*.

If the precondition doesn't exist, the action won't work. If you can't verify whether the precondition exists, you're 
guessing. Playbooks built on guesses are expensive ways to learn you should have done reconnaissance first.

### Execution method

Configuration change, announcement, withdrawal, or human error? Be specific about *how* this is done.

Not "announce prefix". That's not enough detail.

Instead: "Use [FRRouting](https://frrouting.org/) 8.4 on Ubuntu 22.04 LTS host to announce prefix 
203.0.113.128/25 via existing eBGP session with AS64512. Configuration changes:

```
router bgp 64513
 address-family ipv4 unicast
  network 203.0.113.128/25
 exit-address-family
!
```

Apply with `vtysh -c "clear ip bgp * soft out"` to trigger re-advertisement without dropping session. Expected 
announcement propagation: 30-90 seconds to reach AS64512's route reflectors, additional 60-180 seconds for broader 
internet propagation".

The execution detail includes:

- Tool selection (FRRouting, because it's open source and well-documented)
- Version numbers (matters for compatibility and bug reproduction)
- Platform (matters because BGP implementations vary)
- Exact configuration syntax (so someone can execute without guessing)
- Verification command (how to check it worked)
- Timing expectations (so you know whether to wait or investigate)

This level of detail means someone who knows BGP but hasn't read the attack tree can execute the action. It also 
means when something goes wrong (and it will), you have enough information to debug.

### Expected technical effect

On BGP control plane behaviour. What should change in routing tables, reachability, path selection?

For node 1.1.1.1, the expected technical effect is:

"Within 3-5 minutes of announcement:

- AS64512's routing table should show two entries: 203.0.113.0/24 via AS65001 (unchanged), and 203.0.113.128/25 via our AS64513 (new)
- Routers in APAC region choosing path via AS64512 should prefer the /25 due to longest-prefix-match, regardless of AS path length
- Traffic from APAC test hosts (198.51.100.10, 198.51.100.20) to 203.0.113.150 should route via our AS64513
- Traffic from APAC to 203.0.113.10 (outside the /25) should continue routing via legitimate AS65001
- Global routing table outside APAC may or may not see our /25, depending on AS64512's export policies to other peers"

This is your success criterion at the technical layer. If this effect doesn't occur, either the action failed, [or 
your understanding of the control plane was wrong](../spark/control-vs-data-plane.md). Either way, the playbook stops 
here and you investigate before proceeding.

### Expected observational footprint

What might appear in logs, metrics, or alerts? This is defensive perspective. What would a defender see if they were 
looking?

For node 1.1.1.1, the observable footprint:

"`BGP UPDATE` message visible in:

- AS64512's BGP logs showing new prefix 203.0.113.128/25 from AS64513
- AS64512's route reflector logs showing propagation of /25 to internal peers
- Public [BGP collectors](https://www.bgpmon.net/) (RouteViews, RIPE RIS) *may* see announcement if AS64512 exports to their peers; this is not guaranteed
- NetFlow data on AS64512's peering interface should show traffic volume to 203.0.113.128/25 shifting from AS65001 path to AS64513 path

RPKI footprint:

- If AS65001 has RPKI monitoring, they *may* see RPKI INVALID alert for our announcement (if they're subscribed to [RIPE's RPKI Validator](https://www.ripe.net/manage-ips-and-asns/resource-management/certification/tools-and-resources))
- No ROA change footprint because we're not creating new ROAs, just announcing without proper authorisation

Detection likelihood:

- High if AS65001 monitors BGP for unexpected announcements of their space
- Medium if AS64512 monitors for ROA mismatches
- Low if relying only on passive BGP monitoring (most operators aren't watching for /25 announcements within their /24s)
- Very low if no BGP-specific monitoring exists"

Be honest about absence of observability. If the action is realistically undetectable with current monitoring, say so. 
That's valuable information. It tells defenders where their gaps are.

Node 1.6.1.1 *Short-lived hijacks* from the evasion section specifically tries to exploit this gap. Most BGP 
monitoring has 5-15 minute polling intervals. If you announce for 2 minutes and withdraw, you might evade detection. 
But that requires reliable timing control you probably don't have.

If an action cannot be expressed this way, it stays in the tree. It doesn't become a playbook action. It remains 
theoretical until someone figures out how to make it operational.

## Not

Nodes that fail the operational criteria and why:

| Section                       | Node ID(s)                   | Why It Should Be Excluded (The "Action" is Not Executable)                                                                                                                                 |
|:------------------------------|:-----------------------------|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 1.5 Attack objectives         | All (e.g., 1.5.1.1, 1.5.2.1) | These describe goals (e.g., "Man-in-the-middle", "Denial of service"), not executable actions or intents. They are the *outcome* of successful lower-level actions.                        |
| 1.6 Evasion techniques        | All (e.g., 1.6.1.1, 1.6.3.1) | These describe strategies or conditions (e.g., "Short-lived hijacks", "Operating in weak jurisdictions"), not discrete, scriptable steps.                                                  |
| 1.8 Infrastructure abuse      | 1.8.1.1, 1.8.2.1, 1.8.3.1    | These are conceptual categories (e.g., "Cloud provider exploitation", "IXP manipulation"). You cannot execute "IXP manipulation" without breaking it down into specific, concrete actions. |
| 1.4 Exploitation methods      | 1.4.3.1, 1.4.3.2, 1.4.3.3    | These rely on social engineering ("Manipulating network operators"). These are psychological, non-scriptable actions with unpredictable outcomes.                                          |
| 1.3 Sophisticated techniques  | 1.3.1.3, 1.3.2.2, 1.3.3.3    | These are high-level concepts (e.g., "Chronologically coordinated attacks", "Stealthy path manipulation") that require complex planning and multiple underlying actions.                   |
| 1.4.1 Rogue AS attacks        | 1.4.1.3                      | "Social engineering to obtain AS resources" is, again, a non-scriptable social attack.                                                                                                     |
| 1.6.2 Attribution obfuscation | 1.6.2.3                      | "Cross-border routing" is a characteristic of a path, not an action you can directly perform.                                                                                              |

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
            
        1.3.2 Targeted hijacking
            1.3.2.1 Focusing on specific countries or organisations
            1.3.2.3 Attacks against financial or government networks
            
        1.3.3 Advanced persistence
            1.3.3.1 Long-term hijacking for espionage
            1.3.3.2 Low-volume route manipulation
            
    1.4 Exploitation methods [OR]
    
        1.4.1 Rogue AS attacks
            1.4.1.2 Compromising existing AS infrastructure
            
        1.4.2 Compromised routers
            1.4.2.1 Taking control of BGP routers
            1.4.2.2 Manipulating routing tables directly
            1.4.2.3 Exploiting router vulnerabilities
            
    1.5 Attack objectives [OR]
    
        1.5.1 Traffic interception
            1.5.1.2 Eavesdropping on communications
            1.5.1.3 SSL/TLS interception
            
        1.5.2 Denial of service
            1.5.2.2 Routing loops
            1.5.2.3 Path inflation
            
    1.6 Evasion techniques [OR]
    
        1.6.1 Detection avoidance
            1.6.1.2 Low-volume route leaks
            1.6.1.3 Mimicking legitimate announcements
            
        1.6.2 Attribution obfuscation
            1.6.2.1 Using compromised infrastructure
            1.6.2.2 Through multiple AS paths
            
        1.6.3 Legal avoidance
            1.6.3.2 Using bulletproof hosting providers
            1.6.3.3 Exploiting legal grey areas
            
    1.8 Infrastructure abuse [OR]
    
        1.8.1 Cloud provider exploitation
            1.8.1.2 Manipulating cloud routing policies
            1.8.1.3 Exploiting multi-cloud connectivity
            
        1.8.2 IXP manipulation
            1.8.2.2 Route server manipulation
            1.8.2.3 Peering fabric exploitation
            
        1.8.3 Cable system targeting
            1.8.3.2 Terrestrial fibre path influencing
            1.8.3.3 Cross-continental path manipulation
```

## Evaluation criteria

When evaluating any node, ask these questions derived from your text to see if it's playbook-ready:

- Intent: Can you write a precise sentence about what you're trying to make the BGP control plane do?
- Execution: Can you write the exact command (e.g., vtysh), configuration snippet, or GUI click needed to perform it?
- Technical effect: Can you predict the specific change in a routing table or traffic flow that will result?
- Observable footprint: Can you list the specific log entries or monitoring alerts it would generate?

If you can answer "yes" to all four for a node, it's a strong candidate. If any answer is "no" or is vague, the node should be excluded for now.

I hope this systematic breakdown helps you focus your playbook development efforts on the most actionable parts of the tree. Would you like to try applying this framework to one of the candidate nodes, like 1.1.1.2 Exploiting longest prefix match?
