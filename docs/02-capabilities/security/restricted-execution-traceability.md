# Restricted-execution assertion and benchmark traceability

**Status:** Draft promotion-unit mapping  
**Authority:** [Restricted execution](restricted-execution.md)  
**Promotion unit:** `rm.promotion.security.restricted-execution`

| Assertion | Covered normative source | Requirements | Verification intention |
|---|---|---|---|
| `rm.assertion.security.restricted.plan@1` | `restricted-execution.md` | RESTRICTED-0001–0002 | Resolve the complete immutable manifest and provider evidence; reject required unsupported constraints and distinguish explicitly permitted degraded plans. |
| `rm.assertion.security.restricted.pre-release@1` | `restricted-execution.md` | RESTRICTED-0003–0005 | Prove application-controlled code cannot execute until restrictions are applied and verified, inheritance is allowlisted, and transferred authority is attenuated. |
| `rm.assertion.security.restricted.result@1` | `restricted-execution.md` | RESTRICTED-0006, 0008 | Report exact enforcement/degradation/residual assumptions and distinguish creation, restriction, release, and authenticated readiness. |
| `rm.assertion.security.restricted.reconcile@1` | `restricted-execution.md` | RESTRICTED-0007, 0009 | Reconcile cancellation/failure, children, descendants, prepared authority, resources, supervisor failure, termination, reaping, and close. |
| `rm.assertion.security.restricted.audit@1` | `restricted-execution.md` | RESTRICTED-0010 | Emit bounded policy/evidence identifiers without secrets, credentials, or unrestricted child input. |
| `rm.assertion.security.restricted.dependencies@1` | `restricted-execution-dependencies.md` | DEPENDENCY-0001–0005 | Verify process, authority, filesystem/network, IPC, cancellation, profile, and provider composition without inferred universal dependencies. |
| `rm.assertion.security.restricted.quality@1` | `restricted-execution-cross-cutting-review.md` | QUALITY-0001–0004 | Verify security, performance, accessibility, i18n, observability, and operations methods and nonclaims. |
| `rm.assertion.security.restricted.sources@1` | `restricted-execution-source-review.md` | SOURCE-0001–0004 | Bind authoritative mechanisms, exact platform frontier, source invalidation, and documented-versus-observed boundaries. |
| `rm.assertion.security.restricted.ownership@1` | `restricted-execution-ownership.md` | OWNER-0001–0004 | Verify accountable roles, bounded disposable trial, stop conditions, reconciliation, and nonauthorization. |
| `rm.assertion.security.restricted.readiness-boundary@1` | `restricted-execution-readiness-review.md`, `restricted-execution-traceability.md` | READINESS-0001–0003, TRACE-0001–0003 | Verify unit dossier completeness without implying maturity, implementation, sandbox strength, or release readiness. |

## Benchmark scenario mapping

| Scenario | Benchmark requirements | Legacy workloads | Comparison contract |
|---|---|---|---|
| `rm.benchmark.security.restricted.prepare@1` | `RM-SECURITY-RESTRICTED-BENCH-0001`, `RM-SECURITY-RESTRICTED-BENCH-0004`, `RM-SECURITY-RESTRICTED-BENCH-0005` | SEC-BENCH-014 | Same manifest, authority inputs, provider discovery, validation/attenuation, rejection oracle, platform/configuration, and no child release. |
| `rm.benchmark.security.restricted.launch@1` | `RM-SECURITY-RESTRICTED-BENCH-0002`, `RM-SECURITY-RESTRICTED-BENCH-0004`, `RM-SECURITY-RESTRICTED-BENCH-0005` | SEC-BENCH-015, 018 | Same mechanisms/constraints and separate creation, enforcement, verification, release, readiness, and equivalent-native stages. |
| `rm.benchmark.security.restricted.lifecycle@1` | `RM-SECURITY-RESTRICTED-BENCH-0002`, `RM-SECURITY-RESTRICTED-BENCH-0004`, `RM-SECURITY-RESTRICTED-BENCH-0005` | SEC-BENCH-016 | Same readiness, descendant, supervision, shutdown, reaping, cleanup, and terminal-accounting contract. |
| `rm.benchmark.security.restricted.failure@1` | `RM-SECURITY-RESTRICTED-BENCH-0003`, `RM-SECURITY-RESTRICTED-BENCH-0004`, `RM-SECURITY-RESTRICTED-BENCH-0005` | SEC-BENCH-017 | Same stage-specific fault/cancellation schedule, code-execution oracle, authority transfer, reconciliation, and sanitized evidence. |

**RM-SECURITY-RESTRICTED-TRACE-0001:** Every restricted-execution requirement MUST map to a stable assertion and executable case or review method before unit promotion.

**RM-SECURITY-RESTRICTED-TRACE-0002:** Windows, Linux, and macOS evidence MUST preserve assertion identity while reporting exact native composition, platform generation/configuration, enforcement, degradation, and residual assumptions separately.

**RM-SECURITY-RESTRICTED-TRACE-0003:** Planning, native creation, restriction application, verification, release, readiness, supervision, termination, reaping, and cleanup MUST remain distinct evidence milestones.
