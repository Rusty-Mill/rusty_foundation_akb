# Replication, consistency, and failover

**RM-PERSISTENCE-REPLICATION-0001:** A replication profile binds provider/protocol, database/timeline/configuration, replica roles/fault domains, synchronous/async/quorum rules, consistency/read routing, durability acknowledgment, lag representation, conflict policy, fencing, and promotion/recovery.

**RM-PERSISTENCE-REPLICATION-0002:** Primary/leader, synchronous/async replica, voter/learner, read replica, witness, cascading source, promoted, demoted, catching-up, diverged, fenced, and removed are distinct roles/states with generation evidence.

**RM-PERSISTENCE-REPLICATION-0003:** Replication sent/received/persisted/replayed/applied/visible/acknowledged/archived states are distinct. Byte/time/transaction lag records measurement point, clock quality, source position, sampling freshness, and unknown/disconnected state.

**RM-PERSISTENCE-REPLICATION-0004:** Read routing declares consistency/staleness/session guarantees, replica eligibility, applied-position prerequisite, transaction/read-only state, failover behavior, topology/latency/cost, and fallback. A healthy replica can still be too stale for an operation.

**RM-PERSISTENCE-FAILOVER-0001:** Automatic/manual failover binds failure evidence, quorum/fencing, candidate identity and replay position, data-loss bound, outstanding/in-doubt transactions, promotion token, DNS/proxy/pool/session invalidation, application reconciliation, and failback policy.

**RM-PERSISTENCE-FAILOVER-0002:** Promotion success is not service readiness. Recovery, consistency checks, fencing, credentials, schema/migration state, change streams/outbox, pools/caches, write acceptance, and domain health are separately proven.

**RM-PERSISTENCE-FAILOVER-0003:** Rejoining an old primary or divergent replica requires fencing, timeline/history comparison, authoritative-source decision, wipe/rewind/restore/catch-up plan, validation, new generation, and staged promotion. Timestamps cannot merge divergent histories safely.

**RM-PERSISTENCE-REPLICATION-0005:** Multi-primary/conflict-capable systems declare per-object consistency, causality/versioning, conflict detection/resolution, uniqueness/constraint behavior, tombstones/GC, partitions, schema evolution, external effects, and irreconcilable states.

