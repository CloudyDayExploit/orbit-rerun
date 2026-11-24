# The Neutrality Charter

*Orbit Rerun. Published with the first public surface and binding on the operator.
Neutrality here is not a value statement — it is a set of checkable rules. If we
break one, the sealed record itself is the evidence.*

## The rules

1. **Methodology is public and versioned.** Collection methods, discrepancy
   definitions, the gap-score formula, and all thresholds are published in this
   repository. Changes are new versions, announced in advance where practical,
   and never retroactively applied to sealed history without a visible
   re-derivation note.

2. **Corrections are appended, never edited.** This applies to the archive and to
   everything we publish from it — including this project's own mistakes. An
   error is corrected by a new, dated entry linked from the original. The
   original stays. A recorder that quietly fixes its own history has become the
   thing it exists to expose.

3. **No pay-for-placement, ever.** No vendor can pay to be tracked sooner, scored
   gentler, listed higher, or removed. Coverage decisions and the criteria behind
   them are published.

4. **Evidence buyers buy exports, never influence.** Paying customers receive
   artefacts and API capacity. They do not receive advance notice, editorial
   input, methodology exceptions, or the ability to suppress an event. Paying
   relationships are disclosed in aggregate.

5. **Funding transparency.** Revenue sources are published in aggregate — the
   public layer is free; income is evidence exports, API capacity, and licensing —
   so any reader can judge our incentives for themselves.

6. **Claims are recorded verbatim; inference is labelled.** The archive quotes
   vendors exactly and measures independently. Anything we *conclude* is marked
   as inference, with its derivation shown. Vendors hold a right of reply: a
   vendor's response to an event is sealed and linked to that event, unedited,
   and is never used to alter the underlying record.

7. **The recorder records itself.** This project's own services and pipeline are
   tracked under the same rules, gap scores included. Our own discrepancies are
   sealed and published, not quietly fixed. (The founding example is our own:
   during development, two of our public surfaces showed different live incident
   counts at the same moment — 13 vs. 19. That class of drift is exactly what
   the sealed single source of truth exists to prevent, starting with us.)

## Redaction rule (standing, outranks convenience)

Public material published by this project **always redacts sensitive data**:
personal identifiers, email addresses, credentials, tokens, and private details
of individuals. Institutions and case numbers may be named where they are part
of the public record of a disclosure; individuals are referred to by role. When
in doubt, redact. The redaction policy for the founding disclosure archive —
including what was removed and why — is published in
[`../disclosure/REDACTION_LOG.md`](../disclosure/REDACTION_LOG.md), because
transparency about redaction is part of the ethics of publishing at all.

## What neutrality is not

- It is not silence. The recorder publishes discrepancies it can prove from
  sealed evidence, including uncomfortable ones.
- It is not both-sidesism. A claim and an observation are different kinds of
  thing; when they diverge, the divergence is the story, and it is reported as
  measured — not averaged into a shrug.
- It is not permanent perfection. It is a correction mechanism that cannot hide
  its own corrections.

## Enforcement

The charter is enforced structurally, not by goodwill: append-only storage,
public anchoring of the hash chain (see the sealing design), an open-source
offline verifier, and reproducible event derivation — anyone holding the entry
set recomputes the same timelines and scores. The end state this design aims at
is multi-party witnessing: independent parties co-signing daily roots and
running mirror collectors, so the record's integrity no longer rests on one
operator's honesty — including ours.
