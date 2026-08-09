# IPC byte-pipe assertion traceability

**Status:** Draft assertion mapping  
**Authority:** [IPC foundations](README.md)

| Assertion | Covered normative source files | Verification intention |
|---|---|---|
| `rm.assertion.ipc.byte-pipe@1` | `byte-pipe.md` | Verify directional authority, atomic creation, inheritance defaults, partial progress, EOF/broken peer, bounded backpressure, atomic-write scope, duplication, sync/async paths, cancellation, concurrency, errors, and content privacy. |
| `rm.assertion.ipc.dependencies@1` | `dependencies.md` | Verify optional cancellation, process consumer direction, profile Q-level resolution, and capability/service/data-flow separation. |
| `rm.assertion.ipc.quality-review@1` | `cross-cutting.md` | Verify six-dimension applicability, exact evidence methods, provider qualification, and findings. |
| `rm.assertion.ipc.source-review@1` | `source-review.md` | Verify source authority/status, exact provider generations, mutable/archive handling, and invalidation. |
| `rm.assertion.ipc.ownership@1` | `ownership.md` | Verify accountable roles, provider matrix, bounded trial nonclaims, stop conditions, cleanup, and evidence retention. |
| `rm.assertion.ipc.promotion-boundary@1` | `promotion-review.md`, `traceability.md` | Verify mapping invariants and separation of eligibility, maturity, implementation authority, provider choice, and observed evidence. |

## Benchmark scenario mapping

| Scenario | Benchmark requirements | Legacy workloads | Comparison contract |
|---|---|---|---|
| `rm.benchmark.ipc.pipe-create-close@1` | `RM-IPC-BENCH-0001`, `RM-IPC-BENCH-0007`, `RM-IPC-BENCH-0008` | IPC-BENCH-001 | Same direction, flags, requested capacity, ownership, failure injection, close order, and endpoint inventory. |
| `rm.benchmark.ipc.pipe-transfer@1` | `RM-IPC-BENCH-0002`, `RM-IPC-BENCH-0007`, `RM-IPC-BENCH-0008` | IPC-BENCH-002–003 | Same payload, requests, schedules, blocking/backpressure state, partial progress, and sync/Q-level boundary. |
| `rm.benchmark.ipc.pipe-concurrent-writers@1` | `RM-IPC-BENCH-0003`, `RM-IPC-BENCH-0007`, `RM-IPC-BENCH-0008` | IPC-BENCH-004 | Same writers, tagged records, request sizes, atomicity scope, scheduling, and byte-accurate oracle. |
| `rm.benchmark.ipc.pipe-async-scale@1` | `RM-IPC-BENCH-0004`, `RM-IPC-BENCH-0007`, `RM-IPC-BENCH-0008`, `RM-IPC-BENCH-0009` | IPC-BENCH-005 | Same Q-level, pending operations/endpoints, buffers, cancellation points, worker budget, saturation, and terminal-result mix. |
| `rm.benchmark.ipc.pipe-process-redirection@1` | `RM-IPC-BENCH-0005`, `RM-IPC-BENCH-0007`, `RM-IPC-BENCH-0008` | IPC-BENCH-006 | Same child probe, spawn manifest, endpoint allowlist, close schedule, payload, EOF, and leak oracle. |
| `rm.benchmark.ipc.pipe-terminal-paths@1` | `RM-IPC-BENCH-0006`, `RM-IPC-BENCH-0007`, `RM-IPC-BENCH-0008` | IPC-BENCH-007 | Same reference topology, buffered state, peer-close schedule, native signal containment, detection, and cleanup boundary. |

**RM-IPC-TRACE-0001:** Every IPC byte-pipe requirement MUST map to a stable semantic assertion and executable case or review method before Experimental promotion.

**RM-IPC-TRACE-0002:** Windows, Linux, and macOS adapters MUST preserve semantic assertion identity while reporting native mechanism, flags, Q-level, capacity/atomicity scope, runtime integration, and process context separately.

**RM-IPC-TRACE-0003:** Write acceptance, read progress, would-block/pending, confirmed cancellation, broken peer, EOF, endpoint close, and inherited-reference reconciliation MUST remain separate oracles.

**RM-IPC-TRACE-0004:** Legacy `IPC-PIPE-*` and `IPC-BENCH-*` identities remain suite-local and MUST map to stable semantic identities before comparison or promotion use.
