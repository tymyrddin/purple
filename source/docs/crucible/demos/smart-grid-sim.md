# Smart Grid SimLab

![Ankh Morpork feedback loops](/_static/images/smart-grid-simlab.png)

[Smart Grid SimLab](https://github.com/tymyrddin/smart-grid-sim) is a demonstration, not a challenge. It runs
a synthetic smart grid, smart meters, solar inverters, EV chargers and substations, publishing live telemetry
over MQTT, and puts an attack engine between that telemetry and a real-time dashboard. When an attack fires,
the engine changes the data in transit and the dashboard shows the consequence. There are no real devices,
protocols or networks; the grid is synthetic and the point is visibility.

The pitch is the gap between being told and being shown. Being told that an attacker can manipulate sensor
data is one thing. Watching the voltage lines spike and flatline while the physical grid is fine is another.
Each attack in the dropdown carries the real incident behind it, from the plain building blocks (telemetry
spoofing, a Modbus register write, a forced shutdown) to nation-state scenarios modelled on documented
events: the coordinated blackout of Ukraine 2015, Industroyer, the transformer that overheats the way Stuxnet
drove Natanz, the Modbus heating attack of FrostyGoop, the ransomware shutdown of Colonial Pipeline.

It is built for the room where the trade-offs get made: awareness sessions, internal demos, and boardroom
explanations of OT/ICS threats, an audience that does not need to know what Modbus is to follow what the
dashboard is doing.

## Running it

`docker compose up broker`, then `pip install -r requirements.txt` and start the pieces:
`python -m simulator.main`, `python -m attacks.engine`, and `python -m dashboard.app`. The dashboard comes up
at `http://localhost:8050`, or `docker compose up --build` runs everything at once. The Pause button freezes
the dashboard mid-scenario, useful when something worth discussing is on screen and the data would otherwise
race past it.

Blue keeps the defender-facing writeup at
[Smart Grid SimLab](https://blue.tymyrddin.dev/docs/ot/labs/smart-grid-sim/).
