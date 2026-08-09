# Cryptography and key-management promotion-unit readiness review

| Field | Value |
|---|---|
| Status | Proposed unit dossier; no maturity change |
| Subject | `rm.promotion.security.cryptography` |
| Architecture | Model 1.94.0 |
| Proposed decision | Unit planning evidence is reviewable; the unit and security directory remain Draft |
| Implementation authority | None |

| Gate | State | Evidence | Qualification |
|---|---|---|---|
| Contract semantics | Pass | [foundations](crypto-README.md), [policy](crypto-policy.md), [keys](crypto-keys.md), [operations](crypto-operations.md), operation-family and transfer/provider specifications, [ADR-0081](../../adr/0081-cryptographic-policy-precedes-provider-selection.md) | public API, algorithms/suites, encodings/formats, providers/libraries, and product protocol policies remain unselected |
| Unit boundary | Pass | [promotion registry](promotion-units.md), [composition](crypto-dependencies.md), [ADR-0163](../../adr/0163-maturity-promotion-units-follow-evidence-boundaries-not-directory-layout.md) | operation families retain distinct contracts/evidence but share policy/key/provider ownership, compatibility, trial, and release boundary; PKI/issuance remain separate units |
| Dependencies/profiles | Pass | [composition](crypto-dependencies.md), [server profile](../profiles/foundation-server.md), [windowed desktop profile](../profiles/foundation-windowed-desktop.md), [partial graph](../../04-ecosystem/consistency-readiness/dependency-graph.md) | exact conditional relationships are classified; no universal crypto capability node/runtime/provider/protocol edge is invented |
| Platform/source review | Pass | [platform research](crypto-platform-research.md), [source review](crypto-source-review.md) | exact standards, providers/modules/libraries, platform generations, hardware/firmware, modes, validation, and leakage evidence are trial inputs |
| Cross-cutting planning | Pass | [quality review](crypto-cross-cutting-review.md) | no qualified cryptographic review, implementation/provider result, side-channel conclusion, certification, or production operations evidence exists |
| Assertions/cases | Pass | [traceability](crypto-traceability.md), [conformance](crypto-conformance.md) | vectors/corpora and cases are specified but not selected, licensed, pinned, or executed |
| Benchmark scenarios | Pass | [scenario mapping](crypto-traceability.md#benchmark-scenario-mapping), [benchmarks](crypto-benchmarks.md) | no baseline run, numeric budget, native-performance, leakage, energy, or sustained-quality conclusion exists |
| Ownership/trial bounds | Qualified | [ownership](crypto-ownership.md), [trial governance](../../05-governance/implementation-trials/README.md) | roles exist; named qualified people, independent review, authorization, disposable provider environments, artifacts, and closeout do not |

The unit is coherent because policy, keys, operation families, provider evidence, lifecycle, compatibility, and release must be reviewed together. Coherence does not permit generic operations: each algorithm family retains exact typed semantics, assertions, vectors, and benchmarks. The dossier cannot approve an algorithm, provider, module, library, hardware device, remote service, certification mode, or cryptographic composition.

**RM-CRYPTO-READINESS-0001:** Dossier presence or planned evidence MUST NOT be represented as cryptographic correctness/security, algorithm/provider approval, constant-time behavior, hardware confinement, non-export, zeroization, attestation, certification/compliance, native performance, implementation, or release evidence.

**RM-CRYPTO-READINESS-0002:** A named review MUST bind exact workload/policy and standard revisions, algorithms/parameters/encodings, provider/module/library artifact, platform/hardware/firmware/configuration/mode, key lifecycle/protection/export, interaction, transition, exclusions, findings/waivers, qualified accountable people, and decision date.

**RM-CRYPTO-READINESS-0003:** Unit promotion MUST require executed published/independent/adversarial evidence, cross-provider interoperability, lifecycle/fault/concurrency tests, exposure/oracle/leakage review, policy/provider transition, staged/sustained benchmarks, and truthfully scoped hardware/attestation/certification nonclaims.
