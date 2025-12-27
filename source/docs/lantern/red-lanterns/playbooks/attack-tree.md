# What an attack tree is allowed to be

An attack tree is structural, not operational. It exists in the comfortable world of pure logic, where things 
either work or they don't, gates either open or stay closed, and time is merely a dimension I/you/we draw an arrow along.

Take the [BGP hijacking and route leaks attack tree](https://red.tymyrddin.dev/docs/in/network/roots/ip/bgp-hijacking):

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

It's comprehensive. It has branches for sub-prefix hijacking, exact-prefix hijacking, squatting attacks, path 
manipulation, and several dozen other variations. Each node connects logically to its children. The structure is clean.

## Yes

### Preconditions

"Attacker must have BGP peering session" is a precondition. It tells you what state the world needs to be in before 
this branch becomes relevant. It does not tell you how long it took to get that peering session, how many emails were 
exchanged, or whether it was approved by someone who thought BGP was a new type of sandwich.

Looking at node 1.1.1.1 in the hijacking tree: *Announcing a more specific prefix than the legitimate one* has an 
implicit precondition that the attacker has the ability to announce *any* prefix. The tree doesn't specify whether 
that means having legitimate BGP peering, having compromised a router (node 1.4.2), or having social-engineered a 
network operator (node 1.4.3). Those are different attack paths with wildly different execution complexities, 
but the tree treats them as equivalent.

### Dependencies

*This attack requires RPKI validation to be disabled*, is a dependency. It connects one node to another with a 
nice clean line. It does not mention that RPKI validation was disabled three years ago during a migration and 
nobody quite got round to turning it back on, or that it's disabled because the monitoring system couldn't 
parse the logs properly and kept paging people at 3 at night.

Node 1.1.2.3 *Exploiting lack of route validation* depends on RPKI either not being deployed or not being enforced. 
Globally, RPKI deployment is under 40%. That's a dependency you can often count on, but the tree doesn't tell you 
*which* regions or networks have deployment, or whether they're enforcing rejection of invalid routes or just 
logging them.

### Optional paths

"Attacker may choose to announce `/24` OR `/25` prefix" presents options. Both might work. The tree doesn't care 
which you pick. It's democracy for attackers. The tree won't mention that the `/25` option only works on Tuesdays 
when the upstream provider's traffic engineering kicks in, or that the `/24` option requires announcing from an `AS` 
number that looks legitimate enough that nobody checks it.

Node 1.3.1.1 *Short-duration hijacks to avoid detection* and 1.3.1.2 *Pulse hijacking for selective interception* are 
optional variations on the same basic hijacking technique. The tree shows both. It doesn't tell you that 
short-duration hijacks are harder to execute reliably because BGP convergence is slow and unpredictable, or that 
pulse hijacking requires very precise timing that's difficult to achieve when you're depending on peering 
relationships you don't control.

### Defender choke points

*Detection possible via RPKI ROA mismatch alert* identifies where defenders *could* notice something. The tree 
helpfully marks this with a red circle or an exclamation point. It does not estimate the probability that the alert 
is going to an inbox that hasn't been checked since 2019, or that the alert will arrive during a planned maintenance 
window when everyone assumes everything is broken anyway.

The hijacking tree mentions monitoring and alerting as mitigation. What it doesn't say is that BGP monitoring 
services like [BGPmon](https://www.bgpmon.net/), [Cloudflare Radar](https://radar.cloudflare.com/), or 
[RIPE Stat](https://stat.ripe.net/) exist and are excellent, but they require someone to actually look at them 
and recognise that an announcement is suspicious. That's a human bottleneck, not a technical one.

## No

### Timing

How long does it take for a `BGP UPDATE` to propagate? The tree might say "propagation occurs". The universe says 
"anything from 30 seconds to 'never because someone's got a static route that takes precedence and nobody remembers 
why'". The tree shows you a path. It doesn't show you the queue.

Node 1.1.1.2 *Exploiting longest prefix match to attract traffic* makes it sound instant. Announce the `/25`, 
traffic arrives. In reality: announcement takes 5-30 seconds to reach the first peer, 30-180 seconds to propagate 
across most of the visible internet, additional time for routers to recompute best paths, more time for existing 
connections to timeout and new ones to follow the new path. You might get some traffic immediately. You might get 
none for five minutes. The tree offers no guidance.

### Human hesitation

The tree shows an attacker announcing a prefix. It does not show the attacker staring at the terminal for five 
minutes thinking "is this definitely the test environment?" It doesn't model the moment where someone decides to 
wait until after lunch just to be safe, or the point where they realise they forgot to open the change ticket and 
now they need to decide whether to abort or plough ahead.

Node 1.4.3.2 *Social engineering to change routing policies* involves humans making decisions. Humans hesitate. 
They ask questions. They defer to others. They want written confirmation. The tree treats this as a single node 
with no indication that it might take days or weeks of patient social engineering to execute.

### Partial failures

In attack trees, things either work (tick) or fail (cross). In reality, things work *partially*. The BGP 
announcement propagates to 60% of the intended peers. The RPKI validation catches it, but only in one of three 
regions. The monitoring alert fires, but the email gets caught in a spam filter. The tree has no notation for 
"it worked, but only sort of, and now everything is in a weird quantum state where the attack is both succeeding 
and failing simultaneously".

Node 1.2.2.1 *Violating export policies to announce routes to unauthorised peers* might work perfectly on some 
peers and fail completely on others, depending on their individual filter configurations. You might successfully 
hijack traffic from APAC whilst simultaneously failing to affect EMEA. There is no space for partial success in the 
tree.

### Budget driven shortcuts

The tree assumes competent implementation. The world delivers whatever could be built with the budget available 
after the sales team promised features nobody actually wanted and finance approved a third of what engineering 
asked for. The tree says *deploy monitoring*. The implementation says "we've got a cron job that greps the 
logs every six hours and emails the output to a distribution list that includes two people who left the company 
in 2021".

The entire section 1.6 *Evasion techniques* assumes defenders have deployed detection systems worth evading. 
Many networks have no BGP-specific monitoring at all. The evasion section of the tree is aspirational. For in the far, 
far future. If ever.

Those elements belong elsewhere. Specifically, they belong in playbooks, after someone has taken the tree seriously 
enough to ask "but what would this actually *look* like?"
