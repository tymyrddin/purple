Threat actors and capabilities
============================================

.. image:: /_static/images/distribution-threat-landscape-actors.png

State actors have the patience for supply-chain and persistence plays, degrading service on demand or quietly learning
how the network behaves at scale; criminals go where the money is, ransoming the IT layer or defrauding the metering
estate rather than attacking the grid directly; and insiders trade on concentrated access, dressing an unauthorised
act as legitimate maintenance.

.. toctree::
   :maxdepth: 1

   threat-actors

The recurring conclusion is that capability on paper is not capability in practice. The elegant coordinated cascade,
disable protection, corrupt the model, drive devices into unsafe states, runs into three hard constraints: the
operational layer is not internet-facing, so reaching it needs supply-chain, network or physical access; it is
instrumented for forensics, so legitimate-interface use is logged while bypassing the interface needs physical or
supply-chain compromise; and the operator knows what the baseline should look like, so divergence surfaces and a
cascade takes seconds to minutes rather than an instant.

What survives those constraints is not an attack on the equipment but on the processes that manage it: the engineering
workstations, the network model, the certification of who may work. Such an attack exploits legitimate activity that
is hard to audit continuously. A thinning, contractor-heavy workforce concentrates access to those systems in fewer
hands and extends the exposure into the supply chain.
