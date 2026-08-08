# Clipboard and drag-and-drop benchmark specification

**Status:** Draft

| ID | Workload | Measures |
|---|---|---|
| TRANSFER-BENCH-001 | Enumerate 1–1000 items/representations | p50/p95/p99, allocations, cross-process calls, side effects (must be zero) |
| TRANSFER-BENCH-002 | Lazy text/binary transfer from 1 KiB–10 GiB | first-byte/completion latency, throughput, copies, memory, cancellation |
| TRANSFER-BENCH-003 | Conversion and sanitization | latency/throughput, expansion ratio, peak memory, quality/loss evidence |
| TRANSFER-BENCH-004 | Drag hover at high pointer rate/many targets | update latency, UI-thread time, queries, frames missed, materializations (zero) |
| TRANSFER-BENCH-005 | Drop/import/commit copy and move | accept-to-first-byte/commit/result, rollback, source cleanup |
| TRANSFER-BENCH-006 | 1–10k promised files and directories | metadata/stream/publish throughput, peak handles/memory, partial recovery |
| TRANSFER-BENCH-007 | Source/target failure and cancellation | detection, cleanup tail, temporary artifacts, leaked resources |

Results bind OS/session/backend, source/target process model, format/type/converter versions, item/byte counts, storage/network context, sandbox/AV/DLP policy, cache state, sample method, and native baseline with equivalent lazy/streaming and security guarantees. Correct bytes, generations, operation outcomes, cleanup, and UI responsiveness are gates before speed claims.

