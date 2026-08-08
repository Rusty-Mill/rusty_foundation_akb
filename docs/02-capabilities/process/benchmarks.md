# Process foundation benchmark specification

**Status:** Draft

| ID | Measurement | Required reporting |
|---|---|---|
| PROC-BENCH-001 | Minimal spawn-to-created latency | p50/p95/p99, CPU, allocations, native baseline |
| PROC-BENCH-002 | Spawn-to-image-confirmed and spawn-to-ready latency | Milestone mechanism and child startup work separated |
| PROC-BENCH-003 | Spawn plus wait/reap throughput | Concurrency, child duration, tail latency, handle/descriptor peak |
| PROC-BENCH-004 | Argument/environment construction | Entry/byte counts, validation and serialization costs, allocations/copies |
| PROC-BENCH-005 | Inheritance allowlist scaling | Resource count, concurrent launch contention, native attribute/file-action cost |
| PROC-BENCH-006 | Async wait overhead | Wakeups, context switches, registrations, cancellation race cost |
| PROC-BENCH-007 | Failure paths | Failure milestone, cleanup latency, leaked-resource check |
| PROC-BENCH-008 | Single-child control dispatch | Action class, dispatch/terminal latency separated, native baseline |
| PROC-BENCH-009 | Supervised set lifecycle | Containment level, member count/churn, control and empty-set latency, accounting overhead |
| PROC-BENCH-010 | Executable resolution | Root/candidate count, cache state, resolution quality, identity-policy cost |

## Controls

Pin executable probe identity and artifact digest. Record OS/kernel, hardware, virtualization, security software, power policy, filesystem/cache state, toolchain/build, provider, parser convention, sample count, warmup, and confidence interval. Separate cold image/file-cache effects from abstraction overhead. Never use a shell wrapper in the native baseline.

Regression budgets remain evidence-derived. Security validation and allowlist construction remain enabled in compared paths; a faster broad-inheritance or ambiguous-executable path is not a valid baseline.
