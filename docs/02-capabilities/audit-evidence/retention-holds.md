# Retention, legal hold, erasure, and disposal

**RM-AUDIT-RETENTION-0001:** Retention schedules bind event/evidence class, purpose, tenant/jurisdiction, start trigger, minimum/maximum, archive tier, proof/key dependencies, index/cache copies, backups, deletion method, reviewer, and version.

**RM-AUDIT-RETENTION-0002:** Legal/investigation/security holds bind authority, case/scope/query or exact objects, start/review/expiry, custodians, notification/confidentiality, conflict precedence, release, and audit without silently retaining unrelated data.

**RM-AUDIT-RETENTION-0003:** Hold and erasure evaluation produces per-object/field decision evidence and residuals. Neither “immutable” nor “privacy” is an automatic universal priority; qualified policy decides exact conflicts.

**RM-AUDIT-RETENTION-0004:** Cryptographic erasure declares compartment/key scope, shared-data consequences, proof/signature verification survival, backup behavior, residual ciphertext/metadata, and inability to recover.

**RM-AUDIT-RETENTION-0005:** Expiry, hold release, deletion, key destruction, object lock expiry, index/cache purge, backup expiry, and physical reclamation are distinct milestones reconciled across replicas/providers.

**RM-AUDIT-RETENTION-0006:** Disposition creates an evidence record and frontier without preserving prohibited content. Restore/reindex/import applies active holds, suppressions, tombstones, and expired-retention policy before exposure.
