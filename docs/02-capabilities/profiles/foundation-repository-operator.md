# `rm.profile.foundation.repository-operator`

| Field | Value |
|---|---|
| Status | Draft |
| Version | 0.9.0 |
| Extends | [`rm.profile.foundation.server` 1.13.0](foundation-server.md) |
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

## History

- **0.9.0:** Rebases on Server 1.13.0 and constrains optional object storage to verified immutable artifacts, conditional publication, bounded delegation, retention/GC, and mirror recovery.
- **0.8.0:** Rebases on Server 1.12.0 and constrains optional databases to repository invariants, staged migrations, boundary-scoped publication, and verified recovery.
- **0.7.0:** Rebases on Server 1.11.0 and constrains optional coordination to fenced repository actors, precise consistency, quorum policy, and recovery evidence.
- **0.6.0:** Rebases on Server 1.10.0 and constrains optional messaging/RPC to exact repository schemas, command/event authority, staged receipts, and publication reconciliation.
- **0.5.0:** Rebases on Server 1.9.0 and constrains optional real-time observation to revisioned events, bounded fanout, new-session reconnect, and explicit gap/duplicate reconciliation.
- **0.4.0:** Rebases on Server 1.8.0 and constrains optional HTTP endpoints to preserve repository generations, publication replay authority, cache/proxy partitions, overload, and receipt evidence.
- **0.3.0:** Rebases on Server 1.7.0 and requires product-selected TLS/QUIC service endpoints to preserve original repository identity, mutual authentication where selected, ALPN, resumption/early-data, channel-binding, and closure evidence.
- **0.2.0:** Rebases on Server 1.6.0 so repository products can conditionally enroll and renew service/signing/status credentials under the shared lifecycle contract.
- **0.1.0:** Initial publication, repository/mirror, channel, advisory/disclosure, emergency, retention/backup, conformance, and operational-evidence profile.
