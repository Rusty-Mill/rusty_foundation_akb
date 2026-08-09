# Runtime/time assertion traceability

**Status:** Draft assertion mapping  
**Authority:** [Runtime/time domain](README.md)

Semantic assertion identities bind portable propositions. Existing `CT-*` and `ST-*` identifiers in the [conformance specification](conformance.md) remain stable executable case identities and map beneath these propositions; they are not renamed or reused ([ADR-0150](../../adr/0150-semantic-assertions-and-executable-cases-have-distinct-identities.md)).

| Assertion | Covered normative source files | Verification intention |
|---|---|---|
| `rm.assertion.runtime-time.clock@1` | `monotonic-clock.md` | Verify clock domains, monotonicity, suspend semantics, comparability, arithmetic, resolution, and concurrency nonclaims. |
| `rm.assertion.runtime-time.deadline@1` | `deadline-timer.md` | Verify compatible deadlines, non-early readiness, async/sync paths, disarm/expiry/cancellation races, tolerance, metadata, and wake authority. |
| `rm.assertion.runtime-time.cancellation@1` | `cancellation.md` | Verify idempotent request, observation, propagation, reentrancy, race linearization, partial effects, and bounded fanout. |
| `rm.assertion.runtime-time.shutdown@1` | `shutdown.md`, `traceability.md` | Verify quiescence, dependency order, deadlines, escalation, aggregation, reentrancy, reports, and assertion/case identity rules. |
| `rm.assertion.runtime-time.quality-review@1` | `cross-cutting.md` | Verify quality applicability, exact evidence methods, retained higher-layer obligations, timing/privacy review, and semantic benchmark gates. |
| `rm.assertion.runtime-time.source-review@1` | `source-review.md` | Verify source identity/status/frontier, change triggers, mutable-source qualification, and separation of documented, observed, and portable claims. |
| `rm.assertion.runtime-time.ownership@1` | `ownership.md` | Verify accountable roles, question closure, bounded non-authorizing trial plan, stop conditions, and disposal duties. |
| `rm.assertion.runtime-time.promotion-boundary@1` | `promotion-review.md` | Verify eligibility/decision separation, named-review requirements, exact subject binding, open-question disposition, narrowing, and nonauthorization. |

## Benchmark scenario mapping

Scenario identities describe comparable semantics; the legacy `BM-*` catalog labels remain reserved suite-local workload identifiers.

| Scenario | Benchmark requirements | Legacy workloads | Comparison contract |
|---|---|---|---|
| `rm.benchmark.runtime-time.active-clock-read@1` | `RM-RUNTIME-BENCH-0001`, `RM-RUNTIME-BENCH-0010` | BM-TIME-MONO-001 | Equivalent active domain, concurrency, allocation, and provider-call boundary. |
| `rm.benchmark.runtime-time.continuous-clock-read@1` | `RM-RUNTIME-BENCH-0002`, `RM-RUNTIME-BENCH-0010` | BM-TIME-MONO-002 | Equivalent suspend-inclusive semantics; unsupported is not zero cost. |
| `rm.benchmark.runtime-time.instant-arithmetic@1` | `RM-RUNTIME-BENCH-0003`, `RM-RUNTIME-BENCH-0010` | BM-TIME-MONO-003 | Checked arithmetic and incompatible-instant failure remain enabled. |
| `rm.benchmark.runtime-time.timer-lifecycle@1` | `RM-RUNTIME-BENCH-0004`, `RM-RUNTIME-BENCH-0010` | BM-TIME-DEADLINE-001 | Equivalent lifecycle and terminal-race guarantees. |
| `rm.benchmark.runtime-time.timer-delivery@1` | `RM-RUNTIME-BENCH-0005`, `RM-RUNTIME-BENCH-0010` | BM-TIME-DEADLINE-002 | Same clock/deadline/tolerance semantics with zero-early correctness gate. |
| `rm.benchmark.runtime-time.timer-scale@1` | `RM-RUNTIME-BENCH-0006`, `RM-RUNTIME-BENCH-0010` | BM-TIME-DEADLINE-003, BM-TIME-DEADLINE-004 | Same timer population, distribution, churn, and expiration window. |
| `rm.benchmark.runtime-time.cancellation-observation@1` | `RM-RUNTIME-BENCH-0007`, `RM-RUNTIME-BENCH-0010` | BM-RUNTIME-CANCEL-001 | Same observer lifecycle and request/cleanup measurement boundary. |
| `rm.benchmark.runtime-time.cancellation-hierarchy@1` | `RM-RUNTIME-BENCH-0008`, `RM-RUNTIME-BENCH-0010` | BM-RUNTIME-CANCEL-002 | Same topology, requester concurrency, stack bound, and failure policy. |
| `rm.benchmark.runtime-time.shutdown-coordination@1` | `RM-RUNTIME-BENCH-0009`, `RM-RUNTIME-BENCH-0010` | BM-RUNTIME-SHUTDOWN-001 | Same valid DAG, component behavior, deadline/escalation policy, and reporting. |

**RM-RUNTIME-TRACE-0001:** Every runtime/time capability or service requirement MUST map to a semantic assertion and one or more executable cases or review methods before Experimental promotion.

**RM-RUNTIME-TRACE-0002:** A case result MUST record both its case identity and every semantic assertion/requirement it exercises; one passing case MUST NOT be generalized beyond its declared platform, provider, environment, and oracle.

**RM-RUNTIME-TRACE-0003:** Existing `CT-*` and `ST-*` identities remain reserved permanently even when superseded.

**RM-RUNTIME-TRACE-0004:** Existing `BM-*` identities remain suite-local labels and MUST map to a stable semantic benchmark scenario before results can support comparison or promotion.
