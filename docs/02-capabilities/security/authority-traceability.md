# Authority assertion and benchmark traceability

**Status:** Draft promotion-unit mapping  
**Promotion unit:** `rm.promotion.security.authority`

| Assertion | Covered normative source | Requirements | Verification intention |
|---|---|---|---|
| `rm.assertion.security.authority.types@1` | `authority-model.md` | AUTHORITY-0001–0004 | Verify typed identity/claim/context/authority/grant/constraint/result boundaries, namespace-safe comparison, and absence of inferred authority. |
| `rm.assertion.security.authority.descriptor@1` | `authority-model.md` | AUTHORITY-0003/0007/0009 | Verify complete versioned descriptors, opaque native authority, disclosure controls, and serialization prohibition. |
| `rm.assertion.security.authority.ambient-enforcement@1` | `authority-model.md`, ADR-0010 | AUTHORITY-0005/0010 | Verify explicit authority consumption, profiled ambient inputs, operation-time native enforcement, races, and separate milestones. |
| `rm.assertion.security.authority.lifecycle@1` | `authority-model.md` | AUTHORITY-0006/0008 | Verify monotonic derivation/duplication/delegation and separate close/expiry/revoke/alias/in-flight/effect evidence. |
| `rm.assertion.security.authority.policy@1` | `policy-model.md` | POLICY-0001–0008 | Verify complete provenance/freshness, four results, intersection, fail-closed unknowns, cache invalidation, race boundary, explanations, and audit. |
| `rm.assertion.security.authority.delegation@1` | `delegation-model.md` | DELEGATION-0001–0010 | Verify envelope nonauthority, four transfer modes, derive/send default, audience/channel/replay/depth, commit recovery, revocation, inventory, and redaction. |
| `rm.assertion.security.authority.attenuation@1` | `attenuation.md`, `attenuation-traceability.md` | ATTENUATE-0001–0010 | Consume the existing attenuation evidence without promoting its A0–A3 vector into a scalar or unit-wide result. |
| `rm.assertion.security.authority.conformance@1` | `conformance.md` | SEC-AUTH-001–008 | Execute adversarial expansion, comparison, policy, race, disclosure, transfer, and enforcement-vector cases. |
| `rm.assertion.security.authority.dependencies@1` | `authority-dependencies.md` | DEPENDENCY-0001–0005 | Verify ownership and relationship classes across identity, resource domains, policy, native enforcement, transfer, restricted execution, and audit. |
| `rm.assertion.security.authority.quality@1` | `authority-cross-cutting-review.md` | QUALITY-0001–0004 | Verify six quality dimensions, disclosure boundaries, non-grant interaction/telemetry, and qualified performance/availability claims. |
| `rm.assertion.security.authority.sources@1` | `authority-source-review.md` | SOURCE-0001–0005 | Verify authoritative sources, version/deployment frontier, evidence classes, invalidation, and exact provider nonclaims. |
| `rm.assertion.security.authority.ownership@1` | `authority-ownership.md` | OWNER-0001–0004 | Verify roles, matrix, disposable trial, stop conditions, reconciliation, closeout, and nonauthorization. |
| `rm.assertion.security.authority.readiness-boundary@1` | `authority-readiness-review.md`, `authority-traceability.md` | READINESS-0001–0003, TRACE-0001–0003 | Verify complete unit planning evidence without maturity, native equivalence, universal revocation, implementation, or release claims. |

## Benchmark scenario mapping

| Scenario | Benchmark requirements | Legacy workloads | Comparison contract |
|---|---|---|---|
| `rm.benchmark.security.authority.policy-enforcement@1` | `RM-SECURITY-AUTHORITY-BENCH-0001`, `0002`, `0005` | SEC-BENCH-009 | Same policy/evidence/authority/request, evaluation/cache, native enforcement, operation race/effect, audit, and reconciliation boundaries. |
| `rm.benchmark.security.authority.derive-inspect@1` | `RM-SECURITY-AUTHORITY-BENCH-0005`; all `RM-SECURITY-ATTENUATE-BENCH-*` | SEC-BENCH-009–011 | Same multidimensional parent/child, claim vector, provenance/disclosure, native context, concurrency, close, failure, and subset/bypass oracle. |
| `rm.benchmark.security.authority.delegate-transfer@1` | `RM-SECURITY-AUTHORITY-BENCH-0003`, `0005` | SEC-BENCH-012 | Same mode, authority constraints/depth, audience/channel/replay bounds, transaction/failure schedule, ownership inventory, redaction, and cleanup. |
| `rm.benchmark.security.authority.expire-revoke@1` | `RM-SECURITY-AUTHORITY-BENCH-0004`, `0005` | SEC-BENCH-013 | Same generation/alias/partition topology, clocks, in-flight phases/effects, mechanism, propagation/observation, residuals, and reconciliation. |

**RM-SECURITY-AUTHORITY-TRACE-0001:** Every authority, policy, delegation, and consumed attenuation requirement MUST map to a stable assertion and executable case/review method before unit promotion.

**RM-SECURITY-AUTHORITY-TRACE-0002:** Windows, Linux, and macOS adapters MUST preserve stable assertion identity while reporting exact authority/resource kind, provider mechanisms, identity/security context, policy/evidence generations, deployment, aliases, ambient inputs, inheritance, bypasses, and revocation limits.

**RM-SECURITY-AUTHORITY-TRACE-0003:** Identity evidence, authority possession, policy evaluation, native enforcement, operation progress/effect, attenuation, transfer preparation/acceptance/commit, close, expiry, revocation request/observation, audit publication, and reconciliation MUST remain separate evidence boundaries.
