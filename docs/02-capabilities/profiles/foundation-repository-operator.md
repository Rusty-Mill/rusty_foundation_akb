# `rm.profile.foundation.repository-operator`

| Field | Value |
|---|---|
| Status | Draft |
| Version | 0.27.0 |
| Extends | [`rm.profile.foundation.server` 1.23.0](foundation-server.md) |
| Purpose | Operate software publication, authenticated repository metadata, mirrors, advisories, and emergency response without claiming a complete hosted registry product |

## Required composition

**RM-PROFILE-REPOSITORY-OPERATOR-0001:** Requires cryptographic policy/key operations, certificate trust where selected, signed-artifact production/verification, immutable durable storage, structured observability, configuration snapshots, service lifecycle, and network server/application protocols selected by a product RFC.

**RM-PROFILE-REPOSITORY-OPERATOR-0002:** Publication requires immutable release-candidate plans, separated namespace/upload/sign/approve/publish/promote/yank/advisory/revoke/mirror/retention roles, exact artifact/evidence digests, idempotent provider reconciliation, and immutable release records.

**RM-PROFILE-REPOSITORY-OPERATOR-0003:** Repository metadata uses independent root/delegation/targets/snapshot/freshness responsibilities and coherent monotonic snapshots with threshold, expiry, length/digest, rollback/freeze/mix-and-match, rotation, offline-root, and recovery evidence under a selected RFC profile.

**RM-PROFILE-REPOSITORY-OPERATOR-0004:** Channels are signed policy views over immutable digests. Promotion references the same tested digest; yank, deprecation, hold, demotion, revocation, and tombstone remain distinct revisioned overlays.

**RM-PROFILE-REPOSITORY-OPERATOR-0005:** Mirrors serve authenticated metadata/content without becoming authority. Replication, complete-snapshot visibility, lag, equivocation, regional failover, privacy, retention/GC, backup, and restore are evidence-bearing.

**RM-PROFILE-REPOSITORY-OPERATOR-0006:** Advisory operations preserve exact ecosystem/product/version/source/artifact applicability, affected/fixed/not-affected/under-investigation states, severity context, remediations, aliases, signed revisions, conversion loss, and withdrawal history.

**RM-PROFILE-REPOSITORY-OPERATOR-0007:** Coordinated disclosure provides private intake, hostile-artifact isolation, least-privilege cases, triage/escalation, embargo governance, private fix validation, external coordination, synchronized publication, reporter communication, retention, and closure evidence.

**RM-PROFILE-REPOSITORY-OPERATOR-0008:** Emergency operations cover identity/key/workflow/release/repository/mirror compromise and active exploitation with incident authority, publication freeze, credential/delegation/root rotation, exact revocation, consumer propagation, safe replacement, staged recovery, accessible communications, and review.

## Constraints and gaps

**RM-PROFILE-REPOSITORY-OPERATOR-0009:** Human/workload credentials are short-lived and least privilege; high-impact and break-glass actions use configured quorum, expiry, prominent audit, recovery rotation, and independent review.

**RM-PROFILE-REPOSITORY-OPERATOR-0010:** Inventory, reports, private artifacts, embargo data, identities, telemetry, audit, and regional access are classified, minimized, encrypted, access-controlled, redacted, retained, and erased/exported according to governance.

**RM-PROFILE-REPOSITORY-OPERATOR-0011:** Evidence covers role compromise, publication partial failure and immutability attacks, promotion/yank/revocation distinctions, mirror/GC/restore races, advisory range/conversion errors, disclosure leaks, emergency drills, provider outages, accessibility, conformance, and operational benchmarks.

**RM-PROFILE-REPOSITORY-OPERATOR-0012:** This profile does not select HTTP/API protocols, database/object store, queue/coordination topology, TUF/OCI/OSV/CSAF wire profiles, GitHub/crates.io/registry providers, service objectives, legal workflow, or product staffing. Those remain explicit RFC and deployment choices.

**RM-PROFILE-REPOSITORY-OPERATOR-0013:** When a product RFC selects HTTP, repository fetch/publication/advisory endpoints compose Server 1.8.0 with immutable artifact identity, authenticated metadata generation, range/conditional/cache semantics, proxy/privacy partition, replay-safe publication authority, overload/drain, and exact receipt evidence; this profile does not itself select routes, media types, schemas, or wire APIs.

**RM-PROFILE-REPOSITORY-OPERATOR-0014:** When a product selects real-time advisory, publication, mirror, or rollout observation, it composes Server 1.9.0 with immutable event identity/revision, authorization and tenant scope, bounded fanout/backpressure, reconnect as a new session, gap/duplicate/snapshot reconciliation, and no implication that observation authorizes or acknowledges a repository operation.

**RM-PROFILE-REPOSITORY-OPERATOR-0015:** When a product selects messaging/RPC for publication, mirroring, advisory, rollout, or administration workflows, it composes Server 1.10.0 with exact artifact/release/advisory/operation schemas, separated command/event authority, immutable attempt lineage, staged receipts, idempotent reconciliation, and no claim that queue settlement or handler return proves repository publication or consumer adoption.

**RM-PROFILE-REPOSITORY-OPERATOR-0016:** When a repository deployment selects distributed coordination, it composes Server 1.11.0 with exact publication/channel/advisory namespace state, configuration/quorum/fault-domain policy, fenced publishers/garbage collectors/mirror coordinators, testable read/write consistency, immutable recovery plans, and no inference that consensus commit proves external mirror or client adoption.

**RM-PROFILE-REPOSITORY-OPERATOR-0017:** When a repository selects a database, it composes Server 1.12.0 with exact release/channel/advisory/namespace schemas and constraints, publication transaction/idempotency boundaries, staged migrations, immutable audit/change evidence, backup/PITR and failover policy, semantic restore verification, and no inference that database commit proves signed metadata, mirror, or client visibility.

**RM-PROFILE-REPOSITORY-OPERATOR-0018:** When a repository selects object storage, it composes Server 1.13.0 with digest-verified immutable artifact descriptors, exact namespace/key/generation and metadata authority, conditional publication and channel-reference updates, quarantined multipart upload, delegated-download limits, inventory/retention/legal-hold/garbage-collection policy, mirror/replication recovery, and no inference that object commit proves authenticated metadata publication or client adoption.

**RM-PROFILE-REPOSITORY-OPERATOR-0019:** When a repository selects caching or edge delivery, it composes Server 1.14.0 with immutable digest-bearing release keys, credential/private-metadata partitions, bounded freshness for authenticated metadata and advisories, conditional validation, origin shielding, stampede control, revision-scoped purge, signed-download authority, propagation evidence, and no inference that a cache hit or purge proves repository truth or consumer adoption.

**RM-PROFILE-REPOSITORY-OPERATOR-0020:** When a repository selects search, it composes Server 1.15.0 with immutable release/advisory/source generations, exact ecosystem/package/version/platform schemas and analyzers, authenticated publication-to-index capture, tenant/private-artifact isolation, explicit visibility/partial state, stable cursors, bounded lexical/vector/hybrid ranking, rebuild/rollback, and no inference that a result authorizes installation or proves current signed metadata.

**RM-PROFILE-REPOSITORY-OPERATOR-0021:** When a repository selects analytics, it composes Server 1.16.0 with immutable release/download/advisory/mirror/source frontiers, purpose-scoped schemas/functions/materializations, privacy-preserving tenant/user analysis, late/corrected events, resource and retention budgets, reproducible reports, fenced publication effects, and no inference that analytical or checkpoint results authorize release, advisory, revocation, or consumer action.

**RM-PROFILE-REPOSITORY-OPERATOR-0022:** Repository interchange composes Server 1.17.0 with immutable versioned release/channel/advisory/metadata schemas, exact wire and canonical signed views, reserved identifiers and unknown preservation, bounded mirror/client parsing, loss-aware OSV/CSAF/TUF/OCI/native transcoding, authenticated registry/toolchain provenance, and no inference that parse, compatibility, or signature alone authorizes publication or installation.

**RM-PROFILE-REPOSITORY-OPERATOR-0023:** Repository traffic composes Server 1.18.0 with authenticated repository/mirror/metadata/advisory service identity, digest- and generation-aware routes, mirror health and freshness separation, region/data readiness, immutable release canaries, bounded download/publication retries, drain/failover propagation, and no inference that endpoint health or traffic shift proves coherent signed metadata, artifact availability, or consumer adoption.

**RM-PROFILE-REPOSITORY-OPERATOR-0024:** Repository policy composes Server 1.19.0 with typed namespace/upload/sign/approve/publish/promote/yank/advisory/revoke/mirror/retention decisions, immutable release/evidence and principal/tenant generations, mandatory security-policy precedence, quorum/break-glass obligations, fail-closed enforcement, simulation/audit, and no inference that a permit or completed obligation proves publication, mirror propagation, installation, or consumer adoption.

**RM-PROFILE-REPOSITORY-OPERATOR-0025:** Repository archives compose Server 1.20.0 with pinned reproducible profiles, exact codec/container/provider generations, immutable source trees and artifact digests, hostile uploaded-archive validation, bounded metadata/path/link policy, staged extraction, signed-view separation, and no inference that container validity or extraction authorizes publication, installation, or execution.

**RM-PROFILE-REPOSITORY-OPERATOR-0026:** Repository inspection composes Server 1.21.0 with digest-pinned candidates, recursive artifact graphs/SBOM links, origin/quarantine, multi-provider findings and expiry, isolated previews/transforms, private-upload disclosure controls, policy/quorum gates, and no inference that type, no-finding, transformation, signature, or publication implies safe installation/execution.

**RM-PROFILE-REPOSITORY-OPERATOR-0027:** Repository information protection composes Server 1.22.0 with issuer-qualified release/source/advisory/audit classifications, immutable artifact lineage, private namespace and cross-tenant recipient policy, protected uploads/downloads, governed downgrade, publication/export DLP, and no inference that a label or encryption grants publication, consumer access, installation, or legal compliance.

**RM-PROFILE-REPOSITORY-OPERATOR-0028:** Repository privacy composes Server 1.23.0 for accounts, maintainers, publishers, download/security telemetry, support, advisories, abuse/fraud, mirrors, recipients/processors, and analytics with explicit purpose plans, minimization, consent/preference where selected, lineage, rights/erasure/holds, secure exports, and no built-in legal/compliance conclusion.

**RM-PROFILE-REPOSITORY-OPERATOR-0029:** Repository identity governance composes Server 1.24.0 with immutable maintainer/publisher/service/tenant generations, organization/team membership evidence, invitations/federation, scoped publication entitlements, approval/SoD/access-review policy, emergency roles, and deprovisioning across sessions, credentials, signing/publishing grants, namespaces, artifacts, advisories, mirrors, and ownership without inferring publication authority from directory membership.

**RM-PROFILE-REPOSITORY-OPERATOR-0030:** Repository authentication composes Server 1.25.0 with phishing-resistant maintainer/publisher and privileged ceremonies where product policy requires, exact WebAuthn/federation/OAuth client and audience boundaries, separately protected automation credentials, step-up for publication/security effects, recovery with namespace/signing/session/token reconciliation, and no inference that authentication or token possession grants publish, sign, promote, yank, advisory, or revoke authority.

**RM-PROFILE-REPOSITORY-OPERATOR-0031:** Repository authorization composes Server 1.26.0 with typed namespace/package/release/channel/advisory actions, organization/team/maintainer relations, explicit ownership and publication grants/denies, attenuated automation/delegation, quorum obligations, sound private-resource filtering, effective-access review, generation-bound revocation, and final repository/signing/native enforcement without deriving publish authority from authentication, membership, or policy permit alone.

**RM-PROFILE-REPOSITORY-OPERATOR-0032:** Repository secrets compose Server 1.27.0 with workload-brokered upload/sign/publish/mirror/advisory credentials, opaque signing where available, exact automation audiences, staged rotation across CI and mirrors, successor-use and predecessor-denial proof, JIT/emergency operator checkout, leak scanning/response for source/history/artifacts/logs, and recovery that preserves release/signing authority separation.

**RM-PROFILE-REPOSITORY-OPERATOR-0033:** Repository workflows compose Server 1.28.0 with immutable release/advisory/security-response definitions and histories, fenced build/sign/publish/promote/yank/revoke effects, durable approvals/quorum/SoD, timers/embargoes, mirror/rollout children, explicit compensation, versioned in-flight migration, human tasks, and repair without replaying publication effects or claiming rollback of released artifacts.

**RM-PROFILE-REPOSITORY-OPERATOR-0034:** Repository APIs compose Server 1.29.0 with stable package/release/advisory operation identity, immutable contract registry releases, consumer-qualified CLI/SDK/service compatibility, signed generated-artifact provenance, idempotent publication, stable pagination/errors, quota policy, and observed migration before retirement.

**RM-PROFILE-REPOSITORY-OPERATOR-0035:** Repository synchronization composes Server 1.30.0 for mirrors, operator caches, and offline metadata tools while preserving immutable release identity/bytes, authenticated snapshot/frontier authority, signed provenance, yank/advisory/deletion overlays, selective privacy boundaries, conflict rejection, and no offline claim of publication completion.

**RM-PROFILE-REPOSITORY-OPERATOR-0036:** Repository tenant governance composes Server 1.31.0 for private namespaces, storage/transfer/build quotas, plan eligibility, and usage allocation while preserving repository authorization and publication authority, immutable release facts, security/advisory access during commercial faults, signed meter provenance, and no billing status as artifact trust evidence.

## History

- **0.27.0:** Adds constrained private-repository tenancy, plan eligibility, quota and usage governance while preserving publication, authorization, trust, and security-response boundaries.
- **0.26.0:** Adds constrained repository synchronization for mirrors and offline metadata while preserving immutable publication authority, authenticated frontiers, security overlays, and conflict rejection.
- **0.25.0:** Adds governed repository service contracts, generated artifacts, directional compatibility, publication semantics, and evidence-based API retirement.
- **0.24.0:** Rebases on Server 1.28.0 and constrains repository workflows to immutable release histories, fenced publication effects, quorum tasks, embargo timers, mirror children, forward compensation, migration, and repair.
- **0.23.0:** Rebases on Server 1.27.0 and constrains repository secrets to workload-brokered automation, opaque signing, exact audiences, complete CI/mirror rotation, privileged checkout, leak response, and separated release authority.
- **0.22.0:** Rebases on Server 1.26.0 and constrains repository authorization to typed publication resources/actions, ownership/team relations, attenuated automation, quorum, private filtering, effective-access review, and final repository/signing enforcement.
- **0.21.0:** Rebases on Server 1.25.0 and constrains repository authentication to verifier-bound operator ceremonies, exact federation/token audiences, protected automation, publication step-up, and recovery/session/credential reconciliation.
- **0.20.0:** Rebases on Server 1.24.0 and constrains repository identity governance to generation-bound maintainers, teams, publication entitlements, approvals/reviews, emergency roles, ownership, and complete credential/session/resource reconciliation.
- **0.19.0:** Rebases on Server 1.23.0 and constrains repository privacy to explicit purposes, minimized account/telemetry data, recipient/processor lineage, rights and scoped erasure, secure exports, and legal-policy separation.
- **0.18.0:** Rebases on Server 1.22.0 and constrains repository classification to issuer-qualified immutable lineage, private sharing, protected transfer, governed downgrade, publication DLP, and separated release authority.
- **0.17.0:** Rebases on Server 1.21.0 and constrains repository inspection to digest-pinned evidence graphs, provider freshness/privacy, isolated derivation, publication gates, and explicit nonclaims.
- **0.16.0:** Rebases on Server 1.20.0 and constrains repository archives to reproducible immutable artifacts, hostile validation, safe staging, exact signed views, and separated publication authority.
- **0.15.0:** Rebases on Server 1.19.0 and constrains repository policy to typed publication decisions, immutable release/principal evidence, mandatory security precedence, quorum obligations, fail-closed enforcement, and simulation/audit.
- **0.14.0:** Rebases on Server 1.18.0 and constrains repository traffic to authenticated service identity, metadata/artifact generations, mirror freshness, region readiness, bounded attempts, and coherent failover.
- **0.13.0:** Rebases on Server 1.17.0 and constrains repository interchange to immutable schemas, exact signed views, bounded parsing, unknown preservation, loss-aware security-format conversion, and provenance.
- **0.12.0:** Rebases on Server 1.16.0 and constrains optional analytics to immutable repository frontiers, privacy-preserving metrics, late corrections, reproducible reports, and separated publication authority.
- **0.11.0:** Rebases on Server 1.15.0 and constrains optional search to immutable release/advisory identity, authenticated capture, private-artifact isolation, explicit visibility, stable traversal, and source revalidation.
- **0.10.0:** Rebases on Server 1.14.0 and constrains optional caching/edge delivery to immutable releases, authenticated metadata freshness, privacy partitions, bounded purge, and propagation evidence.
- **0.9.0:** Rebases on Server 1.13.0 and constrains optional object storage to verified immutable artifacts, conditional publication, bounded delegation, retention/GC, and mirror recovery.
- **0.8.0:** Rebases on Server 1.12.0 and constrains optional databases to repository invariants, staged migrations, boundary-scoped publication, and verified recovery.
- **0.7.0:** Rebases on Server 1.11.0 and constrains optional coordination to fenced repository actors, precise consistency, quorum policy, and recovery evidence.
- **0.6.0:** Rebases on Server 1.10.0 and constrains optional messaging/RPC to exact repository schemas, command/event authority, staged receipts, and publication reconciliation.
- **0.5.0:** Rebases on Server 1.9.0 and constrains optional real-time observation to revisioned events, bounded fanout, new-session reconnect, and explicit gap/duplicate reconciliation.
- **0.4.0:** Rebases on Server 1.8.0 and constrains optional HTTP endpoints to preserve repository generations, publication replay authority, cache/proxy partitions, overload, and receipt evidence.
- **0.3.0:** Rebases on Server 1.7.0 and requires product-selected TLS/QUIC service endpoints to preserve original repository identity, mutual authentication where selected, ALPN, resumption/early-data, channel-binding, and closure evidence.
- **0.2.0:** Rebases on Server 1.6.0 so repository products can conditionally enroll and renew service/signing/status credentials under the shared lifecycle contract.
- **0.1.0:** Initial publication, repository/mirror, channel, advisory/disclosure, emergency, retention/backup, conformance, and operational-evidence profile.
