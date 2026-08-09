# Authority-attenuation capability readiness review

| Field | Value |
|---|---|
| Status | Proposed capability dossier; no maturity change |
| Subject | `rm.security.attenuate` 0.1.0 |
| Architecture | Model 1.90.0 |
| Proposed decision | Capability evidence is ready for named review; security domain remains incomplete and Draft |
| Implementation authority | None |

| Gate | State | Evidence | Qualification |
|---|---|---|---|
| Contract semantics | Pass | [attenuation](attenuation.md), [authority model](authority-model.md), [delegation](delegation-model.md), ADR-0009/0011/0162 | native authority kinds, exact comparable dimensions, and provider claim vectors remain trial inputs |
| Dependencies/profiles | Pass | [composition](attenuation-dependencies.md), [restricted execution](restricted-execution.md), [graph](../../04-ecosystem/consistency-readiness/dependency-graph.md) | selection is conditional on consumer need; no universal authority capability or sandbox guarantee is inferred |
| Platform/source review | Pass | [platform research](platform-research.md), [source review](attenuation-source-review.md) | exact native mechanisms, deployment contexts, aliases/bypasses, and revocation semantics are unselected |
| Cross-cutting planning | Pass | [quality review](attenuation-cross-cutting-review.md) | no specialist signoff, native bypass result, restricted-execution result, or implementation evidence exists |
| Assertions/cases | Pass | [traceability](attenuation-traceability.md), [conformance](conformance.md#authority-model-assertions) | cases are specified but not executed |
| Benchmark scenarios | Pass | [scenario mapping](attenuation-traceability.md#benchmark-scenario-mapping), [benchmarks](benchmarks.md) | no baseline run, numeric budget, native-performance, or enforcement conclusion exists |
| Ownership/trial bounds | Qualified | [ownership](attenuation-ownership.md), [trial governance](../../05-governance/implementation-trials/README.md) | roles exist; named people, independent review, mechanisms, and disposable environments are absent |

The generated security-domain scorecard remains unknown because the directory includes random, secrets, cryptography, PKI, issuance, restricted execution, and broader authority/policy specifications. This dossier cannot promote the security domain or authorize code.

**RM-SECURITY-ATTENUATE-READINESS-0001:** Capability evidence MUST NOT be aggregated into domain maturity until all in-scope security specifications satisfy domain gates or accepted governance partitions their promotion units.

**RM-SECURITY-ATTENUATE-READINESS-0002:** A named review MUST bind exact authority kinds, dimensions, providers/mechanisms, deployment contexts, claim vectors/bypasses, lifecycle/transfer/revocation scope, exclusions, findings/waivers, accountable people, and date.

**RM-SECURITY-ATTENUATE-READINESS-0003:** Planned evidence MUST NOT be represented as passing native enforcement, isolation, defense in depth, revocation, restricted execution, native performance, implementation, or release evidence.
