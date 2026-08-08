# Renewal, rekey, replacement, and revocation

**RM-PKI-RENEWAL-0001:** Renewal policy derives an eligibility window from certificate validity, issuer guidance, authorization/proofing freshness, risk, outage/retry budget, fleet spreading, maintenance/restart policy, key age/usage, and emergency directives. Local wall-clock heuristics alone are insufficient.

**RM-PKI-RENEWAL-0002:** Issuer-suggested renewal information is authenticated policy input, not execution authority. Clients bound freshness, validate applicability, randomize within windows, preserve minimum retry safety, and handle missing/invalid guidance explicitly.

**RM-PKI-RENEWAL-0003:** Renewal produces a new certificate generation. Same-key renewal and rekey are explicit alternatives; policy may require new keys by age, use, compromise, algorithm/provider transition, cloning/snapshot risk, or protection change.

**RM-PKI-RENEWAL-0004:** Continuity may use an existing certificate/key, account, device/workload identity, reauthorization, administrator approval, or another protocol mechanism. The method binds old/new public keys, subject/identifiers/profile, transaction, channel, and policy; possession of an old key alone does not authorize arbitrary modifications.

**RM-PKI-RENEWAL-0005:** Replacement for lost/unavailable/compromised key does not claim POP of the old key and requires configured recovery/identity proof plus revocation/disable consideration for the prior certificate.

**RM-PKI-RENEWAL-0006:** Activation uses prepare/distribute, readiness, atomic or explicitly non-atomic routing switch, overlap, old-session/cache handling, confirmation, old-certificate retirement, and key destruction according to service policy.

**RM-PKI-RENEWAL-0007:** Renewal success distinguishes issued, installed, distributed, active, observed healthy, replacement reported, and old credential retired/revoked. Failure preserves the last valid generation where safe and escalates before outage.

**RM-PKI-RENEWAL-0008:** Mass renewal/rekey/revocation uses deterministic cohort spreading, CA/HSM/DNS/network/service capacity budgets, priority, pause/abort, missing-device accounting, emergency deadlines, and evidence. Identical cron schedules are prohibited fleet policy.

**RM-PKI-RENEWAL-0009:** Revocation request authority is independent of issuance/renewal. It binds certificate/issuer/serial/digest, reason, effective/compromise time, requester/approvals, protocol, evidence, status publication, affected deployments, and replacement guidance.

