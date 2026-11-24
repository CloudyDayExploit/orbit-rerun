# The Sealed Record

This directory is the recorder's public evidence: the sealed entries
themselves, not a summary of them.

## Genesis batch (2026-11-24)

- `entries.jsonl` — the genesis stream (`orbit-rerun-genesis`): 777
  canonical entries. 776 are the claim store's rows as they stood at
  seal time — `v5_status` (247), `v5_incidents` (309), `v5_changes`
  (220) — each carrying its original capture timestamp; seq 776 is the
  genesis manifest, which states what this batch is and when it was
  sealed. A sealed snapshot of pre-seal history: the entries are dated
  by their captures, the seal by its own instant. Nothing is backdated.
- `batches/` — hourly Merkle batches (83) over the entries.
- `daily/` — daily root records (2026-11-20 → 2026-11-24), each chained
  to the previous day. The genesis root is the final day's root:
  `5f30399dfa09c2f4300a66bee50200661b47b57951c3e644834a26e6be5227d8`
- `anchors/` — the per-day anchor packages (root, manifest, blockchain
  payload, cross-post texts), plus `ANCHOR_LOG.md` beside this file
  recording where each root has been publicly witnessed — and,
  honestly, where it has not yet.
- `proofs.txt` — worked Merkle inclusion proofs (entry → batch → daily
  root) for seq 0 and seq 776, produced by the independent verifier.

## Verify it yourself

The sealing code and the standalone offline verifier ship with this
project (`sealing/` in the project tree). The verifier shares no code
with the sealer. To check this batch: place `entries.jsonl` under a
store directory as `entries/orbit-rerun-genesis.jsonl` with `batches/`
and `daily/` beside it, and run `verify.py <store>`. PASS means every
hash, link, batch, and daily root recomputes exactly. Altering,
inserting, deleting, or reordering any entry breaks it — the tamper
tests ship with the code; run them.
