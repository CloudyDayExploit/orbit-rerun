# Orbit Rerun — The Flight Recorder for the Internet

**On 25 July 2024, a researcher emailed Microsoft about a critical vulnerability.
Five days later, Azure had a major outage. Over the following sixteen months,
Microsoft closed his case as a "non-issue," closed another as "low severity,"
told him "we do not see a correlation… please refrain from submitting this case
to us again," and finally that it was "not able to see evidence." Every one of
those messages survives. They are in this repository, in full, from Day 1 —
because when the only record of an incident belongs to the party that failed,
this is what the record looks like. The internet has no flight recorder. This
project is building one, and this repository is its founding exhibit and its
public record.**

---

## Start with the record: `disclosure/`

The complete email record of the disclosure, excavated from the researcher's
own mailbox — Inbox, Sent, and All Mail, searched by case number, sender, and
subject family back to January 2023 (method in
[disclosure/TIMELINE.md](disclosure/TIMELINE.md#retrieval-method)).

- **30 messages, rendered in full**, 25 July 2024 → 11 December 2025 — every
  acknowledgement, escalation, and dismissal, with Message-IDs preserved so
  any holder of the original mail can verify the renderings.
- **Day 1 is in there.** The first contact — 25 July 2024, 14:29 Pacific,
  subject "Bug" — recovered from Sent mail, with the Bounty Team's reply
  sixteen minutes later.
- **The dismissals are in there, verbatim:**
  > "We have looked through your submissions with multiple teams of engineers
  > and have concluded this as a non-issue." — MSRC, 13 Feb 2025
  >
  > "You have submitted this case to us in the past and our team looked at it
  > extensively. We do not see a correlation with what you are saying and what
  > is reflected in our logs. Please refrain from submitting this case to us
  > again." — MSRC, 18 Sep 2025, one day after the resubmission MSRC itself
  > had suggested
  >
  > "We put a lot of time and energy in your previous submissions and we were
  > not able to see evidence for your submission." — MSRC, 24 Nov 2025
- **So are the gaps.** The portal-submitted report texts that don't survive as
  email, the closure message that was never found, the retrospective known
  only as quoted by the researcher — listed, not reconstructed
  ([TIMELINE.md](disclosure/TIMELINE.md#gaps--referenced-but-not-retrieved)).
- **Redactions are applied and logged** — individuals to roles, all email
  addresses out, the researcher's phone number out; institutions and case
  numbers named, because they are the record. What was removed, and why:
  [disclosure/REDACTION_LOG.md](disclosure/REDACTION_LOG.md).

The case family: **VULN-131121 / MSRC Case 89926 · VULN-136961 · MSRC Case
93814 · VULN-144249 · VULN-148726 · VULN-163108 · VULN-166834** — mapped
together, in the end, by MSRC's own subject line.

**Calibration, because this project's credibility is its only asset:** the
record supports a warning given, a misconfiguration pattern reported, and a
sixteen-month dismissal trail. It does not contain Microsoft attributing the
July 30, 2024 outage to the researcher's report. We don't claim it does. The
claim is the narrow one: *he warned them, they dismissed him, and until now
the only filing system for either fact was theirs.*

## Beneath the exhibit: the instrument

Orbit Rerun records, continuously and under seal, two streams for every
tracked service:

- **Claims** — what the service said about itself: status-page states, every
  revision, incident posts and their edits.
- **Observations** — what independent measurement showed: probes, routing,
  DNS, and certificate signals from vantage points the vendor doesn't control.

Every entry is hashed into an append-only chain the moment it is captured.
Corrections are appended, never edited. The discrepancy between claim and
observation — false-green, false-red, silent edit, timeline drift,
stale-active — is computed by a published formula, not asserted.

**The witnessed record, stated exactly** (store verified by read-only
inspection, 2026-11-24): contemporaneous capture began **2026-11-20** and runs
live — **247 services** under tracking, **309 claimed incidents** and **220
claim transitions** in the first days, **1,148 service-days** of
uptime aggregates. On 2026-11-24 that store was snapshotted into the
genesis seal (777 entries; root `5f30399d…`, see `record/`), and the
first findings run over it is published in
[findings/STATE_OF_THE_RECORD.md](findings/STATE_OF_THE_RECORD.md):
an agreement rate of 98.3%, zero false-green service-days in the
window, 53 stale-active incidents, and the silent-edit finding carried
as *not yet measurable* — in those words. Vendor-claimed incident dates inside that data reach back
to October 2025; those are claim content, not witnessed history, and are
labelled as such wherever they appear. This record is days deep today. It
will be years deep exactly once, and it cannot be backfilled by anyone —
including us. That is the point of starting now, in public.

## Verify it yourself

You do not have to trust the operator of this archive. That is rather the
point.

- **Hash chain.** Every sealed entry carries the hash of the entry before it;
  altering, inserting, or deleting history breaks every subsequent link. The
  sealing code and an **offline verifier** live in this project
  (`sealing/` — chain validation, Merkle proofs, anchor checking; the
  pipeline's tamper tests — byte-flip, truncation, forgery, reorder — all
  fail verification, and you can run them).
- **Anchors.** Daily Merkle roots are published to witnesses the operator
  doesn't control (public git, a public blockchain transaction, independent
  cross-posts), so the chain cannot be quietly rewritten even by us.
  The anchor log opens with the genesis seal of 2026-11-24 — genesis
  root `5f30399d…` (full root and witness status in
  [record/ANCHOR_LOG.md](record/ANCHOR_LOG.md), which also records,
  honestly, which anchors are still pending).
- **The email archive.** Each rendering carries its source message's date,
  subject, and Message-ID. Anyone who lawfully holds the original mail can
  diff our rendering against it; the only differences are the redactions
  logged in [REDACTION_LOG.md](disclosure/REDACTION_LOG.md).
- **The methodology.** Discrepancy definitions and the gap-score formula are
  published ([methodology/](methodology/)) and versioned, so any finding in
  [findings/](findings/) can be recomputed from the sealed entries by a
  stranger.

## The neutrality charter (summary)

Published in full at [methodology/NEUTRALITY_CHARTER.md](methodology/NEUTRALITY_CHARTER.md):

1. Methodology is public and versioned.
2. Corrections are appended, never edited — including ours.
3. No pay-for-placement, ever. No vendor can buy a gentler score or a removal.
4. Evidence buyers buy exports, never influence.
5. Funding is disclosed in aggregate.
6. Claims are recorded verbatim; inference is labelled as inference; vendors
   hold a sealed, linked right of reply.
7. The recorder records itself, gap scores included.

And standing over all of it, the redaction rule: **sensitive data is always
redacted from public view** — individuals, addresses, credentials, private
details. When in doubt, redact.

## How to cite the record

Cite the artefact, not the summary: the message file and its Message-ID for
the disclosure archive; the event's timeline page and its sealed entry range
for incidents; the report edition and methodology version for findings. If
you cite a number from this repository, link the page that derives it.

## Findings

[findings/STATE_OF_THE_RECORD.md](findings/STATE_OF_THE_RECORD.md) — the
flagship findings report. Its methodology and the exact queries behind it are
published now; its numbers are filled only from the sealed store, and its
known limitations (history depth, revision capture, observation granularity)
are printed in the report itself, not discovered by its critics.

## Licenses (summary)

Code (sealing, verifier, tooling): **Apache-2.0** *(recommended; see
REPO_PLAN.md §4)*. Data and documents: **CC-BY-4.0** *(recommended)* — the
record is meant to be cited; attribution is the price, and the seal, not the
license, is the moat. Full reasoning, including the ODbL alternative, in
[REPO_PLAN.md](REPO_PLAN.md).

## Links

- **chyp.ai** — ORBIT, the observatory this recorder grows out of
- **Orbit Rerun on chyp.ai** — public incident timelines `[VERIFY at launch: URL]`
- **Doors 2026 Server Edition** — the same doctrine (verify, checkpoint,
  never trust commanded state) applied to a single machine: demo and manual
  via chyp.ai

## Case files

- **[Case File 001 — Two July Incidents. One Failure Pattern.](case-files/july-2024/)**
  — CrowdStrike (19 July 2024) and Azure Front Door (30 July 2024) read side
  by side from the vendors' own postmortems: one failure-amplification
  pattern, graded claim by claim, sitting on this record's founding exhibit.
- **[Case File 002 — One Outage. Four Accounts.](case-files/nov-2026/)**
  — The Microsoft 365 / Exchange Online outage of 12–13 November 2026 read
  against Microsoft's own successive accounts of it: four documented claim
  revisions, an observation gap where the independent record should be,
  and the vendor's 13 dated commitments held for grading.

---

*Orbit Rerun is operated by Cloudy_Day Cybersecurity (chyp.ai). The founding
exhibit is the operator's own disclosure record, published by the researcher
himself. Institutions named in the record are named as parties to documented
correspondence and sealed observations; a vendor's reply to any event is
sealed and linked, unedited, under the charter's right-of-reply rule.*
