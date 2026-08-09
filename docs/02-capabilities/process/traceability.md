# Process assertion traceability

**Status:** Draft assertion mapping  
**Authority:** [Process foundations](README.md)

| Assertion | Covered normative source files | Verification intention |
|---|---|---|
| `rm.assertion.process.spawn@1` | `spawn.md` | Verify explicit direct launch, native arguments/environment, allowlisted inheritance, startup milestones, owned-child identity, wait/status, cancellation, sync/async completeness, cleanup, and redaction. |
| `rm.assertion.process.control@1` | `control.md` | Verify owned-object targeting, discoverable action mapping, dispatch/terminal separation, action non-degradation, exit races, idempotency, cancellation, and sanitized evidence. |
| `rm.assertion.process.executable-resolve@1` | `executable-resolve.md` | Verify explicit roots/order, component and suffix policy, filesystem R-level, eligibility/identity evidence, caching, authority preservation, and disclosure. |
| `rm.assertion.process.supervision@1` | `supervision.md` | Verify P0–P3 containment, pre-release membership, escape disclosure, dynamic group control/completion, phased shutdown, accounting, close, and degradation behavior. |
| `rm.assertion.process.pipeline@1` | `pipeline.md` | Verify resolved acyclic construction, endpoint ownership, partial-failure reconciliation, drainage/backpressure, failure/cancellation policy, status aggregation, and cleanup. |
| `rm.assertion.process.dependencies@1` | `dependencies.md` | Verify exact required/optional edges, service composition, direction, profile resolution, and non-inference. |
| `rm.assertion.process.quality-review@1` | `cross-cutting.md` | Verify six-dimension applicability, exact evidence methods, provider qualification, and findings. |
| `rm.assertion.process.source-review@1` | `source-review.md` | Verify platform-contract authority/status, exact provider generations, mutable/archive handling, and invalidation. |
| `rm.assertion.process.ownership@1` | `ownership.md` | Verify accountable roles, provider matrix, trial nonclaims, stop conditions, cleanup, and evidence retention. |
| `rm.assertion.process.promotion-boundary@1` | `promotion-review.md`, `traceability.md` | Verify mapping invariants and separation of eligibility, maturity, implementation authority, provider choice, and observed evidence. |

## Benchmark scenario mapping

| Scenario | Benchmark requirements | Legacy workloads | Comparison contract |
|---|---|---|---|
| `rm.benchmark.process.spawn-lifecycle@1` | `RM-PROCESS-BENCH-0001`, `RM-PROCESS-BENCH-0003`, `RM-PROCESS-BENCH-0007`, `RM-PROCESS-BENCH-0008` | PROC-BENCH-001–003, 006–007 | Same manifest, milestone, child work/duration, concurrency, wait/cancel/reap oracle, and leak accounting. |
| `rm.benchmark.process.manifest-construction@1` | `RM-PROCESS-BENCH-0002`, `RM-PROCESS-BENCH-0007`, `RM-PROCESS-BENCH-0008` | PROC-BENCH-004–005 | Same native values, validation/redaction, entry and allowlist sizes, serialization, contention, and ownership transfer. |
| `rm.benchmark.process.control@1` | `RM-PROCESS-BENCH-0003`, `RM-PROCESS-BENCH-0007`, `RM-PROCESS-BENCH-0008` | PROC-BENCH-008 | Same owned target, action, race schedule, dispatch and terminal boundaries, cancellation, and result oracle. |
| `rm.benchmark.process.supervision@1` | `RM-PROCESS-BENCH-0004`, `RM-PROCESS-BENCH-0007`, `RM-PROCESS-BENCH-0008` | PROC-BENCH-009 | Same P-level, membership/churn, shutdown phases, accounting scope, and empty-set observation. |
| `rm.benchmark.process.executable-resolution@1` | `RM-PROCESS-BENCH-0005`, `RM-PROCESS-BENCH-0007`, `RM-PROCESS-BENCH-0008` | PROC-BENCH-010 | Same roots/authority/order, policy, R-level, identity checks, cache state, candidate fixture, and disclosure. |
| `rm.benchmark.process.pipeline-construction@1` | `RM-PROCESS-BENCH-0006`, `RM-PROCESS-BENCH-0007`, `RM-PROCESS-BENCH-0008` | PROC-BENCH-011 | Same graph, endpoint set, release order, failure points, child readiness, and full reconciliation oracle. |
| `rm.benchmark.process.pipeline-flow@1` | `RM-PROCESS-BENCH-0006`, `RM-PROCESS-BENCH-0007`, `RM-PROCESS-BENCH-0008`, `RM-PROCESS-BENCH-0009` | PROC-BENCH-012–013 | Same topology, bytes, slow stage, backpressure/capture, failure/cancel/escalation policy, and drain/result oracle. |

**RM-PROCESS-TRACE-0001:** Every process capability or service requirement MUST map to a stable semantic assertion and executable case or review method before Experimental promotion.

**RM-PROCESS-TRACE-0002:** Windows, Linux, and macOS adapters MUST preserve semantic assertion identity while reporting launch primitive, parser convention, identity/wait mechanism, containment facility, and exact environment separately.

**RM-PROCESS-TRACE-0003:** Preparation, native creation, image confirmation, readiness, control dispatch, terminal observation, reaping, contained-set empty, and pipeline reconciliation MUST remain separate oracles.

**RM-PROCESS-TRACE-0004:** Legacy `PROC-*` case and workload identities remain suite-local and MUST map to stable semantic identities before comparison or promotion use.
