# Benchmarks

**RM-ANALYTICS-BENCH-0001:** Benchmarks publish hardware/OS/provider/version/region, topology, schema/formats/compression, catalog/source snapshots, logical and realized plans, data/query distributions and skew, security/tenant mix, resources, warmup/cache state, repetitions, and uncertainty.

**RM-ANALYTICS-BENCH-0002:** Batch suites measure plan/startup, scan/decode/pruning/pushdown, operators, shuffle/spill, sink, end-to-end latency, throughput, CPU/memory/disk/network/GPU/energy/cost, output correctness, and scale-up/out across cold/warm and failure phases.

**RM-ANALYTICS-BENCH-0003:** Streaming suites measure event/source-to-process/checkpoint/sink/visible latency distributions, sustainable and burst throughput, watermark lag, late/drop/correction, state/checkpoint size/duration, backpressure, recovery, output correctness, and cost.

**RM-ANALYTICS-BENCH-0004:** Join/aggregate/window trials vary cardinality, selectivity, skew, ordering, state horizon, late data, approximation, memory, partitioning, and algorithm while reporting realized decisions and spill/network amplification.

**RM-ANALYTICS-BENCH-0005:** Failure trials interrupt workers/coordinators/networks/source/sink/state/shuffle/checkpoint storage at each milestone and report lost/duplicate/replayed effects, recovery time, backlog catch-up, availability, resource surge, and reconciliation.

**RM-ANALYTICS-BENCH-0006:** Migration/recovery trials measure backfill/live handoff, shadow/dual overhead, savepoint upgrade, rescale, snapshot/source restore, regional failover/failback, RPO/RTO, semantic parity, and old-artifact cleanup.

**RM-ANALYTICS-BENCH-0007:** Results separate exact/approximate correctness, reproducibility class, completeness, freshness, latency, throughput, resource/energy/cost, security, privacy, and accessibility; faster semantically invalid results fail.
