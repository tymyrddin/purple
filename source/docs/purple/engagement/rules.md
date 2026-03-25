# Rules of engagement

Rules protect both organisation and testers. Document and agree them before any testing begins.

## Legal and authorisation

Written permission: Signed authorisation from appropriate authority (CISO, CIO, CEO depending on scope) explicitly permitting all planned activities.

Scope documentation: Detailed scope included in authorisation. No verbal agreements or implied permissions.

Legal review: Legal counsel reviews ROE for compliance with laws, regulations, contracts.

Third-party agreements: If testing could involve third-party systems, ensure contracts permit testing or get explicit consent.

## Technical boundaries

Do not harm criteria: Specific conditions that immediately stop testing:
- Production service outage or degradation
- Data corruption or loss
- Safety system compromise
- Unintended access to highly sensitive data

Notification requirements: When must testers notify exercise manager? Discovering critical vulnerability? Unintended impact? Accessing regulated data?

Credentials and access: Can testers use discovered credentials? Create their own accounts? What about admin credentials?

Tools restrictions: Any tools explicitly prohibited? Loud scanning tools? Destructive exploits? Persistence mechanisms that are difficult to remove?

## Operational guidelines

Communication channels: How do teams communicate during exercise? Dedicated Slack channel? Email thread? Emergency phone number?

Stop conditions: What triggers immediate halt? Safety issue? Scope violation? Request from leadership?

Working hours: Can testing occur 24/7 or only during business hours? Consider impact on on-call staff and business operations.

Evidence handling: How is sensitive data encountered during testing handled? Encrypt? Delete immediately? Report without capturing?

## Social engineering boundaries

Targets: Are all employees fair game or specific roles only? Junior staff? Executives?

Techniques: Which social engineering methods are permitted? Phone calls? Physical visits? Impersonation? What's off limits?

Stress limits: Stop if causing genuine distress. Red teaming isn't about traumatising employees.

Disclosure: How and when are employees told they were part of social engineering test?
