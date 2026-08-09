# Secure-random capability readiness review

| Field | Value |
|---|---|
| Status | Proposed capability dossier; no maturity change |
| Subject | `rm.security.random` 0.1.0 |
| Architecture | Model 1.89.0 |
| Proposed decision | Capability evidence is ready for named review; security domain remains incomplete and Draft |
| Implementation authority | None |

| Gate | State | Evidence | Qualification |
|---|---|---|---|
| Contract semantics | Pass | [random contract](random.md), [ADR-0161](../../adr/0161-random-output-tests-do-not-certify-unpredictability.md) | key/nonce/salt/token/password/DRBG semantics remain consumer contracts |
| Dependencies/profiles | Pass | [composition](random-dependencies.md), [CLI](../profiles/foundation-cli.md), [headless](../profiles/foundation-headless.md), [graph](../../04-ecosystem/consistency-readiness/dependency-graph.md) | exact providers/module boundaries/configurations remain unselected |
| Platform/source review | Pass | [platform research](platform-research.md), [source review](random-source-review.md) | exact generations, lifecycle support, validation mode, and fault mechanisms are trial inputs |
| Cross-cutting planning | Pass | [quality review](random-cross-cutting-review.md) | no specialist signoff or implementation/provider result exists |
| Assertions/cases | Pass | [traceability](random-traceability.md), [conformance](conformance.md#rmsecurityrandom-assertions) | cases are specified but not executed |
| Benchmark scenarios | Pass | [scenario mapping](random-traceability.md#benchmark-scenario-mapping), [benchmarks](benchmarks.md) | no baseline run, budget, performance, or security conclusion exists |
| Ownership/trial bounds | Qualified | [ownership](random-ownership.md), [trial governance](../../05-governance/implementation-trials/README.md) | roles exist; named people, independent review, artifacts, and disposable lifecycle environments are absent |

The generated domain scorecard correctly remains unknown because `security/` contains additional authority, secrets, cryptography, PKI, and issuance specifications without complete domain-wide mapping/reviews. This dossier cannot promote the security domain or authorize code.

**RM-SECURITY-RANDOM-READINESS-0001:** Capability-level evidence MUST NOT be aggregated into domain maturity until every in-scope security specification satisfies the domain gates or is explicitly partitioned by an accepted governance decision.

**RM-SECURITY-RANDOM-READINESS-0002:** A named review MUST bind exact provider/module/configuration/platform/lifecycle scope, exclusions, findings/waivers, accountable people, and decision date.

**RM-SECURITY-RANDOM-READINESS-0003:** Planned evidence MUST NOT be represented as passing unpredictability, cryptographic validation, clone safety, native-performance, implementation, or release evidence.
