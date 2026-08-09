# Process foundation benchmark specification

**Status:** Draft

## Normative comparison requirements

- **RM-PROCESS-BENCH-0001:** Spawn comparisons **MUST** bind the same executable artifact/identity policy, argument convention, environment, working directory, inheritance allowlist, standard-stream bindings, startup milestone, and child work.
- **RM-PROCESS-BENCH-0002:** Construction comparisons **MUST** use equivalent native values, validation, redaction, entry/resource counts, serialization rules, and ownership-transfer boundaries.
- **RM-PROCESS-BENCH-0003:** Wait and control comparisons **MUST** separate dispatch, native notification, terminal observation, reaping, and close milestones and preserve equivalent cancellation semantics.
- **RM-PROCESS-BENCH-0004:** Supervision comparisons **MUST** bind the same P-level, membership/breakaway/orphan policy, member churn, shutdown phases, accounting scope, and terminal-set oracle.
- **RM-PROCESS-BENCH-0005:** Executable-resolution comparisons **MUST** bind root order/authority, suffix/case policy, R-level, candidate identity policy, filesystem/cache state, and rejection disclosure.
- **RM-PROCESS-BENCH-0006:** Pipeline comparisons **MUST** bind the same graph, endpoint ownership, release order, backpressure/capture limits, supervision, failure propagation, cancellation, and aggregate-status policy.
- **RM-PROCESS-BENCH-0007:** Every run **MUST** record provider artifact, OS/kernel/SDK, hardware/virtualization, security/service/sandbox context, filesystem/cache state, parser convention, toolchain, warmup, samples, statistics, and correctness results.
- **RM-PROCESS-BENCH-0008:** A shell wrapper, ambient search, broad inheritance, PID-only control, weaker containment, unbounded capture, or hidden blocking worker **MUST NOT** serve as an equivalent faster baseline.
- **RM-PROCESS-BENCH-0009:** Numeric budgets and native-performance claims **MUST** derive from reviewed representative runs and **MUST NOT** be inferred from planned scenarios or structural budgets.

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
| PROC-BENCH-011 | Pipeline construction | Node/edge count, preparation/release latency, allocations, endpoint peak, native shell-free baseline |
| PROC-BENCH-012 | Pipeline throughput/backpressure | Topology, transfer size, slowest stage, capture policy, CPU/copies/context switches |
| PROC-BENCH-013 | Pipeline failure/cancellation | Failure position, stop/escalation policy, reconciliation and full-drain latency |

## Controls

Pin executable probe identity and artifact digest. Record OS/kernel, hardware, virtualization, security software, power policy, filesystem/cache state, toolchain/build, provider, parser convention, sample count, warmup, and confidence interval. Separate cold image/file-cache effects from abstraction overhead. Never use a shell wrapper in the native baseline.

Regression budgets remain evidence-derived. Security validation and allowlist construction remain enabled in compared paths; a faster broad-inheritance or ambiguous-executable path is not a valid baseline.
