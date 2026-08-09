# Async I/O assertion traceability

**Status:** Draft assertion mapping  
**Authority:** [Async I/O foundations](README.md)

| Assertion | Covered normative source files | Verification intention |
|---|---|---|
| `rm.assertion.async-io.operation@1` | `operation-model.md` | Verify generation-scoped identity, exactly-once terminalization, complete result/progress, immediate/deferred equivalence, and drop policy. |
| `rm.assertion.async-io.engine@1` | `readiness-completion.md` | Verify completion-oriented contracts, readiness translation, drain/rearm, stale/duplicate/coalesced tolerance, would-block retry, ordering nonclaims, and bounded adaptation. |
| `rm.assertion.async-io.cancellation@1` | `cancellation-lifetime.md` | Verify cancel/complete arbitration, retained buffers/control state, timeout distinctions, close policy, side-effect disclosure, and ABA defense. |
| `rm.assertion.async-io.registration@1` | `registration-resources.md` | Verify resource/engine generations, concurrent ordering, descriptor reuse defense, fork/transfer/restart invalidation, and safe deregistration. |
| `rm.assertion.async-io.load@1` | `backpressure-fairness.md` | Verify hard bounds, typed saturation, bounded work batches, scoped fairness/nonclaims, QoS ordering, and bounded telemetry. |
| `rm.assertion.async-io.runtime@1` | `runtime-integration.md` | Verify executor independence, wake semantics, bounded callbacks, shutdown/drain, sync completeness, and thread/run-loop/fork constraints. |
| `rm.assertion.async-io.observability@1` | `errors-observability.md` | Verify submission/terminal failure distinction, invalid completion quarantine, causal redacted traces, bounded metrics, recursion safety, and timing boundaries. |
| `rm.assertion.async-io.dependencies@1` | `dependencies.md` | Verify integration relationships, injected dependencies, provider-owned domain semantics, and graph noninference. |
| `rm.assertion.async-io.quality-review@1` | `cross-cutting.md` | Verify six-dimension applicability, exact evidence methods, provider qualification, and findings. |
| `rm.assertion.async-io.source-review@1` | `source-review.md` | Verify source authority/status, mechanism/version frontier, mutable/archive handling, and invalidation. |
| `rm.assertion.async-io.ownership@1` | `ownership.md` | Verify accountable roles, engine/consumer matrix, bounded trial nonclaims, stop conditions, cleanup, and evidence retention. |
| `rm.assertion.async-io.promotion-boundary@1` | `promotion-review.md`, `traceability.md` | Verify mapping invariants and separation of eligibility, framework maturity, provider maturity, implementation authority, and observed evidence. |

## Benchmark scenario mapping

| Scenario | Benchmark requirements | Legacy workload | Comparison contract |
|---|---|---|---|
| `rm.benchmark.async-io.submit-complete@1` | `RM-ASYNC-BENCH-0001`, `RM-ASYNC-BENCH-0007`, `RM-ASYNC-BENCH-0008` | Submission/completion | Same operation/resource semantics, mode/mix, submit/issue/dequeue/wake/resume boundaries, progress, and terminal oracle. |
| `rm.benchmark.async-io.scale@1` | `RM-ASYNC-BENCH-0002`, `RM-ASYNC-BENCH-0007`, `RM-ASYNC-BENCH-0008` | Throughput scaling | Same mix, depths/bounds, resources/producers/workers, batches, buffers, and correctness/resource gates. |
| `rm.benchmark.async-io.readiness-translation@1` | `RM-ASYNC-BENCH-0003`, `RM-ASYNC-BENCH-0007`, `RM-ASYNC-BENCH-0008` | Readiness translation | Same readiness mode, drain/rearm, syscall budget, stale/would-block schedule, hot-resource distribution, and completion oracle. |
| `rm.benchmark.async-io.cancellation@1` | `RM-ASYNC-BENCH-0004`, `RM-ASYNC-BENCH-0007`, `RM-ASYNC-BENCH-0008` | Cancellation | Same operation phase, native issue, progress/side effects, request/ack/terminal boundaries, and lifetime accounting. |
| `rm.benchmark.async-io.saturation-fairness@1` | `RM-ASYNC-BENCH-0005`, `RM-ASYNC-BENCH-0007`, `RM-ASYNC-BENCH-0008`, `RM-ASYNC-BENCH-0009` | Saturation | Same limits, rejection/recovery, fairness scope, priorities/distribution, worker/memory bounds, and tail oracle. |
| `rm.benchmark.async-io.registration-churn@1` | `RM-ASYNC-BENCH-0006`, `RM-ASYNC-BENCH-0007`, `RM-ASYNC-BENCH-0008` | Registration | Same generation/reuse schedule, registration mutation, late-event injection, native resources, and reclamation oracle. |
| `rm.benchmark.async-io.idle-power@1` | `RM-ASYNC-BENCH-0002`, `RM-ASYNC-BENCH-0007`, `RM-ASYNC-BENCH-0008` | Idle/power | Same idle resources, polling strategy, latency target, power policy, wake/time basis, and observation interval. |
| `rm.benchmark.async-io.shutdown@1` | `RM-ASYNC-BENCH-0006`, `RM-ASYNC-BENCH-0007`, `RM-ASYNC-BENCH-0008` | Shutdown | Same mixed operations, stop-admission point, cancel/drain policy, stalled fallback, late-event schedule, and survivor/cleanup oracle. |

**RM-ASYNC-TRACE-0001:** Every async I/O foundation requirement MUST map to a stable semantic assertion and executable model/case or review method before Experimental promotion.

**RM-ASYNC-TRACE-0002:** IOCP/overlapped, io_uring, epoll, kqueue/dispatch, and blocking-adapter cases MUST preserve assertion identity while reporting exact operation/resource/mechanism/version scope separately.

**RM-ASYNC-TRACE-0003:** Submission acceptance, native issue, readiness, syscall progress, native completion, engine dequeue, cancellation acknowledgement, wake, consumer resume, and domain effect MUST remain separate oracles.

**RM-ASYNC-TRACE-0004:** Legacy benchmark labels remain suite-local and MUST map to stable semantic scenario identities before comparison or promotion use.
