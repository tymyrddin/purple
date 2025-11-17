# Blue → Red: Defence-led emulation

## Collaboration framework

### Share defensive coverage

Example Blue Team brief:

    ✅ **Blocked:**  
    - Excel 4.0 macros (ASR rule `BlockExcel4Macros`)  
    - RDP brute force (Network IDS threshold: 5 attempts/min)  

    ❓ **Uncertain:**  
    - Detection quality for CLR DLL sideloading  
    - Response time for Azure AD token theft  

    🔥 **Priority Tests Needed:**  
    - MFA bypass via token replay (T1556)  
    - Container escapes to host (T1611)  

### Tailor red team campaigns

Red Team adjusts emulation to:

* Avoid "wasted" tests (e.g., known-blocked TTPs).
* Focus on defence blind spots.

## Tools

* [Threat Informed Defense (TID) Platform](https://github.com/center-for-threat-informed-defense)
* [CALDERA](https://github.com/mitre/caldera) for adaptive emulation