# Performance and resource engineering

**RM-DEV-PERF-0001:** Performance requirements define boundary, workload, correctness, resource metrics, environment, native/equivalent baseline, objective/budget, and statistical method before optimization.

**RM-DEV-PERF-0002:** Optimize measured bottlenecks after contract correctness. Complexity, allocation/copy reduction, batching, caching, vectorization, concurrency, native specialization, and unsafe code each retain semantic and resource proofs.

**RM-DEV-PERF-0003:** Benchmarks use stable semantic scenario identities and immutable runs. They publish raw samples/distributions, warmup, repetitions, uncertainty, outlier policy, noise, hardware/OS/toolchain/provider/configuration, and artifact provenance.

**RM-DEV-PERF-0004:** Native and abstraction paths use equivalent validation, authority, security, durability, cancellation, completion, and observability semantics. A weaker path is reported separately, not declared faster.

**RM-DEV-PERF-0005:** Measure latency distributions, throughput/goodput, CPU, allocations/copies, memory/high-water, handles, storage/network amplification, startup, binary size, wakeups/context switches, and energy/thermal effects where material.

**RM-DEV-PERF-0006:** Load tests include steady state, cold start, saturation, fairness, small/large mixes, failure/recovery, backlog drain, and sustained leak/resource growth.

**RM-DEV-PERF-0007:** Regression budgets are versioned and owned. Budget changes preserve prior conclusions and require rationale; noisy or incomparable evidence yields unknown, not pass.

**RM-DEV-PERF-0008:** Debug assertions and observability needed for correctness/security remain available under governed production policy; optimization cannot silently remove evidence required by the contract.
