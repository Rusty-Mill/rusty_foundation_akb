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
| TERM-BENCH-008 | Incremental parser/emulator | Dialect corpus, chunk distribution, bytes/sequences/cells per second, allocations, peak bounded state |
| TERM-BENCH-009 | State delta/checkpoint | Dirty-cell/line ratio, revision rate, serialization size/time, consumer fanout |
| TERM-BENCH-010 | Input/IME encoding | Event class, mode revision contention, p50/p95/p99, allocation, queue/backpressure |
| TERM-BENCH-011 | Accessibility updates | Mutation/announcement rate, coalescing delay, history size, platform adapter CPU/memory |
| TERM-BENCH-012 | Recording/replay | Data classes, encryption/integrity, event rate, storage throughput, compression, replay speed/divergence cost |
| TERM-BENCH-013 | Terminal frame | Grid/viewport size, dirty ratio, glyph/style mix, p50/p95/p99 build-to-present, CPU/GPU, allocations/uploads |
| TERM-BENCH-014 | Text shaping/fallback | Script/emoji corpus, cache state, cells/clusters per second, fallback misses, memory |
| TERM-BENCH-015 | Resize/scale/device recovery | Event rate, full/delta redraw cost, frames dropped, peak resources, time to correct frame |
| TERM-BENCH-016 | Accessibility + render fanout | Revision rate, independent consumer lag, retained snapshots, coalescing, end-to-end update latency |

ConPTY measurements report synchronous transport threads/queues separately. POSIX measurements report readiness registration and termios mode. Protocol/emulator benchmarks do not mix glyph rendering or accessibility-tree update cost into raw session overhead; higher-layer benchmarks measure those explicitly.

Renderer benchmarks pin font files, shaping/rasterizer versions, driver/device, display scale/color space, surface format, frame policy, and user preferences. Full-redraw and exact native text/graphics baselines use identical logical state and capture protections.
