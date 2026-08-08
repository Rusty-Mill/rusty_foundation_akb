# Credential and identity-session benchmarks

Benchmarks measure abstraction cost and lifecycle bounds without turning security ceremonies into throughput contests.

| Benchmark | Measures | Required parameters |
|---|---|---|
| ID-BENCH-001 | Warm/cold current-context snapshot latency | attribute set, group/claim count, cache state, provider |
| ID-BENCH-002 | Principal enumeration and expansion | realm size, page size, requested attributes, local/remote provider |
| ID-BENCH-003 | Session change convergence | source count, event gap/coalescing, provider restart, reconciliation size |
| ID-BENCH-004 | Credential-handle operation overhead | handle class, broker boundary, interaction prohibited, success/denial |
| ID-BENCH-005 | Delegated-operation overhead | context entry/revert, operation class, nesting policy, worker isolation |
| ID-BENCH-006 | Authentication lifecycle bounds | provider UI launch/cancel/terminal cleanup only; never secret-entry speed |

Record median, tail percentiles, confidence interval, allocations, handles, context switches, broker IPC, cache state, and failure mix. Compare the same native mechanism and policy; do not compare weaker silent/cached behavior with a fresh interactive ceremony. Sustained tests verify no handle, UI, credential, context, worker-thread, or audit-queue leakage after cancellation, denial, provider restart, panic injection, or owner retirement.
