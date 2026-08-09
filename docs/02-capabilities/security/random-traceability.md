# Secure-random assertion and benchmark traceability

**Status:** Draft capability mapping  
**Authority:** [`rm.security.random`](random.md)

| Assertion | Covered normative source | Requirements | Verification intention |
|---|---|---|---|
| `rm.assertion.security.random.exact-fill@1` | `random.md` | RANDOM-0001–0005 | Verify zero/boundary/large requests, checked conversion/chunking, entire-region initialization, atomic public success/failure, and no predictable fallback. |
| `rm.assertion.security.random.readiness@1` | `random.md` | RANDOM-0006–0008 | Verify fail-closed initialization, genuine sync path, cancellable non-worker-blocking readiness where applicable, and no hidden runtime. |
| `rm.assertion.security.random.secrecy@1` | `random.md` | RANDOM-0009/0011 | Verify output/intermediate/caller memory exclusion from every diagnostic sink and sanitized failure evidence without substitute bytes. |
| `rm.assertion.security.random.lifecycle@1` | `random.md` | RANDOM-0010 | Verify declared fork, VM/container clone/snapshot, suspend/resume, and reinitialization behavior within supported environments. |
| `rm.assertion.security.random.claims@1` | `random.md` | RANDOM-0012 | Verify certification/validation claims bind exact provider/module boundary, configuration, platform, and evidence or remain absent. |
| `rm.assertion.security.random.dependencies@1` | `random-dependencies.md` | DEPENDENCY-0001–0004 | Verify optional cancellation/readiness composition, profile satisfaction, consumer direction, and prohibited inference. |
| `rm.assertion.security.random.quality@1` | `random-cross-cutting-review.md` | QUALITY-0001–0003 | Verify six quality dimensions, evidence methods, nonclaims, and specialist boundaries. |
| `rm.assertion.security.random.sources@1` | `random-source-review.md` | SOURCE-0001–0004 | Verify exact authoritative sources, provider/configuration frontier, expiry/invalidation, and documented-versus-observed separation. |
| `rm.assertion.security.random.ownership@1` | `random-ownership.md` | OWNER-0001–0004 | Verify accountable roles, bounded trial, lifecycle matrix, stop conditions, disposal, and nonauthorization. |
| `rm.assertion.security.random.readiness-boundary@1` | `random-readiness-review.md`, `random-traceability.md` | READINESS-0001–0003, TRACE-0001–0003 | Verify capability-dossier completeness without implying security-domain maturity, implementation authority, or statistical certification. |

## Benchmark scenario mapping

| Scenario | Benchmark requirements | Legacy workloads | Comparison contract |
|---|---|---|---|
| `rm.benchmark.security.random.fill@1` | `RM-SECURITY-RANDOM-BENCH-0001`, `RM-SECURITY-RANDOM-BENCH-0004`, `RM-SECURITY-RANDOM-BENCH-0005` | SEC-BENCH-001, 003–004 | Same OS source/configuration, readiness, sizes/chunking, exact-fill semantics, memory policy, concurrency, build, and no output-derived artifacts. |
| `rm.benchmark.security.random.first-use@1` | `RM-SECURITY-RANDOM-BENCH-0002`, `RM-SECURITY-RANDOM-BENCH-0004`, `RM-SECURITY-RANDOM-BENCH-0005` | SEC-BENCH-002 | Same cold provider/source state, construction/readiness/fill boundaries, cancellation policy, environment lifecycle, and no asymmetric prewarming. |
| `rm.benchmark.security.random.failure@1` | `RM-SECURITY-RANDOM-BENCH-0003`, `RM-SECURITY-RANDOM-BENCH-0004`, `RM-SECURITY-RANDOM-BENCH-0005` | SEC-BENCH-005 | Same controlled fault, partial native state, public failure boundary, unusable-output oracle, fallback prohibition, and sanitized diagnostics. |

**RM-SECURITY-RANDOM-TRACE-0001:** Every secure-random requirement MUST map to a stable assertion and executable case/review method before capability promotion.

**RM-SECURITY-RANDOM-TRACE-0002:** Windows, Linux, and macOS adapters MUST preserve assertion identity while reporting exact provider/module/configuration/platform/lifecycle scope separately.

**RM-SECURITY-RANDOM-TRACE-0003:** Provider readiness, fill completion, public success, caller use, lifecycle reinitialization, statistical observation, and certification claims MUST remain separate evidence boundaries.
