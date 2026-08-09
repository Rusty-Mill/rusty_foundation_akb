# Benchmarks

**RM-APP-SYNC-BENCH-0001:** Measure local read/write and optimistic projection latency, durable enqueue cost, UI notification delay, and overhead against equivalent local persistence by object/change shape and pending backlog.

**RM-APP-SYNC-BENCH-0002:** Measure initial snapshot, incremental catch-up, steady-state push/pull, reconnect/resume, invalid-checkpoint resnapshot, and convergence time by object count, churn, partitions, RTT/bandwidth/loss, compression, and concurrency.

**RM-APP-SYNC-BENCH-0003:** Measure causal-context compare/merge/growth/compaction and conflict detection/resolution for each selected CRDT/OT/custom policy under realistic concurrency and adversarial histories.

**RM-APP-SYNC-BENCH-0004:** Measure selective-query evaluation, dependency closure, tombstone density, schema migration, attachment chunk/resume/dedup, encryption, authorization, telemetry, and storage amplification.

**RM-APP-SYNC-BENCH-0005:** Sustained tests report backlog bounds, fairness, battery/energy, metered bytes, disk/CPU/memory, thermal behavior, retry storms, quota pressure, recovery, and data correctness.

**RM-APP-SYNC-BENCH-0006:** Reports pin corpus/history digest, schema/policy/topology, provider/protocol/build, replicas/devices/OS, storage/network/fault model, warmup, distributions/confidence, achieved frontiers/convergence, conflicts/loss, and cost. Native baselines use equivalent semantics and evidence.
