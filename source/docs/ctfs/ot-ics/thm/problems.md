# Potential problems

We are not building an ICS lab. We are building a convincing story about one, under severe resource constraints,
for an audience that will try to break it in creative ways.

## Common failure modes

* VM fails to start under 0.5 GB RAM: the simulation stack is too heavy, services silently crash or never start
* Services attempt to fetch dependencies at runtime and fail with no useful error (no internet inside the VM)
* Race conditions on startup under resource contention: services come up in the wrong order, protocol interactions break
* OVA rejected on upload: typically caused by UEFI boot, oversized disk image, or incorrect export settings
* Debian 8 package gaps: packages available in modern repos may not exist or may be too old to behave as expected
* Reboot wipes state: anything that wrote to disk during a session is gone, breaking challenges that rely on persistence
* VirtualBox OVF export producing an OVA that re-imports incorrectly: test the import before submitting

## Dependencies

| Dependency         | Notes                                             |
|:-------------------|:--------------------------------------------------|
| VMware Workstation | VM build environment                              |
| VirtualBox         | Required for OVA export step only                 |
| Python 3           | For deterministic simulator                       |
| Docker Engine      | For micro-Docker option only (2-3 containers max) |
| Git                | Repo cloning during VM build, not at runtime      |

Fewer runtime dependencies reduce the chances of a silent failure inside the VM.
