# Windowing benchmark specification

**Status:** Draft

## Workloads

| ID | Workload | Measures |
|---|---|---|
| WIN-BENCH-001 | Cold/warm create-to-first-committed-snapshot | p50/p95/p99 latency, allocations, native calls |
| WIN-BENCH-002 | Request-to-observed resize under interactive drag | event latency, coalescing ratio, queue depth, CPU |
| WIN-BENCH-003 | Mixed-scale display traversal | snapshot latency, surface generations, coordinate drift |
| WIN-BENCH-004 | Display hot-plug/mode storm | topology convergence, lost revisions, allocation peak |
| WIN-BENCH-005 | Create/show/hide/destroy churn | throughput, handle/resource high-water mark, cleanup tail |
| WIN-BENCH-006 | Surface invalidation and reacquisition | interruption duration, stale-present rejection cost |

Each benchmark records OS/build, compositor/session, display topology, scale/orientation, hardware, power mode, provider version, contract version, native baseline, warm-up, sample count, and distribution. Native baseline and Rusty Mill path must provide equivalent guarantees. No fixed release budget is accepted until representative providers establish baselines.

