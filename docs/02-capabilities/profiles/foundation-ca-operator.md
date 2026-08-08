# `rm.profile.foundation.ca-operator`

| Field | Value |
|---|---|
| Status | Draft |
| Version | 0.2.0 |
| Extends | [`rm.profile.foundation.server` 1.7.0](foundation-server.md) |
| Purpose | Operate registration, certificate issuance, renewal, status, and CA lifecycle without claiming a complete public or enterprise CA product |

## Required composition

**RM-PROFILE-CA-OPERATOR-0001:** Requires cryptographic policy and hardware/remote key operations selected by risk, certificate/path/status validation, signed evidence, durable append-safe issuance ledger, structured observability, configuration generations, service lifecycle, backup/recovery, and product-selected network/application protocols.

**RM-PROFILE-CA-OPERATOR-0002:** Separates root, intermediate/issuing, registration/validation, approval, status/CRL/OCSP, transparency, audit, recovery, and administration roles with least privilege, quorum, offline/online boundaries, and ceremonies.

**RM-PROFILE-CA-OPERATOR-0003:** Issuance binds exact request/POP, subject/identifier proofing, enrollment authority, profile/policy, key/attestation, validity/serial, CA key operation, post-issuance lint, status/transparency, release, and requested-versus-issued evidence.

**RM-PROFILE-CA-OPERATOR-0004:** The ledger prevents transaction/serial rollback and duplicate release across concurrency, failover, restore, and retries. Partial or ambiguous operations reconcile before new issuance.

**RM-PROFILE-CA-OPERATOR-0005:** Renewal/rekey/replacement, mass rotation/revocation, hierarchy migration/cross-signing, key ceremonies, compromise response, backup/restore, audit, and CA termination are explicit generation-scoped workflows.

**RM-PROFILE-CA-OPERATOR-0006:** Evidence covers malicious requests, authority/POP/attestation escalation, policy construction, serial durability, HSM/provider failure, CT/status release, protocol replay/polling, renewal storms, root/intermediate rotation, cloned issuers, compromise, recovery, privacy, accessibility, conformance, and benchmarks.

## Explicit gaps

**RM-PROFILE-CA-OPERATOR-0007:** This profile does not select ACME/EST/SCEP/CMP/CMC or proprietary wire protocols, public-versus-private trust model, certificate profiles/policies/CPS, HSM/vendor, transparency/status topology, database/queue/coordination, legal/audit regime, SLA, staffing, or relying-party policy.

**RM-PROFILE-CA-OPERATOR-0008:** Server-generated keys, archival/escrow/recovery, subordinate-CA issuance, public-trust issuance, code-signing/timestamp services, and on-behalf-of enrollment are separately selected high-risk profiles and are not implied.

## History

- **0.2.0:** Rebases on Server 1.7.0 so enrollment, status, audit, and administration endpoints compose exact TLS/QUIC identity, mutual-authentication, ALPN, resumption/early-data, channel-binding, overload, and closure policy.
- **0.1.0:** Initial CA authority, issuance ledger/policy, enrollment protocols, renewal/revocation, hierarchy/key lifecycle, recovery, conformance, and benchmark profile.
