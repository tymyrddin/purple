# Environment

The rooms use `power-and-light-sim` as a single-process Python service inside a VMware-built
VM uploaded to TryHackMe. TryHackMe allocates 0.5-1 GiB RAM and 1 CPU core to uploaded VMs,
which is why a single-process simulator is the right fit. Lock the VM build approach before
starting; changing it later means rebuilding.

## Host environment

| Component      | Specification       |
|:---------------|:--------------------|
| Host OS        | Ubuntu              |
| Virtualisation | VMware Workstation  |

## VM base

| Component  | Specification                          |
|:-----------|:---------------------------------------|
| OS         | Debian 8 compatible                    |
| Boot       | BIOS, not UEFI                         |
| Network    | DHCP only, no static IP                |
| RAM target | Functional at 512 MB, 1 GB comfortable |
| CPU        | 1 core                                 |

## Runtime environment

Python 3 and pip, plus whatever tools the room requires. All Python dependencies are vendored
into a local directory during the VM build using `pip install --find-links`. Nothing fetches
from the internet at runtime; the VM has no outbound internet access after upload.

Services run as `systemd` units and start automatically on boot without manual intervention.

## Room structure

TryHackMe rooms are built from tasks. Each task has a description and optional questions.
There are no other section types.

| Element            | Notes                                                                      |
|:-------------------|:---------------------------------------------------------------------------|
| Tasks              | Primary unit; each has a description and 0 or more questions               |
| Question types     | Free-text (specific answer required), multiple choice, no answer needed     |
| Max questions      | 15 per room; more requires explicit admin approval                          |
| Attached VM        | One VM per room, attached at task level                                     |
| Room type (public) | Challenge (CTF) only; walkthrough rooms are not reviewed for public release |

"No answer needed" is a valid question type and is how reading-focused or reflection tasks
work on the platform. The task description carries the content; the question is a
placeholder that confirms the participant read it.

There is no dedicated reflection, discussion, or open-ended section type. Anything that
functions as reflection is a task with no-answer-needed questions.

## TryHackMe documentation

* [Room creation overview](https://help.tryhackme.com/en/articles/6495805-room-creation-overview)
* [Creating your first room](https://help.tryhackme.com/en/articles/6633511-creating-your-first-room)
* [Building a successful community room](https://help.tryhackme.com/en/articles/8979423-building-a-successful-community-room-with-outc4s7)
* [Making your room public](https://help.tryhackme.com/en/articles/6495828-making-your-room-public)
* [The room review process](https://help.tryhackme.com/en/articles/6495836-the-room-review-process)
* [Managing your rooms](https://help.tryhackme.com/en/articles/6633579-managing-your-rooms)
