# Benchmarks

**RM-CACHE-BENCH-0001:** Benchmarks publish hardware/OS/provider/region, topology, configuration, dataset/key/value distributions, working set, privacy partitions, concurrency, clocks, origin latency/cost, warmup, repetitions, and uncertainty.

**RM-CACHE-BENCH-0002:** Local tiers measure hit/miss/insert/validation latency distributions, throughput, memory/disk amplification, serialization/compression, startup/recovery, eviction, and energy under cold, warm, churn, and pressure phases.

**RM-CACHE-BENCH-0003:** Distributed tiers measure network bytes, tail latency, shard rebalance, replication/failover, hot keys, collapse effectiveness, origin amplification, staleness, and cost during partitions and recovery.

**RM-CACHE-BENCH-0004:** Edge trials measure cold/warm regional latency, byte and request offload, fill/shield behavior, transformation/range cost, invalidation and configuration propagation distributions, failover, and origin recovery load.

**RM-CACHE-BENCH-0005:** Stampede trials use synchronized expiry, invalidation, cold start, and origin slowdown with bounded/unbounded baselines; report admitted, queued, collapsed, rejected, stale-served, origin, and failed requests.

**RM-CACHE-BENCH-0006:** Negative and low-popularity workloads disclose pollution, false reuse, eviction fairness, tenant isolation, and attacker-shaped key distributions.

**RM-CACHE-BENCH-0007:** Results separate latency, availability, freshness, correctness, resource use, and monetary cost; faster results with forbidden reuse, cross-tenant leakage, or hidden staleness are failures.
