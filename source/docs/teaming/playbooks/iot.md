# IoT exploitation & defence playbook

From device reconnaissance to RF attacks and embedded system hardening

## IoT threat landscape

IoT attack surface ([MITRE T0891](https://attack.mitre.org/techniques/T0891/)): Default credentials, unpatched firmware, exposed services

Tool: Shodan queries for vulnerable devices

```bash
# Find exposed IoT cameras  
shodan search 'http.title:"Camera" port:80'  
# Discover industrial PLCs  
shodan search 'product:"Modbus"'  
```

IoT worm propagation

* Case Study: Mirai (CVE-2016-6277, CVE-2017-17215)
* MITRE: [T1587.001](https://attack.mitre.org/techniques/T1587/001/) (Malware Development)

Purple team actions

- [x] Red: Simulate worm propagation with Mirai-API.
- [x] Blue: Deploy network segmentation and monitor for Telnet/SSH brute force (Zeek/Suricata rules).

## Embedded device dissection

### Attack paths

#### Hardware reconnaissance

MITRE: [T1600](https://attack.mitre.org/techniques/T1600/) (Hardware Access)

Tools:

```bash
    # Identify CPU architecture  
    cat /proc/cpuinfo  # Linux  
    strings firmware.bin | grep -i "ARM\|MIPS"  
```

#### UART/JTAG exploitation

MITRE: [T1180](https://attack.mitre.org/techniques/T1180/) (Physical Access)

Tools:

```bash
# Connect to UART (115200 baud common)  
screen /dev/ttyUSB0 115200  
# JTAG pinout discovery with JTAGenum  
./jtagenum.py -d /dev/ttyACM0  
```

Purple team actions

- [x] Red: Extract firmware via UART/JTAG using Flashrom.
- [x] Blue: Physically disable debug ports (epoxy, PCB traces) and monitor for GPIO tampering.

## Embedded device exploitation

### Attack paths

#### Static analysis

MITRE: [T1595](https://attack.mitre.org/techniques/T1595/) (Firmware Analysis)

Tools:

```bash
# Extract firmware with binwalk  
binwalk -e firmware.bin  
# Find hardcoded credentials  
strings firmware.bin | grep -i "admin\|password"  
```

#### Dynamic analysis (Emulation)

MITRE: [T1550](https://attack.mitre.org/techniques/T1550/) (Device Emulation)

Tools:

```bash
# Emulate MIPS firmware with QEMU  
qemu-mips -L ./ squashfs-root/bin/httpd  
# Fuzz with AFL++  
afl-fuzz -i input/ -o output/ -- ./httpd  
```

Purple team actions

- [x] Red: Exploit buffer overflows in emulated services (GDB + Pwntools).
- [x] Blue: Deploy anomaly detection for memory corruption (e.g., Canary).

## Software-Defined Radio (SDR) Attacks

### Attack paths

#### RF reconnaissance (SCRAPE methodology)

1. Survey: Identify target frequency (e.g., 433 MHz for garage doors).
2. Capture: Use rtl_433:

```bash
    rtl_433 -f 433.92M -s 250k  
````
3. Replay: Transmit captured signals with HackRF:

```bash
    hackrf_transfer -t captured_signal.raw -f 433920000 -s 2000000 -x 40  
```

#### Rolling Code Bypass

MITRE: [T1597](https://attack.mitre.org/techniques/T1597/) (RF Interception)

Tools:

```python
# Jam signals to force re-transmission (GNU Radio)  
from gnuradio import blocks, analog  
jammer = analog.sig_source_c(433.92e6, analog.GR_SIN_WAVE, 0, 1)  
```

Purple team actions

- [x] Red: Clone RFID badges with Proxmark3.
- [x] Blue: Implement frequency hopping (e.g., Bluetooth LE) and monitor for RF jamming.

## Zigbee & Z-Wave Exploitation

### Attack paths

#### Zigbee recon & eavesdropping

MITRE: [T1597.001](https://attack.mitre.org/techniques/T1597/001/) (Wireless Sniffing)

Tools:

```bash
# Capture Zigbee traffic with Ubertooth  
ubertooth-btle -f -c capture.pcap  
# Decrypt with known network key (KillerBee)  
zbdump -w zigbee.pcap -c 11  
```

#### Z-Wave key extraction

MITRE: [T1600.001](https://attack.mitre.org/techniques/T1600/001/) (Physical Theft)

Tools:

```python
# Dump Z-Wave keys via exposed UART (Raspberry Pi + Z-Stick)  
import serial  
ser = serial.Serial('/dev/ttyACM0', 115200)  
ser.write(b'\x01\x08\x00\xF2\x51\x01\x00\x00\x00\x00\x00\x00')  # Request network keys  
```

Purple team actions

- [x] Red: Clone Zigbee door locks with CC2531.
- [x] Blue: Rotate Zigbee network keys monthly; monitor for abnormal join requests.

## IoT Honeypots (HoneyThing)

### Attack paths

#### Emulating vulnerable devices

MITRE: [T1584.005](https://attack.mitre.org/techniques/T1584/005/) (Botnet)

Tools:

```bash
# Deploy HoneyThing (Telnet honeypot)  
docker run -p 23:23 -d honeypots/honeything  
# Log attacker IPs and commands  
tail -f /var/log/honeything.log  
```

#### RF Honeypots (Fake smart home)

MITRE: [T1596](https://attack.mitre.org/techniques/T1596/) (Scanning)

Tools:

```bash
# Simulate Zigbee thermostat (RTL-SDR + GNU Radio)  
grc -l zbsim.grc  # Generates fake temperature broadcasts  
```

Purple team actions

- [x] Red: Test honeypot effectiveness with automated scanners (e.g., Shodan-CLI).
- [x] Blue: Feed honeypot data to SIEM (e.g., Splunk query for dest_port:23 AND NOT internal_ip).

## Purple team outcomes

### Red team

* PoC exploits (firmware RCE, RF replay attacks).
* Shodan-based exposure reports.
* Zigbee/Z-Wave: PoC for smart lock bypass via key re-use and PCAPs of encrypted vs. unencrypted Z-Wave traffic.
* Honeypots: Map attacker TTPs to IoT-specific ATT&CK.

### Blue team

* Hardened firmware images (signed updates, stripped debug symbols).
* RF intrusion detection (e.g., RFeye).
* RF Defense: Zigbee network segmentation (PAN ID isolation) and Z-Wave S2 encryption enforcement.
* Honeypot hardening: Deploy CanaryTokens in firmware images.

### Final deliverable 

Joint report with:

* Attack Trees: UART → Firmware Extraction → RCE.
* MITRE Mapping: Aligns with ICS Matrix.
* Toolkit: Custom scripts (Shodan scraper, RF replay tool).

Suggestions for:

* Red: Zigbee clustering attacks: Exploit poorly implemented ZCL (Zigbee Cluster Library).
* Blue: Honeypot automation: Integrate HoneyThing with TheHive for incident response.
