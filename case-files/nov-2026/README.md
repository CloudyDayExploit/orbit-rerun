# Case File 002 — One Outage. Four Accounts.

**Microsoft 365 & Exchange Online, 12–13 November 2026 — the "Code Red" outage: a claim-drift case file.**

> **The outage ended. The accounts differ.**

On 12–13 November 2026, Microsoft 365 and Exchange Online suffered the
most customer-impacting outage in Exchange Online's history (incidents
EX1550543 / MO1550821). The mechanism, in Microsoft's final account, is
well documented: a latent Windows lock-contention defect in a
gateway-specific update deployed from July 2026, dormant for more than
three months, triggered when ~14% of gateway capacity was out for
maintenance, a worldwide Teams failover landed at 01:07 UTC, and peak
North America traffic arrived; traffic redistribution then spread the
failure until more than 80% of North America gateway servers were
unresponsive, and the months-old change defeated the rollback machinery,
so the fix went server by server. Microsoft's official window runs
16:20 UTC 12 November → 16:10 UTC 13 November; resolution was declared
14 November, 04:15 UTC.

This case file's subject is not the mechanism. It is the **record about
the mechanism** — four documented revisions between Microsoft's own
successive accounts of the same incident:

1. **The start time.** The public Service Health record opened the
   incident at **10:05 UTC** — a 30 h 05 min outage. Both
   post-incident reviews give **16:20 UTC**, with no explanation for
   the change. 16:20 UTC is Microsoft's own alert time; the final
   review's own timeline shows customer-visible trouble from
   00:25 UTC.
2. **The cause.** During the incident, the framing pointed at a recent
   network configuration change being reverted. The final account
   attributes the outage to a latent defect introduced months earlier.
3. **The capacity.** The ~14% of gateway capacity out of service was,
   in the preliminary review, an unrelated issue from the previous
   day. In the final review, it is planned maintenance.
4. **The mail.** "No mail was lost" survives in the final review's
   summary. Its detail section says no *enterprise* mail was lost,
   with consumer expiries underneath.

Alongside the drift sits an **observation gap**: Orbit Rerun holds no
record of this incident at all. No Microsoft 365 claim feed exists —
Service Health is tenant-gated — and this recorder's sealed capture
began 2026-11-20, after the incident regardless. The largest Exchange
outage in history is absent from the independent record, and this file
documents that absence as a finding about gated-vendor recording.

**What this case file does not claim.** It does not claim Microsoft hid
the outage's length — that is graded **not established**: both windows
are Microsoft-published, and no motive is evidenced. What is established
is that the outage's official length depends on which Microsoft
document you read. It claims no causal link to the incidents of
[Case File 001](../july-2024/). The researcher whose disclosure record
is this repository's founding exhibit **did not predict this incident**,
and nothing in this file suggests otherwise. And ORBIT **did not
observe** this incident — the capture caveat above is part of the file,
not a footnote to it.

## The dossier

**[Case-File-002-One-Outage-Four-Accounts-Dossier.pdf](Case-File-002-One-Outage-Four-Accounts-Dossier.pdf)**
— 38 pages, A4, 3,281,891 bytes.
SHA-256: `24a5460584e02d71b38094a0d7d5baa69396954657cc2d0c88e2e4a4916d3a51`

Inside, in brief:

- **Executive summary** — the claim-drift thesis, with the not-claimed
  list printed on the same page, not buried.
- **The 24 Hours** — the incident on four clocks (first trouble, public
  start, official start, resolution): the disagreeing windows are the
  story.
- **Anatomy of the Failure** — the final review's mechanism taken
  apart: the dormant defect, the three trigger conditions, the
  redistribution cascade, and why recovery had to go server by server.
- **Claim Drift** — the four revisions above, each shown as Microsoft
  first stated it and as Microsoft finally stated it, in a single
  side-by-side table.
- **In Their Own Words** — the internal memo record as reported by
  Reuters (labelled as reporting throughout), and the chief
  executive's public remarks on the outage.
- **The Empty Chair** — the observation gap: what the recorder holds
  (nothing), why, and what that means for recording a gated vendor.
- **The Rhyme, Labelled** — a labelled comparison with Case File 001's
  failure-amplification pattern, with a "where the rhyme stops" box:
  distinct incidents, distinct defects, no causal link.
- **Claims That Survive Review** — every claim in the file, graded:
  supported, revised by the vendor itself, or not established.
- **What Would Change the Assessment** — the evidence that would move
  any grade, named in advance.
- **Appendices** — the source register (with the final review's gating
  stated plainly); the method, tiering and redaction standards; and
  **the Vendor's Own Scorecard**: the final review's 13 next-step
  commitments with their exact target dates (4× CY26 Q4, 5× CY27 Q1,
  4× TBD), laid out to be graded in future editions.
- **Annex E** — the load-bearing excerpts from each source, with
  verification pointers to the originals.

## Evidence basis

Claims are tiered, and the tiers are never blended:

- **Tier 1 — vendor primary.** Microsoft's final post-incident review
  (EX1550543 / MO1550821, 20 November 2026). The review is
  admin-center-gated and is not publicly linkable; the copy this file
  rests on was obtained via a public mirror of the gated PDF and
  cross-checked against four independent renderings, all in agreement.
  The preliminary review (15 November) is public only as fragments,
  and is used only at that strength.
- **Tier 2 — reputable reporting.** Reuters' account of the internal
  "Code Red" memos (the response's own description of itself:
  fragmented tracking, more than 11,000 messages across 11 chats, a
  "fog of war"), and the chief executive's public remarks of
  18 November, including the "bulkheads" line.
- **Tier 3 — the recorder's own store.** A read-only query of
  Orbit Rerun's database documenting the absence: zero Microsoft 365
  rows, for the two reasons given above.

This dossier was built public-safe from birth: it carries short
excerpts and verification pointers rather than complete vendor
documents. Attribution is not a redistribution licence, and the
publishers' terms govern their documents — so the dossier points every
reader to the originals instead of reprinting them. The complete
final review stays in the project evidence archive.

## Why it sits in this repository

Case File 001 examined what two vendors claimed about their failures
against a disclosure record that preceded them. Case File 002 examines
something narrower and, for a recorder, more fundamental: what one
vendor claimed about its own failure, against *itself*, over time —
and what an independent record can and cannot hold when the vendor's
record is gated. The scorecard appendix is the forward commitment:
the vendor published 13 dated promises; future editions of this file
will grade them against the vendor's own dates.

- Case File 001: [../july-2024/](../july-2024/)
- The repository: [../../README.md](../../README.md)

## Method

Claims are tiered throughout: **vendor primary sources** first,
**reputable reporting** second, the **recorder's own documented
record** third, and **labelled inference** last — never blended. The
standing rule of this repository applies to the dossier itself:
corrections append, never rewrite. Where this file's sources conflict
— the final review lists three trigger conditions in its summary and
four factors in its root-cause section; the preliminary and final
reviews frame the containment failure differently — the conflict is
shown in the open and labelled, not silently resolved.

---

*Case File 002 · Orbit Rerun · Operated by Cloudy_Day Cybersecurity
(chyp.ai). Data and documents in this repository are published under
CC-BY-4.0; vendor documents remain © their respective publishers and are
quoted in excerpt only.*
