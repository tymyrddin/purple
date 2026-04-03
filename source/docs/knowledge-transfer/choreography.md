# Why security knowledge does not easily transfer

After every significant incident, the organisation produces documentation. Findings are written up, lessons are 
captured, playbooks are updated, post-mortems are filed. Then the next incident arrives, and the team encounters 
the same gaps in roughly the same places.

This is not a documentation format problem. It is a conditions problem.

[Satir's work on congruence](../foundations/organisational-development/satir-core.md) is directly applicable here. The 
stated culture says: we learn from incidents and document what we find. The actual culture often says something 
different: honest findings attract scrutiny, scrutiny generates workload, and the person who names the real cause 
carries a disproportionate share of what follows. People make rational decisions about what to document based on the 
actual culture, not the stated one. The result is documentation that reflects the process the organisation wishes it 
had, not the one it uses.

[SEM offers a complementary diagnosis](../foundations/system-effectiveness/core-triad.md). An incident is not a 
deviation from normal operations: It is normal operations with one model assumption exposed as false. A playbook 
that documents the sequence of the incident without examining the model that produced it leaves that model intact. 
The system will generate the same class of failure again with different timestamps, and the next playbook update 
will document that one too.

The practical work of knowledge transfer, building playbooks, manuals, dashboards, and workflows that actually get 
used, is not separable from the conditions question. Playbooks decay not because nobody maintains them but because 
the people who know what they should say do not feel it is safe to say it. Manuals fail not because of bad formatting 
but because they were written by people who have never used them under pressure, and the people who have are not the 
ones writing. Dashboards become decoration not because of bad design choices but because the incentive to show good 
numbers shapes what gets displayed.

Getting the conditions right does not require resolving all of this before doing the practical work. It requires 
naming it, building processes that produce honest rather than safe documentation, and treating the gap between the 
written version and the operational reality as a finding rather than an embarrassment.

So how to build playbooks that survive contact with reality, 
manuals that get used at 3:00, dashboards that answer the question the analyst is actually asking, and workflows 
that reduce friction rather than add it. They are most useful when the conditions for honest documentation exist. 
Where those conditions are still being built, the section on 
[organisational development](../foundations/organisational-development/satir-core.md) is the place to start.

## Related

- [Playbooks that actually work](playbooks.md)
- [Moving beyond manuals nobody reads](manuals.md)
- [Dashboards that actually get used](dashboards.md)
- [Workflows that get followed](workflows.md)
- [SIRT structure](../making-of/sirt/structure.md)
- [SOC workflows](../making-of/soc/workflows.md)
