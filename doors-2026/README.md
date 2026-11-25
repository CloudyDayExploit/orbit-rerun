# Doors 2026 — GUI Edition (Beta 2)

**The console era is over.**

Doors 2026 is a hardened Linux-based operating system built on the
Layer 0 doctrine: security begins at the chip, and every change passes
a gate — checkpointed before, health-checked after, rolled back
automatically when it fails, and written to a ledger either way.

Beta 2 is the GUI edition: a full desktop from the first boot — a
themed boot menu, the Layer 0 boot ceremony, a login screen that shows
the machine's attestation verdict before sign-in, an original startup
chime, and Doors Control, the native app where checkpoints, changes
and the ledger live. The gate underneath is Beta 1's, unchanged.

## The guide

**[Doors-2026-GUI-Edition-User-Guide-Beta2.pdf](Doors-2026-GUI-Edition-User-Guide-Beta2.pdf)**
— 28 pages, A4, 1,611,391 bytes.
SHA-256: `713f402ffbcd8977c1fd2a8907a9d304b5d16a0f050ebb931101d89a1176b250`

Release: [Doors 2026 — GUI Edition User Guide (Beta 2)](https://github.com/CloudyDayExploit/orbit-rerun/releases/tag/doors-2026-beta2-guide)

## Status — stated plainly

The guide is published here first, as its interim public home. **The
Beta 2 ISO is not yet released.** It launches on Internet Archive,
with this guide, after the real-hardware verification pass.

Verified from the shipped ISO: themed GRUB and the Plymouth Layer 0
ceremony render on BIOS and UEFI (the guide prints the real captures,
labelled as captures); doors-gate exercised from the shipped layer,
including a checkpoint → change → rollback cycle with the /etc diff
empty.

Not yet verified: the live desktop session on real hardware (the
emulation sandbox cannot finish starting the GNOME session — the
stock base fails identically there), install-to-disk for the GUI
edition, and Secure Boot.

ISO (not yet released): `doors-2026-beta2-amd64.iso`, 6,289,901,568 bytes.
SHA-256: `6b4808960352ef99d1676e6aec58d9d968e2f45c6bcc69b887ae5f4a864f70df`

Beta 1 (Server Edition) is live on Internet Archive:
https://archive.org/details/doors-2026-server-beta1

---

*Doors 2026 · Cloudy_Day Cybersecurity (chyp.ai). This guide is
published under CC-BY-4.0.*
