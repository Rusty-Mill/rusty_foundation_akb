# Anonymous byte-pipe benchmark specification

**Status:** Draft

## Normative comparison requirements

- **RM-IPC-BENCH-0001:** Creation/close comparisons **MUST** bind identical direction, inheritance/transfer defaults, blocking mode, buffer request, security attributes, and endpoint-lifecycle oracle.
- **RM-IPC-BENCH-0002:** Transfer comparisons **MUST** bind identical byte counts, request sizes, producer/consumer schedules, capacity/backpressure state, cache/warmup policy, and partial-progress oracle.
- **RM-IPC-BENCH-0003:** Concurrent-writer comparisons **MUST** bind writer count, record/request sizes, claimed atomic-write scope, scheduling method, and byte-accurate interleaving oracle.
- **RM-IPC-BENCH-0004:** Async comparisons **MUST** bind Q-level, pending operation/endpoint count, buffer lifetime, readiness/completion boundary, cancellation schedule, bounded-worker policy, and saturation state.
- **RM-IPC-BENCH-0005:** Process-redirection comparisons **MUST** bind the same spawn manifest, inherited endpoint allowlist, duplicate-close schedule, child payload, EOF oracle, and leak inventory.
- **RM-IPC-BENCH-0006:** Broken-peer/EOF comparisons **MUST** bind the same reference topology, buffered-byte state, close schedule, signal/exception containment, terminal observation, and cleanup boundary.
- **RM-IPC-BENCH-0007:** Every run **MUST** record provider artifact, OS/kernel/SDK, hardware/virtualization, native mechanism/flags, Q-level, capacity/atomicity claims, runtime integration, samples/statistics, and conformance result.
- **RM-IPC-BENCH-0008:** A baseline with broader inheritance, unbounded buffering, weaker EOF/broken-peer semantics, content capture, busy spinning, or a hidden unbounded blocking pool **MUST NOT** be treated as equivalent.
- **RM-IPC-BENCH-0009:** Numeric budgets and native-performance claims **MUST** derive from reviewed representative runs and **MUST NOT** be inferred from planned scenarios or observed native capacity alone.

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
