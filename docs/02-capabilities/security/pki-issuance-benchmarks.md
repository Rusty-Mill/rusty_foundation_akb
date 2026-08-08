# PKI issuance benchmarks

**RM-PKI-ISSUANCE-BENCH-0001:** Measure key generation, request construction/signing, authentication/authorization/challenge, CA queue/approval, issuance/HSM signing, CT/status, response delivery, verification/install, service distribution/activation, renewal, revocation, and reconciliation separately and end to end.

**RM-PKI-ISSUANCE-BENCH-0002:** Scenarios cover interactive user, unattended service, managed device, TLS fleet, code-signing certificate, local software/hardware/remote keys, manual/out-of-band, pending approval, multi-identifier requests, short-lived certificates, root/intermediate rotation, and mass renewal/revocation.

**RM-PKI-ISSUANCE-BENCH-0003:** Report latency distributions, throughput, queue/approval/provider/network waits, protocol requests/bytes/retries/polls, CPU/memory/allocations, HSM operations/rate limits, CT/status lag, install/activation time, cancellation/recovery, and failure/indeterminate rates.

**RM-PKI-ISSUANCE-BENCH-0004:** Fleet tests measure renewal-window spread, deadline success and unknown denominator, CA/HSM/DNS/network/service peak load, retry/backoff fairness, early/late replacement, outage tolerance, pause/abort, and emergency-revocation propagation.

**RM-PKI-ISSUANCE-BENCH-0005:** CA durability tests quantify ledger commit, serial allocation, backup/restore, failover, issuance halt, key rotation, full hierarchy recovery, and assurance that no active clone or serial rollback occurs.

**RM-PKI-ISSUANCE-BENCH-0006:** Compare native enrollment, protocol-specific client, Rusty Mill adapter, and complete install/activation path only with equivalent proofing, POP, key protection, issuer policy, status/transparency, durability, and audit guarantees.

Initial budgets remain RFC-owned after representative Windows, Apple-managed, Linux/portable, ACME, EST/SCEP/CMP, software-key, and hardware/remote-key baselines exist.

