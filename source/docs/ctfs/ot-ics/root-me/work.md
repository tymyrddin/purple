# Sequence of work

This plan covers the creation and submission of CTF challenges for Root-Me using OT/ICS protocols such as 
[Modbus, DNP3, and IEC-104](../attack-surface.md). The environment is based on 
[two complementary simulation approaches](../resources.md):

* A dynamic, multi-component ICS environment
* A deterministic, single-system simulator

No external hosting is required. Execution occurs within Root-Me infrastructure using Docker-based setups 
or standalone artefacts such as PCAP files.

### Phase 1: define the core mechanic

1. Select challenge concept
2. Identify the single technique being tested
3. If the flag is vague, the challenge is vague. Define flag location and retrieval method

### Phase 2: choose the environment

4. Decide between dynamic (`ics-simlab`) and deterministic (`power-and-light-sim`)
5. Justify the choice based on:

   * Interaction needs
   * Reproducibility
   * Complexity budget

This decision prevents over-engineering later.

### Phase 3: build the minimal scenario

6. Implement only the components required for the mechanic
7. Remove or disable unrelated services
8. Stabilise behaviour:

   * Fix values where randomness adds no value
   * Keep dynamic effects only if they are part of the lesson

### Phase 4: validate the attack path

9. Execute the full attack from scratch
10. Record commands and outputs
11. Check for unintended alternative solutions

If a shortcut exists, it becomes the solution.

### Phase 5: generate artefacts

12. For Network challenges:

    * Capture traffic during exploitation
    * Verify completeness and clarity

13. For Realist challenges:

    * Verify service exposure
    * Confirm consistent startup behaviour

### Phase 6: write documentation

14. README:

    * Objective
    * Minimal setup
    * Target description

15. Solution:

    * Exact steps
    * Expected outputs
    * Explanation of impact

16. This is where the challenge stops being a trick and becomes useful. Add context:

    * What would break the attack in reality
    * Detection opportunities
    * Incorrect assumptions

### Phase 7: package and verify

Documentation that is not tested is fiction.

17. Create `.zip`
18. Extract on clean system
19. Follow README exactly
20. Confirm solution still works

### Phase 8: submit and iterate

Patterns in reviewer feedback are more valuable than initial design assumptions.

21. Submit small batch
22. Incorporate feedback
23. Refine subsequent challenges

