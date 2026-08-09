# Secret-protection assertion and benchmark traceability

**Status:** Draft promotion-unit mapping  
**Authority:** [`rm.security.secret-store`](secret-store.md)  
**Promotion unit:** `rm.promotion.security.secrets`

| Assertion | Covered normative source | Requirements | Verification intention |
|---|---|---|---|
| `rm.assertion.security.secret.selection@1` | `secret-store.md`, `secret-protection-model.md` | SECRET-0001–0002, 0015 | Mutate every protection dimension independently; unknown/unavailable values fail requirements, and assurance/hardware/deletion claims retain exact scope. |
| `rm.assertion.security.secret.identity-mutation@1` | `secret-store.md` | SECRET-0003–0004, 0008 | Verify provider-scoped identity, collision safety, explicit replace authority, generations/conflicts, and no identifier-as-authority inference. |
| `rm.assertion.security.secret.exposure@1` | `secret-store.md`, `secret-value.md` | SECRET-0005, 0010–0011 | Verify opaque/scoped/owned modes, enumeration/metadata authority, non-clone/display/serialize defaults, and value/derived-fingerprint exclusion from sinks. |
| `rm.assertion.security.secret.interaction@1` | `secret-store.md` | SECRET-0006–0007, 0013–0014 | Verify discovery and operation interaction states, safe sync/async paths, UI-thread prohibition, cancellation/completion/indeterminate outcomes, and sanitized errors. |
| `rm.assertion.security.secret.lifecycle@1` | `secret-store.md` | SECRET-0009, 0012 | Exercise lock/logout/account/password/migration/backup/restore/sync/sandbox/headless states and report exact logical, replica, garbage-collection, and erasure effects. |
| `rm.assertion.security.secret.dependencies@1` | `secret-dependencies.md` | DEPENDENCY-0001–0005 | Verify authority, cancellation, UI interaction, profile, provider, filesystem, and consumer relationships without hidden fallback or inferred edges. |
| `rm.assertion.security.secret.quality@1` | `secret-cross-cutting-review.md` | QUALITY-0001–0004 | Verify six quality dimensions, exposure boundaries, nonclaims, evidence methods, and specialist obligations. |
| `rm.assertion.security.secret.sources@1` | `secret-source-review.md` | SOURCE-0001–0004 | Bind exact authoritative sources, provider/configuration frontier, invalidation, and documented-versus-observed separation. |
| `rm.assertion.security.secret.ownership@1` | `secret-ownership.md` | OWNER-0001–0004 | Verify accountable roles, bounded disposable trial, provider/lifecycle matrix, stop conditions, and complete closeout. |
| `rm.assertion.security.secret.readiness-boundary@1` | `secret-readiness-review.md`, `secret-traceability.md` | READINESS-0001–0003, TRACE-0001–0003 | Verify unit dossier reviewability without implying provider selection, protection strength, implementation, or release readiness. |

## Benchmark scenario mapping

| Scenario | Benchmark requirements | Legacy workloads | Comparison contract |
|---|---|---|---|
| `rm.benchmark.security.secret.lifecycle@1` | `RM-SECURITY-SECRET-BENCH-0001`, `RM-SECURITY-SECRET-BENCH-0004`, `RM-SECURITY-SECRET-BENCH-0005` | SEC-BENCH-006, 019 | Same provider/item class, claim vector, item size, interaction/session state, generation policy, operation milestones, and cleanup. |
| `rm.benchmark.security.secret.scale@1` | `RM-SECURITY-SECRET-BENCH-0002`, `RM-SECURITY-SECRET-BENCH-0004`, `RM-SECURITY-SECRET-BENCH-0005` | SEC-BENCH-007 | Same item population, lookup/enumeration authority, metadata policy, concurrency, provider limits, and terminal outcomes. |
| `rm.benchmark.security.secret.exposure@1` | `RM-SECURITY-SECRET-BENCH-0003`, `RM-SECURITY-SECRET-BENCH-0004`, `RM-SECURITY-SECRET-BENCH-0005` | SEC-BENCH-008, 020 | Same named operation and opaque/scoped/owned boundary, copies, provider transitions, interaction, and secret-canary policy. |
| `rm.benchmark.security.secret.interaction@1` | `RM-SECURITY-SECRET-BENCH-0001`, `RM-SECURITY-SECRET-BENCH-0004`, `RM-SECURITY-SECRET-BENCH-0005` | SEC-BENCH-021 | Same prompt/session policy, human time separation, cancellation schedule, completion/indeterminate oracle, and recovery. |
| `rm.benchmark.security.secret.failure@1` | `RM-SECURITY-SECRET-BENCH-0001`, `RM-SECURITY-SECRET-BENCH-0004`, `RM-SECURITY-SECRET-BENCH-0005` | SEC-BENCH-022 | Same boundary-specific fault, partial provider state, public outcome, generation/visibility reconciliation, and secret-free diagnostics. |

**RM-SECURITY-SECRET-TRACE-0001:** Every secret-protection requirement MUST map to a stable assertion and executable case or review method before unit promotion.

**RM-SECURITY-SECRET-TRACE-0002:** Windows, Linux, and macOS evidence MUST preserve assertion identity while reporting exact provider, store, item class, account/session, sandbox, interaction, replication, and lifecycle scope separately.

**RM-SECURITY-SECRET-TRACE-0003:** Discovery, selection, plaintext submission, provider acceptance, logical visibility, exposure/use, replace/delete acceptance, replica/backup effects, garbage collection, and evidenced erasure MUST remain distinct milestones.
