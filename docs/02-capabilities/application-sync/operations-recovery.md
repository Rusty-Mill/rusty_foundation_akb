# Operations and recovery

**RM-APP-SYNC-OPS-0001:** Operators can inspect lag/frontiers, backlog, conflicts, failed/quarantined changes, replica membership, checkpoint ancestry, schema populations, tombstone horizons, and resource pressure without reading protected content by default.

**RM-APP-SYNC-OPS-0002:** Pause, resume, drain, reprioritize, retry, reject, quarantine, rebase, resnapshot, resolve, exclude, and retire are authorized idempotent operations with previews, bounded scope, receipts, and audit.

**RM-APP-SYNC-OPS-0003:** Repair never edits history silently. It emits a new administrative change or rebuild generation with evidence, preserving displaced intent and residual uncertainty.

**RM-APP-SYNC-OPS-0004:** Backup/restore validates dataset and replica identity, schema/policy, causal frontier, tombstones, pending changes, keys, attachments, and checkpoints; restored writable state receives safe incarnation handling.

**RM-APP-SYNC-OPS-0005:** Disaster recovery declares RPO/RTO, authoritative survivor selection, split-brain prevention, accepting/losing writes, reconciliation, client rebase, and resumption evidence.

**RM-APP-SYNC-OPS-0006:** Protocol/provider migration runs shadow/differential sync, compares semantic state and hidden metadata, stages populations, preserves rollback horizons, and proves convergence before retirement.
