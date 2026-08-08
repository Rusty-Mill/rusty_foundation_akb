# Memory and mapping benchmark specification

| Workload | Metrics |
|---|---|
| Reserve/commit | latency, page-table cost, faults, resident/commit accounting |
| Touch/fault | first-touch and steady latency, minor/major faults, bandwidth |
| Protect | transition latency by pages/threads, synchronization cost, TLB/cache effects |
| File mapping | map/unmap, sequential/random read/write, faults, flush stages versus ordinary I/O |
| Shared memory | cross-process throughput/latency, synchronization overhead, transfer setup |
| Lock/discard | latency, quota scaling, refault/reinitialize cost |
| Large pages | setup, TLB-sensitive workload, fragmentation and fallback |
| Allocator | size/alignment matrix, allocation/free/realloc latency, throughput, fragmentation, RSS/commit peak |
| JIT publication | write/protect/cache-sync/commit latency and generation turnover |

Results record hardware/NUMA, OS/build, architecture, page sizes, memory pressure, swap/compression/overcommit, allocator/provider, security mitigations, backing filesystem/storage, access pattern, working-set size, thread/process count, warm/cold state, and statistical variance. Reserved bytes, committed backing, RSS, private/shared dirty pages, and application payload are reported separately where available.

