# Graphics and presentation benchmark specification

**Status:** Draft

| ID | Workload | Measures |
|---|---|---|
| GRAPH-BENCH-001 | Device/session cold and warm creation | p50/p95/p99 latency, cache state, allocations, driver work |
| GRAPH-BENCH-002 | Small UI/terminal damage versus full redraw | CPU/GPU time, bandwidth, power, present latency |
| GRAPH-BENCH-003 | Sustained frame pacing at fixed/variable refresh | frame-time distribution, queue depth, drops, stutter, power |
| GRAPH-BENCH-004 | Acquire under saturation/occlusion | wait distribution, CPU wakeups, memory high-water, recovery latency |
| GRAPH-BENCH-005 | Resize/scale/color and surface recreation storm | interruption, allocations, old-generation retirement, peak memory |
| GRAPH-BENCH-006 | Device loss and provider recovery | detection, teardown, re-resolution, first correct frame, leaked resources |
| GRAPH-BENCH-007 | Resource upload/map/readback | throughput, latency, copies, coherency cost, budget behavior |
| GRAPH-BENCH-008 | Submission/synchronization microbenchmarks | abstraction overhead, queue concurrency, wait/wakeup cost |

Each result records exact workload contract, provider/API/driver, adapter, OS, compositor, display mode/scale/color/refresh, power/thermal state, resource formats/sizes, cache state, validation state, sample method, and native baseline with equivalent guarantees. Visual correctness and loss recovery conformance are prerequisites to performance claims.

