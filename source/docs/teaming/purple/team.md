# Building your purple team

Purple teaming is a practice, not an org chart. Different organisations structure it differently based on size and maturity.

## Small organisations

Combined roles: Same people might play red and blue roles at different times. IT staff with security responsibilities can simulate attacks then validate defences.

External assistance: Partner with consultants or service providers for red team capability. Internal staff focus on blue team response and learning.

Scheduled exercises: Quarterly or semi-annual focused testing rather than continuous operations. Make each exercise count.

Focus on basics: Test common attack paths, validate core detections, ensure incident response works. Don't try to emulate sophisticated adversaries.

## Medium organisations

Dedicated roles: Separate red and blue team members, even if small teams. Security analysts handle detection and response, dedicated tester or small red team simulates attacks.

Purple team facilitator: One person coordinates exercises, ensures both sides prepare adequately, facilitates debriefs, tracks improvements. Might be security manager or senior analyst.

Regular cadence: Monthly or quarterly exercises testing different attack scenarios or defensive capabilities.

Tool investment: SIEM, EDR, and testing frameworks (Atomic Red Team, etc.) enable more sophisticated validation.

## Large organisations

Dedicated teams: Full red team, blue team (SOC), and purple team coordination function. Each team has specialised skills and dedicated time.

Continuous operations: Regular exercise cycles, threat hunting integrated with red team intelligence, automated adversary simulation.

Purple team program: Formal program with defined objectives, maturity model, metrics, and continuous improvement process.

Advanced testing: Full adversary emulation, assumed breach scenarios, targeted campaign simulations.

## Role clarity

Red team responsibilities:
- Plan and execute attack simulations
- Document all actions and TTPs used
- Operate within defined rules of engagement
- Share findings and techniques with blue team
- Provide realistic adversary perspective

Blue team responsibilities:
- Monitor for and respond to simulated attacks
- Document what was detected and how quickly
- Investigate alerts and suspicious activity
- Execute incident response procedures
- Identify detection gaps and defensive weaknesses

Purple team facilitator responsibilities:
- Coordinate exercise planning and scheduling
- Ensure both teams understand objectives
- Facilitate communication during exercises
- Lead debrief sessions
- Track findings and improvements
- Report progress to leadership
