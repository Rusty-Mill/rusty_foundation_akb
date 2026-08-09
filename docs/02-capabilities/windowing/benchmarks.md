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

## Benchmark requirements

**RM-WINDOWING-BENCH-0001:** Creation measurement MUST separate descriptor validation, native creation, initial configuration, first committed snapshot, surface availability, and first presentation; only equivalent milestones may be compared.

**RM-WINDOWING-BENCH-0002:** Resize measurement MUST preserve request-versus-observation semantics and report input/event time basis, coalesced revision intervals, queue depth, committed-snapshot latency, surface churn, and lost/non-coalescible events.

**RM-WINDOWING-BENCH-0003:** Mixed-scale traversal MUST cover fractional scale, rotation, negative/unknown origins, display association, logical/pixel extents, transform revision, and drift-free round trips.

**RM-WINDOWING-BENCH-0004:** Topology-storm measurement MUST report enumeration/subscription races, convergence time, gap/resnapshot behavior, allocation peak, and correct mirror/virtual/remote/headless semantics.

**RM-WINDOWING-BENCH-0005:** Lifecycle churn MUST verify idempotent destruction, terminal event closure, native-handle/resource release, callback detachment, and high-water recovery before throughput results are valid.

**RM-WINDOWING-BENCH-0006:** Surface-generation measurement MUST preserve invalidation ordering, reject stale presentation, distinguish window-side readiness from displayed frames, and report reacquisition interruption and resource cost.

**RM-WINDOWING-BENCH-0007:** Every run MUST bind immutable scenario/run identities, source/build, exact OS/compositor/session/provider, display topology, scale/orientation/color state, hardware/power, native baseline semantics, samples/statistics, correctness cases, exclusions, and artifacts.

Each benchmark records OS/build, compositor/session, display topology, scale/orientation, hardware, power mode, provider version, contract version, native baseline, warm-up, sample count, and distribution. Native baseline and Rusty Mill path must provide equivalent guarantees. No fixed release budget is accepted until representative providers establish baselines.
