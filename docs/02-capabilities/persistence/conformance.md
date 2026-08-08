# Persistence conformance specification

**RM-PERSISTENCE-CONFORMANCE-0001:** Reports bind engine/service/driver/protocol/OS/filesystem/storage builds, database/schema/topology generations, security, transaction/consistency/durability, workload, limits, clocks, fixtures, fault schedule, and canonical operation/history traces.

**RM-PERSISTENCE-CONFORMANCE-0002:** Data/query tests cover every logical/provider type, null/presence/range/precision/time/collation conversion, keys, parameter binding/injection, predicates/joins/aggregates/order/pagination, partial streaming/cancel, native extensions, plans, limits, and malformed/stored hostile data.

**RM-PERSISTENCE-CONFORMANCE-0003:** Transaction history tests verify each declared isolation model under concurrency; savepoints, constraints, locks/deadlocks, serialization retry, commit timeout/disconnect, cancellation, crash/power/storage faults, durability levels, external-effect nonclaims, and unknown-outcome reconciliation.

**RM-PERSISTENCE-CONFORMANCE-0004:** Session/pool tests cover identity/tenant/role isolation, reset of every state kind, prepared-plan invalidation, credential/schema/topology rotation, cancellation/aborted transactions, leaks, starvation/fairness, saturation, drain, and shutdown.

**RM-PERSISTENCE-CONFORMANCE-0005:** Migration tests cover mixed old/new readers/writers, expand/backfill/validate/contract, concurrent mutations, locks/rewrites/log impact, pause/crash/restart, mismatch repair, replicas/change feeds/caches/backups, rollback boundaries, and destructive-step recovery.

**RM-PERSISTENCE-CONFORMANCE-0006:** Change/integration tests fault snapshot/log/read/encode/publish/settle/consume boundaries, exercise schema/timeline/failover gaps/duplicates/overlap, retention/backpressure, outbox fencing/retry/cleanup, privacy/erasure, and authoritative resnapshot reconciliation.

**RM-PERSISTENCE-CONFORMANCE-0007:** Backup/restore/replication tests cover full/incremental/log chains, corruption/missing/reorder/wrong keys, isolated semantic restore, PITR targets/timelines, clone fencing, RPO/RTO, replica lag/read routing, primary loss/promotion/divergence/rejoin, and multi-primary conflicts.

**RM-PERSISTENCE-CONFORMANCE-0008:** Cross-provider matrices compare canonical typed results, isolation histories, durability/recovery, migration/change, security/privacy/accessibility, and performance evidence across embedded/native/service providers on Windows/Linux/macOS; unsupported semantics stay gaps.

