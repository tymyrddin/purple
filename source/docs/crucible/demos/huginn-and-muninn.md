# Huginn and Muninn

[Huginn and Muninn](https://github.com/tymyrddin/huginn-and-muninn) are Odin's ravens, Thought and Memory, and
here they are a small local toolkit for watching the real routing world. It reads public data and announces
nothing: no cloud, no peering, no ASN of its own, a laptop is plenty. Huginn is the now, live observation of
what is being announced, by whom, and whether the table believes it. Muninn is the then, the history of who
announced a prefix and when, from RIPE's routing archive.

Where [inter-domain-simlab](../ctfs/inter-domain-simlab.md) is the safe range, this watches the commons for
real. `huginn/watch.py 203.0.113.0/24 --more-specific` streams every announcement and withdrawal touching a
prefix, including the more-specific kind a hijack makes. `huginn/glass.py` takes a snapshot of who is
announcing a prefix right now, grouped by origin and flagging a MOAS, more than one origin, which is what a
hijack looks like from the outside. `huginn/validity.py 65020 203.0.113.0/25` asks whether an origin and
prefix are RPKI-valid, through RIPEstat's public API or a locally run Routinator for a verdict that needs no
third party. The recon is the fun half: the same watching an attacker does before a hijack, run from the
defender's chair.

## Running it

`pip install -r requirements.txt` (only the live websocket watcher needs it; the snapshot and validity tools
use the standard library), then run the scripts above. Nothing leaves the machine except the calls to the
public RIPE data it reads.
