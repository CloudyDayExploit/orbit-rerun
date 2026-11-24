# Researcher — Direct message to Azure Core leadership, VULN-131121

- **Date:** 2025-10-19 09:11 UTC (2025-10-19 02:11 Pacific)
- **Case:** Case #89926 / VULN-131121 — "[30-JUL-2024 AZURE DDOS CASE]"
- **Direction:** Researcher → a Microsoft Technical Fellow, Azure Core (individual name redacted to role), MSRC team addressed in the greeting
- **Subject:** Clarification and Continuity Regarding VULN-131121 (Azure / Hyper-V Bounty Alignment) [30-JUL-2024 AZURE DDOS CASE]
- **Message-ID:** CAONZsFmxM7cQsp09GzrkABb4gqi3-UqgViDxzhOvvmhmBwLzNA@mail.gmail.com
- **Redactions:** email addresses; the recipient's name (greeting rendered with role); see ../REDACTION_LOG.md

---

[30-JUL-2024 AZURE DDOS CASE]

Hi [Technical Fellow] and MSRC Team,

I hope you're doing well.

I wanted to follow up on case #89926 / VULN-131121, originally submitted under the Microsoft Hyper-V Bounty Program.

From day one, our goal has been simple—resilience. We set out to help strengthen the systems we all depend on by testing entirely within the published Hyper-V bounty guidelines active prior to the August 2025 revision. Every step of our proof-of-concept, testing, and documentation process followed those terms exactly, focusing on authorized DoS and host-level service-disruption scenarios.

Over the past 16 months we have continued tracking the same network behaviors we documented during that submission. Telemetry captured before, during, and after the July 30 2024 Azure event clearly shows Layer 7 congestion interacting with transport-layer saturation across multiple ASN 8075 nodes (notably Berlin and Frankfurt). These behaviors pre-date the public impact window and directly contradict the later assertion that "Layer 7 was not a factor."

Our dataset—packet traces, routing evidence, and reproducible Hyper-V conditions—aligns 100 percent internally and externally. Nothing in our analysis conflicts with Microsoft's published sequence; in fact, it fills the visibility gap between the application and network layers. We followed every rule and provided the blueprint exactly as the program requested; the only misunderstanding came in later interpretation, not in the data itself.

---

[The message continues with a reference section setting out the Hyper-V bounty schedule as it stood at the time of submission (Feb 2021 – Aug 2025), including the award ranges the researcher understood to apply to host-disruption denial-of-service and information-disclosure findings. That schedule detail is elided here; the full text is retained in the sealed archive. All technical characterisations above are the researcher's own, presented as his account.]

---

*Archive note: sixteen months in, the researcher took the record directly to Azure Core engineering leadership. The reply is archived as 2025-10-20_azure-fellow_reply.md.*
