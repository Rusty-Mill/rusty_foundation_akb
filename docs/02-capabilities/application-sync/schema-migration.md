# Schema and data migration

**RM-APP-SYNC-MIGRATE-0001:** Schema evolution declares readable, writable, mergeable, forwardable, and preservable generation ranges independently for each replica/provider version.

**RM-APP-SYNC-MIGRATE-0002:** Migration plans cover old/new readers and writers, queued offline changes, snapshots/checkpoints, causal metadata, merge rules, indexes, constraints, attachments, tombstones, and rollback horizons.

**RM-APP-SYNC-MIGRATE-0003:** Changes are interpreted under their original schema then explicitly upcast/transformed with provenance and loss; applying a new schema to old bytes without resolution is prohibited.

**RM-APP-SYNC-MIGRATE-0004:** Dual-read/write or expand-migrate-contract stages bind exact populations and frontiers. Contracting old fields waits for active and plausibly returning offline replicas or applies explicit rebase/exclusion policy.

**RM-APP-SYNC-MIGRATE-0005:** Merge-policy changes define interaction between changes created under different policies and cannot retroactively relabel prior losing intent as resolved.

**RM-APP-SYNC-MIGRATE-0006:** Restore, downgrade, and application rollback detect future schema/causal state and fail safely, preserve it opaquely, or require a new replica incarnation and full reconciliation.
