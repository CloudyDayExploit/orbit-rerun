# Redaction Log — The Disclosure Archive

*This archive is published under a standing rule: **sensitive data is always
redacted from public view.** Transparency about the redaction itself is part of
the ethics of publishing — a reader should be able to see exactly what was taken
out, and why, without being able to recover it.*

## The rule

Redact personal identifiers, credentials, and private details — always, and
when in doubt, redact. Institutions and case numbers may be named: they are the
public record of a disclosure, and the researcher has approved his own
disclosure record as this project's founding exhibit. Individuals are referred
to by role. The researcher's own byline identity — Cloudy_Day Cybersecurity /
chyp.ai — is retained, because this is his disclosure and his project.

## What was redacted, by class

| Class | Treatment | Why |
|---|---|---|
| **Email addresses** (all parties, all directions) | Removed everywhere; mailboxes referred to by organisation ("MSRC", "Microsoft Bounty Team") | Addresses are personal/contact identifiers; the institution is the actor that matters to the record |
| **Individual names — vendor side** | Replaced with role: "[MSRC reviewer]", "[Technical Fellow — Azure Core]" (title retained, name removed) | The dismissals were institutional acts. Naming individual employees adds exposure, not evidence |
| **The researcher's personal name in headers, greetings, and signatures** | Rendered as "the researcher" / Cloudy_Day Cybersecurity byline | His public identity for this work is his research byline; his legal name and personal contact details are not evidence |
| **Phone number** (in the researcher's escalation signature) | Removed | Personal contact detail, no evidentiary value |
| **CRM tracking tokens** in subject lines | Replaced with "[CRM token redacted]"; VULN/MSRC case numbers retained | CRM tokens are internal routing identifiers; case numbers are the approved public reference points of the disclosure |
| **Session-tracking parameters** in two informational links (MSRC mail, Sep/Nov 2025) | Parameters stripped; link destinations (microsoft.com/msrc pages) retained in description | Tracking parameters are link artefacts, potentially session-linked; the destination pages are public |
| **Quoted-thread duplication** | Where a message quotes an earlier message that is archived in its own file, the quote is noted, not duplicated | Keeps each message's own words primary and the archive readable; nothing is lost — the quoted original is one link away |
| **Two middle paragraphs of the 2025-09-13 restatement** | Elided, marked "[…]", with the elision and its reason stated in the file | They concern market/earnings timing, not the disclosure record; the full text is retained in the sealed archive |
| **The Hyper-V bounty schedule reference** in the 2025-10-19 message | Summarised in brackets after the main text | Length and focus; the summary states what the section is, and the full text is retained in the sealed archive |

## What was NOT redacted

- **Case numbers** — VULN-131121, VULN-136961, VULN-144249, VULN-148726,
  VULN-163108, VULN-166834, MSRC Cases 89926 and 93814, and the #88926 variant
  as it appears in MSRC's own 2025-11-24 subject line.
- **Message-IDs** — retained in file headers. They let any reader with access
  to the original mail verify a rendering against the genuine message.
- **Dates and timestamps**, in UTC and the researcher's local time.
- **The vendor's words** — dismissals are quoted in full, in context, including
  the standard informational link lists (compressed after first occurrence,
  and marked where compressed).
- **The researcher's words** — rendered verbatim, including spelling and
  informality. A disclosure archive that polishes its author is a press
  release, not a record.
- **Unflattering structure** — the 24-hour PoC deadline, the closed-then-
  "still assessing" contradiction, the suggested-resubmission-then-dismissal
  sequence: all preserved in order. So are the gaps (see TIMELINE.md).

## Verification

Each rendering names its source message's date, subject, and Message-ID. The
unredacted originals remain in the researcher's mailbox and in the project's
sealed archive. Anyone who lawfully holds the original mail can check any
rendering line by line; the redactions above are the only differences, and
this log is the complete list of redaction classes applied.

*If a future reader believes a redaction was missed, the correction process is
the project's own rule: the fix is appended and noted — the published file's
history shows it. Contact via chyp.ai.*
