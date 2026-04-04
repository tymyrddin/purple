# Sequence of work

## Phase 1: Design the attack story

1. [Define attacker goal, not just “get root”](https://red.tymyrddin.dev/docs/power/)
2. Anchor it in an ICS narrative, even if slightly theatrical ;-)
3. Design a linear but not obvious path:
   * discovery
   * protocol interaction
   * manipulation
   * consequence
4. Define flags early, not at the end when everything is glued together

A common failure mode is building a lab first and trying to retrofit a story later. That tends to produce confusion dressed as difficulty.

## Phase 2: Reduce the simulation

5. Identify the minimum viable system:
   * one PLC equivalent
   * one control interface or service
   * one observable physical effect
6. Remove everything that does not contribute to the attack path
7. Hard-code or simplify physics where needed

If a component does not create or support a question, it is clutter.

## Phase 3: Build the VM

8. Create VMware VM:

   * Debian 8 compatible base
   * BIOS boot
   * DHCP networking

9. Install only what is needed:

   * Python environment or Docker
   * Networking tools such as `nmap`, `netcat`, `tcpdump`
   * Protocol tools if relevant

10. Avoid runtime downloads:

    * Clone repos during build
    * Vendor dependencies locally if possible

This avoids the silent failure when the VM wakes up in a network-less void.

## Phase 4: implement the simulation

11. Install and configure chosen simulation:

    * Option A: Run `power-and-light-sim` as a background service
    * Option B: Deploy minimal Docker compose

12. Make startup deterministic:

    * `systemd` service or `init` script
    * No manual steps required by the user

13. Expose only necessary ports:

    * Modbus 502, or equivalent
    * Avoid noise

14. Introduce controlled weaknesses:

    * Predictable register values
    * Writable coils
    * Weak service configs

## Phase 5: design the challenge layer

15. Place flags logically:

    * Inside protocol data
    * In filesystem
    * Tied to physical outcome

16. Ensure each task teaches something:

    * Scanning
    * Protocol interaction
    * Manipulation
    * Escalation

17. Avoid accidental shortcuts:

    * Remove unnecessary SUID binaries
    * Close unrelated services

Otherwise, someone solves it in three commands and learns nothing except disappointment.

## Phase 6: test under constraint

18. Throttle the VM:

    * 1 CPU
    * 1 GB RAM, then try 0.5 GB

19. Run full attack path:

    * From zero knowledge
    * No assumptions

20. If it only works when everything behaves perfectly, it will fail in production. Everything fails in production. Test failure modes:

    * Restart VM
    * Partial service startup
    * Slow responses

## Phase 7: optimise

21. Reduce footprint:

    * Remove build tools
    * Clean package cache
    * Compress logs

22. Stabilise timing:

    * Avoid race conditions on startup
    * Delay services if needed

23. Consistency beats realism here:

    * Same results after reboot
    * Same flag paths

## Phase 8: export and validate

24. Shutdown cleanly
25. Export to OVF via VMware
26. Convert to OVA via VirtualBox
27. Re-import and test

The VirtualBox hop is not elegance, it is survival.

## Phase 9: integrate with TryHackMe

28. Upload VM
29. Create room
30. Map tasks to attack stages
31. Attach VM
32. Use platform variables where possible:

    * `machine_ip`
    * Dynamic hints

## Phase 10: write the solution

33. Document the intended path
34. Include commands, reasoning, and expected outputs
35. Keep it aligned with the design, not with whatever accidental path worked during testing (I know myself)
