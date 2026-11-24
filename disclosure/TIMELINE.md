# Timeline — The Disclosure Record, From Day 1

*The founding exhibit of Orbit Rerun: the complete email record of one researcher's
disclosure to Microsoft, excavated from his own mailbox and rendered with redactions
(see REDACTION_LOG.md). Every entry below is backed by a message in
`correspondence/`. Where the record is the researcher's own account rather than a
document, it is labelled as his account. Where something is referenced but could not
be retrieved, it is listed under Gaps — not reconstructed.*

**The record in one line:** 30 messages, rendered in full, spanning
**25 July 2024 → 11 December 2025 (504 days)**; more than fifty further messages —
forwards, duplicates, survey and portal notifications — sit on the same threads;
the researcher's wider MSRC correspondence in the same period spans 16 VULN case
numbers. The vendor's own subject lines map the family together.

---

## Day 1

### 2024-07-25 — The first contact

**14:29 Pacific — Researcher → Microsoft Bounty Team. Subject: "Bug."**
([correspondence](correspondence/2024-07-25_researcher_to_microsoft-bounty_day-one.md))

Day 1 is this email. It is the earliest message in the record, and the excavation
searched for anything earlier — Microsoft mail back to January 2023 — and found no
security-disclosure correspondence before it (see Retrieval method, below). What
the message is, precisely:

> "Hello! I found a vulnerability that I feel is extremely critical, i discovered
> your bug bounty program yesterday for Hyper-V Server, I was able to quickly
> implement and test something appeared to start working, so i stopped it
> immediately after verifying it was most likely valid. My intentions are always
> good, and I hope to help you guys patch a gigantic hole in the server security
> systems."

**What Day 1 is and is not.** It *is* a dated, surviving first contact: a
Hyper-V Server finding, reported the day after the researcher found the bounty
program, five days before the 30 July 2024 Azure outage. It is *not*, in its own
text, an Azure denial-of-service report — that framing enters the written record
over the following days, as the case moved to MSRC (the MSRC reviewer's reply of
26 July already discusses a Microsoft asset "vulnerable to Denial Of Service").
The researcher's account is that the July 25 contact began the single disclosure
that became the Azure case; MSRC's own subject line of 2025-11-24 maps the
July 2024 submission, VULN-131121, and "Hyper-V VULN-166834" as one family of
related cases. Both facts are in the record. Readers can weigh the connection
themselves — that is what a record is for.

**14:45 Pacific — Microsoft Bounty Team → Researcher.**
([correspondence](correspondence/2024-07-25_microsoft-bounty_reply.md))
Sixteen minutes later: submit via the MSRC Researcher Portal. He did, the same
evening.

**17:27 Pacific (2024-07-26 00:27 UTC) — MSRC acknowledges VULN-131121.**
([correspondence](correspondence/2024-07-26_msrc_acknowledgement_vuln-131121.md))

## 2024 — The outage, and the case that would not stay answered

### 2024-07-26 — MSRC's first substantive reply
([correspondence](correspondence/2024-07-26_msrc_reply_vuln-131121.md))
An MSRC reviewer writes that he is "struggling to determine what is it that you
are reporting," asks whether a named Microsoft asset is "vulnerable to Denial Of
Service - DOS," requests a proof-of-concept video, and adds: "I will keep this
open for 24-hours."

### 2024-07-29 — The researcher tries the press (metadata only)
Sent-mail metadata shows news tips sent to four outlets late on 29 July Pacific
— one carrying the subject "Critical IT Bug," the others generic news-tip
subjects. The archive records the subjects and recipient organisations only;
the bodies were not excavated for this exhibit, and no claim is made here about
their content beyond the subject lines.

### 2024-07-30 — The Azure outage; Case 89926 opened
**07:08 Pacific — MSRC opens MSRC Case 89926.**
([correspondence](correspondence/2024-07-30_msrc_case-89926_opened.md))
The researcher's own timeline (2025-09-13, below) records the outage at 5am
Pacific that morning and case acceptance at 7am. The case-opening email is
timestamped 07:08. The outage itself — a major Azure disruption on 30 July 2024 —
is a matter of public record outside this archive.

### 2024-07-31 — The researcher's reply
([correspondence](correspondence/2024-07-31_researcher_reply_case-89926.md))
Sent just after midnight Pacific. In his contemporaneous account, testing on
Microsoft's side that morning had confirmed his expectations; he thanks MSRC
"for mitigating this issue." His characterisation is presented as his account.

### 2024-09-04 — Update request
([correspondence](correspondence/2024-09-04_researcher_update-request_case-89926.md))
Six weeks on, he asks for an update on Case #89926 — and checks, before speaking
to a journalist, that doing so would not "interfere with your mitigation
process."

### 2024-09-26 — Case closed (per the researcher's account)
No closure email survives in the mailbox; the date comes from the researcher's
15 October message: "my case was open from july 25th until september 26th."
Listed here as his account, and under Gaps.

### 2024-10-15 — "Is there any bounty or acknowledgement?"
([correspondence](correspondence/2024-10-15_researcher_message_vuln-131121.md))
The researcher writes to MSRC Researcher Communications: the case was open from
July 25 to September 26; "This was the exploit that caused the Azure outage end
of July" (his claim, labelled as such); is there any bounty or acknowledgement
now that it is closed?

### 2024-10-16 — VULN-136961 acknowledged
([correspondence](correspondence/2024-10-16_msrc_acknowledgement_vuln-136961.md))
The outage submission — MSRC's later subject line describes it as "Submitted
July 30–31, 2024" — is acknowledged under its own case number.

### 2024-10-22 — "Still in the assessment and planning phase"
([correspondence](correspondence/2024-10-22_msrc_researcher-communications_vuln-131121.md))
MSRC's Recognition Team describes the case the researcher understood to be
closed as still in assessment. The contradiction is preserved as found.

### 2024-10-25 — PoC demanded; closure threatened
([correspondence](correspondence/2024-10-25_msrc_reply_vuln-136961.md))
"To investigate your report, we require a valid proof of concept (PoC)… Since we
have not heard from you, we will need to close this report."

### 2024-12-25 — VULN-144249 acknowledged
([correspondence](correspondence/2024-12-25_msrc_acknowledgement_vuln-144249.md))
A further related case enters the family; the researcher sends his material the
same day and MSRC replies on the thread the next.

## 2025 — Escalation, dismissal, resubmission, dismissal

### 2025-01-02 — MSRC Case 93814 opened
([correspondence](correspondence/2025-01-02_msrc_case-93814_opened.md))

### 2025-02-05 — Case 93814 closed, "low severity"
([correspondence](correspondence/2025-02-05_msrc_closure_case-93814.md))
"After careful investigation, this case has been assessed as **low severity**…
'Marking this as 'Low Severity' as we were not able to see any sensitive
information as reported.'"

### 2025-02-11 — Escalation to the Board
([correspondence](correspondence/2025-02-11_researcher_escalation_vuln-131121.md))
The researcher takes the record over MSRC's head, to Microsoft's Board /
Corporate Governance mailbox: the July 2024 disclosure "provided clear technical
proof of how misconfigured rate limits, exposed APIs, and persistent randomized
request patterns could bypass Azure's DDoS protections." The escalation quotes
Microsoft's own outage retrospective — a network misconfiguration that prolonged
congestion, persistent retry logic overwhelming misconfigured APIs, a network
device in Europe that failed to obey control-plane commands. **Calibration:**
those retrospective lines are the researcher's quotation inside his escalation;
the archive holds no separately retrieved Microsoft original of the retrospective,
and no message in this record has Microsoft attributing the outage to his report.
The archive's claim is the narrower, provable one — see the closing note.

### 2025-02-12 — The Board mailbox deflects
([correspondence](correspondence/2025-02-12_msrc_researcher-communications_reply.md))
The Recognition Team replies that its mailbox "does not have any impact on the
assessment process" and directs him back to the case thread.

### 2025-02-13 — "Concluded this as a non-issue"
([correspondence](correspondence/2025-02-13_msrc_dismissal_vuln-131121.md))
One day later, on the case thread:

> "We unfortunately haven't been able to link what you've submitted to a
> legitimate finding. We have looked through your submissions with multiple
> teams of engineers and have concluded this as a non-issue."

### 2025-02-24 — Researcher's follow-up (index only)
A further researcher message, "Urgent: Azure Outage Findings & Disclosure
Concerns," is recorded in the mailbox index for this date. Its full text was not
separately rendered for this exhibit; see Gaps.

### 2025-02-26 — VULN-148726 acknowledged
([correspondence](correspondence/2025-02-26_msrc_acknowledgement_vuln-148726.md))
The family grows again. The researcher replies on the thread on 2 March.

### 2025-09-13 — The researcher restates the record, with his timeline
([correspondence](correspondence/2025-09-13_researcher_restatement_vuln-136961.md))
"I submitted the Azure outage details before it happened. July 25th I told you
guys in my case in an email to [the bounty mailbox], then they said to add to
MSRC." His timeline — July 25 2024 submission; July 30 2024, 5am PST, Azure
outage; July 30, 7am PST, case accepted — matches the surviving mail at every
checkable point.

### 2025-09-15 — MSRC suggests resubmission
([correspondence](correspondence/2025-09-15_msrc_reply_vuln-136961.md))
"I suggest that you resubmit the issue within your portal since this report is
almost a year old. You can certainly add my name for faster routing of the new
report." The researcher replies the same day: "Will do, thank you."
([correspondence](correspondence/2025-09-15_researcher_reply_vuln-136961.md))

### 2025-09-17 — The resubmission: VULN-163108
Portal submission acknowledged 07:52 UTC
([correspondence](correspondence/2025-09-17_msrc_acknowledgement_vuln-163108.md));
the researcher posts the new case number to the thread:
([correspondence](correspondence/2025-09-17_researcher_resubmission_vuln-163108.md))

> VULN-163108

### 2025-09-18 — "Please refrain from submitting this case to us again"
([correspondence](correspondence/2025-09-18_msrc_dismissal_vuln-163108.md))
The resubmission MSRC suggested is answered within a day:

> "You have submitted this case to us in the past and our team looked at it
> extensively. We do not see a correlation with what you are saying and what is
> reflected in our logs. Please refrain from submitting this case to us again."

### 2025-10-19 / 2025-10-20 — Azure Core leadership replies
The researcher writes directly to a Technical Fellow in Azure Core
([correspondence](correspondence/2025-10-19_researcher_to_azure-fellow_vuln-131121.md)).
The Fellow replies the next day: "Thanks for reaching out to me. I'm looking
into the information you sent. May I ask who you've been communicating with in
MSRC?"
([correspondence](correspondence/2025-10-20_azure-fellow_reply.md))
The archive records the exchange exactly as far as the mail goes, and no
further: what came of the looking-into is not in the record.

### 2025-11-12 — Follow-up
([correspondence](correspondence/2025-11-12_researcher_followup_vuln-136961.md))
"Was [the Fellow] able to contact you? I found a contradiction in his statement
from the outage, and have a way better explanation now of how it works."

### 2025-11-21 — VULN-166834 acknowledged
([correspondence](correspondence/2025-11-21_msrc_acknowledgement_vuln-166834.md))
The Hyper-V case — the thread back to Day 1's subject — is acknowledged under
its own number.

### 2025-11-24 — "Not able to see evidence"; MSRC maps the family itself
([correspondence](correspondence/2025-11-24_msrc_reply_vuln-136961.md))

> "We put a lot of time and energy in your previous submissions and we were not
> able to see evidence for your submission."

The subject line of that same message does the archive's work for it:
"Reference (Original July 2024 submission): MSRC Case ID VULN-136961 – Submitted
July 30–31, 2024 (Mapped to later related cases including VULN-131121 / Case
#88926 - Hyper-V VULN-166834". Note the case number as MSRC renders it there —
#88926; every 2024 artefact in this archive reads 89926. The discrepancy is in
the original and is preserved, not corrected.

### 2025-12-11 — The last word in the record is the researcher's
([correspondence](correspondence/2025-12-11_researcher_to_microsoft-bounty_retrospective.md))
To the Bounty Team, where Day 1 began: "Hey guys, I read the comments made at
blackhat Europe, can we coordinate for my July 30 2024 azure ddos case for the
retrospective? Thanks." No reply appears in the mailbox as of excavation.

---

## Retrieval method

This archive was excavated from the researcher's own mailbox on 2026-11-24, by
searching — not by selecting from memory:

- **Folders:** Inbox, Sent, and All Mail. Sent was searched specifically because
  the original July 2024 contact had never surfaced in inbox-focused searches;
  Day 1 was found there.
- **Query families:** each case number individually (VULN-131121, VULN-136961,
  VULN-144249, VULN-148726, VULN-163108, VULN-166834, MSRC 93814, #89926 and the
  #88926 variant found in the mail); sender families (MSRC, MSRC Researcher
  Communications, Microsoft Bounty); subject families (DenialOfService, Azure,
  DDoS, "rate limit"); and date-bounded passes — before 2024-09-01 first, then
  widened through 2026, plus a dedicated pre-July-2024 pass over all Microsoft
  mail back to January 2023 to test for anything earlier than Day 1.
- **Result:** 214 messages inventoried across all passes; 30 rendered in full in
  `correspondence/`; the balance are forwards, duplicates, survey invitations,
  portal notifications, and the researcher's wider MSRC correspondence (16 VULN
  case numbers in total across 2024–2025, of which the seven in this exhibit are
  the Azure/Hyper-V family).
- **Pre-July-2024 check:** all Microsoft mail from January 2023 to 25 July 2024
  in the searched families is consumer account, order, and product mail. No
  earlier security-disclosure correspondence exists in this mailbox. Day 1 is
  Day 1.

## Gaps — referenced, but not retrieved

Honesty about the holes is part of the exhibit:

1. **The detailed MSRC portal submission(s) of July 2024.** The portal
   submissions themselves were made through a web form; what survives in mail
   is the first-contact email (Day 1), the acknowledgements, and the threads.
   The full technical report text as submitted to the portal is **not** in this
   archive, and nothing here reconstructs it.
2. **The original text of the July 30–31, 2024 outage submission** (the
   submission VULN-136961 was later attached to). Its existence and dates are
   documented by MSRC's own subject lines; the submitted text does not survive
   as an email.
3. **A closure message for the September 26, 2024 case closing.** The date is
   the researcher's own statement (2024-10-15); no closure email was found.
4. **The researcher's 2025-02-24 follow-up** ("Urgent: Azure Outage Findings &
   Disclosure Concerns") is indexed by subject and date; it was not separately
   rendered in this pass.
5. **Microsoft's July 30, 2024 outage retrospective.** Known to this archive
   only as quoted inside the researcher's 2025-02-11 escalation. The archive
   does not present the quotation as a Microsoft document.
6. **Any outcome of the October 2025 Azure Core exchange** beyond the two
   messages archived, and any reply to the 2025-12-11 message. Absence from
   this mailbox is stated as absence from this mailbox — nothing more.

## The closing note — what this record does and does not claim

The mail strongly supports: a researcher reported a critical finding to
Microsoft on 25 July 2024; a case was open before and on the morning of a major
Azure outage five days later; the reported pattern — misconfigured rate limits,
exposed APIs, retry behaviour — is a misconfiguration story; and over the
following sixteen months the file was closed as a "non-issue," closed as "low
severity," answered with "we do not see a correlation… refrain from submitting
again," and finally with "not able to see evidence" — including a dismissal,
one day after it was sent, of a resubmission Microsoft itself had suggested.

The mail does **not** contain Microsoft attributing the July 30, 2024 outage to
the researcher's report, or to any change or deployment, in so many words. The
archive does not claim it does. The founding claim of Orbit Rerun is the narrow,
provable one: **a researcher warned a vendor, the vendor dismissed him, and
until now the only record of either was the vendor's.** That is the gap this
project exists to close.
