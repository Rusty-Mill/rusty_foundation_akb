# Mirrors, availability, retention, and backup

**RM-REPOSITORY-MIRROR-0001:** A mirror is an untrusted distribution replica unless separately configured as a metadata authority. Consumers authenticate repository metadata and object digests independent of mirror transport.

**RM-REPOSITORY-MIRROR-0002:** Replication tracks source snapshot, complete object set, target mirror, start/completion, lag, omissions, verification, and checkpoint. A mirror advertises a snapshot only after all referenced required objects are retrievable.

**RM-REPOSITORY-MIRROR-0003:** Mirror selection/failover is bounded by region, privacy, proxy, cost, health, freshness, retry/backoff, and equivocation policy. A bad mirror cannot force rollback, wrong-target selection, or unbounded transfer.

**RM-REPOSITORY-MIRROR-0004:** Repository availability objectives separately cover metadata freshness, object retrieval, publication visibility, advisory/emergency propagation, control-plane mutation, and recovery. Success from one region/provider is not global availability.

**RM-REPOSITORY-RETENTION-0001:** Retention policy distinguishes published artifacts, metadata history, signatures/attestations/SBOMs, advisories, audit/ceremony, unpublished staging, logs, backups, and personal/security-sensitive reports.

**RM-REPOSITORY-RETENTION-0002:** Published release objects are retained according to ecosystem permanence promises. Legal/security takedown uses authenticated tombstone metadata and preserves the minimum audit/history permitted; consumers are never served different bytes under the old digest/version.

**RM-REPOSITORY-RETENTION-0003:** Garbage collection traces reachability from every retained snapshot/channel/release/advisory/referrer and honors replication/backup/legal holds. Mark/sweep generations prevent races with concurrent publication.

**RM-REPOSITORY-BACKUP-0001:** Backups include immutable objects, metadata history and signing inputs, ownership/authority state, advisories, audit evidence, and restoration manifests; private keys remain under their own protected recovery design.

**RM-REPOSITORY-BACKUP-0002:** Restore drills prove digest integrity, namespace continuity, monotonic metadata, non-reuse of deleted identities, channel/advisory state, mirror bootstrap, credential re-establishment, and recovery time/data-loss objectives.

