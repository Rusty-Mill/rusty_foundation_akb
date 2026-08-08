# Persistence cross-cutting requirements

**RM-PERSISTENCE-CROSS-0001:** Database principals and roles use least privilege, short-lived credentials where possible, separate application/schema/admin/backup/restore/replication/key authorities, tenant/row policy, audited break-glass, and no ambient superuser fallback.

**RM-PERSISTENCE-CROSS-0002:** Data is classified by field/record/table/tenant and protected in transit, at rest, backups/logs/replicas/temp/spill/indexes/caches/telemetry. Encryption claims name keys/providers/generations, coverage, rotation/rekey, backup/restore, and plaintext exposure.

**RM-PERSISTENCE-CROSS-0003:** Privacy governs purpose/minimization, row/field authorization, query and inference controls, audit, retention/TTL, deletion/erasure across replicas/backups/change feeds/derived stores, export, legal hold, and provable residuals.

**RM-PERSISTENCE-CROSS-0004:** Security review covers injection, unsafe native queries, privilege/search-path confusion, tenant bypass, parser/type/coercion ambiguity, malicious stored data, inference, stale plans, backup/log theft, replica/failover takeover, restore clone, migration escalation, and denial of service.

**RM-PERSISTENCE-CROSS-0005:** Observability correlates logical operation/attempt, database/schema/session/transaction/query plan, provider endpoint/replica, consistency/durability, rows/bytes, lock/conflict/retry, pool/queue, change/migration/backup/recovery, and domain result without logging sensitive values by default.

**RM-PERSISTENCE-CROSS-0006:** Diagnostics, migration/recovery approvals, conflicts, backup/restore state, and user-facing data operations expose database purpose/scope, affected data, consistency/durability/data-loss/downtime, point of no return, progress, cancellation limits, and recovery accessibly and locally.

**RM-PERSISTENCE-CROSS-0007:** Identifiers, schemas, query semantics, decimal/time units, collations, and wire/provider syntax are locale-independent. Human display/search/sort policy uses explicit locale/Unicode/time-zone context and never mutates database session defaults implicitly.

