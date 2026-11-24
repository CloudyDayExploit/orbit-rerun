# Researcher — Escalation to Microsoft Board / Corporate Governance, VULN-131121

- **Date:** 2025-02-11 21:35 UTC (2025-02-11 13:35 Pacific)
- **Case:** Case #89926 | VULN-131121
- **Direction:** Researcher → Microsoft Board of Directors mailbox (shareholder mail), cc MSRC Researcher Communications
- **Subject:** Urgent Security Concern – Azure Front Door Outage & Unmitigated Vulnerability (Case #89926 | VULN-131121)
- **Message-ID:** CAONZsFmdtTpPtSuVpT+Oc9-ryxAUnBokOpmbu5EF++onbKAvKQ@mail.gmail.com
- **Redactions:** email addresses; the researcher's phone number and personal-name signature (his byline, Cloudy_Day Cybersecurity, is retained); see ../REDACTION_LOG.md

---

Dear Microsoft Corporate Governance Team,

I am formally escalating an unmitigated security vulnerability that has remained unresolved for over seven months, despite being directly linked to the Azure Front Door outage on July 30, 2024. Our original disclosure to MSRC (Case #89926 | VULN-131121) in July 2024 provided clear technical proof of how misconfigured rate limits, exposed APIs, and persistent randomized request patterns could bypass Azure's DDoS protections and cause widespread service failures.

Microsoft failed to act, and the exact scenario we predicted played out, causing a major Azure service outage that affected Microsoft 365, Purview, and other cloud services.

---

Direct Link Between Our Research and the July 30 Azure Outage

Microsoft's own retrospective report confirms that the outage was caused by:

✔ A volumetric TCP SYN flood attack on Azure services.

✔ A network misconfiguration that prolonged congestion and degraded services.

✔ Persistent retry logic that overwhelmed misconfigured APIs.

✔ A network device in Europe that failed to obey control plane commands, keeping traffic congested.

Our original vulnerability report to MSRC detailed this exact scenario:

✔ Azure rate limits were ineffective, allowing thousands of requests per second.

✔ Misconfigured APIs bypassed WAF protections and remained exposed.

✔ Persistent, randomized API retry requests exacerbated congestion.

✔ Azure's DDoS mitigations failed to disengage, requiring manual intervention to restore services.

---

Microsoft's Ongoing Failure to Address This Vulnerability

Despite the July 30 outage confirming the severity of our findings, MSRC has failed to implement a full mitigation strategy, leaving Microsoft cloud customers at continued risk.

✔ This is no longer a theoretical concern—it has already resulted in a real-world service disruption.

✔ MSRC's inaction directly contributed to the scale of the Azure outage.

✔ A repeat failure is likely unless this vulnerability is fully addressed.

Microsoft must acknowledge the failure to act on our initial disclosure and take immediate corrective actions.

---

Immediate Action Required

1. Formal acknowledgment from Microsoft leadership that our findings were valid and should have been addressed before the July 30 outage.

2. Immediate implementation of stronger rate limits and API security protections across Azure services.

3. A commitment to industry-wide security improvements to prevent future large-scale cloud failures.

4. Direct engagement from Microsoft security executives to ensure that this issue does not remain unresolved.

This vulnerability remains unmitigated and poses a significant risk to Azure, Microsoft 365, and enterprise customers. Immediate intervention from Microsoft leadership is required.

Please confirm receipt and provide a timeline for corrective action within 24 hours.

---

Best regards,

Cloudy_Day Cybersecurity [personal name and phone number redacted]

---

*Archive note — calibration, stated plainly because this archive's credibility depends on it: the four "retrospective" bullet points above are the researcher's quotation of Microsoft's July 30, 2024 outage retrospective, inside his own escalation. The archive does not hold a separately retrieved Microsoft original of that retrospective, and nothing in the correspondence contains Microsoft attributing the outage to the researcher's reported issue. What the correspondence does contain, verbatim, is in the surrounding files: the July 2024 case openings, and the dismissals that followed this escalation.*
