# Case File 001 — Two July Incidents. One Failure Pattern.

**CrowdStrike, 19 July 2024 · Azure Front Door, 30 July 2024 — an evidence comparison.**

> **A trigger alone does not explain the blast radius.**

Two of the largest outages of 2024 were filed under opposite stories — a
defective content update, and a DDoS attack. Read side by side, the vendors'
own post-incident reviews describe the same underlying pattern: a privileged
protection system accepted or retained a faulty state, a validation or
containment boundary failed, and the consequence reached far beyond the
initial change or trigger. CrowdStrike propagated faulty content to Windows
sensors because a template expected 21 inputs and the sensor supplied 20, on
a code path the tests had never exercised. Azure Front Door drew traffic
from outside Europe into European DDoS infrastructure because a device that
had been told to stand down kept attracting traffic, and a missing
configuration clause had removed the geographic containment that should have
kept the fault local.

**What this case file does not claim.** It does not claim that one incident
caused the other. It does not attribute either incident to the researcher
whose disclosure record is this repository's founding exhibit. The
assessment carried in the dossier, in its own words: *the researcher
predicted or caused both vendor-specific failures — not established.* The
comparison is a shared failure-amplification pattern drawn from the official
postmortems, and it is presented at exactly that level — no higher.

## The dossier

**[July-2024-One-Failure-Pattern-Dossier-Public.pdf](July-2024-One-Failure-Pattern-Dossier-Public.pdf)**
— Public Edition, 35 pages, A4, 2,073,104 bytes.
SHA-256: `90147cca15cde318ed5756df450a5e408feaf73638f6029d534565cd64ebc330`

Inside, in brief:

- **Executive summary** — the defensible thesis, with the not-claimed list
  printed on the same page, not buried.
- **The Fortnight** — the ordered record, 14 July – 6 August 2024, as a
  designed timeline: the researcher's submissions, both incidents, and the
  vendors' publications, each entry sourced.
- **The Mechanism Map** — the two incidents in five rows (initial condition,
  latent defect, failure in service, reach, recovery tail), with the key
  distinction stated plainly: CrowdStrike had no DDoS trigger; Azure had no
  Falcon content update.
- **Anatomy I & II** — each incident taken apart from its own postmortem.
- **In Their Own Words** — verified, timecoded excerpts from Microsoft's
  official Azure incident retrospective video, cross-checked against the
  written review.
- **The Researcher's Record** — the disclosure chronology, calibrated to
  what the receipts actually establish, including a stated-plainly box of
  what the record does *not* establish.
- **Claims That Survive Review** — every claim in the file, graded:
  supported, incorrect, or not established.
- **What Would Change the Assessment** — the evidence that would move any
  grade, named in advance.
- **Appendices** — the full source register, and the method, tiering and
  redaction standards the file was built under.
- **Annex E** — the load-bearing excerpts from each primary source, with
  verification pointers to the publishers' originals.

## The Proof — the visual guide

**[The-Proof-Jul19-vs-Jul30-Visual-Guide.pdf](The-Proof-Jul19-vs-Jul30-Visual-Guide.pdf)**
— 21 pages, A4, 1,734,330 bytes.
SHA-256: `c1d623a7f50e50becb3ce77477d131b23069045be1d01187a29bafe0df6033fc`

The dossier's companion, built for reading rather than reference: the
fortnight timeline, the seven similarity rows (S1–S7) with their grades
printed at full size, the vendors' key passages as pull-quotes, and the
verdict in three panels — proven, supported, not established. What the
dossier grades, the guide shows; nothing in it is graded higher than
the dossier grades it.

Release: [The Proof — Two July Incidents. One Failure Pattern (Visual
Guide)](https://github.com/CloudyDayExploit/orbit-rerun/releases/tag/the-proof)

## Evidence basis

Every mechanism claim rests on the vendors' own publications, cited in the
dossier's source register: CrowdStrike's preliminary post-incident review
and its external technical root-cause analysis of Channel File 291;
Microsoft's final post-incident review of the 30 July Azure Front Door
incident and its separate review of the 18 July Central US incident;
OpenAI's status record for 17 July; and Microsoft's official retrospective
video, quoted only where the wording was verified against its transcript.

This is the **public edition**: it carries short excerpts and verification
pointers rather than the complete postmortems. Attribution is not a
redistribution licence, and the publishers' terms govern their documents —
so the dossier points every reader to the originals instead of reprinting
them. A private archival edition, including the complete source documents,
is held in the project evidence archive.

## Why it sits in this repository

Orbit Rerun's founding exhibit is a disclosure record that begins on
**25 July 2024** — the researcher's first message to Microsoft, acknowledged
the same evening as case **VULN-131121** — five days before the Azure Front
Door incident and six days after CrowdStrike. This case file is the
analytical companion to that record: the correspondence shows what was
reported and when; the dossier shows what the vendors later established, in
their own words, about the two failures that bracket it. The two are kept
deliberately separate — the timeline is evidence, the comparison is
analysis, and neither is allowed to borrow the other's strength.

- The record: [../../disclosure/TIMELINE.md](../../disclosure/TIMELINE.md)
- The repository: [../../README.md](../../README.md)

## Method

Claims are tiered throughout: **vendor primary sources** first, the
**contemporaneous disclosure record** second, and **labelled inference**
third — never blended. The standing rule of this repository applies to the
dossier itself: corrections append, never rewrite. The dossier's Appendix B
logs seven corrections made across three external review rounds — a clock
label, a headline narrowed to what both postmortems support, a defect
located where the root-cause analysis actually puts it, two recovery
mechanisms separated, a traffic claim scoped to the source's wording, the
annex re-scoped for publication, and a source link verified and restored —
each recorded in the open, in the document it corrected.

---

*Case File 001 · Orbit Rerun · Operated by Cloudy_Day Cybersecurity
(chyp.ai). Data and documents in this repository are published under
CC-BY-4.0; vendor documents remain © their respective publishers and are
quoted in excerpt only.*
