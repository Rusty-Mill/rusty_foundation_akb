# Activation and association benchmarks

| Benchmark | Measures | Required parameters |
|---|---|---|
| ACTIVATE-BENCH-001 | Handler/default query latency | target kind/type/role, handler count, cache, scope/provider |
| ACTIVATE-BENCH-002 | Intent validation/resolution | target count, URI/path complexity, policy, valid/rejected |
| ACTIVATE-BENCH-003 | Submit-to-broker acceptance | file/URI/app/reveal, default/ask/exact, cold/warm broker |
| ACTIVATE-BENCH-004 | Accepted-to-receipt/readiness | new/existing instance, package type, startup state, target count |
| ACTIVATE-BENCH-005 | Instance redirection and queue | concurrent requests, payload size, dedup policy, startup load |
| ACTIVATE-BENCH-006 | Association-change convergence | handler count, install/update/remove, event gap, full rescan |

Record p50/p95/p99/max, allocations/peak memory, IPC/context switches, bytes/targets, cache hit/miss, chooser/user time separately, broker/app process state, startup/readiness stages, duplicate/unknown outcomes, and idle observation overhead. Benchmarks never automate or measure a user's decision speed as platform performance.

Compare identical native mechanism, handler/application state, association policy, authority, target, interaction mode, and evidence boundary. Direct process spawn, shell execution, bypassed chooser, prewarmed handler, dropped validation, or weaker authority is not an equivalent baseline. Sustained tests cover handler changes, duplicate storms, broker/app crashes, cancellation, session switch, and prove bounded queues/resources with no target/payload leakage.
