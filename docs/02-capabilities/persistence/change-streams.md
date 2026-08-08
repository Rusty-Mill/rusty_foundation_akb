# Change streams and integration

**RM-PERSISTENCE-CHANGE-0001:** A change subscription binds database/schema/table/key/filter generation, exact source/log mechanism, start snapshot/position, event schema, transaction grouping/order, before/after/key/image policy, authority, retention, and resource limits.

**RM-PERSISTENCE-CHANGE-0002:** Snapshot rows, transaction begin/changes/commit, schema change, heartbeat/watermark, gap/reset, rollback/abort, truncate, partition/rebalance, and end are distinct records. Consumers apply only committed changes according to the selected profile.

**RM-PERSISTENCE-CHANGE-0003:** Change position/cursor is opaque provider evidence with database/timeline/log generation, partition, offset, commit version/time, integrity, retention and resume rules. It is not a universal wall-clock or domain-event identity.

**RM-PERSISTENCE-CHANGE-0004:** Database commit, log availability, connector read, event encode/publish, broker acceptance, consumer receipt, materialized-view update, and downstream domain effect are separate. Change data capture alone does not atomically publish an application event.

**RM-PERSISTENCE-CHANGE-0005:** Reconnect/failover/resnapshot preserves duplicates, overlap, gaps, source timeline changes, schema evolution, and unknown last position explicitly. Products reconcile by transaction/change/domain identity and authoritative snapshots.

**RM-PERSISTENCE-CHANGE-0006:** Change capture minimizes and classifies data, filters rows/columns at the authoritative boundary, protects credentials/cursors, handles deletion/erasure propagation, bounds lag/retention/backlog, and prevents untrusted sink backpressure from exhausting the source.

**RM-PERSISTENCE-CHANGE-0007:** Transactional outbox ties domain mutation and append-only publication intent atomically within one database transaction. Relay claim/fencing, retry, broker settlement, cleanup, deduplication, ordering, schema migration, and reconciliation remain separate.

