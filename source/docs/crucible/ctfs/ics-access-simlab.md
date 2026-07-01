# ICS Access and Persistence SimLab

[ICS Access and Persistence SimLab](https://github.com/tymyrddin/ics-access-simlab) models the estate of
Unseen University Power and Light Co., Ankh-Morpork's utility provider: infrastructure assembled over decades,
documentation patchy, security posture emergent. Five network zones on real Linux bridges, FRR-routed
boundaries with actual iptables forwarding policy, around thirty-five containers on a single Linux host.
Vulnerabilities are properties of the simulated systems, not options in a configuration file, so the
consequences follow from what a player actually does.

## Where a player starts

`./ctl ssh` drops the player onto `unseen-gate` in the internet zone (10.10.0.0/24), holding only what that
position carries. From there the estate runs inward through Purdue-model layers: internet and city network,
a directly reachable DMZ, corporate enterprise, site operations, and the control zone with the field devices.
Five FRR routers enforce a deny-by-default forwarding policy between the zones, and the routers are themselves
discoverable: their SSH admin plane lands in `vtysh` with default credentials that open configure mode.

## The DMZ, reachable without a foothold

Four targets sit in the Guild Quarter, directly reachable from the internet zone.

`contractors-gate` is an SSH bastion with root password authentication and an optional CVE-2024-6387 path. The
root password is reused on the Neuron gateway in the same zone, a credential-reuse find that opens two
directions at once. `guild-exchange` runs an umatiGateway management UI with no authentication
(CVE-2025-27615); the OPC-UA endpoint it exposes takes no credentials with its security policy set to None, and
the callable methods include `stopPump()`. Two hops from a browser to a stopped pump. `substation-rtu` exposes
an unauthenticated REST API that writes IEC-104 datapoints, so any IEC-104 master polling the RTU receives
whatever the REST call last wrote; consistent falsification looks like a grid event, inconsistent falsification
looks like a sensor fault. `guild-clock` is an unauthenticated NTP server, more useful as a precondition than a
prize: shifted timestamps corrupt log correlation and widen replay windows.

## The IT to OT pivot

Entry through `wizzards-retreat` (SSH, an NFS mount, or OSINT) lands on a host with standing VPN tunnels into
enterprise and operational. A short path uses an Ed25519 key found there to reach the engineering workstation
in two hops. The full chain adds enterprise credential harvesting through anonymous FTP and SMB on a legacy
file server, SCADA access with default credentials, and a choice between path traversal and SQL injection
against the historian. The control zone holds the turbine PLC, two relay IEDs and a revenue meter, all speaking
Modbus with no authentication. There are three ways to trip the turbine: an emergency-stop coil write (logged
as an estop, noisy), an overspeed setpoint write (appears as a protection event), or a relay overcurrent
threshold write that brings the turbine down through its own protection acting on a threshold the player set.
Poisoning the historian ingest with normal-looking readings while the turbine is offline keeps the dashboard
green for as long as the injected values stay plausible.

## Real routing, real failure

Zone separation is not simulated; it is enforced by actual iptables rules on actual Linux bridges. A chain that
cannot find its way through the forwarding policy fails the way it would on a real network, not because a
scoring system says so. The chains branch on real choices: noisy or stealthy, consistent or inconsistent
falsification, speed or coverage. The Discworld setting is decorative. The vulnerabilities are not.

The defender's side of the same estate, what the detection and monitoring plane can and cannot see, is written
up in blue:
[ICS Access and Persistence SimLab, from the defensive view](https://blue.tymyrddin.dev/docs/ot/labs/ics-access-simlab/).
