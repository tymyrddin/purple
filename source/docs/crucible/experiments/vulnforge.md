# Vulnforge

[Vulnforge](https://github.com/tymyrddin/vulnforge) is a proof of concept with a claim to test: that a local
AI model can be useful for finding vulnerabilities in code without ever being trusted to decide whether it has
found one, and without anything it reads leaving the machine.

The experiment is in the division of labour. The model proposes, pointing at a function and hypothesising
where a vulnerability might sit. Code disposes: whether the hypothesis holds is decided by synthesising a
payload, running it in an isolated sandbox, and observing what actually happens, not by asking the model to
grade its own guess. The model's output is a model of the code in the systems sense, and execution is the
test that reads the error back. A hypothesis that survives contact with the sandbox is a finding; one that
does not is discarded, and the discarding is recorded.

Two further constraints keep it an experiment rather than a demo. Nothing leaves the host: after a one-off
online bootstrap that fetches the weights and builds the sandbox image, the analysis host runs offline, so no
prompt reaches a vendor and no third party logs what was investigated. And every step is written to a
tamper-evident audit log, so any finding traces back through the exact prompt, output, grounding, and
execution that produced it. `vulnforge audit-verify` walks the hash chain.

## Running it

`vulnforge bootstrap` does the one online step, fetching local open-source weights (the default is a Qwen 7B
that runs in an 8 GiB cgroup on a normal workstation) and building the rootless-podman sandbox image.
Afterwards `vulnforge scan path/to/repo` runs the staged pipeline offline: index, hypothesise, ground,
synthesise, execute, verify, report. `vulnforge probe path/to/file --function NAME` runs a single function
through the hypothesis and grounding stages without spending a payload synthesis or a container launch,
useful for watching where the reasoning holds and where it breaks. `vulnforge plumbing` is the end-to-end
smoke test.

## What it is testing

The wider bet is that AI reasoning works better as an arrangement of subsystems than as a single model asked
to do everything, including judge itself. Vulnforge is one worked example applied to vulnerability research:
the model supplies the intuition, the sandbox supplies the verdict, and the audit log supplies the
accountability. Whether that arrangement earns its keep is the kind of question the crucible exists to
answer, by running it rather than arguing about it.

*Last updated: 1 July 2026*
