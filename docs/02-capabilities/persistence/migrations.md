# Schema evolution and migrations

**RM-PERSISTENCE-MIGRATION-0001:** A migration plan binds source/target schema and application protocol generations, exact ordered steps, preconditions, affected objects/data/indexes/constraints/code paths, compatibility matrix, locks/resources, backup/recovery point, authority, and rollback/roll-forward boundaries.

**RM-PERSISTENCE-MIGRATION-0002:** Expand/deploy/backfill/validate/switch-contract phases preserve old/new readers and writers according to an explicit matrix. Destructive contraction occurs only after evidence proves old code, jobs, replicas, change consumers, backups, and rollback paths no longer require the old shape.

**RM-PERSISTENCE-MIGRATION-0003:** DDL transactionality, metadata locks, table rewrites/copies, online/concurrent behavior, replication/log impact, defaults/generated values, index/constraint build, and cancellation differ by provider and are resolved before execution.

**RM-PERSISTENCE-MIGRATION-0004:** Backfills are resumable generation-scoped jobs with stable selection, batch/checkpoint, throttling, idempotency, concurrent-write reconciliation, validation, failure quarantine, progress, deadline, and no assumption that row count equals semantic completion.

**RM-PERSISTENCE-MIGRATION-0005:** Dual read/write or shadow paths declare source of truth, precedence, atomicity, ordering, mismatch handling, repair, metrics, duration, failure modes, and removal gate. They cannot silently extend indefinitely.

**RM-PERSISTENCE-MIGRATION-0006:** Migration history is append-safe evidence binding plan/tool/application/provider versions, exact step/checksum, executor authority, start/end, transaction and lock state, data validation, warnings, point of no return, residuals, and recovery action.

**RM-PERSISTENCE-MIGRATION-0007:** Rollback is available only for declared pre-commit steps whose old schema/data remains compatible. After destructive or semantically lossy change, recovery is a new restore/repair/forward migration with explicit data-loss and downtime evidence.

**RM-PERSISTENCE-MIGRATION-0008:** Mixed application/database versions, rolling deployment, read replicas, offline clients, queues/change streams, backups/PITR, caches, analytics, and imports/exports are migration participants or declared external dependencies—not afterthoughts.

