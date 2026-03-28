# Playbooks and runbooks

Both playbooks and runbooks are operational documents. They look similar on the surface — both describe what to do in a given situation — but they serve different purposes and are used differently in practice.

## Playbooks

A playbook describes how to handle a *class of scenarios*. It includes decision points, branching logic, and adaptation to context. You use it as a guide, not a script.

A playbook is the right format when:

- The situation requires judgement about which path to take
- The same scenario can unfold in several different ways
- The document needs to be adapted to the specific environment or engagement
- You want to capture tactics, techniques, and decision rationale alongside the steps

Examples: an attack playbook for initial access via phishing (which varies by target), a detection playbook for lateral movement (which branches depending on what tooling you have), a response playbook for ransomware (which depends on what is affected).

## Runbooks

A runbook describes how to carry out a *specific procedure*. It is linear, prescriptive, and meant to be followed as written. Consistency is the point.

A runbook is the right format when:

- The steps are the same every time
- Accuracy matters more than adaptation
- The document will be used by someone who needs to execute, not decide
- You want to reduce variation and error in a routine operation

Examples: a runbook for standing up C2 infrastructure, a runbook for DNS tunnelling exfiltration, a runbook for rotating credentials after an engagement, a runbook for restoring a system to baseline.

## Both sides use both

The distinction is not about which team the document belongs to. Red teams have playbooks (attack scenarios, technique chains) and runbooks (infrastructure setup, tool procedures). Blue teams have playbooks (detection and response for known threat types) and runbooks (alert triage steps, containment procedures, recovery checklists).

The question to ask when categorising a document: does it require the reader to make decisions, or does it require them to follow steps? If decisions, it is a playbook. If steps, it is a runbook.

## When the line blurs

Some documents contain both. A response playbook might embed a runbook for a specific containment procedure. An attack playbook might reference a runbook for tool setup. That is fine — the outer document sets the scenario and the decision logic; the inner procedure handles the execution detail.

If a document has grown into something that is neither clearly one nor the other, it is usually a sign it needs to be split.

## Examples
                                                                                                                                                                                                               
- [Playbooks: when judgement is required](https://green.tymyrddin.dev/docs/playbooks/)
- [Runbooks: step-by-step procedures](https://green.tymyrddin.dev/docs/runbooks)