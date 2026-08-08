# Anonymous byte-pipe benchmark specification

**Status:** Draft

| ID | Measurement | Required reporting |
|---|---|---|
| IPC-BENCH-001 | Create/close pair | p50/p95/p99, handles/descriptors, allocations, native baseline |
| IPC-BENCH-002 | Throughput by transfer size | 1 B through 1 MiB, CPU, copies, context switches, capacity/backpressure state |
| IPC-BENCH-003 | One-way latency | Warm/cold p50/p95/p99, sync and declared async quality |
| IPC-BENCH-004 | Concurrent writers | Writer count, record size relative to atomicity claim, interleaving, fairness distribution |
| IPC-BENCH-005 | Async scale | Pending operations/endpoints, worker threads, wakeups, memory, cancellation cost |
| IPC-BENCH-006 | Process redirection | Spawn/read-to-EOF latency, inheritance setup, leak/extra-reference check |
| IPC-BENCH-007 | Broken-peer/EOF paths | Detection latency, cleanup, signal/exception containment overhead |

Native baselines use matching direction, blocking mode, buffer configuration, and security/inheritance flags. Q1 blocking-adapter results include worker saturation and queue delay and cannot be compared as though they were native Q2/Q3 async.

