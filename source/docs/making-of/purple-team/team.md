# Building the team

Purple teaming is a practice, not an org chart. Different organisations structure it differently based on size, maturity, and what they are trying to accomplish. The structure should follow the purpose, not the other way around.

## Small organisations

In small organisations, the same people often play red and blue roles at different times. IT staff with security responsibilities simulate attacks and then validate defences. This works when the people involved can genuinely shift perspective between the two roles, which requires deliberate effort: the habits and assumptions of the defensive mindset do not automatically produce good offensive simulation, and vice versa.

External assistance for red team capability is a common and sensible approach when internal offensive skill is limited. Internal staff focus on blue team response and learning. The value depends on how the external and internal parties communicate: an external red team that produces a report and disappears has not contributed to the learning loop.

Scheduled exercises, quarterly or semi-annual, rather than continuous operations. Make each exercise count by focusing on common attack paths, validating core detections, and ensuring incident response works. The goal is not sophistication; it is honest assessment of actual capability.

## Medium organisations

Separate red and blue team members, even if small. Security analysts handle detection and response; a dedicated tester or small red team simulates attacks. The separation allows each side to develop depth in their domain.

A purple team facilitator who coordinates exercises, ensures both sides prepare adequately, facilitates debriefs, and tracks improvements is worth having even in organisations where this is part of someone's role rather than their whole job. The facilitation is a skill in its own right: running a debrief that surfaces honest findings rather than defensive or placating accounts requires attention to the emotional and political layers as well as the technical ones.

Regular exercise cadence, monthly or quarterly, testing different attack scenarios or defensive capabilities. Tool investment in SIEM, EDR, and testing frameworks enables more systematic validation.

## Large organisations

Dedicated teams with specialised skills, defined time, and a formal programme. Purple team coordination becomes a programme function with its own objectives, maturity model, metrics, and improvement process.

Continuous operations: regular exercise cycles, threat hunting integrated with red team intelligence, automated adversary simulation. The risk at this scale is that the programme becomes process-heavy and loses the honest feedback loop that gives it value. A programme that produces excellent documentation of exercises that everyone knows are unrealistic is not producing useful information.

## Role clarity in any structure

Whatever the structure, the responsibilities need to be explicit before the exercise, not negotiated during it.

Red team responsibilities: plan and execute attack simulations, document all actions and TTPs used, operate within defined rules of engagement, share findings and techniques with the blue team in a form the blue team can use. The last part is often underinvested. A list of findings without context about how they were reached and what changed if specific controls had been in place is less useful than findings with that context.

Blue team responsibilities: monitor for and respond to simulated attacks, document what was detected and how quickly, investigate alerts and suspicious activity, execute incident response procedures, identify detection gaps and defensive weaknesses. The discipline to document during the exercise is harder than it sounds and worth practising separately.

Purple team facilitator responsibilities: coordinate exercise planning and scheduling, ensure both teams understand objectives, facilitate communication during exercises, lead debrief sessions, track findings and improvements, report progress to leadership. The facilitation role is the one most directly responsible for whether the emotional and political layers of the exercise are handled well.
