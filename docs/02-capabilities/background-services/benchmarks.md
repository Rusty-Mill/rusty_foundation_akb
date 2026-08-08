# Background services and durable scheduling benchmark specification

| Benchmark | Measures |
|---|---|
| Registration | validate/commit/observe/enable/disable/remove latency and writes under clean, update, and recovery paths |
| Demand activation | request to broker acceptance, process start, initialization, readiness, request acceptance, and first response |
| Scheduled dispatch | target/window to trigger, admission, process start, work claim, checkpoint, and completion; early/late/coalesced/missed distribution |
| Trigger convergence | native event to attempt and authoritative-state reconciliation, including storms, duplicate/loss, broker restart, and suspend/resume |
| Throughput/fairness | attempts/requests per second, queue age/occupancy, overlap, tenant/foreground fairness, rate limiting and saturation recovery |
| Idle/resource | resident and demand-start memory/CPU/wakeups, idle shutdown/restart, socket broker overhead, steady service cost |
| Checkpoint/retry | checkpoint size/latency/durability, crash recovery, dedupe/claim contention, backoff, poison isolation and effect ambiguity |
| Update/recovery | admission switch, drain/coexist/cancel, health gate, rollback, reboot/power-loss reconciliation, complete removal |
| Energy/thermal | wake amplification, CPU/I/O/network energy, maintenance batching, battery/saver/thermal deferral and recovery |

Results report p50/p95/p99/max and distributions for every milestone, schedule early/late/miss/coalesce counts, activation/attempt/restart rates, queue age/occupancy, CPU/memory/I/O/network/wakeups, allocations, checkpoint/result bytes, energy, and thermal state. Runs disclose machine, OS/build/service manager/scheduler, workload kind/scope/principal, definition/package generation, trigger/schedule/time-zone policy, dependencies, budgets, concurrency/retry/update settings, power/network/session state, and raw measurement method. Human approval and administrator interaction are reported separately as UX evidence.
