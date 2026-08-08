# Migration, rebuild, and recovery

**RM-SEARCH-MIGRATE-0001:** Mapping/analyzer/model/ranking/topology changes use immutable new index generations with plan, capacity estimate, source watermark, backfill, catch-up, validation, shadow/dual query where needed, atomic alias/routing switch, rollback, and retirement.

**RM-SEARCH-MIGRATE-0002:** Rebuilds originate from an authoritative snapshot plus ordered changes, prove document/tombstone/authorization convergence, and do not copy unknown corruption as truth.

**RM-SEARCH-MIGRATE-0003:** Mixed application/index generations publish a compatibility matrix for writes, queries, fields, cursors, ranking, and rollback; old cursors fail explicitly after incompatible view retirement.

**RM-SEARCH-RECOVERY-0001:** Replica recovery, remote segment restore, and snapshot restore validate index identity, schema/configuration generation, integrity, source watermark, tombstones, tenant/security policy, and provider version compatibility.

**RM-SEARCH-RECOVERY-0002:** Snapshots identify included indexes/generations, consistency boundary, encryption/key generation, retention/immutability, incomplete state, restore prerequisites, and independently tested semantic recovery.

**RM-SEARCH-RECOVERY-0003:** Failover names routing/configuration generation, accepted write boundary, visibility lag, read consistency, partial search, split-brain prevention, source reconciliation, and controlled failback.

**RM-SEARCH-RECOVERY-0004:** Disaster recovery proves source-to-index reconstruction, not only provider snapshot restoration, and measures RPO/RTO plus relevance/security parity.

**RM-SEARCH-MIGRATE-0004:** Index lifecycle, tier migration, segment merge, force merge, shrink/split, rollover, retention, and deletion preserve alias/view/cursor authority and avoid silent query gaps.
