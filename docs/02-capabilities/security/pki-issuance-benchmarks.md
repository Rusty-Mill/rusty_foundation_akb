# PKI issuance benchmarks

**RM-PKI-ISSUANCE-BENCH-0001:** Measure key generation, request construction/signing, authentication/authorization/challenge, CA queue/approval, issuance/HSM signing, CT/status, response delivery, verification/install, service distribution/activation, renewal, revocation, and reconciliation separately and end to end.

**RM-PKI-ISSUANCE-BENCH-0002:** Scenarios cover interactive user, unattended service, managed device, TLS fleet, code-signing certificate, local software/hardware/remote keys, manual/out-of-band, pending approval, multi-identifier requests, short-lived certificates, root/intermediate rotation, and mass renewal/revocation.

**RM-PKI-ISSUANCE-BENCH-0003:** Report latency distributions, throughput, queue/approval/provider/network waits, protocol requests/bytes/retries/polls, CPU/memory/allocations, HSM operations/rate limits, CT/status lag, install/activation time, cancellation/recovery, and failure/indeterminate rates.

**RM-PKI-ISSUANCE-BENCH-0004:** Fleet tests measure renewal-window spread, deadline success and unknown denominator, CA/HSM/DNS/network/service peak load, retry/backoff fairness, early/late replacement, outage tolerance, pause/abort, and emergency-revocation propagation.

**RM-PKI-ISSUANCE-BENCH-0005:** CA durability tests quantify ledger commit, serial allocation, backup/restore, failover, issuance halt, key rotation, full hierarchy recovery, and assurance that no active clone or serial rollback occurs.

**RM-PKI-ISSUANCE-BENCH-0006:** Compare native enrollment, protocol-specific client, Rusty Mill adapter, and complete install/activation path only with equivalent proofing, POP, key protection, issuer policy, status/transparency, durability, and audit guarantees.

Initial budgets remain RFC-owned after representative Windows, Apple-managed, Linux/portable, ACME, EST/SCEP/CMP, software-key, and hardware/remote-key baselines exist.

## Stable scenario families

| Scenario | Scope | Required separation |
|---|---|---|
| `PKI-ISSUANCE-BENCH-001` | one complete issuance transaction | intent, proofing, authorization, POP, request, policy, ledger commit, signing, delivery, install, and activation |
| `PKI-ISSUANCE-BENCH-002` | workload/provider/protocol matrix | interactive, unattended, device, fleet, code-signing; software, hardware, remote keys; ACME, EST, SCEP, CMP, native, and out-of-band paths |
| `PKI-ISSUANCE-BENCH-003` | fleet renewal and revocation | scheduling input, randomized selection, retries, deadlines, replacement activation, old-generation retirement, status propagation, and reconciliation |
| `PKI-ISSUANCE-BENCH-004` | CA durability and recovery | ledger/serial commit, HSM operations, backup/restore, failover, clone prevention, hierarchy/key rotation, issuance halt, and restart |

Each result binds the exact protocol/profile, platform/provider/CA/key context, workload, concurrency, network, clock, policy, installation/activation consumer, measurement method, exclusions, and raw-evidence provenance. Cross-scenario summaries may compare compatible dimensions but never erase different assurance or lifecycle guarantees.
