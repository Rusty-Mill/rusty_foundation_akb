# Operations, recovery, and migration

**RM-AUDIT-OPS-0001:** Operators observe producer/source inventory, expected/received rates, sequence gaps, spool/backlog, validation/quarantine, append/durability, proof/anchor/key status, index lag, exporter frontiers, retention/holds, and restore verification.

**RM-AUDIT-OPS-0002:** Schema/policy/source enrollment, pause/drain, quarantine/release, backfill, reconcile, finalize, reindex, proof verify, hold/dispose, export, and repair are authorized idempotent plans with preview, receipts, audit, and rollback/nonrollback boundaries.

**RM-AUDIT-OPS-0003:** Configuration changes are versioned and audited; disabling capture, integrity, export, retention, alerting, or reconciliation requires explicit authority, reason, time bound where applicable, impact estimate, and compensating monitoring.

**RM-AUDIT-OPS-0004:** Backup/restore validates collection/segment/manifests/proofs, schema/policy, keys/trust, sequence/frontiers, corrections/suppressions, holds/retention, indexes, provider cursors, and known gaps before exposure.

**RM-AUDIT-OPS-0005:** Disaster recovery declares RPO/RTO, accepted event loss/duplication, source spool behavior, new collection/sequence/proof generations, fork prevention, backfill/reconciliation, and restored query/report limitations.

**RM-AUDIT-OPS-0006:** Store/protocol/schema/provider migration runs dual/shadow capture against controlled evidence, compares semantics/counts/digests/frontiers/proofs/query results, stages readers/writers, preserves chain continuity or declares genesis, and retains rollback evidence.
