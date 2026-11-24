#!/usr/bin/env python3
"""Orbit Rerun — State of the Record, first full run: Q6 computation.

Deterministic. Inputs are the raw Q1-Q5 result sets in this directory
(pulled SELECT-only from orbit-db). Every rule applied here is stated in
findings/STATE_OF_THE_RECORD.md §1/§2. No Gap Scores are computed:
methodology v1 weights are placeholders until v1.0 (see GAP_SCORE.md);
this script computes the published discrepancy *inputs* and the headline
measures the template defines.

Definitions (UTC days; window = witnessed capture window):
- Claim state per service-day is reconstructed from Q2 transitions
  (state before a service's first transition = that transition's
  from_ind; services with no transitions hold their Q3 indicator, set
  at Q3.changed_at). A day is claim-bad if the indicator was in
  {minor, major, critical} at any point that day, or a Q1 incident with
  impact in {minor, major, critical} covers the day (started_at ..
  resolved_at, open-ended if unresolved).
- Observation tiers per Q4 service-day: clean (bad = 0), degraded
  (0 < bad/checks < 0.5), failure (bad/checks >= 0.5).
- False-green day (strong): observation failure AND claim green the
  whole day (no claim-bad, no maintenance). Weak tier: degraded.
- False-red day: the claim *indicator* was in {minor, major, critical}
  at some point that day AND observation clean. Days where an incident
  post is open but the indicator itself is green are a separate,
  labelled class (open-incident/green-indicator days) — the service's
  two claim streams disagreeing — not false-red.
- Day-level classification uses complete UTC days only; the snapshot
  day is partial (its uptime aggregate is still accumulating) and is
  excluded from day counts, though it is the stale-active reference.
- Stale-active incident: status not in {resolved, completed} at the
  snapshot; first seen >= 24h before the snapshot; and the service's
  last bad-check day is at least one full clean day before the
  snapshot day (observed recovery, incident still listed active).
- Drift: Q5 outage events (key svc:<slug>) matched to the Q1 incident
  of the same slug minimising |started_at - first_at| (<= 48h).
  drift = (claimed start - first event assembly) in minutes.
- Agreement: Q1 incidents with impact in {minor, major, critical} and
  Q4 coverage of their claimed span; corroborated if any covered day
  has bad > 0 or a Q5 outage event matches.
"""
import csv, json, os
from collections import defaultdict
from datetime import datetime, timezone

HERE = os.path.dirname(os.path.abspath(__file__))
load = lambda n: json.load(open(os.path.join(HERE, n + ".json")))
inc, chg, st, up, ev = (load("q1_incidents"), load("q2_changes"),
                        load("q3_status"), load("q4_uptime"), load("q5_events"))

def iso(ms): return datetime.fromtimestamp(ms / 1000, timezone.utc)
def day(ms): return iso(ms).strftime("%Y-%m-%d")

snapshot_ms = max(r["checked_at"] for r in st)
window_start_ms = min(r["ts"] for r in chg)
days = sorted(set(r["day"] for r in up))
BAD_IND = {"minor", "major", "critical"}

# ---- claim state per service-day -------------------------------------
chg_by_slug = defaultdict(list)
for r in chg: chg_by_slug[r["slug"]].append(r)
for v in chg_by_slug.values(): v.sort(key=lambda r: r["ts"])
status_by_slug = {r["slug"]: r for r in st}

def claim_indicator_during(slug, day_str):
    """Set of indicators the claim held at any point on day_str."""
    d0 = datetime.fromisoformat(day_str).replace(tzinfo=timezone.utc)
    d0ms, d1ms = int(d0.timestamp() * 1000), int(d0.timestamp() * 1000) + 86400000
    trans = chg_by_slug.get(slug, [])
    inds = set()
    if not trans:
        s = status_by_slug.get(slug)
        return {s["indicator"]} if s else set()
    # state at day start
    state = trans[0]["from_ind"]
    for t in trans:
        if t["ts"] <= d0ms: state = t["to_ind"]
        else: break
    inds.add(state)
    for t in trans:
        if d0ms < t["ts"] < d1ms: inds.add(t["to_ind"])
    return inds

inc_by_slug = defaultdict(list)
for r in inc: inc_by_slug[r["slug"]].append(r)

def incident_covers(r, day_str):
    if r["impact"] not in BAD_IND: return False
    if day(r["started_at"]) > day_str: return False
    if r["resolved_at"] and day(r["resolved_at"]) < day_str: return False
    return True

# ---- per-day discrepancy classification -------------------------------
up_by = {(r["slug"], r["day"]): r for r in up}
slugs = sorted(set([r["slug"] for r in up]) |
               set([r["slug"] for r in inc]) | set(chg_by_slug))
complete_days = [d for d in days if d < day(snapshot_ms)]
fg_strong, fg_weak, fr_days, oig_days = [], [], [], []
per_service = {}
for slug in slugs:
    ps = {"slug": slug, "incidents": len(inc_by_slug.get(slug, [])),
          "transitions": len(chg_by_slug.get(slug, [])),
          "false_green_days": 0, "false_green_weak_days": 0,
          "false_red_days": 0, "open_incident_green_days": 0,
          "stale_active": 0,
          "obs_bad_days": 0, "checks": 0, "bad": 0}
    for dstr in days:
        u = up_by.get((slug, dstr))
        if not u: continue
        ps["checks"] += u["checks"]; ps["bad"] += u["bad"]
        if u["bad"] > 0: ps["obs_bad_days"] += 1
        if dstr not in complete_days: continue
        frac = u["bad"] / u["checks"] if u["checks"] else 0
        tier = "clean" if u["bad"] == 0 else ("failure" if frac >= 0.5 else "degraded")
        inds = claim_indicator_during(slug, dstr)
        ind_bad = bool(inds & BAD_IND)
        inc_covers = any(incident_covers(r, dstr) for r in inc_by_slug.get(slug, []))
        claim_bad = ind_bad or inc_covers
        claim_green = not claim_bad and not (inds & {"maintenance"}) and not any(
            r["impact"] == "maintenance" and
            day(r["started_at"]) <= dstr and
            (not r["resolved_at"] or day(r["resolved_at"]) >= dstr)
            for r in inc_by_slug.get(slug, []))
        if tier == "failure" and claim_green:
            fg_strong.append((slug, dstr)); ps["false_green_days"] += 1
        elif tier == "degraded" and claim_green:
            fg_weak.append((slug, dstr)); ps["false_green_weak_days"] += 1
        elif tier == "clean" and ind_bad:
            fr_days.append((slug, dstr)); ps["false_red_days"] += 1
        if inc_covers and not ind_bad:
            oig_days.append((slug, dstr)); ps["open_incident_green_days"] += 1
    per_service[slug] = ps

# ---- stale-active ------------------------------------------------------
snap_day = day(snapshot_ms)
last_bad_day = {}
for r in up:
    if r["bad"] > 0: last_bad_day[r["slug"]] = max(last_bad_day.get(r["slug"], ""), r["day"])
stale = []
for r in inc:
    if r["status"] in ("resolved", "completed"): continue
    if snapshot_ms - r["seen_at"] < 86400000: continue
    lbd = last_bad_day.get(r["slug"])
    if lbd is not None and lbd < snap_day and \
       (datetime.fromisoformat(snap_day) - datetime.fromisoformat(lbd)).days >= 1 and \
       all(up_by.get((r["slug"], d), {}).get("bad", 0) == 0
           for d in days if d > lbd):
        stale.append(r)
        per_service[r["slug"]]["stale_active"] += 1
stale.sort(key=lambda r: r["seen_at"])

# ---- drift (Q1 x Q5) ----------------------------------------------------
outage_ev = [e for e in ev if e["kind"] == "outage" and e["key"].startswith("svc:")]
matches, indep_matches = [], []
for e in outage_ev:
    slug = e["key"][4:]
    cands = [r for r in inc_by_slug.get(slug, [])
             if abs(r["started_at"] - e["first_at"]) <= 48 * 3600 * 1000]
    if not cands: continue
    best = min(cands, key=lambda r: abs(r["started_at"] - e["first_at"]))
    drift_min = (best["started_at"] - e["first_at"]) / 60000.0
    srcs = json.loads(e["sources"]) if e["sources"] else {}
    rec = {"slug": slug, "incident": best["name"], "drift_min": round(drift_min, 1),
           "independent_source": any(k != "status" for k in srcs)}
    matches.append(rec)
    if rec["independent_source"]: indep_matches.append(rec)

def med(xs): 
    xs = sorted(xs); n = len(xs)
    return xs[n // 2] if n % 2 else (xs[n // 2 - 1] + xs[n // 2]) / 2
drifts = [m["drift_min"] for m in matches]
idrifts = [m["drift_min"] for m in indep_matches]

# ---- agreement -----------------------------------------------------------
ev_slugs = set(e["key"][4:] for e in outage_ev)
denom, corro = 0, 0
uncorro = []
for r in inc:
    if r["impact"] not in BAD_IND: continue
    d0 = day(r["started_at"]); d1 = day(r["resolved_at"]) if r["resolved_at"] else snap_day
    covered = [up_by[(r["slug"], d)] for d in days
               if d0 <= d <= d1 and (r["slug"], d) in up_by]
    if not covered: continue
    denom += 1
    if any(u["bad"] > 0 for u in covered) or r["slug"] in ev_slugs and \
       any(abs(r["started_at"] - e["first_at"]) <= 48 * 3600 * 1000
           for e in outage_ev if e["key"] == "svc:" + r["slug"]):
        corro += 1
    else:
        uncorro.append(r)

out = {
    "snapshot_utc": iso(snapshot_ms).strftime("%Y-%m-%dT%H:%M:%SZ"),
    "window_start_utc": iso(window_start_ms).strftime("%Y-%m-%dT%H:%M:%SZ"),
    "days": days,
    "counts": {"services_tracked": len(st), "incidents": len(inc),
               "transitions": len(chg), "uptime_service_days": len(up),
               "events": len(ev), "outage_events": len(outage_ev)},
    "complete_days": complete_days,
    "false_green_strong_days": fg_strong, "false_green_weak_days": fg_weak,
    "false_red_days": fr_days, "open_incident_green_days": oig_days,
    "stale_active": [{"slug": r["slug"], "name": r["name"], "status": r["status"],
                      "vendor_started": iso(r["started_at"]).strftime("%Y-%m-%dT%H:%M:%SZ"),
                      "first_seen": iso(r["seen_at"]).strftime("%Y-%m-%dT%H:%M:%SZ")}
                     for r in stale],
    "drift": {"matched": len(matches),
              "median_min": med(drifts) if drifts else None,
              "max_abs_min": max((abs(x) for x in drifts), default=None),
              "independent_matched": len(indep_matches),
              "independent_median_min": med(idrifts) if idrifts else None,
              "independent_max_abs_min": max((abs(x) for x in idrifts), default=None),
              "matches": matches},
    "agreement": {"denominator": denom, "corroborated": corro,
                  "rate_pct": round(100.0 * corro / denom, 1) if denom else None,
                  "uncorroborated": len(uncorro)},
    "per_service": [per_service[s] for s in slugs],
}
with open(os.path.join(HERE, "q6_analysis.json"), "w") as fh:
    json.dump(out, fh, indent=1)
with open(os.path.join(HERE, "per_service.csv"), "w", newline="") as fh:
    w = csv.DictWriter(fh, fieldnames=list(next(iter(per_service.values())).keys()))
    w.writeheader(); w.writerows(out["per_service"])
print(json.dumps({k: out[k] for k in ("snapshot_utc", "window_start_utc", "counts",
      "agreement", "drift") if k != "drift"}, indent=1))
print("drift:", {k: out["drift"][k] for k in out["drift"] if k != "matches"})
print("FG strong:", len(fg_strong), fg_strong)
print("FG weak:", len(fg_weak), fg_weak)
print("FR:", len(fr_days), fr_days)
print("OIG:", len(oig_days))
print("stale:", len(stale), [(r["slug"], r["status"]) for r in stale[:8]])
from collections import Counter
print("stale status dist:", Counter(r["status"] for r in stale))
