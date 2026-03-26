# What could break it: vulnerability identification

Duration: 45 to 60 minutes

Materials: asset cards from the previous exercise, new cards for vulnerabilities, markers

## The exercise

For each critical asset, identify specific ways it could fail, be compromised, or become unavailable. Vulnerabilities are not just technical weaknesses. They are any condition that makes an asset exposed to a threat.

The [SEM](../foundations/system-effectiveness/index.rst) framing is useful here. Most recurring vulnerability classes have a model underneath them. Unpatched systems persist because the model is "patching creates operational risk" and there is no mechanism for establishing that the risk of not patching is higher. Secrets in source code persist because the model is "secret management is someone else's concern" and no safe alternative exists within the workflow. Identifying the vulnerability without identifying the model that produced it means the vulnerability will return in a different form after it is addressed.

Step 1: Focus on one asset at a time (5 minutes to select)

Start with the most critical asset. Trying to assess all assets simultaneously produces superficial coverage of everything. Depth on the most important assets is more valuable than breadth across all of them.

Step 2: Brainstorm vulnerabilities (15 minutes per asset)

Ask: what could go wrong? Work across four categories:

Technical weaknesses: unpatched systems, weak or absent authentication, no backups, single points of failure, insecure configurations, insufficient monitoring. Be specific. "Weak security" is not a vulnerability. "Admin accounts without MFA on the payment processing system" is.

Process failures: absent change control, missing documentation, inadequate testing procedures, poor access management lifecycle, no formal offboarding process.

Human factors: susceptibility to social engineering, key person dependencies where only one person understands a critical system, decisions made under pressure without adequate review, training that produces awareness without capability.

External exposure: supplier failures, third-party access that is broader than necessary, regulatory changes that create new compliance obligations, dependencies on services outside the organisation's control.

Step 3: Reality check (10 minutes)

For each vulnerability, ask: does this actually exist, or is it theoretical? Can it realistically be exploited given the access a plausible adversary would have? Has something like this happened here or in comparable organisations?

Remove items that are theoretical or that require adversary capabilities well beyond any realistic threat actor. Keep the list grounded in what is real and current.

Step 4: Group by type and repeat

Cluster the vulnerabilities by the four types above, then repeat for the next four or five critical assets.

## Output

Vulnerabilities mapped to critical assets, grouped by type, verified as current and realistic, and specific enough to be addressed. The specificity requirement is worth enforcing: a vulnerability description that is too vague to be given an owner is too vague to be a finding.

## What the exercise reveals

The distribution of vulnerabilities across the four categories is informative. A list that is predominantly technical and nearly empty on the human and process sides reflects the composition and focus of the group rather than the actual vulnerability landscape. Organisations rarely fail primarily for technical reasons.

The reality check step is where the conversation becomes most useful. When the group disagrees about whether a vulnerability is real or theoretical, that disagreement is revealing either a gap in shared understanding of the system or a gap between the group's model of the system and the system itself.
