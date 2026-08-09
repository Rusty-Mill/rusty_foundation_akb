# Asynchronous I/O benchmark specification

## Normative comparison requirements

- **RM-ASYNC-BENCH-0001:** Submission/completion comparisons **MUST** bind the same domain operation/resource semantics, provider mode, immediate/deferred mix, measured milestones, progress oracle, and consumer wake/resume policy.
- **RM-ASYNC-BENCH-0002:** Scaling comparisons **MUST** bind operation/resource mix, queue depth/bounds, producer/worker count, batch/poll policy, buffer sizes/alignment, and correctness constraints.
- **RM-ASYNC-BENCH-0003:** Readiness translation comparisons **MUST** bind level/edge/one-shot mode, drain/rearm policy, syscall work budget, stale/would-block schedule, hot-resource distribution, and completion oracle.
- **RM-ASYNC-BENCH-0004:** Cancellation comparisons **MUST** bind operation phase, native issue state, progress side effects, request/acknowledgement/terminal boundaries, provider support, and retained-memory accounting.
- **RM-ASYNC-BENCH-0005:** Saturation/fairness comparisons **MUST** bind hard/configured bounds, rejection policy, recovery reserve, fairness scope, priority classes, tenant/resource distribution, and tail-latency oracle.
- **RM-ASYNC-BENCH-0006:** Registration/shutdown comparisons **MUST** bind resource/engine generations, churn/reuse schedule, late-event injection, stop-admission/cancel/drain policy, survivor classification, and cleanup boundary.
- **RM-ASYNC-BENCH-0007:** Every run **MUST** record provider/executor artifacts, OS/kernel/SDK, hardware/virtualization, operation matrix, engine/queue/poll settings, clocks, storage/network/device/cache/power conditions, samples/statistics, and conformance results.
- **RM-ASYNC-BENCH-0008:** Native completion, readiness translation, and bounded blocking adaptation **MUST** be labeled separately; hidden runtimes, unbounded workers/queues, busy spinning, weaker cancellation, or omitted lifetime checks are non-equivalent baselines.
- **RM-ASYNC-BENCH-0009:** Numeric budgets and native-performance claims **MUST** derive from reviewed representative runs and **MUST NOT** be inferred from architecture, mechanism names, or planned scenarios.

| Benchmark | Measures |
|---|---|
| Submission/completion | per-operation latency distributions from consumer submit through native issue, terminal dequeue, wake, and resume |
| Throughput scaling | operations/bytes per second versus queue depth, resource count, producer count, completion batch, and worker count |
| Readiness translation | syscalls per completion, stale/would-block rates, rearm cost, hot-resource drain behavior |
| Cancellation | request-to-terminal latency and normal/cancelled/failed outcomes by operation phase and provider |
| Saturation | rejection point, bounded memory/threads, recovery latency, fairness and tail latency under overload |
| Registration | register/mutate/deregister cost and descriptor/handle churn |
| Idle/power | idle wakeups, CPU, memory, handles, and latency/power tradeoff by polling strategy |
| Shutdown | stop-admission and drain latency with mixed operations, cancellations, stalled resources, and late events |

Results report p50/p95/p99/p99.9/max, throughput, CPU, allocations, peak retained buffer bytes, syscalls, context switches, wakeups, queue occupancy, rejects, stale events, and cancellation outcomes. Runs disclose hardware, OS/kernel, mitigations, engine/provider and executor versions, operation/resource mix, buffer sizes/alignment, queue/batch/poll settings, cache/network/storage/device conditions, power policy, contention, and raw measurement boundaries.

Comparisons separate native completion, readiness translation, and blocking fallback. A higher-throughput configuration cannot claim superiority if it violates declared memory, cancellation, fairness, tail-latency, or power constraints.
