# Recording mess honestly

Playbooks are not PR documents. They're not trying to make the attack look elegant. They're trying to make the 
attack *repeatable* and the test results *meaningful*.

This means recording the mess honestly.

## What?

### Manual steps

Document them. All of them. Including the boring ones.

Looking at node 1.4.3.2 *Social engineering to change routing policies* (it has already been removed as 
non-operationable) from the [hijacking tree](https://red.tymyrddin.dev/docs/in/network/roots/ip/bgp-hijacking), this 
node is also almost entirely manual steps disguised as a single tree node.

"Manually verify BGP session state before proceeding" is a manual step. It might take 30 seconds. It might take 10 
minutes if the session is flapping. It requires human judgment about whether "Established" means "actually working" 
or "technically up but not passing traffic because of some other problem".

"Check with operations team that maintenance window is still valid" is a manual step. It requires talking to humans. 
Humans might be in meetings. Or on leave. Or assuming that someone else confirmed it.

"Wait for RPKI propagation to complete before testing validation" is a manual step disguised as a waiting period. 
Someone has to decide when "complete" has happened. They decide by checking multiple validators 
([Routinator](https://www.nlnetlabs.nl/projects/rpki/routinator/), [FORT](https://github.com/NICMx/FORT-validator), 
[rpki-client](https://www.rpki-client.org/)), comparing propagation across regions, and making a judgment call 
about whether the differences matter.

Manual steps make playbooks slower. They make them harder to automate. They also make them *work*. Automated 
playbooks that skip manual verification steps either fail messily or succeed in causing actual incidents. 
Neither is ideal.

### Timing uncertainty

BGP propagation is not instant. It's also not consistently slow. It's inconsistently variable, depending on route 
reflector topology, update pacing timers, session state, and whether someone's doing maintenance somewhere 
between you and the target.

Node 1.1.1.2 from the hijacking tree says *Exploiting longest prefix match to attract traffic*. It doesn't mention 
that "attract traffic" might take:

- 30 seconds (if you're lucky and all BGP sessions converge quickly)
- 5 minutes (typical case with some route flapping)
- 20 minutes (if there's a route reflector somewhere with a misconfigured timer)
- Never (if there's a more-specific static route someone added years ago and forgot about)

RPKI propagation is even worse. Repositories update on different schedules. Validators poll at different intervals. 
Routers poll validators at different intervals. The entire chain might take 15 minutes, or 45 minutes, or "whenever 
that one validator finally crashes and restarts because it's been running for 18 months and nobody wanted to be the 
one who turned it off and on again".

Change management approval might take 10 minutes during business hours in an organisation with streamlined processes. 
It might take three days if the request lands on a Friday before a long weekend. It might take "never" if the request 
looks slightly weird and nobody wants to approve it without asking questions first.

Document the uncertainty. Put ranges on timing expectations. Make it clear which delays are expected (propagation), 
which are variable (human approval), and which indicate something has gone wrong (connection timeout).

### Reliance on third party behaviour

Real networks involve third parties. Upstream providers. Peers. Transit providers. Route server operators. RPKI 
repository publishers. They're all third parties, and none of them are under your control.

Node 1.2.2.1 *Violating export policies to announce routes to unauthorised peers* explicitly depends on third-party 
routing policy. If your attack relies on a peer accepting and propagating your announcement, you're relying on 
their BGP configuration not filtering you out. You probably checked this during reconnaissance. You probably 
verified it's currently configured that way. You don't *know* that it will still be configured that way when 
you execute, because configurations change.

Node 1.8.2 *IXP manipulation* depends entirely on Internet Exchange Point policies and the behaviour of other 
members. You don't control the [route server](https://www.euro-ix.net/en/forixps/route-server/), you don't 
control peering fabric policies, and you definitely don't control whether other IXP members have implemented 
proper filtering.

If your attack relies on RPKI validation being deployed but not enforced (a common state for networks 
transitioning to RPKI), you're relying on validators being in "log only" mode. That's the default configuration 
for many deployments. It's also the configuration that cautious operators change to "drop invalid" once 
they're confident their ROAs are correct. You don't control when that happens.

If your attack relies on traffic patterns making certain routes preferred, you're relying on traffic engineering 
policies you didn't set and can't modify. Those policies might change because of traffic shifts, maintenance, or 
someone optimising costs by moving traffic to cheaper transit.

Document which third parties you're depending on and what you're depending them to do (or not do). When the playbook 
fails or succeeds unexpectedly, this list is the first place to look for explanations.

### Places where best practice lost to budget reality

This is perhaps the most important mess to record honestly.

Best practice says (from the hijacking tree's mitigation section): deploy RPKI validation, enforce invalid rejection, 
filter customer prefixes, monitor for unexpected announcements, require peer review for BGP changes, maintain 
documentation of prefix ownership, test regularly.

Budget reality says: we deployed RPKI validation in two of five regions because that's what we could afford. We're 
not enforcing rejection yet because we don't trust our ROA coverage. We filter some customer prefixes based on a 
spreadsheet someone maintains when they remember. We have monitoring but it's noisy so people ignore it. Peer 
review requires booking someone's time and everyone's busy. Documentation is stored in a wiki that might be current. 
Testing is aspirational.

The gap between best practice and budget reality is not a failure of operations teams. It's a consequence of finite 
resources, competing priorities, and organisations making rational decisions about acceptable risk given available 
budget.

Playbooks that assume best practice will discover that many attacks from the tree are theoretically impossible. 
Playbooks that assume budget reality will discover which attacks are actually concerning.

Record where your test environment differs from best practice. Record why (usually: budget, time, complexity, or 
"it's on the roadmap"). Record what controls *are* in place, even if they're not the gold-standard version.

For the sub-prefix hijacking playbook we're building from node 1.1.1.1:

"Budget reality gaps in test environment:

- RPKI deployed in EMEA and AMER regions, not yet in APAC (budget constraint, planned for Q3 2024)
- Existing RPKI validation in EMEA is 'log only', not 'drop invalid' (operational caution, waiting for 95% ROA coverage before enforcing)
- Prefix filtering on peer AS64512 session is based on 2019 IRR snapshot (maintenance backlog, no resource to update)
- BGP monitoring exists via commercial service, but alerts go to shared inbox checked twice daily (staffing constraint)
- No automated detection of /25 announcements within known /24 space (feature not available in current monitoring tool)"

This makes your test results meaningful. If an attack succeeds, you know which control gaps enabled it. If an attack 
fails, you know which pragmatic controls actually worked, even if they're not perfect.

Lantern playbooks are judged on plausibility, not elegance. An elegant attack that requires perfect implementation is 
less valuable than a messy attack that exploits realistic gaps. The mess is the point. The mess is what makes the 
test worth running.

The [BGP hijacking tree](https://red.tymyrddin.dev/docs/in/network/roots/ip/bgp-hijacking) shows you everything that 
*could* go wrong. Playbooks show you what *actually* goes wrong given how networks are really built, really 
maintained, and really defended.
