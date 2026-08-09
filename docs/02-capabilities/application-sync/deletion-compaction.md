# Deletion, tombstones, compaction, and retirement

**RM-APP-SYNC-DELETE-0001:** Delete is a versioned change with object/incarnation, causal context, actor/authority, reason class, effective scope, retention, undo/restore policy, and downstream effect semantics.

**RM-APP-SYNC-DELETE-0002:** Tombstones fence stale creates/updates and survive checkpoints, snapshots, backups/restores, retries, schema migration, and selection changes long enough to prevent resurrection.

**RM-APP-SYNC-DELETE-0003:** Tombstone reclamation requires a proven retirement frontier covering every replica/incarnation or a policy that permanently rejects its future history. Time elapsed alone is insufficient.

**RM-APP-SYNC-DELETE-0004:** Lost, retired, cloned, or indefinitely offline replicas have explicit exclusion/re-enrollment and full-rebase rules before reclamation can advance.

**RM-APP-SYNC-DELETE-0005:** Compaction preserves the information required for causality, idempotency, conflicts, audit, legal hold, erasure, and late-peer safety; semantic loss and recovery horizon are declared.

**RM-APP-SYNC-DELETE-0006:** Privacy erasure minimizes tombstones to purpose-bound fencing evidence and reconciles replicas, indexes, attachments, logs, backups, and pending changes without claiming universal disappearance.
