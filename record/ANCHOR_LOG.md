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
   The proof currently carries calendar attestations; the Bitcoin
   confirmation aggregates over the following hours, after which
   `ots upgrade` will be run and committed. When upgraded, the proof
   will show the genesis root existed no later than the stamped
   Bitcoin block — a timestamp nobody, including the operator, can
   backdate.
3. **Cross-posts** — **PENDING-GATE-3.** Dated slots, to be filled with
   real URLs when posted (never backfilled):
   - Cross-post 1 (repo release/announcement): PENDING-GATE-3
   - Cross-post 2 (independent public location): PENDING-GATE-3

## Daily anchors

*From the day the sealing pipeline wraps the live archiver stream,
each day's root gets a line here: day, root, git commit, blockchain
tx/proof, both cross-post URLs, verifier PASS. Missed days are logged
as missed, with the reason — never silently skipped (Runbook, failure
handling).*
