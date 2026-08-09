# `rm.profile.foundation.ca-operator`

| Field | Value |
|---|---|
| Status | Draft |
| Version | 0.25.0 |
| Extends | [`rm.profile.foundation.server` 1.23.0](foundation-server.md) |
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

**RM-PROFILE-CA-OPERATOR-0013:** When a CA selects a database, it composes Server 1.12.0 with exact account/request/serial/issuance/status/audit schemas and constraints, transaction-to-key-operation/release reconciliation, staged migrations, append-safe change evidence, encrypted backup/PITR and failover, semantic restore verification, and no inference that database commit proves certificate release, revocation propagation, or relying-party observation.

**RM-PROFILE-CA-OPERATOR-0014:** When a CA selects object storage, it composes Server 1.13.0 with exact generation-bound encrypted objects and independently verified content descriptors for certificates, CRLs, audit evidence, ceremony records, and backups; least-privilege delegated access; conditional publication; retention/legal hold/erasure policy; replicated recovery; and no inference that object commit proves ledger consistency, status publication, transparency inclusion, or relying-party observation.

**RM-PROFILE-CA-OPERATOR-0015:** When a CA selects caching or edge delivery, it composes Server 1.14.0 with strict account/credential/privacy partitions, profile-qualified certificate/status/CRL keys, bounded freshness and validation, revocation/status invalidation and propagation evidence, origin shielding and storm control, signed access where selected, and no inference that a hit, miss, or purge proves current ledger truth or relying-party observation.

**RM-PROFILE-CA-OPERATOR-0016:** When a CA selects search, it composes Server 1.15.0 with exact account/request/serial/certificate/status/audit source generations, purpose-scoped schemas and analyzers, strict tenant/field/document isolation, ordered ledger-to-index capture including revocation/erasure, explicit visibility/partial state, stable audited traversal, bounded diagnostics, rebuild/recovery, and no inference that a result proves issuance validity, current status, or relying-party trust.

**RM-PROFILE-CA-OPERATOR-0017:** When a CA selects analytics, it composes Server 1.16.0 with exact ledger/status/transparency/audit source frontiers, approved schemas/functions/materializations, strict tenant and sensitive-field controls, event-time/late correction, disclosure-resistant aggregates, reproducible compliance evidence, checkpoint-to-HSM/status/transparency effect separation, and no inference that analytical state authorizes issuance, revocation, key use, or relying-party trust.

**RM-PROFILE-CA-OPERATOR-0018:** CA interchange composes Server 1.17.0 with exact versioned certificate/request/status/protocol/audit schemas and ASN.1/DER plus selected protocol mappings, canonical signed regions, strict hostile-input constraints, unknown critical-extension rejection, preserved noncritical evidence, loss-aware conversion, authenticated schema/OID registries, and no inference that parsing or canonicality proves trust, issuance authority, possession, or status.

**RM-PROFILE-CA-OPERATOR-0019:** CA traffic composes Server 1.18.0 with authenticated enrollment/status/transparency/administration service identities and endpoint generations, profile/tenant routes, readiness separated from key/ledger/status/data health, bounded replay-safe attempts, fenced issuer effects, region/ceremony capacity, controlled failover/failback, emergency revocation propagation, and no inference that health or routing grants signing/issuance authority or proves relying-party status.

**RM-PROFILE-CA-OPERATOR-0020:** CA policy composes Server 1.19.0 with typed enrollment/validation/approval/profile/issuance/status/revocation/key/ceremony decisions, immutable request/identity/POP/attestation/ledger/time generations, mandatory cryptographic/trust/legal-policy precedence, quorum/HSM/transparency/status obligations, fail-closed enforcement, simulation/audit, and no inference that a permit grants key authority or proves issuance, status propagation, or relying-party trust.

**RM-PROFILE-CA-OPERATOR-0021:** CA archives compose Server 1.20.0 with exact reproducible container/codec profiles for ceremony, audit, CRL, evidence, and backup artifacts; independently verified digests/signatures/encryption; strict metadata/path/link policy; staged restore; key separation; and no inference that decode or extraction proves ledger consistency, key authority, status, or trust.

**RM-PROFILE-CA-OPERATOR-0022:** CA content inspection composes Server 1.21.0 for enrollment attachments, attestation/evidence bundles, ceremony media, audit imports, and backups with exact subject/origin generations, recursive bounded inspection, offline/private-provider policy, quarantine, isolated transformations, and no inference that type/no-finding/transform permits key use, issuance, restore, publication, or trust.

**RM-PROFILE-CA-OPERATOR-0023:** CA information protection composes Server 1.22.0 with issuer-qualified classifications for requests/identity evidence/key material/ceremonies/ledgers/audit/backups, compartmented recipients and channels, rights/encryption/markings, quorum downgrade, offline/revocation/recovery, DLP, and no inference that a label grants HSM/key/issuance/status/publication/trust authority.

**RM-PROFILE-CA-OPERATOR-0024:** CA privacy composes Server 1.23.0 for account/identity/validation/attestation/contact/audit/security data with exact issuance/status/security/legal-purpose plans, minimized projections, processor/region routes, retention/holds, subject rights and scoped erasure where policy permits, and no inference that privacy workflow can alter immutable certificate/ledger/trust facts.

**RM-PROFILE-CA-OPERATOR-0025:** CA identity governance composes Server 1.24.0 with immutable operator/approver/auditor/service/tenant generations, ceremony and issuance entitlements, separation of duties, quorum/access reviews, JIT/emergency roles, and deprovisioning across directory, sessions, credentials, HSM/key shares, issuance/status/transparency authority, ledgers, backups, and ownership without inferring key or issuance authority from membership.

**RM-PROFILE-CA-OPERATOR-0026:** CA authentication composes Server 1.25.0 with phishing-resistant and non-exportable operator authentication where policy requires, verifier-bound administration/ceremony audiences, separately authenticated service/automation identities, transaction-bound step-up for key/issuance/status effects, quorum preserved after authentication, and recovery that rotates/revokes authenticators, sessions, tokens, key access, and emergency material without inferring issuance authority.

**RM-PROFILE-CA-OPERATOR-0027:** CA authorization composes Server 1.26.0 with typed issuer/key/profile/request/order/certificate/status/ceremony actions, operator/service/tenant relations, mandatory denies and quorum/SoD obligations, attenuated enrollment/signing/status delegation, sound private-ledger filtering, effective-access review, generation-bound emergency revocation, and final HSM/ledger/native enforcement without deriving key or issuance authority from authentication, role, or policy permit alone.

**RM-PROFILE-CA-OPERATOR-0028:** CA secrets compose Server 1.27.0 with HSM/provider-mediated key use, workload-brokered enrollment/status/transparency credentials, dynamic operator sessions, exact lease/ceremony scopes, staged issuer/service rotation with successor-use and predecessor-denial evidence, dual-control checkout and offline break-glass, leak/compromise response, backup/migration/deletion boundaries, and no plaintext private-key assumption.

**RM-PROFILE-CA-OPERATOR-0029:** CA workflows compose Server 1.28.0 with immutable enrollment/issuance/revocation/key-ceremony/hierarchy-recovery histories, fenced HSM/ledger/status effects, timers and pending approvals, quorum/SoD human tasks, child ceremonies, forward compensation and residuals, versioned migration, repair/recovery, and no replay of signing or issuance effects.

**RM-PROFILE-CA-OPERATOR-0030:** CA APIs compose Server 1.29.0 with stable enrollment/issuance/status/revocation operation identity, exact contract and profile generations, directional relying-party/agent compatibility, generated-client provenance, idempotent effect identity, privacy-safe errors, bounded quotas, and migration evidence before retirement.

**RM-PROFILE-CA-OPERATOR-0031:** CA synchronization composes Server 1.30.0 only for authenticated status, policy, inventory, and ceremony projections; issuance, revocation, signing, key, and ledger effects require current fenced authority. Conflicts never use generic last-write-wins, and revocation/tombstone evidence cannot be compacted before every admitted replica is retired or rebased.

## History

- **0.25.0:** Adds constrained CA projection synchronization while prohibiting offline authority for issuance/key/status effects and preserving conflict, revocation, and retirement evidence.
- **0.24.0:** Adds governed CA service contracts, compatibility across agents and relying parties, generated artifacts, issuance-effect semantics, and evidence-based retirement.
- **0.23.0:** Rebases on Server 1.28.0 and constrains CA workflows to immutable issuance histories, fenced HSM/ledger effects, pending timers, quorum ceremonies, forward compensation, migration, and repair without replayed signing.
- **0.22.0:** Rebases on Server 1.27.0 and constrains CA secrets to HSM-mediated use, brokered service identity, scoped leases, complete issuer/service rotation, dual-control emergency access, compromise response, and explicit recovery/deletion boundaries.
- **0.21.0:** Rebases on Server 1.26.0 and constrains CA authorization to typed issuer/key effects, operator/service relations, mandatory deny/quorum, attenuated delegation, private-ledger filtering, effective-access review, and final HSM/ledger enforcement.
- **0.20.0:** Rebases on Server 1.25.0 and constrains CA authentication to verifier-bound operator ceremonies, exact service audiences, transaction-bound step-up, preserved quorum, and recovery across authenticators/sessions/tokens/key access.
- **0.19.0:** Rebases on Server 1.24.0 and constrains CA identity governance to immutable operator roles, ceremony/issuance entitlements, quorum/SoD/reviews, emergency access, and complete credential/key/session/resource reconciliation.
- **0.18.0:** Rebases on Server 1.23.0 and constrains CA privacy to explicit issuance/security purposes, minimized identity evidence, processors/regions, rights/holds/scoped erasure, and preservation of immutable certificate/ledger facts.
- **0.17.0:** Rebases on Server 1.22.0 and constrains CA classification to compartmented immutable evidence, protected channels, quorum downgrade, DLP, offline/revocation, and separated key/issuance/trust authority.
- **0.16.0:** Rebases on Server 1.21.0 and constrains CA content inspection to private generation-bound evidence, bounded recursion, quarantine, isolated derivation, and separated issuance/key/trust authority.
- **0.15.0:** Rebases on Server 1.20.0 and constrains CA archives to reproducible evidence, independent cryptographic verification, key separation, safe staged restore, and separated ledger/trust authority.
- **0.14.0:** Rebases on Server 1.19.0 and constrains CA policy to typed issuance decisions, immutable request/identity/ledger evidence, mandatory trust precedence, quorum/HSM obligations, fail-closed enforcement, and simulation/audit.
- **0.13.0:** Rebases on Server 1.18.0 and constrains CA traffic to authenticated service identity, separated key/ledger/status health, replay-safe attempts, fenced effects, controlled failover, and emergency revocation.
- **0.12.0:** Rebases on Server 1.17.0 and constrains CA interchange to exact ASN.1/DER and protocol schemas, canonical signed regions, hostile parsing, critical extensions, registries, and loss-aware conversion.
- **0.11.0:** Rebases on Server 1.16.0 and constrains optional analytics to exact CA frontiers, disclosure-resistant aggregates, reproducible evidence, late corrections, and separated key/status effects.
- **0.10.0:** Rebases on Server 1.15.0 and constrains optional search to exact CA source generations, strict isolation, ordered status capture, explicit visibility, audited traversal, and source revalidation.
- **0.9.0:** Rebases on Server 1.14.0 and constrains optional caching/edge delivery to strict identity partitions, bounded status freshness, storm control, and propagation evidence.
- **0.8.0:** Rebases on Server 1.13.0 and constrains optional object storage to generation-bound encrypted evidence, verified content, conditional publication, retention, and recovery.
- **0.7.0:** Rebases on Server 1.12.0 and constrains optional databases to CA ledger invariants, staged migrations, key/effect reconciliation, and verified recovery.
- **0.6.0:** Rebases on Server 1.11.0 and constrains optional coordination to fenced CA actors, precise ledger/status consistency, quorum policy, and disaster recovery.
- **0.5.0:** Rebases on Server 1.10.0 and constrains optional messaging/RPC to exact CA schemas, separated authority, staged effects, durable idempotency, and reconciliation.
- **0.4.0:** Rebases on Server 1.9.0 and constrains optional real-time observation to authenticated revisioned events, bounded fanout, new-session reconnect, and no authority from observation.
- **0.3.0:** Rebases on Server 1.8.0 and constrains optional HTTP mappings with exact transaction, replay/polling, credential/cache/proxy, overload, and ambiguous-result evidence.
- **0.2.0:** Rebases on Server 1.7.0 so enrollment, status, audit, and administration endpoints compose exact TLS/QUIC identity, mutual-authentication, ALPN, resumption/early-data, channel-binding, overload, and closure policy.
- **0.1.0:** Initial CA authority, issuance ledger/policy, enrollment protocols, renewal/revocation, hierarchy/key lifecycle, recovery, conformance, and benchmark profile.
