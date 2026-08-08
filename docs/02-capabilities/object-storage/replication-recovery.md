# Replication, recovery, and portability

**RM-OBJECT-REPLICATION-0001:** Replication policy binds source/destination namespace generations and accounts/regions, selection, live/noncurrent/delete-marker/metadata/tag/retention coverage, ordering/conflicts, encryption/keys, authority, lag, failure/retry, and ownership/billing.

**RM-OBJECT-REPLICATION-0002:** Source committed, replication queued, transferred, destination generation committed, metadata/retention synchronized, destination visible, verified, failed/blocked, and caught-up are separate with exact source/destination versions and lag evidence.

**RM-OBJECT-REPLICATION-0003:** Bidirectional/multi-writer replication declares version vector/generation mapping, concurrent overwrite/delete/metadata conflict policy, clock assumptions, tombstones, loop prevention, authority, and irreconcilable/manual states.

**RM-OBJECT-RECOVERY-0001:** Recovery source may be exact retained version, soft-deleted state, replica, inventory, backup/archive, content-addressed mirror, or application reconstruction; each has freshness, completeness, integrity, authority, cost, and semantic-verification evidence.

**RM-OBJECT-RECOVERY-0002:** Restore/copy-back creates a new target generation under explicit conditional commit, metadata/encryption/retention policy, provenance, validation, cache/event effects, and application readiness. It does not rewind namespace history.

**RM-OBJECT-RECOVERY-0003:** Regional/service failover preserves provider domain/namespace identity, exact replication checkpoint, read/write consistency, stale/delete conflict, credentials/endpoints, delegated tokens, multipart sessions, event/inventory continuity, cost, and failback.

**RM-OBJECT-PORTABILITY-0001:** Export/migration manifests bind exact objects/versions/descriptors/metadata, namespace mapping, unsupported/lossy fields, retention/holds, encryption/keys, order, checkpoints, source freeze or change reconciliation, destination verification, and cutover/rollback.

**RM-OBJECT-PORTABILITY-0002:** Provider portability never maps ETags, storage classes, ACLs, leases, version IDs, retention modes, checksums, event ordering, or consistency by name alone. Every mapping records semantic loss or fails.

