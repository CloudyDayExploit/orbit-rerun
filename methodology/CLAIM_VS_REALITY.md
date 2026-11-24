# The Claim-vs-Reality Model

*Orbit Rerun methodology, v1 draft. This document defines the objects the recorder
keeps and the rules by which disagreements between them are detected. It is public,
versioned, and applied identically to every tracked service.*

## Why two streams

A status page is a **claim**: a service asserting something about itself. A probe
result is an **observation**: a measurement made by someone the service does not
control. Post-incident history is usually written from claims alone — by the party
that made them. Orbit Rerun keeps both streams, sealed at the moment of capture, and
treats the gap between them as a recorded fact in its own right.

A discrepancy is not an accusation. It is a defined, mechanical relationship between
a claim and an observation, detected by rule, inspectable by anyone.

## The three object types

### Claim

A single, verbatim, timestamped assertion by a service about itself, captured with
provenance:

- source URL or feed it was captured from;
- capture time (multi-source, see `SEALING.md` when published — timestamps are never
  taken from a single clock);
- the raw payload, stored verbatim and hashed;
- the rendered text as a reader would have seen it.

A claim is never summarised at capture time. The raw artefact is the evidence. A
later edit to an incident post is a **new claim** that supersedes the old one — the
old one is never replaced or deleted.

### Observation

A single, timestamped measurement from a source the vendor does not control:

- an HTTP/TLS probe result from a named vantage point;
- a DNS answer set;
- a BGP announcement or withdrawal seen by public collectors;
- a certificate appearing in a public Certificate Transparency log.

Each observation records its method and its vantage point, so any reader can judge
how much weight it carries. One vantage point is an anecdote; corroboration across
independent vantage points is what turns an observation into a discrepancy finding.

### Event

A derived, human-readable grouping: claims and observations for one service aligned
into an incident timeline — first observed anomaly, first claim, claim changes,
observed recovery, claimed recovery.

Events are **views** over sealed entries. They can be re-derived and re-published as
methodology improves without touching the underlying record. **All inference lives
at the Event layer, and is always labelled as inference.** The sealed layer contains
claims and observations only.

## The discrepancy taxonomy

| Type | Definition |
|---|---|
| **False-green** | The service claims "operational" while independent observations show failure or severe degradation beyond a published threshold. |
| **False-red** | The service claims an outage or degradation while observations from all vantage points show normal operation. |
| **Silent edit** | A published claim (incident post, timeline entry, severity) changes or disappears with no new claim acknowledging the change. |
| **Timeline drift** | Claimed start/end times move between revisions, or differ from the first/last observed anomaly by more than a published tolerance. |
| **Stale-active** | An incident remains listed as active/ongoing long after observations show recovery and no updates are posted. |

Each type has a mechanical detection rule: thresholds and tolerances are published
in `GAP_SCORE.md` and in the methodology version in force at the time of detection.
A detection that cannot be reproduced from the sealed entries and the published
rule is withdrawn — by appending a correction, never by editing the original
(see the [Neutrality Charter](NEUTRALITY_CHARTER.md)).

## What this model deliberately does not do

- It does not rate vendors, assign blame, or infer intent. A gap score summarises
  the *record's consistency*, never a company's competence or honesty.
- It does not monitor private systems. The recorder archives public claims and
  coarse public observations — not packet captures, not customer data, not
  anything behind authentication.
- It does not treat any single source — including this project's own probes — as
  ground truth. Cloudflare Radar, vendor status feeds, and aggregators are all
  recorded as what they are: claims or observations with stated provenance.

## Provenance of this document

Adapted from the Orbit Rerun Phase 0 architecture (2026-11-23). Methodology
changes are released as new versions; sealed history is never silently
re-scored under a new version without a visible re-derivation note.
