# State of the Record — Findings Report

*Orbit Rerun's flagship findings publication. Edition 1 is the first full
run of the queries published in §3. The template for this report — and its
methodology — were published before the numbers existed, so the method
could be criticised before it produced conclusions. Every number below
traces to a query result from the run; the raw result sets and the
computation script (`compute_q6.py`, shipped beside this report) are the
evidence.*

**Report version:** Edition 1 · **Methodology:** v1 draft
(../methodology/) · **Data as of:** 2026-11-24T08:32:23Z (the latest
collector check in the snapshot) · **Witnessed window:**
2026-11-20T09:22:47Z → 2026-11-24T08:32:23Z

---

## 0. What this report measures

The gap between what tracked services **claimed** about their own availability
and what independent observation **showed** — counted, timed, and classified by
the discrepancy taxonomy (false-green, false-red, silent edit, timeline drift,
stale-active). The report covers the recorder's own archive only: claims and
observations captured contemporaneously by ORBIT's collectors. It does not
scrape together a history the recorder did not witness. (From this edition
forward, the archive is also sealed under the hash chain — see the genesis
seal in `../record/`. The window below predates the seal and is therefore
labelled, per §4, snapshotted-not-sealed history.)

**The archive's honest starting line** (verified against the store by
read-only schema inspection, 2026-11-24, and by this run):

- Contemporaneous capture begins **2026-11-20** and runs live. That is the
  depth of the witnessed record today — days, not years — and this report will
  say so in every edition until the record has earned a longer sentence.
- At this run: **247 services** under current-state tracking; **309 claimed
  incidents**; **220 claim transitions** (status flips) recorded since
  2026-11-20 09:22 UTC; **1,148 service-days** of uptime aggregates;
  **162 assembled events**, of which 69 are outage events.
- Vendor-claimed incident start dates reach back to **2025-10-27** — dates
  *asserted inside claims*, first captured 2026-11-20. They are claim content,
  never observation history, and are reported in a separate, labelled column
  wherever used.

**How this edition classifies days (stated here, applied by the shipped
script).** Observation tiers per service-day, from Q4: *clean* (0 bad
checks), *degraded* (0 < bad/checks < 0.5), *failure* (bad/checks ≥ 0.5).
Claim state per service-day is reconstructed from the Q2 transition stream
(the state before a service's first recorded transition is that
transition's from-indicator; services with no transitions hold their Q3
indicator). Day-level classes are computed over **complete UTC days only**
(2026-11-20 → 2026-11-23; 902 service-days): the snapshot day,
2026-11-24, is partial — its uptime aggregate is still accumulating — and
is used only as the reference point for stale-active. All day-level
findings are **single-collector, day-granularity candidate windows**:
the methodology's corroboration rule (two independent vantage points, or
one plus an independent public signal) cannot be met by daily aggregates
alone, so this edition publishes no corroborated false-green/false-red
*findings* — it publishes the measured windows and says what they are.

## 1. Headline findings

1. **False-green exposure: 0 service-days.** Across the four complete
   days, the observation layer recorded **95 failure-tier service-days**
   and **41 degraded service-days** — and on every one of them, the
   claim side carried a matching signal (an open incident or a
   non-green indicator). At the strong tier (observation failure,
   claim green all day) and at the weak tier (observation degraded,
   claim green all day), the count is **zero**. Service-*minutes* are
   not measurable at daily observation granularity and are not claimed;
   service-days are the honest unit until probe-level storage lands.
2. **Silent edits: not yet measurable.** The current store does not
   capture incident-post text revisions (see §4 and Q7), so this
   finding is carried as *not yet measurable*, in those words. What
   the recorder *did* witness is the claim-revision stream at indicator
   level: **220 claim transitions across 72 services**. This edition
   also records a neighbouring, mechanically defined class the window
   made visible: **54 open-incident / green-indicator service-days** —
   days on which a service had an incident post open while its own
   headline indicator read operational the entire day (bunny: 4 days;
   mongodb: 4; cashapp, gemini-x, godaddy, grafana: 3 each). The two
   claim streams disagreeing with each other is a fact of the record,
   whatever either of them says about reality.
3. **Timeline drift.** 61 of the 69 assembled outage events matched a
   claimed incident of the same service within 48 hours. Across those
   matches, the median difference between the vendor-claimed incident
   start and the collector's first event assembly is **−4.8 minutes**
   (claims and collector assembly track closely, as expected where the
   event's source is the status feed itself). The maximum absolute
   drift is **2,032.9 minutes (≈33.9 hours)**. Only **2** matched
   events carry an independent (non-status-feed) source; their drifts
   are **+2,032.9 minutes** (Anthropic, "Elevated errors for multiple
   models" — the vendor-claimed start falls ~33.9 hours *after* the
   event was first assembled from independent signals) and **−5.1
   minutes** (Bitbucket). With n = 2, the independent-source figure is
   reported as two data points, not a statistic.
4. **Stale-active: 53 incidents.** 53 claimed incidents — first seen by
   the recorder at least 24 hours before the snapshot, on services
   whose checks have been clean for at least one full day since their
   last bad check — were still listed in an active status at the
   snapshot (in_progress: 21; monitoring: 18; investigating: 10;
   ongoing: 3; identified: 1). The longest-running examples are named
   in §2.1. "Monitoring" is a vendor status, not a resolution; the
   record reports the status verbatim and the observed cleanliness
   beside it, and draws no conclusion about which is right.
5. **The agreement rate: 98.3%.** Of 173 claimed incidents with a
   non-maintenance impact and observation coverage of their claimed
   span, **170 were corroborated** (at least one bad-check day inside
   the claimed span, or a matched assembled outage event). The 3
   uncorroborated incidents are named in §2.2. The report leads with
   the gap, but it publishes the agreement rate beside it, every time.
   A record that only publishes divergence is advocacy, not
   measurement.

## 2. Per-service tables

For each tracked service with any activity in the window: incidents in
window; claim transitions; observed bad days (any bad checks, complete
days); false-green and false-red days under the rules of §0;
open-incident / green-indicator days; stale-active count. Services are
listed alphabetically. There is no ranking table and no "worst vendor"
framing: the table summarises record consistency, not corporate
character. **Gap Scores are not published in this edition**: the
methodology v1 weights are placeholders until v1.0 (see
../methodology/GAP_SCORE.md), so the table publishes the score's
*inputs* — the discrepancy counts themselves — and no derived score.
The full machine-readable table (all 246 services with uptime coverage)
is `per_service.csv` in the run's raw result sets.

| Service | Incidents | Transitions | Obs. bad days | False-green days | False-red days | Open-incident / green-indicator days | Stale-active incidents |
|---|---|---|---|---|---|---|---|
| aiven | 1 | 0 | 0 | 0 | 0 | 0 | 0 |
| akamai | 4 | 1 | 4 | 0 | 0 | 0 | 1 |
| alchemy | 4 | 0 | 4 | 0 | 0 | 0 | 0 |
| anthropic | 2 | 3 | 2 | 0 | 0 | 0 | 0 |
| authorizenet | 1 | 1 | 0 | 0 | 0 | 0 | 0 |
| aws | 2 | 1 | 2 | 0 | 0 | 2 | 0 |
| bandwidth | 2 | 4 | 2 | 0 | 0 | 1 | 0 |
| baseten | 1 | 2 | 0 | 0 | 0 | 0 | 0 |
| bigcommerce | 1 | 2 | 2 | 0 | 0 | 0 | 1 |
| bitbucket | 1 | 2 | 1 | 0 | 0 | 0 | 0 |
| bunny | 3 | 2 | 0 | 0 | 0 | 4 | 0 |
| canva | 1 | 4 | 1 | 0 | 0 | 1 | 1 |
| cashapp | 1 | 1 | 1 | 0 | 0 | 3 | 1 |
| chargebee | 2 | 1 | 2 | 0 | 0 | 2 | 0 |
| circleci | 2 | 5 | 3 | 0 | 0 | 2 | 0 |
| clerk | 1 | 2 | 1 | 0 | 0 | 0 | 0 |
| cloudflare | 8 | 0 | 5 | 0 | 0 | 0 | 0 |
| cloudflare-dns | 5 | 0 | 5 | 0 | 0 | 0 | 0 |
| cloudflare-zt | 5 | 0 | 5 | 0 | 0 | 0 | 0 |
| cloudfront | 2 | 1 | 2 | 0 | 0 | 2 | 0 |
| codecov | 0 | 2 | 1 | 0 | 0 | 0 | 0 |
| coinbase | 2 | 0 | 0 | 0 | 0 | 0 | 0 |
| confluence | 1 | 2 | 1 | 0 | 0 | 0 | 0 |
| convex | 1 | 2 | 1 | 0 | 0 | 1 | 1 |
| cryptocom | 7 | 0 | 0 | 0 | 0 | 0 | 0 |
| cursor-ide | 2 | 2 | 1 | 0 | 0 | 0 | 1 |
| customerio | 5 | 0 | 4 | 0 | 0 | 0 | 0 |
| dialpad | 1 | 2 | 2 | 0 | 0 | 0 | 0 |
| easypost | 6 | 0 | 4 | 0 | 0 | 0 | 0 |
| elastic | 1 | 1 | 5 | 0 | 0 | 0 | 0 |
| fireworks | 5 | 10 | 3 | 0 | 0 | 0 | 0 |
| fivetran | 3 | 4 | 2 | 0 | 0 | 1 | 1 |
| flyio | 1 | 2 | 1 | 0 | 0 | 1 | 1 |
| gandi | 4 | 14 | 0 | 0 | 0 | 0 | 0 |
| gemini-x | 3 | 5 | 1 | 0 | 0 | 3 | 0 |
| godaddy | 1 | 2 | 1 | 0 | 0 | 3 | 1 |
| gotomeeting | 1 | 4 | 1 | 0 | 0 | 0 | 0 |
| grafana | 1 | 2 | 1 | 0 | 0 | 3 | 1 |
| hashicorp | 2 | 1 | 1 | 0 | 0 | 2 | 0 |
| hotjar | 1 | 0 | 0 | 0 | 0 | 0 | 0 |
| imgur | 0 | 0 | 4 | 0 | 0 | 0 | 0 |
| imperva | 6 | 14 | 2 | 0 | 0 | 1 | 2 |
| incidentio | 1 | 2 | 1 | 0 | 0 | 0 | 0 |
| jfrog | 5 | 0 | 0 | 0 | 0 | 0 | 0 |
| jira | 1 | 2 | 1 | 0 | 0 | 0 | 0 |
| klarna | 5 | 8 | 1 | 0 | 0 | 0 | 3 |
| kraken | 17 | 0 | 5 | 0 | 0 | 0 | 0 |
| linode | 2 | 4 | 2 | 0 | 0 | 2 | 0 |
| login-gov | 1 | 0 | 0 | 0 | 0 | 0 | 0 |
| loom | 5 | 1 | 4 | 0 | 0 | 0 | 0 |
| mailgun | 1 | 0 | 0 | 0 | 0 | 0 | 0 |
| mastodon-social | 1 | 1 | 2 | 0 | 0 | 2 | 0 |
| mistral | 1 | 1 | 2 | 0 | 0 | 2 | 0 |
| modal | 2 | 1 | 0 | 0 | 0 | 0 | 0 |
| mongodb | 1 | 0 | 0 | 0 | 0 | 4 | 0 |
| mux | 1 | 2 | 1 | 0 | 0 | 1 | 1 |
| netlify | 1 | 2 | 1 | 0 | 0 | 0 | 0 |
| openai | 1 | 2 | 1 | 0 | 0 | 0 | 0 |
| ovhcloud | 4 | 4 | 5 | 0 | 0 | 0 | 0 |
| pantheon | 1 | 0 | 0 | 0 | 0 | 0 | 0 |
| patreon | 1 | 2 | 1 | 0 | 0 | 1 | 1 |
| pinecone | 1 | 1 | 2 | 0 | 0 | 0 | 0 |
| pingidentity | 1 | 0 | 0 | 0 | 0 | 0 | 0 |
| postman | 1 | 2 | 0 | 0 | 0 | 0 | 0 |
| quay | 1 | 2 | 1 | 0 | 0 | 0 | 0 |
| rippling | 1 | 2 | 1 | 0 | 0 | 0 | 0 |
| route53 | 2 | 1 | 2 | 0 | 0 | 2 | 0 |
| salesforce | 3 | 4 | 2 | 0 | 0 | 2 | 3 |
| saucelabs | 1 | 2 | 0 | 0 | 0 | 0 | 0 |
| scaleway | 11 | 0 | 5 | 0 | 0 | 0 | 0 |
| sendgrid | 27 | 2 | 5 | 0 | 0 | 0 | 0 |
| sentinelone | 1 | 2 | 0 | 0 | 0 | 0 | 0 |
| sentry | 1 | 2 | 1 | 0 | 0 | 0 | 0 |
| shippo | 11 | 3 | 3 | 0 | 0 | 0 | 10 |
| shipstation | 4 | 0 | 0 | 0 | 0 | 3 | 0 |
| shopify | 2 | 4 | 1 | 0 | 0 | 0 | 0 |
| sinch | 7 | 2 | 4 | 0 | 0 | 0 | 0 |
| smartsheet | 1 | 2 | 1 | 0 | 0 | 0 | 0 |
| snowflake | 1 | 2 | 1 | 0 | 0 | 2 | 1 |
| snyk | 1 | 2 | 1 | 0 | 0 | 0 | 0 |
| supabase | 2 | 1 | 2 | 0 | 0 | 0 | 0 |
| tailscale | 1 | 2 | 2 | 0 | 0 | 0 | 0 |
| telnyx | 4 | 1 | 0 | 0 | 0 | 0 | 0 |
| together | 0 | 2 | 1 | 0 | 0 | 0 | 0 |
| trello | 1 | 3 | 1 | 0 | 0 | 0 | 0 |
| twilio | 27 | 2 | 5 | 0 | 0 | 0 | 0 |
| vonage | 21 | 25 | 3 | 0 | 0 | 1 | 11 |
| wasabi | 2 | 4 | 0 | 0 | 0 | 0 | 0 |
| wise | 2 | 1 | 4 | 0 | 0 | 0 | 0 |
| workos | 2 | 4 | 2 | 0 | 0 | 0 | 0 |
| xero | 6 | 3 | 4 | 0 | 0 | 0 | 5 |
| zapier | 1 | 0 | 0 | 0 | 0 | 0 | 0 |
| zoom | 7 | 4 | 1 | 0 | 0 | 0 | 6 |

### 2.1 Stale-active — longest-running examples

The twelve earliest first-seen of the 53 stale-active incidents (§1.4).
The full list is in the run's raw result sets (`q6_analysis.json`).

- **vonage** — "Japan SMS - Delivery degradation affecting NTT DoCoMo Network" (status: monitoring; vendor-claimed start 2026-11-20T08:56:22Z; first seen by the recorder 2026-11-20T10:58:10Z)
- **godaddy** — "Voice Support Services Degraded" (status: investigating; vendor-claimed start 2026-11-20T10:52:23Z; first seen by the recorder 2026-11-20T11:09:04Z)
- **vonage** — "Belgium SMS - Delivery degradation towards Proximus network" (status: monitoring; vendor-claimed start 2026-11-20T08:59:06Z; first seen by the recorder 2026-11-20T11:19:59Z)
- **vonage** — "China SMS - Delivery degradation affecting multiple networks" (status: monitoring; vendor-claimed start 2026-11-20T07:09:20Z; first seen by the recorder 2026-11-20T11:35:53Z)
- **salesforce** — "coreService on USA258S" (status: ongoing; vendor-claimed start 2026-11-20T13:32:44Z; first seen by the recorder 2026-11-20T14:03:22Z)
- **grafana** — "Plugin installs and updates from the plugin catalog may fail" (status: monitoring; vendor-claimed start 2026-11-20T11:52:24Z; first seen by the recorder 2026-11-20T14:32:50Z)
- **zoom** — "Zoom Team Chat Update" (status: in_progress; vendor-claimed start 2026-11-05T15:01:42Z; first seen by the recorder 2026-11-20T14:58:41Z)
- **vonage** — "Belgium SMS - Delivery degradation towards Proximus network" (status: investigating; vendor-claimed start 2026-11-20T12:35:55Z; first seen by the recorder 2026-11-20T15:03:26Z)
- **cashapp** — "Withdrawal Issue" (status: monitoring; vendor-claimed start 2026-11-18T16:55:29Z; first seen by the recorder 2026-11-20T15:05:37Z)
- **salesforce** — "Customer360Audiences on ARE2S, ARE4S, ARE6, ARE12…" (status: ongoing; vendor-claimed start 2026-11-20T11:52:40Z; first seen by the recorder 2026-11-20T15:07:58Z)
- **zoom** — "Zoom Phone Maintenance (Sydney Data Center): November 20, 2026" (status: in_progress; vendor-claimed start 2026-10-29T15:07:22Z; first seen by the recorder 2026-11-20T16:13:34Z)
- **akamai** — "Edge Delivery Issues in Singapore and Japan Regions" (status: monitoring; vendor-claimed start 2026-11-17T17:40:53Z; first seen by the recorder 2026-11-21T00:00:20Z)

### 2.2 Uncorroborated claimed incidents

The 3 claimed incidents (§1.5) with no bad-check day inside their
claimed span and no matched assembled event. Uncorroborated is a
statement about this record's observation layer — daily aggregates from
a single collector — not a finding that nothing happened:

- **bunny** — "Crypto Payment Failures" (impact: minor; status: investigating)
- **mongodb** — "Impaired Cluster operations in AWS me-central-1 and AWS me-south-1" (impact: major; status: monitoring)
- **shipstation** — "Important Change: DDU Shipments to Germany No Longer Accepted" (impact: minor; status: investigating)

## 3. The exact queries behind this report

*Content-level queries against the live store. These were specified
here, in public, before they were run — the report's methods were not
reverse-engineered from its conclusions.*

- **Q1 — Claim inventory.** All rows of the incidents table for the window:
  service, claimed impact, claimed status, vendor-stated start/resolve times,
  first-seen time. (Establishes the claim set; vendor-stated times are used
  only as claim content.)
- **Q2 — Transition stream.** All rows of the claim-transitions table ordered
  by service and timestamp: from-indicator → to-indicator with descriptions.
  (The false-green/false-red windows are computed from Q2 joined against Q4.)
- **Q3 — Current-state snapshot set.** The current-status table's per-service
  indicator, open-incident count, last-change and last-check timestamps, and
  fetch-error field. (Snapshot provenance for the report's "as of" claims.)
- **Q4 — Observation aggregates.** The uptime table's per-service per-day
  checks run, bad checks, and worst state, for every day in the window.
  (Corroboration layer for discrepancy windows; daily granularity is a known
  limitation until probe-level storage lands — stated in the report, not
  footnoted away.)
- **Q5 — Event assembly.** The signals/events tables: assembled events with
  first/last seen, confidence, and linked sources, joined to Q1 by service and
  time window. (Supplies the event layer; all inference labelled.)
- **Q6 — Gap-score computation.** For each event from Q5: the discrepancy
  inputs per the published formula (false-green/red minutes from Q2×Q4, drift
  from Q1×Q5, stale-active from Q1×Q4). Deterministic; the computation script
  ships with the report.
- **Q7 — Revision deltas (future).** Once the revision watcher is live:
  successive incident-post texts per incident, diffed, with capture hashes.
  (Silent-edit counts cannot be produced before this exists. Any edition of
  this report published earlier carries the silent-edit finding as "not yet
  measurable," in those words.)

**Run note — Edition 1 (2026-11-24).** Q1–Q6 were run exactly as
specified, SELECT-only, against the tables named above; no query needed
a corrective fix (the specifications matched the store's schema as
inspected). Q7 was not run — the revision capture it reads does not
exist yet. Two classification rules were made explicit for this edition
and are stated in §0 and in the shipped script: day-level classes use
complete UTC days only (the snapshot day is partial), and
open-incident / green-indicator days are reported as their own class
rather than folded into false-red. Q6's deterministic inputs are
published in §1/§2; numeric Gap Scores were **not** computed, because
the methodology v1 weights remain placeholders until v1.0 — inventing
weights to produce a score would be exactly the kind of number this
report exists to refuse. Raw result sets (JSON + CSV) and
`compute_q6.py` accompany the run.

## 4. Known limitations of the current store

Stated in the report, not discovered by critics:

1. **History depth.** Witnessed capture begins 2026-11-20. Findings describe
   the window actually witnessed — no more.
2. **Current-state overwrite.** The live status table mutates in place; the
   transition log is what preserves claim history. History before the
   genesis seal (2026-11-24) is snapshotted, not sealed, and this edition
   is labelled that way; editions after the seal work from sealed
   entries.
3. **No incident-text revisions yet.** Silent edits *inside* an incident post
   are not captured by the current store (see Q7). Indicator-level flips are.
4. **Observation granularity.** Uptime evidence is per-day aggregates without
   stored vantage-point identity. Discrepancy windows are therefore computed
   at the granularity the evidence supports, and the corroboration rule in the
   methodology is applied conservatively.
5. **Single-clock timestamps** on current claim/observation rows (collector
   time). Multi-source time is a sealing-pipeline property, applied from the
   seal forward.

## 5. How to cite this report

Cite the edition, the window, and the methodology version — and link the
event's public timeline page, not this summary, wherever an individual
incident is referenced. The summary is a view; the sealed timeline is the
evidence.

## 6. Corrections

Corrections to any edition are appended to that edition as dated notes; the
original text stands. If a number in §1 is ever wrong, the correction will be
more visible than the number was.
