# Communications evidence

Stedin's distribution network communicates via IEC 60870-5-104 telecontrol between the e-terra SCADA and field RTUs, and
via CDMA machine-to-machine on Utility Connect's network for smart-meter collection. Network traffic, protocol captures,
and timing anomalies form the observable layer for communications security.

## IEC 60870-5-104 protocol structure

IEC 60870-5-104 is Stedin's primary field-to-control communications protocol. It is a master-slave protocol where the
SCADA (master) initiates connections to RTUs (slaves) and issues commands or queries for state. The protocol defines
specific message types: command messages (Close, Open), response messages (command executed, state report), and
unsolicited reports (alarms, faults). Each message has a structure defined by the standard, with a common address and
information-object addresses and type identifiers. The protocol runs over TCP/IP on port 2404, which carries the
transport-level integrity; the application frame itself defines no checksum.

Normal IEC 60870-5-104 traffic shows a predictable pattern. The SCADA connects to an RTU, performs a sequence of
operations (reading state, issuing commands, reading back new state), and closes the connection. Each message is
acknowledged by the RTU. The timing is regular: SCADA connects, sends request, waits for response (typically
milliseconds), sends next request. This sequence repeats for each RTU the SCADA manages. Outside of maintenance windows,
traffic is lightweight (a few messages per minute per RTU, mostly unsolicited reports from RTUs to SCADA when state
changes).

During a maintenance operation (an operator at the control centre executing a planned switching sequence), traffic to a
specific RTU increases as operators issue commands and query state. The increase is expected and documented (a
bedieningsplan specifies the sequence of commands). The operator's view of the sequence matches the RTU's view: commands
issued match commands received, in the same order, with the same timing.

## Protocol capture and anomaly detection

Network captures of IEC 60870-5-104 traffic are the raw forensic source. A network analyser or IDS watching the network
can record all traffic between the SCADA and RTUs. The captures are stored in pcap (packet capture) format, readable by
standard tools like Wireshark. For forensic analysis, a pcap file is a complete transcript of what was communicated.

Normal protocol operation shows messages that conform to the IEC 60870-5-104 standard. Each message type can be parsed
by a protocol decoder and the payload understood. Command messages have specific structures, response messages match
expected types. Replay detection is straightforward: if a command message appears twice in rapid succession (less than a
second apart) and the SCADA's own log shows only one command being issued, the second message in the capture is a
replay.

Anomalies in protocol captures indicate either legitimate protocol violations (if the SCADA or RTUs are
non-conformant) or active attacks. A message that does not conform to the standard structure is anomalous: a command
with an invalid type identifier, or a response that does not match any valid response type. A message with a malformed
address field (the device address is outside the expected range) indicates either misconfiguration or tampering. A
sequence of messages where the SCADA sends a command and the RTU responds to a different command (the SCADA issues "
Close switchpoint A" and the RTU responds with "OK, switchpoint B is now Closed") indicates command injection or RTU
misconfiguration.

Timing anomalies are also observable in pcap files. The time between a command and its response is consistent (
typically 10-500 milliseconds depending on network latency). If the time is orders of magnitude longer than expected (
5-10 seconds), that could indicate network congestion or a compromised RTU processing the command slowly. If multiple
commands from the SCADA arrive at the RTU in rapid succession without waiting for responses (the SCADA sends command A,
command B, command C all within 10 milliseconds before receiving any response), that is unusual and could indicate
either pipelined operation (if the protocol supports it) or an attacker sending commands automatically.

## Network topology and unexpected connections

Stedin's distribution network topology is well-defined: the e-terra SCADA is in the control centre, RTUs are in
substations scattered across the region, and communication flows between them over dedicated network links or VPN
tunnels. Unexpected connections to RTUs (a connection from an engineering workstation that is not the authorised
engineering tool, or a connection from outside Stedin's network) are anomalies.

Authorised connections include: the main SCADA (initiating connections to all RTUs regularly), authorised engineering
workstations (connecting to RTUs during maintenance windows), and backup systems (standby SCADA or engineering tools
configured as redundancy). Any connection outside this list does not fit the baseline. A connection from an arbitrary IP address to
an RTU's IEC 60870-5-104 port (2404) is a red flag. If the firewall logs show such a connection, and no Stedin
staff authorised it, it is evidence of either a network intrusion or a serious misconfiguration.

Stedin's control-centre network is segmented from corporate IT for security. An RTU in a substation is directly
connected to the control centre's OT network, or connected via an encrypted VPN tunnel if it is remote. A connection
from an external network (the public internet, a contractor's network) directly to an RTU would require bypassing
the network perimeter, which would be detected by firewall logs. If such a connection appears in Stedin's logs with
no corresponding firewall alert, either the firewall logs were not complete or the connection was made through a
compromised path (a device inside Stedin's network acting as a relay).

## Metering communications and CDMA patterns

Stedin's smart meters communicate with the Utility Connect CDMA network to report consumption. The meters (Landis+Gyr,
Iskraemeco, Kaifa, Sagemcom) periodically transmit their readings to data concentrators that relay the data to the
metering platform. The normal pattern is a high-frequency burst of meter readings coming into the platform during the
metering windows (typically once or twice daily when meters report).

A baseline for metering traffic is the expected number of meters reporting during each collection window, the typical
consumption values, and the distribution of readings across the customer base. Anomalies in metering traffic include: a
sudden drop in the number of meters reporting (half of the meters in a feeder suddenly go silent), sudden spikes in
consumption readings (a feeder that normally shows 100 kW suddenly shows 1000 kW), consumption data that is suspiciously
round (all meters reporting exactly 1000 Wh with no variation), or missing periods (the metering data collection for an
entire hour is missing).

Tampering with metering data can occur at different points: at the meter itself (if an attacker can access a meter
physically and modify the stored consumption value), during transmission (if the CDMA network is compromised and
messages are intercepted or modified), or at the platform (if the metering database is compromised). The observable
evidence at each layer is different. Tampering at the meter would show up as individual meters reporting wrong values
that differ from physical verification (a technician measures the actual consumption by checking the meter's display, 
and it does not match the reported value). Tampering in transmission would affect groups of meters simultaneously (all
meters on a particular CDMA concentrator reporting anomalously). Tampering at the platform would affect the recorded
data in the database without necessarily affecting the meters themselves.

## CDMA network logs and transmission patterns

Utility Connect operates the CDMA machine-to-machine network. The CDMA network maintains logs of which meters
transmitted, when, and what data was received. For forensic analysis, access to Utility Connect's logs (if permitted)
provides an independent view of metering traffic. If Stedin's metering platform shows meter XYZ reported 500 Wh at 15:00
UTC, Utility Connect's logs show the meter transmitted that data at approximately the same time.

A divergence between Stedin's platform record and Utility Connect's network log indicates tampering at either layer. If
the platform shows a meter reported 500 Wh but Utility Connect's log shows the meter transmitted 450 Wh, the
platform data was edited after reception. If Utility Connect shows transmission at 15:00 UTC but the platform
records the same transmission at 15:15 UTC, there is a time-synchronisation issue or the data was held and inserted
later.

Normal CDMA transmission patterns are regular and repeating. Meters transmit during defined windows (typically early
morning or late evening), the transmission latency is consistent (seconds to minutes from meter transmission to platform
receipt), and the volume is stable (the same percentage of meters report each cycle). Anomalies include transmission
windows that shift (meters reporting at unusual times), increased latency (data arriving hours late), or missing
transmissions (transmission windows with no data arriving).

## IDS and anomaly detection

Stedin's network infrastructure (firewalls, network switches, and potentially intrusion-detection systems) logs
connections, traffic volume, and protocol anomalies. If Stedin has deployed an IDS on the OT network, it would detect
suspicious patterns: port scans, protocol violations, unusual traffic volumes, or traffic to unexpected destinations.

An IDS watching IEC 60870-5-104 traffic would flag messages that do not conform to the protocol standard, unusual
command sequences, or high-frequency commands that exceed normal baselines. Modern IDS systems can be trained on
baseline normal traffic and then flag deviations. If the IDS shows a surge in IEC 60870-5-104 commands to a
specific RTU, with the commands coming from an unexpected source, that is evidence of anomalous activity.

The limitation of IDS alerts is that they can generate false positives. A legitimate but unusual command sequence (
perhaps a technician manually testing an RTU with a sequence that rarely occurs) might trigger an IDS alert without
being malicious. IDS alerts provide initial pointers for investigation, and need reading against operational
activity and work orders before they mean much.

## Traffic volume and timing baselines

Beyond protocol-level analysis, traffic volume and timing provide forensic clues. Stedin's SCADA maintains a predictable
communication pattern: regular polling of all RTUs on a cycle (perhaps every minute), occasional commands during
operational windows, and unsolicited reports when RTU state changes. The total traffic volume per hour is relatively
stable: thousands of IEC 60870-5-104 messages per hour, but the rate is consistent.

A sudden spike in traffic volume stands out. If the average traffic is 5000 messages per hour but a specific hour
shows 50,000 messages, something unusual happened. The spike could be a legitimate operational activity (an extended
switching operation requiring hundreds of manual commands) or it could be an attack (an attacker issuing commands
automatically). Distinguishing them requires examining the messages themselves to see if they correspond to documented
work or not.

Timing baselines are also observable. If Stedin normally exchanges IEC 60870-5-104 traffic during working hours
(08:00-18:00) with minimal traffic at night, a sudden burst of traffic at 03:00 is anomalous. Again, this could be explained
by legitimate out-of-hours emergency work (a fault requiring urgent response) or it could be an attack. The explanation
depends on whether an emergency was documented and whether the traffic pattern matches the expected emergency response.

*Last updated: 12 July 2026*
