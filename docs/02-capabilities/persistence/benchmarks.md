# Persistence benchmark specification

**RM-PERSISTENCE-BENCH-0001:** Benchmarks publish hardware, OS/filesystem/storage, engine/service/driver builds, topology, schema/indexes/data distribution, consistency/isolation/durability, security, pool/cache, concurrency, limits, faults, clocks, samples, variance, and raw histories.

**RM-PERSISTENCE-BENCH-0002:** Workloads cover point/range/key/document/relational reads/writes, joins/aggregates/order/pagination, small/large/blob/streaming values, read-only/update transactions, hot/cold plans/caches, contention/skew, constraints/indexes, pools, and mixed tenants.

**RM-PERSISTENCE-BENCH-0003:** Report operation/transaction latency distributions, commit/durable/visible/archive time, throughput/goodput, rows/bytes, plan/execute/lock/queue/pool time, conflicts/retries, CPU, allocations/copies, memory/disk/network, cache hit, write/space amplification, and energy.

**RM-PERSISTENCE-BENCH-0004:** Migration/change workloads measure DDL lock/rewrite/log/replica impact, online index/constraint/backfill throughput, mixed-version latency, change-feed lag/backlog, outbox relay, pause/resume, validation/repair, and recovery while preserving foreground correctness/SLO evidence.

**RM-PERSISTENCE-BENCH-0005:** Backup/recovery/replication workloads measure snapshot/log/archive overhead, backup/verify/restore/PITR rate, compression/encryption, RPO/RTO, replica lag/read staleness, failover/promotion/readiness, backlog catch-up, divergence recovery, and regional/cost trade-offs.

**RM-PERSISTENCE-BENCH-0006:** Fault benchmarks inject crash/power/storage-full/latency/corruption, network partition, primary/replica loss, clock discontinuity, credential/key rotation, schema/topology change, and restore under load with isolation/durability/data-integrity history checks.

**RM-PERSISTENCE-BENCH-0007:** Provider and Rusty Mill paths use identical schema/types, queries, transaction histories, constraints/indexes, durability, security, pool/cache, telemetry, faults, and completion boundaries. Weaker correctness, durability, or recovery cannot be counted as speed.

