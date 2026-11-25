# Anchor Log — Orbit Rerun

*One line per anchored root, per the Anchor Runbook. The anchors are the
evidence; this log is bookkeeping that points at them.*

## Genesis seal — 2026-11-24

The record's first sealed batch: a snapshot of the claim store
(`v5_status` 247 rows, `v5_incidents` 309 rows, `v5_changes` 220 rows)
plus a genesis manifest entry — **777 entries**, stream
`orbit-rerun-genesis`, sealed **2026-11-24** (seal instant recorded in
the manifest entry itself). Entries carry their original capture
timestamps (witnessed capture 2026-11-20 → 2026-11-24); the seal is
dated when it happened. Nothing is backdated.

Daily roots (each chains to the previous day; the genesis root is the
final day's root):

| Day | Daily root |
|---|---|
| 2026-11-20 | `1306cd78ee4a444d51670ce24241ac86f2e9154de17c48530a2fd6fbd729b073` |
| 2026-11-21 | `cf0a98620fc167830fab3722507814a2e993fe04276cc5d51c3c8dba6b18392b` |
| 2026-11-22 | `142f37394b97e4c887faaaab13e61bcd6f394f34dc2568fa738780b8bb00a0d5` |
| 2026-11-23 | `690bd0ef3133ccb74fa6cf2cc266a3b71e48b5f8431ae05fc1e120458adbf2ec` |
| 2026-11-24 | `5f30399dfa09c2f4300a66bee50200661b47b57951c3e644834a26e6be5227d8` |

**Genesis root: `5f30399dfa09c2f4300a66bee50200661b47b57951c3e644834a26e6be5227d8`**

Verification at seal time: `verify.py` — **PASS** (777 entries, 83
hourly batches, 5 daily roots, chain intact). Inclusion proofs for
entry seq 0 and the genesis manifest (seq 776) are in `proofs.txt`.

### Anchor status

1. **Public git** — **LIVE.** This repository's history carries the
   genesis batch and this log. Repo URL:
   https://github.com/CloudyDayExploit/orbit-rerun (created
   2026-11-24). The history was mirrored to GitHub on 2026-11-24 via
   the Git Data API; every commit SHA on the remote matches the
   locally sealed history byte for byte. Mirrored head at push time:
   `eab1184e516a1633d315001518b12a9315b40718`.
2. **Blockchain timestamp (OpenTimestamps)** — **STAMPED
   2026-11-24** (proof: `anchors/2026-11-24/daily_root.txt.ots`,
   committed with this log). Two earlier attempts the same day
   returned 0 attestations inside the client's 5-second default
   timeout; the successful stamp used a 60-second calendar timeout.
   The proof carried calendar attestations while the Bitcoin
   confirmation aggregated; **`ots upgrade` completed 2026-11-24**
   ("Timestamp complete") and the proof now embeds two independent
   **Bitcoin block header attestations — blocks 977388 and 977390** —
   proving the genesis root existed no later than those blocks: a
   timestamp nobody, including the operator, can backdate. (One
   calendar's attestation was still pending at upgrade time; the two
   completed Bitcoin attestations are independent of it. Full header
   verification is offline-checkable by anyone running a Bitcoin
   node.)
3. **Cross-posts** — dated slots, filled with real URLs when posted
   (never backfilled):
   - Cross-post 1 (repo release/announcement): **LIVE 2026-11-24** —
     GitHub Release "State of the Record — Edition 1 · Genesis Seal":
     https://github.com/CloudyDayExploit/orbit-rerun/releases/tag/edition-1
   - Cross-post 2 (independent public location): PENDING

## Daily anchors

*From the day the sealing pipeline wraps the live archiver stream,
each day's root gets a line here: day, root, git commit, blockchain
tx/proof, both cross-post URLs, verifier PASS. Missed days are logged
as missed, with the reason — never silently skipped (Runbook, failure
handling).*

## Publications

*Repository releases that carry documents beyond the sealed record
itself — publication anchors, logged when they happen. Cross-post 2
above remains pending; no entry here fills it.*

- **2026-11-25 — The Proof (visual guide; Case File 001 companion).**
  Release: https://github.com/CloudyDayExploit/orbit-rerun/releases/tag/the-proof
  Document: `case-files/july-2024/The-Proof-Jul19-vs-Jul30-Visual-Guide.pdf`
  — 21 pages, 1,734,330 bytes, SHA-256
  `c1d623a7f50e50becb3ce77477d131b23069045be1d01187a29bafe0df6033fc`.
  Publication commit: `78fa0faf895528a65260a806dd02bff881e085d3`.
- **2026-11-25 — Doors 2026 GUI Edition User Guide (Beta 2).**
  Release: https://github.com/CloudyDayExploit/orbit-rerun/releases/tag/doors-2026-beta2-guide
  Document: `doors-2026/Doors-2026-GUI-Edition-User-Guide-Beta2.pdf`
  — 28 pages, 1,611,391 bytes, SHA-256
  `713f402ffbcd8977c1fd2a8907a9d304b5d16a0f050ebb931101d89a1176b250`.
  Publication commit: `f232ef6bee4f8768a1548d8dd75cbce04ce58d78`.
  Interim-home decision (2026-11-25): the guide publishes here now;
  the Beta 2 ISO is not released — it launches on Internet Archive
  with this guide after the real-hardware verification pass.
