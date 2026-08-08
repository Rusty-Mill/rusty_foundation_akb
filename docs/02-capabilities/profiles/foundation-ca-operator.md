# `rm.profile.foundation.ca-operator`

| Field | Value |
|---|---|
| Status | Draft |
| Version | 0.6.0 |
| Extends | [`rm.profile.foundation.server` 1.11.0](foundation-server.md) |
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

**RM-PROFILE-CA-OPERATOR-0009:** When an enrollment/status/administration RFC selects HTTP, it composes Server 1.8.0 with exact account/request/nonce/transaction generations, replay and polling authority, credential/privacy partition, cache prohibition or freshness policy, bounded bodies, proxy/redirect constraints, overload, ambiguous-result reconciliation, and auditable response evidence; this profile does not choose the protocol mapping.

**RM-PROFILE-CA-OPERATOR-0010:** When a product selects real-time status, audit, approval, or ceremony observation, it composes Server 1.9.0 with authenticated least-privilege subscriptions, exact ledger/status revision, bounded fanout, reconnect as a new session, gap/duplicate/snapshot reconciliation, and an explicit nonclaim that observing or acknowledging an event grants approval or issuance authority.

**RM-PROFILE-CA-OPERATOR-0011:** When a product selects messaging/RPC for enrollment, validation, approval, issuance, status, audit, or ceremony workflows, it composes Server 1.10.0 with exact request/ledger/credential schemas, separated command/event authority, immutable attempts, deadline/cancellation nonrollback, durable idempotency/reconciliation, and no claim that broker settlement or handler return proves issuance, activation, revocation, or relying-party observation.

**RM-PROFILE-CA-OPERATOR-0012:** When a CA deployment selects distributed coordination, it composes Server 1.11.0 with exact issuer/ledger/serial/status configuration, fault-domain/quorum policy, resource-enforced fencing for signing/serial/status actors, precisely checked consistency, key/ledger external-effect reconciliation, immutable disaster recovery, and no inference that election alone authorizes CA key use.

## History

- **0.6.0:** Rebases on Server 1.11.0 and constrains optional coordination to fenced CA actors, precise ledger/status consistency, quorum policy, and disaster recovery.
- **0.5.0:** Rebases on Server 1.10.0 and constrains optional messaging/RPC to exact CA schemas, separated authority, staged effects, durable idempotency, and reconciliation.
- **0.4.0:** Rebases on Server 1.9.0 and constrains optional real-time observation to authenticated revisioned events, bounded fanout, new-session reconnect, and no authority from observation.
- **0.3.0:** Rebases on Server 1.8.0 and constrains optional HTTP mappings with exact transaction, replay/polling, credential/cache/proxy, overload, and ambiguous-result evidence.
- **0.2.0:** Rebases on Server 1.7.0 so enrollment, status, audit, and administration endpoints compose exact TLS/QUIC identity, mutual-authentication, ALPN, resumption/early-data, channel-binding, overload, and closure policy.
- **0.1.0:** Initial CA authority, issuance ledger/policy, enrollment protocols, renewal/revocation, hierarchy/key lifecycle, recovery, conformance, and benchmark profile.
