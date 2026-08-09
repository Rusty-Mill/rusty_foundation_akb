# Queries, snapshots, and change streams

**RM-IDENTITY-GOV-QUERY-0001:** Queries declare tenant/source scope, object kinds, filter semantics, attribute projection, consistency/freshness request, page limits, ordering, privacy purpose, and authority.

**RM-IDENTITY-GOV-QUERY-0002:** Page tokens bind query, source, snapshot or revision frontier, ordering, policy generation, and expiry. Clients do not combine pages from incompatible frontiers into a coherent snapshot.

**RM-IDENTITY-GOV-QUERY-0003:** Change records carry object identity/generation, operation, source revision, ordering scope, before/after availability, gaps, duplicates, and tombstones. A cursor is scoped progress evidence, not proof of global completeness.

**RM-IDENTITY-GOV-QUERY-0004:** Consumers persist checkpoints only after durable application, handle at-least-once delivery, detect invalid/expired cursors, and perform a new snapshot-plus-delta reconciliation without duplicating effects.

**RM-IDENTITY-GOV-QUERY-0005:** Enumeration, filtering, errors, counts, timing, and change feeds apply anti-enumeration, minimization, audit, rate, and tenant-isolation controls.
