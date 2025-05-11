# Hypervisor exploitation & defence playbook

From architecture analysis to VM escape exploits and defensive hardening

## Hypervisor fundamentals

Key concepts

***x86 Virtualization (MITRE: [T1496](https://attack.mitre.org/techniques/T1496/))***: CPU rings, VT-x/AMD-V extensions, EPT/NPT

Tool: Check virtualization support:

```bash
grep -E "svm|vmx" /proc/cpuinfo  # Linux
systeminfo | findstr "Hyper-V"    # Windows
```

***Paravirtualization vs. Hardware-Assisted***

* Xen (PV), KVM (HVM), Hyper-V enlightenments

Purple team actions

- [x] Red: Identify hypervisor presence via timing attacks (e.g., RDTSC).
- [x] Blue: Monitor for abnormal CPUID/MSR reads (e.g., Splunk query for syscall_instruction events).

## Research framework development

### Attack paths

#### Guest-to-Host interface exploration

MITRE: [T1068](https://attack.mitre.org/techniques/T1068/)

Tools:

```c
// Unikernel example (e.g., IncludeOS) to trigger hypercalls
#include <stdint.h>
void _start() { asm volatile("vmcall"); }
```

```python
# Python script to fuzz hypervisor interfaces
import mmap, os
def fuzz_msr(msr): os.write("/dev/cpu/0/msr", msr.to_bytes(8, "little"))
```

#### Synthetic device testing

MITRE: [T1496](https://attack.mitre.org/techniques/T1496/)

Tools:

```bash

# List Hyper-V synthetic devices (Windows)
Get-VMHostSupportedVersion | fl *  # PowerShell
```

Purple team actions

- [x] Red: Fuzz VMBus channels with Boofuzz.
- [x] Blue: Audit hypervisor logs for unexpected MSR/hypercall access (e.g., Windows ETW Hyper-V-* providers).

## Hyper-V Deep Dive

### Attack paths

#### Synthetic MSR/SynIC exploitation

MITRE: [T1068](https://attack.mitre.org/techniques/T1068/)

Tools:

```c
// Trigger Hyper-V SynIC interrupt
__writemsr(0x40000080, 0x1);  // HV_X64_MSR_SIMP
```

#### VMBus EoP exploits

MITRE: [T1496](https://attack.mitre.org/techniques/T1496/)

Tools:

```bash
# List VMBus devices (Linux guest)
ls /sys/bus/vmbus/devices/
```

Purple team actions

- [x] Red: Exploit VMBus race conditions (CVE-2021-28476 PoC).
- [x] Blue: Monitor vmms.exe for crashes (Windows Event ID 41).

## Case Study: QEMU VM escape

### Attack paths

#### USB Emulation Bug (CVE-2021-20255)

MITRE: [T1496](https://attack.mitre.org/techniques/T1496/)

Tools:

```c
// EHCI DMA exploit (simplified)
struct ehci_qtd *qtd = mmap(0, 0x1000, PROT_READ|PROT_WRITE, MAP_FIXED);
qtd->token = 0x80008000;  // Force host memory write
```

### User-mode QEMU exploit

MITRE: [T1068](https://attack.mitre.org/techniques/T1068/)

Tools:

```bash
# Crash QEMU process with malformed USB packet
python3 -c 'print("\x00"*1024)' > /dev/usbmon0
```

Purple team actions:

- [x] Red: Use QEMU-AFL to fuzz device models.
- [x] Blue: Restrict QEMU with SELinux policies (e.g., deny mmap_zero).

## Purple team outcomes

### Red team 

* Hypervisor exploit PoCs (e.g., MSR write -> host RCE).

### Blue team

* Detection rules for abnormal hypercalls (Sigma/YARA).
* Hardening guides (disable legacy emulation, patch QEMU).

### Final deliverable

Joint report with:

* Attack trees for VM escapes.
* Hypervisor-specific MITRE ATT&CK mappings.
* Custom tools (unikernel fuzzer, VMBus tracer).
