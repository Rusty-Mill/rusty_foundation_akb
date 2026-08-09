# Application synchronization Experimental promotion review

| Field | Value |
|---|---|
| Status | Proposed; no maturity change |
| Subject | Application synchronization domain 0.1.1; portable contract generation 0.1.x |
| Architecture | Model 1.81.0 |
| Proposed decision | Eligible for explicit Experimental promotion review; remain Draft pending disposition |
| Implementation authority | None |

## Gate assessment

| Gate | State | Exact evidence | Qualification |
|---|---|---|---|
| Contract semantics | Pass | [domain model and contracts](README.md#documents), ADR-0138, ADR-0139 | Product dataset, topology, merge policy, and authority remain explicit inputs |
| Dependencies/profile impact | Pass | [composition register](dependencies.md) | Domain composition is explicit; stable capability-node extraction remains CR-002 work |
| Platform/provider research | Pass | [research](platform-research.md), [freshness review](source-review.md) | No shared native OS sync facility and no provider is selected |
| Cross-cutting planning | Pass | [quality review](cross-cutting.md) | Implementation and specialist product evidence do not yet exist |
| Assertions/cases | Pass | [traceability](traceability.md), [conformance](conformance.md) | Deterministic histories are specified, not executed |
| Benchmark scenarios | Pass | [scenario mapping](traceability.md#benchmark-scenarios), [benchmarks](benchmarks.md) | No baseline, budget, run, cost, energy, or convergence result exists |
| Ownership/trial bounds | Qualified | [ownership](ownership.md), [trial governance](../../05-governance/implementation-trials/README.md) | Accountable roles exist; named people and independent signoffs are absent |

## Decision boundary

The generated scorecard may report planning eligibility. Application synchronization remains Draft until an accepted record binds named accountable people, reviewer independence, exact promoted scope/generation, dependency/profile resolution frontier, findings/waivers, decision date, and permitted trial constraints. A repository standards profile and a separately accepted trial record would still be required before code.

**RM-APP-SYNC-PROMOTION-0001:** Eligibility evidence MUST NOT change maturity, select a provider, or authorize implementation without an explicit accepted promotion decision.

**RM-APP-SYNC-PROMOTION-0002:** Promotion MUST bind exact convergence, authority, topology, history, selection, deletion, schema/merge-policy, attachment, platform, and profile claims; unspecified dimensions remain unsupported or unknown.

**RM-APP-SYNC-PROMOTION-0003:** A promotion decision MUST NOT convert planned histories or benchmark scenarios into passing provider, performance, cost, energy, security, or recovery evidence.

