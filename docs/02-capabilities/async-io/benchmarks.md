# Asynchronous I/O benchmark specification

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
