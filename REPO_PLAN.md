# Repo Plan — The Orbit Rerun Drop

*Strategy for the public repository. This plan is written before launch and is
itself part of the package: the drop's credibility strategy, in the open.*

## 1. Repo name

Options considered: `orbit-rerun`, `orbit-record`, `the-record`.

**Recommendation: `orbit-rerun`.** The product's adopted name is Orbit Rerun;
the repo should carry the product's name so every citation, star, and link
compounds one identity. `orbit-record` preserves the earlier naming candidate
and reads well, but running two near-identical names splits the citation graph
the drop exists to build. `the-record` is evocative and unownable — generic in
search, indefensible as an identity. One name, everywhere: **Orbit Rerun**.

## 2. Structure map

```
orbit-rerun/
├── README.md                  ← the drop's front page: the email record leads
├── disclosure/                ← the founding exhibit
│   ├── TIMELINE.md            ← Day 1 → today, gaps included
│   ├── REDACTION_LOG.md       ← what was removed, and why — published, not promised
│   └── correspondence/        ← 30 messages, redacted renderings, Message-ID headed
├── findings/
│   └── STATE_OF_THE_RECORD.md ← findings report: methodology + template, then editions
├── methodology/
│   ├── CLAIM_VS_REALITY.md    ← the two-stream model and discrepancy taxonomy
│   ├── GAP_SCORE.md           ← the published formula
│   └── NEUTRALITY_CHARTER.md  ← the seven rules, incl. the redaction rule
├── sealing/                   ← (from the sealing build) hash-chain + verifier code
├── anchors/                   ← daily Merkle roots, published as they begin
└── LICENSE / LICENSE-DATA     ← see §4 — code and data are separate decisions
```

## 3. Topics / tags

`flight-recorder` · `status-pages` · `incident-history` · `claim-vs-reality` ·
`transparency-log` · `hash-chain` · `merkle-tree` · `sla-evidence` ·
`internet-measurement` · `coordinated-disclosure` · `accountability` ·
`orbit-rerun`

Description line: *"The flight recorder for the internet: what services claimed
vs. what was observed — sealed when it happens, so history can be corrected but
never rewritten."*

## 4. Licensing — two different decisions

**Code** (sealing pipeline, offline verifier, tooling): **MIT vs Apache-2.0.**
Recommendation: **Apache-2.0.** The verifier's entire value is that strangers —
insurers, courts, vendors' own engineers — run it without trusting us; the
Apache patent grant and explicit trademark non-grant are the professional-grade
signals for exactly that audience, at no practical cost over MIT.

**Data & documents** (the archive, timelines, findings): **CC-BY-4.0 vs ODbL.**
- *CC-BY-4.0:* attribution-only. Maximises citation and reuse — journalists,
  researchers, and enterprises can build on the record with a credit line.
  The counter-risk: a commercial actor can enclose derived products without
  sharing back.
- *ODbL:* share-alike for databases. Protects the commons against enclosure,
  but its obligations deter exactly the enterprise/insurer adoption the
  evidence layer (Phase 2, deferred) is built for, and its database-rights
  framing travels poorly outside the EU.
Recommendation: **CC-BY-4.0 for data/documents.** The project's moat is not
legal restriction — it is that the sealed history cannot be backfilled by
anyone, licensed or not. Attribution is the citation engine; openness is the
strategy. *(Recommendation only — the operator decides at launch.)*

## 5. Social-preview image plan

Reuse the established art direction — the monumental door at the foundation
layer, deep blue-black palette, cyan accent, warm light from the doorway (the
Doors 2026 / LinkedIn visual family). One dedicated 1280×640 social-preview
render for this repo: the door, a hash-chain of sealed entries receding like
flight-recorder tape, and the line *"What they claimed. What happened. Sealed."*
No vendor logos, no outage screenshots, no individual's name or face.
`[VERIFY at build: final render asset path]`

## 6. The launch sequence — the strategic core

**The recorder must be public before the incident it will be cited for.** A
flight recorder installed after the crash is a press release. Every element of
the sequence follows from that:

1. **Repo public.** README, disclosure archive, methodology, charter — the
   founding exhibit and the rules, visible before any claim is made on the
   data. The email record leads because it is complete *now*; it proves why
   the recorder must exist using a record nobody sealed at the time.
2. **Methodology and charter visible, and criticised.** The gap-score formula
   and discrepancy definitions sit in public, open to issues, *before* the
   first scored event. A methodology published after its first controversial
   score is worthless.
3. **Sealing anchors live.** The hash chain's daily roots begin publishing
   (git + blockchain + cross-posts). From this date, the record's integrity
   claim is checkable by anyone, and every subsequent day is un-backfillable.
4. **Then: every future outage is a citation event.** When a major service
   fails, the recorder does not announce itself — it simply already has the
   timeline page, sealed from before the vendor's first edit. The drop is not
   the launch post. The drop is being *already there*, permanently, the next
   time the industry goes looking for what actually happened.

The disclosure archive is what makes step 1 land today instead of someday:
the industry does not have to wait for the recorder to accumulate years of
history to see the problem — sixteen months of it is in `disclosure/`,
unavoidable and checkable.

## 7. First 72 hours checklist

- [ ] Repo public with the structure in §2; README rendering checked on
      desktop and mobile
- [ ] Social-preview image set (§5); link unfurls verified
- [ ] Pinned issue: "Methodology v1 — open for criticism" linking
      `methodology/` and inviting reproduction of the gap-score computation
- [ ] Discussion seeds (three, no more): (1) the discrepancy taxonomy — what's
      missing? (2) anchoring design — where else should daily roots live?
      (3) coverage criteria — which services must a flight recorder never miss?
- [ ] The founding-exhibit post on the operator's own channels: one link, the
      Day 1 date, the three dismissal quotes, nothing else — the record makes
      the argument
- [ ] Outreach, in order, to archetypes (no named individuals, no contact
      scraping): internet-measurement researchers; outage/postmortem
      journalists at trade press; SRE/reliability community moderators;
      transparency-log and archival-project maintainers; SLA/vendor-management
      practitioners. Each gets the specific artefact relevant to them —
      methodology, timeline, or charter — never a generic blast
- [ ] Watch issues/PRs with a 24-hour response discipline; corrections, if
      any, appended visibly per the charter — the first correction is a
      credibility event, handle it like one

## 8. What NOT to do

- **No hype thread without evidence links.** Every public claim points at a
  sealed entry, a rendered message, or a published formula — or it doesn't
  ship. The moment this project overclaims once, it becomes the thing it
  records.
- **No unredacted drops, ever.** Not "temporarily," not in a gist, not in a
  screenshot. The redaction rule has no launch-day exception.
- **No engaging vendors' comms teams in the repo.** Vendor responses are
  welcomed through the charter's right-of-reply — sealed and linked — not
  debated in issue threads. The repo is a record office, not a forum fight.
- **No "3 years of data" claim.** The witnessed data record begins
  2026-11-20 and the copy says so. The deep record in this drop is the
  *email* record (Jul 2024 → Dec 2025), and it is labelled as exactly that.
- **No launch timed to someone else's outage.** Publishing the drop *during*
  a live vendor incident to surf it would trade the neutrality charter for a
  news cycle. The sequence in §6 is the opposite: be public first, be cited
  later.
