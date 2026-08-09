# Restricted-execution promotion-unit readiness review

| Field | Value |
|---|---|
| Status | Proposed unit dossier; no maturity change |
| Subject | `rm.promotion.security.restricted-execution` |
| Architecture | Model 1.92.0 |
| Proposed decision | Unit planning evidence is reviewable; the unit and security directory remain Draft |
| Implementation authority | None |

| Gate | State | Evidence | Qualification |
|---|---|---|---|
| Contract semantics | Pass | [restricted execution](restricted-execution.md), [threat model](threat-model.md) | exact public API, manifest serialization, provider composition, platform generations, and deployment threat model remain unselected |
| Dependencies/profiles | Pass | [composition](restricted-execution-dependencies.md), [process dependencies](../process/dependencies.md), [process supervision](../process/supervision.md), [graph](../../04-ecosystem/consistency-readiness/dependency-graph.md) | relationships are classified; no universal sandbox, runtime, container, or capability edge is inferred |
| Platform/source review | Pass | [platform research](platform-research.md), [source review](restricted-execution-source-review.md) | exact mechanisms/order/configuration/privilege/signing/container and bypass probes are trial inputs |
| Cross-cutting planning | Pass | [quality review](restricted-execution-cross-cutting-review.md) | no specialist signoff, deployment threat model, implementation result, or production operations evidence exists |
| Assertions/cases | Pass | [traceability](restricted-execution-traceability.md), [conformance](conformance.md#restricted-execution-assertions) | cases are specified but not executed |
| Benchmark scenarios | Pass | [scenario mapping](restricted-execution-traceability.md#benchmark-scenario-mapping), [benchmarks](benchmarks.md) | no baseline run, budget, performance, or isolation-strength conclusion exists |
| Ownership/trial bounds | Qualified | [ownership](restricted-execution-ownership.md), [trial governance](../../05-governance/implementation-trials/README.md) | roles exist; named people, independent review, authorization, disposable environments, artifacts, and closeout do not |

The dossier establishes reviewability, not successful isolation. The generated security-domain scorecard remains unknown, and the promotion-unit registry remains Draft. A provider may expose a separately authorized degraded outcome only before release and with exact constraint deltas; it cannot silently fall back after preparation or treat partial isolation as success.

**RM-SECURITY-RESTRICTED-READINESS-0001:** Dossier presence or planned assertions MUST NOT be represented as successful confinement, sandbox strength, native performance, implementation, profile satisfaction, or release evidence.

**RM-SECURITY-RESTRICTED-READINESS-0002:** A named review MUST bind exact manifest/contract version, provider composition, platform/deployment frontier, required and permitted-degraded constraints, exclusions, findings/waivers, accountable people, and decision date.

**RM-SECURITY-RESTRICTED-READINESS-0003:** Unit promotion MUST require executed adversarial evidence that application-controlled code never precedes verification and that every failure/cancellation/supervisor path reconciles children, descendants, authority, and native resources.
