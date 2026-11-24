# The Gap Score

*Orbit Rerun methodology, v1 draft. The formula below is the public definition.
When it changes, the version changes, the change is announced, and history is
not silently re-scored.*

## What the score is

Each Event (see `CLAIM_VS_REALITY.md`) receives a **Gap Score**: a deterministic
function of its discrepancies, normalised to **0–100**, where **0 means claims and
observations agreed throughout the event**.

The score summarises one thing only: **how far a service's public claims diverged
from independently observed reality during an incident, as preserved in the sealed
record.** It does not measure uptime, severity, competence, or intent. A service
can have a catastrophic outage and a gap score of 0 — if it said so, promptly and
accurately. A service can have a minor blip and a high gap score — if its status
page said "all systems operational" throughout.

## Inputs

For one event, the score is computed from the sealed entries alone:

| Input | What is counted |
|---|---|
| False-green windows | Number of windows, and their total duration, in which the claim was "operational" while corroborated observations showed failure/degradation beyond threshold |
| False-red windows | Number and total duration, symmetrically |
| Silent edits | Count of claim revisions or deletions with no acknowledging claim |
| Timeline drift | Difference, in minutes, between claimed start/end and first/last observed anomaly, beyond the published tolerance |
| Stale-active duration | Time an incident remained listed active after observed recovery with no update |

Corroboration rule: an observation counts toward a false-green or false-red window
only when it is confirmed from at least two independent vantage points, or by one
vantage point plus an independent public signal (BGP, CT, or a second collector).
A single probe never moves a score.

## Properties the formula must keep

1. **Deterministic.** Anyone holding the sealed entry set and this document
   recomputes the identical score.
2. **Monotone in the evidence.** More divergence, longer divergence, or more
   silent edits can never lower a score.
3. **Duration-aware.** A five-minute false-green and a five-hour false-green are
   different facts and score differently.
4. **Vendor-blind.** The function has no per-service parameters. It is applied
   identically to every tracked service — including services operated by this
   project's own operator, whose events are scored and published under the same
   rules.
5. **Versioned.** Scores are published with the methodology version that produced
   them (e.g. "Gap Score 41 · methodology v1"). Re-derivation under a new version
   is published as a new value alongside the old, never as a replacement.

## Worked illustration (hypothetical)

*The following numbers are invented to show the shape of the computation; they are
not a measurement of any real service.*

An incident post claims a degradation from 14:00 to 14:38 (38 minutes). Sealed
observations show the first anomaly at 13:41 and recovery at 15:20. The status page
showed "operational" from 13:41 to 13:58 (a 17-minute false-green window), and the
incident post's start time was edited once, from 13:52 to 14:00, without an
acknowledging update (one silent edit). Timeline drift: start +19 minutes beyond
tolerance, end −42 minutes. The event's gap score reflects all four components —
the outage itself contributes nothing.

## What a high score does and does not say

A high gap score says: *"During this event, the public record and the measurements
diverged, here is the sealed evidence, check it yourself."*

It does not say the vendor lied. Divergence has innocent causes — status tooling
lags, regional scope differences, human update delays. The recorder's job is to
make the divergence **undeniable and inspectable**, not to explain it. Explanations
belong to the vendor, whose response, when offered, is sealed and linked to the
event under the right-of-reply rule in the
[Neutrality Charter](NEUTRALITY_CHARTER.md).

## Status

v1 draft, published with this repository for comment before the first scored
event is released. The exact weights are fixed at v1.0 and recorded in this file's
history; until then, numeric weights in drafts are placeholders and no event has
been scored.
