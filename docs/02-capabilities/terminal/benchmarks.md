# Terminal foundation benchmark specification

**Status:** Draft

| ID | Measurement | Required reporting |
|---|---|---|
| TERM-BENCH-001 | PTY create/close | Wire profile, size, handles/descriptors, allocations, p50/p95/p99, native baseline |
| TERM-BENCH-002 | Session spawn-to-attachment/image/ready | Each milestone latency and setup mechanism |
| TERM-BENCH-003 | Bidirectional throughput/latency | Input/output transfer sizes, concurrent progress, CPU, copies, context switches |
| TERM-BENCH-004 | Resize processing | Resize rate, provider acceptance latency, notification/application-observation where measurable |
| TERM-BENCH-005 | Protocol translation | Wire profile, corpus, bytes/code points/sequences, throughput, allocation, malformed-input cost |
| TERM-BENCH-006 | Concurrent sessions | Session/process count, pending I/O, worker threads, memory, handles/descriptors, wakeups |
| TERM-BENCH-007 | Shutdown and output drain | Stop policy, buffered output, child/descendant count, p95/p99 terminal completion |

ConPTY measurements report synchronous transport threads/queues separately. POSIX measurements report readiness registration and termios mode. Protocol/emulator benchmarks do not mix glyph rendering or accessibility-tree update cost into raw session overhead; higher-layer benchmarks measure those explicitly.

