# `rm.profile.foundation.repository-operator`

| Field | Value |
|---|---|
| Status | Draft |
| Version | 0.3.0 |
| Extends | [`rm.profile.foundation.server` 1.7.0](foundation-server.md) |
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

## History

- **0.3.0:** Rebases on Server 1.7.0 and requires product-selected TLS/QUIC service endpoints to preserve original repository identity, mutual authentication where selected, ALPN, resumption/early-data, channel-binding, and closure evidence.
- **0.2.0:** Rebases on Server 1.6.0 so repository products can conditionally enroll and renew service/signing/status credentials under the shared lifecycle contract.
- **0.1.0:** Initial publication, repository/mirror, channel, advisory/disclosure, emergency, retention/backup, conformance, and operational-evidence profile.
