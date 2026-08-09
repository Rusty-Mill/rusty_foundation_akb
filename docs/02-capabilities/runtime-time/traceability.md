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

**RM-RUNTIME-TRACE-0001:** Every runtime/time capability or service requirement MUST map to a semantic assertion and one or more executable cases or review methods before Experimental promotion.

**RM-RUNTIME-TRACE-0002:** A case result MUST record both its case identity and every semantic assertion/requirement it exercises; one passing case MUST NOT be generalized beyond its declared platform, provider, environment, and oracle.

**RM-RUNTIME-TRACE-0003:** Existing `CT-*` and `ST-*` identities remain reserved permanently even when superseded.
