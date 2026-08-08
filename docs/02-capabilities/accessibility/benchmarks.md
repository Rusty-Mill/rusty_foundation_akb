# Accessibility benchmark specification

**Status:** Draft

| ID | Workload | Measures |
|---|---|---|
| ACCESS-BENCH-001 | Build/diff semantic trees at 100, 10k, 100k nodes | latency, allocations, peak memory, changed-node proportionality |
| ACCESS-BENCH-002 | Native cross-process property/action query | p50/p95/p99, timeouts, UI-thread occupancy, cache hit |
| ACCESS-BENCH-003 | Large text chunk/range/navigation/geometry | throughput, round trips, tail latency, memory |
| ACCESS-BENCH-004 | Update/live-region/terminal-output storm | event rate, coalescing, focus/action latency, queue/memory bound |
| ACCESS-BENCH-005 | Virtualized list/table/tree navigation | realization latency, query count, retained nodes, focus stability |
| ACCESS-BENCH-006 | Adapter disconnect/restart and full resnapshot | downtime, rebuild time, first usable query, leaked native objects |
| ACCESS-BENCH-007 | Input/action-to-semantic-to-present correlation | each milestone latency, AT overhead, visual/semantic convergence |

Benchmarks preserve correctness first: no speed result is valid if focus, action outcome, text range, final semantic snapshot, or required event is lost. Results bind exact semantic workload, OS/native API, assistive technology, adapter/process mode, locale, user preferences, tree/text size, cache state, sample method, and equivalent native baseline.

